"""
Algorithm Complexity Analysis Exercises

This file contains exercises to practice analyzing algorithm complexity.
For each function, determine the time and space complexity and implement
the requested optimizations.

Instructions:
1. Analyze the time and space complexity of each function
2. Write your analysis in the comments above each function
3. Implement the optimized versions where requested
4. Run the tests to verify your implementations
"""

import time
import random
from typing import List, Tuple


# Exercise 1: Basic Complexity Analysis
def exercise_1_analyze_complexity():
    """
    Analyze the time and space complexity of the following functions.
    Write your analysis in the comments above each function.
    """
    
    # TODO: Analyze this function's complexity
    # Time Complexity: ?
    # Space Complexity: ?
    def function_a(arr: List[int]) -> int:
        total = 0
        for num in arr:
            total += num
        return total
    
    # TODO: Analyze this function's complexity
    # Time Complexity: ?
    # Space Complexity: ?
    def function_b(arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    result.append(arr[i] + arr[j])
        return result
    
    # TODO: Analyze this function's complexity
    # Time Complexity: ?
    # Space Complexity: ?
    def function_c(n: int) -> int:
        if n <= 1:
            return n
        return function_c(n - 1) + function_c(n - 2)
    
    # TODO: Analyze this function's complexity
    # Time Complexity: ?
    # Space Complexity: ?
    def function_d(arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    return True
        return False


# Exercise 2: Optimization Challenge
def exercise_2_optimize_algorithms():
    """
    Optimize the given algorithms to improve their time complexity.
    """
    
    # Original: O(n²) time complexity
    def find_duplicates_slow(arr: List[int]) -> List[int]:
        """Find all duplicate elements in the array."""
        duplicates = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j] and arr[i] not in duplicates:
                    duplicates.append(arr[i])
        return duplicates
    
    # TODO: Implement an optimized version with better time complexity
    def find_duplicates_fast(arr: List[int]) -> List[int]:
        """
        Find all duplicate elements in the array.
        Target: O(n) time complexity
        """
        # TODO: Implement optimized version
        pass
    
    # Original: O(n²) time complexity
    def two_sum_slow(arr: List[int], target: int) -> Tuple[int, int]:
        """Find two numbers that add up to target, return their indices."""
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    return (i, j)
        return (-1, -1)
    
    # TODO: Implement an optimized version with better time complexity
    def two_sum_fast(arr: List[int], target: int) -> Tuple[int, int]:
        """
        Find two numbers that add up to target, return their indices.
        Target: O(n) time complexity
        """
        # TODO: Implement optimized version
        pass


# Exercise 3: Space-Time Tradeoffs
def exercise_3_space_time_tradeoffs():
    """
    Explore tradeoffs between time and space complexity.
    """
    
    # Version 1: O(1) space, O(n²) time
    def is_palindrome_constant_space(s: str) -> bool:
        """Check if string is palindrome using constant extra space."""
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    # TODO: Implement a version that trades space for time
    def is_palindrome_linear_space(s: str) -> bool:
        """
        Check if string is palindrome using linear extra space.
        This version should be faster for repeated checks on the same string.
        """
        # TODO: Implement version that uses more space but could be faster
        # for repeated operations
        pass
    
    # Fibonacci with exponential time complexity
    def fibonacci_slow(n: int) -> int:
        """Naive recursive Fibonacci - O(2^n) time."""
        if n <= 1:
            return n
        return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)
    
    # TODO: Implement optimized Fibonacci using memoization
    def fibonacci_memoized(n: int, memo: dict = None) -> int:
        """
        Fibonacci with memoization - O(n) time, O(n) space.
        """
        # TODO: Implement memoized version
        pass
    
    # TODO: Implement iterative Fibonacci
    def fibonacci_iterative(n: int) -> int:
        """
        Iterative Fibonacci - O(n) time, O(1) space.
        """
        # TODO: Implement iterative version
        pass


# Exercise 4: Complexity Comparison
def exercise_4_complexity_comparison():
    """
    Compare different algorithms and measure their actual performance.
    """
    
    def linear_search(arr: List[int], target: int) -> int:
        """O(n) search algorithm."""
        for i, element in enumerate(arr):
            if element == target:
                return i
        return -1
    
    def binary_search(arr: List[int], target: int) -> int:
        """O(log n) search algorithm - requires sorted array."""
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    # TODO: Implement a function to measure and compare performance
    def compare_search_algorithms(sizes: List[int]) -> None:
        """
        Compare linear search vs binary search performance.
        Create arrays of different sizes and measure execution time.
        """
        # TODO: Implement performance comparison
        pass


# Exercise 5: Algorithm Design Challenge
def exercise_5_design_challenge():
    """
    Design algorithms with specific complexity requirements.
    """
    
    # TODO: Design an algorithm to find the kth largest element
    def find_kth_largest_efficient(arr: List[int], k: int) -> int:
        """
        Find the kth largest element in the array.
        Target: Better than O(n log n) time complexity
        Hint: Consider using quickselect algorithm
        """
        # TODO: Implement efficient kth largest algorithm
        pass
    
    # TODO: Design an algorithm to detect cycles in a list
    def has_cycle_efficient(arr: List[int]) -> bool:
        """
        Detect if there's a cycle when following array indices.
        arr[i] represents the next index to visit from index i.
        Target: O(n) time, O(1) space
        Hint: Consider Floyd's cycle detection algorithm
        """
        # TODO: Implement cycle detection
        pass
    
    # TODO: Design an algorithm for efficient string matching
    def string_match_efficient(text: str, pattern: str) -> List[int]:
        """
        Find all occurrences of pattern in text.
        Target: Better than O(n*m) time complexity
        Hint: Consider KMP or Rabin-Karp algorithm
        """
        # TODO: Implement efficient string matching
        pass


# Performance Testing Utilities
def measure_time(func, *args, **kwargs):
    """Utility function to measure execution time."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time


def generate_test_data(size: int, max_value: int = 1000) -> List[int]:
    """Generate random test data for performance testing."""
    return [random.randint(1, max_value) for _ in range(size)]


# Test Functions
def test_exercise_1():
    """Test complexity analysis exercise."""
    print("Testing Exercise 1: Complexity Analysis")
    
    # Test data
    test_arr = [1, 2, 3, 4, 5]
    
    # These should work with the original functions
    # (Students need to analyze complexity, not modify functions)
    print("✓ Exercise 1 functions are ready for analysis")


def test_exercise_2():
    """Test optimization exercise."""
    print("Testing Exercise 2: Algorithm Optimization")
    
    # Test find_duplicates
    test_arr = [1, 2, 3, 2, 4, 5, 3]
    expected_duplicates = [2, 3]  # Order may vary
    
    try:
        result = find_duplicates_fast(test_arr)
        if set(result) == set(expected_duplicates):
            print("✓ find_duplicates_fast works correctly")
        else:
            print("✗ find_duplicates_fast incorrect result")
    except:
        print("✗ find_duplicates_fast not implemented")
    
    # Test two_sum
    test_arr = [2, 7, 11, 15]
    target = 9
    expected = (0, 1)  # indices of 2 and 7
    
    try:
        result = two_sum_fast(test_arr, target)
        if result == expected or result == (1, 0):
            print("✓ two_sum_fast works correctly")
        else:
            print("✗ two_sum_fast incorrect result")
    except:
        print("✗ two_sum_fast not implemented")


def test_exercise_3():
    """Test space-time tradeoffs exercise."""
    print("Testing Exercise 3: Space-Time Tradeoffs")
    
    # Test Fibonacci implementations
    test_cases = [0, 1, 5, 10]
    expected = [0, 1, 5, 55]
    
    for i, n in enumerate(test_cases):
        try:
            result = fibonacci_memoized(n)
            if result == expected[i]:
                print(f"✓ fibonacci_memoized({n}) = {result}")
            else:
                print(f"✗ fibonacci_memoized({n}) = {result}, expected {expected[i]}")
        except:
            print(f"✗ fibonacci_memoized not implemented")
        
        try:
            result = fibonacci_iterative(n)
            if result == expected[i]:
                print(f"✓ fibonacci_iterative({n}) = {result}")
            else:
                print(f"✗ fibonacci_iterative({n}) = {result}, expected {expected[i]}")
        except:
            print(f"✗ fibonacci_iterative not implemented")


def test_exercise_4():
    """Test complexity comparison exercise."""
    print("Testing Exercise 4: Complexity Comparison")
    
    try:
        compare_search_algorithms([100, 1000, 10000])
        print("✓ Performance comparison completed")
    except:
        print("✗ compare_search_algorithms not implemented")


def test_exercise_5():
    """Test algorithm design challenge."""
    print("Testing Exercise 5: Design Challenge")
    
    # Test kth largest
    test_arr = [3, 2, 1, 5, 6, 4]
    k = 2
    expected = 5  # 2nd largest is 5
    
    try:
        result = find_kth_largest_efficient(test_arr, k)
        if result == expected:
            print("✓ find_kth_largest_efficient works correctly")
        else:
            print("✗ find_kth_largest_efficient incorrect result")
    except:
        print("✗ find_kth_largest_efficient not implemented")


def run_all_tests():
    """Run all test functions."""
    print("=" * 50)
    print("ALGORITHM COMPLEXITY EXERCISES - TEST RESULTS")
    print("=" * 50)
    
    test_exercise_1()
    print()
    test_exercise_2()
    print()
    test_exercise_3()
    print()
    test_exercise_4()
    print()
    test_exercise_5()
    
    print("\n" + "=" * 50)
    print("Complete the TODO sections to pass all tests!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()