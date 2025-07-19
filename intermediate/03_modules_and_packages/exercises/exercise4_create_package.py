"""
Exercise 4: Create a Package

Instructions:
1. Create a package called 'utilities' with the following structure:
   utilities/
       __init__.py
       string_tools/
           __init__.py
           formatters.py
           validators.py
       math_tools/
           __init__.py
           basic.py
           advanced.py
       file_tools/
           __init__.py
           readers.py
           writers.py

2. Implement the modules with useful functions
3. Set up proper __init__.py files to control the package API
4. Create a test script to demonstrate the package usage

This exercise will be completed by creating the actual package structure
in the same directory as this file.
"""

# TODO: Create the package structure described above
# Start by creating the directories and __init__.py files

# Package structure to create:
"""
utilities/
    __init__.py                 # Main package init
    string_tools/
        __init__.py            # String tools subpackage init
        formatters.py          # String formatting functions
        validators.py          # String validation functions
    math_tools/
        __init__.py            # Math tools subpackage init
        basic.py               # Basic math operations
        advanced.py            # Advanced math operations
    file_tools/
        __init__.py            # File tools subpackage init
        readers.py             # File reading utilities
        writers.py             # File writing utilities
"""

# Functions to implement in each module:

# utilities/string_tools/formatters.py
"""
Functions to implement:
- capitalize_words(text) -> str
- snake_to_camel(text) -> str
- camel_to_snake(text) -> str
- format_phone(phone) -> str
- truncate_text(text, max_length) -> str
"""

# utilities/string_tools/validators.py
"""
Functions to implement:
- is_email(email) -> bool
- is_phone(phone) -> bool
- is_url(url) -> bool
- is_strong_password(password) -> bool
- contains_only_letters(text) -> bool
"""

# utilities/math_tools/basic.py
"""
Functions to implement:
- add(a, b) -> number
- subtract(a, b) -> number
- multiply(a, b) -> number
- divide(a, b) -> float
- percentage(part, whole) -> float
"""

# utilities/math_tools/advanced.py
"""
Functions to implement:
- factorial(n) -> int
- fibonacci(n) -> int
- is_prime(n) -> bool
- gcd(a, b) -> int
- lcm(a, b) -> int
"""

# utilities/file_tools/readers.py
"""
Functions to implement:
- read_text_file(filepath) -> str
- read_json_file(filepath) -> dict
- read_csv_file(filepath) -> list
- count_lines(filepath) -> int
- get_file_size(filepath) -> int
"""

# utilities/file_tools/writers.py
"""
Functions to implement:
- write_text_file(filepath, content) -> None
- write_json_file(filepath, data) -> None
- write_csv_file(filepath, data) -> None
- append_to_file(filepath, content) -> None
- create_backup(filepath) -> str
"""

def test_package():
    """
    Test the utilities package after creation.
    
    This function should import and test various functions from the package.
    """
    print("Testing Utilities Package:")
    print("=" * 30)
    
    try:
        # TODO: Import and test functions from the utilities package
        # Example imports (uncomment after creating the package):
        
        # from utilities.string_tools import capitalize_words, is_email
        # from utilities.math_tools import add, factorial
        # from utilities.file_tools import read_text_file, write_text_file
        
        # Test string tools
        # result = capitalize_words("hello world")
        # print(f"capitalize_words('hello world') = {result}")
        
        # Test math tools
        # result = add(5, 3)
        # print(f"add(5, 3) = {result}")
        
        # Test file tools
        # write_text_file("test.txt", "Hello, World!")
        # content = read_text_file("test.txt")
        # print(f"File content: {content}")
        
        print("Package tests completed successfully!")
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure you've created the package structure first!")
    except Exception as e:
        print(f"Error testing package: {e}")

def main():
    """Main function to run the exercise."""
    print("Package Creation Exercise")
    print("=" * 40)
    print("1. Create the utilities package structure")
    print("2. Implement all the required functions")
    print("3. Set up proper __init__.py files")
    print("4. Run this script to test your package")
    print()
    
    test_package()

if __name__ == "__main__":
    main()

# Instructions for completing this exercise:
# 1. Create the directory structure as shown above
# 2. Implement all the functions in their respective modules
# 3. Create proper __init__.py files that import the functions
# 4. Test your package by running this script
# 5. Try different import methods to access your functions