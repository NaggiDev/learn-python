"""Data validation utilities."""

import re
import json
from typing import Any
from ..exceptions import ValidationError

def validate_email(email: str) -> bool:
    """
    Validate email address format.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    if not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str, country_code: str = "US") -> bool:
    """
    Validate phone number format.
    
    Args:
        phone (str): Phone number to validate
        country_code (str): Country code for validation
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> validate_phone("(123) 456-7890")
        True
        >>> validate_phone("123-456-7890")
        True
    """
    if not isinstance(phone, str):
        return False
    
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    if country_code == "US":
        # US phone numbers: 10 digits or 11 digits starting with 1
        return len(digits) == 10 or (len(digits) == 11 and digits[0] == '1')
    else:
        # Basic validation for other countries (7-15 digits)
        return 7 <= len(digits) <= 15

def validate_url(url: str) -> bool:
    """
    Validate URL format.
    
    Args:
        url (str): URL to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> validate_url("https://www.example.com")
        True
        >>> validate_url("not-a-url")
        False
    """
    if not isinstance(url, str):
        return False
    
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(pattern, url) is not None

def is_valid_json(text: str) -> bool:
    """
    Check if text is valid JSON.
    
    Args:
        text (str): Text to validate
        
    Returns:
        bool: True if valid JSON, False otherwise
        
    Example:
        >>> is_valid_json('{"name": "John", "age": 30}')
        True
        >>> is_valid_json('invalid json')
        False
    """
    if not isinstance(text, str):
        return False
    
    try:
        json.loads(text)
        return True
    except (json.JSONDecodeError, ValueError):
        return False

def validate_credit_card(card_number: str) -> bool:
    """
    Validate credit card number using Luhn algorithm.
    
    Args:
        card_number (str): Credit card number
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> validate_credit_card("4532015112830366")  # Valid test number
        True
    """
    if not isinstance(card_number, str):
        return False
    
    # Remove spaces and dashes
    card_number = re.sub(r'[\s-]', '', card_number)
    
    # Check if all digits
    if not card_number.isdigit():
        return False
    
    # Check length (13-19 digits for most cards)
    if not (13 <= len(card_number) <= 19):
        return False
    
    # Luhn algorithm
    def luhn_check(card_num):
        digits = [int(d) for d in card_num]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0
    
    return luhn_check(card_number)

def validate_password_strength(password: str) -> dict:
    """
    Validate password strength and return detailed analysis.
    
    Args:
        password (str): Password to validate
        
    Returns:
        dict: Dictionary with strength analysis
        
    Example:
        >>> result = validate_password_strength("MyPass123!")
        >>> result['is_strong']
        True
    """
    if not isinstance(password, str):
        raise ValidationError("Password must be a string")
    
    analysis = {
        'length': len(password),
        'has_upper': bool(re.search(r'[A-Z]', password)),
        'has_lower': bool(re.search(r'[a-z]', password)),
        'has_digit': bool(re.search(r'\d', password)),
        'has_special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        'is_strong': False,
        'score': 0,
        'feedback': []
    }
    
    # Calculate score
    if analysis['length'] >= 8:
        analysis['score'] += 1
    else:
        analysis['feedback'].append("Password should be at least 8 characters long")
    
    if analysis['has_upper']:
        analysis['score'] += 1
    else:
        analysis['feedback'].append("Password should contain uppercase letters")
    
    if analysis['has_lower']:
        analysis['score'] += 1
    else:
        analysis['feedback'].append("Password should contain lowercase letters")
    
    if analysis['has_digit']:
        analysis['score'] += 1
    else:
        analysis['feedback'].append("Password should contain numbers")
    
    if analysis['has_special']:
        analysis['score'] += 1
    else:
        analysis['feedback'].append("Password should contain special characters")
    
    # Determine if strong (score >= 4)
    analysis['is_strong'] = analysis['score'] >= 4
    
    if analysis['is_strong']:
        analysis['feedback'] = ["Password is strong!"]
    
    return analysis