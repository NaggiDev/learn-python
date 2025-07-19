"""
Utilities Package

A comprehensive collection of utility functions organized into subpackages:
- string_tools: String formatting and validation utilities
- math_tools: Mathematical operations and calculations
- file_tools: File reading and writing utilities

Author: Python Learning Path
Version: 1.0.0
"""

# Import commonly used functions to package level for convenience
from .string_tools.formatters import capitalize_words, snake_to_camel
from .string_tools.validators import is_email, is_phone
from .math_tools.basic import add, subtract, multiply, divide
from .math_tools.advanced import factorial, is_prime
from .file_tools.readers import read_text_file, read_json_file
from .file_tools.writers import write_text_file, write_json_file

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Learning Path"

# Define what gets imported with "from utilities import *"
__all__ = [
    # String tools
    'capitalize_words', 'snake_to_camel', 'is_email', 'is_phone',
    # Math tools
    'add', 'subtract', 'multiply', 'divide', 'factorial', 'is_prime',
    # File tools
    'read_text_file', 'read_json_file', 'write_text_file', 'write_json_file'
]