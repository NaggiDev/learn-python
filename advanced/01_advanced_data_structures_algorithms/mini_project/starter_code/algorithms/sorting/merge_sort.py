"""
Merge Sort Algorithm Implementation

This module implements the Merge Sort algorithm in both recursive and iterative versions.
Merge Sort is a stable, divide-and-conquer algorithm that divides the array into halves,
sorts them separately, and then merges them back together.

Time Complexity: O(n log n) in all cases
Space Complexity: O(n) for auxiliary arrays
"""

from typing import List, TypeVar

T = TypeVar('T')


def merge_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using the recursive Merge Sort algorithm.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        New sorted list
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Example:
        >>> merge_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr.copy()
    
    # TODO: Implement recursive merge sort
    # 1. Divide the array into two halves
    # 2. Recursively sort both halves
    # 3. Merge the sorted halves
    pass


def merge_sort_iterative(arr: List[T]) -> List[T]:
    """
    Sort an array using the iterative Merge Sort algorithm.
    
    This version uses bottom-up approach, starting with subarrays of size 1
    and doubling the size in each iteration.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        New sorted list
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr.copy()
    
    # TODO: Implement iterative merge sort
    # Use bottom-up approach with increasing subarray sizes
    pass


def _merge(left: List[T], right: List[T]) -> List[T]:
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left: First sorted array
        right: Second sorted array
        
    Returns:
        Merged sorted array
        
    Time Complexity: O(n + m) where n, m are lengths of input arrays
    Space Complexity: O(n + m)
    """
    # TODO: Implement merge function
    # Compare elements from both arrays and merge in sorted order
    pass


def _merge_inplace(arr: List[T], left: int, mid: int, right: int) -> None:
    """
    Merge two sorted subarrays in place.
    
    Args:
        arr: Array containing both subarrays
        left: Starting index of first subarray
        mid: Ending index of first subarray
        right: Ending index of second subarray
    """
    # TODO: Implement in-place merge for iterative version
    # This is more complex but saves space
    pass