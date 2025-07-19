"""Text formatting utilities."""

import re
from typing import Optional
from ..exceptions import ProcessingError

def clean_text(text: str) -> str:
    """
    Clean text by removing extra whitespace and normalizing.
    
    Args:
        text (str): Input text to clean
        
    Returns:
        str: Cleaned text
        
    Example:
        >>> clean_text("  Hello   World  ")
        'Hello World'
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    # Remove extra whitespace and normalize
    return ' '.join(text.split())

def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text with capitalized words
        
    Example:
        >>> capitalize_words("hello world python")
        'Hello World Python'
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
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
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
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
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    if not text:
        return ""
    
    # Insert underscore before uppercase letters
    result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', text)
    return result.lower()

def format_title(text: str, style: str = "title") -> str:
    """
    Format text as a title with various styles.
    
    Args:
        text (str): Input text
        style (str): Title style ('title', 'upper', 'lower', 'sentence')
        
    Returns:
        str: Formatted title
        
    Example:
        >>> format_title("hello world", "title")
        'Hello World'
        >>> format_title("hello world", "sentence")
        'Hello world'
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    if style == "title":
        return text.title()
    elif style == "upper":
        return text.upper()
    elif style == "lower":
        return text.lower()
    elif style == "sentence":
        return text.capitalize()
    else:
        raise ProcessingError(f"Unknown style: {style}")

def pad_text(text: str, width: int, char: str = " ", align: str = "center") -> str:
    """
    Pad text to specified width.
    
    Args:
        text (str): Input text
        width (int): Target width
        char (str): Padding character
        align (str): Alignment ('left', 'right', 'center')
        
    Returns:
        str: Padded text
        
    Example:
        >>> pad_text("hello", 10, "*", "center")
        '**hello***'
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    if len(text) >= width:
        return text
    
    if align == "left":
        return text.ljust(width, char)
    elif align == "right":
        return text.rjust(width, char)
    elif align == "center":
        return text.center(width, char)
    else:
        raise ProcessingError(f"Unknown alignment: {align}")