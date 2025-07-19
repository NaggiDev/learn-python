"""
Algorithm Complexity Analysis - Solutions

This file contains the solutions to the complexity analysis exercises.
Each solution includes detailed complexity analysis and explanations.
"""

import time
import random
from typing import List, Tuple, Dict


# Exercise 1: Basic Complexity Analysis - SOLUTIONS
def exercise_1_analyze_complexity():
    """
    Solutions with complexity analysis for each function.
    """
    
    # Time Complexity: O(n) - single loop through array
    # Space Complexity: O(1) - only using constant extra space
    def function_a(arr: List[int]) -> int:
        total = 0
        for num in arr:  # O(n) iterations
            total += num  # O(1) operation
        return total
    
    # Time Complexity: O(n²) - nested loops, each running n times
    # Space Complexity: O(n²) - result array can contain up to n² elements
    def function_b(arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):      # O(n) iterations
            for j in range(len(arr)):  # O(n) iterations for each i
                if i != j:             # O(1) comparison
                    result.append(arr[i] + arr[j])  # O(1) operation
        return result
    
    # Time Complexity: O(2^n) - exponential due to recursive calls
    # Space Complexity: O(n) - maximum recursion depth is n
    def function_c(n: int) -> int:
        if n <= 1:
            return n
        # Each call spawns 2 more calls, creating 2^n total calls
        return function_c(n - 1) + function_c(n - 2)
    
    # Time Complexity: O(n²) - nested loops with early termination possible
    # Space Complexity: O(1) - only using constant extra space
    def function_d(arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):          # O(n) iterations
            for j in range(i + 1, n):  # O(n) iterations in worst case
                if arr[i] == arr[j]:   # O(1) comparison
                    return True        # Early termination possible
        return False


# Exercise 2: Optimization Challenge - SOLUTIONS
def exercise_2_optimize_algorithms():
    """
    Optimized algorithms with improved time complexity.
    """
    
    def find_duplicates_fast(arr: List[int]) -> List[int]:
        """
        Find all duplicate elements in the array.
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(n) - hash set for tracking seen elements
        """
        seen = set()
        duplicates = set()
        
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        return list(duplicates)
    
    def two_sum_fast(arr: List[int], target: int) -> Tuple[int, int]:
        """
        Find two numbers that add up to target, return their indices.
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(n) - hash map for storing values and indices
        """
        num_to_index = {}
        
        for i, num in enumerate(arr):
            complement = target - num
            if complement in num_to_index:
                return (num_to_index[complement], i)
            num_to_index[num] = i
        
        return (-1, -1)


# Exercise 3: Space-Time Tradeoffs - SOLUTIONS
def exercise_3_space_time_tradeoffs():
    """
    Solutions exploring tradeoffs between time and space complexity.
    """
    
    def is_palindrome_constant_space(s: str) -> bool:
        """
        Check if string is palindrome using constant extra space.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def is_palindrome_linear_space(s: str) -> bool:
        """
        Check if string is palindrome using linear extra space.
        Time Complexity: O(n) for first check, O(1) for subsequent checks
        Space Complexity: O(n) - stores reversed string
        
        This version is faster for repeated checks on the same string
        because it can cache the reversed version.
        """
        # In a real implementation, you might cache this globally
        reversed_s = s[::-1]
        return s == reversed_s
    
    def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
        """
        Fibonacci with memoization.
        Time Complexity: O(n) - each number calculated once
        Space Complexity: O(n) - memo dictionary + recursion stack
        """
        if memo is None:
            memo = {}
        
        if n in memo:
            return memo[n]
        
        if n <= 1:
            return n
        
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
        return memo[n]
    
    def fibonacci_iterative(n: int) -> int:
        """
        Iterative Fibonacci.
        Time Complexity: O(n)
        Space Complexity: O(1) - only uses constant extra space
        """
        if n <= 1:
            return n
        
        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        
        return prev1


# Exercise 4: Complexity Comparison - SOLUTIONS
def exercise_4_complexity_comparison():
    """
    Performance comparison between different algorithms.
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
    
    def compare_search_algorithms(sizes: List[int]) -> None:
        """
        Compare linear search vs binary search performance.
        """
        print("Search Algorithm Performance Comparison")
        print("-" * 50)
        print(f"{'Size':<10} {'Linear (ms)':<12} {'Binary (ms)':<12} {'Speedup':<10}")
        print("-" * 50)
        
        for size in sizes:
            # Generate sorted test data
            arr = list(range(size))
            target = size // 2  # Middle element
            
            # Measure linear search
            start_time = time.time()
            for _ in range(100):  # Run multiple times for better measurement
                linear_search(arr, target)
            linear_time = (time.time() - start_time) * 1000 / 100
            
            # Measure binary search
            start_time = time.time()
            for _ in range(100):  # Run multiple times for better measurement
                binary_search(arr, target)
            binary_time = (time.time() - start_time) * 1000 / 100
            
            speedup = linear_time / binary_time if binary_time > 0 else float('inf')
            
            print(f"{size:<10} {linear_time:<12.4f} {binary_time:<12.4f} {speedup:<10.2f}x")


# Exercise 5: Algorithm Design Challenge - SOLUTIONS
def exercise_5_design_challenge():
    """
    Advanced algorithm design solutions.
    """
    
    def find_kth_largest_efficient(arr: List[int], k: int) -> int:
        """
        Find the kth largest element using quickselect algorithm.
        Time Complexity: O(n) average case, O(n²) worst case
        Space Complexity: O(1) if implemented iteratively
        """
        def quickselect(arr, left, right, k):
            if left == right:
                return arr[left]
            
            # Partition the array
            pivot_index = partition(arr, left, right)
            
            # The pivot is in its final sorted position
            if k == pivot_index:
                return arr[k]
            elif k < pivot_index:
                return quickselect(arr, left, pivot_index - 1, k)
            else:
                return quickselect(arr, pivot_index + 1, right, k)
        
        def partition(arr, left, right):
            # Choose rightmost element as pivot
            pivot = arr[right]
            i = left
            
            for j in range(left, right):
                if arr[j] >= pivot:  # For kth largest, we want descending order
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            
            arr[i], arr[right] = arr[right], arr[i]
            return i
        
        # Make a copy to avoid modifying original array
        arr_copy = arr.copy()
        return quickselect(arr_copy, 0, len(arr_copy) - 1, k - 1)
    
    def has_cycle_efficient(arr: List[int]) -> bool:
        """
        Detect cycle using Floyd's cycle detection algorithm (tortoise and hare).
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr:
            return False
        
        # Start both pointers at index 0
        slow = fast = 0
        
        # Move pointers until they meet or fast goes out of bounds
        while True:
            # Move slow pointer one step
            if slow < 0 or slow >= len(arr):
                return False
            slow = arr[slow]
            
            # Move fast pointer two steps
            if fast < 0 or fast >= len(arr):
                return False
            fast = arr[fast]
            if fast < 0 or fast >= len(arr):
                return False
            fast = arr[fast]
            
            # If pointers meet, there's a cycle
            if slow == fast:
                return True
    
    def string_match_efficient(text: str, pattern: str) -> List[int]:
        """
        Find all occurrences using KMP (Knuth-Morris-Pratt) algorithm.
        Time Complexity: O(n + m) where n = len(text), m = len(pattern)
        Space Complexity: O(m) for the failure function
        """
        if not pattern:
            return []
        
        # Build failure function (partial match table)
        def build_failure_function(pattern):
            failure = [0] * len(pattern)
            j = 0
            
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = failure[j - 1]
                
                if pattern[i] == pattern[j]:
                    j += 1
                
                failure[i] = j
            
            return failure
        
        failure = build_failure_function(pattern)
        matches = []
        j = 0  # Index for pattern
        
        for i in range(len(text)):  # Index for text
            while j > 0 and text[i] != pattern[j]:
                j = failure[j - 1]
            
            if text[i] == pattern[j]:
                j += 1
            
            if j == len(pattern):
                matches.append(i - j + 1)
                j = failure[j - 1]
        
        return matches


# Performance Testing and Demonstration
def demonstrate_complexity_differences():
    """
    Demonstrate the practical impact of different complexities.
    """
    print("Complexity Demonstration")
    print("=" * 50)
    
    # Demonstrate exponential vs linear Fibonacci
    print("Fibonacci Performance Comparison:")
    print("-" * 30)
    
    def fibonacci_exponential(n):
        if n <= 1:
            return n
        return fibonacci_exponential(n - 1) + fibonacci_exponential(n - 2)
    
    def fibonacci_linear(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    test_values = [10, 20, 25, 30]
    
    for n in test_values:
        # Linear version
        start_time = time.time()
        result_linear = fibonacci_linear(n)
        linear_time = time.time() - start_time
        
        # Exponential version (only for smaller values)
        if n <= 25:
            start_time = time.time()
            result_exp = fibonacci_exponential(n)
            exp_time = time.time() - start_time
            speedup = exp_time / linear_time if linear_time > 0 else float('inf')
            print(f"n={n}: Linear={linear_time:.6f}s, Exponential={exp_time:.6f}s, Speedup={speedup:.0f}x")
        else:
            print(f"n={n}: Linear={linear_time:.6f}s, Exponential=too slow!")


# Test all solutions
def test_all_solutions():
    """Test all solution implementations."""
    print("Testing All Solutions")
    print("=" * 50)
    
    # Test Exercise 2 solutions
    print("Testing optimized algorithms:")
    
    # Test find_duplicates_fast
    test_arr = [1, 2, 3, 2, 4, 5, 3]
    result = find_duplicates_fast(test_arr)
    print(f"find_duplicates_fast([1,2,3,2,4,5,3]) = {result}")
    
    # Test two_sum_fast
    test_arr = [2, 7, 11, 15]
    result = two_sum_fast(test_arr, 9)
    print(f"two_sum_fast([2,7,11,15], 9) = {result}")
    
    # Test Exercise 3 solutions
    print("\nTesting Fibonacci implementations:")
    for n in [10, 20, 30]:
        result_memo = fibonacci_memoized(n)
        result_iter = fibonacci_iterative(n)
        print(f"fibonacci({n}): memoized={result_memo}, iterative={result_iter}")
    
    # Test Exercise 5 solutions
    print("\nTesting advanced algorithms:")
    
    # Test kth largest
    test_arr = [3, 2, 1, 5, 6, 4]
    result = find_kth_largest_efficient(test_arr, 2)
    print(f"find_kth_largest([3,2,1,5,6,4], 2) = {result}")
    
    # Test cycle detection
    cycle_arr = [1, 2, 3, 1]  # 0->1->2->3->1 (cycle)
    no_cycle_arr = [1, 2, 3, 0]  # 0->1->2->3->0 (no cycle, goes out of bounds)
    print(f"has_cycle([1,2,3,1]) = {has_cycle_efficient(cycle_arr)}")
    
    # Test string matching
    text = "ababcababa"
    pattern = "ababa"
    matches = string_match_efficient(text, pattern)
    print(f"string_match('{text}', '{pattern}') = {matches}")


if __name__ == "__main__":
    test_all_solutions()
    print("\n")
    demonstrate_complexity_differences()
    print("\n")
    compare_search_algorithms([1000, 10000, 100000])