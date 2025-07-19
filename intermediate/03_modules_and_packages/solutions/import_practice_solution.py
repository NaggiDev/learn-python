"""
Import Practice - Solution

Demonstrates various import techniques and best practices.
This solution shows how to properly import and use modules.

Author: Python Learning Path
Version: 1.0
"""

# Different import methods for the calculator module
import sys
import os

# Add the solutions directory to the path so we can import our modules
sys.path.append(os.path.dirname(__file__))

# Method 1: Import entire module
import calculator

# Method 2: Import specific functions
from calculator import add, subtract

# Method 3: Import with alias
import calculator as calc

# Method 4: Import text processor module
import text_processor as tp

def demonstrate_imports():
    """Demonstrate different import methods."""
    print("Import Demonstration:")
    print("=" * 30)
    
    # Using full module name
    result1 = calculator.add(5, 3)
    print(f"Using full module name: calculator.add(5, 3) = {result1}")
    
    # Using imported function directly
    result2 = add(5, 3)
    print(f"Using imported function: add(5, 3) = {result2}")
    
    # Using alias
    result3 = calc.multiply(4, 6)
    print(f"Using alias: calc.multiply(4, 6) = {result3}")
    
    # Using text processor with alias
    word_count = tp.word_count("Hello world Python")
    print(f"Using text processor: tp.word_count('Hello world Python') = {word_count}")
    
    # Demonstrating that different import methods access the same functions
    print(f"\nVerifying same function: calculator.add is add = {calculator.add is add}")
    print(f"Verifying same module: calculator is calc = {calculator is calc}")

def safe_import_demo():
    """Demonstrate safe importing with error handling."""
    print("\nSafe Import Demonstration:")
    print("=" * 30)
    
    # Try to import a module that doesn't exist
    try:
        import nonexistent_module
        print("Successfully imported nonexistent_module")
    except ImportError as e:
        print(f"Failed to import nonexistent_module: {e}")
    
    # Try importing optional dependencies
    optional_modules = ['requests', 'numpy', 'pandas', 'matplotlib']
    
    for module_name in optional_modules:
        try:
            __import__(module_name)
            print(f"✓ {module_name} is available")
        except ImportError:
            print(f"✗ {module_name} is not available")
    
    # Conditional import example
    try:
        import json
        JSON_MODULE = json
        print("Using built-in json module")
    except ImportError:
        try:
            import simplejson as json
            JSON_MODULE = json
            print("Using simplejson module")
        except ImportError:
            JSON_MODULE = None
            print("No JSON module available")
    
    if JSON_MODULE:
        data = {"name": "Python", "type": "language"}
        json_string = JSON_MODULE.dumps(data)
        print(f"JSON string: {json_string}")

def module_introspection():
    """Explore module attributes and help."""
    print("\nModule Introspection:")
    print("=" * 30)
    
    # Explore calculator module attributes
    print(f"Calculator module name: {calculator.__name__}")
    print(f"Calculator module file: {getattr(calculator, '__file__', 'Built-in')}")
    print(f"Calculator module docstring: {calculator.__doc__}")
    
    # List all attributes
    calc_attributes = [attr for attr in dir(calculator) if not attr.startswith('_')]
    print(f"Calculator public attributes: {calc_attributes}")
    
    # Get function signatures and docstrings
    print(f"\nFunction details:")
    for attr_name in calc_attributes:
        attr = getattr(calculator, attr_name)
        if callable(attr):
            print(f"  {attr_name}: {attr.__doc__.split('.')[0] if attr.__doc__ else 'No docstring'}")

def conditional_imports():
    """Demonstrate conditional imports based on availability."""
    print("\nConditional Imports:")
    print("=" * 30)
    
    # Pattern 1: Try multiple alternatives
    math_module = None
    try:
        import math
        math_module = math
        print("Using built-in math module")
    except ImportError:
        try:
            import numpy as math
            math_module = math
            print("Using numpy as math module")
        except ImportError:
            print("No math module available")
    
    if math_module:
        print(f"π = {math_module.pi}")
        print(f"sqrt(16) = {math_module.sqrt(16)}")
    
    # Pattern 2: Feature flags based on availability
    features = {}
    
    # Check for advanced text processing
    try:
        import re
        features['regex'] = True
        print("✓ Regular expressions available")
    except ImportError:
        features['regex'] = False
        print("✗ Regular expressions not available")
    
    # Check for file operations
    try:
        import os
        features['file_ops'] = True
        print("✓ File operations available")
    except ImportError:
        features['file_ops'] = False
        print("✗ File operations not available")
    
    print(f"Available features: {features}")

def import_from_different_locations():
    """Demonstrate importing from different locations."""
    print("\nImporting from Different Locations:")
    print("=" * 30)
    
    # Standard library
    import datetime
    print(f"Current time: {datetime.datetime.now()}")
    
    # Built-in modules
    import sys
    print(f"Python version: {sys.version_info}")
    
    # Local modules (our calculator and text_processor)
    print(f"Local calculator module: {calculator.__name__}")
    print(f"Local text processor module: {tp.__name__}")
    
    # Show module search path
    print(f"\nPython module search path (first 3 entries):")
    for i, path in enumerate(sys.path[:3]):
        print(f"  {i+1}. {path}")

def main():
    """Run all import demonstrations."""
    print("Python Import Practice - Solution")
    print("=" * 50)
    
    demonstrate_imports()
    safe_import_demo()
    module_introspection()
    conditional_imports()
    import_from_different_locations()
    
    print("\n" + "=" * 50)
    print("Import practice completed successfully!")
    
    # Bonus: Show how to reload a module (advanced topic)
    print("\nBonus - Module Reloading:")
    import importlib
    print("You can reload a module using importlib.reload(module)")
    print("This is useful during development but should be avoided in production")

if __name__ == "__main__":
    main()