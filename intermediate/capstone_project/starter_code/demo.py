#!/usr/bin/env python3
"""
Demo script for the Weather Analyzer application.

This script demonstrates the key features and capabilities of the
weather analyzer system. It's designed to be run after the core
functionality has been implemented.
"""

import sys
import os
from datetime import datetime, timedelta

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from weather_analyzer.models.weather_data import WeatherData, WeatherCondition
from weather_analyzer.models.location import Location, Coordinates
from weather_analyzer.analysis.statistics import WeatherStatistics
from weather_analyzer.analysis.trends import TrendAnalyzer
from weather_analyzer.visualization.charts import ChartGenerator
from weather_analyzer.services.data_storage import DataStorage


def create_sample_weather_data():
    """Create sample weather data for demonstration."""
    print("Creating sample weather data...")
    
    base_time = datetime.now() - timedelta(days=7)
    weather_data = []
    
    # Create a week of sample weather data with some variation
    cities = ["London", "Paris", "Berlin", "Madrid"]
    
    for i in range(7):
        for j, city in enumerate(cities):
            # Create some realistic weather variation
            temp_base = 15 + j * 3  # Different base temps for different cities
            temp_variation = 5 * (0.5 - abs(0.5 - (i / 6)))  # Temperature curve
            
            weather = WeatherData(
                city=city,
                country="Europe",
                latitude=50.0 + j,
                longitude=0.0 + j * 2,
                timestamp=base_time + timedelta(days=i, hours=j),
                timezone_offset=3600,
                temperature=temp_base + temp_variation + (i - 3) * 0.5,
                feels_like=temp_base + temp_variation + (i - 3) * 0.5 + 2,
                temp_min=temp_base + temp_variation + (i - 3) * 0.5 - 3,
                temp_max=temp_base + temp_variation + (i - 3) * 0.5 + 5,
                pressure=1013 + (i - 3) * 2 + j,
                humidity=60 + (i * 3) % 40,
                wind_speed=3.0 + (i + j) % 8,
                condition=WeatherCondition.CLEAR if i % 3 == 0 else WeatherCondition.CLOUDS,
                description="clear sky" if i % 3 == 0 else "scattered clouds"
            )
            weather_data.append(weather)
    
    print(f"Created {len(weather_data)} sample weather data points")
    return weather_data


def demonstrate_models():
    """Demonstrate the data models."""
    print("\n" + "="*50)
    print("DEMONSTRATING DATA MODELS")
    print("="*50)
    
    # Demonstrate Coordinates
    print("\n1. Coordinates Model:")
    coords = Coordinates(51.5074, -0.1278)  # London
    print(f"   London coordinates: {coords}")
    
    # Demonstrate Location
    print("\n2. Location Model:")
    location = Location("London", "UK", coords)
    print(f"   Location: {location}")
    print(f"   Full name: {location.full_name}")
    
    # Demonstrate WeatherData
    print("\n3. Weather Data Model:")
    weather = WeatherData(
        city="London", country="UK", latitude=51.5074, longitude=-0.1278,
        timestamp=datetime.now(), timezone_offset=0,
        temperature=18.5, feels_like=20.0, temp_min=15.0, temp_max=22.0,
        pressure=1015.3, humidity=72, wind_speed=4.2,
        condition=WeatherCondition.CLOUDS, description="scattered clouds"
    )
    print(f"   Weather: {weather}")
    print(f"   Temperature in Fahrenheit: {weather.temperature_fahrenheit:.1f}°F")
    print(f"   Wind speed in mph: {weather.wind_speed_mph:.1f} mph")


def demonstrate_statistics(weather_data):
    """Demonstrate statistical analysis."""
    print("\n" + "="*50)
    print("DEMONSTRATING STATISTICAL ANALYSIS")
    print("="*50)
    
    stats = WeatherStatistics()
    
    # Temperature statistics
    print("\n1. Temperature Statistics:")
    temp_stats = stats.calculate_temperature_stats(weather_data)
    if temp_stats:
        print(f"   Mean temperature: {temp_stats.get('mean', 0):.1f}°C")
        print(f"   Min temperature: {temp_stats.get('min', 0):.1f}°C")
        print(f"   Max temperature: {temp_stats.get('max', 0):.1f}°C")
        print(f"   Standard deviation: {temp_stats.get('std_dev', 0):.1f}°C")
        print(f"   Data points: {temp_stats.get('count', 0)}")
    
    # Comprehensive statistics
    print("\n2. Comprehensive Statistics:")
    comprehensive_stats = stats.calculate_comprehensive_stats(weather_data)
    for param, param_stats in comprehensive_stats.items():
        if param_stats:
            print(f"   {param.title()}:")
            print(f"     Mean: {param_stats.get('mean', 0):.1f}")
            print(f"     Range: {param_stats.get('min', 0):.1f} - {param_stats.get('max', 0):.1f}")


def demonstrate_trends(weather_data):
    """Demonstrate trend analysis."""
    print("\n" + "="*50)
    print("DEMONSTRATING TREND ANALYSIS")
    print("="*50)
    
    trend_analyzer = TrendAnalyzer()
    
    # Temperature trend
    print("\n1. Temperature Trend Analysis:")
    temp_trend = trend_analyzer.analyze_temperature_trend(weather_data)
    print(f"   Trend direction: {temp_trend['trend'].value}")
    print(f"   Confidence: {temp_trend['confidence']:.2f}")
    print(f"   Total change: {temp_trend['total_change']:.1f}°C")
    print(f"   Start temperature: {temp_trend['start_temp']:.1f}°C")
    print(f"   End temperature: {temp_trend['end_temp']:.1f}°C")
    
    # Weather patterns
    print("\n2. Weather Pattern Detection:")
    patterns = trend_analyzer.detect_weather_patterns(weather_data)
    print(f"   Daily cycles detected: {len(patterns['daily_cycles'])}")
    print(f"   Weekly patterns detected: {len(patterns['weekly_patterns'])}")
    print(f"   Seasonal patterns detected: {len(patterns['seasonal_patterns'])}")


def demonstrate_visualization(weather_data):
    """Demonstrate visualization capabilities."""
    print("\n" + "="*50)
    print("DEMONSTRATING VISUALIZATION")
    print("="*50)
    
    chart_gen = ChartGenerator()
    
    # Temperature line chart
    print("\n1. Temperature Line Chart:")
    temp_chart = chart_gen.create_temperature_line_chart(weather_data[:10])
    print(temp_chart)
    
    # Weather summary table
    print("\n2. Weather Summary Table:")
    summary_table = chart_gen.create_weather_summary_table(weather_data[:5])
    print(summary_table)
    
    # Trend visualization
    print("\n3. Trend Visualization:")
    trend_viz = chart_gen.create_trend_visualization(weather_data[:10])
    print(trend_viz)


def demonstrate_data_storage(weather_data):
    """Demonstrate data storage capabilities."""
    print("\n" + "="*50)
    print("DEMONSTRATING DATA STORAGE")
    print("="*50)
    
    storage = DataStorage("demo_data")
    
    # Save a report
    print("\n1. Saving Weather Report:")
    report_content = f"""
Weather Analysis Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Total data points analyzed: {len(weather_data)}
Temperature range: {min(w.temperature for w in weather_data):.1f}°C to {max(w.temperature for w in weather_data):.1f}°C
Cities covered: {len(set(w.city for w in weather_data))}

This is a sample report demonstrating the weather analyzer capabilities.
"""
    
    storage.save_report(report_content, "demo_report.txt")
    print("   Report saved to demo_data/reports/demo_report.txt")
    
    # Storage statistics
    print("\n2. Storage Statistics:")
    stats = storage.get_storage_stats()
    print(f"   Cache files: {stats['cache_files']}")
    print(f"   Report files: {stats['report_files']}")
    print(f"   Total size: {stats['total_size_mb']:.2f} MB")


def demonstrate_error_handling():
    """Demonstrate error handling capabilities."""
    print("\n" + "="*50)
    print("DEMONSTRATING ERROR HANDLING")
    print("="*50)
    
    # Invalid coordinates
    print("\n1. Invalid Coordinates Handling:")
    try:
        invalid_coords = Coordinates(91.0, 0.0)  # Invalid latitude
    except ValueError as e:
        print(f"   Caught error: {e}")
    
    # Empty location name
    print("\n2. Empty Location Name Handling:")
    try:
        coords = Coordinates(0.0, 0.0)
        invalid_location = Location("", "Country", coords)
    except ValueError as e:
        print(f"   Caught error: {e}")
    
    # Statistics with empty data
    print("\n3. Statistics with Empty Data:")
    stats = WeatherStatistics()
    empty_stats = stats.calculate_temperature_stats([])
    print(f"   Empty data result: {empty_stats}")


def main():
    """Main demonstration function."""
    print("WEATHER ANALYZER DEMONSTRATION")
    print("=" * 60)
    print("This demo showcases the key features of the Weather Analyzer application.")
    print("Note: Some features are placeholder implementations and will be completed")
    print("as you work through the project tasks.")
    
    try:
        # Create sample data
        weather_data = create_sample_weather_data()
        
        # Demonstrate each component
        demonstrate_models()
        demonstrate_statistics(weather_data)
        demonstrate_trends(weather_data)
        demonstrate_visualization(weather_data)
        demonstrate_data_storage(weather_data)
        demonstrate_error_handling()
        
        print("\n" + "="*60)
        print("DEMONSTRATION COMPLETE")
        print("="*60)
        print("Next steps:")
        print("1. Get your OpenWeatherMap API key")
        print("2. Create a .env file with your API key")
        print("3. Start implementing the TODO items in the code")
        print("4. Run the tests: pytest")
        print("5. Use the main application: python -m weather_analyzer")
        
    except Exception as e:
        print(f"\nError during demonstration: {e}")
        print("This is expected since many features are not yet implemented.")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())