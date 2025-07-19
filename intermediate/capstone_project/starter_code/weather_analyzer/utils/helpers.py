"""
Helper functions and utilities for the Weather Analyzer application.
"""

import re
from datetime import datetime, timezone
from typing import Optional, Tuple, Union


def format_temperature(temp_celsius: float, units: str = 'metric', 
                      decimals: int = 1) -> str:
    """
    Format temperature value with appropriate units.
    
    Args:
        temp_celsius: Temperature in Celsius
        units: Unit system ('metric', 'imperial', 'kelvin')
        decimals: Number of decimal places
        
    Returns:
        str: Formatted temperature string
    """
    # TODO: Implement temperature formatting
    # 1. Convert temperature to requested units
    # 2. Format with appropriate decimal places
    # 3. Add unit symbol
    
    if units == 'metric':
        return f"{temp_celsius:.{decimals}f}°C"
    elif units == 'imperial':
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        return f"{temp_fahrenheit:.{decimals}f}°F"
    elif units == 'kelvin':
        temp_kelvin = temp_celsius + 273.15
        return f"{temp_kelvin:.{decimals}f}K"
    else:
        return f"{temp_celsius:.{decimals}f}°C"


def format_wind_speed(speed_ms: float, units: str = 'metric', 
                     decimals: int = 1) -> str:
    """
    Format wind speed with appropriate units.
    
    Args:
        speed_ms: Wind speed in meters per second
        units: Unit system ('metric', 'imperial')
        decimals: Number of decimal places
        
    Returns:
        str: Formatted wind speed string
    """
    # TODO: Implement wind speed formatting
    # 1. Convert to appropriate units
    # 2. Format with decimal places
    # 3. Add unit abbreviation
    
    if units == 'metric':
        # Convert to km/h
        speed_kmh = speed_ms * 3.6
        return f"{speed_kmh:.{decimals}f} km/h"
    elif units == 'imperial':
        # Convert to mph
        speed_mph = speed_ms * 2.237
        return f"{speed_mph:.{decimals}f} mph"
    else:
        return f"{speed_ms:.{decimals}f} m/s"


def format_pressure(pressure_hpa: float, units: str = 'metric', 
                   decimals: int = 1) -> str:
    """
    Format atmospheric pressure with appropriate units.
    
    Args:
        pressure_hpa: Pressure in hectopascals (hPa)
        units: Unit system ('metric', 'imperial')
        decimals: Number of decimal places
        
    Returns:
        str: Formatted pressure string
    """
    # TODO: Implement pressure formatting
    # 1. Convert to appropriate units if needed
    # 2. Format with decimal places
    # 3. Add unit abbreviation
    
    if units == 'imperial':
        # Convert to inches of mercury
        pressure_inhg = pressure_hpa * 0.02953
        return f"{pressure_inhg:.{decimals}f} inHg"
    else:
        return f"{pressure_hpa:.{decimals}f} hPa"


def format_humidity(humidity_percent: int) -> str:
    """
    Format humidity percentage.
    
    Args:
        humidity_percent: Humidity as percentage
        
    Returns:
        str: Formatted humidity string
    """
    return f"{humidity_percent}%"


def format_visibility(visibility_meters: Optional[float], 
                     units: str = 'metric') -> str:
    """
    Format visibility distance.
    
    Args:
        visibility_meters: Visibility in meters
        units: Unit system ('metric', 'imperial')
        
    Returns:
        str: Formatted visibility string
    """
    if visibility_meters is None:
        return "N/A"
    
    if units == 'imperial':
        # Convert to miles
        visibility_miles = visibility_meters / 1609.34
        if visibility_miles >= 1:
            return f"{visibility_miles:.1f} mi"
        else:
            # Show in feet for short distances
            visibility_feet = visibility_meters * 3.28084
            return f"{visibility_feet:.0f} ft"
    else:
        # Metric units
        if visibility_meters >= 1000:
            visibility_km = visibility_meters / 1000
            return f"{visibility_km:.1f} km"
        else:
            return f"{visibility_meters:.0f} m"


def format_wind_direction(degrees: Optional[int]) -> str:
    """
    Convert wind direction degrees to compass direction.
    
    Args:
        degrees: Wind direction in degrees (0-360)
        
    Returns:
        str: Compass direction (N, NE, E, SE, S, SW, W, NW)
    """
    if degrees is None:
        return "N/A"
    
    # TODO: Implement wind direction conversion
    # 1. Normalize degrees to 0-360 range
    # 2. Map to 8 or 16 compass directions
    # 3. Return appropriate compass direction string
    
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = round(degrees / 45) % 8
    return directions[index]


def parse_city_name(city_input: str) -> Tuple[str, Optional[str]]:
    """
    Parse city input to extract city name and country code.
    
    Args:
        city_input: City input string (e.g., "London", "Paris,FR", "New York,US")
        
    Returns:
        Tuple[str, Optional[str]]: City name and optional country code
    """
    # TODO: Implement city name parsing
    # 1. Split on comma if present
    # 2. Clean up whitespace
    # 3. Validate country code format if provided
    # 4. Return tuple of city and country
    
    parts = city_input.split(',')
    city = parts[0].strip()
    country = parts[1].strip() if len(parts) > 1 else None
    
    return city, country


def validate_coordinates(latitude: float, longitude: float) -> bool:
    """
    Validate geographic coordinates.
    
    Args:
        latitude: Latitude value
        longitude: Longitude value
        
    Returns:
        bool: True if coordinates are valid
    """
    return -90 <= latitude <= 90 and -180 <= longitude <= 180


def calculate_heat_index(temperature_celsius: float, humidity_percent: int) -> float:
    """
    Calculate heat index (apparent temperature) based on temperature and humidity.
    
    Args:
        temperature_celsius: Temperature in Celsius
        humidity_percent: Relative humidity percentage
        
    Returns:
        float: Heat index in Celsius
    """
    # TODO: Implement heat index calculation
    # 1. Convert temperature to Fahrenheit for calculation
    # 2. Apply heat index formula
    # 3. Convert result back to Celsius
    # 4. Handle edge cases (low temperature/humidity)
    
    # Convert to Fahrenheit for calculation
    temp_f = (temperature_celsius * 9/5) + 32
    
    # Simplified heat index calculation (full formula is more complex)
    if temp_f < 80 or humidity_percent < 40:
        return temperature_celsius  # Heat index not applicable
    
    # TODO: Implement full heat index formula
    heat_index_f = temp_f  # Placeholder
    
    # Convert back to Celsius
    heat_index_c = (heat_index_f - 32) * 5/9
    return heat_index_c


def calculate_wind_chill(temperature_celsius: float, wind_speed_ms: float) -> float:
    """
    Calculate wind chill temperature.
    
    Args:
        temperature_celsius: Temperature in Celsius
        wind_speed_ms: Wind speed in meters per second
        
    Returns:
        float: Wind chill temperature in Celsius
    """
    # TODO: Implement wind chill calculation
    # 1. Check if conditions warrant wind chill calculation
    # 2. Apply wind chill formula
    # 3. Handle edge cases
    
    # Wind chill only applies at low temperatures and sufficient wind
    if temperature_celsius > 10 or wind_speed_ms < 1.34:  # 1.34 m/s = 3 mph
        return temperature_celsius
    
    # Convert wind speed to km/h for calculation
    wind_speed_kmh = wind_speed_ms * 3.6
    
    # Wind chill formula (Environment Canada)
    wind_chill = (13.12 + 0.6215 * temperature_celsius - 
                  11.37 * (wind_speed_kmh ** 0.16) + 
                  0.3965 * temperature_celsius * (wind_speed_kmh ** 0.16))
    
    return wind_chill


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format datetime object to string.
    
    Args:
        dt: Datetime object
        format_str: Format string
        
    Returns:
        str: Formatted datetime string
    """
    return dt.strftime(format_str)


def parse_datetime(date_str: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Parse datetime string to datetime object.
    
    Args:
        date_str: Date string
        format_str: Expected format string
        
    Returns:
        datetime: Parsed datetime object
    """
    return datetime.strptime(date_str, format_str)


def safe_float(value: Union[str, int, float], default: float = 0.0) -> float:
    """
    Safely convert value to float with default fallback.
    
    Args:
        value: Value to convert
        default: Default value if conversion fails
        
    Returns:
        float: Converted value or default
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def safe_int(value: Union[str, int, float], default: int = 0) -> int:
    """
    Safely convert value to int with default fallback.
    
    Args:
        value: Value to convert
        default: Default value if conversion fails
        
    Returns:
        int: Converted value or default
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate string to maximum length with optional suffix.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        str: Truncated string
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix