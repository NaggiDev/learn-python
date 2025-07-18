"""
Exercise: String Manipulation

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

Learning objectives:
- Create and manipulate strings
- Use string methods for common operations
- Format strings using different techniques
- Implement basic text processing functions
"""

def reverse_string(text):
    """
    Reverse a string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The reversed string
    """
    # TODO: Implement this function
    pass


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    The function should be case-insensitive.
    
    Args:
        text (str): The input string
        
    Returns:
        int: The number of vowels in the string
    """
    # TODO: Implement this function
    pass


def capitalize_words(text):
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The string with each word capitalized
    """
    # TODO: Implement this function
    pass


def is_palindrome(text):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    The function should ignore case and non-alphanumeric characters.
    
    Args:
        text (str): The input string
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # TODO: Implement this function
    pass


def count_substring(text, substring):
    """
    Count the number of occurrences of a substring in a string.
    
    Args:
        text (str): The input string
        substring (str): The substring to count
        
    Returns:
        int: The number of occurrences of the substring
    """
    # TODO: Implement this function
    pass


def remove_whitespace(text):
    """
    Remove all whitespace characters from a string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The string with all whitespace removed
    """
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


def title_case(text):
    """
    Convert a string to title case (first letter of each word capitalized, rest lowercase).
    The function should handle apostrophes correctly (e.g., "don't" -> "Don't").
    
    Args:
        text (str): The input string
        
    Returns:
        str: The string in title case
    """
    # TODO: Implement this function
    pass


def count_words(text):
    """
    Count the number of words in a string.
    Words are separated by one or more whitespace characters.
    
    Args:
        text (str): The input string
        
    Returns:
        int: The number of words in the string
    """
    # TODO: Implement this function
    pass


def snake_to_camel_case(snake_case):
    """
    Convert a snake_case string to camelCase.
    For example, "hello_world" becomes "helloWorld".
    
    Args:
        snake_case (str): The snake_case string
        
    Returns:
        str: The camelCase string
    """
    # TODO: Implement this function
    pass


# Tests
def test_reverse_string():
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"
    assert reverse_string("") == ""
    print("✓ test_reverse_string passed")


def test_count_vowels():
    assert count_vowels("Python") == 1
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    print("✓ test_count_vowels passed")


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"
    assert capitalize_words("") == ""
    print("✓ test_capitalize_words passed")


def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Python") == False
    assert is_palindrome("") == True
    print("✓ test_is_palindrome passed")


def test_count_substring():
    assert count_substring("Python Programming", "P") == 2
    assert count_substring("banana", "ana") == 1
    assert count_substring("banana", "an") == 2
    assert count_substring("banana", "x") == 0
    print("✓ test_count_substring passed")


def test_remove_whitespace():
    assert remove_whitespace("Hello, World!") == "Hello,World!"
    assert remove_whitespace("  Python  Programming  ") == "PythonProgramming"
    assert remove_whitespace("\t\nTest\r\n") == "Test"
    print("✓ test_remove_whitespace passed")


def test_replace_substring():
    assert replace_substring("Hello, World!", "World", "Python") == "Hello, Python!"
    assert replace_substring("banana", "ana", "XXX") == "bXXXna"
    assert replace_substring("banana", "x", "y") == "banana"
    print("✓ test_replace_substring passed")


def test_split_and_join():
    assert split_and_join("Hello,World,Python", ",", "-") == "Hello-World-Python"
    assert split_and_join("a b c d", " ", "") == "abcd"
    assert split_and_join("no-delimiter-here", "x", "_") == "no-delimiter-here"
    print("✓ test_split_and_join passed")


def test_find_first_occurrence():
    assert find_first_occurrence("Hello, World!", "World") == 7
    assert find_first_occurrence("banana", "ana") == 1
    assert find_first_occurrence("banana", "x") == -1
    print("✓ test_find_first_occurrence passed")


def test_format_name_and_age():
    assert format_name_and_age("Alice", 30) == "My name is Alice and I am 30 years old."
    assert format_name_and_age("Bob", 25) == "My name is Bob and I am 25 years old."
    print("✓ test_format_name_and_age passed")


def test_extract_domain():
    assert extract_domain("user@example.com") == "example.com"
    assert extract_domain("contact@python.org") == "python.org"
    assert extract_domain("invalid-email") == None
    print("✓ test_extract_domain passed")


def test_mask_credit_card():
    assert mask_credit_card("1234567890123456") == "************3456"
    assert mask_credit_card("1234-5678-9012-3456") == "************3456"
    assert mask_credit_card("1234 5678 9012 3456") == "************3456"
    print("✓ test_mask_credit_card passed")


def test_title_case():
    assert title_case("hello world") == "Hello World"
    assert title_case("PYTHON PROGRAMMING") == "Python Programming"
    assert title_case("don't stop believing") == "Don't Stop Believing"
    print("✓ test_title_case passed")


def test_count_words():
    assert count_words("Hello, World!") == 2
    assert count_words("Python  Programming   Language") == 3
    assert count_words("   Spaces   ") == 1
    assert count_words("") == 0
    print("✓ test_count_words passed")


def test_snake_to_camel_case():
    assert snake_to_camel_case("hello_world") == "helloWorld"
    assert snake_to_camel_case("python_programming_language") == "pythonProgrammingLanguage"
    assert snake_to_camel_case("no_underscores") == "noUnderscores"
    print("✓ test_snake_to_camel_case passed")


if __name__ == "__main__":
    print("Running tests for string manipulation...")
    test_reverse_string()
    test_count_vowels()
    test_capitalize_words()
    test_is_palindrome()
    test_count_substring()
    test_remove_whitespace()
    test_replace_substring()
    test_split_and_join()
    test_find_first_occurrence()
    test_format_name_and_age()
    test_extract_domain()
    test_mask_credit_card()
    test_title_case()
    test_count_words()
    test_snake_to_camel_case()
    print("All tests passed!")