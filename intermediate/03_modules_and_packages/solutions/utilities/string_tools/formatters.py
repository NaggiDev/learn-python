"""
String formatting utilities.

This module provides functions for formatting and transforming strings
in various ways commonly needed in programming tasks.
"""

import re
from typing import Optional

def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in the text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text with capitalized words
        
    Example:
        >>> capitalize_words("hello world python")
        'Hello World Python'
    """
    if not text:
        return ""
    return text.title()

def snake_to_camel(text: str) -> str:
    """
    Convert snake_case to camelCase.
    
    Args:
        text (str): Snake case string
        
    Returns:
        str: Camel case string
        
    Example:
        >>> snake_to_camel("hello_world_python")
        'helloWorldPython'
    """
    if not text:
        return ""
    
    components = text.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])

def camel_to_snake(text: str) -> str:
    """
    Convert camelCase to snake_case.
    
    Args:
        text (str): Camel case string
        
    Returns:
        str: Snake case string
        
    Example:
        >>> camel_to_snake("helloWorldPython")
        'hello_world_python'
    """
    if not text:
        return ""
    
    # Insert underscore before uppercase letters
    result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', text)
    return result.lower()

def format_phone(phone: str) -> str:
    """
    Format a phone number to (XXX) XXX-XXXX format.
    
    Args:
        phone (str): Phone number string
        
    Returns:
        str: Formatted phone number
        
    Example:
        >>> format_phone("1234567890")
        '(123) 456-7890'
        >>> format_phone("123-456-7890")
        '(123) 456-7890'
    """
    if not phone:
        return ""
    
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    # Handle different lengths
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return phone  # Return original if can't format

def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length and add suffix if truncated.
    
    Args:
        text (str): Input text
        max_length (int): Maximum length of result
        suffix (str): Suffix to add if truncated
        
    Returns:
        str: Truncated text
        
    Example:
        >>> truncate_text("This is a long text", 10)
        'This is...'
        >>> truncate_text("Short", 10)
        'Short'
    """
    if not text:
        return ""
    
    if len(text) <= max_length:
        return text
    
    # Make sure we have room for the suffix
    truncate_at = max_length - len(suffix)
    if truncate_at <= 0:
        return suffix[:max_length]
    
    return text[:truncate_at] + suffix