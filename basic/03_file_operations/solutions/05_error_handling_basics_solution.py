"""
Solution: Error Handling Basics

This file contains solutions to the error handling basics exercise.
"""

def safe_divide(a, b):
    """
    Safely divide a by b, handling potential errors.
    
    Args:
        a (float): Numerator
        b (float): Denominator
        
    Returns:
        float: Result of a / b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def safe_convert_to_int(value):
    """
    Convert a value to an integer, handling potential errors.
    
    Args:
        value: Value to convert
        
    Returns:
        int or None: Converted integer, or None if conversion fails
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def get_dict_value(dictionary, key, default=None):
    """
    Safely get a value from a dictionary by key.
    
    Args:
        dictionary (dict): Dictionary to get value from
        key: Key to look up
        default: Value to return if key is not found
        
    Returns:
        Value associated with key, or default if key is not found
    """
    try:
        return dictionary[key]
    except KeyError:
        return default


def read_file_safely(file_path):
    """
    Read a file safely, handling potential errors.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str or None: File content, or None if file cannot be read
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except (FileNotFoundError, PermissionError, IOError):
        return None


def execute_with_retry(func, max_attempts=3):
    """
    Execute a function with retry logic.
    
    Args:
        func: Function to execute (takes no arguments)
        max_attempts (int): Maximum number of attempts
        
    Returns:
        Result of the function if successful
        
    Raises:
        Exception: If all attempts fail
    """
    attempts = 0
    last_error = None
    
    while attempts < max_attempts:
        try:
            return func()
        except Exception as e:
            attempts += 1
            last_error = e
            
            # If we've reached max attempts, re-raise the last error
            if attempts >= max_attempts:
                raise last_error


# Test functions
def test_error_handling_basics():
    # Test safe_divide
    assert safe_divide(10, 2) == 5, "Expected 10/2 = 5"
    
    try:
        safe_divide(10, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass  # This is expected
    
    # Test safe_convert_to_int
    assert safe_convert_to_int("42") == 42, "Expected '42' to convert to 42"
    assert safe_convert_to_int("hello") is None, "Expected 'hello' to convert to None"
    assert safe_convert_to_int(3.14) == 3, "Expected 3.14 to convert to 3"
    
    # Test get_dict_value
    test_dict = {"a": 1, "b": 2, "c": 3}
    assert get_dict_value(test_dict, "a") == 1, "Expected test_dict['a'] = 1"
    assert get_dict_value(test_dict, "d") is None, "Expected test_dict['d'] = None"
    assert get_dict_value(test_dict, "d", 0) == 0, "Expected test_dict['d'] with default = 0"
    
    # Test read_file_safely
    import os
    
    # Create a test file
    with open("test_file.txt", "w") as f:
        f.write("Hello, World!")
    
    content = read_file_safely("test_file.txt")
    assert content == "Hello, World!", f"Expected 'Hello, World!', got '{content}'"
    
    # Test with non-existent file
    content = read_file_safely("nonexistent_file.txt")
    assert content is None, f"Expected None for nonexistent file, got '{content}'"
    
    # Clean up
    os.remove("test_file.txt")
    
    # Test execute_with_retry
    global attempt_count
    attempt_count = 0
    
    def succeed_on_third_attempt():
        global attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ValueError("Not yet")
        return "Success"
    
    result = execute_with_retry(succeed_on_third_attempt)
    assert result == "Success", f"Expected 'Success', got '{result}'"
    assert attempt_count == 3, f"Expected 3 attempts, got {attempt_count}"
    
    # Test with function that always fails
    attempt_count = 0
    
    def always_fail():
        global attempt_count
        attempt_count += 1
        raise ValueError("Always fails")
    
    try:
        execute_with_retry(always_fail, max_attempts=2)
        assert False, "Expected function to raise an exception"
    except ValueError:
        assert attempt_count == 2, f"Expected 2 attempts, got {attempt_count}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_error_handling_basics()