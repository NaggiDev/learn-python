"""
Chart generation functions for weather data visualization.
"""

import logging
from typing import Dict, List, Optional, Tuple
from datetime import datetime

from weather_analyzer.models.weather_data import WeatherData


class ChartGenerator:
    """
    Class for generating text-based charts and visualizations.
    
    This class provides methods for creating various types of charts
    and visualizations that can be displayed in a terminal or saved
    to text files.
    """
    
    def __init__(self, width: int = 80, height: int = 20):
        """
        Initialize the chart generator.
        
        Args:
            width: Default width for charts in characters
            height: Default height for charts in characters
        """
        self.width = width
        self.height = height
        self.logger = logging.getLogger(__name__)
    
    def create_temperature_line_chart(self, weather_data: List[WeatherData], 
                                    title: str = "Temperature Over Time") -> str:
        """
        Create a text-based line chart for temperature data.
        
        Args:
            weather_data: List of weather data points
            title: Chart title
            
        Returns:
            str: ASCII line chart
        """
        # TODO: Implement temperature line chart
        # 1. Sort data by timestamp
        # 2. Extract temperature values
        # 3. Scale values to fit chart dimensions
        # 4. Create ASCII line chart
        # 5. Add axis labels and title
        
        if not weather_data:
            return "No data available for chart"
        
        # Sort data by timestamp
        sorted_data = sorted(weather_data, key=lambda x: x.timestamp)
        temperatures = [data.temperature for data in sorted_data]
        
        # Placeholder implementation
        chart_lines = [
            f" {title}",
            f" {'=' * len(title)}",
            "",
            " TODO: Implement temperature line chart",
            f" Data points: {len(temperatures)}",
            f" Temperature range: {min(temperatures):.1f}°C to {max(temperatures):.1f}°C",
            ""
        ]
        
        return "\n".join(chart_lines)
    
    def create_bar_chart(self, data: Dict[str, float], title: str = "Bar Chart", 
                        unit: str = "") -> str:
        """
        Create a horizontal bar chart.
        
        Args:
            data: Dictionary mapping labels to values
            title: Chart title
            unit: Unit of measurement for values
            
        Returns:
            str: ASCII bar chart
        """
        # TODO: Implement horizontal bar chart
        # 1. Find maximum value for scaling
        # 2. Calculate bar lengths proportional to values
        # 3. Create horizontal bars with labels
        # 4. Add title and formatting
        
        if not data:
            return "No data available for chart"
        
        max_value = max(data.values()) if data.values() else 1
        max_label_length = max(len(label) for label in data.keys()) if data else 0
        
        chart_lines = [
            f" {title}",
            f" {'=' * len(title)}",
            ""
        ]
        
        # TODO: Create actual bar chart
        for label, value in data.items():
            chart_lines.append(f" {label:<{max_label_length}} | TODO: bar")
        
        chart_lines.append("")
        return "\n".join(chart_lines)
    
    def create_histogram(self, values: List[float], bins: int = 10, 
                        title: str = "Histogram", unit: str = "") -> str:
        """
        Create a histogram from numerical data.
        
        Args:
            values: List of numerical values
            bins: Number of histogram bins
            title: Chart title
            unit: Unit of measurement
            
        Returns:
            str: ASCII histogram
        """
        # TODO: Implement histogram creation
        # 1. Calculate bin ranges
        # 2. Count values in each bin
        # 3. Create vertical or horizontal histogram
        # 4. Add labels and formatting
        
        if not values:
            return "No data available for histogram"
        
        min_val = min(values)
        max_val = max(values)
        
        chart_lines = [
            f" {title}",
            f" {'=' * len(title)}",
            "",
            f" Range: {min_val:.1f} to {max_val:.1f} {unit}",
            f" Total values: {len(values)}",
            "",
            " TODO: Implement histogram visualization",
            ""
        ]
        
        return "\n".join(chart_lines)
    
    def create_weather_summary_table(self, weather_data: List[WeatherData]) -> str:
        """
        Create a formatted table summarizing weather data.
        
        Args:
            weather_data: List of weather data points
            
        Returns:
            str: Formatted weather summary table
        """
        # TODO: Implement weather summary table
        # 1. Create table headers
        # 2. Format each weather data point as a table row
        # 3. Align columns properly
        # 4. Add borders and formatting
        
        if not weather_data:
            return "No weather data available"
        
        # Table headers
        headers = ["Date/Time", "City", "Temp(°C)", "Humidity(%)", "Pressure(hPa)", "Wind(m/s)", "Condition"]
        
        # Calculate column widths
        col_widths = [len(header) for header in headers]
        
        # TODO: Calculate actual column widths based on data
        # TODO: Format data rows
        
        table_lines = [
            " Weather Summary",
            " ===============",
            "",
            " TODO: Implement weather summary table",
            f" Total records: {len(weather_data)}",
            ""
        ]
        
        return "\n".join(table_lines)
    
    def create_comparison_chart(self, location_data: Dict[str, List[WeatherData]], 
                              parameter: str = 'temperature') -> str:
        """
        Create a comparison chart for multiple locations.
        
        Args:
            location_data: Dictionary mapping location names to weather data
            parameter: Weather parameter to compare
            
        Returns:
            str: Comparison chart
        """
        # TODO: Implement location comparison chart
        # 1. Calculate statistics for each location
        # 2. Create side-by-side comparison
        # 3. Use bar chart or table format
        # 4. Highlight significant differences
        
        if not location_data:
            return "No location data available for comparison"
        
        chart_lines = [
            f" Location Comparison - {parameter.title()}",
            f" {'=' * (25 + len(parameter))}",
            "",
            " TODO: Implement location comparison chart",
            f" Locations: {', '.join(location_data.keys())}",
            ""
        ]
        
        return "\n".join(chart_lines)
    
    def create_trend_visualization(self, weather_data: List[WeatherData], 
                                 parameter: str = 'temperature') -> str:
        """
        Create a visualization showing trends over time.
        
        Args:
            weather_data: List of weather data points
            parameter: Weather parameter to visualize
            
        Returns:
            str: Trend visualization
        """
        # TODO: Implement trend visualization
        # 1. Sort data by timestamp
        # 2. Calculate moving averages or trend lines
        # 3. Create line chart showing trend
        # 4. Add trend direction indicators
        
        if not weather_data:
            return "No data available for trend visualization"
        
        sorted_data = sorted(weather_data, key=lambda x: x.timestamp)
        
        chart_lines = [
            f" {parameter.title()} Trend Analysis",
            f" {'=' * (len(parameter) + 15)}",
            "",
            " TODO: Implement trend visualization",
            f" Data points: {len(sorted_data)}",
            f" Time span: {sorted_data[0].timestamp.date()} to {sorted_data[-1].timestamp.date()}",
            ""
        ]
        
        return "\n".join(chart_lines)
    
    def create_weather_report(self, weather_data: List[WeatherData], 
                            location: str = "Unknown") -> str:
        """
        Create a comprehensive weather report.
        
        Args:
            weather_data: List of weather data points
            location: Location name for the report
            
        Returns:
            str: Formatted weather report
        """
        # TODO: Implement comprehensive weather report
        # 1. Include summary statistics
        # 2. Add trend analysis
        # 3. Include charts and visualizations
        # 4. Add insights and observations
        # 5. Format professionally
        
        if not weather_data:
            return f"No weather data available for {location}"
        
        sorted_data = sorted(weather_data, key=lambda x: x.timestamp)
        start_date = sorted_data[0].timestamp.date()
        end_date = sorted_data[-1].timestamp.date()
        
        report_lines = [
            f" WEATHER ANALYSIS REPORT",
            f" {'=' * 23}",
            "",
            f" Location: {location}",
            f" Period: {start_date} to {end_date}",
            f" Data Points: {len(weather_data)}",
            f" Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            " SUMMARY STATISTICS",
            " ------------------",
            " TODO: Add summary statistics",
            "",
            " TREND ANALYSIS",
            " --------------",
            " TODO: Add trend analysis",
            "",
            " EXTREME VALUES",
            " --------------",
            " TODO: Add extreme values",
            "",
            " INSIGHTS",
            " --------",
            " TODO: Add insights and observations",
            ""
        ]
        
        return "\n".join(report_lines)
    
    def _scale_value(self, value: float, min_val: float, max_val: float, 
                    scale_min: int = 0, scale_max: int = 50) -> int:
        """
        Scale a value to fit within chart dimensions.
        
        Args:
            value: Value to scale
            min_val: Minimum value in dataset
            max_val: Maximum value in dataset
            scale_min: Minimum scale value
            scale_max: Maximum scale value
            
        Returns:
            int: Scaled value
        """
        if max_val == min_val:
            return scale_min
        
        return int(scale_min + (value - min_val) * (scale_max - scale_min) / (max_val - min_val))
    
    def _create_horizontal_line(self, length: int, char: str = "█") -> str:
        """Create a horizontal line for bar charts."""
        return char * length
    
    def _format_number(self, value: float, decimals: int = 1) -> str:
        """Format a number for display in charts."""
        return f"{value:.{decimals}f}"