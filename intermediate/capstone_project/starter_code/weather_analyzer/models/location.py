"""
Location models for representing geographic locations and coordinates.
"""

from dataclasses import dataclass
from typing import Optional, Tuple
import math


@dataclass
class Coordinates:
    """
    Represents geographic coordinates (latitude and longitude).
    """
    latitude: float
    longitude: float
    
    def __post_init__(self):
        """Validate coordinates after initialization."""
        if not (-90 <= self.latitude <= 90):
            raise ValueError(f"Invalid latitude: {self.latitude}. Must be between -90 and 90.")
        if not (-180 <= self.longitude <= 180):
            raise ValueError(f"Invalid longitude: {self.longitude}. Must be between -180 and 180.")
    
    def distance_to(self, other: 'Coordinates') -> float:
        """
        Calculate the distance to another coordinate using the Haversine formula.
        
        Args:
            other: Another Coordinates object
            
        Returns:
            float: Distance in kilometers
        """
        # TODO: Implement Haversine distance calculation
        # Use the Haversine formula to calculate great-circle distance
        # Return distance in kilometers
        return 0.0
    
    def __str__(self) -> str:
        """String representation of coordinates."""
        lat_dir = "N" if self.latitude >= 0 else "S"
        lon_dir = "E" if self.longitude >= 0 else "W"
        return f"{abs(self.latitude):.4f}°{lat_dir}, {abs(self.longitude):.4f}°{lon_dir}"


@dataclass
class Location:
    """
    Represents a geographic location with name and coordinates.
    """
    name: str
    country: str
    coordinates: Coordinates
    state: Optional[str] = None
    timezone: Optional[str] = None
    population: Optional[int] = None
    
    def __post_init__(self):
        """Validate location data after initialization."""
        if not self.name.strip():
            raise ValueError("Location name cannot be empty")
        if not self.country.strip():
            raise ValueError("Country name cannot be empty")
    
    @property
    def full_name(self) -> str:
        """Get the full name of the location."""
        if self.state:
            return f"{self.name}, {self.state}, {self.country}"
        return f"{self.name}, {self.country}"
    
    def distance_to(self, other: 'Location') -> float:
        """
        Calculate distance to another location.
        
        Args:
            other: Another Location object
            
        Returns:
            float: Distance in kilometers
        """
        return self.coordinates.distance_to(other.coordinates)
    
    def is_nearby(self, other: 'Location', max_distance_km: float = 50.0) -> bool:
        """
        Check if another location is nearby.
        
        Args:
            other: Another Location object
            max_distance_km: Maximum distance to consider as nearby
            
        Returns:
            bool: True if locations are within the specified distance
        """
        return self.distance_to(other) <= max_distance_km
    
    @classmethod
    def from_city_name(cls, city_name: str, country: str = "") -> 'Location':
        """
        Create a Location from city name (placeholder for geocoding).
        
        Args:
            city_name: Name of the city
            country: Country name (optional)
            
        Returns:
            Location: Location object with estimated coordinates
            
        Note:
            This is a placeholder implementation. In a real application,
            you would use a geocoding service to get actual coordinates.
        """
        # TODO: Implement geocoding functionality
        # Use a geocoding service (like OpenWeatherMap's geocoding API)
        # to convert city names to coordinates
        
        # Placeholder coordinates (London, UK)
        coordinates = Coordinates(51.5074, -0.1278)
        return cls(
            name=city_name,
            country=country or "Unknown",
            coordinates=coordinates
        )
    
    def to_dict(self) -> dict:
        """Convert location to dictionary format."""
        return {
            'name': self.name,
            'country': self.country,
            'state': self.state,
            'latitude': self.coordinates.latitude,
            'longitude': self.coordinates.longitude,
            'timezone': self.timezone,
            'population': self.population
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Location':
        """Create Location from dictionary data."""
        coordinates = Coordinates(data['latitude'], data['longitude'])
        return cls(
            name=data['name'],
            country=data['country'],
            coordinates=coordinates,
            state=data.get('state'),
            timezone=data.get('timezone'),
            population=data.get('population')
        )
    
    def __str__(self) -> str:
        """String representation of location."""
        return self.full_name
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return (f"Location(name='{self.name}', country='{self.country}', "
                f"coordinates={self.coordinates})")