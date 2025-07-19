"""
Radix Sort Algorithm Implementation

This module implements the Radix Sort algorithm for integers.
Radix Sort is a non-comparative sorting algorithm that sorts integers
by processing individual digits.

Time Complexity: O(d * (n + k)) where d is number of digits, k is range of digits
Space Complexity: O(n + k)
"""

from typing import List


def radix_sort(arr: List[int]) -> List[int]:
    """
    Sort an array of non-negative integers using Radix Sort.
    
    Args:
        arr: List of non-negative integers to sort
        
    Returns:
        New sorted list
        
    Time Complexity: O(d * (n + k)) where d is digits, k is base (10)
    Space Complexity: O(n + k)
    
    Example:
        >>> radix_sort([170, 45, 75, 90, 2, 802, 24, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]
    """
    if not arr or len(arr) <= 1:
        return arr.copy()
    
    # TODO: Implement radix sort algorithm
    # 1. Find the maximum number to determine number of digits
    # 2. Sort by each digit position using counting sort
    # 3. Process from least significant to most significant digit
    pass


def _counting_sort_by_digit(arr: List[int], exp: int) -> List[int]:
    """
    Sort array by a specific digit position using counting sort.
    
    Args:
        arr: Array to sort
        exp: Exponent representing the digit position (1, 10, 100, etc.)
        
    Returns:
        Array sorted by the specified digit
        
    Time Complexity: O(n + k) where k is the range of digits (0-9)
    Space Complexity: O(n + k)
    """
    # TODO: Implement counting sort for specific digit position
    # Use the digit at position 'exp' as the key for sorting
    pass


def _get_max(arr: List[int]) -> int:
    """
    Find the maximum value in the array.
    
    Args:
        arr: Array of integers
        
    Returns:
        Maximum value in the array
    """
    # TODO: Find and return the maximum value
    pass


def radix_sort_with_negatives(arr: List[int]) -> List[int]:
    """
    Sort an array of integers (including negative numbers) using Radix Sort.
    
    This version handles negative numbers by separating them, sorting separately,
    and then combining the results.
    
    Args:
        arr: List of integers (can include negative numbers)
        
    Returns:
        New sorted list
        
    Time Complexity: O(d * (n + k))
    Space Complexity: O(n + k)
    """
    if not arr or len(arr) <= 1:
        return arr.copy()
    
    # TODO: Implement radix sort for arrays with negative numbers
    # 1. Separate positive and negative numbers
    # 2. Sort positive numbers normally
    # 3. Sort absolute values of negative numbers and reverse
    # 4. Combine results
    pass