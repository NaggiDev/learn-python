# Error Handling Cheat Sheet

## Basic Exception Handling

### Try-Except Structure
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero!")
```

### Multiple Exception Types
```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catching Multiple Exceptions
```python
try:
    # Some risky code
    pass
except (ValueError, TypeError, KeyError) as e:
    print(f"An error occurred: {e}")
```

### Generic Exception Handling
```python
try:
    # Some code
    pass
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Complete Try-Except Structure

### Try-Except-Else-Finally
```python
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found!")
    data = None
except PermissionError:
    print("Permission denied!")
    data = None
else:
    # Executed if no exception occurs
    print("File read successfully!")
finally:
    # Always executed
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")
```

## Common Built-in Exceptions

### ValueError
```python
try:
    age = int("not_a_number")
except ValueError as e:
    print(f"ValueError: {e}")

# Example: Converting invalid string to int
def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer")
        return None
```

### TypeError
```python
try:
    result = "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# Example: Function with wrong argument types
def add_numbers(a, b):
    try:
        return a + b
    except TypeError:
        print("Both arguments must be numbers")
        return None
```

### KeyError
```python
person = {"name": "Alice", "age": 30}

try:
    height = person["height"]
except KeyError as e:
    print(f"Key {e} not found in dictionary")

# Better approach using get()
height = person.get("height", "Unknown")
```

### IndexError
```python
my_list = [1, 2, 3]

try:
    value = my_list[10]
except IndexError as e:
    print(f"IndexError: {e}")

# Safe list access
def safe_list_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default
```

### FileNotFoundError
```python
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist")
    # Create default file or handle appropriately
```

### AttributeError
```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")

try:
    print(person.age)  # age attribute doesn't exist
except AttributeError as e:
    print(f"AttributeError: {e}")
```

## Custom Exceptions

### Creating Custom Exceptions
```python
class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

class ValidationError(CustomError):
    """Raised when validation fails"""
    pass

class DatabaseError(CustomError):
    """Raised when database operations fail"""
    pass

# Using custom exceptions
def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer")
    if age < 0:
        raise ValidationError("Age cannot be negative")
    if age > 150:
        raise ValidationError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValidationError as e:
    print(f"Validation failed: {e}")
```

### Custom Exception with Additional Data
```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance={balance}, requested={amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Cannot withdraw ${e.amount}. Current balance: ${e.balance}")
```

## Raising Exceptions

### Basic Raise
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

### Re-raising Exceptions
```python
def process_data(data):
    try:
        # Some processing that might fail
        result = risky_operation(data)
    except ValueError as e:
        # Log the error
        print(f"Error processing data: {e}")
        # Re-raise the exception
        raise
    return result
```

### Raising from Another Exception
```python
def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        raise TypeError("Invalid type for conversion") from e

try:
    result = convert_to_int("abc")
except TypeError as e:
    print(f"TypeError: {e}")
    print(f"Original cause: {e.__cause__}")
```

## Exception Handling Patterns

### Validation Pattern
```python
def validate_user_input(data):
    errors = []
    
    if not data.get('name'):
        errors.append("Name is required")
    
    if not data.get('email'):
        errors.append("Email is required")
    elif '@' not in data['email']:
        errors.append("Invalid email format")
    
    if data.get('age') and data['age'] < 0:
        errors.append("Age cannot be negative")
    
    if errors:
        raise ValidationError("; ".join(errors))
    
    return True

# Usage
user_data = {"name": "", "email": "invalid", "age": -5}
try:
    validate_user_input(user_data)
except ValidationError as e:
    print(f"Validation errors: {e}")
```

### Retry Pattern
```python
import time
import random

def retry_operation(func, max_attempts=3, delay=1):
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                # Last attempt, re-raise the exception
                raise
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)

def unreliable_operation():
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network error")
    return "Success!"

try:
    result = retry_operation(unreliable_operation)
    print(result)
except ConnectionError as e:
    print(f"Operation failed after all retries: {e}")
```

### Context Manager for Exception Handling
```python
class ErrorHandler:
    def __init__(self, ignore_errors=False):
        self.ignore_errors = ignore_errors
        self.errors = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.errors.append(exc_val)
            if self.ignore_errors:
                print(f"Ignoring error: {exc_val}")
                return True  # Suppress the exception
        return False

# Usage
with ErrorHandler(ignore_errors=True) as handler:
    # Code that might raise exceptions
    result = 10 / 0  # This would normally raise ZeroDivisionError

print("Continued execution after error")
```

## Debugging and Logging

### Using Traceback
```python
import traceback

try:
    # Some code that raises an exception
    result = 1 / 0
except Exception as e:
    # Print full traceback
    traceback.print_exc()
    
    # Get traceback as string
    tb_str = traceback.format_exc()
    print("Traceback as string:", tb_str)
```

### Logging Exceptions
```python
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def risky_function():
    try:
        # Some risky operation
        result = 10 / 0
    except Exception as e:
        # Log the exception with traceback
        logging.exception("An error occurred in risky_function")
        # Or log with specific level
        logging.error("Error: %s", str(e), exc_info=True)
        raise  # Re-raise if needed

try:
    risky_function()
except:
    pass  # Exception already logged
```

### Assert Statements for Debugging
```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    
    return sum(numbers) / len(numbers)

# Assertions can be disabled with python -O script.py
try:
    avg = calculate_average([])
except AssertionError as e:
    print(f"Assertion failed: {e}")
```

## Best Practices

### Specific Exception Handling
```python
# Good: Catch specific exceptions
try:
    value = int(user_input)
    result = 10 / value
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Number cannot be zero")

# Avoid: Catching all exceptions
try:
    # some code
    pass
except:  # Don't do this
    print("Something went wrong")
```

### Exception Chaining
```python
def process_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
            return json.loads(data)
    except FileNotFoundError as e:
        raise ProcessingError(f"Cannot process {filename}") from e
    except json.JSONDecodeError as e:
        raise ProcessingError(f"Invalid JSON in {filename}") from e
```

### Clean Resource Management
```python
# Good: Using context managers
def process_files(filenames):
    results = []
    for filename in filenames:
        try:
            with open(filename, 'r') as f:
                results.append(f.read())
        except FileNotFoundError:
            print(f"Warning: {filename} not found, skipping")
            continue
    return results

# Alternative: Manual cleanup with try-finally
def process_file_manual(filename):
    f = None
    try:
        f = open(filename, 'r')
        return f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    finally:
        if f:
            f.close()
```

### Error Recovery
```python
def robust_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Warning: Division by zero, returning infinity")
        return float('inf')
    except TypeError:
        print("Warning: Invalid types, attempting conversion")
        try:
            return float(a) / float(b)
        except (ValueError, ZeroDivisionError):
            print("Error: Cannot perform division")
            return None

# Usage
results = [
    robust_division(10, 2),    # 5.0
    robust_division(10, 0),    # inf
    robust_division("10", "2"), # 5.0
    robust_division("a", "b"),  # None
]
```

## Common Anti-patterns to Avoid

### Don't Ignore Exceptions
```python
# Bad
try:
    risky_operation()
except:
    pass  # Silent failure

# Good
try:
    risky_operation()
except SpecificException as e:
    logging.error(f"Operation failed: {e}")
    # Handle appropriately
```

### Don't Catch and Re-raise Without Purpose
```python
# Bad
try:
    operation()
except Exception as e:
    raise e  # Loses original traceback

# Good
try:
    operation()
except Exception as e:
    logging.error(f"Operation failed: {e}")
    raise  # Preserves original traceback
```

### Don't Use Exceptions for Control Flow
```python
# Bad
try:
    while True:
        item = get_next_item()
        process(item)
except StopIteration:
    pass

# Good
while True:
    item = get_next_item()
    if item is None:
        break
    process(item)
```

## Testing Exception Handling

### Using pytest
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_normal():
    assert divide(10, 2) == 5
```

### Using unittest
```python
import unittest

class TestDivision(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)
```