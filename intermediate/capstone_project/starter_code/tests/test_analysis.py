"""
Unit tests for analysis modules.
"""

import pytest
from datetime import datetime, timedelta
from weather_analyzer.analysis.statistics import WeatherStatistics
from weather_analyzer.analysis.trends import TrendAnalyzer, TrendDirection
from weather_analyzer.models.weather_data import WeatherData, WeatherCondition


class TestWeatherStatistics:
    """Test cases for the WeatherStatistics class."""
    
    @pytest.fixture
    def weather_stats(self):
        """Fixture providing weather statistics instance."""
        return WeatherStatistics()
    
    @pytest.fixture
    def sample_weather_data(self):
        """Fixture providing sample weather data for testing."""
        base_time = datetime.now()
        return [
            WeatherData(
                city="Test", country="Test", latitude=0, longitude=0,
                timestamp=base_time, timezone_offset=0,
                temperature=20.0, feels_like=22.0, temp_min=18.0, temp_max=25.0,
                pressure=1013.25, humidity=65, wind_speed=3.5,
                condition=WeatherCondition.CLEAR, description="clear sky"
            ),
            WeatherData(
                city="Test", country="Test", latitude=0, longitude=0,
                timestamp=base_time + timedelta(hours=1), timezone_offset=0,
                temperature=22.5, feels_like=24.0, temp_min=20.0, temp_max=27.0,
                pressure=1012.0, humidity=60, wind_speed=4.2,
                condition=WeatherCondition.CLOUDS, description="few clouds"
            ),
            WeatherData(
                city="Test", country="Test", latitude=0, longitude=0,
                timestamp=base_time + timedelta(hours=2), timezone_offset=0,
                temperature=18.5, feels_like=19.0, temp_min=16.0, temp_max=22.0,
                pressure=1015.5, humidity=75, wind_speed=2.8,
                condition=WeatherCondition.RAIN, description="light rain"
            )
        ]
    
    def test_temperature_stats_calculation(self, weather_stats, sample_weather_data):
        """Test temperature statistics calculation."""
        stats = weather_stats.calculate_temperature_stats(sample_weather_data)
        
        assert isinstance(stats, dict)
        assert 'mean' in stats
        assert 'median' in stats
        assert 'min' in stats
        assert 'max' in stats
        assert 'std_dev' in stats
        assert 'count' in stats
        
        # Check specific values
        temperatures = [20.0, 22.5, 18.5]
        assert stats['mean'] == sum(temperatures) / len(temperatures)
        assert stats['min'] == min(temperatures)
        assert stats['max'] == max(temperatures)
        assert stats['count'] == len(temperatures)
    
    def test_temperature_stats_empty_data(self, weather_stats):
        """Test temperature statistics with empty data."""
        stats = weather_stats.calculate_temperature_stats([])
        assert stats == {}
    
    def test_temperature_stats_single_data_point(self, weather_stats):
        """Test temperature statistics with single data point."""
        single_data = [WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=datetime.now(), timezone_offset=0,
            temperature=25.0, feels_like=27.0, temp_min=23.0, temp_max=28.0,
            pressure=1010.0, humidity=50, wind_speed=1.5,
            condition=WeatherCondition.CLEAR, description="clear"
        )]
        
        stats = weather_stats.calculate_temperature_stats(single_data)
        
        assert stats['mean'] == 25.0
        assert stats['min'] == 25.0
        assert stats['max'] == 25.0
        assert stats['std_dev'] == 0.0  # No deviation with single point
        assert stats['count'] == 1
    
    def test_comprehensive_stats(self, weather_stats, sample_weather_data):
        """Test comprehensive statistics calculation."""
        stats = weather_stats.calculate_comprehensive_stats(sample_weather_data)
        
        assert isinstance(stats, dict)
        assert 'temperature' in stats
        assert 'humidity' in stats
        assert 'pressure' in stats
        assert 'wind' in stats
        
        # Temperature stats should be populated
        temp_stats = stats['temperature']
        assert 'mean' in temp_stats
        assert temp_stats['count'] == 3
    
    def test_comprehensive_stats_empty_data(self, weather_stats):
        """Test comprehensive statistics with empty data."""
        stats = weather_stats.calculate_comprehensive_stats([])
        assert stats == {}
    
    def test_extreme_values_detection(self, weather_stats, sample_weather_data):
        """Test extreme values detection."""
        extremes = weather_stats.find_extreme_values(sample_weather_data)
        
        assert isinstance(extremes, dict)
        assert 'temperature' in extremes
        assert 'wind_speed' in extremes
        assert 'pressure' in extremes
        
        # TODO: Add more specific assertions once method is implemented
    
    def test_comfort_index_distribution(self, weather_stats, sample_weather_data):
        """Test comfort index distribution calculation."""
        distribution = weather_stats.calculate_comfort_index_distribution(sample_weather_data)
        
        assert isinstance(distribution, dict)
        assert 'Very Comfortable' in distribution
        assert 'Comfortable' in distribution
        assert 'Uncomfortable' in distribution
        assert 'Very Uncomfortable' in distribution
        
        # All values should be integers (counts)
        for count in distribution.values():
            assert isinstance(count, int)
            assert count >= 0
    
    def test_location_comparison(self, weather_stats, sample_weather_data):
        """Test location comparison functionality."""
        location_data = {
            'London': sample_weather_data[:2],
            'Paris': sample_weather_data[1:]
        }
        
        comparison = weather_stats.compare_locations(location_data)
        
        assert isinstance(comparison, dict)
        assert 'London' in comparison
        assert 'Paris' in comparison
        
        # Each location should have comprehensive stats
        for location_stats in comparison.values():
            assert 'temperature' in location_stats
    
    def test_anomaly_detection_insufficient_data(self, weather_stats):
        """Test anomaly detection with insufficient data."""
        # Less than 3 data points
        limited_data = [WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=datetime.now(), timezone_offset=0,
            temperature=20.0, feels_like=22.0, temp_min=18.0, temp_max=25.0,
            pressure=1013.25, humidity=65, wind_speed=3.5,
            condition=WeatherCondition.CLEAR, description="clear"
        )]
        
        anomalies = weather_stats.detect_anomalies(limited_data)
        assert anomalies == []


class TestTrendAnalyzer:
    """Test cases for the TrendAnalyzer class."""
    
    @pytest.fixture
    def trend_analyzer(self):
        """Fixture providing trend analyzer instance."""
        return TrendAnalyzer()
    
    @pytest.fixture
    def trending_weather_data(self):
        """Fixture providing weather data with clear trend."""
        base_time = datetime.now()
        data = []
        
        # Create data with increasing temperature trend
        for i in range(5):
            data.append(WeatherData(
                city="Test", country="Test", latitude=0, longitude=0,
                timestamp=base_time + timedelta(hours=i),
                timezone_offset=0,
                temperature=15.0 + i * 2.0,  # Increasing by 2°C each hour
                feels_like=17.0 + i * 2.0,
                temp_min=13.0 + i * 2.0,
                temp_max=18.0 + i * 2.0,
                pressure=1013.0 - i * 0.5,  # Slightly decreasing pressure
                humidity=70 - i * 2,  # Decreasing humidity
                wind_speed=3.0 + i * 0.5,  # Increasing wind
                condition=WeatherCondition.CLEAR,
                description="clear"
            ))
        
        return data
    
    def test_temperature_trend_analysis(self, trend_analyzer, trending_weather_data):
        """Test temperature trend analysis."""
        trend_result = trend_analyzer.analyze_temperature_trend(trending_weather_data)
        
        assert isinstance(trend_result, dict)
        assert 'trend' in trend_result
        assert 'confidence' in trend_result
        assert 'rate_of_change' in trend_result
        assert 'start_temp' in trend_result
        assert 'end_temp' in trend_result
        assert 'total_change' in trend_result
        
        # Check that trend direction is detected
        assert isinstance(trend_result['trend'], TrendDirection)
        assert isinstance(trend_result['confidence'], float)
        
        # Start and end temperatures should match our test data
        assert trend_result['start_temp'] == 15.0
        assert trend_result['end_temp'] == 23.0  # 15 + 4*2
        assert trend_result['total_change'] == 8.0  # 23 - 15
    
    def test_temperature_trend_insufficient_data(self, trend_analyzer):
        """Test temperature trend analysis with insufficient data."""
        single_data = [WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=datetime.now(), timezone_offset=0,
            temperature=20.0, feels_like=22.0, temp_min=18.0, temp_max=25.0,
            pressure=1013.25, humidity=65, wind_speed=3.5,
            condition=WeatherCondition.CLEAR, description="clear"
        )]
        
        trend_result = trend_analyzer.analyze_temperature_trend(single_data)
        
        assert trend_result['trend'] == TrendDirection.STABLE
        assert trend_result['confidence'] == 0.0
    
    def test_moving_average_calculation(self, trend_analyzer, trending_weather_data):
        """Test moving average calculation."""
        moving_avg = trend_analyzer.calculate_moving_average(
            trending_weather_data, window_size=3, parameter='temperature'
        )
        
        # Should return empty list until implemented
        # TODO: Update this test once moving average is implemented
        assert isinstance(moving_avg, list)
    
    def test_moving_average_insufficient_data(self, trend_analyzer):
        """Test moving average with insufficient data."""
        limited_data = [WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=datetime.now(), timezone_offset=0,
            temperature=20.0, feels_like=22.0, temp_min=18.0, temp_max=25.0,
            pressure=1013.25, humidity=65, wind_speed=3.5,
            condition=WeatherCondition.CLEAR, description="clear"
        )]
        
        moving_avg = trend_analyzer.calculate_moving_average(
            limited_data, window_size=3, parameter='temperature'
        )
        
        assert moving_avg == []
    
    def test_weather_pattern_detection(self, trend_analyzer, trending_weather_data):
        """Test weather pattern detection."""
        patterns = trend_analyzer.detect_weather_patterns(trending_weather_data)
        
        assert isinstance(patterns, dict)
        assert 'daily_cycles' in patterns
        assert 'weekly_patterns' in patterns
        assert 'seasonal_patterns' in patterns
        assert 'correlation_patterns' in patterns
        
        # All pattern lists should be lists
        for pattern_list in patterns.values():
            assert isinstance(pattern_list, list)
    
    def test_pattern_detection_insufficient_data(self, trend_analyzer):
        """Test pattern detection with insufficient data."""
        limited_data = []  # Less than 7 days
        
        patterns = trend_analyzer.detect_weather_patterns(limited_data)
        
        # Should return empty patterns
        for pattern_list in patterns.values():
            assert pattern_list == []
    
    def test_precipitation_pattern_analysis(self, trend_analyzer, trending_weather_data):
        """Test precipitation pattern analysis."""
        analysis = trend_analyzer.analyze_precipitation_patterns(trending_weather_data)
        
        assert isinstance(analysis, dict)
        assert 'total_precipitation_days' in analysis
        assert 'dry_days' in analysis
        assert 'precipitation_frequency' in analysis
        
        # All values should be numeric
        for key, value in analysis.items():
            if key in ['total_precipitation_days', 'dry_days', 'longest_dry_spell', 'longest_wet_spell']:
                assert isinstance(value, int)
            else:
                assert isinstance(value, (int, float))
    
    def test_time_period_comparison(self, trend_analyzer, trending_weather_data):
        """Test time period comparison."""
        period1 = trending_weather_data[:3]
        period2 = trending_weather_data[2:]
        
        comparison = trend_analyzer.compare_time_periods(period1, period2)
        
        assert isinstance(comparison, dict)
        assert 'temperature' in comparison
        assert 'humidity' in comparison
        assert 'pressure' in comparison
        
        # Each parameter should have comparison metrics
        for param_comparison in comparison.values():
            assert 'period1_avg' in param_comparison
            assert 'period2_avg' in param_comparison
            assert 'difference' in param_comparison
            assert 'percent_change' in param_comparison
    
    def test_simple_trend_forecast(self, trend_analyzer, trending_weather_data):
        """Test simple trend-based forecasting."""
        forecast = trend_analyzer.forecast_simple_trend(trending_weather_data, days_ahead=2)
        
        assert isinstance(forecast, list)
        # TODO: Add more specific assertions once method is implemented
    
    def test_forecast_insufficient_data(self, trend_analyzer):
        """Test forecasting with insufficient data."""
        limited_data = []  # Less than 3 data points
        
        forecast = trend_analyzer.forecast_simple_trend(limited_data)
        assert forecast == []
    
    def test_extreme_weather_event_detection(self, trend_analyzer, trending_weather_data):
        """Test extreme weather event detection."""
        events = trend_analyzer.identify_extreme_weather_events(trending_weather_data)
        
        assert isinstance(events, list)
        # TODO: Add more specific assertions once method is implemented
    
    def test_weather_volatility_calculation(self, trend_analyzer, trending_weather_data):
        """Test weather volatility calculation."""
        volatility = trend_analyzer.calculate_weather_volatility(
            trending_weather_data, parameter='temperature'
        )
        
        assert isinstance(volatility, float)
        assert volatility >= 0.0
    
    def test_volatility_insufficient_data(self, trend_analyzer):
        """Test volatility calculation with insufficient data."""
        single_data = [WeatherData(
            city="Test", country="Test", latitude=0, longitude=0,
            timestamp=datetime.now(), timezone_offset=0,
            temperature=20.0, feels_like=22.0, temp_min=18.0, temp_max=25.0,
            pressure=1013.25, humidity=65, wind_speed=3.5,
            condition=WeatherCondition.CLEAR, description="clear"
        )]
        
        volatility = trend_analyzer.calculate_weather_volatility(single_data)
        assert volatility == 0.0
    
    def test_volatility_invalid_parameter(self, trend_analyzer, trending_weather_data):
        """Test volatility calculation with invalid parameter."""
        volatility = trend_analyzer.calculate_weather_volatility(
            trending_weather_data, parameter='invalid_param'
        )
        
        assert volatility == 0.0