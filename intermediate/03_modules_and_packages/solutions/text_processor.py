"""
Text Processing Module - Solution

A comprehensive text processing module with various string manipulation
and analysis functions. Demonstrates proper error handling, type hints,
and documentation.

Author: Python Learning Path
Version: 1.0
"""

import re
import string
from typing import List, Dict, Optional

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
    if not text:
        return ""
    return ' '.join(text.split())

def word_count(text: str) -> int:
    """
    Count the number of words in text.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Number of words
        
    Example:
        >>> word_count("Hello world")
        2
        >>> word_count("")
        0
    """
    if not text:
        return 0
    return len(text.split())

def character_frequency(text: str) -> Dict[str, int]:
    """
    Count frequency of each character in text.
    
    Args:
        text (str): Input text
        
    Returns:
        Dict[str, int]: Dictionary with character frequencies
        
    Example:
        >>> character_frequency("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    if not text:
        return {}
    
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def reverse_words(text: str) -> str:
    """
    Reverse the order of words in text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text with words in reverse order
        
    Example:
        >>> reverse_words("Hello World Python")
        'Python World Hello'
    """
    if not text:
        return ""
    words = text.split()
    return ' '.join(reversed(words))

def is_palindrome(text: str) -> bool:
    """
    Check if text is a palindrome (ignoring case and spaces).
    
    Args:
        text (str): Input text
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    if not text:
        return True
    
    # Remove spaces and punctuation, convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text using regex.
    
    Args:
        text (str): Input text
        
    Returns:
        List[str]: List of email addresses found
        
    Example:
        >>> extract_emails("Contact us at test@example.com or admin@test.org")
        ['test@example.com', 'admin@test.org']
    """
    if not text:
        return []
    
    # Simple email pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

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
    if not text:
        return ""
    return text.title()

def remove_punctuation(text: str) -> str:
    """
    Remove all punctuation from text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text without punctuation
        
    Example:
        >>> remove_punctuation("Hello, World!")
        'Hello World'
    """
    if not text:
        return ""
    
    # Remove punctuation but keep spaces
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def text_statistics(text: str) -> Dict[str, int]:
    """
    Generate comprehensive text statistics.
    
    Args:
        text (str): Input text
        
    Returns:
        Dict[str, int]: Dictionary with various text statistics
        
    Example:
        >>> stats = text_statistics("Hello world. How are you?")
        >>> stats['word_count']
        5
    """
    if not text:
        return {
            'character_count': 0,
            'word_count': 0,
            'sentence_count': 0,
            'paragraph_count': 0
        }
    
    # Count characters (including spaces)
    char_count = len(text)
    
    # Count words
    word_count_val = word_count(text)
    
    # Count sentences (approximate - count sentence-ending punctuation)
    sentence_count = len(re.findall(r'[.!?]+', text))
    
    # Count paragraphs (separated by double newlines)
    paragraph_count = len([p for p in text.split('\n\n') if p.strip()])
    
    return {
        'character_count': char_count,
        'word_count': word_count_val,
        'sentence_count': max(1, sentence_count),  # At least 1 if there's text
        'paragraph_count': max(1, paragraph_count)  # At least 1 if there's text
    }

def main():
    """Test all text processing functions."""
    test_text = """
    Hello World! This is a test text.
    It contains multiple sentences and paragraphs.
    
    Contact us at: test@example.com or admin@test.org
    
    A man a plan a canal Panama.
    """
    
    print("Text Processing Module Test:")
    print("=" * 40)
    
    # Test clean_text
    cleaned = clean_text(test_text)
    print(f"Original text length: {len(test_text)}")
    print(f"Cleaned text length: {len(cleaned)}")
    print(f"Cleaned text preview: {cleaned[:50]}...")
    
    # Test word_count
    words = word_count(test_text)
    print(f"\nWord count: {words}")
    
    # Test character_frequency
    freq = character_frequency("hello world")
    print(f"\nCharacter frequency for 'hello world': {freq}")
    
    # Test reverse_words
    reversed_text = reverse_words("Hello World Python")
    print(f"\nReversed words: {reversed_text}")
    
    # Test is_palindrome
    palindrome_test = "A man a plan a canal Panama"
    is_pal = is_palindrome(palindrome_test)
    print(f"\nIs '{palindrome_test}' a palindrome? {is_pal}")
    
    # Test extract_emails
    emails = extract_emails(test_text)
    print(f"\nExtracted emails: {emails}")
    
    # Test capitalize_words
    capitalized = capitalize_words("hello world python")
    print(f"\nCapitalized: {capitalized}")
    
    # Test remove_punctuation
    no_punct = remove_punctuation("Hello, World! How are you?")
    print(f"\nWithout punctuation: '{no_punct}'")
    
    # Test text_statistics
    stats = text_statistics(test_text)
    print(f"\nText statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 40)
    print("All tests completed successfully!")

if __name__ == "__main__":
    main()