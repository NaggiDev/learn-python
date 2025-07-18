# Error Handling in Python

## Introduction

Error handling is a critical aspect of writing robust and reliable Python code. When working with files, network resources, user input, or any external systems, many things can go wrong: files might not exist, network connections might fail, or input data might be invalid. Without proper error handling, these issues can cause your program to crash unexpectedly.

In this lesson, you'll learn how to:
- Understand Python's exception hierarchy
- Use try/except blocks to catch and handle errors
- Implement proper error recovery strategies
- Create and raise custom exceptions
- Use context managers for resource cleanup

## Understanding Exceptions

In Python, errors during execution are called exceptions. When an exception occurs, normal program flow is interrupted, and Python looks for an exception handler to deal with the situation.

### Common Built-in Exceptions

Python has many built-in exceptions. Here are some of the most common ones:

- `SyntaxError`: Raised when the parser encounters a syntax error
- `NameError`: Raised when a local or global name is not found
- `TypeError`: Raised when an operation or function is applied to an object of inappropriate type
- `ValueError`: Raised when a function gets an argument of correct type but inappropriate value
- `FileNotFoundError`: Raised when a file or directory is requested but doesn't exist
- `PermissionError`: Raised when trying to access a file without adequate permissions
- `IndexError`: Raised when a sequence subscript is out of range
- `KeyError`: Raised when a dictionary key is not found
- `ZeroDivisionError`: Raised when division or modulo by zero is performed

### Exception Hierarchy

Python's exceptions form a hierarchy, with `BaseException` at the top. Here's a simplified view:

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── Exception
 │    ├── ArithmeticError
 │    │    ├── FloatingPointError
 │    │    ├── OverflowError
 │    │    └── ZeroDivisionError
 │    ├── AssertionError
 │    ├── AttributeError
 │    ├── EOFError
 │    ├── ImportError
 │    │    └── ModuleNotFoundError
 │    ├── LookupError
 │    │    ├── IndexError
 │    │    └── KeyError
 │    ├── NameError
 │    ├── OSError
 │    │    ├── FileNotFoundError
 │    │    ├── PermissionError
 │    │    └── TimeoutError
 │    ├── TypeError
 │    └── ValueError
 └── ... (other exceptions)
```

Understanding this hierarchy is important because when you catch an exception, you also catch all its subclasses.

## Basic Exception Handling

### The try/except Block

The basic structure for exception handling in Python is the `try`/`except` block:

```python
try:
    # Code that might raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"10 / {x} = {result}")
except:
    # Code to handle the exception
    print("An error occurred")
```

However, this approach catches all exceptions, which is generally not recommended. It's better to catch specific exceptions:

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"10 / {x} = {result}")
except ValueError:
    print("That's not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Handling Multiple Exceptions

You can handle multiple exceptions in the same block:

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"10 / {x} = {result}")
except (ValueError, ZeroDivisionError):
    print("Invalid input")
```

### The else Clause

The `else` clause executes if no exception is raised in the `try` block:

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"10 / {x} = {result}")  # Only executes if no exception occurred
```

### The finally Clause

The `finally` clause always executes, whether an exception occurred or not:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("The file does not exist")
finally:
    # This will always execute, even if an exception occurred
    file.close()  # This will raise an error if file wasn't opened successfully
```

To avoid the potential error in the `finally` block, you can check if the file was opened:

```python
file = None
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("The file does not exist")
finally:
    if file:
        file.close()
```

## Exception Information

### Accessing Exception Details

You can access details about the exception using the `as` keyword:

```python
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")  # Prints: Error: [Errno 2] No such file or directory: 'nonexistent_file.txt'
    print(f"Error type: {type(e).__name__}")  # Prints: Error type: FileNotFoundError
```

### Traceback Information

For debugging, you might want to access the full traceback:

```python
import traceback

try:
    1 / 0
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()  # Prints the full traceback
```

## Raising Exceptions

You can raise exceptions explicitly using the `raise` statement:

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

Sometimes you want to catch an exception, perform some action, and then re-raise it:

```python
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("Logging: File not found")
    raise  # Re-raises the last exception
```

### Custom Exceptions

You can create custom exceptions by subclassing `Exception` or one of its subclasses:

```python
class InvalidAgeError(ValueError):
    """Raised when the input age is negative or unreasonably high."""
    pass

def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age > 150:
        raise InvalidAgeError("Age is unreasonably high")
    return age

try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)
except ValueError as e:
    if isinstance(e, InvalidAgeError):
        print(f"Invalid age: {e}")
    else:
        print("Please enter a valid number")
```

## Context Managers

Context managers are a clean way to manage resources like files, network connections, or database connections. They ensure proper cleanup even if an exception occurs.

### The with Statement

The most common way to use context managers is with the `with` statement:

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist")
```

The `with` statement automatically closes the file when the block is exited, even if an exception occurs.

### Creating Context Managers

You can create your own context managers using the `contextlib` module or by implementing the `__enter__` and `__exit__` methods:

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return False to propagate exceptions, True to suppress them
        return False

try:
    with FileManager("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist")
```

## Error Handling Strategies

### Fail Fast

The "fail fast" approach means detecting errors as early as possible and stopping execution:

```python
def process_data(data):
    if not data:
        raise ValueError("Empty data cannot be processed")
    # Process the data...
```

### Graceful Degradation

Graceful degradation means continuing execution with reduced functionality:

```python
def load_configuration():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Warning: Using default configuration")
        return {"default": True}
```

### Retry Logic

For transient errors, you might implement retry logic:

```python
import time

def connect_to_server(max_retries=3, delay=1):
    retries = 0
    while retries < max_retries:
        try:
            # Attempt to connect
            return server_connection()
        except ConnectionError:
            retries += 1
            if retries == max_retries:
                raise  # Re-raise the last exception if all retries failed
            print(f"Connection failed. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
```

## Best Practices

1. **Be specific about which exceptions you catch**. Avoid catching all exceptions unless you have a good reason.

2. **Handle exceptions at the appropriate level**. Catch exceptions where you can handle them meaningfully.

3. **Use context managers** for resource cleanup.

4. **Log exceptions** for debugging and monitoring.

5. **Document the exceptions** your functions might raise.

6. **Don't use exceptions for flow control**. Exceptions should be for exceptional conditions.

7. **Keep the try block as small as possible**. Only include code that might raise the exceptions you're catching.

## Common Pitfalls

1. **Catching all exceptions** can hide bugs and make debugging difficult:

   ```python
   # Bad practice
   try:
       # A lot of code
   except:
       pass  # Silently ignore all errors
   ```

2. **Raising generic exceptions** makes error handling less precise:

   ```python
   # Less helpful
   raise Exception("Something went wrong")
   
   # More helpful
   raise ValueError("Age must be a positive number")
   ```

3. **Not closing resources** can lead to resource leaks:

   ```python
   # Bad practice
   file = open("data.txt", "r")
   content = file.read()
   # What if an exception occurs before the next line?
   file.close()
   
   # Good practice
   with open("data.txt", "r") as file:
       content = file.read()
   ```

4. **Suppressing exceptions** without handling them properly:

   ```python
   # Bad practice
   try:
       risky_operation()
   except Exception:
       # Ignoring the error without handling it
       pass
   ```

## Summary

In this lesson, you've learned:
- The basics of Python's exception handling with try/except blocks
- How to handle multiple exceptions and use else/finally clauses
- How to access exception details and traceback information
- How to raise exceptions and create custom exception classes
- How to use context managers for resource cleanup
- Different error handling strategies and best practices

Error handling is a crucial aspect of writing robust Python code, especially when working with files and external resources. By implementing proper error handling, you can make your programs more reliable and user-friendly.

## Additional Resources

- [Python Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Documentation: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python Documentation: Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)