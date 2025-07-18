"""
Decorators Exercises

Complete the following exercises to practice creating and using decorators.
Each exercise has test cases to verify your solution.
"""

import functools
import time
from datetime import datetime

# Exercise 1: Basic Decorator
# TODO: Create a decorator that prints "Before" and "After" around function calls
def simple_decorator(func):
    # Your decorator implementation here
    pass

# Exercise 2: Timing Decorator
# TODO: Create a decorator that measures and prints the execution time of a function
def timer_decorator(func):
    # Your decorator implementation here
    pass

# Exercise 3: Logging Decorator
# TODO: Create a decorator that logs function calls with timestamp, arguments, and return value
def log_decorator(func):
    # Your decorator implementation here
    pass

# Exercise 4: Retry Decorator
# TODO: Create a decorator that retries a function up to 3 times if it raises an exception
def retry_decorator(func):
    # Your decorator implementation here
    pass

# Exercise 5: Parameterized Decorator
# TODO: Create a decorator factory that repeats function execution N times
def repeat(times):
    # Your decorator factory implementation here
    pass

# Exercise 6: Validation Decorator
# TODO: Create a decorator that validates function arguments are positive numbers
def validate_positive(func):
    # Your decorator implementation here
    pass

# Exercise 7: Caching Decorator
# TODO: Create a simple memoization decorator that caches function results
def cache_decorator(func):
    # Your decorator implementation here
    pass

# Exercise 8: Class-based Decorator
# TODO: Create a class-based decorator that counts function calls
class CallCounter:
    # Your class-based decorator implementation here
    pass

# Exercise 9: Multiple Decorators
# TODO: Apply multiple decorators to a function and understand the order
# Apply timer_decorator and log_decorator to this function
def complex_calculation(n):
    """Calculate the sum of squares from 1 to n"""
    return sum(i**2 for i in range(1, n+1))

# Exercise 10: Property Decorator
# TODO: Create a class with properties using @property decorator
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    # TODO: Create a property for celsius with getter and setter
    # TODO: Create a read-only property for fahrenheit
    # TODO: Create a read-only property for kelvin
    pass


# Test Functions and Sample Usage

# Test functions for Exercise 1
@simple_decorator
def test_function_1():
    print("Inside test function 1")

# Test functions for Exercise 2
@timer_decorator
def slow_function():
    time.sleep(0.1)  # Simulate slow operation
    return "Completed"

# Test functions for Exercise 3
@log_decorator
def add_numbers(a, b):
    return a + b

# Test functions for Exercise 4
import random

@retry_decorator
def unreliable_function():
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("Random failure!")
    return "Success!"

# Test functions for Exercise 5
@repeat(times=3)
def greet_user(name):
    print(f"Hello, {name}!")

# Test functions for Exercise 6
@validate_positive
def calculate_area(length, width):
    return length * width

# Test functions for Exercise 7
@cache_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test functions for Exercise 8
@CallCounter
def sample_function():
    return "Called!"


def test_exercise_1():
    """Test simple decorator"""
    print("Testing Exercise 1: Simple Decorator")
    try:
        print("Expected output: 'Before', 'Inside test function 1', 'After'")
        test_function_1()
        print("✅ Exercise 1: Manual verification needed - check output above")
        return True
    except Exception as e:
        print(f"❌ Exercise 1: {e}")
        return False

def test_exercise_2():
    """Test timing decorator"""
    print("\nTesting Exercise 2: Timer Decorator")
    try:
        result = slow_function()
        print(f"Function returned: {result}")
        print("✅ Exercise 2: Manual verification needed - check if timing was printed")
        return True
    except Exception as e:
        print(f"❌ Exercise 2: {e}")
        return False

def test_exercise_3():
    """Test logging decorator"""
    print("\nTesting Exercise 3: Logging Decorator")
    try:
        result = add_numbers(5, 3)
        print(f"Function returned: {result}")
        print("✅ Exercise 3: Manual verification needed - check if logging was printed")
        return True
    except Exception as e:
        print(f"❌ Exercise 3: {e}")
        return False

def test_exercise_4():
    """Test retry decorator"""
    print("\nTesting Exercise 4: Retry Decorator")
    try:
        # Set seed for reproducible testing
        random.seed(42)
        result = unreliable_function()
        print(f"Function eventually returned: {result}")
        print("✅ Exercise 4: Manual verification needed - check if retries were attempted")
        return True
    except Exception as e:
        print(f"❌ Exercise 4: {e}")
        return False

def test_exercise_5():
    """Test repeat decorator"""
    print("\nTesting Exercise 5: Repeat Decorator")
    try:
        print("Expected: 'Hello, Alice!' printed 3 times")
        greet_user("Alice")
        print("✅ Exercise 5: Manual verification needed - check if function was called 3 times")
        return True
    except Exception as e:
        print(f"❌ Exercise 5: {e}")
        return False

def test_exercise_6():
    """Test validation decorator"""
    print("\nTesting Exercise 6: Validation Decorator")
    try:
        # Test with positive numbers
        result1 = calculate_area(5, 3)
        print(f"Area with positive numbers: {result1}")
        
        # Test with negative number (should raise exception)
        try:
            result2 = calculate_area(-5, 3)
            print("❌ Exercise 6: Should have raised exception for negative number")
            return False
        except ValueError:
            print("✅ Exercise 6: Correctly raised exception for negative number")
            return True
    except Exception as e:
        print(f"❌ Exercise 6: {e}")
        return False

def test_exercise_7():
    """Test caching decorator"""
    print("\nTesting Exercise 7: Caching Decorator")
    try:
        print("Computing fibonacci(10) - should show caching behavior")
        result = fibonacci(10)
        print(f"Fibonacci(10) = {result}")
        
        print("Computing fibonacci(10) again - should use cache")
        result2 = fibonacci(10)
        print(f"Fibonacci(10) = {result2}")
        
        if result == result2 == 55:
            print("✅ Exercise 7: Correct result - manual verification needed for caching behavior")
            return True
        else:
            print(f"❌ Exercise 7: Incorrect result. Expected 55, got {result}")
            return False
    except Exception as e:
        print(f"❌ Exercise 7: {e}")
        return False

def test_exercise_8():
    """Test class-based decorator"""
    print("\nTesting Exercise 8: Class-based Decorator")
    try:
        print("Calling function multiple times to test call counting:")
        for i in range(3):
            result = sample_function()
            print(f"Call {i+1}: {result}")
        
        print("✅ Exercise 8: Manual verification needed - check if call counts were printed")
        return True
    except Exception as e:
        print(f"❌ Exercise 8: {e}")
        return False

def test_exercise_9():
    """Test multiple decorators"""
    print("\nTesting Exercise 9: Multiple Decorators")
    try:
        print("Testing function with multiple decorators:")
        result = complex_calculation(5)
        print(f"Result: {result}")
        print("✅ Exercise 9: Manual verification needed - check decorator order")
        return True
    except Exception as e:
        print(f"❌ Exercise 9: {e}")
        return False

def test_exercise_10():
    """Test property decorator"""
    print("\nTesting Exercise 10: Property Decorator")
    try:
        temp = Temperature(25)
        
        # Test celsius property
        print(f"Celsius: {temp.celsius}")
        
        # Test fahrenheit property
        fahrenheit = temp.fahrenheit
        expected_fahrenheit = 25 * 9/5 + 32
        print(f"Fahrenheit: {fahrenheit} (expected: {expected_fahrenheit})")
        
        # Test kelvin property
        kelvin = temp.kelvin
        expected_kelvin = 25 + 273.15
        print(f"Kelvin: {kelvin} (expected: {expected_kelvin})")
        
        # Test setter
        temp.celsius = 0
        print(f"After setting to 0°C: {temp.celsius}°C, {temp.fahrenheit}°F, {temp.kelvin}K")
        
        # Test validation (should raise exception for invalid temperature)
        try:
            temp.celsius = -300  # Below absolute zero
            print("❌ Exercise 10: Should have raised exception for invalid temperature")
            return False
        except ValueError:
            print("✅ Exercise 10: Correctly raised exception for invalid temperature")
            return True
            
    except Exception as e:
        print(f"❌ Exercise 10: {e}")
        return False

def run_all_tests():
    """Run all test functions"""
    print("Running Decorators Exercises Tests...\n")
    
    tests = [
        test_exercise_1, test_exercise_2, test_exercise_3, test_exercise_4,
        test_exercise_5, test_exercise_6, test_exercise_7, test_exercise_8,
        test_exercise_9, test_exercise_10
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Results: {passed}/{total} tests passed")
    print("Note: Many decorator tests require manual verification of output behavior.")
    
    if passed == total:
        print("🎉 Congratulations! All decorator exercises completed successfully!")
    else:
        print("📚 Keep working on the remaining exercises. Decorators are powerful tools!")

if __name__ == "__main__":
    run_all_tests()