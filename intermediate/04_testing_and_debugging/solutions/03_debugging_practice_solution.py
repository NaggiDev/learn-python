"""
Solution: Debugging Practice

This file contains the fixed versions of all the buggy functions
with explanations of what was wrong and how it was fixed.
"""

import pdb
import string


def fixed_factorial(n):
    """
    Calculate factorial of n.
    
    Bugs fixed:
    1. result was initialized to 0 instead of 1
    2. range was range(1, n) instead of range(1, n+1)
    """
    if n == 0:
        return 1
    
    result = 1  # FIXED: Changed from 0 to 1
    for i in range(1, n + 1):  # FIXED: Changed from range(1, n) to range(1, n+1)
        result *= i
    
    return result


def fixed_find_average(numbers):
    """
    Find the average of a list of numbers.
    
    Bugs fixed:
    1. No check for empty list causing division by zero
    """
    if not numbers:  # FIXED: Added check for empty list
        return 0  # or raise ValueError("Cannot calculate average of empty list")
    
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    average = total / count
    return average


def fixed_reverse_words(sentence):
    """
    Reverse the order of words in a sentence.
    
    Bugs fixed:
    1. The loop was appending words in the same order instead of reversing
    """
    words = sentence.split(" ")
    reversed_words = []
    
    # FIXED: Iterate backwards through the list
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    
    # Alternative fix: return " ".join(words[::-1])
    return " ".join(reversed_words)


def fixed_count_vowels(text):
    """
    Count the number of vowels in a text.
    
    Bugs fixed:
    1. Not handling uppercase vowels
    """
    vowels = "aeiouAEIOU"  # FIXED: Added uppercase vowels
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count


def fixed_fibonacci(n):
    """
    Generate the nth Fibonacci number.
    
    Bugs fixed:
    1. Range was range(2, n) instead of range(2, n+1)
    2. Returning 'a' instead of 'b'
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, n + 1):  # FIXED: Changed from range(2, n) to range(2, n+1)
        a, b = b, a + b
    
    return b  # FIXED: Changed from returning 'a' to returning 'b'


def fixed_remove_duplicates(lst):
    """
    Remove duplicates from a list while preserving order.
    
    Bugs fixed:
    1. Modifying list while iterating causes index issues
    
    Solution: Use a different approach that doesn't modify the original list during iteration
    """
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result


def fixed_is_palindrome(text):
    """
    Check if a text is a palindrome (ignoring spaces and case).
    
    Bugs fixed:
    1. Not removing spaces
    2. Not handling case sensitivity
    """
    # FIXED: Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    
    # Alternative: Remove all non-alphanumeric characters
    # cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    return cleaned == cleaned[::-1]


def fixed_grade_calculator(scores):
    """
    Calculate letter grades for a list of numeric scores.
    
    Bugs fixed:
    1. All boundary conditions used > instead of >=
    """
    grades = []
    
    for score in scores:
        # FIXED: Changed all > to >= for correct boundary conditions
        if score >= 90:
            grades.append('A')
        elif score >= 80:
            grades.append('B')
        elif score >= 70:
            grades.append('C')
        elif score >= 60:
            grades.append('D')
        else:
            grades.append('F')
    
    return grades


def fixed_binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Bugs fixed:
    1. right was initialized to len(arr) instead of len(arr) - 1
    """
    left = 0
    right = len(arr) - 1  # FIXED: Changed from len(arr) to len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def fixed_word_frequency(text):
    """
    Count the frequency of each word in a text.
    
    Bugs fixed:
    1. Not handling punctuation
    2. Not converting to lowercase for case-insensitive counting
    """
    # FIXED: Remove punctuation and convert to lowercase
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    
    words = cleaned_text.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency


# Alternative debugging approaches for some functions
def factorial_with_debug_prints(n):
    """Factorial with debug prints to show the debugging process."""
    print(f"DEBUG: Calculating factorial of {n}")
    
    if n == 0:
        print("DEBUG: Base case reached, returning 1")
        return 1
    
    result = 1
    print(f"DEBUG: Starting with result = {result}")
    
    for i in range(1, n + 1):
        old_result = result
        result *= i
        print(f"DEBUG: Step {i}: {old_result} * {i} = {result}")
    
    print(f"DEBUG: Final result = {result}")
    return result


def fibonacci_with_assertions(n):
    """Fibonacci with assertions to catch errors early."""
    assert n >= 0, f"n must be non-negative, got {n}"
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    
    for i in range(2, n + 1):
        old_a, old_b = a, b
        a, b = b, a + b
        
        # Assertion to verify the sequence is correct
        assert b == old_a + old_b, f"Fibonacci sequence error at step {i}"
    
    return b


def remove_duplicates_with_logging(lst):
    """Remove duplicates with detailed logging."""
    import logging
    
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    
    logger.debug(f"Input list: {lst}")
    
    seen = set()
    result = []
    
    for i, item in enumerate(lst):
        logger.debug(f"Processing item {i}: {item}")
        
        if item not in seen:
            logger.debug(f"Item {item} is new, adding to result")
            seen.add(item)
            result.append(item)
        else:
            logger.debug(f"Item {item} already seen, skipping")
    
    logger.debug(f"Final result: {result}")
    return result


# Test functions for the fixed versions
def test_fixed_functions():
    """Test all the fixed functions to verify they work correctly."""
    
    print("Testing fixed_factorial:")
    result = fixed_factorial(5)
    print(f"factorial(5) = {result} (expected: 120) - {'✓' if result == 120 else '✗'}")
    
    print("\nTesting fixed_find_average:")
    result = fixed_find_average([1, 2, 3, 4, 5])
    print(f"average([1,2,3,4,5]) = {result} (expected: 3.0) - {'✓' if result == 3.0 else '✗'}")
    
    result = fixed_find_average([])
    print(f"average([]) = {result} (expected: 0) - {'✓' if result == 0 else '✗'}")
    
    print("\nTesting fixed_reverse_words:")
    result = fixed_reverse_words("hello world python")
    expected = "python world hello"
    print(f"reverse_words('hello world python') = '{result}' (expected: '{expected}') - {'✓' if result == expected else '✗'}")
    
    print("\nTesting fixed_count_vowels:")
    result = fixed_count_vowels("Hello World")
    print(f"count_vowels('Hello World') = {result} (expected: 3) - {'✓' if result == 3 else '✗'}")
    
    print("\nTesting fixed_fibonacci:")
    result = fixed_fibonacci(7)
    print(f"fibonacci(7) = {result} (expected: 13) - {'✓' if result == 13 else '✗'}")
    
    print("\nTesting fixed_remove_duplicates:")
    test_list = [1, 2, 2, 3, 3, 3, 4]
    result = fixed_remove_duplicates(test_list)
    expected = [1, 2, 3, 4]
    print(f"remove_duplicates([1,2,2,3,3,3,4]) = {result} (expected: {expected}) - {'✓' if result == expected else '✗'}")
    
    print("\nTesting fixed_is_palindrome:")
    result = fixed_is_palindrome("A man a plan a canal Panama")
    print(f"is_palindrome('A man a plan a canal Panama') = {result} (expected: True) - {'✓' if result == True else '✗'}")
    
    print("\nTesting fixed_grade_calculator:")
    result = fixed_grade_calculator([90, 85, 70, 60, 50])
    expected = ['A', 'B', 'C', 'D', 'F']
    print(f"grade_calculator([90,85,70,60,50]) = {result} (expected: {expected}) - {'✓' if result == expected else '✗'}")
    
    print("\nTesting fixed_binary_search:")
    result = fixed_binary_search([1, 3, 5, 7, 9], 5)
    print(f"binary_search([1,3,5,7,9], 5) = {result} (expected: 2) - {'✓' if result == 2 else '✗'}")
    
    print("\nTesting fixed_word_frequency:")
    result = fixed_word_frequency("Hello, world! Hello Python.")
    expected_keys = {'hello', 'world', 'python'}
    actual_keys = set(result.keys())
    print(f"word_frequency('Hello, world! Hello Python.') = {result}")
    print(f"Keys match expected: {'✓' if actual_keys == expected_keys else '✗'}")
    print(f"'hello' count: {result.get('hello', 0)} (expected: 2) - {'✓' if result.get('hello', 0) == 2 else '✗'}")


def demonstrate_debugging_techniques():
    """Demonstrate various debugging techniques."""
    
    print("\n" + "=" * 60)
    print("DEBUGGING TECHNIQUES DEMONSTRATION")
    print("=" * 60)
    
    print("\n1. Debug with print statements:")
    factorial_with_debug_prints(4)
    
    print("\n2. Debug with assertions:")
    try:
        result = fibonacci_with_assertions(6)
        print(f"Fibonacci(6) with assertions: {result}")
    except AssertionError as e:
        print(f"Assertion error caught: {e}")
    
    print("\n3. Debug with logging:")
    remove_duplicates_with_logging([1, 2, 2, 3, 1, 4])


# Common debugging patterns and tips
class DebuggingTips:
    """Collection of debugging tips and patterns."""
    
    @staticmethod
    def print_debug(func):
        """Decorator to add debug prints to any function."""
        def wrapper(*args, **kwargs):
            print(f"DEBUG: Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"DEBUG: {func.__name__} returned {result}")
            return result
        return wrapper
    
    @staticmethod
    def safe_divide(a, b):
        """Example of defensive programming with detailed error information."""
        try:
            if not isinstance(a, (int, float)):
                raise TypeError(f"First argument must be a number, got {type(a)}")
            if not isinstance(b, (int, float)):
                raise TypeError(f"Second argument must be a number, got {type(b)}")
            if b == 0:
                raise ValueError("Cannot divide by zero")
            
            result = a / b
            return result
            
        except Exception as e:
            print(f"Error in safe_divide({a}, {b}): {e}")
            print(f"Types: a={type(a)}, b={type(b)}")
            raise
    
    @staticmethod
    def debug_list_operation(lst, operation):
        """Debug helper for list operations."""
        print(f"DEBUG: List before {operation}: {lst}")
        print(f"DEBUG: List length: {len(lst)}")
        print(f"DEBUG: List type: {type(lst)}")
        
        if lst:
            print(f"DEBUG: First element: {lst[0]} (type: {type(lst[0])})")
            print(f"DEBUG: Last element: {lst[-1]} (type: {type(lst[-1])})")


if __name__ == "__main__":
    print("=" * 60)
    print("DEBUGGING PRACTICE - SOLUTIONS")
    print("=" * 60)
    
    test_fixed_functions()
    
    demonstrate_debugging_techniques()
    
    print("\n" + "=" * 60)
    print("DEBUGGING TIPS:")
    print("1. Read error messages carefully")
    print("2. Use print statements to trace execution")
    print("3. Check boundary conditions")
    print("4. Verify your assumptions with assertions")
    print("5. Use the debugger for complex issues")
    print("6. Create minimal test cases")
    print("7. Don't change too much at once")
    print("=" * 60)