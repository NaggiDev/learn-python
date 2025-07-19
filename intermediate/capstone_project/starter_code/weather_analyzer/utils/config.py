"""
Configuration management for the Weather Analyzer application.
"""

import os
import logging
from typing import Optional
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass


class Config:
    """
    Configuration management class.
    
    This class handles loading configuration from environment variables,
    .env files, and providing default values for application settings.
    """
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize configuration.
        
        Args:
            config_file: Optional path to configuration file
        """
        self.logger = logging.getLogger(__name__)
        
        # Load environment variables from .env file if available
        if load_dotenv and config_file:
            load_dotenv(config_file)
        elif load_dotenv:
            # Try to load from default .env file
            env_file = Path('.env')
            if env_file.exists():
                load_dotenv(env_file)
        
        # Load configuration values
        self._load_config()
    
    def _load_config(self) -> None:
        """Load configuration values from environment variables."""
        # Weather API configuration
        self.weather_api_key = os.getenv('WEATHER_API_KEY')
        if not self.weather_api_key:
            raise ConfigError(
                "WEATHER_API_KEY environment variable is required. "
                "Please set it in your .env file or environment."
            )
        
        self.weather_api_base_url = os.getenv(
            'WEATHER_API_BASE_URL', 
            'https://api.openweathermap.org/data/2.5'
        )
        
        # Application configuration
        self.log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        self.cache_duration = int(os.getenv('CACHE_DURATION', '3600'))  # 1 hour default
        self.data_dir = os.getenv('DATA_DIR', 'data')
        
        # API rate limiting
        self.api_rate_limit = int(os.getenv('API_RATE_LIMIT', '60'))  # calls per minute
        self.request_timeout = int(os.getenv('REQUEST_TIMEOUT', '10'))  # seconds
        
        # Default units
        self.default_units = os.getenv('DEFAULT_UNITS', 'metric')  # metric, imperial, kelvin
        
        # Chart configuration
        self.chart_width = int(os.getenv('CHART_WIDTH', '80'))
        self.chart_height = int(os.getenv('CHART_HEIGHT', '20'))
        
        self.logger.debug("Configuration loaded successfully")
    
    def validate_config(self) -> bool:
        """
        Validate the current configuration.
        
        Returns:
            bool: True if configuration is valid, False otherwise
        """
        # TODO: Implement configuration validation
        # 1. Check if API key is valid format
        # 2. Validate URL format
        # 3. Check if data directory is writable
        # 4. Validate numeric values are in reasonable ranges
        
        try:
            # Check API key format (basic validation)
            if not self.weather_api_key or len(self.weather_api_key) < 10:
                self.logger.error("Invalid API key format")
                return False
            
            # Check if data directory can be created
            data_path = Path(self.data_dir)
            data_path.mkdir(parents=True, exist_ok=True)
            
            # Validate log level
            valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
            if self.log_level not in valid_log_levels:
                self.logger.warning(f"Invalid log level: {self.log_level}, using INFO")
                self.log_level = 'INFO'
            
            # Validate units
            valid_units = ['metric', 'imperial', 'kelvin']
            if self.default_units not in valid_units:
                self.logger.warning(f"Invalid units: {self.default_units}, using metric")
                self.default_units = 'metric'
            
            return True
            
        except Exception as e:
            self.logger.error(f"Configuration validation failed: {e}")
            return False
    
    def get_api_url(self, endpoint: str) -> str:
        """
        Get the full API URL for a specific endpoint.
        
        Args:
            endpoint: API endpoint (e.g., 'weather', 'forecast')
            
        Returns:
            str: Full API URL
        """
        return f"{self.weather_api_base_url}/{endpoint}"
    
    def get_cache_file_path(self, cache_key: str) -> Path:
        """
        Get the full path for a cache file.
        
        Args:
            cache_key: Cache key identifier
            
        Returns:
            Path: Full path to cache file
        """
        return Path(self.data_dir) / "cache" / f"{cache_key}.json"
    
    def get_report_file_path(self, filename: str) -> Path:
        """
        Get the full path for a report file.
        
        Args:
            filename: Report filename
            
        Returns:
            Path: Full path to report file
        """
        return Path(self.data_dir) / "reports" / filename
    
    def to_dict(self) -> dict:
        """
        Convert configuration to dictionary format.
        
        Returns:
            dict: Configuration as dictionary (excluding sensitive data)
        """
        return {
            'weather_api_base_url': self.weather_api_base_url,
            'log_level': self.log_level,
            'cache_duration': self.cache_duration,
            'data_dir': self.data_dir,
            'api_rate_limit': self.api_rate_limit,
            'request_timeout': self.request_timeout,
            'default_units': self.default_units,
            'chart_width': self.chart_width,
            'chart_height': self.chart_height,
            # Note: API key is excluded for security
        }
    
    def __str__(self) -> str:
        """String representation of configuration."""
        config_dict = self.to_dict()
        lines = ["Configuration:"]
        for key, value in config_dict.items():
            lines.append(f"  {key}: {value}")
        return "\n".join(lines)
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return f"Config(api_url='{self.weather_api_base_url}', data_dir='{self.data_dir}')"