"""
Weather data models for representing weather observations and conditions.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class WeatherCondition(Enum):
    """Enumeration of possible weather conditions."""
    CLEAR = "clear"
    CLOUDS = "clouds"
    RAIN = "rain"
    DRIZZLE = "drizzle"
    THUNDERSTORM = "thunderstorm"
    SNOW = "snow"
    MIST = "mist"
    FOG = "fog"
    UNKNOWN = "unknown"


@dataclass
class WeatherData:
    """
    Represents a single weather observation.
    
    This class encapsulates all the weather information for a specific
    location and time, including temperature, humidity, pressure, and
    other meteorological data.
    """
    
    # Location information
    city: str
    country: str
    latitude: float
    longitude: float
    
    # Time information
    timestamp: datetime
    timezone_offset: int  # Offset from UTC in seconds
    
    # Temperature data (in Celsius)
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    
    # Atmospheric data
    pressure: float  # hPa
    humidity: int    # percentage
    visibility: Optional[float] = None  # meters
    
    # Wind data
    wind_speed: float  # m/s
    wind_direction: Optional[int] = None  # degrees
    wind_gust: Optional[float] = None  # m/s
    
    # Weather conditions
    condition: WeatherCondition = WeatherCondition.UNKNOWN
    description: str = ""
    
    # Precipitation
    rain_1h: Optional[float] = None  # mm
    rain_3h: Optional[float] = None  # mm
    snow_1h: Optional[float] = None  # mm
    snow_3h: Optional[float] = None  # mm
    
    # Cloud coverage
    cloudiness: Optional[int] = None  # percentage
    
    def __post_init__(self):
        """Validate data after initialization."""
        # TODO: Add validation logic
        # - Temperature should be within reasonable bounds
        # - Humidity should be 0-100%
        # - Pressure should be positive
        # - Wind speed should be non-negative
        pass
    
    @property
    def temperature_fahrenheit(self) -> float:
        """Convert temperature to Fahrenheit."""
        return (self.temperature * 9/5) + 32
    
    @property
    def wind_speed_mph(self) -> float:
        """Convert wind speed to miles per hour."""
        return self.wind_speed * 2.237
    
    @property
    def wind_speed_kmh(self) -> float:
        """Convert wind speed to kilometers per hour."""
        return self.wind_speed * 3.6
    
    def is_precipitation(self) -> bool:
        """Check if there is any precipitation."""
        # TODO: Implement precipitation check
        # Check rain_1h, rain_3h, snow_1h, snow_3h values
        return False
    
    def get_comfort_index(self) -> str:
        """
        Calculate a simple comfort index based on temperature and humidity.
        
        Returns:
            str: Comfort level description
        """
        # TODO: Implement comfort index calculation
        # Consider temperature, humidity, and wind speed
        # Return one of: "Very Comfortable", "Comfortable", "Uncomfortable", "Very Uncomfortable"
        return "Unknown"
    
    def to_dict(self) -> dict:
        """Convert weather data to dictionary format."""
        # TODO: Implement dictionary conversion
        # Include all relevant fields in a structured format
        return {}
    
    @classmethod
    def from_api_response(cls, api_data: dict) -> 'WeatherData':
        """
        Create WeatherData instance from API response.
        
        Args:
            api_data: Raw API response data
            
        Returns:
            WeatherData: Parsed weather data object
        """
        # TODO: Implement API response parsing
        # Parse the API response and create a WeatherData instance
        # Handle missing or invalid data gracefully
        raise NotImplementedError("API response parsing not implemented")
    
    def __str__(self) -> str:
        """String representation of weather data."""
        return (f"Weather in {self.city}, {self.country}: "
                f"{self.temperature:.1f}°C, {self.description}")
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return (f"WeatherData(city='{self.city}', temperature={self.temperature}, "
                f"condition={self.condition.value}, timestamp={self.timestamp})")