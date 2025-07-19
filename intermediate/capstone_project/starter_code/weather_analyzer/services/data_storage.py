"""
Data storage service for caching and persisting weather data.
"""

import json
import csv
import logging
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Union

from weather_analyzer.models.weather_data import WeatherData
from weather_analyzer.models.location import Location


class DataStorage:
    """
    Service for storing and retrieving weather data.
    
    This class handles caching of API responses, storing historical data,
    and managing data persistence in various formats.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the data storage service.
        
        Args:
            data_dir: Directory for storing data files
        """
        self.data_dir = Path(data_dir)
        self.cache_dir = self.data_dir / "cache"
        self.reports_dir = self.data_dir / "reports"
        self.logger = logging.getLogger(__name__)
        
        # Create directories if they don't exist
        self._create_directories()
    
    def _create_directories(self) -> None:
        """Create necessary directories for data storage."""
        directories = [self.data_dir, self.cache_dir, self.reports_dir]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            self.logger.debug(f"Created directory: {directory}")
    
    def _get_cache_key(self, location: str, data_type: str) -> str:
        """
        Generate a cache key for storing data.
        
        Args:
            location: Location identifier
            data_type: Type of data (current, forecast, historical)
            
        Returns:
            str: Cache key
        """
        # TODO: Implement cache key generation
        # Create a unique key based on location and data type
        # Consider normalizing location names for consistency
        return f"{location}_{data_type}".replace(" ", "_").lower()
    
    def _get_cache_file_path(self, cache_key: str) -> Path:
        """Get the file path for a cache entry."""
        return self.cache_dir / f"{cache_key}.json"
    
    def is_cache_valid(self, cache_key: str, max_age_hours: int = 1) -> bool:
        """
        Check if cached data is still valid.
        
        Args:
            cache_key: Cache key to check
            max_age_hours: Maximum age of cache in hours
            
        Returns:
            bool: True if cache is valid, False otherwise
        """
        # TODO: Implement cache validation
        # 1. Check if cache file exists
        # 2. Check the modification time of the file
        # 3. Compare with max_age_hours to determine if still valid
        
        cache_file = self._get_cache_file_path(cache_key)
        
        if not cache_file.exists():
            return False
        
        # Placeholder implementation
        return False
    
    def save_to_cache(self, cache_key: str, data: Union[WeatherData, List[WeatherData]]) -> None:
        """
        Save weather data to cache.
        
        Args:
            cache_key: Cache key for the data
            data: Weather data to cache
        """
        # TODO: Implement cache saving
        # 1. Convert WeatherData object(s) to dictionary format
        # 2. Add timestamp for cache validation
        # 3. Save to JSON file
        # 4. Handle errors gracefully
        
        cache_file = self._get_cache_file_path(cache_key)
        
        try:
            # Placeholder implementation
            cache_data = {
                'timestamp': datetime.now().isoformat(),
                'data': data  # This needs to be converted to dict format
            }
            
            with open(cache_file, 'w') as f:
                json.dump(cache_data, f, indent=2)
            
            self.logger.debug(f"Saved data to cache: {cache_file}")
            
        except Exception as e:
            self.logger.error(f"Failed to save cache: {e}")
    
    def load_from_cache(self, cache_key: str) -> Optional[Union[WeatherData, List[WeatherData]]]:
        """
        Load weather data from cache.
        
        Args:
            cache_key: Cache key for the data
            
        Returns:
            Weather data if found and valid, None otherwise
        """
        # TODO: Implement cache loading
        # 1. Check if cache is valid
        # 2. Load JSON data from file
        # 3. Convert back to WeatherData object(s)
        # 4. Handle errors gracefully
        
        if not self.is_cache_valid(cache_key):
            return None
        
        cache_file = self._get_cache_file_path(cache_key)
        
        try:
            with open(cache_file, 'r') as f:
                cache_data = json.load(f)
            
            # TODO: Convert dictionary data back to WeatherData objects
            self.logger.debug(f"Loaded data from cache: {cache_file}")
            return None  # Placeholder
            
        except Exception as e:
            self.logger.error(f"Failed to load cache: {e}")
            return None
    
    def save_weather_data_csv(self, weather_data: List[WeatherData], 
                             filename: str) -> None:
        """
        Save weather data to CSV file.
        
        Args:
            weather_data: List of weather data to save
            filename: Name of the CSV file
        """
        # TODO: Implement CSV export
        # 1. Define CSV headers based on WeatherData fields
        # 2. Convert WeatherData objects to CSV rows
        # 3. Write to CSV file with proper formatting
        # 4. Handle errors gracefully
        
        csv_file = self.reports_dir / filename
        
        try:
            # Placeholder implementation
            headers = [
                'timestamp', 'city', 'country', 'temperature', 'humidity',
                'pressure', 'wind_speed', 'condition', 'description'
            ]
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                
                # TODO: Write weather data rows
                
            self.logger.info(f"Saved weather data to CSV: {csv_file}")
            
        except Exception as e:
            self.logger.error(f"Failed to save CSV: {e}")
    
    def load_weather_data_csv(self, filename: str) -> List[WeatherData]:
        """
        Load weather data from CSV file.
        
        Args:
            filename: Name of the CSV file
            
        Returns:
            List[WeatherData]: Loaded weather data
        """
        # TODO: Implement CSV import
        # 1. Read CSV file
        # 2. Parse rows into WeatherData objects
        # 3. Handle data type conversions
        # 4. Handle errors gracefully
        
        csv_file = self.reports_dir / filename
        weather_data = []
        
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    # TODO: Convert CSV row to WeatherData object
                    pass
            
            self.logger.info(f"Loaded weather data from CSV: {csv_file}")
            return weather_data
            
        except Exception as e:
            self.logger.error(f"Failed to load CSV: {e}")
            return []
    
    def save_report(self, report_content: str, filename: str) -> None:
        """
        Save a text report to file.
        
        Args:
            report_content: Content of the report
            filename: Name of the report file
        """
        report_file = self.reports_dir / filename
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            self.logger.info(f"Saved report: {report_file}")
            
        except Exception as e:
            self.logger.error(f"Failed to save report: {e}")
    
    def clear_cache(self, older_than_hours: int = 24) -> int:
        """
        Clear old cache files.
        
        Args:
            older_than_hours: Remove cache files older than this many hours
            
        Returns:
            int: Number of files removed
        """
        # TODO: Implement cache cleanup
        # 1. Iterate through cache files
        # 2. Check file modification times
        # 3. Remove files older than specified time
        # 4. Return count of removed files
        
        removed_count = 0
        cutoff_time = datetime.now() - timedelta(hours=older_than_hours)
        
        try:
            for cache_file in self.cache_dir.glob("*.json"):
                file_time = datetime.fromtimestamp(cache_file.stat().st_mtime)
                if file_time < cutoff_time:
                    cache_file.unlink()
                    removed_count += 1
            
            self.logger.info(f"Cleared {removed_count} old cache files")
            return removed_count
            
        except Exception as e:
            self.logger.error(f"Failed to clear cache: {e}")
            return 0
    
    def get_storage_stats(self) -> Dict[str, Union[int, str]]:
        """
        Get statistics about stored data.
        
        Returns:
            dict: Storage statistics
        """
        # TODO: Implement storage statistics
        # 1. Count files in each directory
        # 2. Calculate total storage size
        # 3. Get oldest and newest file dates
        # 4. Return comprehensive statistics
        
        stats = {
            'cache_files': 0,
            'report_files': 0,
            'total_size_mb': 0.0,
            'oldest_cache': 'N/A',
            'newest_cache': 'N/A'
        }
        
        try:
            # Count cache files
            cache_files = list(self.cache_dir.glob("*.json"))
            stats['cache_files'] = len(cache_files)
            
            # Count report files
            report_files = list(self.reports_dir.glob("*"))
            stats['report_files'] = len(report_files)
            
            # TODO: Calculate total size and dates
            
        except Exception as e:
            self.logger.error(f"Failed to get storage stats: {e}")
        
        return stats