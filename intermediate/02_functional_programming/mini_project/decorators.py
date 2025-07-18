"""
Decorators Module

This module contains custom decorators for the data processing pipeline.
Implement the decorators below to add logging, timing, and validation functionality.
"""

import functools
import time
from datetime import datetime
from typing import Any, Callable, Dict, List

# TODO: Implement the decorators below

def timer(func: Callable) -> Callable:
    """
    Decorator that measures and logs the execution time of a function.
    
    Args:
        func: Function to be decorated
        
    Returns:
        Wrapped function that logs execution time
    """
    # TODO: Implement this decorator
    # Hint: Use time.time() to measure execution time
    pass

def logger(func: Callable) -> Callable:
    """
    Decorator that logs function calls with arguments and return values.
    
    Args:
        func: Function to be decorated
        
    Returns:
        Wrapped function that logs calls
    """
    # TODO: Implement this decorator
    # Hint: Log function name, arguments, and return value
    pass

def validate_data(required_fields: List[str] = None) -> Callable:
    """
    Decorator factory that validates data has required fields.
    
    Args:
        required_fields: List of required field names
        
    Returns:
        Decorator function
    """
    # TODO: Implement this decorator factory
    # Hint: Check if data (first argument) has all required fields
    pass

def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """
    Decorator factory that retries function execution on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between retries in seconds
        
    Returns:
        Decorator function
    """
    # TODO: Implement this decorator factory
    # Hint: Catch exceptions and retry up to max_attempts times
    pass

def cache_results(func: Callable) -> Callable:
    """
    Decorator that caches function results to avoid repeated calculations.
    
    Args:
        func: Function to be decorated
        
    Returns:
        Wrapped function with caching
    """
    # TODO: Implement this decorator
    # Hint: Use a dictionary to store results based on function arguments
    pass

def rate_limit(calls_per_second: float) -> Callable:
    """
    Decorator factory that limits the rate of function calls.
    
    Args:
        calls_per_second: Maximum number of calls per second
        
    Returns:
        Decorator function
    """
    # TODO: Implement this decorator factory
    # Hint: Track call times and add delays if necessary
    pass

def exception_handler(default_return: Any = None, log_errors: bool = True) -> Callable:
    """
    Decorator factory that handles exceptions gracefully.
    
    Args:
        default_return: Value to return if exception occurs
        log_errors: Whether to log errors
        
    Returns:
        Decorator function
    """
    # TODO: Implement this decorator factory
    # Hint: Catch exceptions and return default value or re-raise
    pass

def performance_monitor(func: Callable) -> Callable:
    """
    Decorator that monitors function performance and resource usage.
    
    Args:
        func: Function to be decorated
        
    Returns:
        Wrapped function that monitors performance
    """
    # TODO: Implement this decorator
    # Hint: Monitor execution time, memory usage, and call frequency
    pass

# Utility functions for decorators
def log_message(message: str, level: str = "INFO") -> None:
    """
    Log a message with timestamp and level.
    
    Args:
        message: Message to log
        level: Log level (INFO, WARNING, ERROR)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {level}: {message}")

def format_args_kwargs(args: tuple, kwargs: dict) -> str:
    """
    Format function arguments for logging.
    
    Args:
        args: Positional arguments
        kwargs: Keyword arguments
        
    Returns:
        Formatted string representation of arguments
    """
    arg_strs = [repr(arg) for arg in args]
    kwarg_strs = [f"{k}={repr(v)}" for k, v in kwargs.items()]
    all_args = arg_strs + kwarg_strs
    return ", ".join(all_args)

# Example usage and test functions
@timer
@logger
def sample_function(x: int, y: int = 10) -> int:
    """Sample function for testing decorators."""
    time.sleep(0.1)  # Simulate some work
    return x + y

@validate_data(required_fields=["id", "name"])
def process_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """Sample function that processes a record."""
    return {"processed": True, **record}

@retry(max_attempts=3, delay=0.5)
def unreliable_function() -> str:
    """Function that sometimes fails for testing retry decorator."""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("Random failure!")
    return "Success!"

@cache_results
def expensive_calculation(n: int) -> int:
    """Expensive calculation for testing cache decorator."""
    time.sleep(0.1)  # Simulate expensive operation
    return sum(range(n))

def test_decorators():
    """Test all decorators to ensure they work correctly."""
    print("Testing decorators...")
    
    # Test timer and logger decorators
    print("\n1. Testing timer and logger decorators:")
    try:
        result = sample_function(5, y=15)
        print(f"   Result: {result}")
        print("   ✅ Timer and logger decorators work!")
    except Exception as e:
        print(f"   ❌ Timer/logger decorator error: {e}")
    
    # Test validation decorator
    print("\n2. Testing validation decorator:")
    try:
        valid_record = {"id": 1, "name": "Test", "extra": "data"}
        result = process_record(valid_record)
        print(f"   Valid record result: {result}")
        
        # This should raise an exception
        try:
            invalid_record = {"id": 1}  # Missing 'name' field
            process_record(invalid_record)
            print("   ❌ Validation should have failed!")
        except Exception:
            print("   ✅ Validation correctly rejected invalid data!")
    except Exception as e:
        print(f"   ❌ Validation decorator error: {e}")
    
    # Test retry decorator
    print("\n3. Testing retry decorator:")
    try:
        import random
        random.seed(42)  # For reproducible results
        result = unreliable_function()
        print(f"   Retry result: {result}")
        print("   ✅ Retry decorator works!")
    except Exception as e:
        print(f"   ❌ Retry decorator error: {e}")
    
    # Test cache decorator
    print("\n4. Testing cache decorator:")
    try:
        print("   First call (should be slow):")
        start_time = time.time()
        result1 = expensive_calculation(1000)
        time1 = time.time() - start_time
        
        print("   Second call (should be fast - cached):")
        start_time = time.time()
        result2 = expensive_calculation(1000)
        time2 = time.time() - start_time
        
        print(f"   First call time: {time1:.3f}s, Second call time: {time2:.3f}s")
        if time2 < time1 / 2:  # Second call should be much faster
            print("   ✅ Cache decorator works!")
        else:
            print("   ❌ Cache decorator may not be working properly")
    except Exception as e:
        print(f"   ❌ Cache decorator error: {e}")

if __name__ == "__main__":
    test_decorators()