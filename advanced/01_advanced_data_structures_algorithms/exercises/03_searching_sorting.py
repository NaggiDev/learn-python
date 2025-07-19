"""
Searching and Sorting Algorithms Exercises

This file contains exercises to practice implementing and optimizing
searching and sorting algorithms. Focus on understanding the algorithms,
their complexity, and when to use each one.

Instructions:
1. Implement each algorithm according to the specifications
2. Pay attention to time and space complexity
3. Consider edge cases and optimizations
4. Run the tests to verify your implementations
"""

import random
import time
from typing import List, Tuple, Optional, Callable


# Exercise 1: Searching Algorithms
def exercise_1_searching_algorithms():
    """
    Implement various searching algorithms and compare their performance.
    """
    
    # TODO: Implement linear search
    def linear_search(arr: List[int], target: int) -> int:
        """
        Find target in array using linear search.
        
        Args:
            arr: List of integers to search
            target: Value to find
        
        Returns:
            Index of target if found, -1 otherwise
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Examples:
            linear_search([1, 3, 5, 7, 9], 5) -> 2
            linear_search([1, 3, 5, 7, 9], 6) -> -1
        """
        # TODO: Implement linear search
        pass
    
    # TODO: Implement binary search (iterative)
    def binary_se