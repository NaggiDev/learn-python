"""
Complete implementation of Weather API service.
This is the reference solution showing how to properly integrate with the OpenWeatherMap API.
"""

import logging
import time
import json
from typing import Dict, List, Optional
import requests
from datetime import datetime, timedelta

from weather_analyzer.models.weather_data import WeatherData, WeatherCondition
from weather_analyzer.models.location import Location, Coordinates
from weather_analyzer.utils.config import Config


class WeatherAPIError(Exception):
    """Custom exception for weather API errors."""
    pass


class RateLimitError(WeatherAPIError):
    """Exception raised when API rate limit is exceeded."""
    pass


class WeatherAPIService:
    """
    Complete implementation of weather API service.
    
    This service handles all interactions with the OpenWeatherMap API,
    including current weather, forecasts, and historical data.
    """
    
    def __init__(self, config: Config):
        """Initialize the weather API service."""
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
        """Make a request to the weather API with comprehensive error handling."""
        self._rate_limit()
        
        try:
            # Add API key to parameters
            params['appid'] = self.config.weather_api_key
            
            self.logger.debug(f"Making API request to {url} with params: {params}")
            response = self.session.get(url, params=params, timeout=10)
            
            # Handle different HTTP status codes
            if response.status_code == 429:
                raise RateLimitError("API rate limit exceeded. Please wait before making more requests.")
            elif response.status_code == 401:
                raise WeatherAPIError("Invalid API key. Please check your configuration.")
            elif response.status_code == 404:
                raise WeatherAPIError("Location not found. Please check the city name.")
            elif response.status_code == 400:
                raise WeatherAPIError("Bad request. Please check your parameters.")
            elif not response.ok:
                raise WeatherAPIError(f"API request failed with status {response.status_code}: {response.text}")
            
            return response.json()
            
        except requests.RequestException as e:
            raise WeatherAPIError(f"Network error occurred: {e}")
        except json.JSONDecodeError as e:
            raise WeatherAPIError(f"Invalid JSON response from API: {e}")
    
    def get_current_weather(self, location: str, units: str = "metric") -> WeatherData:
        """
        Get current weather data for a location.
        
        This is a complete implementation showing proper API integration,
        error handling, and data parsing.
        """
        url = f"{self.config.weather_api_base_url}/weather"
        params = {
            'q': location,
            'units': units
        }
        
        self.logger.info(f"Fetching current weather for {location}")
        
        try:
            api_data = self._make_request(url, params)
            return self._parse_current_weather_response(api_data)
            
        except WeatherAPIError:
            raise
        except Exception as e:
            raise WeatherAPIError(f"Unexpected error while fetching weather data: {e}")
    
    def _parse_current_weather_response(self, api_data: Dict) -> WeatherData:
        """
        Parse OpenWeatherMap current weather API response into WeatherData object.
        
        This shows how to properly extract and validate data from API responses.
        """
        try:
            # Extract basic location information
            city = api_data.get('name', 'Unknown')
            country = api_data.get('sys', {}).get('country', 'Unknown')
            coords = api_data.get('coord', {})
            latitude = float(coords.get('lat', 0.0))
            longitude = float(coords.get('lon', 0.0))
            
            # Extract timestamp and timezone
            timestamp = datetime.fromtimestamp(api_data.get('dt', 0))
            timezone_offset = api_data.get('timezone', 0)
            
            # Extract temperature data
            main_data = api_data.get('main', {})
            temperature = float(main_data.get('temp', 0.0))
            feels_like = float(main_data.get('feels_like', temperature))
            temp_min = float(main_data.get('temp_min', temperature))
            temp_max = float(main_data.get('temp_max', temperature))
            
            # Extract atmospheric data
            pressure = float(main_data.get('pressure', 1013.25))
            humidity = int(main_data.get('humidity', 50))
            visibility = api_data.get('visibility')  # Optional field
            
            # Extract wind data
            wind_data = api_data.get('wind', {})
            wind_speed = float(wind_data.get('speed', 0.0))
            wind_direction = wind_data.get('deg')  # Optional field
            wind_gust = wind_data.get('gust')  # Optional field
            
            # Extract weather conditions
            weather_list = api_data.get('weather', [{}])
            weather_info = weather_list[0] if weather_list else {}
            
            condition_main = weather_info.get('main', '').lower()
            condition = self._map_weather_condition(condition_main)
            description = weather_info.get('description', '')
            
            # Extract precipitation data
            rain_data = api_data.get('rain', {})
            rain_1h = rain_data.get('1h')
            rain_3h = rain_data.get('3h')
            
            snow_data = api_data.get('snow', {})
            snow_1h = snow_data.get('1h')
            snow_3h = snow_data.get('3h')
            
            # Extract cloud data
            clouds_data = api_data.get('clouds', {})
            cloudiness = clouds_data.get('all')
            
            # Create WeatherData object
            weather_data = WeatherData(
                city=city,
                country=country,
                latitude=latitude,
                longitude=longitude,
                timestamp=timestamp,
                timezone_offset=timezone_offset,
                temperature=temperature,
                feels_like=feels_like,
                temp_min=temp_min,
                temp_max=temp_max,
                pressure=pressure,
                humidity=humidity,
                visibility=visibility,
                wind_speed=wind_speed,
                wind_direction=wind_direction,
                wind_gust=wind_gust,
                condition=condition,
                description=description,
                rain_1h=rain_1h,
                rain_3h=rain_3h,
                snow_1h=snow_1h,
                snow_3h=snow_3h,
                cloudiness=cloudiness
            )
            
            self.logger.debug(f"Successfully parsed weather data for {city}")
            return weather_data
            
        except (KeyError, ValueError, TypeError) as e:
            raise WeatherAPIError(f"Failed to parse API response: {e}")
    
    def _map_weather_condition(self, condition_main: str) -> WeatherCondition:
        """Map OpenWeatherMap weather condition to our enum."""
        condition_mapping = {
            'clear': WeatherCondition.CLEAR,
            'clouds': WeatherCondition.CLOUDS,
            'rain': WeatherCondition.RAIN,
            'drizzle': WeatherCondition.DRIZZLE,
            'thunderstorm': WeatherCondition.THUNDERSTORM,
            'snow': WeatherCondition.SNOW,
            'mist': WeatherCondition.MIST,
            'fog': WeatherCondition.FOG,
        }
        
        return condition_mapping.get(condition_main, WeatherCondition.UNKNOWN)
    
    def get_weather_forecast(self, location: str, days: int = 5, 
                           units: str = "metric") -> List[WeatherData]:
        """
        Get weather forecast for a location.
        
        Complete implementation with proper error handling and data parsing.
        """
        if not 1 <= days <= 5:
            raise ValueError("Days must be between 1 and 5 for the free API tier")
        
        url = f"{self.config.weather_api_base_url}/forecast"
        params = {
            'q': location,
            'units': units
        }
        
        self.logger.info(f"Fetching {days}-day forecast for {location}")
        
        try:
            api_data = self._make_request(url, params)
            return self._parse_forecast_response(api_data, days)
            
        except WeatherAPIError:
            raise
        except Exception as e:
            raise WeatherAPIError(f"Unexpected error while fetching forecast: {e}")
    
    def _parse_forecast_response(self, api_data: Dict, days: int) -> List[WeatherData]:
        """Parse forecast API response into list of WeatherData objects."""
        try:
            forecast_list = []
            city_info = api_data.get('city', {})
            city_name = city_info.get('name', 'Unknown')
            country = city_info.get('country', 'Unknown')
            coords = city_info.get('coord', {})
            latitude = float(coords.get('lat', 0.0))
            longitude = float(coords.get('lon', 0.0))
            timezone_offset = api_data.get('city', {}).get('timezone', 0)
            
            # Process forecast entries
            forecast_entries = api_data.get('list', [])
            cutoff_time = datetime.now() + timedelta(days=days)
            
            for entry in forecast_entries:
                timestamp = datetime.fromtimestamp(entry.get('dt', 0))
                
                # Only include forecasts within the requested time range
                if timestamp > cutoff_time:
                    break
                
                # Parse each forecast entry similar to current weather
                main_data = entry.get('main', {})
                weather_data = WeatherData(
                    city=city_name,
                    country=country,
                    latitude=latitude,
                    longitude=longitude,
                    timestamp=timestamp,
                    timezone_offset=timezone_offset,
                    temperature=float(main_data.get('temp', 0.0)),
                    feels_like=float(main_data.get('feels_like', 0.0)),
                    temp_min=float(main_data.get('temp_min', 0.0)),
                    temp_max=float(main_data.get('temp_max', 0.0)),
                    pressure=float(main_data.get('pressure', 1013.25)),
                    humidity=int(main_data.get('humidity', 50)),
                    wind_speed=float(entry.get('wind', {}).get('speed', 0.0)),
                    wind_direction=entry.get('wind', {}).get('deg'),
                    condition=self._map_weather_condition(
                        entry.get('weather', [{}])[0].get('main', '').lower()
                    ),
                    description=entry.get('weather', [{}])[0].get('description', ''),
                    cloudiness=entry.get('clouds', {}).get('all'),
                    rain_3h=entry.get('rain', {}).get('3h'),
                    snow_3h=entry.get('snow', {}).get('3h')
                )
                
                forecast_list.append(weather_data)
            
            self.logger.debug(f"Successfully parsed {len(forecast_list)} forecast entries")
            return forecast_list
            
        except (KeyError, ValueError, TypeError) as e:
            raise WeatherAPIError(f"Failed to parse forecast response: {e}")
    
    def search_locations(self, query: str, limit: int = 5) -> List[Location]:
        """
        Search for locations using the geocoding API.
        
        Complete implementation showing how to use multiple API endpoints.
        """
        url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {
            'q': query,
            'limit': limit
        }
        
        self.logger.info(f"Searching for locations matching '{query}'")
        
        try:
            api_data = self._make_request(url, params)
            return self._parse_geocoding_response(api_data)
            
        except WeatherAPIError:
            raise
        except Exception as e:
            raise WeatherAPIError(f"Unexpected error while searching locations: {e}")
    
    def _parse_geocoding_response(self, api_data: List[Dict]) -> List[Location]:
        """Parse geocoding API response into Location objects."""
        locations = []
        
        for entry in api_data:
            try:
                name = entry.get('name', 'Unknown')
                country = entry.get('country', 'Unknown')
                state = entry.get('state')
                latitude = float(entry.get('lat', 0.0))
                longitude = float(entry.get('lon', 0.0))
                
                coordinates = Coordinates(latitude, longitude)
                location = Location(
                    name=name,
                    country=country,
                    coordinates=coordinates,
                    state=state
                )
                
                locations.append(location)
                
            except (KeyError, ValueError, TypeError) as e:
                self.logger.warning(f"Failed to parse location entry: {e}")
                continue
        
        return locations
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close the session."""
        self.session.close()