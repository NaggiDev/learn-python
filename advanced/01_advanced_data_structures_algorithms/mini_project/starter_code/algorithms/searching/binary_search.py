"""
Binary Search Algorithm Implementation

This module implements binary search in both iterative and recursive versions.
Binary search works on sorted arrays by repeatedly dividing the search interval in half.

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""

from typing import List, TypeVar, Optional

T = TypeVar('T')


def binary_search(arr: List[T], target: T) -> Optional[int]:
    """
    Search for a target value in a sorted array using iterative binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
        
    Returns:
        Index of target if found, None otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Example:
        >>> binary_search([1, 3, 5, 7, 9, 11], 7)
        3
        >>> binary_search([1, 3, 5, 7, 9, 11], 4)
        None
    """
    if not arr:
        return None
    
    # TODO: Implement iterative binary search
    # Use two pointers (left and right) and narrow the search space
    pass


def binary_search_recursive(arr: List[T], target: T, left: int = 0, right: Optional[int] = None) -> Optional[int]:
    """
    Search for a target value in a sorted array using recursive binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
        left: Left boundary of search range
        right: Right boundary of search range
        
    Returns:
        Index of target if found, None otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if not arr:
        return None
    
    if right is None:
        right = len(arr) - 1
    
    # TODO: Implement recursive binary search
    # Base case: left > right means element not found
    # Recursive case: compare with middle element and search appropriate half
    pass


def binary_search_leftmost(arr: List[T], target: T) -> Optional[int]:
    """
    Find the leftmost occurrence of target in a sorted array with duplicates.
    
    Args:
        arr: Sorted list of comparable elements (may contain duplicates)
        target: Element to search for
        
    Returns:
        Index of leftmost occurrence if found, None otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # TODO: Implement binary search to find leftmost occurrence
    # Continue searching left even after finding the target
    pass


def binary_search_rightmost(arr: List[T], target: T) -> Optional[int]:
    """
    Find the rightmost occurrence of target in a sorted array with duplicates.
    
    Args:
        arr: Sorted list of comparable elements (may contain duplicates)
        target: Element to search for
        
    Returns:
        Index of rightmost occurrence if found, None otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # TODO: Implement binary search to find rightmost occurrence
    # Continue searching right even after finding the target
    pass


def binary_search_range(arr: List[T], target: T) -> tuple[Optional[int], Optional[int]]:
    """
    Find the range of indices where target appears in a sorted array.
    
    Args:
        arr: Sorted list of comparable elements (may contain duplicates)
        target: Element to search for
        
    Returns:
        Tuple of (leftmost_index, rightmost_index) if found, (None, None) otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # TODO: Use leftmost and rightmost binary search to find range
    pass