# Unit Testing with pytest

## Introduction

Unit testing is a fundamental practice in software development where individual components (functions, methods, classes) are tested in isolation to ensure they work correctly. Python's `pytest` framework is the most popular testing tool in the Python ecosystem, offering powerful features while maintaining simplicity.

## Why Testing Matters

Testing provides several critical benefits:

- **Bug Detection**: Catch errors before they reach production
- **Regression Prevention**: Ensure new changes don't break existing functionality
- **Documentation**: Tests serve as living documentation of how code should behave
- **Confidence**: Make changes with confidence knowing tests will catch issues
- **Design Improvement**: Writing tests often reveals design flaws early

## Installing pytest

First, install pytest in your virtual environment:

```bash
pip install pytest
```

## Basic Test Structure

A pytest test is simply a Python function that starts with `test_`. Here's the basic structure:

```python
def test_function_name():
    # Arrange: Set up test data
    # Act: Call the function being tested
    # Assert: Check the result
    assert result == expected_value
```

## Writing Your First Test

Let's start with a simple example. Create a file called `calculator.py`:

```python
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide two numbers and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Now create a test file called `test_calculator.py`:

```python
import pytest
from calculator import add, multiply, divide

def test_add():
    """Test the add function with positive numbers."""
    result = add(2, 3)
    assert result == 5

def test_add_negative():
    """Test the add function with negative numbers."""
    result = add(-1, -2)
    assert result == -3

def test_multiply():
    """Test the multiply function."""
    result = multiply(4, 5)
    assert result == 20

def test_divide():
    """Test the divide function."""
    result = divide(10, 2)
    assert result == 5.0

def test_divide_by_zero():
    """Test that dividing by zero raises an exception."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

## Running Tests

Run your tests with:

```bash
pytest test_calculator.py
```

Or run all tests in the current directory:

```bash
pytest
```

## Common Assertions

pytest provides many assertion methods:

```python
# Basic assertions
assert value == expected
assert value != unexpected
assert value > threshold
assert value in collection
assert value is None
assert value is True

# String assertions
assert "substring" in text
assert text.startswith("prefix")
assert text.endswith("suffix")

# Collection assertions
assert len(collection) == expected_length
assert item in collection
assert set(actual) == set(expected)

# Exception assertions
with pytest.raises(ExceptionType):
    function_that_should_raise()

with pytest.raises(ValueError, match="specific message"):
    function_that_should_raise()
```

## Test Organization

### Test Classes

Group related tests using classes:

```python
class TestCalculator:
    """Test class for calculator functions."""
    
    def test_add_positive(self):
        assert add(1, 2) == 3
    
    def test_add_zero(self):
        assert add(5, 0) == 5
    
    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
```

### Test Fixtures

Fixtures provide reusable test data and setup:

```python
import pytest

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def calculator():
    """Provide a calculator instance for tests."""
    return Calculator()

def test_sum_with_fixture(sample_data):
    """Test using fixture data."""
    result = sum(sample_data)
    assert result == 15

def test_calculator_with_fixture(calculator):
    """Test using calculator fixture."""
    result = calculator.add(2, 3)
    assert result == 5
```

## Parameterized Tests

Test multiple inputs efficiently:

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 5, 5),
    (-1, 1, 0),
    (10, -5, 5),
])
def test_add_parametrized(a, b, expected):
    """Test add function with multiple parameter sets."""
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b", [
    (1, 0),
    (10, 0),
    (-5, 0),
])
def test_divide_by_zero_parametrized(a, b):
    """Test divide by zero with multiple values."""
    with pytest.raises(ValueError):
        divide(a, b)
```

## Test Discovery

pytest automatically discovers tests based on these conventions:

- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*()`
- Test classes: `Test*`
- Test methods in classes: `test_*()`

## Best Practices

### 1. Follow the AAA Pattern

```python
def test_user_creation():
    # Arrange
    name = "John Doe"
    email = "john@example.com"
    
    # Act
    user = User(name, email)
    
    # Assert
    assert user.name == name
    assert user.email == email
```

### 2. Use Descriptive Test Names

```python
# Good
def test_user_login_with_valid_credentials_returns_success():
    pass

def test_user_login_with_invalid_password_raises_authentication_error():
    pass

# Less clear
def test_login():
    pass

def test_login_fail():
    pass
```

### 3. Test One Thing at a Time

```python
# Good - focused test
def test_user_email_validation():
    user = User("John", "invalid-email")
    with pytest.raises(ValueError, match="Invalid email format"):
        user.validate()

# Less focused - testing multiple things
def test_user_validation():
    user = User("", "invalid-email")
    # Testing both name and email validation
    with pytest.raises(ValueError):
        user.validate()
```

### 4. Use Fixtures for Setup

```python
@pytest.fixture
def user_data():
    return {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30
    }

@pytest.fixture
def database_connection():
    # Setup
    conn = create_test_database()
    yield conn
    # Teardown
    conn.close()
```

## Advanced Features

### Markers

Mark tests for selective running:

```python
import pytest

@pytest.mark.slow
def test_complex_calculation():
    # This test takes a long time
    pass

@pytest.mark.integration
def test_database_integration():
    # This test requires database
    pass

# Run only fast tests
# pytest -m "not slow"

# Run only integration tests
# pytest -m integration
```

### Skipping Tests

```python
import pytest
import sys

@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_python38_feature():
    pass
```

## Test Coverage

Install and use pytest-cov for coverage reporting:

```bash
pip install pytest-cov
pytest --cov=calculator test_calculator.py
```

## Common Testing Patterns

### Testing Exceptions

```python
def test_invalid_input_raises_exception():
    with pytest.raises(ValueError) as exc_info:
        process_data("invalid")
    
    assert "Invalid data format" in str(exc_info.value)
```

### Testing with Mock Data

```python
from unittest.mock import Mock, patch

def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"status": "success"}
        
        result = fetch_data_from_api()
        
        assert result["status"] == "success"
        mock_get.assert_called_once()
```

## Summary

Unit testing with pytest provides:

- Simple, readable test syntax
- Powerful assertion capabilities
- Flexible test organization
- Rich ecosystem of plugins
- Excellent error reporting

Key takeaways:
- Write tests for all public functions and methods
- Use descriptive test names
- Follow the AAA pattern (Arrange, Act, Assert)
- Use fixtures for reusable setup
- Parametrize tests for multiple inputs
- Aim for high test coverage
- Run tests frequently during development

## Next Steps

Practice writing tests for your own code, and explore pytest's extensive plugin ecosystem for additional functionality like parallel test execution, HTML reports, and integration with various tools and frameworks.

---

**Next**: [Debugging Techniques](02_debugging_techniques.md)