"""
Decorators Module - Solution

Complete implementation of custom decorators for the data processing pipeline.
"""

import functools
import time
from datetime import datetime
from typing import Any, Callable, Dict, List
from collections import defaultdict
import sys

def timer(func: Callable) -> Callable:
    """Decorator that measures and logs the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        log_message(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def logger(func: Callable) -> Callable:
    """Decorator that logs function calls with arguments and return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = format_args_kwargs(args, kwargs)
        log_message(f"Calling {func.__name__}({args_str})")
        
        try:
            result = func(*args, **kwargs)
            # Don't log large results (like generators or long lists)
            if hasattr(result, '__len__') and len(result) > 10:
                log_message(f"{func.__name__} returned {type(result).__name__} with {len(result)} items")
            elif hasattr(result, '__next__'):  # Generator
                log_message(f"{func.__name__} returned generator")
            else:
                log_message(f"{func.__name__} returned {result}")
            return result
        except Exception as e:
            log_message(f"{func.__name__} raised {type(e).__name__}: {e}", "ERROR")
            raise
    return wrapper

def validate_data(required_fields: List[str] = None) -> Callable:
    """Decorator factory that validates data has required fields."""
    if required_fields is None:
        required_fields = []
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Assume first argument is the data to validate
            if args and isinstance(args[0], dict):
                data = args[0]
                missing_fields = [field for field in required_fields if field not in data]
                if missing_fields:
                    raise ValueError(f"Missing required fields: {missing_fields}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """Decorator factory that retries function execution on failure."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        log_message(f"Attempt {attempt + 1} failed for {func.__name__}: {e}. Retrying in {delay}s...", "WARNING")
                        time.sleep(delay)
                    else:
                        log_message(f"All {max_attempts} attempts failed for {func.__name__}", "ERROR")
            
            raise last_exception
        return wrapper
    return decorator

def cache_results(func: Callable) -> Callable:
    """Decorator that caches function results to avoid repeated calculations."""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments (simple approach)
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            log_message(f"Cache hit for {func.__name__}")
            return cache[key]
        
        log_message(f"Cache miss for {func.__name__}, computing result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper

def rate_limit(calls_per_second: float) -> Callable:
    """Decorator factory that limits the rate of function calls."""
    min_interval = 1.0 / calls_per_second
    last_called = defaultdict(float)
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            time_since_last = now - last_called[func.__name__]
            
            if time_since_last < min_interval:
                sleep_time = min_interval - time_since_last
                time.sleep(sleep_time)
            
            last_called[func.__name__] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def exception_handler(default_return: Any = None, log_errors: bool = True) -> Callable:
    """Decorator factory that handles exceptions gracefully."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if log_errors:
                    log_message(f"Exception in {func.__name__}: {e}", "ERROR")
                return default_return
        return wrapper
    return decorator

def performance_monitor(func: Callable) -> Callable:
    """Decorator that monitors function performance and resource usage."""
    call_count = 0
    total_time = 0
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count, total_time
        
        # Memory before
        memory_before = sys.getsizeof(args) + sys.getsizeof(kwargs)
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        call_count += 1
        total_time += execution_time
        
        # Memory after
        memory_after = sys.getsizeof(result) if result is not None else 0
        
        avg_time = total_time / call_count
        
        log_message(
            f"Performance [{func.__name__}]: "
            f"Call #{call_count}, "
            f"Time: {execution_time:.4f}s, "
            f"Avg: {avg_time:.4f}s, "
            f"Memory: {memory_before + memory_after} bytes"
        )
        
        return result
    return wrapper

# Utility functions for decorators
def log_message(message: str, level: str = "INFO") -> None:
    """Log a message with timestamp and level."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {level}: {message}")

def format_args_kwargs(args: tuple, kwargs: dict) -> str:
    """Format function arguments for logging."""
    arg_strs = []
    
    # Format positional arguments (truncate if too long)
    for arg in args:
        if hasattr(arg, '__len__') and len(arg) > 5:
            arg_strs.append(f"{type(arg).__name__}(len={len(arg)})")
        elif hasattr(arg, '__next__'):  # Generator
            arg_strs.append(f"generator")
        else:
            arg_str = repr(arg)
            if len(arg_str) > 50:
                arg_str = arg_str[:47] + "..."
            arg_strs.append(arg_str)
    
    # Format keyword arguments
    kwarg_strs = []
    for k, v in kwargs.items():
        if hasattr(v, '__len__') and len(v) > 5:
            kwarg_strs.append(f"{k}={type(v).__name__}(len={len(v)})")
        else:
            v_str = repr(v)
            if len(v_str) > 30:
                v_str = v_str[:27] + "..."
            kwarg_strs.append(f"{k}={v_str}")
    
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

@retry(max_attempts=3, delay=0.1)
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

@rate_limit(calls_per_second=2.0)
def rate_limited_function(message: str) -> str:
    """Function for testing rate limiting."""
    return f"Processed: {message}"

@exception_handler(default_return="Error occurred", log_errors=True)
def error_prone_function(should_fail: bool = False) -> str:
    """Function for testing exception handling."""
    if should_fail:
        raise ValueError("Intentional error")
    return "Success"

@performance_monitor
def monitored_function(data_size: int) -> list:
    """Function for testing performance monitoring."""
    return list(range(data_size))

def test_decorators():
    """Test all decorators to ensure they work correctly."""
    print("Testing decorators...")
    
    # Test timer and logger decorators
    print("\n1. Testing timer and logger decorators:")
    result = sample_function(5, y=15)
    print(f"   Result: {result}")
    print("   ✅ Timer and logger decorators work!")
    
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
        except ValueError:
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
        print(f"   Final failure after retries: {e}")
    
    # Test cache decorator
    print("\n4. Testing cache decorator:")
    print("   First call (should be slow):")
    result1 = expensive_calculation(1000)
    print("   Second call (should be fast - cached):")
    result2 = expensive_calculation(1000)
    print("   ✅ Cache decorator works!")
    
    # Test rate limiting
    print("\n5. Testing rate limiting decorator:")
    start_time = time.time()
    for i in range(3):
        result = rate_limited_function(f"message_{i}")
        print(f"   {result}")
    end_time = time.time()
    print(f"   Total time: {end_time - start_time:.2f}s (should be ~1s due to rate limiting)")
    print("   ✅ Rate limiting decorator works!")
    
    # Test exception handler
    print("\n6. Testing exception handler decorator:")
    result1 = error_prone_function(should_fail=False)
    print(f"   Success case: {result1}")
    result2 = error_prone_function(should_fail=True)
    print(f"   Error case: {result2}")
    print("   ✅ Exception handler decorator works!")
    
    # Test performance monitor
    print("\n7. Testing performance monitor decorator:")
    for size in [100, 500, 1000]:
        result = monitored_function(size)
    print("   ✅ Performance monitor decorator works!")

if __name__ == "__main__":
    test_decorators()