"""
Solution: File Basics

This file contains solutions to the file basics exercise.
"""

def read_entire_file(file_path):
    """
    Read and return the entire content of a file as a string.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: Content of the file
    """
    with open(file_path, 'r') as file:
        return file.read()


def read_file_lines(file_path):
    """
    Read and return the content of a file as a list of lines.
    Strip newline characters from each line.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        list: List of strings, each representing a line from the file
    """
    with open(file_path, 'r') as file:
        return [line.rstrip('\n') for line in file]


def write_lines_to_file(file_path, lines):
    """
    Write a list of strings to a file, with each string on a new line.
    
    Args:
        file_path (str): Path to the file
        lines (list): List of strings to write
        
    Returns:
        None
    """
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')


def append_to_file(file_path, text):
    """
    Append text to the end of a file.
    
    Args:
        file_path (str): Path to the file
        text (str): Text to append
        
    Returns:
        None
    """
    with open(file_path, 'a') as file:
        file.write(text + '\n')


def count_words_in_file(file_path):
    """
    Count the number of words in a file.
    Words are separated by whitespace.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        int: Number of words in the file
    """
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)


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