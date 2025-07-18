# Decorators in Python

## Introduction

Decorators are one of Python's most powerful and elegant features. They allow you to modify or extend the behavior of functions, methods, or classes without permanently modifying their code. Decorators follow the decorator pattern, which is a structural design pattern that allows behavior to be added to objects dynamically.

In Python, decorators are essentially functions that take another function as an argument and return a modified version of that function. They provide a clean and readable way to implement cross-cutting concerns like logging, timing, authentication, caching, and more.

## Understanding Functions as First-Class Objects

Before diving into decorators, it's important to understand that in Python, functions are first-class objects. This means:

1. Functions can be assigned to variables
2. Functions can be passed as arguments to other functions
3. Functions can be returned from other functions
4. Functions can be stored in data structures

```python
# Functions can be assigned to variables
def greet(name):
    return f"Hello, {name}!"

say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!

# Functions can be passed as arguments
def apply_twice(func, arg):
    return func(func(arg))

def add_one(x):
    return x + 1

result = apply_twice(add_one, 5)
print(result)  # Output: 7

# Functions can be returned from other functions
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(5))  # Output: 10
```

## Basic Decorator Syntax

The most common way to use decorators is with the `@` symbol:

```python
@decorator_function
def target_function():
    pass
```

This is equivalent to:

```python
def target_function():
    pass

target_function = decorator_function(target_function)
```

## Creating Your First Decorator

Let's create a simple decorator that prints a message before and after a function call:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# When we call say_hello(), the decorator is executed
say_hello()
```

Output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

## Decorators with Arguments

To handle functions that take arguments, we need to modify our decorator:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    return f"{greeting}, {name}!"

result = greet("Alice", greeting="Hi")
print(f"Returned: {result}")
```

## Practical Decorator Examples

### 1. Timing Decorator

```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

result = slow_function()
```

### 2. Logging Decorator

```python
import functools
from datetime import datetime

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] {func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

result = add(3, 5)
```

### 3. Retry Decorator

```python
import functools
import random
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("Random failure!")
    return "Success!"

# This will retry up to 3 times if it fails
result = unreliable_function()
```

### 4. Cache/Memoization Decorator

```python
import functools

def memoize(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"Cache hit for {func.__name__}")
            return cache[key]
        
        print(f"Computing {func.__name__}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Will use caching for efficiency
```

## Decorators with Parameters

Sometimes you want to pass parameters to your decorators:

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Will print the greeting 3 times
```

## Class-Based Decorators

You can also create decorators using classes:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # say_hello has been called 1 times
say_hello()  # say_hello has been called 2 times
```

## Multiple Decorators

You can apply multiple decorators to a single function:

```python
@timer
@log_calls
@retry(max_attempts=2)
def complex_function(x, y):
    if random.random() < 0.5:
        raise Exception("Random error!")
    return x * y

# Decorators are applied from bottom to top (inside out)
# This is equivalent to: timer(log_calls(retry(max_attempts=2)(complex_function)))
```

## Built-in Decorators

Python provides several built-in decorators:

### @property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.area)  # Calculated property
circle.radius = 10  # Uses setter
```

### @staticmethod and @classmethod

```python
class MathUtils:
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

# Static method - doesn't need class instance
result = MathUtils.add(5, 3)

# Class method - receives class as first argument
area = MathUtils.circle_area(5)
```

## Advanced Decorator Patterns

### 1. Decorator Factory with Configuration

```python
def validate_types(**expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Validate types
            for param_name, expected_type in expected_types.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"{param_name} must be of type {expected_type.__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(name=str, age=int)
def create_person(name, age):
    return f"Person: {name}, Age: {age}"

# This will work
person1 = create_person("Alice", 25)

# This will raise TypeError
# person2 = create_person("Bob", "25")
```

### 2. Context Manager Decorator

```python
def with_context(context_manager):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with context_manager:
                return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage with file handling
@with_context(open('example.txt', 'w'))
def write_data(file_obj, data):
    file_obj.write(data)
```

### 3. Rate Limiting Decorator

```python
import time
from collections import defaultdict

def rate_limit(max_calls, time_window):
    calls = defaultdict(list)
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            func_calls = calls[func.__name__]
            
            # Remove old calls outside the time window
            calls[func.__name__] = [call_time for call_time in func_calls 
                                  if now - call_time < time_window]
            
            if len(calls[func.__name__]) >= max_calls:
                raise Exception(f"Rate limit exceeded for {func.__name__}")
            
            calls[func.__name__].append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, time_window=60)  # 3 calls per minute
def api_call():
    return "API response"
```

## Best Practices

### 1. Use functools.wraps

Always use `@functools.wraps(func)` to preserve the original function's metadata:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # This preserves func's __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 2. Handle Return Values

Make sure your decorator returns the result of the original function:

```python
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)  # Store the result
        # Do something after
        return result  # Return the result
    return wrapper
```

### 3. Use *args and **kwargs

This makes your decorator work with any function signature:

```python
def universal_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Your decorator logic here
        return func(*args, **kwargs)
    return wrapper
```

### 4. Consider Performance

Decorators add overhead. For performance-critical code, consider:
- Using decorators sparingly
- Implementing efficient decorator logic
- Using built-in decorators when possible

## Common Use Cases

1. **Logging and Debugging**: Track function calls and parameters
2. **Authentication and Authorization**: Check permissions before function execution
3. **Caching**: Store function results to avoid repeated calculations
4. **Timing and Performance Monitoring**: Measure execution time
5. **Input Validation**: Validate function arguments
6. **Error Handling**: Add retry logic or error recovery
7. **Rate Limiting**: Control how often functions can be called
8. **Database Transactions**: Wrap functions in database transactions

## Debugging Decorated Functions

When debugging decorated functions, remember:

1. The actual function being called is the wrapper
2. Use `functools.wraps` to preserve original function information
3. You can access the original function through the `__wrapped__` attribute

```python
@my_decorator
def original_function():
    """This is the original function."""
    pass

print(original_function.__name__)     # Should print 'original_function'
print(original_function.__doc__)      # Should print the docstring
print(original_function.__wrapped__)  # Access to original function
```

## Summary

Decorators are a powerful Python feature that allows you to:

- Modify function behavior without changing the function itself
- Implement cross-cutting concerns cleanly
- Create reusable code patterns
- Write more maintainable and readable code

Key points to remember:
- Decorators are functions that take functions as arguments
- Use `@functools.wraps` to preserve function metadata
- Handle `*args` and `**kwargs` for flexibility
- Return the result of the original function
- Decorators can be stacked and parameterized
- They're excellent for logging, timing, caching, and validation

Decorators embody the principle of separation of concerns and help you write cleaner, more modular code.