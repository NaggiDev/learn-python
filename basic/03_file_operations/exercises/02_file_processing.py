"""
Exercise: File Processing

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

This exercise covers:
- Processing files line by line
- Filtering file content
- Modifying file content
- Working with file paths
"""

import os
from pathlib import Path


def count_lines_in_file(file_path):
    """
    Count the number of lines in a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        int: Number of lines in the file
    """
    # TODO: Implement this function
    pass


def find_lines_containing(file_path, search_string):
    """
    Find all lines in a file that contain a specific string.
    
    Args:
        file_path (str): Path to the file
        search_string (str): String to search for
        
    Returns:
        list: List of lines containing the search string
    """
    # TODO: Implement this function
    pass


def replace_in_file(input_path, output_path, old_string, new_string):
    """
    Create a new file with all occurrences of old_string replaced by new_string.
    
    Args:
        input_path (str): Path to the input file
        output_path (str): Path to the output file
        old_string (str): String to replace
        new_string (str): Replacement string
        
    Returns:
        int: Number of replacements made
    """
    # TODO: Implement this function
    pass


def merge_files(file_paths, output_path):
    """
    Merge multiple text files into a single file.
    
    Args:
        file_paths (list): List of paths to the input files
        output_path (str): Path to the output file
        
    Returns:
        int: Total number of lines in the merged file
    """
    # TODO: Implement this function
    pass


def get_file_info(file_path):
    """
    Get information about a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        dict: Dictionary containing:
            - 'size': File size in bytes
            - 'modified': Last modified timestamp
            - 'extension': File extension
            - 'directory': Directory containing the file
    """
    # TODO: Implement this function
    pass


# Test functions
def test_file_processing():
    # Create test files
    os.makedirs("test_dir", exist_ok=True)
    
    # Test file 1
    with open("test_dir/file1.txt", "w") as f:
        f.write("This is line 1\nThis is line 2\nThis contains python\nThis is line 4\n")
    
    # Test file 2
    with open("test_dir/file2.txt", "w") as f:
        f.write("File 2 line 1\nFile 2 line 2\nFile 2 contains PYTHON\n")
    
    # Test count_lines_in_file
    line_count = count_lines_in_file("test_dir/file1.txt")
    assert line_count == 4, f"Expected 4 lines, got {line_count}"
    
    # Test find_lines_containing
    python_lines = find_lines_containing("test_dir/file1.txt", "python")
    assert len(python_lines) == 1, f"Expected 1 line containing 'python', got {len(python_lines)}"
    assert python_lines[0] == "This contains python", f"Expected 'This contains python', got '{python_lines[0]}'"
    
    # Test replace_in_file
    replacements = replace_in_file("test_dir/file1.txt", "test_dir/file1_modified.txt", "line", "row")
    assert replacements == 3, f"Expected 3 replacements, got {replacements}"
    
    with open("test_dir/file1_modified.txt", "r") as f:
        content = f.read()
    assert "This is row 1" in content, "Replacement failed"
    
    # Test merge_files
    total_lines = merge_files(["test_dir/file1.txt", "test_dir/file2.txt"], "test_dir/merged.txt")
    assert total_lines == 7, f"Expected 7 lines in merged file, got {total_lines}"
    
    with open("test_dir/merged.txt", "r") as f:
        merged_content = f.read()
    assert "This is line 1" in merged_content and "File 2 line 1" in merged_content, "Merge failed"
    
    # Test get_file_info
    file_info = get_file_info("test_dir/file1.txt")
    assert "size" in file_info, "File info missing 'size'"
    assert "modified" in file_info, "File info missing 'modified'"
    assert file_info["extension"] == ".txt", f"Expected extension '.txt', got '{file_info['extension']}'"
    assert os.path.basename(file_info["directory"]) == "test_dir", f"Expected directory 'test_dir', got '{file_info['directory']}'"
    
    # Clean up
    for file in ["test_dir/file1.txt", "test_dir/file2.txt", "test_dir/file1_modified.txt", "test_dir/merged.txt"]:
        if os.path.exists(file):
            os.remove(file)
    os.rmdir("test_dir")
    
    print("All tests passed!")


if __name__ == "__main__":
    test_file_processing()