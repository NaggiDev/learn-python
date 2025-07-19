"""
Complete implementation of statistical analysis for weather data.
This reference solution shows proper statistical calculations and data analysis.
"""

import statistics
import math
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import logging

from weather_analyzer.models.weather_data import WeatherData


class WeatherStatistics:
    """
    Complete implementation of weather statistics calculator.
    
    This class demonstrates proper statistical analysis techniques
    applied to weather data, including descriptive statistics,
    anomaly detection, and comparative analysis.
    """
    
    def __init__(self):
        """Initialize the weather statistics calculator."""
        self.logger = logging.getLogger(__name__)
    
    def calculate_temperature_stats(self, weather_data: List[WeatherData]) -> Dict[str, float]:
        """
        Calculate comprehensive temperature statistics.
        
        This implementation shows proper statistical calculations
        with error handling and edge case management.
        """
        if not weather_data:
            self.logger.warning("No weather data provided for temperature statistics")
            return {}
        
        temperatures = [data.temperature for data in weather_data]
        
        try:
            stats = {
                'mean': statistics.mean(temperatures),
                'median': statistics.median(temperatures),
                'mode': self._safe_mode(temperatures),
                'min': min(temperatures),
                'max': max(temperatures),
                'range': max(temperatures) - min(temperatures),
                'std_dev': statistics.stdev(temperatures) if len(temperatures) > 1 else 0.0,
                'variance': statistics.variance(temperatures) if len(temperatures) > 1 else 0.0,
                'count': len(temperatures),
                'q1': self._calculate_percentile(temperatures, 25),
                'q3': self._calculate_percentile(temperatures, 75),
                'iqr': self._calculate_percentile(temperatures, 75) - self._calculate_percentile(temperatures, 25)
            }
            
            # Add coefficient of variation
            if stats['mean'] != 0:
                stats['cv'] = stats['std_dev'] / abs(stats['mean'])
            else:
                stats['cv'] = 0.0
            
            self.logger.debug(f"Calculated temperature stats for {len(temperatures)} data points")
            return stats
            
        except Exception as e:
            self.logger.error(f"Error calculating temperature stats: {e}")
            return {}
    
    def calculate_humidity_stats(self, weather_data: List[WeatherData]) -> Dict[str, float]:
        """Calculate comprehensive humidity statistics."""
        if not weather_data:
            return {}
        
        humidity_values = [data.humidity for data in weather_data]
        
        try:
            stats = {
                'mean': statistics.mean(humidity_values),
                'median': statistics.median(humidity_values),
                'min': min(humidity_values),
                'max': max(humidity_values),
                'range': max(humidity_values) - min(humidity_values),
                'std_dev': statistics.stdev(humidity_values) if len(humidity_values) > 1 else 0.0,
                'count': len(humidity_values)
            }
            
            # Humidity-specific analysis
            stats['dry_days'] = sum(1 for h in humidity_values if h < 30)
            stats['humid_days'] = sum(1 for h in humidity_values if h > 70)
            stats['comfortable_days'] = sum(1 for h in humidity_values if 30 <= h <= 70)
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Error calculating humidity stats: {e}")
            return {}
    
    def calculate_pressure_stats(self, weather_data: List[WeatherData]) -> Dict[str, float]:
        """Calculate atmospheric pressure statistics."""
        if not weather_data:
            return {}
        
        pressure_values = [data.pressure for data in weather_data]
        
        try:
            stats = {
                'mean': statistics.mean(pressure_values),
                'median': statistics.median(pressure_values),
                'min': min(pressure_values),
                'max': max(pressure_values),
                'range': max(pressure_values) - min(pressure_values),
                'std_dev': statistics.stdev(pressure_values) if len(pressure_values) > 1 else 0.0,
                'count': len(pressure_values)
            }
            
            # Pressure-specific analysis
            normal_pressure = 1013.25  # Standard atmospheric pressure
            stats['above_normal'] = sum(1 for p in pressure_values if p > normal_pressure)
            stats['below_normal'] = sum(1 for p in pressure_values if p < normal_pressure)
            stats['pressure_trend'] = self._calculate_pressure_trend(weather_data)
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Error calculating pressure stats: {e}")
            return {}
    
    def calculate_wind_stats(self, weather_data: List[WeatherData]) -> Dict[str, float]:
        """
        Calculate wind statistics including speed and direction analysis.
        
        This implementation shows how to handle circular statistics
        for wind direction data.
        """
        if not weather_data:
            return {}
        
        wind_speeds = [data.wind_speed for data in weather_data]
        wind_directions = [data.wind_direction for data in weather_data if data.wind_direction is not None]
        
        try:
            stats = {
                'speed_mean': statistics.mean(wind_speeds),
                'speed_median': statistics.median(wind_speeds),
                'speed_min': min(wind_speeds),
                'speed_max': max(wind_speeds),
                'speed_std_dev': statistics.stdev(wind_speeds) if len(wind_speeds) > 1 else 0.0,
                'count': len(wind_speeds)
            }
            
            # Wind speed categories (Beaufort scale)
            stats['calm_days'] = sum(1 for ws in wind_speeds if ws < 0.3)
            stats['light_breeze'] = sum(1 for ws in wind_speeds if 0.3 <= ws < 3.4)
            stats['moderate_breeze'] = sum(1 for ws in wind_speeds if 3.4 <= ws < 8.0)
            stats['strong_wind'] = sum(1 for ws in wind_speeds if ws >= 8.0)
            
            # Wind direction analysis (circular statistics)
            if wind_directions:
                stats['direction_mean'] = self._calculate_mean_wind_direction(wind_directions)
                stats['direction_consistency'] = self._calculate_wind_direction_consistency(wind_directions)
                stats['prevailing_direction'] = self._get_prevailing_wind_direction(wind_directions)
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Error calculating wind stats: {e}")
            return {}
    
    def calculate_comprehensive_stats(self, weather_data: List[WeatherData]) -> Dict[str, Dict[str, float]]:
        """Calculate comprehensive statistics for all weather parameters."""
        if not weather_data:
            return {}
        
        return {
            'temperature': self.calculate_temperature_stats(weather_data),
            'humidity': self.calculate_humidity_stats(weather_data),
            'pressure': self.calculate_pressure_stats(weather_data),
            'wind': self.calculate_wind_stats(weather_data)
        }
    
    def find_extreme_values(self, weather_data: List[WeatherData]) -> Dict[str, Dict[str, any]]:
        """
        Find extreme weather values and their occurrences.
        
        This implementation shows how to identify and report
        extreme weather events with context.
        """
        if not weather_data:
            return {}
        
        # Sort data by different parameters to find extremes
        temp_sorted = sorted(weather_data, key=lambda x: x.temperature)
        wind_sorted = sorted(weather_data, key=lambda x: x.wind_speed, reverse=True)
        pressure_sorted = sorted(weather_data, key=lambda x: x.pressure)
        humidity_sorted = sorted(weather_data, key=lambda x: x.humidity)
        
        extremes = {
            'temperature': {
                'highest': {
                    'value': temp_sorted[-1].temperature,
                    'date': temp_sorted[-1].timestamp,
                    'location': f"{temp_sorted[-1].city}, {temp_sorted[-1].country}"
                },
                'lowest': {
                    'value': temp_sorted[0].temperature,
                    'date': temp_sorted[0].timestamp,
                    'location': f"{temp_sorted[0].city}, {temp_sorted[0].country}"
                }
            },
            'wind_speed': {
                'highest': {
                    'value': wind_sorted[0].wind_speed,
                    'date': wind_sorted[0].timestamp,
                    'location': f"{wind_sorted[0].city}, {wind_sorted[0].country}"
                }
            },
            'pressure': {
                'highest': {
                    'value': pressure_sorted[-1].pressure,
                    'date': pressure_sorted[-1].timestamp,
                    'location': f"{pressure_sorted[-1].city}, {pressure_sorted[-1].country}"
                },
                'lowest': {
                    'value': pressure_sorted[0].pressure,
                    'date': pressure_sorted[0].timestamp,
                    'location': f"{pressure_sorted[0].city}, {pressure_sorted[0].country}"
                }
            },
            'humidity': {
                'highest': {
                    'value': humidity_sorted[-1].humidity,
                    'date': humidity_sorted[-1].timestamp,
                    'location': f"{humidity_sorted[-1].city}, {humidity_sorted[-1].country}"
                },
                'lowest': {
                    'value': humidity_sorted[0].humidity,
                    'date': humidity_sorted[0].timestamp,
                    'location': f"{humidity_sorted[0].city}, {humidity_sorted[0].country}"
                }
            }
        }
        
        return extremes
    
    def calculate_comfort_index_distribution(self, weather_data: List[WeatherData]) -> Dict[str, int]:
        """
        Calculate the distribution of comfort index values.
        
        This implementation shows how to create custom comfort metrics
        based on multiple weather parameters.
        """
        if not weather_data:
            return {}
        
        distribution = {
            'Very Comfortable': 0,
            'Comfortable': 0,
            'Uncomfortable': 0,
            'Very Uncomfortable': 0
        }
        
        for data in weather_data:
            comfort_level = self._calculate_comfort_index(data)
            distribution[comfort_level] += 1
        
        return distribution
    
    def _calculate_comfort_index(self, weather_data: WeatherData) -> str:
        """
        Calculate comfort index based on temperature, humidity, and wind.
        
        This is a simplified comfort index calculation.
        """
        temp = weather_data.temperature
        humidity = weather_data.humidity
        wind_speed = weather_data.wind_speed
        
        # Temperature comfort (optimal around 20-25°C)
        temp_score = 0
        if 18 <= temp <= 26:
            temp_score = 2
        elif 15 <= temp < 18 or 26 < temp <= 30:
            temp_score = 1
        elif 10 <= temp < 15 or 30 < temp <= 35:
            temp_score = -1
        else:
            temp_score = -2
        
        # Humidity comfort (optimal 40-60%)
        humidity_score = 0
        if 40 <= humidity <= 60:
            humidity_score = 1
        elif 30 <= humidity < 40 or 60 < humidity <= 70:
            humidity_score = 0
        else:
            humidity_score = -1
        
        # Wind comfort (light breeze is pleasant)
        wind_score = 0
        if 1 <= wind_speed <= 5:
            wind_score = 1
        elif wind_speed > 10:
            wind_score = -1
        
        total_score = temp_score + humidity_score + wind_score
        
        if total_score >= 3:
            return 'Very Comfortable'
        elif total_score >= 1:
            return 'Comfortable'
        elif total_score >= -1:
            return 'Uncomfortable'
        else:
            return 'Very Uncomfortable'
    
    def compare_locations(self, location_data: Dict[str, List[WeatherData]]) -> Dict[str, Dict[str, float]]:
        """
        Compare weather statistics across multiple locations.
        
        This implementation shows how to perform comparative analysis
        and identify significant differences between locations.
        """
        if not location_data:
            return {}
        
        comparison = {}
        
        for location, data in location_data.items():
            comparison[location] = self.calculate_comprehensive_stats(data)
        
        # Add comparative metrics
        if len(location_data) > 1:
            comparison['_comparison'] = self._calculate_location_differences(comparison)
        
        return comparison
    
    def _calculate_location_differences(self, location_stats: Dict) -> Dict:
        """Calculate differences between locations for comparison."""
        differences = {}
        
        # Get all locations (excluding comparison data)
        locations = [loc for loc in location_stats.keys() if not loc.startswith('_')]
        
        if len(locations) >= 2:
            # Compare temperature differences
            temp_means = []
            for loc in locations:
                temp_stats = location_stats[loc].get('temperature', {})
                if temp_stats:
                    temp_means.append((loc, temp_stats.get('mean', 0)))
            
            if len(temp_means) >= 2:
                temp_means.sort(key=lambda x: x[1])
                differences['temperature_range'] = {
                    'coldest_location': temp_means[0][0],
                    'coldest_temp': temp_means[0][1],
                    'warmest_location': temp_means[-1][0],
                    'warmest_temp': temp_means[-1][1],
                    'difference': temp_means[-1][1] - temp_means[0][1]
                }
        
        return differences
    
    def detect_anomalies(self, weather_data: List[WeatherData], 
                        threshold_std_dev: float = 2.0) -> List[WeatherData]:
        """
        Detect anomalous weather readings using statistical methods.
        
        This implementation uses the standard deviation method
        to identify outliers in weather data.
        """
        if not weather_data or len(weather_data) < 3:
            return []
        
        anomalies = []
        
        # Calculate statistics for each parameter
        temperatures = [data.temperature for data in weather_data]
        temp_mean = statistics.mean(temperatures)
        temp_std = statistics.stdev(temperatures)
        
        pressures = [data.pressure for data in weather_data]
        pressure_mean = statistics.mean(pressures)
        pressure_std = statistics.stdev(pressures)
        
        wind_speeds = [data.wind_speed for data in weather_data]
        wind_mean = statistics.mean(wind_speeds)
        wind_std = statistics.stdev(wind_speeds)
        
        # Check each data point for anomalies
        for data in weather_data:
            is_anomaly = False
            
            # Temperature anomaly
            temp_z_score = abs(data.temperature - temp_mean) / temp_std if temp_std > 0 else 0
            if temp_z_score > threshold_std_dev:
                is_anomaly = True
            
            # Pressure anomaly
            pressure_z_score = abs(data.pressure - pressure_mean) / pressure_std if pressure_std > 0 else 0
            if pressure_z_score > threshold_std_dev:
                is_anomaly = True
            
            # Wind speed anomaly
            wind_z_score = abs(data.wind_speed - wind_mean) / wind_std if wind_std > 0 else 0
            if wind_z_score > threshold_std_dev:
                is_anomaly = True
            
            if is_anomaly:
                anomalies.append(data)
        
        self.logger.info(f"Detected {len(anomalies)} anomalous readings out of {len(weather_data)} total")
        return anomalies
    
    # Helper methods
    
    def _safe_mode(self, values: List[float]) -> Optional[float]:
        """Safely calculate mode, handling cases where no mode exists."""
        try:
            return statistics.mode(values)
        except statistics.StatisticsError:
            return None
    
    def _calculate_percentile(self, values: List[float], percentile: float) -> float:
        """Calculate percentile value."""
        sorted_values = sorted(values)
        index = (percentile / 100) * (len(sorted_values) - 1)
        
        if index.is_integer():
            return sorted_values[int(index)]
        else:
            lower_index = int(index)
            upper_index = lower_index + 1
            weight = index - lower_index
            return sorted_values[lower_index] * (1 - weight) + sorted_values[upper_index] * weight
    
    def _calculate_pressure_trend(self, weather_data: List[WeatherData]) -> str:
        """Calculate overall pressure trend."""
        if len(weather_data) < 2:
            return 'stable'
        
        sorted_data = sorted(weather_data, key=lambda x: x.timestamp)
        first_half = sorted_data[:len(sorted_data)//2]
        second_half = sorted_data[len(sorted_data)//2:]
        
        first_avg = statistics.mean([d.pressure for d in first_half])
        second_avg = statistics.mean([d.pressure for d in second_half])
        
        difference = second_avg - first_avg
        
        if difference > 2:
            return 'rising'
        elif difference < -2:
            return 'falling'
        else:
            return 'stable'
    
    def _calculate_mean_wind_direction(self, directions: List[int]) -> float:
        """Calculate mean wind direction using circular statistics."""
        # Convert degrees to radians
        radians = [math.radians(d) for d in directions]
        
        # Calculate mean of sine and cosine components
        sin_sum = sum(math.sin(r) for r in radians)
        cos_sum = sum(math.cos(r) for r in radians)
        
        # Calculate mean direction
        mean_direction = math.atan2(sin_sum, cos_sum)
        
        # Convert back to degrees and normalize to 0-360
        mean_degrees = math.degrees(mean_direction)
        if mean_degrees < 0:
            mean_degrees += 360
        
        return mean_degrees
    
    def _calculate_wind_direction_consistency(self, directions: List[int]) -> float:
        """Calculate wind direction consistency (0 = highly variable, 1 = consistent)."""
        if not directions:
            return 0.0
        
        # Convert to radians and calculate vector components
        radians = [math.radians(d) for d in directions]
        sin_sum = sum(math.sin(r) for r in radians)
        cos_sum = sum(math.cos(r) for r in radians)
        
        # Calculate resultant vector length
        resultant_length = math.sqrt(sin_sum**2 + cos_sum**2)
        
        # Normalize by number of observations
        consistency = resultant_length / len(directions)
        
        return consistency
    
    def _get_prevailing_wind_direction(self, directions: List[int]) -> str:
        """Get the prevailing wind direction as a compass direction."""
        if not directions:
            return 'Variable'
        
        mean_direction = self._calculate_mean_wind_direction(directions)
        
        # Convert to compass direction
        compass_directions = [
            'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
            'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'
        ]
        
        index = round(mean_direction / 22.5) % 16
        return compass_directions[index]