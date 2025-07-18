"""
Decorators - Solutions

This file contains the solutions for the decorators exercises.
"""

import functools
import time
import random
from datetime import datetime

# Exercise 1: Basic Decorator
def simple_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

# Exercise 2: Timing Decorator
def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

# Exercise 3: Logging Decorator
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] {func.__name__} returned: {result}")
        return result
    return wrapper

# Exercise 4: Retry Decorator
def retry_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise e
                print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
        return None
    return wrapper

# Exercise 5: Parameterized Decorator
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Exercise 6: Validation Decorator
def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check all positional arguments
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"All arguments must be positive numbers. Got: {arg}")
        
        # Check all keyword arguments
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError(f"All arguments must be positive numbers. Got {key}={value}")
        
        return func(*args, **kwargs)
    return wrapper

# Exercise 7: Caching Decorator
def cache_decorator(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"Cache hit for {func.__name__}{args}")
            return cache[key]
        
        print(f"Computing {func.__name__}{args}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper

# Exercise 8: Class-based Decorator
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

# Exercise 9: Multiple Decorators
@timer_decorator
@log_decorator
def complex_calculation(n):
    """Calculate the sum of squares from 1 to n"""
    return sum(i**2 for i in range(1, n+1))

# Exercise 10: Property Decorator
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15

# Test functions with decorators applied
@simple_decorator
def test_function_1():
    print("Inside test function 1")

@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "Completed"

@log_decorator
def add_numbers(a, b):
    return a + b

@retry_decorator
def unreliable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

@repeat(times=3)
def greet_user(name):
    print(f"Hello, {name}!")

@validate_positive
def calculate_area(length, width):
    return length * width

@cache_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@CallCounter
def sample_function():
    return "Called!"

def demonstrate_solutions():
    """Demonstrate all decorator solutions"""
    print("Decorators Solutions Demonstration\n")
    
    # Exercise 1: Simple Decorator
    print("1. Simple Decorator:")
    test_function_1()
    
    # Exercise 2: Timer Decorator
    print("\n2. Timer Decorator:")
    result = slow_function()
    print(f"Result: {result}")
    
    # Exercise 3: Logging Decorator
    print("\n3. Logging Decorator:")
    result = add_numbers(10, 5)
    
    # Exercise 4: Retry Decorator
    print("\n4. Retry Decorator:")
    random.seed(42)  # For reproducible results
    try:
        result = unreliable_function()
        print(f"Final result: {result}")
    except Exception as e:
        print(f"Failed after retries: {e}")
    
    # Exercise 5: Repeat Decorator
    print("\n5. Repeat Decorator:")
    greet_user("Alice")
    
    # Exercise 6: Validation Decorator
    print("\n6. Validation Decorator:")
    try:
        area = calculate_area(5, 3)
        print(f"Area: {area}")
        
        # This should raise an exception
        area = calculate_area(-5, 3)
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Exercise 7: Caching Decorator
    print("\n7. Caching Decorator:")
    print("First calculation:")
    result1 = fibonacci(10)
    print(f"Fibonacci(10) = {result1}")
    
    print("Second calculation (should use cache):")
    result2 = fibonacci(10)
    print(f"Fibonacci(10) = {result2}")
    
    # Exercise 8: Class-based Decorator
    print("\n8. Class-based Decorator:")
    for i in range(3):
        result = sample_function()
    
    # Exercise 9: Multiple Decorators
    print("\n9. Multiple Decorators:")
    result = complex_calculation(5)
    
    # Exercise 10: Property Decorator
    print("\n10. Property Decorator:")
    temp = Temperature(25)
    print(f"25°C = {temp.fahrenheit}°F = {temp.kelvin}K")
    
    temp.celsius = 0
    print(f"0°C = {temp.fahrenheit}°F = {temp.kelvin}K")
    
    try:
        temp.celsius = -300  # Should raise exception
    except ValueError as e:
        print(f"Validation error: {e}")

def advanced_decorator_examples():
    """Show additional advanced decorator examples"""
    print("\n" + "="*60)
    print("Advanced Decorator Examples")
    print("="*60)
    
    # Example 1: Rate Limiting Decorator
    print("\n1. Rate Limiting Decorator:")
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
    
    @rate_limit(max_calls=2, time_window=5)
    def api_call(endpoint):
        return f"Called {endpoint}"
    
    try:
        print(api_call("users"))
        print(api_call("posts"))
        print(api_call("comments"))  # This should fail
    except Exception as e:
        print(f"Rate limit error: {e}")
    
    # Example 2: Type Checking Decorator
    print("\n2. Type Checking Decorator:")
    def type_check(**expected_types):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                import inspect
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                
                for param_name, expected_type in expected_types.items():
                    if param_name in bound_args.arguments:
                        value = bound_args.arguments[param_name]
                        if not isinstance(value, expected_type):
                            raise TypeError(f"{param_name} must be {expected_type.__name__}, got {type(value).__name__}")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @type_check(name=str, age=int)
    def create_person(name, age):
        return f"Person: {name}, Age: {age}"
    
    try:
        person1 = create_person("Alice", 25)
        print(person1)
        
        person2 = create_person("Bob", "25")  # Should fail
    except TypeError as e:
        print(f"Type error: {e}")
    
    # Example 3: Conditional Decorator
    print("\n3. Conditional Decorator:")
    def conditional_decorator(condition):
        def decorator(func):
            if condition:
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    print(f"Decorator applied to {func.__name__}")
                    return func(*args, **kwargs)
                return wrapper
            else:
                return func  # Return original function unchanged
        return decorator
    
    DEBUG = True
    
    @conditional_decorator(DEBUG)
    def debug_function():
        return "Debug output"
    
    result = debug_function()
    print(f"Result: {result}")
    
    # Example 4: Decorator with Cleanup
    print("\n4. Decorator with Cleanup:")
    def with_cleanup(setup_func, cleanup_func):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                setup_func()
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    cleanup_func()
            return wrapper
        return decorator
    
    def setup():
        print("Setting up resources...")
    
    def cleanup():
        print("Cleaning up resources...")
    
    @with_cleanup(setup, cleanup)
    def process_data():
        print("Processing data...")
        return "Data processed"
    
    result = process_data()
    print(f"Result: {result}")

if __name__ == "__main__":
    demonstrate_solutions()
    advanced_decorator_examples()