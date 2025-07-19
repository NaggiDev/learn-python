# Mini-Project: Custom Utility Package

## Project Overview

In this mini-project, you'll create a comprehensive utility package called `devtools` that demonstrates all the concepts learned in the Modules and Packages module. This package will include multiple subpackages, proper documentation, testing, and distribution setup.

## Learning Objectives

By completing this project, you will:

1. **Package Structure**: Create a well-organized package hierarchy
2. **Module Design**: Implement reusable utility functions
3. **Documentation**: Write comprehensive docstrings and README files
4. **Testing**: Create unit tests for your package
5. **Virtual Environments**: Set up isolated development environment
6. **Dependency Management**: Manage package dependencies properly
7. **Distribution**: Prepare package for distribution

## Project Requirements

### Core Features

Your `devtools` package should include the following subpackages:

1. **Text Processing** (`devtools.text`)
   - String manipulation utilities
   - Text analysis functions
   - File content processing

2. **Data Utilities** (`devtools.data`)
   - Data validation functions
   - Data transformation utilities
   - Format conversion tools

3. **System Utilities** (`devtools.system`)
   - File system operations
   - Environment variable management
   - System information gathering

4. **Web Utilities** (`devtools.web`)
   - URL validation and parsing
   - HTTP request helpers
   - JSON processing utilities

### Technical Requirements

1. **Package Structure**: Proper `__init__.py` files with controlled imports
2. **Documentation**: Comprehensive docstrings for all functions
3. **Type Hints**: Use type hints throughout the codebase
4. **Error Handling**: Proper exception handling with custom exceptions
5. **Testing**: Unit tests with at least 80% code coverage
6. **Dependencies**: Minimal external dependencies, properly managed
7. **Distribution**: Setup for package installation and distribution

## Project Structure

```
devtools/
├── devtools/                    # Main package directory
│   ├── __init__.py             # Main package init
│   ├── exceptions.py           # Custom exceptions
│   ├── text/                   # Text processing subpackage
│   │   ├── __init__.py
│   │   ├── analyzers.py        # Text analysis functions
│   │   ├── formatters.py       # Text formatting utilities
│   │   └── processors.py       # Text processing functions
│   ├── data/                   # Data utilities subpackage
│   │   ├── __init__.py
│   │   ├── validators.py       # Data validation functions
│   │   ├── converters.py       # Data conversion utilities
│   │   └── transformers.py     # Data transformation functions
│   ├── system/                 # System utilities subpackage
│   │   ├── __init__.py
│   │   ├── files.py           # File system operations
│   │   ├── environment.py     # Environment management
│   │   └── info.py            # System information
│   └── web/                    # Web utilities subpackage
│       ├── __init__.py
│       ├── urls.py            # URL utilities
│       ├── requests.py        # HTTP request helpers
│       └── json_utils.py      # JSON processing
├── tests/                      # Test directory
│   ├── __init__.py
│   ├── test_text/
│   ├── test_data/
│   ├── test_system/
│   └── test_web/
├── docs/                       # Documentation
│   ├── README.md
│   ├── API.md
│   └── examples/
├── requirements/               # Requirements files
│   ├── base.txt
│   ├── dev.txt
│   └── test.txt
├── setup.py                    # Package setup
├── setup.cfg                   # Setup configuration
├── pyproject.toml             # Modern Python packaging
├── README.md                   # Project README
├── LICENSE                     # License file
├── .gitignore                 # Git ignore file
└── Makefile                   # Development commands
```

## Implementation Steps

### Phase 1: Project Setup (30 minutes)

1. **Create Project Structure**
   ```bash
   mkdir devtools-project
   cd devtools-project
   mkdir -p devtools/{text,data,system,web}
   mkdir -p tests/{test_text,test_data,test_system,test_web}
   mkdir -p docs/examples
   mkdir requirements
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or venv\Scripts\activate  # Windows
   ```

3. **Create Basic Files**
   - Create all `__init__.py` files
   - Set up basic `setup.py`
   - Create requirements files
   - Initialize git repository

### Phase 2: Core Implementation (2-3 hours)

1. **Implement Text Processing Subpackage**
   - Text analysis functions (word count, readability, etc.)
   - Text formatting utilities (case conversion, cleaning, etc.)
   - Text processing functions (extraction, transformation, etc.)

2. **Implement Data Utilities Subpackage**
   - Data validation (email, phone, URL validation)
   - Data conversion (JSON, CSV, XML handling)
   - Data transformation (normalization, aggregation)

3. **Implement System Utilities Subpackage**
   - File operations (copy, move, backup)
   - Environment management (get/set variables)
   - System information (OS, Python version, disk space)

4. **Implement Web Utilities Subpackage**
   - URL parsing and validation
   - HTTP request helpers
   - JSON processing utilities

### Phase 3: Testing and Documentation (1-2 hours)

1. **Write Unit Tests**
   - Test all public functions
   - Include edge cases and error conditions
   - Aim for high code coverage

2. **Create Documentation**
   - Write comprehensive README
   - Document API with examples
   - Create usage examples

### Phase 4: Packaging and Distribution (30 minutes)

1. **Set Up Package Distribution**
   - Configure `setup.py` and `pyproject.toml`
   - Test package installation
   - Create distribution files

2. **Final Testing**
   - Test in clean environment
   - Verify all imports work
   - Run full test suite

## Starter Code

### Main Package `__init__.py`

```python
"""
DevTools - A comprehensive utility package for Python developers.

This package provides utilities for text processing, data manipulation,
system operations, and web development tasks.
"""

from .text import clean_text, word_count, analyze_readability
from .data import validate_email, convert_to_json, normalize_data
from .system import get_system_info, backup_file, get_env_var
from .web import validate_url, make_request, parse_json

__version__ = "1.0.0"
__author__ = "Python Learning Path"
__email__ = "learning@python.dev"

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
```

### Custom Exceptions

```python
"""Custom exceptions for the devtools package."""

class DevToolsError(Exception):
    """Base exception for devtools package."""
    pass

class ValidationError(DevToolsError):
    """Raised when data validation fails."""
    pass

class ProcessingError(DevToolsError):
    """Raised when data processing fails."""
    pass

class SystemError(DevToolsError):
    """Raised when system operations fail."""
    pass

class WebError(DevToolsError):
    """Raised when web operations fail."""
    pass
```

### Sample Function Implementation

```python
# devtools/text/analyzers.py
"""Text analysis utilities."""

import re
from typing import Dict, List
from ..exceptions import ProcessingError

def word_count(text: str) -> int:
    """
    Count the number of words in text.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        int: Number of words in the text
        
    Raises:
        ProcessingError: If text processing fails
        
    Example:
        >>> word_count("Hello world")
        2
        >>> word_count("")
        0
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    if not text.strip():
        return 0
    
    words = text.split()
    return len(words)

def analyze_readability(text: str) -> Dict[str, float]:
    """
    Analyze text readability using various metrics.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        Dict[str, float]: Dictionary with readability metrics
        
    Example:
        >>> metrics = analyze_readability("This is a simple sentence.")
        >>> 'avg_sentence_length' in metrics
        True
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    words = text.split()
    
    if not sentences or not words:
        return {
            'avg_sentence_length': 0.0,
            'avg_word_length': 0.0,
            'sentence_count': 0,
            'word_count': 0
        }
    
    avg_sentence_length = len(words) / len(sentences)
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    return {
        'avg_sentence_length': round(avg_sentence_length, 2),
        'avg_word_length': round(avg_word_length, 2),
        'sentence_count': len(sentences),
        'word_count': len(words)
    }
```

## Testing Requirements

### Sample Test File

```python
# tests/test_text/test_analyzers.py
"""Tests for text analysis utilities."""

import pytest
from devtools.text.analyzers import word_count, analyze_readability
from devtools.exceptions import ProcessingError

class TestWordCount:
    """Test word_count function."""
    
    def test_simple_text(self):
        """Test word count with simple text."""
        assert word_count("hello world") == 2
    
    def test_empty_string(self):
        """Test word count with empty string."""
        assert word_count("") == 0
    
    def test_whitespace_only(self):
        """Test word count with whitespace only."""
        assert word_count("   ") == 0
    
    def test_multiple_spaces(self):
        """Test word count with multiple spaces."""
        assert word_count("hello    world") == 2
    
    def test_invalid_input(self):
        """Test word count with invalid input."""
        with pytest.raises(ProcessingError):
            word_count(123)

class TestAnalyzeReadability:
    """Test analyze_readability function."""
    
    def test_simple_sentence(self):
        """Test readability analysis with simple sentence."""
        result = analyze_readability("This is a test.")
        assert result['sentence_count'] == 1
        assert result['word_count'] == 4
        assert result['avg_sentence_length'] == 4.0
    
    def test_empty_text(self):
        """Test readability analysis with empty text."""
        result = analyze_readability("")
        assert result['sentence_count'] == 0
        assert result['word_count'] == 0
```

## Evaluation Criteria

Your project will be evaluated on:

1. **Code Quality** (25%)
   - Clean, readable code
   - Proper naming conventions
   - Consistent style

2. **Package Structure** (20%)
   - Logical organization
   - Proper `__init__.py` files
   - Clear module separation

3. **Documentation** (20%)
   - Comprehensive docstrings
   - Clear README
   - Usage examples

4. **Testing** (20%)
   - Good test coverage
   - Edge case handling
   - Proper test organization

5. **Functionality** (15%)
   - All required features implemented
   - Functions work as specified
   - Error handling

## Bonus Features

For extra credit, consider implementing:

1. **Command Line Interface**: Add CLI commands using Click
2. **Configuration Management**: Support for config files
3. **Logging**: Comprehensive logging throughout the package
4. **Performance Optimization**: Optimize critical functions
5. **Additional Utilities**: More utility functions in each subpackage

## Submission Guidelines

1. **Code Repository**: Submit complete project in a Git repository
2. **Documentation**: Include comprehensive README and API documentation
3. **Tests**: All tests should pass with good coverage
4. **Demo**: Prepare a brief demonstration of your package
5. **Reflection**: Write a short reflection on what you learned

## Getting Started

1. Create the project structure as outlined above
2. Set up your virtual environment and dependencies
3. Start with one subpackage and implement it fully
4. Add tests as you implement each function
5. Document your code thoroughly
6. Test your package in a clean environment

Good luck with your custom utility package! This project will give you hands-on experience with all aspects of Python package development.