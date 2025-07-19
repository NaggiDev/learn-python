"""
Unit tests for service classes.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import json
import tempfile
import os
from pathlib import Path

from weather_analyzer.services.weather_api import WeatherAPIService, WeatherAPIError, RateLimitError
from weather_analyzer.services.data_storage import DataStorage
from weather_analyzer.utils.config import Config
from weather_analyzer.models.weather_data import WeatherData, WeatherCondition
from datetime import datetime


class TestWeatherAPIService:
    """Test cases for the WeatherAPIService class."""
    
    @pytest.fixture
    def mock_config(self):
        """Fixture providing mock configuration."""
        config = Mock(spec=Config)
        config.weather_api_key = "test_api_key"
        config.weather_api_base_url = "https://api.test.com/data/2.5"
        return config
    
    @pytest.fixture
    def weather_service(self, mock_config):
        """Fixture providing weather API service."""
        return WeatherAPIService(mock_config)
    
    def test_service_initialization(self, mock_config):
        """Test service initialization."""
        service = WeatherAPIService(mock_config)
        assert service.config == mock_config
        assert service.min_request_interval == 1.0
    
    def test_rate_limiting(self, weather_service):
        """Test rate limiting functionality."""
        # First request should not be rate limited
        start_time = weather_service.last_request_time
        weather_service._rate_limit()
        
        # Second immediate request should be rate limited
        with patch('time.sleep') as mock_sleep:
            weather_service._rate_limit()
            # Should have called sleep since requests are too close together
            # (This test may need adjustment based on actual implementation)
    
    @patch('requests.Session.get')
    def test_successful_api_request(self, mock_get, weather_service):
        """Test successful API request."""
        # Mock successful response
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.json.return_value = {'test': 'data'}
        mock_get.return_value = mock_response
        
        result = weather_service._make_request("http://test.com", {'q': 'London'})
        
        assert result == {'test': 'data'}
        mock_get.assert_called_once()
    
    @patch('requests.Session.get')
    def test_api_rate_limit_error(self, mock_get, weather_service):
        """Test API rate limit error handling."""
        mock_response = Mock()
        mock_response.status_code = 429
        mock_get.return_value = mock_response
        
        with pytest.raises(RateLimitError):
            weather_service._make_request("http://test.com", {'q': 'London'})
    
    @patch('requests.Session.get')
    def test_api_unauthorized_error(self, mock_get, weather_service):
        """Test API unauthorized error handling."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response
        
        with pytest.raises(WeatherAPIError, match="Invalid API key"):
            weather_service._make_request("http://test.com", {'q': 'London'})
    
    @patch('requests.Session.get')
    def test_api_not_found_error(self, mock_get, weather_service):
        """Test API not found error handling."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        with pytest.raises(WeatherAPIError, match="Location not found"):
            weather_service._make_request("http://test.com", {'q': 'InvalidCity'})
    
    def test_get_current_weather_not_implemented(self, weather_service):
        """Test that get_current_weather raises NotImplementedError."""
        with pytest.raises(NotImplementedError):
            weather_service.get_current_weather("London")
    
    def test_get_weather_forecast_validation(self, weather_service):
        """Test weather forecast parameter validation."""
        with pytest.raises(ValueError, match="Days must be between 1 and 5"):
            weather_service.get_weather_forecast("London", days=0)
        
        with pytest.raises(ValueError, match="Days must be between 1 and 5"):
            weather_service.get_weather_forecast("London", days=6)
    
    def test_get_historical_weather_validation(self, weather_service):
        """Test historical weather parameter validation."""
        from datetime import datetime, timedelta
        
        start_date = datetime.now()
        end_date = start_date - timedelta(days=1)  # End before start
        
        with pytest.raises(ValueError, match="Start date must be before end date"):
            weather_service.get_historical_weather("London", start_date, end_date)
        
        future_date = datetime.now() + timedelta(days=1)
        with pytest.raises(ValueError, match="End date cannot be in the future"):
            weather_service.get_historical_weather("London", start_date, future_date)
    
    def test_context_manager(self, weather_service):
        """Test context manager functionality."""
        with weather_service as service:
            assert service == weather_service
        
        # Session should be closed after context exit
        # (This would need to be verified by checking session state)


class TestDataStorage:
    """Test cases for the DataStorage class."""
    
    @pytest.fixture
    def temp_data_dir(self):
        """Fixture providing temporary data directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield temp_dir
    
    @pytest.fixture
    def data_storage(self, temp_data_dir):
        """Fixture providing data storage service."""
        return DataStorage(temp_data_dir)
    
    def test_storage_initialization(self, temp_data_dir):
        """Test storage service initialization."""
        storage = DataStorage(temp_data_dir)
        
        assert storage.data_dir == Path(temp_data_dir)
        assert storage.cache_dir == Path(temp_data_dir) / "cache"
        assert storage.reports_dir == Path(temp_data_dir) / "reports"
        
        # Check that directories were created
        assert storage.cache_dir.exists()
        assert storage.reports_dir.exists()
    
    def test_cache_key_generation(self, data_storage):
        """Test cache key generation."""
        cache_key = data_storage._get_cache_key("New York", "current")
        assert isinstance(cache_key, str)
        assert "new_york" in cache_key.lower()
        assert "current" in cache_key.lower()
    
    def test_cache_file_path(self, data_storage):
        """Test cache file path generation."""
        cache_key = "test_key"
        file_path = data_storage._get_cache_file_path(cache_key)
        
        assert file_path.name == "test_key.json"
        assert file_path.parent == data_storage.cache_dir
    
    def test_cache_validation_nonexistent_file(self, data_storage):
        """Test cache validation for non-existent file."""
        is_valid = data_storage.is_cache_valid("nonexistent_key")
        assert is_valid is False
    
    def test_save_report(self, data_storage):
        """Test saving text report."""
        report_content = "Test weather report content"
        filename = "test_report.txt"
        
        data_storage.save_report(report_content, filename)
        
        report_file = data_storage.reports_dir / filename
        assert report_file.exists()
        
        with open(report_file, 'r', encoding='utf-8') as f:
            saved_content = f.read()
        
        assert saved_content == report_content
    
    def test_clear_cache(self, data_storage):
        """Test cache clearing functionality."""
        # Create some test cache files
        test_files = ["test1.json", "test2.json"]
        for filename in test_files:
            cache_file = data_storage.cache_dir / filename
            cache_file.write_text('{"test": "data"}')
        
        # Clear cache
        removed_count = data_storage.clear_cache(older_than_hours=0)
        
        # Should have removed the test files
        assert removed_count == len(test_files)
        
        # Files should no longer exist
        for filename in test_files:
            cache_file = data_storage.cache_dir / filename
            assert not cache_file.exists()
    
    def test_storage_stats(self, data_storage):
        """Test storage statistics."""
        # Create some test files
        cache_file = data_storage.cache_dir / "test.json"
        cache_file.write_text('{"test": "data"}')
        
        report_file = data_storage.reports_dir / "test_report.txt"
        report_file.write_text("Test report")
        
        stats = data_storage.get_storage_stats()
        
        assert isinstance(stats, dict)
        assert 'cache_files' in stats
        assert 'report_files' in stats
        assert stats['cache_files'] >= 1
        assert stats['report_files'] >= 1
    
    def test_csv_operations_not_implemented(self, data_storage):
        """Test that CSV operations are not yet implemented."""
        # These should not raise errors but return empty results
        # since they're placeholder implementations
        
        weather_data = []  # Empty list
        data_storage.save_weather_data_csv(weather_data, "test.csv")
        
        loaded_data = data_storage.load_weather_data_csv("nonexistent.csv")
        assert loaded_data == []


# Test fixtures for common test data
@pytest.fixture
def sample_api_response():
    """Fixture providing sample API response data."""
    return {
        "coord": {"lon": -0.1278, "lat": 51.5074},
        "weather": [{"id": 800, "main": "Clear", "description": "clear sky"}],
        "main": {
            "temp": 20.5,
            "feels_like": 22.0,
            "temp_min": 18.0,
            "temp_max": 23.0,
            "pressure": 1013,
            "humidity": 65
        },
        "wind": {"speed": 3.5, "deg": 180},
        "dt": 1634567890,
        "name": "London",
        "sys": {"country": "GB"}
    }


@pytest.fixture
def sample_weather_data_list():
    """Fixture providing list of sample weather data."""
    return [
        WeatherData(
            city="London", country="UK", latitude=51.5074, longitude=-0.1278,
            timestamp=datetime.now(), timezone_offset=0,
            temperature=20.0, feels_like=22.0, temp_min=18.0, temp_max=25.0,
            pressure=1013.25, humidity=65, wind_speed=3.5,
            condition=WeatherCondition.CLEAR, description="clear sky"
        ),
        WeatherData(
            city="London", country="UK", latitude=51.5074, longitude=-0.1278,
            timestamp=datetime.now(), timezone_offset=0,
            temperature=18.5, feels_like=20.0, temp_min=16.0, temp_max=22.0,
            pressure=1015.0, humidity=70, wind_speed=2.8,
            condition=WeatherCondition.CLOUDS, description="few clouds"
        )
    ]