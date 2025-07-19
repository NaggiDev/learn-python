"""Text analysis utilities."""

import re
from typing import Dict, List
from ..exceptions import ProcessingError

def word_count(text: str) -> int:
    """
    Count the number of words in text.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        int: Number of words in the text
        
    Raises:
        ProcessingError: If text processing fails
        
    Example:
        >>> word_count("Hello world")
        2
        >>> word_count("")
        0
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    if not text.strip():
        return 0
    
    words = text.split()
    return len(words)

def count_characters(text: str, include_spaces: bool = True) -> int:
    """
    Count characters in text.
    
    Args:
        text (str): Input text
        include_spaces (bool): Whether to include spaces in count
        
    Returns:
        int: Number of characters
        
    Example:
        >>> count_characters("hello")
        5
        >>> count_characters("hello world", include_spaces=False)
        10
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(' ', ''))

def analyze_readability(text: str) -> Dict[str, float]:
    """
    Analyze text readability using various metrics.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        Dict[str, float]: Dictionary with readability metrics
        
    Example:
        >>> metrics = analyze_readability("This is a simple sentence.")
        >>> 'avg_sentence_length' in metrics
        True
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Split into words
    words = text.split()
    
    if not sentences or not words:
        return {
            'avg_sentence_length': 0.0,
            'avg_word_length': 0.0,
            'sentence_count': 0,
            'word_count': 0,
            'character_count': 0
        }
    
    avg_sentence_length = len(words) / len(sentences)
    avg_word_length = sum(len(word.strip('.,!?;:')) for word in words) / len(words)
    
    return {
        'avg_sentence_length': round(avg_sentence_length, 2),
        'avg_word_length': round(avg_word_length, 2),
        'sentence_count': len(sentences),
        'word_count': len(words),
        'character_count': len(text)
    }