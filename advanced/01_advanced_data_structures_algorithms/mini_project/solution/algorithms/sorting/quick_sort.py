"""
Quick Sort Algorithm Implementation - Reference Solution

This module implements the Quick Sort algorithm with optimizations.
Quick Sort is a divide-and-conquer algorithm that picks a 'pivot' element
and partitions the array around the pivot.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n) 
- Worst Case: O(n²)

Space Complexity: O(log n) due to recursion stack
"""

from typing import List, TypeVar
import random

T = TypeVar('T')


def quick_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using the Quick Sort algorithm.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        New sorted list
        
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) for recursion stack
    
    Example:
        >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr.copy()
    
    result = arr.copy()
    _quick_sort_inplace(result, 0, len(result) - 1)
    return result


def quick_sort_optimized(arr: List[T]) -> List[T]:
    """
    Optimized Quick Sort with improvements for small arrays and better pivot selection.
    
    Optimizations:
    1. Use insertion sort for small arrays (< 10 elements)
    2. Use median-of-three pivot selection
    3. Handle duplicate elements efficiently
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        New sorted list
        
    Time Complexity: O(n log n) average, O(n²) worst case (but rare)
    Space Complexity: O(log n) for recursion stack
    """
    if len(arr) <= 1:
        return arr.copy()
    
    result = arr.copy()
    _quick_sort_optimized_inplace(result, 0, len(result) - 1)
    return result


def _quick_sort_inplace(arr: List[T], low: int, high: int) -> None:
    """
    In-place quick sort implementation.
    
    Args:
        arr: Array to sort (modified in place)
        low: Starting index
        high: Ending index
    """
    if low < high:
        # Partition the array and get pivot index
        pivot_index = _partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        _quick_sort_inplace(arr, low, pivot_index - 1)
        _quick_sort_inplace(arr, pivot_index + 1, high)


def _quick_sort_optimized_inplace(arr: List[T], low: int, high: int) -> None:
    """
    Optimized in-place quick sort implementation.
    
    Args:
        arr: Array to sort (modified in place)
        low: Starting index
        high: Ending index
    """
    while low < high:
        # Use insertion sort for small subarrays
        if high - low + 1 < 10:
            _insertion_sort(arr, low, high)
            break
        
        # Use median-of-three for pivot selection
        median_index = _median_of_three(arr, low, high)
        arr[median_index], arr[high] = arr[high], arr[median_index]
        
        # Partition the array
        pivot_index = _partition(arr, low, high)
        
        # Recursively sort the smaller partition, iterate on the larger
        # This reduces the recursion depth
        if pivot_index - low < high - pivot_index:
            _quick_sort_optimized_inplace(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            _quick_sort_optimized_inplace(arr, pivot_index + 1, high)
            high = pivot_index - 1


def _partition(arr: List[T], low: int, high: int) -> int:
    """
    Partition function for quick sort using Lomuto partition scheme.
    
    Args:
        arr: Array to partition
        low: Starting index
        high: Ending index
        
    Returns:
        Index of the pivot after partitioning
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element (indicates right position of pivot)
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _median_of_three(arr: List[T], low: int, high: int) -> int:
    """
    Find median of three elements for better pivot selection.
    
    Args:
        arr: Array to find median from
        low: Starting index
        high: Ending index
        
    Returns:
        Index of median element
    """
    mid = (low + high) // 2
    
    # Sort the three elements and return middle index
    if arr[low] > arr[mid]:
        if arr[mid] > arr[high]:
            return mid
        elif arr[low] > arr[high]:
            return high
        else:
            return low
    else:  # arr[low] <= arr[mid]
        if arr[low] > arr[high]:
            return low
        elif arr[mid] > arr[high]:
            return high
        else:
            return mid


def _insertion_sort(arr: List[T], low: int, high: int) -> None:
    """
    Insertion sort for small subarrays (in-place).
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
    """
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key


# Additional utility functions for analysis

def quick_sort_with_stats(arr: List[T]) -> tuple[List[T], dict]:
    """
    Quick sort that also returns performance statistics.
    
    Args:
        arr: List to sort
        
    Returns:
        Tuple of (sorted_list, stats_dict)
    """
    if len(arr) <= 1:
        return arr.copy(), {"comparisons": 0, "swaps": 0, "recursion_depth": 0}
    
    stats = {"comparisons": 0, "swaps": 0, "recursion_depth": 0}
    result = arr.copy()
    _quick_sort_with_stats(result, 0, len(result) - 1, stats, 0)
    return result, stats


def _quick_sort_with_stats(arr: List[T], low: int, high: int, stats: dict, depth: int) -> None:
    """Quick sort with statistics tracking."""
    stats["recursion_depth"] = max(stats["recursion_depth"], depth)
    
    if low < high:
        pivot_index, partition_stats = _partition_with_stats(arr, low, high)
        stats["comparisons"] += partition_stats["comparisons"]
        stats["swaps"] += partition_stats["swaps"]
        
        _quick_sort_with_stats(arr, low, pivot_index - 1, stats, depth + 1)
        _quick_sort_with_stats(arr, pivot_index + 1, high, stats, depth + 1)


def _partition_with_stats(arr: List[T], low: int, high: int) -> tuple[int, dict]:
    """Partition with statistics tracking."""
    stats = {"comparisons": 0, "swaps": 0}
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        stats["comparisons"] += 1
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                stats["swaps"] += 1
    
    if i + 1 != high:
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stats["swaps"] += 1
    
    return i + 1, stats