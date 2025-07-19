"""
Heap Sort Algorithm Implementation

This module implements the Heap Sort algorithm using a binary heap.
Heap Sort builds a max heap from the input array and repeatedly extracts
the maximum element to build the sorted array.

Time Complexity: O(n log n) in all cases
Space Complexity: O(1) - sorts in place
"""

from typing import List, TypeVar

T = TypeVar('T')


def heap_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using the Heap Sort algorithm.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        New sorted list
        
    Time Complexity: O(n log n)
    Space Complexity: O(1) - sorts in place
    
    Example:
        >>> heap_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr.copy()
    
    # TODO: Implement heap sort algorithm
    # 1. Build a max heap from the input array
    # 2. Repeatedly extract the maximum element
    # 3. Place it at the end of the sorted portion
    pass


def _build_max_heap(arr: List[T]) -> None:
    """
    Build a max heap from an unsorted array.
    
    Args:
        arr: Array to convert to max heap (modified in place)
        
    Time Complexity: O(n)
    """
    # TODO: Build max heap by calling heapify on all non-leaf nodes
    # Start from the last non-leaf node and work backwards
    pass


def _heapify(arr: List[T], n: int, i: int) -> None:
    """
    Maintain the max heap property for a subtree rooted at index i.
    
    Args:
        arr: Array representing the heap
        n: Size of the heap
        i: Index of the root of the subtree
        
    Time Complexity: O(log n)
    """
    # TODO: Implement heapify to maintain max heap property
    # Compare root with its children and swap if necessary
    # Recursively heapify the affected subtree
    pass


def _parent(i: int) -> int:
    """Get the parent index of node at index i."""
    return (i - 1) // 2


def _left_child(i: int) -> int:
    """Get the left child index of node at index i."""
    return 2 * i + 1


def _right_child(i: int) -> int:
    """Get the right child index of node at index i."""
    return 2 * i + 2