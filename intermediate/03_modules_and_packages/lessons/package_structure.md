# Package Structure

## What is a Package?

A package in Python is a way of organizing related modules into a directory hierarchy. Packages allow you to structure your code in a logical way and avoid naming conflicts between modules. A package is essentially a directory that contains Python modules and a special `__init__.py` file.

## Basic Package Structure

The simplest package structure looks like this:

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

The `__init__.py` file (which can be empty) tells Python that the directory should be treated as a package.

## Creating Your First Package

Let's create a simple package called `mathtools`:

### Step 1: Create the Package Directory

```
mathtools/
    __init__.py
    basic.py
    advanced.py
```

### Step 2: Create the Modules

**mathtools/basic.py**:
```python
"""Basic mathematical operations."""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

**mathtools/advanced.py**:
```python
"""Advanced mathematical operations."""

import math

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)

def power(base, exponent):
    """Calculate base raised to exponent."""
    return base ** exponent

def sqrt(n):
    """Calculate square root."""
    return math.sqrt(n)

def gcd(a, b):
    """Calculate greatest common divisor."""
    return math.gcd(a, b)
```

**mathtools/__init__.py**:
```python
"""
MathTools Package

A collection of mathematical utility functions.
"""

# Import commonly used functions to package level
from .basic import add, subtract, multiply, divide
from .advanced import factorial, power, sqrt

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Learning Path"

# Define what gets imported with "from mathtools import *"
__all__ = ['add', 'subtract', 'multiply', 'divide', 'factorial', 'power', 'sqrt']
```

## Using Packages

### Method 1: Import the entire package
```python
import mathtools

result = mathtools.add(5, 3)
print(f"5 + 3 = {result}")
```

### Method 2: Import specific modules
```python
from mathtools import basic, advanced

result = basic.add(5, 3)
factorial_result = advanced.factorial(5)
```

### Method 3: Import specific functions
```python
from mathtools import add, factorial

result = add(5, 3)
fact_result = factorial(5)
```

### Method 4: Import from submodules
```python
from mathtools.basic import add, multiply
from mathtools.advanced import factorial, sqrt
```

## Nested Packages

Packages can contain other packages, creating a hierarchy:

```
myproject/
    __init__.py
    utils/
        __init__.py
        string_utils.py
        file_utils.py
    data/
        __init__.py
        processors/
            __init__.py
            text_processor.py
            image_processor.py
        validators/
            __init__.py
            email_validator.py
            phone_validator.py
```

## The `__init__.py` File

The `__init__.py` file serves several purposes:

### 1. Package Initialization
```python
# mypackage/__init__.py
print("Initializing mypackage")

# Initialize package-level variables
DEFAULT_CONFIG = {
    'debug': False,
    'version': '1.0.0'
}
```

### 2. Control Public API
```python
# mypackage/__init__.py
from .module1 import function1, Class1
from .module2 import function2

# Only these will be available when using "from mypackage import *"
__all__ = ['function1', 'Class1', 'function2']
```

### 3. Convenience Imports
```python
# mypackage/__init__.py
# Make deeply nested functions available at package level
from .subpackage.module import important_function

# Now users can do: from mypackage import important_function
# Instead of: from mypackage.subpackage.module import important_function
```

## Relative vs Absolute Imports

### Absolute Imports
Always specify the full path from the top-level package:

```python
# Inside myproject/data/processors/text_processor.py
from myproject.utils.string_utils import clean_text
from myproject.data.validators.email_validator import is_valid_email
```

### Relative Imports
Use dots to specify relative locations:

```python
# Inside myproject/data/processors/text_processor.py
from ...utils.string_utils import clean_text  # Go up 3 levels, then down
from ..validators.email_validator import is_valid_email  # Go up 1 level, then down
from .image_processor import process_image  # Same directory
```

**Relative Import Rules:**
- `.` = current package
- `..` = parent package
- `...` = grandparent package
- Can only be used within packages
- Cannot be used in scripts run directly

## Package Example: Web Utilities

Let's create a more complex package:

```
webutils/
    __init__.py
    http/
        __init__.py
        client.py
        server.py
    validation/
        __init__.py
        email.py
        url.py
    parsing/
        __init__.py
        html.py
        json.py
```

**webutils/__init__.py**:
```python
"""
Web Utilities Package

A collection of web-related utility functions.
"""

# Import commonly used functions to package level
from .validation.email import is_valid_email
from .validation.url import is_valid_url
from .parsing.json import parse_json, to_json

__version__ = "1.0.0"
__all__ = ['is_valid_email', 'is_valid_url', 'parse_json', 'to_json']
```

**webutils/validation/__init__.py**:
```python
"""Validation utilities."""

from .email import is_valid_email
from .url import is_valid_url

__all__ = ['is_valid_email', 'is_valid_url']
```

**webutils/validation/email.py**:
```python
"""Email validation utilities."""

import re

def is_valid_email(email):
    """Check if email address is valid."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def extract_domain(email):
    """Extract domain from email address."""
    if not is_valid_email(email):
        raise ValueError("Invalid email address")
    return email.split('@')[1]
```

## Namespace Packages

Python 3.3+ supports namespace packages - packages split across multiple directories:

```
# Directory 1
mycompany-core/
    mycompany/
        core/
            __init__.py
            database.py

# Directory 2  
mycompany-web/
    mycompany/
        web/
            __init__.py
            server.py
```

Both can be imported as `mycompany.core` and `mycompany.web` respectively.

## Best Practices for Package Structure

### 1. Logical Organization
```
myproject/
    __init__.py
    models/          # Data models
        __init__.py
        user.py
        product.py
    views/           # User interface
        __init__.py
        user_view.py
        product_view.py
    controllers/     # Business logic
        __init__.py
        user_controller.py
        product_controller.py
    utils/           # Utility functions
        __init__.py
        helpers.py
        validators.py
```

### 2. Clear Naming
- Use lowercase with underscores for package names
- Make names descriptive but not too long
- Avoid conflicts with standard library names

### 3. Proper `__init__.py` Files
```python
# Good __init__.py
"""
Package description.
"""

from .module1 import Class1, function1
from .module2 import Class2

__version__ = "1.0.0"
__all__ = ['Class1', 'function1', 'Class2']
```

### 4. Documentation
- Document packages and modules
- Include examples in docstrings
- Provide clear README files

### 5. Testing Structure
```
myproject/
    myproject/
        __init__.py
        module1.py
        module2.py
    tests/
        __init__.py
        test_module1.py
        test_module2.py
    setup.py
    README.md
```

## Common Package Patterns

### 1. Plugin Architecture
```
myapp/
    __init__.py
    core/
        __init__.py
        engine.py
    plugins/
        __init__.py
        plugin1.py
        plugin2.py
```

### 2. MVC Pattern
```
webapp/
    __init__.py
    models/
        __init__.py
        user.py
    views/
        __init__.py
        templates/
    controllers/
        __init__.py
        user_controller.py
```

### 3. Layered Architecture
```
myservice/
    __init__.py
    presentation/    # API layer
        __init__.py
    business/        # Business logic
        __init__.py
    data/           # Data access
        __init__.py
```

## Troubleshooting Package Issues

### Common Problems:

1. **ModuleNotFoundError**: Package not in Python path
2. **ImportError**: Circular imports between modules
3. **AttributeError**: Function not available at expected level

### Solutions:

1. **Check Python Path**:
```python
import sys
print(sys.path)
```

2. **Avoid Circular Imports**:
- Restructure code to remove circular dependencies
- Use imports inside functions if necessary

3. **Check `__init__.py`**:
- Ensure proper imports in `__init__.py`
- Verify `__all__` list is correct

## Package Distribution

To make your package installable:

**setup.py**:
```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # List dependencies here
    ],
    author="Your Name",
    description="A sample Python package",
    python_requires=">=3.6",
)
```

Install in development mode:
```bash
pip install -e .
```

## Summary

Packages are essential for organizing Python code:

- Use `__init__.py` to create packages
- Organize code logically into modules and subpackages
- Control the public API through `__init__.py`
- Use absolute imports for clarity
- Follow naming conventions and best practices
- Document your packages well

In the next lesson, we'll explore virtual environments to manage package dependencies effectively.