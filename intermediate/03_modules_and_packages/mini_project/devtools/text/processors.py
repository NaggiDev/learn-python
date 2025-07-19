"""Text processing utilities."""

import re
from typing import List
from ..exceptions import ProcessingError

def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text.
    
    Args:
        text (str): Input text
        
    Returns:
        List[str]: List of email addresses found
        
    Example:
        >>> extract_emails("Contact us at test@example.com or admin@test.org")
        ['test@example.com', 'admin@test.org']
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

def extract_urls(text: str) -> List[str]:
    """
    Extract URLs from text.
    
    Args:
        text (str): Input text
        
    Returns:
        List[str]: List of URLs found
        
    Example:
        >>> extract_urls("Visit https://example.com or http://test.org")
        ['https://example.com', 'http://test.org']
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    return re.findall(url_pattern, text)

def remove_html_tags(text: str) -> str:
    """
    Remove HTML tags from text.
    
    Args:
        text (str): Input text with HTML tags
        
    Returns:
        str: Text without HTML tags
        
    Example:
        >>> remove_html_tags("<p>Hello <b>world</b></p>")
        'Hello world'
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', '', text)
    # Clean up extra whitespace
    return ' '.join(clean.split())

def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to maximum length with suffix.
    
    Args:
        text (str): Input text
        max_length (int): Maximum length
        suffix (str): Suffix to add if truncated
        
    Returns:
        str: Truncated text
        
    Example:
        >>> truncate_text("This is a long text", 10)
        'This is...'
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    if len(text) <= max_length:
        return text
    
    # Make sure we have room for the suffix
    truncate_at = max_length - len(suffix)
    if truncate_at <= 0:
        return suffix[:max_length]
    
    return text[:truncate_at] + suffix

def extract_numbers(text: str) -> List[float]:
    """
    Extract numbers from text.
    
    Args:
        text (str): Input text
        
    Returns:
        List[float]: List of numbers found
        
    Example:
        >>> extract_numbers("I have 5 apples and 3.5 oranges")
        [5.0, 3.5]
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    # Pattern to match integers and floats
    number_pattern = r'-?\d+\.?\d*'
    matches = re.findall(number_pattern, text)
    
    numbers = []
    for match in matches:
        try:
            if '.' in match:
                numbers.append(float(match))
            else:
                numbers.append(float(int(match)))
        except ValueError:
            continue
    
    return numbers

def replace_multiple_spaces(text: str, replacement: str = " ") -> str:
    """
    Replace multiple consecutive spaces with single space or replacement.
    
    Args:
        text (str): Input text
        replacement (str): Replacement string
        
    Returns:
        str: Text with normalized spacing
        
    Example:
        >>> replace_multiple_spaces("Hello    world")
        'Hello world'
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    return re.sub(r'\s+', replacement, text)