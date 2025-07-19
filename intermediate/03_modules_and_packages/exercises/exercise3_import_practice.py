"""
Exercise 3: Import Practice

Instructions:
1. Practice different ways of importing modules
2. Create a main script that imports and uses functions from other modules
3. Demonstrate various import techniques
4. Handle import errors gracefully

This exercise assumes you have completed exercises 1 and 2.
"""

# TODO: Import the calculator module you created in exercise 1
# Try different import methods:

# Method 1: Import entire module
# import calculator

# Method 2: Import specific functions
# from calculator import add, subtract

# Method 3: Import with alias
# import calculator as calc

# Method 4: Import all (not recommended, but for learning)
# from calculator import *

def demonstrate_imports():
    """Demonstrate different import methods."""
    print("Import Demonstration:")
    print("=" * 30)
    
    # TODO: Use the calculator module with different import methods
    # Show how each import method works
    
    # Example tests:
    # print(f"Using full module name: calculator.add(5, 3) = {calculator.add(5, 3)}")
    # print(f"Using imported function: add(5, 3) = {add(5, 3)}")
    # print(f"Using alias: calc.multiply(4, 6) = {calc.multiply(4, 6)}")
    
    pass

def safe_import_demo():
    """Demonstrate safe importing with error handling."""
    print("\nSafe Import Demonstration:")
    print("=" * 30)
    
    # TODO: Try to import modules that might not exist
    # Use try/except to handle ImportError
    
    try:
        # Try to import a module that might not exist
        import nonexistent_module
        print("Successfully imported nonexistent_module")
    except ImportError as e:
        print(f"Failed to import: {e}")
    
    # TODO: Try importing optional dependencies
    try:
        import requests  # This might not be installed
        print("requests library is available")
    except ImportError:
        print("requests library is not available")
        print("You can install it with: pip install requests")

def module_introspection():
    """Explore module attributes and help."""
    print("\nModule Introspection:")
    print("=" * 30)
    
    # TODO: Import your calculator module and explore its attributes
    # Use dir(), help(), and __doc__ to inspect the module
    
    # Example:
    # import calculator
    # print(f"Calculator module attributes: {dir(calculator)}")
    # print(f"Calculator module docstring: {calculator.__doc__}")
    
    pass

def conditional_imports():
    """Demonstrate conditional imports based on availability."""
    print("\nConditional Imports:")
    print("=" * 30)
    
    # TODO: Implement conditional imports
    # Import different modules based on what's available
    
    # Example pattern:
    try:
        import json
        JSON_AVAILABLE = True
        print("Using built-in json module")
    except ImportError:
        try:
            import simplejson as json
            JSON_AVAILABLE = True
            print("Using simplejson module")
        except ImportError:
            JSON_AVAILABLE = False
            print("No JSON module available")
    
    if JSON_AVAILABLE:
        # Use json module
        data = {"name": "Python", "type": "language"}
        json_string = json.dumps(data)
        print(f"JSON string: {json_string}")

def main():
    """Run all import demonstrations."""
    print("Python Import Practice")
    print("=" * 50)
    
    demonstrate_imports()
    safe_import_demo()
    module_introspection()
    conditional_imports()
    
    print("\n" + "=" * 50)
    print("Import practice completed!")

if __name__ == "__main__":
    main()

# Additional exercises:
# 1. Create a script that imports and uses your text processor module
# 2. Try importing standard library modules (os, sys, datetime, etc.)
# 3. Practice with relative imports (we'll cover this in packages lesson)