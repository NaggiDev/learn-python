"""
String validation utilities.

This module provides functions for validating various string formats
commonly used in applications.
"""

import re
from typing import Optional

def is_email(email: str) -> bool:
    """
    Check if a string is a valid email address.
    
    Args:
        email (str): Email string to validate
        
    Returns:
        bool: True if valid email format, False otherwise
        
    Example:
        >>> is_email("user@example.com")
        True
        >>> is_email("invalid-email")
        False
    """
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_phone(phone: str) -> bool:
    """
    Check if a string is a valid phone number.
    
    Args:
        phone (str): Phone string to validate
        
    Returns:
        bool: True if valid phone format, False otherwise
        
    Example:
        >>> is_phone("(123) 456-7890")
        True
        >>> is_phone("123-456-7890")
        True
        >>> is_phone("1234567890")
        True
    """
    if not phone:
        return False
    
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    # Valid if 10 digits or 11 digits starting with 1
    return len(digits) == 10 or (len(digits) == 11 and digits[0] == '1')

def is_url(url: str) -> bool:
    """
    Check if a string is a valid URL.
    
    Args:
        url (str): URL string to validate
        
    Returns:
        bool: True if valid URL format, False otherwise
        
    Example:
        >>> is_url("https://www.example.com")
        True
        >>> is_url("http://example.com/path")
        True
        >>> is_url("not-a-url")
        False
    """
    if not url:
        return False
    
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(pattern, url) is not None

def is_strong_password(password: str) -> bool:
    """
    Check if a password meets strong password criteria.
    
    Criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    
    Args:
        password (str): Password to validate
        
    Returns:
        bool: True if password is strong, False otherwise
        
    Example:
        >>> is_strong_password("MyPass123!")
        True
        >>> is_strong_password("weak")
        False
    """
    if not password or len(password) < 8:
        return False
    
    # Check for required character types
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    return all([has_upper, has_lower, has_digit, has_special])

def contains_only_letters(text: str) -> bool:
    """
    Check if text contains only letters (no numbers or special characters).
    
    Args:
        text (str): Text to validate
        
    Returns:
        bool: True if contains only letters, False otherwise
        
    Example:
        >>> contains_only_letters("HelloWorld")
        True
        >>> contains_only_letters("Hello123")
        False
    """
    if not text:
        return False
    
    return text.isalpha()