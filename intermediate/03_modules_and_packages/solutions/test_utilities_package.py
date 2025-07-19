"""
Test script for the utilities package.

This script demonstrates how to use the utilities package and tests
all its functionality.
"""

import sys
import os
import tempfile
import json

# Add the solutions directory to the path
sys.path.insert(0, os.path.dirname(__file__))

def test_string_tools():
    """Test string tools functionality."""
    print("Testing String Tools:")
    print("-" * 20)
    
    # Import string tools
    from utilities.string_tools import formatters, validators
    from utilities import capitalize_words, is_email  # Test package-level imports
    
    # Test formatters
    print("Formatters:")
    print(f"  capitalize_words('hello world'): {formatters.capitalize_words('hello world')}")
    print(f"  snake_to_camel('hello_world_python'): {formatters.snake_to_camel('hello_world_python')}")
    print(f"  camel_to_snake('helloWorldPython'): {formatters.camel_to_snake('helloWorldPython')}")
    print(f"  format_phone('1234567890'): {formatters.format_phone('1234567890')}")
    print(f"  truncate_text('This is a long text', 10): {formatters.truncate_text('This is a long text', 10)}")
    
    # Test validators
    print("\nValidators:")
    print(f"  is_email('test@example.com'): {validators.is_email('test@example.com')}")
    print(f"  is_phone('(123) 456-7890'): {validators.is_phone('(123) 456-7890')}")
    print(f"  is_url('https://www.example.com'): {validators.is_url('https://www.example.com')}")
    print(f"  is_strong_password('MyPass123!'): {validators.is_strong_password('MyPass123!')}")
    print(f"  contains_only_letters('HelloWorld'): {validators.contains_only_letters('HelloWorld')}")
    
    # Test package-level imports
    print(f"\nPackage-level imports:")
    print(f"  capitalize_words('package test'): {capitalize_words('package test')}")
    print(f"  is_email('package@test.com'): {is_email('package@test.com')}")

def test_math_tools():
    """Test math tools functionality."""
    print("\nTesting Math Tools:")
    print("-" * 20)
    
    # Import math tools
    from utilities.math_tools import basic, advanced
    from utilities import add, factorial  # Test package-level imports
    
    # Test basic operations
    print("Basic Operations:")
    print(f"  add(5, 3): {basic.add(5, 3)}")
    print(f"  subtract(10, 4): {basic.subtract(10, 4)}")
    print(f"  multiply(6, 7): {basic.multiply(6, 7)}")
    print(f"  divide(15, 3): {basic.divide(15, 3)}")
    print(f"  percentage(25, 100): {basic.percentage(25, 100)}")
    
    # Test advanced operations
    print("\nAdvanced Operations:")
    print(f"  factorial(5): {advanced.factorial(5)}")
    print(f"  fibonacci(10): {advanced.fibonacci(10)}")
    print(f"  is_prime(17): {advanced.is_prime(17)}")
    print(f"  gcd(48, 18): {advanced.gcd(48, 18)}")
    print(f"  lcm(12, 18): {advanced.lcm(12, 18)}")
    
    # Test package-level imports
    print(f"\nPackage-level imports:")
    print(f"  add(10, 20): {add(10, 20)}")
    print(f"  factorial(4): {factorial(4)}")
    
    # Test error handling
    print("\nError Handling:")
    try:
        basic.divide(10, 0)
    except ValueError as e:
        print(f"  Division by zero handled: {e}")

def test_file_tools():
    """Test file tools functionality."""
    print("\nTesting File Tools:")
    print("-" * 20)
    
    # Import file tools
    from utilities.file_tools import readers, writers
    from utilities import read_text_file, write_text_file  # Test package-level imports
    
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test text file operations
        text_file = os.path.join(temp_dir, "test.txt")
        test_content = "Hello, World!\nThis is a test file."
        
        print("Text File Operations:")
        writers.write_text_file(text_file, test_content)
        print(f"  Wrote text file: {text_file}")
        
        content = readers.read_text_file(text_file)
        print(f"  Read text file: {len(content)} characters")
        
        line_count = readers.count_lines(text_file)
        print(f"  Line count: {line_count}")
        
        file_size = readers.get_file_size(text_file)
        print(f"  File size: {file_size} bytes")
        
        # Test JSON file operations
        json_file = os.path.join(temp_dir, "test.json")
        test_data = {"name": "Python", "version": "3.9", "features": ["modules", "packages"]}
        
        print("\nJSON File Operations:")
        writers.write_json_file(json_file, test_data)
        print(f"  Wrote JSON file: {json_file}")
        
        json_data = readers.read_json_file(json_file)
        print(f"  Read JSON file: {json_data['name']} v{json_data['version']}")
        
        # Test CSV file operations
        csv_file = os.path.join(temp_dir, "test.csv")
        csv_data = [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 25, "city": "San Francisco"},
            {"name": "Charlie", "age": 35, "city": "Chicago"}
        ]
        
        print("\nCSV File Operations:")
        writers.write_csv_file(csv_file, csv_data)
        print(f"  Wrote CSV file: {csv_file}")
        
        csv_content = readers.read_csv_file(csv_file)
        print(f"  Read CSV file: {len(csv_content)} rows")
        print(f"  First row: {csv_content[0]}")
        
        # Test append operation
        writers.append_to_file(text_file, "\nAppended line.")
        updated_content = readers.read_text_file(text_file)
        print(f"\nAppend Operation:")
        print(f"  Updated file length: {len(updated_content)} characters")
        
        # Test backup creation
        backup_path = writers.create_backup(text_file)
        print(f"  Created backup: {os.path.basename(backup_path)}")
        
        # Test package-level imports
        print(f"\nPackage-level imports:")
        write_text_file(os.path.join(temp_dir, "package_test.txt"), "Package level test")
        package_content = read_text_file(os.path.join(temp_dir, "package_test.txt"))
        print(f"  Package-level file operations: {len(package_content)} characters")

def test_import_methods():
    """Test different import methods."""
    print("\nTesting Import Methods:")
    print("-" * 20)
    
    # Method 1: Import entire package
    import utilities
    print("Method 1 - Import entire package:")
    print(f"  utilities.add(1, 2): {utilities.add(1, 2)}")
    
    # Method 2: Import subpackages
    from utilities import string_tools, math_tools
    print("\nMethod 2 - Import subpackages:")
    print(f"  string_tools.capitalize_words('test'): {string_tools.capitalize_words('test')}")
    print(f"  math_tools.add(3, 4): {math_tools.add(3, 4)}")
    
    # Method 3: Import specific modules
    from utilities.string_tools import formatters
    from utilities.math_tools import advanced
    print("\nMethod 3 - Import specific modules:")
    print(f"  formatters.snake_to_camel('test_case'): {formatters.snake_to_camel('test_case')}")
    print(f"  advanced.fibonacci(7): {advanced.fibonacci(7)}")
    
    # Method 4: Import specific functions
    from utilities.string_tools.validators import is_email
    from utilities.math_tools.basic import multiply
    print("\nMethod 4 - Import specific functions:")
    print(f"  is_email('direct@import.com'): {is_email('direct@import.com')}")
    print(f"  multiply(7, 8): {multiply(7, 8)}")

def test_package_introspection():
    """Test package introspection capabilities."""
    print("\nTesting Package Introspection:")
    print("-" * 20)
    
    import utilities
    
    print(f"Package name: {utilities.__name__}")
    print(f"Package version: {utilities.__version__}")
    print(f"Package author: {utilities.__author__}")
    
    # List package contents
    public_attrs = [attr for attr in dir(utilities) if not attr.startswith('_')]
    print(f"Public attributes: {public_attrs}")
    
    # Check __all__ attribute
    if hasattr(utilities, '__all__'):
        print(f"__all__ contents: {utilities.__all__}")

def main():
    """Run all tests."""
    print("Utilities Package Test Suite")
    print("=" * 50)
    
    try:
        test_string_tools()
        test_math_tools()
        test_file_tools()
        test_import_methods()
        test_package_introspection()
        
        print("\n" + "=" * 50)
        print("All tests completed successfully!")
        print("\nThe utilities package is working correctly.")
        print("You can now use it in your own projects!")
        
    except ImportError as e:
        print(f"Import Error: {e}")
        print("Make sure the utilities package is properly created.")
    except Exception as e:
        print(f"Test Error: {e}")
        print("There was an error during testing.")

if __name__ == "__main__":
    main()