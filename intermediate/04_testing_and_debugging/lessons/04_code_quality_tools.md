# Code Quality Tools

## Introduction

Code quality tools help maintain consistent, readable, and error-free code. They automate the process of checking for style violations, potential bugs, and code smells. Using these tools is essential for professional Python development and team collaboration.

## Why Code Quality Matters

### Benefits of High-Quality Code
- **Readability**: Easier for others (and future you) to understand
- **Maintainability**: Simpler to modify and extend
- **Reliability**: Fewer bugs and unexpected behaviors
- **Collaboration**: Consistent style across team members
- **Performance**: Often leads to more efficient code

### Problems with Poor Code Quality
- Increased debugging time
- Difficulty adding new features
- Higher risk of introducing bugs
- Reduced team productivity
- Technical debt accumulation

## Types of Code Quality Tools

### 1. Linters
Analyze code for potential errors, style violations, and suspicious constructs:
- **pylint**: Comprehensive linting with detailed reports
- **flake8**: Fast, focused on PEP 8 and common errors
- **pycodestyle**: Specifically checks PEP 8 compliance

### 2. Formatters
Automatically format code to follow consistent style:
- **black**: Opinionated, automatic code formatter
- **autopep8**: Formats code to conform to PEP 8
- **yapf**: Configurable formatter from Google

### 3. Type Checkers
Analyze type annotations for consistency:
- **mypy**: Static type checker for Python
- **pyright**: Microsoft's type checker
- **pyre**: Facebook's type checker

### 4. Import Sorters
Organize import statements:
- **isort**: Sorts imports alphabetically and by type

### 5. Security Analyzers
Check for security vulnerabilities:
- **bandit**: Finds common security issues
- **safety**: Checks dependencies for known vulnerabilities

## PEP 8: Python Style Guide

PEP 8 is the official style guide for Python code. Key principles:

### Indentation
```python
# Good
if condition:
    do_something()
    if nested_condition:
        do_nested_thing()

# Bad
if condition:
  do_something()
    if nested_condition:
      do_nested_thing()
```

### Line Length
```python
# Good - under 79 characters
short_variable_name = some_function(arg1, arg2)

# Good - break long lines
long_variable_name = some_very_long_function_name(
    argument_one,
    argument_two,
    argument_three
)

# Bad - over 79 characters
very_long_variable_name = some_very_long_function_name(argument_one, argument_two, argument_three, argument_four)
```

### Naming Conventions
```python
# Variables and functions: snake_case
user_name = "john"
def calculate_total():
    pass

# Classes: PascalCase
class UserAccount:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_CONNECTIONS = 100

# Private attributes: leading underscore
class MyClass:
    def __init__(self):
        self._private_var = 42
        self.__very_private = 99
```

### Whitespace
```python
# Good
spam(ham[1], {eggs: 2})
if x == 4:
    print(x, y)
x, y = y, x

# Bad
spam( ham[ 1 ], { eggs : 2 } )
if x == 4 :
    print(x , y)
x , y = y , x
```

## Pylint

Pylint is a comprehensive linter that checks for errors, enforces coding standards, and looks for code smells.

### Installation
```bash
pip install pylint
```

### Basic Usage
```bash
# Check a single file
pylint myfile.py

# Check a package
pylint mypackage/

# Generate configuration file
pylint --generate-rcfile > .pylintrc
```

### Example Output
```
************* Module example
example.py:1:0: C0114: Missing module docstring (missing-module-docstring)
example.py:3:0: C0103: Constant name "userName" doesn't conform to UPPER_CASE naming style (invalid-name)
example.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
example.py:6:4: W0612: Unused variable 'result' (unused-variable)

------------------------------------------------------------------
Your code has been rated at 2.50/10 (previous run: 2.50/10)
```

### Configuration Example (.pylintrc)
```ini
[MASTER]
# Add files or directories to the blacklist
ignore=migrations,venv

[MESSAGES CONTROL]
# Disable specific warnings
disable=missing-docstring,too-few-public-methods

[FORMAT]
# Maximum number of characters on a single line
max-line-length=88

[DESIGN]
# Maximum number of arguments for function / method
max-args=7
```

### Common Pylint Messages
- **C0103**: Invalid name (doesn't conform to naming convention)
- **W0613**: Unused argument
- **R0903**: Too few public methods
- **R0913**: Too many arguments
- **E1101**: Instance has no member

## Flake8

Flake8 is a fast linter that combines pycodestyle, pyflakes, and mccabe.

### Installation
```bash
pip install flake8
```

### Basic Usage
```bash
# Check files
flake8 myfile.py
flake8 mypackage/

# Check with specific configuration
flake8 --max-line-length=88 --ignore=E203,W503 myfile.py
```

### Configuration (.flake8 or setup.cfg)
```ini
[flake8]
max-line-length = 88
ignore = E203, W503, E501
exclude = 
    .git,
    __pycache__,
    venv,
    migrations
per-file-ignores =
    __init__.py:F401
```

### Common Flake8 Error Codes
- **E**: pycodestyle errors
- **W**: pycodestyle warnings
- **F**: pyflakes errors
- **C**: mccabe complexity warnings

## Black: The Uncompromising Code Formatter

Black automatically formats Python code with minimal configuration.

### Installation
```bash
pip install black
```

### Basic Usage
```bash
# Format a file (shows diff)
black --diff myfile.py

# Format a file (in-place)
black myfile.py

# Format entire project
black .

# Check if files would be reformatted
black --check .
```

### Example Transformation
```python
# Before Black
def very_important_function(template: str,*args,**kwargs,):
    """Fixes bugs and issues reported by users."""
    return template.format(*args, **kwargs)

# After Black
def very_important_function(template: str, *args, **kwargs):
    """Fixes bugs and issues reported by users."""
    return template.format(*args, **kwargs)
```

### Configuration (pyproject.toml)
```toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
exclude = '''
/(
    \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

## isort: Import Sorting

isort automatically sorts and organizes import statements.

### Installation
```bash
pip install isort
```

### Basic Usage
```bash
# Sort imports in a file
isort myfile.py

# Check if imports are sorted
isort --check-only myfile.py

# Show diff of what would change
isort --diff myfile.py
```

### Example Transformation
```python
# Before isort
import os
from mypackage import mymodule
import sys
from collections import defaultdict
import json

# After isort
import json
import os
import sys
from collections import defaultdict

from mypackage import mymodule
```

### Configuration (.isort.cfg or pyproject.toml)
```toml
[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["mypackage"]
known_third_party = ["requests", "django"]
```

## MyPy: Static Type Checking

MyPy checks type annotations for consistency and catches type-related errors.

### Installation
```bash
pip install mypy
```

### Basic Usage
```bash
# Type check a file
mypy myfile.py

# Type check a package
mypy mypackage/

# Generate configuration file
mypy --config-file mypy.ini myfile.py
```

### Type Annotations Example
```python
from typing import List, Optional, Dict, Any

def process_users(users: List[Dict[str, Any]]) -> Optional[str]:
    """Process a list of user dictionaries."""
    if not users:
        return None
    
    processed_count: int = 0
    for user in users:
        name: str = user.get("name", "Unknown")
        age: Optional[int] = user.get("age")
        
        if age is not None and age >= 18:
            processed_count += 1
    
    return f"Processed {processed_count} adult users"

# MyPy will catch type errors
result: int = process_users([])  # Error: incompatible types
```

### Configuration (mypy.ini)
```ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True

[mypy-requests.*]
ignore_missing_imports = True
```

## Bandit: Security Linter

Bandit finds common security issues in Python code.

### Installation
```bash
pip install bandit
```

### Basic Usage
```bash
# Scan a file
bandit myfile.py

# Scan a directory
bandit -r mypackage/

# Generate report
bandit -r mypackage/ -f json -o report.json
```

### Example Security Issues
```python
# Hardcoded password (B105)
password = "admin123"

# SQL injection risk (B608)
query = "SELECT * FROM users WHERE id = " + user_id

# Use of exec (B102)
exec(user_input)

# Insecure random (B311)
import random
token = random.random()
```

## Pre-commit Hooks

Pre-commit hooks automatically run code quality tools before commits.

### Installation
```bash
pip install pre-commit
```

### Configuration (.pre-commit-config.yaml)
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3.8

  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
        args: [--max-line-length=88]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.950
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]

  - repo: https://github.com/pycqa/bandit
    rev: 1.7.4
    hooks:
      - id: bandit
        args: ["-c", "pyproject.toml"]
```

### Setup
```bash
# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

## IDE Integration

### VS Code
Install extensions:
- Python (Microsoft)
- Pylance
- Black Formatter
- isort

Settings (settings.json):
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.sortImports.args": ["--profile", "black"],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

### PyCharm
Built-in support for:
- PEP 8 checking
- Code inspection
- Automatic formatting
- Import optimization

## Continuous Integration

### GitHub Actions Example
```yaml
name: Code Quality

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    
    - name: Install dependencies
      run: |
        pip install black isort flake8 mypy bandit
    
    - name: Check formatting with Black
      run: black --check .
    
    - name: Check import sorting
      run: isort --check-only .
    
    - name: Lint with flake8
      run: flake8 .
    
    - name: Type check with mypy
      run: mypy .
    
    - name: Security check with bandit
      run: bandit -r .
```

## Best Practices

### 1. Start Simple
Begin with basic tools and gradually add more:
1. Start with Black for formatting
2. Add flake8 for basic linting
3. Introduce mypy for type checking
4. Add pre-commit hooks

### 2. Team Consistency
- Agree on tool configuration as a team
- Use shared configuration files
- Document the setup process
- Automate with pre-commit hooks

### 3. Gradual Adoption
```python
# Add type hints gradually
def process_data(data):  # Start without types
    pass

def process_data(data: list):  # Add basic types
    pass

def process_data(data: List[Dict[str, Any]]) -> Optional[str]:  # Full typing
    pass
```

### 4. Configuration Management
Keep all tool configurations in version control:
- `.pylintrc`
- `.flake8` or `setup.cfg`
- `pyproject.toml`
- `.pre-commit-config.yaml`

### 5. Ignore Rules Judiciously
```python
# Good - specific suppression with reason
def legacy_function():  # pylint: disable=too-many-locals
    # This function has many locals due to legacy requirements
    pass

# Bad - blanket suppression
# pylint: disable=all
```

## Tool Comparison

| Tool | Purpose | Speed | Configurability | Learning Curve |
|------|---------|-------|-----------------|----------------|
| Black | Formatting | Fast | Low | Easy |
| autopep8 | Formatting | Fast | Medium | Easy |
| flake8 | Linting | Fast | High | Easy |
| pylint | Linting | Slow | Very High | Medium |
| mypy | Type checking | Medium | High | Hard |
| isort | Import sorting | Fast | High | Easy |
| bandit | Security | Fast | Medium | Easy |

## Common Workflow

1. **Write code** with your preferred style
2. **Run isort** to organize imports
3. **Run Black** to format code
4. **Run flake8** to check for issues
5. **Run mypy** to check types
6. **Run tests** to ensure functionality
7. **Commit** with pre-commit hooks

## Troubleshooting

### Common Issues

#### Black and flake8 Conflicts
```ini
# .flake8
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

#### MyPy Import Errors
```ini
# mypy.ini
[mypy-package_name.*]
ignore_missing_imports = True
```

#### Pre-commit Hook Failures
```bash
# Skip hooks temporarily
git commit --no-verify

# Fix and re-run
pre-commit run --all-files
```

## Summary

Code quality tools are essential for professional Python development:

- **Use Black** for consistent formatting
- **Use flake8** for fast linting
- **Use mypy** for type safety
- **Use isort** for import organization
- **Use bandit** for security checks
- **Set up pre-commit hooks** for automation
- **Configure tools** to work together
- **Integrate with your IDE** for real-time feedback
- **Use in CI/CD** for team consistency

Start with basic tools and gradually adopt more advanced ones as your projects grow in complexity. The investment in setup pays off quickly in reduced debugging time and improved code quality.

---

**Next**: [Mini-Project: Test-Driven Development Exercise](../mini_project/README.md)