"""
Weather API service for fetching weather data from external sources.
"""

import logging
import time
from typing import Dict, List, Optional
import requests
from datetime import datetime, timedelta

from weather_analyzer.models.weather_data import WeatherData
from weather_analyzer.models.location import Location
from weather_analyzer.utils.config import Config


class WeatherAPIError(Exception):
    """Custom exception for weather API errors."""
    pass


class RateLimitError(WeatherAPIError):
    """Exception raised when API rate limit is exceeded."""
    pass


class WeatherAPIService:
    """
    Service for interacting with weather APIs.
    
    This class handles API requests, rate limiting, error handling,
    and data parsing for weather information.
    """
    
    def __init__(self, config: Config):
        """
        Initialize the weather API service.
        
        Args:
            config: Configuration object containing API settings
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.session = requests.Session()
        self.last_request_time = 0
        self.min_request_interval = 1.0  # Minimum seconds between requests
        
        # Set up session headers
        self.session.headers.update({
            'User-Agent': 'Weather-Analyzer/1.0'
        })
    
    def _rate_limit(self) -> None:
        """Implement rate limiting to avoid exceeding API limits."""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        
        if time_since_last_request < self.min_request_interval:
            sleep_time = self.min_request_interval - time_since_last_request
            self.logger.debug(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def _make_request(self, url: str, params: Dict) -> Dict:
        """
        Make a request to the weather API with error handling.
        
        Args:
            url: API endpoint URL
            params: Request parameters
            
        Returns:
            dict: API response data
            
        Raises:
            WeatherAPIError: If the API request fails
            RateLimitError: If rate limit is exceeded
        """
        self._rate_limit()
        
        try:
            # Add API key to parameters
            params['appid'] = self.config.weather_api_key
            
            self.logger.debug(f"Making API request to {url} with params: {params}")
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 429:
                raise RateLimitError("API rate limit exceeded")
            elif response.status_code == 401:
                raise WeatherAPIError("Invalid API key")
            elif response.status_code == 404:
                raise WeatherAPIError("Location not found")
            elif not response.ok:
                raise WeatherAPIError(f"API request failed: {response.status_code}")
            
            return response.json()
            
        except requests.RequestException as e:
            raise WeatherAPIError(f"Network error: {e}")
    
    def get_current_weather(self, location: str, units: str = "metric") -> WeatherData:
        """
        Get current weather data for a location.
        
        Args:
            location: City name or coordinates
            units: Temperature units ('metric', 'imperial', 'kelvin')
            
        Returns:
            WeatherData: Current weather information
            
        Raises:
            WeatherAPIError: If the API request fails
        """
        # TODO: Implement current weather fetching
        # 1. Build the API URL and parameters
        # 2. Make the API request
        # 3. Parse the response into a WeatherData object
        # 4. Handle errors appropriately
        
        url = f"{self.config.weather_api_base_url}/weather"
        params = {
            'q': location,
            'units': units
        }
        
        self.logger.info(f"Fetching current weather for {location}")
        
        # Placeholder implementation
        raise NotImplementedError("Current weather fetching not implemented")
    
    def get_weather_forecast(self, location: str, days: int = 5, 
                           units: str = "metric") -> List[WeatherData]:
        """
        Get weather forecast for a location.
        
        Args:
            location: City name or coordinates
            days: Number of days to forecast (1-5)
            units: Temperature units ('metric', 'imperial', 'kelvin')
            
        Returns:
            List[WeatherData]: List of weather forecasts
            
        Raises:
            WeatherAPIError: If the API request fails
        """
        # TODO: Implement weather forecast fetching
        # 1. Validate the number of days (API typically supports 5 days)
        # 2. Build the API URL and parameters
        # 3. Make the API request
        # 4. Parse the response into a list of WeatherData objects
        # 5. Handle errors appropriately
        
        if not 1 <= days <= 5:
            raise ValueError("Days must be between 1 and 5")
        
        url = f"{self.config.weather_api_base_url}/forecast"
        params = {
            'q': location,
            'units': units
        }
        
        self.logger.info(f"Fetching {days}-day forecast for {location}")
        
        # Placeholder implementation
        raise NotImplementedError("Weather forecast fetching not implemented")
    
    def get_historical_weather(self, location: str, start_date: datetime, 
                             end_date: datetime, units: str = "metric") -> List[WeatherData]:
        """
        Get historical weather data for a location.
        
        Args:
            location: City name or coordinates
            start_date: Start date for historical data
            end_date: End date for historical data
            units: Temperature units ('metric', 'imperial', 'kelvin')
            
        Returns:
            List[WeatherData]: List of historical weather data
            
        Raises:
            WeatherAPIError: If the API request fails
            
        Note:
            Historical weather data may require a paid API plan.
        """
        # TODO: Implement historical weather fetching
        # 1. Validate date range
        # 2. Convert dates to Unix timestamps
        # 3. Make API requests (may need multiple requests for large date ranges)
        # 4. Parse responses into WeatherData objects
        # 5. Handle pagination if necessary
        
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")
        
        if end_date > datetime.now():
            raise ValueError("End date cannot be in the future")
        
        self.logger.info(f"Fetching historical weather for {location} "
                        f"from {start_date} to {end_date}")
        
        # Placeholder implementation
        raise NotImplementedError("Historical weather fetching not implemented")
    
    def search_locations(self, query: str, limit: int = 5) -> List[Location]:
        """
        Search for locations by name.
        
        Args:
            query: Location search query
            limit: Maximum number of results to return
            
        Returns:
            List[Location]: List of matching locations
            
        Raises:
            WeatherAPIError: If the API request fails
        """
        # TODO: Implement location search using geocoding API
        # 1. Use the geocoding API to search for locations
        # 2. Parse the response into Location objects
        # 3. Limit the number of results
        # 4. Handle cases where no locations are found
        
        url = f"{self.config.weather_api_base_url}/geo/1.0/direct"
        params = {
            'q': query,
            'limit': limit
        }
        
        self.logger.info(f"Searching for locations matching '{query}'")
        
        # Placeholder implementation
        raise NotImplementedError("Location search not implemented")
    
    def get_air_quality(self, location: str) -> Dict:
        """
        Get air quality data for a location.
        
        Args:
            location: City name or coordinates
            
        Returns:
            dict: Air quality information
            
        Raises:
            WeatherAPIError: If the API request fails
        """
        # TODO: Implement air quality data fetching
        # This is an optional feature that uses the air pollution API
        
        self.logger.info(f"Fetching air quality data for {location}")
        
        # Placeholder implementation
        raise NotImplementedError("Air quality fetching not implemented")
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close the session."""
        self.session.close()