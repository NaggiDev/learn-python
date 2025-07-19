"""
Data models for the Weather Analyzer application.

This module contains the core data structures used throughout the application
to represent weather data, locations, and related information.
"""

from .weather_data import WeatherData, WeatherCondition
from .location import Location, Coordinates

__all__ = ['WeatherData', 'WeatherCondition', 'Location', 'Coordinates']