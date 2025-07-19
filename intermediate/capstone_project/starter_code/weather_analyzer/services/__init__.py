"""
Services module for external integrations and data access.

This module contains services for interacting with external APIs,
data storage, and other external systems.
"""

from .weather_api import WeatherAPIService
from .data_storage import DataStorage

__all__ = ['WeatherAPIService', 'DataStorage']