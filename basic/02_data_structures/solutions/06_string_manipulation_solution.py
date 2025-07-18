"""
Solution: String Manipulation

This file contains solutions to the string manipulation exercises.
"""

def reverse_string(text):
    """
    Reverse a string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The reversed string
    """
    return text[::-1]


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    The function should be case-insensitive.
    
    Args:
        text (str): The input string
        
    Returns:
        int: The number of vowels in the string
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def capitalize_words(text):
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The string with each word capitalized
    """
    return text.title()


def is_palindrome(text):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    The function should ignore case and non-alphanumeric characters.
    
    Args:
        text (str): The input string
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


def count_substring(text, substring):
    """
    Count the number of occurrences of a substring in a string.
    
    Args:
        text (str): The input string
        substring (str): The substring to count
        
    Returns:
        int: The number of occurrences of the substring
    """
    return text.count(substring)


def remove_whitespace(text):
    """
    Remove all whitespace characters from a string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The string with all whitespace removed
    """
    return ''.join(text.split())


def replace_substring(text, old, new):
    """
    Replace all occurrences of a substring with another substring.
    
    Args:
        text (str): The input string
        old (str): The substring to replace
        new (str): The replacement substring
        
    Returns:
        str: The string with all occurrences of 'old' replaced by 'new'
    """
    return text.replace(old, new)


def split_and_join(text, delimiter, join_char):
    """
    Split a string by a delimiter and join the parts with a different character.
    
    Args:
        text (str): The input string
        delimiter (str): The delimiter to split by
        join_char (str): The character to join with
        
    Returns:
        str: The split and rejoined string
    """
    parts = text.split(delimiter)
    return join_char.join(parts)


def find_first_occurrence(text, substring):
    """
    Find the index of the first occurrence of a substring in a string.
    If the substring is not found, return -1.
    
    Args:
        text (str): The input string
        substring (str): The substring to find
        
    Returns:
        int: The index of the first occurrence, or -1 if not found
    """
    return text.find(substring)


def format_name_and_age(name, age):
    """
    Format a name and age into a string using f-strings.
    The format should be: "My name is {name} and I am {age} years old."
    
    Args:
        name (str): The name
        age (int): The age
        
    Returns:
        str: The formatted string
    """
    return f"My name is {name} and I am {age} years old."


def extract_domain(email):
    """
    Extract the domain part from an email address.
    For example, from "user@example.com" extract "example.com".
    If the input is not a valid email format, return None.
    
    Args:
        email (str): The email address
        
    Returns:
        str or None: The domain part of the email, or None if invalid format
    """
    if '@' not in email:
        return None
    
    parts = email.split('@')
    if len(parts) != 2 or not parts[1]:
        return None
    
    return parts[1]


def mask_credit_card(card_number):
    """
    Mask a credit card number by replacing all but the last 4 digits with '*'.
    For example, "1234567890123456" becomes "************3456".
    The function should handle spaces and hyphens in the input.
    
    Args:
        card_number (str): The credit card number
        
    Returns:
        str: The masked credit card number
    """
    # Remove spaces and hyphens
    cleaned_number = card_number.replace(' ', '').replace('-', '')
    
    # Keep only the last 4 digits
    last_four = cleaned_number[-4:]
    masked = '*' * (len(cleaned_number) - 4) + last_four
    
    return masked


def title_case(text):
    """
    Convert a string to title case (first letter of each word capitalized, rest lowercase).
    The function should handle apostrophes correctly (e.g., "don't" -> "Don't").
    
    Args:
        text (str): The input string
        
    Returns:
        str: The string in title case
    """
    words = text.lower().split()
    title_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(title_words)


def count_words(text):
    """
    Count the number of words in a string.
    Words are separated by one or more whitespace characters.
    
    Args:
        text (str): The input string
        
    Returns:
        int: The number of words in the string
    """
    if not text.strip():
        return 0
    
    return len(text.split())


def snake_to_camel_case(snake_case):
    """
    Convert a snake_case string to camelCase.
    For example, "hello_world" becomes "helloWorld".
    
    Args:
        snake_case (str): The snake_case string
        
    Returns:
        str: The camelCase string
    """
    words = snake_case.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])