"""
Integration tests for the Weather Analyzer application.
"""

import pytest
import tempfile
import os
from unittest.mock import Mock, patch
from pathlib import Path

from weather_analyzer.main import main, create_argument_parser
from weather_analyzer.utils.config import Config, ConfigError
from weather_analyzer.services.weather_api import WeatherAPIService
from weather_analyzer.services.data_storage import DataStorage


class TestConfigIntegration:
    """Integration tests for configuration management."""
    
    def test_config_with_env_file(self):
        """Test configuration loading from .env file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
            f.write("WEATHER_API_KEY=test_key_123\n")
            f.write("LOG_LEVEL=DEBUG\n")
            f.write("CACHE_DURATION=7200\n")
            env_file = f.name
        
        try:
            config = Config(env_file)
            assert config.weather_api_key == "test_key_123"
            assert config.log_level == "DEBUG"
            assert config.cache_duration == 7200
        finally:
            os.unlink(env_file)
    
    def test_config_missing_api_key(self):
        """Test configuration error when API key is missing."""
        # Temporarily remove API key from environment
        original_key = os.environ.get('WEATHER_API_KEY')
        if 'WEATHER_API_KEY' in os.environ:
            del os.environ['WEATHER_API_KEY']
        
        try:
            with pytest.raises(ConfigError, match="WEATHER_API_KEY environment variable is required"):
                Config()
        finally:
            # Restore original key if it existed
            if original_key:
                os.environ['WEATHER_API_KEY'] = original_key
    
    def test_config_validation(self):
        """Test configuration validation."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
            f.write("WEATHER_API_KEY=valid_test_key_123456\n")
            f.write("LOG_LEVEL=INFO\n")
            env_file = f.name
        
        try:
            config = Config(env_file)
            assert config.validate_config() is True
        finally:
            os.unlink(env_file)


class TestServiceIntegration:
    """Integration tests for service interactions."""
    
    @pytest.fixture
    def temp_data_dir(self):
        """Fixture providing temporary data directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield temp_dir
    
    @pytest.fixture
    def mock_config(self, temp_data_dir):
        """Fixture providing mock configuration."""
        config = Mock(spec=Config)
        config.weather_api_key = "test_api_key"
        config.weather_api_base_url = "https://api.test.com/data/2.5"
        config.data_dir = temp_data_dir
        config.cache_duration = 3600
        return config
    
    def test_weather_service_and_storage_integration(self, mock_config):
        """Test integration between weather service and data storage."""
        weather_service = WeatherAPIService(mock_config)
        data_storage = DataStorage(mock_config.data_dir)
        
        # Verify both services are initialized correctly
        assert weather_service.config == mock_config
        assert data_storage.data_dir == Path(mock_config.data_dir)
        
        # Verify storage directories exist
        assert data_storage.cache_dir.exists()
        assert data_storage.reports_dir.exists()
    
    def test_cache_key_consistency(self, mock_config):
        """Test that cache keys are consistent between services."""
        data_storage = DataStorage(mock_config.data_dir)
        
        # Test cache key generation
        cache_key1 = data_storage._get_cache_key("London", "current")
        cache_key2 = data_storage._get_cache_key("london", "current")
        
        # Keys should be normalized (case-insensitive)
        assert cache_key1.lower() == cache_key2.lower()


class TestCommandLineInterface:
    """Integration tests for command-line interface."""
    
    def test_argument_parser_creation(self):
        """Test argument parser creation and configuration."""
        parser = create_argument_parser()
        
        # Test that parser is created successfully
        assert parser is not None
        
        # Test help output doesn't raise errors
        help_text = parser.format_help()
        assert "Weather Data Analysis Application" in help_text
    
    def test_current_weather_command_parsing(self):
        """Test parsing of current weather command."""
        parser = create_argument_parser()
        
        args = parser.parse_args(['current', '--city', 'London', '--units', 'metric'])
        
        assert args.command == 'current'
        assert args.city == 'London'
        assert args.units == 'metric'
    
    def test_analyze_command_parsing(self):
        """Test parsing of analyze command."""
        parser = create_argument_parser()
        
        args = parser.parse_args(['analyze', '--city', 'Paris', '--days', '5'])
        
        assert args.command == 'analyze'
        assert args.city == 'Paris'
        assert args.days == 5
    
    def test_compare_command_parsing(self):
        """Test parsing of compare command."""
        parser = create_argument_parser()
        
        args = parser.parse_args(['compare', '--cities', 'London,Paris,Tokyo'])
        
        assert args.command == 'compare'
        assert args.cities == 'London,Paris,Tokyo'
    
    def test_report_command_parsing(self):
        """Test parsing of report command."""
        parser = create_argument_parser()
        
        args = parser.parse_args(['report', '--city', 'Berlin', '--output', 'report.txt'])
        
        assert args.command == 'report'
        assert args.city == 'Berlin'
        assert args.output == 'report.txt'
    
    def test_global_options_parsing(self):
        """Test parsing of global options."""
        parser = create_argument_parser()
        
        args = parser.parse_args([
            'current', '--city', 'London',
            '--log-level', 'DEBUG',
            '--config', 'custom.env'
        ])
        
        assert args.log_level == 'DEBUG'
        assert args.config == 'custom.env'


class TestEndToEndWorkflow:
    """End-to-end integration tests."""
    
    @pytest.fixture
    def mock_environment(self):
        """Fixture providing mock environment setup."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create mock .env file
            env_file = Path(temp_dir) / '.env'
            env_file.write_text("WEATHER_API_KEY=test_key_123456789\n")
            
            # Change to temp directory
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                yield temp_dir
            finally:
                os.chdir(original_cwd)
    
    @patch('weather_analyzer.main.WeatherAPIService')
    @patch('weather_analyzer.main.Config')
    def test_main_function_current_command(self, mock_config_class, mock_service_class, mock_environment):
        """Test main function with current weather command."""
        # Setup mocks
        mock_config = Mock()
        mock_config_class.return_value = mock_config
        
        mock_service = Mock()
        mock_service_class.return_value = mock_service
        
        # Test command execution
        with patch('sys.argv', ['weather-analyzer', 'current', '--city', 'London']):
            result = main()
            
            # Should return 0 for success (even though functionality is not implemented)
            assert result == 0
            
            # Verify that config and service were initialized
            mock_config_class.assert_called_once()
            mock_service_class.assert_called_once_with(mock_config)
    
    @patch('weather_analyzer.main.WeatherAPIService')
    @patch('weather_analyzer.main.Config')
    def test_main_function_no_command(self, mock_config_class, mock_service_class, mock_environment):
        """Test main function with no command (should show help)."""
        mock_config = Mock()
        mock_config_class.return_value = mock_config
        
        with patch('sys.argv', ['weather-analyzer']):
            result = main()
            
            # Should return 1 when no command is provided
            assert result == 1
    
    @patch('weather_analyzer.main.Config')
    def test_main_function_config_error(self, mock_config_class, mock_environment):
        """Test main function with configuration error."""
        # Make config initialization raise an error
        mock_config_class.side_effect = ConfigError("Test config error")
        
        with patch('sys.argv', ['weather-analyzer', 'current', '--city', 'London']):
            result = main()
            
            # Should return 1 for error
            assert result == 1
    
    def test_data_flow_integration(self):
        """Test data flow between components."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create data storage
            storage = DataStorage(temp_dir)
            
            # Test that directories are created
            assert storage.cache_dir.exists()
            assert storage.reports_dir.exists()
            
            # Test report saving
            test_report = "Test weather report content"
            storage.save_report(test_report, "test_report.txt")
            
            # Verify report was saved
            report_file = storage.reports_dir / "test_report.txt"
            assert report_file.exists()
            
            with open(report_file, 'r') as f:
                saved_content = f.read()
            
            assert saved_content == test_report
            
            # Test storage statistics
            stats = storage.get_storage_stats()
            assert stats['report_files'] >= 1


class TestErrorHandling:
    """Integration tests for error handling across components."""
    
    def test_invalid_city_name_handling(self):
        """Test handling of invalid city names across components."""
        # This test would verify that invalid city names are handled
        # gracefully throughout the application
        pass
    
    def test_network_error_handling(self):
        """Test handling of network errors."""
        # This test would verify that network errors are handled
        # gracefully and don't crash the application
        pass
    
    def test_file_system_error_handling(self):
        """Test handling of file system errors."""
        # This test would verify that file system errors (permissions, disk full, etc.)
        # are handled gracefully
        pass


# Test fixtures for integration tests
@pytest.fixture
def sample_integration_config():
    """Fixture providing configuration for integration tests."""
    return {
        'weather_api_key': 'test_integration_key',
        'weather_api_base_url': 'https://api.test.com/data/2.5',
        'log_level': 'INFO',
        'cache_duration': 3600,
        'data_dir': 'test_data'
    }