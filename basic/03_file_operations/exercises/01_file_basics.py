"""
Exercise: File Basics

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

This exercise covers:
- Opening and reading files
- Writing to files
- Using context managers (with statement)
"""

def read_entire_file(file_path):
    """
    Read and return the entire content of a file as a string.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: Content of the file
    """
    # TODO: Implement this function
    pass


def read_file_lines(file_path):
    """
    Read and return the content of a file as a list of lines.
    Strip newline characters from each line.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        list: List of strings, each representing a line from the file
    """
    # TODO: Implement this function
    pass


def write_lines_to_file(file_path, lines):
    """
    Write a list of strings to a file, with each string on a new line.
    
    Args:
        file_path (str): Path to the file
        lines (list): List of strings to write
        
    Returns:
        None
    """
    # TODO: Implement this function
    pass


def append_to_file(file_path, text):
    """
    Append text to the end of a file.
    
    Args:
        file_path (str): Path to the file
        text (str): Text to append
        
    Returns:
        None
    """
    # TODO: Implement this function
    pass


def count_words_in_file(file_path):
    """
    Count the number of words in a file.
    Words are separated by whitespace.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        int: Number of words in the file
    """
    # TODO: Implement this function
    pass


# Test functions
def test_file_operations():
    import os
    
    # Test file path
    test_file = "test_file.txt"
    
    # Test data
    test_lines = ["First line", "Second line", "Third line"]
    
    # Test write_lines_to_file
    write_lines_to_file(test_file, test_lines)
    assert os.path.exists(test_file), "File was not created"
    
    # Test read_entire_file
    content = read_entire_file(test_file)
    expected_content = "First line\nSecond line\nThird line\n"
    assert content == expected_content, f"Expected '{expected_content}', got '{content}'"
    
    # Test read_file_lines
    lines = read_file_lines(test_file)
    assert lines == test_lines, f"Expected {test_lines}, got {lines}"
    
    # Test append_to_file
    append_text = "Fourth line"
    append_to_file(test_file, append_text)
    
    # Verify append worked
    content = read_entire_file(test_file)
    expected_content = "First line\nSecond line\nThird line\nFourth line\n"
    assert content == expected_content, f"Expected '{expected_content}', got '{content}'"
    
    # Test count_words_in_file
    word_count = count_words_in_file(test_file)
    expected_count = 8  # "First line Second line Third line Fourth line" has 8 words
    assert word_count == expected_count, f"Expected {expected_count} words, got {word_count}"
    
    # Clean up
    os.remove(test_file)
    
    print("All tests passed!")


if __name__ == "__main__":
    test_file_operations()