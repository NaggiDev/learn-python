# DevTools - Custom Utility Package

A comprehensive utility package for Python developers, created as part of the Python Learning Path modules and packages mini-project.

## 🎯 Project Overview

DevTools is a well-structured Python package that demonstrates best practices in:
- Package organization and structure
- Module design and implementation
- Documentation and testing
- Virtual environment management
- Dependency management
- Distribution setup

## 📦 Package Structure

```
devtools/
├── devtools/                    # Main package
│   ├── __init__.py             # Package initialization
│   ├── exceptions.py           # Custom exceptions
│   ├── text/                   # Text processing utilities
│   │   ├── analyzers.py        # Text analysis functions
│   │   ├── formatters.py       # Text formatting utilities
│   │   └── processors.py       # Text processing functions
│   ├── data/                   # Data utilities
│   │   ├── validators.py       # Data validation functions
│   │   ├── converters.py       # Data conversion utilities
│   │   └── transformers.py     # Data transformation functions
│   ├── system/                 # System utilities
│   │   ├── files.py           # File system operations
│   │   ├── environment.py     # Environment management
│   │   └── info.py            # System information
│   └── web/                    # Web utilities
│       ├── urls.py            # URL utilities
│       ├── requests.py        # HTTP request helpers
│       └── json_utils.py      # JSON processing
├── tests/                      # Comprehensive test suite
├── requirements/               # Environment-specific requirements
├── setup.py                    # Package setup configuration
└── docs/                       # Documentation
```

## 🚀 Quick Start

### 1. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements/dev.txt

# Install package in editable mode
pip install -e .
```

### 2. Basic Usage

```python
import devtools

# Text processing
text = "  Hello World  "
clean = devtools.clean_text(text)  # "Hello World"
words = devtools.word_count(text)  # 2

# Data validation
email_valid = devtools.validate_email("user@example.com")  # True
phone_valid = devtools.validate_phone("(123) 456-7890")   # True

# System operations
info = devtools.get_system_info()
backup = devtools.backup_file("important.txt")

# Web utilities
url_valid = devtools.validate_url("https://example.com")  # True
json_data = devtools.parse_json('{"name": "John"}')
```

### 3. Subpackage Usage

```python
# Text processing subpackage
from devtools.text import analyzers, formatters, processors

# Analyze text
metrics = analyzers.analyze_readability("This is a test sentence.")
print(f"Average sentence length: {metrics['avg_sentence_length']}")

# Format text
camel_case = formatters.snake_to_camel("hello_world")  # "helloWorld"
title = formatters.capitalize_words("hello world")     # "Hello World"

# Process text
emails = processors.extract_emails("Contact us at test@example.com")
clean_html = processors.remove_html_tags("<p>Hello <b>world</b></p>")
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=devtools

# Run specific test file
pytest tests/test_text/test_analyzers.py

# Run with verbose output
pytest -v
```

## 📋 Features

### Text Processing (`devtools.text`)
- **Analyzers**: Word count, readability analysis, character counting
- **Formatters**: Text cleaning, case conversion, title formatting
- **Processors**: Email extraction, HTML tag removal, text truncation

### Data Utilities (`devtools.data`)
- **Validators**: Email, phone, URL, JSON, password strength validation
- **Converters**: JSON, CSV, XML conversion utilities
- **Transformers**: Data normalization, flattening, grouping, aggregation

### System Utilities (`devtools.system`)
- **Files**: Backup, copy, file info, directory listing
- **Environment**: Environment variable management, path operations
- **Info**: System information, Python info, disk usage

### Web Utilities (`devtools.web`)
- **URLs**: URL validation, parsing, building, domain extraction
- **Requests**: HTTP requests, file downloads, status checking
- **JSON**: JSON parsing, formatting, schema validation

## 🛠️ Development

### Code Quality

```bash
# Format code
black devtools/

# Check code style
flake8 devtools/

# Type checking
mypy devtools/

# Sort imports
isort devtools/
```

### Adding New Features

1. Create new module in appropriate subpackage
2. Add comprehensive docstrings with examples
3. Include type hints
4. Write unit tests
5. Update `__init__.py` files
6. Update documentation

### Testing Guidelines

- Write tests for all public functions
- Include edge cases and error conditions
- Use descriptive test names
- Aim for high code coverage
- Test both success and failure scenarios

## 📚 API Documentation

### Text Processing

#### `devtools.text.analyzers`
- `word_count(text: str) -> int`: Count words in text
- `analyze_readability(text: str) -> Dict[str, float]`: Analyze text readability
- `count_characters(text: str, include_spaces: bool = True) -> int`: Count characters

#### `devtools.text.formatters`
- `clean_text(text: str) -> str`: Remove extra whitespace
- `capitalize_words(text: str) -> str`: Capitalize each word
- `snake_to_camel(text: str) -> str`: Convert snake_case to camelCase

### Data Utilities

#### `devtools.data.validators`
- `validate_email(email: str) -> bool`: Validate email format
- `validate_phone(phone: str) -> bool`: Validate phone number
- `validate_password_strength(password: str) -> dict`: Analyze password strength

#### `devtools.data.converters`
- `convert_to_json(data: Any) -> str`: Convert data to JSON
- `dict_to_csv(data: List[Dict]) -> str`: Convert dict list to CSV

### System Utilities

#### `devtools.system.files`
- `backup_file(filepath: str) -> str`: Create file backup
- `get_file_info(filepath: str) -> Dict`: Get file information
- `list_directory(directory: str) -> List[Dict]`: List directory contents

#### `devtools.system.info`
- `get_system_info() -> Dict`: Get system information
- `get_python_info() -> Dict`: Get Python interpreter info

### Web Utilities

#### `devtools.web.urls`
- `validate_url(url: str) -> bool`: Validate URL format
- `parse_url(url: str) -> Dict`: Parse URL components
- `extract_domain(url: str) -> str`: Extract domain from URL

## 🔧 Configuration

### Requirements Files

- `requirements/base.txt`: Core dependencies (minimal)
- `requirements/dev.txt`: Development dependencies
- `requirements/test.txt`: Testing dependencies

### Setup Configuration

The package is configured for distribution with:
- `setup.py`: Package metadata and dependencies
- `pyproject.toml`: Modern Python packaging configuration
- Entry points for command-line tools
- Proper classifiers and metadata

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎓 Learning Objectives Achieved

This project demonstrates mastery of:

✅ **Package Structure**: Well-organized hierarchy with proper `__init__.py` files  
✅ **Module Design**: Focused, reusable utility functions  
✅ **Documentation**: Comprehensive docstrings and examples  
✅ **Testing**: Unit tests with good coverage  
✅ **Virtual Environments**: Proper environment isolation  
✅ **Dependency Management**: Organized requirements files  
✅ **Distribution**: Ready for package installation  
✅ **Error Handling**: Custom exceptions and proper error handling  
✅ **Type Hints**: Modern Python typing throughout  
✅ **Code Quality**: Consistent style and best practices  

## 🚀 Next Steps

- Add command-line interface (CLI)
- Implement logging throughout the package
- Add configuration file support
- Create comprehensive documentation site
- Publish to PyPI
- Add continuous integration (CI/CD)
- Performance optimization
- Additional utility functions

---

**Created as part of the Python Learning Path - Modules and Packages Module**