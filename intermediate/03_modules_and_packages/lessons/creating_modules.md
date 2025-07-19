# Creating Modules

## What is a Module?

A module in Python is simply a file containing Python code. It can define functions, classes, and variables, and can also include runnable code. Modules allow you to organize your code logically and reuse it across different programs.

## Why Use Modules?

1. **Code Organization**: Break large programs into smaller, manageable files
2. **Code Reusability**: Write once, use many times
3. **Namespace Management**: Avoid naming conflicts
4. **Maintainability**: Easier to debug and update specific functionality
5. **Collaboration**: Team members can work on different modules independently

## Creating Your First Module

Let's create a simple module called `math_utils.py`:

```python
# math_utils.py
"""
A utility module for mathematical operations.
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Module-level variable
PI = 3.14159

# This code runs when the module is imported
print(f"Math utils module loaded. PI = {PI}")
```

## Importing Modules

There are several ways to import modules:

### 1. Import the entire module

```python
import math_utils

result = math_utils.add(5, 3)
print(f"5 + 3 = {result}")
print(f"PI = {math_utils.PI}")
```

### 2. Import specific functions/variables

```python
from math_utils import add, PI

result = add(5, 3)
print(f"5 + 3 = {result}")
print(f"PI = {PI}")
```

### 3. Import with an alias

```python
import math_utils as mu

result = mu.multiply(4, 7)
print(f"4 * 7 = {result}")
```

### 4. Import all (not recommended)

```python
from math_utils import *

result = factorial(5)
print(f"5! = {result}")
```

**Note**: Using `import *` is generally discouraged as it can lead to namespace pollution and make code harder to understand.

## The `__name__` Variable

Every module has a built-in variable called `__name__`. When a module is run directly, `__name__` is set to `"__main__"`. When imported, `__name__` is set to the module's name.

```python
# math_utils.py (updated)
"""
A utility module for mathematical operations.
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

PI = 3.14159

def main():
    """Main function for testing the module."""
    print("Testing math_utils module:")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"multiply(4, 5) = {multiply(4, 5)}")

# This block only runs when the script is executed directly
if __name__ == "__main__":
    main()
```

## Module Search Path

Python looks for modules in the following order:

1. Current directory
2. PYTHONPATH environment variable directories
3. Standard library directories
4. Site-packages directory

You can check the search path:

```python
import sys
print(sys.path)
```

## Module Documentation

Good modules should include documentation:

```python
# string_utils.py
"""
String utility functions for common text processing tasks.

This module provides functions for:
- Text cleaning and formatting
- String validation
- Text analysis

Author: Your Name
Version: 1.0
"""

def clean_text(text):
    """
    Clean and normalize text by removing extra whitespace.
    
    Args:
        text (str): The input text to clean
        
    Returns:
        str: Cleaned text with normalized whitespace
        
    Example:
        >>> clean_text("  Hello   World  ")
        'Hello World'
    """
    return ' '.join(text.split())

def is_email(email):
    """
    Check if a string is a valid email format.
    
    Args:
        email (str): Email string to validate
        
    Returns:
        bool: True if email format is valid, False otherwise
        
    Example:
        >>> is_email("user@example.com")
        True
        >>> is_email("invalid-email")
        False
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def word_count(text):
    """
    Count the number of words in a text.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Number of words in the text
        
    Example:
        >>> word_count("Hello world")
        2
    """
    return len(text.split())

# Module metadata
__version__ = "1.0"
__author__ = "Your Name"
```

## Best Practices for Module Creation

1. **Use descriptive names**: Module names should be lowercase with underscores
2. **Include docstrings**: Document your module, functions, and classes
3. **Keep modules focused**: Each module should have a single, clear purpose
4. **Use `if __name__ == "__main__":`**: Allow modules to be both imported and run
5. **Handle imports gracefully**: Use try/except for optional dependencies
6. **Follow PEP 8**: Maintain consistent code style

## Common Pitfalls

1. **Circular imports**: Module A imports Module B, which imports Module A
2. **Modifying sys.path**: Generally avoid changing the module search path
3. **Global state**: Be careful with module-level variables that change
4. **Import side effects**: Minimize code that runs during import

## Example: A Complete Module

Here's a complete example of a well-structured module:

```python
# file_utils.py
"""
File utility functions for common file operations.

This module provides safe and convenient functions for:
- Reading and writing files
- File system operations
- File validation

Author: Python Learning Path
Version: 1.0
Date: 2024
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

__version__ = "1.0"
__author__ = "Python Learning Path"

def read_text_file(filepath: str, encoding: str = 'utf-8') -> str:
    """
    Safely read a text file and return its contents.
    
    Args:
        filepath (str): Path to the file
        encoding (str): File encoding (default: utf-8)
        
    Returns:
        str: File contents
        
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file cannot be read
    """
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading file {filepath}: {e}")

def write_text_file(filepath: str, content: str, encoding: str = 'utf-8') -> None:
    """
    Safely write content to a text file.
    
    Args:
        filepath (str): Path to the file
        content (str): Content to write
        encoding (str): File encoding (default: utf-8)
        
    Raises:
        IOError: If file cannot be written
    """
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding=encoding) as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Error writing file {filepath}: {e}")

def file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    return os.path.isfile(filepath)

def get_file_size(filepath: str) -> int:
    """
    Get the size of a file in bytes.
    
    Args:
        filepath (str): Path to the file
        
    Returns:
        int: File size in bytes
        
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not file_exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return os.path.getsize(filepath)

def main():
    """Test the file utilities."""
    test_file = "test.txt"
    test_content = "Hello, World!\nThis is a test file."
    
    print("Testing file utilities:")
    
    # Write test file
    write_text_file(test_file, test_content)
    print(f"✓ Created {test_file}")
    
    # Read test file
    content = read_text_file(test_file)
    print(f"✓ Read {test_file}: {len(content)} characters")
    
    # Check file size
    size = get_file_size(test_file)
    print(f"✓ File size: {size} bytes")
    
    # Clean up
    os.remove(test_file)
    print(f"✓ Cleaned up {test_file}")

if __name__ == "__main__":
    main()
```

This module demonstrates:
- Clear documentation and type hints
- Error handling
- Proper use of `if __name__ == "__main__"`
- Following Python conventions
- Practical, reusable functions

In the next lesson, we'll explore how to organize multiple modules into packages.