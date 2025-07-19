"""
Exercise 5: Package Import Techniques

Instructions:
1. Practice different ways of importing from packages
2. Understand the difference between absolute and relative imports
3. Work with nested package structures
4. Handle import errors gracefully

This exercise assumes you have completed Exercise 4 (creating the utilities package).
"""

import sys
import os

def demonstrate_absolute_imports():
    """Demonstrate absolute import techniques."""
    print("Absolute Import Techniques:")
    print("-" * 30)
    
    try:
        # TODO: Try different absolute import methods
        
        # Method 1: Import entire package
        # import utilities
        # print(f"Imported utilities package: {utilities}")
        
        # Method 2: Import subpackages
        # from utilities import string_tools, math_tools
        # print("Imported string_tools and math_tools subpackages")
        
        # Method 3: Import specific modules
        # from utilities.string_tools import formatters, validators
        # print("Imported formatters and validators modules")
        
        # Method 4: Import specific functions
        # from utilities.string_tools.formatters import capitalize_words
        # from utilities.math_tools.basic import add, multiply
        # print("Imported specific functions")
        
        # Test the imported functions
        # result = capitalize_words("hello world")
        # print(f"capitalize_words result: {result}")
        
        # result = add(5, 3)
        # print(f"add(5, 3) = {result}")
        
        print("Absolute imports completed successfully!")
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure the utilities package is created and in the correct location")

def demonstrate_import_aliases():
    """Demonstrate importing with aliases."""
    print("\nImport Aliases:")
    print("-" * 30)
    
    try:
        # TODO: Import with aliases
        
        # Import subpackages with aliases
        # from utilities import string_tools as st, math_tools as mt
        # print("Imported with aliases: st (string_tools), mt (math_tools)")
        
        # Import modules with aliases
        # from utilities.string_tools import formatters as fmt
        # from utilities.math_tools import advanced as adv_math
        # print("Imported modules with aliases")
        
        # Test aliased imports
        # result = fmt.capitalize_words("python programming")
        # print(f"Using alias fmt: {result}")
        
        # result = adv_math.factorial(5)
        # print(f"Using alias adv_math: factorial(5) = {result}")
        
        print("Import aliases completed successfully!")
        
    except ImportError as e:
        print(f"Import error: {e}")

def demonstrate_selective_imports():
    """Demonstrate selective importing."""
    print("\nSelective Imports:")
    print("-" * 30)
    
    try:
        # TODO: Import only what you need
        
        # Import only specific functions you'll use
        # from utilities.string_tools.validators import is_email, is_phone
        # from utilities.math_tools.advanced import is_prime, fibonacci
        # from utilities.file_tools.readers import read_text_file
        
        # Test selective imports
        # print(f"is_email('test@example.com'): {is_email('test@example.com')}")
        # print(f"is_prime(17): {is_prime(17)}")
        # print(f"fibonacci(10): {fibonacci(10)}")
        
        print("Selective imports completed successfully!")
        
    except ImportError as e:
        print(f"Import error: {e}")

def demonstrate_conditional_imports():
    """Demonstrate conditional importing based on availability."""
    print("\nConditional Imports:")
    print("-" * 30)
    
    # Try to import optional functionality
    string_tools_available = False
    math_tools_available = False
    file_tools_available = False
    
    try:
        from utilities import string_tools
        string_tools_available = True
        print("✓ String tools available")
    except ImportError:
        print("✗ String tools not available")
    
    try:
        from utilities import math_tools
        math_tools_available = True
        print("✓ Math tools available")
    except ImportError:
        print("✗ Math tools not available")
    
    try:
        from utilities import file_tools
        file_tools_available = True
        print("✓ File tools available")
    except ImportError:
        print("✗ File tools not available")
    
    # Use available tools
    if string_tools_available:
        try:
            from utilities.string_tools.formatters import capitalize_words
            result = capitalize_words("conditional import test")
            print(f"String tool result: {result}")
        except (ImportError, AttributeError) as e:
            print(f"Error using string tools: {e}")
    
    if math_tools_available:
        try:
            from utilities.math_tools.basic import add
            result = add(10, 20)
            print(f"Math tool result: {result}")
        except (ImportError, AttributeError) as e:
            print(f"Error using math tools: {e}")

def demonstrate_import_introspection():
    """Demonstrate package and module introspection."""
    print("\nImport Introspection:")
    print("-" * 30)
    
    try:
        # TODO: Explore package structure programmatically
        
        # Import the main package
        # import utilities
        
        # Explore package attributes
        # print(f"Package name: {utilities.__name__}")
        # print(f"Package file: {getattr(utilities, '__file__', 'No file')}")
        # print(f"Package path: {getattr(utilities, '__path__', 'No path')}")
        
        # List package contents
        # package_contents = [item for item in dir(utilities) if not item.startswith('_')]
        # print(f"Package contents: {package_contents}")
        
        # Explore subpackages
        # from utilities import string_tools
        # subpackage_contents = [item for item in dir(string_tools) if not item.startswith('_')]
        # print(f"String tools contents: {subpackage_contents}")
        
        print("Import introspection completed!")
        
    except ImportError as e:
        print(f"Import error: {e}")

def demonstrate_dynamic_imports():
    """Demonstrate dynamic importing using importlib."""
    print("\nDynamic Imports:")
    print("-" * 30)
    
    import importlib
    
    # List of modules to try importing dynamically
    modules_to_import = [
        'utilities.string_tools.formatters',
        'utilities.math_tools.basic',
        'utilities.file_tools.readers'
    ]
    
    for module_name in modules_to_import:
        try:
            # Dynamic import
            module = importlib.import_module(module_name)
            print(f"✓ Successfully imported {module_name}")
            
            # List module functions
            functions = [item for item in dir(module) if not item.startswith('_') and callable(getattr(module, item))]
            print(f"  Functions: {functions}")
            
        except ImportError as e:
            print(f"✗ Failed to import {module_name}: {e}")

def test_package_api():
    """Test the package's public API."""
    print("\nTesting Package API:")
    print("-" * 30)
    
    try:
        # TODO: Test the main package API
        
        # Import from main package level (if configured in __init__.py)
        # from utilities import capitalize_words, add, is_email
        # print("Imported functions from main package level")
        
        # Test the functions
        # print(f"capitalize_words('api test'): {capitalize_words('api test')}")
        # print(f"add(15, 25): {add(15, 25)}")
        # print(f"is_email('api@test.com'): {is_email('api@test.com')}")
        
        print("Package API test completed!")
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure your __init__.py files are properly configured")

def main():
    """Run all import demonstrations."""
    print("Package Import Techniques Exercise")
    print("=" * 50)
    
    demonstrate_absolute_imports()
    demonstrate_import_aliases()
    demonstrate_selective_imports()
    demonstrate_conditional_imports()
    demonstrate_import_introspection()
    demonstrate_dynamic_imports()
    test_package_api()
    
    print("\n" + "=" * 50)
    print("Import techniques exercise completed!")
    print("\nKey takeaways:")
    print("1. Use absolute imports for clarity")
    print("2. Import only what you need")
    print("3. Use aliases for long package names")
    print("4. Handle import errors gracefully")
    print("5. Configure __init__.py files to control the public API")

if __name__ == "__main__":
    main()

# Additional exercises to try:
# 1. Create a script that imports functions from different subpackages
# 2. Experiment with the __all__ variable in __init__.py files
# 3. Try creating circular imports and see what happens
# 4. Practice with relative imports (create modules that import from each other)