"""
Exercise 3: Debugging Practice

This file contains several functions with bugs. Your task is to:
1. Identify the bugs
2. Fix them
3. Add appropriate debugging techniques
4. Test your fixes

Instructions:
1. Run each function to see the error
2. Use debugging techniques (print statements, pdb, etc.) to identify the issue
3. Fix the bug
4. Add comments explaining what was wrong
5. Test with the provided test cases

Run this file to see the bugs in action: python 03_debugging_practice.py
"""

import pdb


def buggy_factorial(n):
    """
    Calculate factorial of n.
    Bug: This function has a logic error.
    """
    if n == 0:
        return 1
    
    result = 0  # BUG: Should be 1, not 0
    for i in range(1, n):  # BUG: Should be range(1, n+1)
        result *= i
    
    return result


def buggy_find_average(numbers):
    """
    Find the average of a list of numbers.
    Bug: This function has multiple issues.
    """
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    # BUG: No check for empty list
    average = total / count
    return average


def buggy_reverse_words(sentence):
    """
    Reverse the order of words in a sentence.
    Bug: This function doesn't work correctly.
    """
    words = sentence.split(" ")
    reversed_words = []
    
    # BUG: Logic error in the loop
    for i in range(len(words)):
        reversed_words.append(words[i])
    
    return " ".join(reversed_words)


def buggy_count_vowels(text):
    """
    Count the number of vowels in a text.
    Bug: This function has a subtle error.
    """
    vowels = "aeiou"
    count = 0
    
    for char in text:
        # BUG: Not handling uppercase vowels
        if char in vowels:
            count += 1
    
    return count


def buggy_fibonacci(n):
    """
    Generate the nth Fibonacci number.
    Bug: This function has an off-by-one error.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # BUG: Logic error in the calculation
    a, b = 0, 1
    for i in range(2, n):  # BUG: Should be range(2, n+1)
        a, b = b, a + b
    
    return a  # BUG: Should return b


def buggy_remove_duplicates(lst):
    """
    Remove duplicates from a list while preserving order.
    Bug: This function modifies the list incorrectly.
    """
    # BUG: Modifying list while iterating
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                lst.remove(lst[j])  # BUG: This changes indices
    
    return lst


def buggy_is_palindrome(text):
    """
    Check if a text is a palindrome (ignoring spaces and case).
    Bug: This function doesn't handle spaces and case correctly.
    """
    # BUG: Not removing spaces or handling case
    cleaned = text
    return cleaned == cleaned[::-1]


def buggy_grade_calculator(scores):
    """
    Calculate letter grades for a list of numeric scores.
    Bug: This function has boundary condition errors.
    """
    grades = []
    
    for score in scores:
        # BUG: Incorrect boundary conditions
        if score > 90:  # BUG: Should be >= 90
            grades.append('A')
        elif score > 80:  # BUG: Should be >= 80
            grades.append('B')
        elif score > 70:  # BUG: Should be >= 70
            grades.append('C')
        elif score > 60:  # BUG: Should be >= 60
            grades.append('D')
        else:
            grades.append('F')
    
    return grades


def buggy_binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    Bug: This function has logic errors.
    """
    left = 0
    right = len(arr)  # BUG: Should be len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def buggy_word_frequency(text):
    """
    Count the frequency of each word in a text.
    Bug: This function doesn't handle punctuation correctly.
    """
    # BUG: Not handling punctuation
    words = text.split()
    frequency = {}
    
    for word in words:
        # BUG: Not converting to lowercase
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency


# Test functions - DO NOT MODIFY THESE
def test_functions():
    """Test all the buggy functions to see the errors."""
    
    print("Testing buggy_factorial:")
    try:
        result = buggy_factorial(5)
        print(f"factorial(5) = {result} (should be 120)")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_find_average:")
    try:
        result = buggy_find_average([1, 2, 3, 4, 5])
        print(f"average([1,2,3,4,5]) = {result} (should be 3.0)")
        
        result = buggy_find_average([])
        print(f"average([]) = {result} (should handle empty list)")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_reverse_words:")
    try:
        result = buggy_reverse_words("hello world python")
        print(f"reverse_words('hello world python') = '{result}' (should be 'python world hello')")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_count_vowels:")
    try:
        result = buggy_count_vowels("Hello World")
        print(f"count_vowels('Hello World') = {result} (should be 3)")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_fibonacci:")
    try:
        result = buggy_fibonacci(7)
        print(f"fibonacci(7) = {result} (should be 13)")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_remove_duplicates:")
    try:
        test_list = [1, 2, 2, 3, 3, 3, 4]
        result = buggy_remove_duplicates(test_list.copy())
        print(f"remove_duplicates([1,2,2,3,3,3,4]) = {result} (should be [1,2,3,4])")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_is_palindrome:")
    try:
        result = buggy_is_palindrome("A man a plan a canal Panama")
        print(f"is_palindrome('A man a plan a canal Panama') = {result} (should be True)")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_grade_calculator:")
    try:
        result = buggy_grade_calculator([90, 85, 70, 60, 50])
        print(f"grade_calculator([90,85,70,60,50]) = {result} (should be ['A','B','C','D','F'])")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_binary_search:")
    try:
        result = buggy_binary_search([1, 3, 5, 7, 9], 5)
        print(f"binary_search([1,3,5,7,9], 5) = {result} (should be 2)")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting buggy_word_frequency:")
    try:
        result = buggy_word_frequency("Hello, world! Hello Python.")
        print(f"word_frequency('Hello, world! Hello Python.') = {result}")
        print("(should handle punctuation and case)")
    except Exception as e:
        print(f"Error: {e}")


# Debugging exercise template
def debug_with_prints_example():
    """
    Example of how to debug using print statements.
    This function demonstrates debugging the factorial function.
    """
    def debug_factorial(n):
        print(f"DEBUG: factorial called with n={n}")
        
        if n == 0:
            print("DEBUG: Base case, returning 1")
            return 1
        
        result = 1  # Fixed: was 0
        print(f"DEBUG: Initial result = {result}")
        
        for i in range(1, n + 1):  # Fixed: was range(1, n)
            print(f"DEBUG: Loop iteration i={i}, result before={result}")
            result *= i
            print(f"DEBUG: result after multiply = {result}")
        
        print(f"DEBUG: Final result = {result}")
        return result
    
    print("Debugging factorial with print statements:")
    debug_factorial(5)


def debug_with_pdb_example():
    """
    Example of how to use pdb for debugging.
    Uncomment the pdb.set_trace() line to activate debugging.
    """
    def debug_average(numbers):
        # pdb.set_trace()  # Uncomment this line to start debugging
        
        if not numbers:  # Fixed: added empty list check
            return 0
        
        total = 0
        count = 0
        
        for num in numbers:
            total += num
            count += 1
        
        average = total / count
        return average
    
    print("Example with pdb (uncomment pdb.set_trace() to try):")
    result = debug_average([1, 2, 3, 4, 5])
    print(f"Average: {result}")


if __name__ == "__main__":
    print("=" * 50)
    print("DEBUGGING EXERCISE")
    print("=" * 50)
    print("This file contains buggy functions. Your task is to fix them.")
    print("Run the test functions to see the bugs in action.\n")
    
    test_functions()
    
    print("\n" + "=" * 50)
    print("DEBUGGING EXAMPLES")
    print("=" * 50)
    
    debug_with_prints_example()
    print()
    debug_with_pdb_example()
    
    print("\n" + "=" * 50)
    print("YOUR TASK:")
    print("1. Fix each buggy function above")
    print("2. Add comments explaining what was wrong")
    print("3. Test your fixes by running this file again")
    print("4. Practice using different debugging techniques")
    print("=" * 50)