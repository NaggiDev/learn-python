"""
DevTools - A comprehensive utility package for Python developers.

This package provides utilities for text processing, data manipulation,
system operations, and web development tasks.

Author: Python Learning Path
Version: 1.0.0
"""

# Import commonly used functions to package level
from .text import clean_text, word_count, analyze_readability
from .data import validate_email, convert_to_json, normalize_data
from .system import get_system_info, backup_file, get_env_var
from .web import validate_url, make_request, parse_json

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Learning Path"
__email__ = "learning@python.dev"
__description__ = "A comprehensive utility package for Python developers"

# Define what gets imported with "from devtools import *"
__all__ = [
    # Text utilities
    'clean_text', 'word_count', 'analyze_readability',
    # Data utilities
    'validate_email', 'convert_to_json', 'normalize_data',
    # System utilities
    'get_system_info', 'backup_file', 'get_env_var',
    # Web utilities
    'validate_url', 'make_request', 'parse_json'
]