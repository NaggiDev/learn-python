"""
Unit tests for weather data models.
"""

import pytest
from datetime import datetime
from weather_analyzer.models.weather_data import WeatherData, WeatherCondition
from weather_analyzer.models.location import Location, Coordinates


class TestCoordinates:
    """Test cases for the Coordinates class."""
    
    def test_valid_coordinates(self):
        """Test creation of valid coordinates."""
        coords = Coordinates(40.7128, -74.0060)  # New York City
        assert coords.latitude == 40.7128
        assert coords.longitude == -74.0060
    
    def test_invalid_latitude(self):
        """Test that invalid latitude raises ValueError."""
        with pytest.raises(ValueError):
            Coordinates(91.0, 0.0)  # Latitude > 90
        
        with pytest.raises(ValueError):
            Coordinates(-91.0, 0.0)  # Latitude < -90
    
    def test_invalid_longitude(self):
        """Test that invalid longitude raises ValueError."""
        with pytest.raises(ValueError):
            Coordinates(0.0, 181.0)  # Longitude > 180
        
        with pytest.raises(ValueError):
            Coordinates(0.0, -181.0)  # Longitude < -180
    
    def test_coordinates_string_representation(self):
        """Test string representation of coordinates."""
        coords = Coordinates(40.7128, -74.0060)
        str_repr = str(coords)
        assert "40.7128°N" in str_repr
        assert "74.0060°W" in str_repr
    
    def test_distance_calculation(self):
        """Test distance calculation between coordinates."""
        # TODO: Implement this test once distance_to method is implemented
        coords1 = Coordinates(40.7128, -74.0060)  # NYC
        coords2 = Coordinates(34.0522, -118.2437)  # LA
        
        # This test will pass once distance_to is implemented
        distance = coords1.distance_to(coords2)
        assert isinstance(distance, float)
        assert distance >= 0


class TestLocation:
    """Test cases for the Location class."""
    
    def test_location_creation(self):
        """Test creation of a location."""
        coords = Coordinates(40.7128, -74.0060)
        location = Location("New York", "USA", coords)
        
        assert location.name == "New York"
        assert location.country == "USA"
        assert location.coordinates == coords
    
    def test_location_full_name(self):
        """Test full name property."""
        coords = Coordinates(40.7128, -74.0060)
        location = Location("New York", "USA", coords, state="NY")
        
        assert location.full_name == "New York, NY, USA"
    
    def test_location_full_name_without_state(self):
        """Test full name property without state."""
        coords = Coordinates(51.5074, -0.1278)
        location = Location("London", "UK", coords)
        
        assert location.full_name == "London, UK"
    
    def test_empty_name_raises_error(self):
        """Test that empty name raises ValueError."""
        coords = Coordinates(0.0, 0.0)
        
        with pytest.raises(ValueError):
            Location("", "Country", coords)
    
    def test_empty_country_raises_error(self):
        """Test that empty country raises ValueError."""
        coords = Coordinates(0.0, 0.0)
        
        with pytest.raises(ValueError):
            Location("City", "", coords)
    
    def test_location_to_dict(self):
        """Test conversion to dictionary."""
        coords = Coordinates(40.7128, -74.0060)
        location = Location("New York", "USA", coords, state="NY")
        
        location_dict = location.to_dict()
        
        assert location_dict['name'] == "New York"
        assert location_dict['country'] == "USA"
        assert location_dict['state'] == "NY"
        assert location_dict['latitude'] == 40.7128
        assert location_dict['longitude'] == -74.0060
    
    def test_location_from_dict(self):
        """Test creation from dictionary."""
        data = {
            'name': 'Paris',
            'country': 'France',
            'latitude': 48.8566,
            'longitude': 2.3522
        }
        
        location = Location.from_dict(data)
        
        assert location.name == 'Paris'
        assert location.country == 'France'
        assert location.coordinates.latitude == 48.8566
        assert location.coordinates.longitude == 2.3522


class TestWeatherData:
    """Test cases for the WeatherData class."""
    
    def test_weather_data_creation(self):
        """Test creation of weather data."""
        timestamp = datetime.now()
        weather = WeatherData(
            city="London",
            country="UK",
            latitude=51.5074,
            longitude=-0.1278,
            timestamp=timestamp,
            timezone_offset=0,
            temperature=20.0,
            feels_like=22.0,
            temp_min=18.0,
            temp_max=25.0,
            pressure=1013.25,
            humidity=65,
            wind_speed=5.5,
            condition=WeatherCondition.CLEAR,
            description="clear sky"
        )
        
        assert weather.city == "London"
        assert weather.temperature == 20.0
        assert weather.condition == WeatherCondition.CLEAR
    
    def test_temperature_fahrenheit_conversion(self):
        """Test temperature conversion to Fahrenheit."""
        timestamp = datetime.now()
        weather = WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=timestamp, timezone_offset=0,
            temperature=0.0, feels_like=0.0, temp_min=0.0, temp_max=0.0,
            pressure=1013.25, humidity=50, wind_speed=0.0
        )
        
        assert weather.temperature_fahrenheit == 32.0  # 0°C = 32°F
    
    def test_wind_speed_conversions(self):
        """Test wind speed conversions."""
        timestamp = datetime.now()
        weather = WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=timestamp, timezone_offset=0,
            temperature=20.0, feels_like=20.0, temp_min=20.0, temp_max=20.0,
            pressure=1013.25, humidity=50, wind_speed=10.0  # 10 m/s
        )
        
        # 10 m/s = 22.37 mph (approximately)
        assert abs(weather.wind_speed_mph - 22.37) < 0.1
        
        # 10 m/s = 36 km/h
        assert weather.wind_speed_kmh == 36.0
    
    def test_weather_data_string_representation(self):
        """Test string representation of weather data."""
        timestamp = datetime.now()
        weather = WeatherData(
            city="Paris", country="France", latitude=48.8566, longitude=2.3522,
            timestamp=timestamp, timezone_offset=3600,
            temperature=25.5, feels_like=27.0, temp_min=23.0, temp_max=28.0,
            pressure=1015.0, humidity=60, wind_speed=3.2,
            condition=WeatherCondition.CLOUDS, description="few clouds"
        )
        
        str_repr = str(weather)
        assert "Paris" in str_repr
        assert "France" in str_repr
        assert "25.5°C" in str_repr
        assert "few clouds" in str_repr
    
    def test_precipitation_check(self):
        """Test precipitation detection."""
        timestamp = datetime.now()
        weather = WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=timestamp, timezone_offset=0,
            temperature=15.0, feels_like=15.0, temp_min=15.0, temp_max=15.0,
            pressure=1010.0, humidity=80, wind_speed=2.0,
            rain_1h=2.5  # 2.5mm of rain
        )
        
        # TODO: This test will pass once is_precipitation method is implemented
        # assert weather.is_precipitation() == True
    
    def test_comfort_index_calculation(self):
        """Test comfort index calculation."""
        timestamp = datetime.now()
        weather = WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=timestamp, timezone_offset=0,
            temperature=22.0, feels_like=24.0, temp_min=20.0, temp_max=25.0,
            pressure=1013.0, humidity=55, wind_speed=1.5
        )
        
        # TODO: This test will pass once get_comfort_index method is implemented
        comfort = weather.get_comfort_index()
        assert isinstance(comfort, str)


# Test fixtures for common test data
@pytest.fixture
def sample_coordinates():
    """Fixture providing sample coordinates."""
    return Coordinates(40.7128, -74.0060)


@pytest.fixture
def sample_location(sample_coordinates):
    """Fixture providing sample location."""
    return Location("New York", "USA", sample_coordinates, state="NY")


@pytest.fixture
def sample_weather_data():
    """Fixture providing sample weather data."""
    return WeatherData(
        city="London",
        country="UK",
        latitude=51.5074,
        longitude=-0.1278,
        timestamp=datetime.now(),
        timezone_offset=0,
        temperature=18.5,
        feels_like=20.0,
        temp_min=15.0,
        temp_max=22.0,
        pressure=1015.3,
        humidity=72,
        wind_speed=4.2,
        condition=WeatherCondition.CLOUDS,
        description="scattered clouds"
    )