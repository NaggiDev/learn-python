"""
Test Suite for Sorting Algorithms

This module contains comprehensive tests for all sorting algorithm implementations
including correctness tests, edge cases, and performance tests.
"""

import pytest
import random
from typing import List, Callable
from algorithms.sorting import (
    quick_sort, quick_sort_optimized,
    merge_sort, merge_sort_iterative,
    heap_sort, radix_sort
)


class TestSortingAlgorithms:
    """Test class for all sorting algorithms."""
    
    @pytest.fixture
    def sorting_algorithms(self) -> List[Callable]:
        """Fixture providing all sorting algorithms to test."""
        return [
            quick_sort,
            quick_sort_optimized,
            merge_sort,
            merge_sort_iterative,
            heap_sort,
        ]
    
    @pytest.fixture
    def integer_sorting_algorithms(self) -> List[Callable]:
        """Fixture providing sorting algorithms that work on integers."""
        return [radix_sort]
    
    @pytest.fixture
    def test_arrays(self) -> List[List[int]]:
        """Fixture providing various test arrays."""
        return [
            [],  # Empty array
            [1],  # Single element
            [1, 2],  # Two elements (sorted)
            [2, 1],  # Two elements (reverse)
            [1, 1],  # Two identical elements
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],  # Random array
            [1, 2, 3, 4, 5],  # Already sorted
            [5, 4, 3, 2, 1],  # Reverse sorted
            [1, 1, 1, 1, 1],  # All identical
            list(range(100)),  # Large sorted array
            list(range(100, 0, -1)),  # Large reverse sorted
            [random.randint(1, 1000) for _ in range(100)],  # Large random
        ]
    
    def test_empty_array(self, sorting_algorithms):
        """Test sorting empty arrays."""
        for sort_func in sorting_algorithms:
            result = sort_func([])
            assert result == []
    
    def test_single_element(self, sorting_algorithms):
        """Test sorting single-element arrays."""
        for sort_func in sorting_algorithms:
            result = sort_func([42])
            assert result == [42]
    
    def test_two_elements(self, sorting_algorithms):
        """Test sorting two-element arrays."""
        for sort_func in sorting_algorithms:
            assert sort_func([1, 2]) == [1, 2]
            assert sort_func([2, 1]) == [1, 2]
            assert sort_func([1, 1]) == [1, 1]
    
    def test_correctness(self, sorting_algorithms, test_arrays):
        """Test that all algorithms produce correct sorted output."""
        for sort_func in sorting_algorithms:
            for test_array in test_arrays:
                result = sort_func(test_array.copy())
                expected = sorted(test_array)
                assert result == expected, f"{sort_func.__name__} failed on {test_array}"
    
    def test_stability_preservation(self):
        """Test that stable sorting algorithms preserve relative order of equal elements."""
        # TODO: Implement stability test using objects with equal keys
        # Create test data with equal keys but different secondary values
        # Verify that stable sorts preserve the original order
        pass
    
    def test_original_array_unchanged(self, sorting_algorithms):
        """Test that original arrays are not modified."""
        original = [3, 1, 4, 1, 5, 9, 2, 6]
        original_copy = original.copy()
        
        for sort_func in sorting_algorithms:
            sort_func(original)
            assert original == original_copy, f"{sort_func.__name__} modified original array"
    
    def test_large_arrays(self, sorting_algorithms):
        """Test sorting large arrays."""
        large_array = [random.randint(1, 10000) for _ in range(1000)]
        expected = sorted(large_array)
        
        for sort_func in sorting_algorithms:
            result = sort_func(large_array.copy())
            assert result == expected, f"{sort_func.__name__} failed on large array"
    
    def test_radix_sort_integers(self, integer_sorting_algorithms):
        """Test radix sort with integer arrays."""
        test_arrays = [
            [],
            [0],
            [1, 0],
            [170, 45, 75, 90, 2, 802, 24, 66],
            [1000, 999, 998, 997, 996],
            [1, 1, 1, 1, 1],
        ]
        
        for sort_func in integer_sorting_algorithms:
            for test_array in test_arrays:
                result = sort_func(test_array.copy())
                expected = sorted(test_array)
                assert result == expected, f"{sort_func.__name__} failed on {test_array}"
    
    def test_radix_sort_negative_numbers(self):
        """Test radix sort with negative numbers if implemented."""
        # TODO: Test radix_sort_with_negatives if implemented
        pass
    
    @pytest.mark.performance
    def test_performance_comparison(self, sorting_algorithms):
        """Compare performance of different sorting algorithms."""
        # TODO: Implement performance comparison test
        # Generate different types of input (random, sorted, reverse)
        # Measure execution time for each algorithm
        # Assert reasonable performance characteristics
        pass
    
    def test_worst_case_performance(self):
        """Test algorithms on their worst-case inputs."""
        # TODO: Test each algorithm on inputs that trigger worst-case behavior
        # Quick sort: already sorted array (without optimization)
        # Merge sort: any input (consistent O(n log n))
        # Heap sort: any input (consistent O(n log n))
        pass
    
    def test_best_case_performance(self):
        """Test algorithms on their best-case inputs."""
        # TODO: Test each algorithm on inputs that trigger best-case behavior
        pass
    
    def test_memory_usage(self):
        """Test memory usage of sorting algorithms."""
        # TODO: Measure memory usage of each algorithm
        # In-place algorithms should use O(1) extra space
        # Merge sort should use O(n) extra space
        pass


class TestQuickSort:
    """Specific tests for Quick Sort implementations."""
    
    def test_partition_function(self):
        """Test the partition function if accessible."""
        # TODO: Test partition function directly if it's exposed
        pass
    
    def test_pivot_selection(self):
        """Test different pivot selection strategies."""
        # TODO: Test median-of-three vs last element pivot
        pass
    
    def test_optimization_threshold(self):
        """Test that optimized version uses insertion sort for small arrays."""
        # TODO: Verify that optimized quick sort switches to insertion sort
        pass


class TestMergeSort:
    """Specific tests for Merge Sort implementations."""
    
    def test_merge_function(self):
        """Test the merge function if accessible."""
        # TODO: Test merge function directly
        pass
    
    def test_iterative_vs_recursive(self):
        """Test that iterative and recursive versions produce same results."""
        test_arrays = [
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
            [random.randint(1, 100) for _ in range(50)],
        ]
        
        for test_array in test_arrays:
            recursive_result = merge_sort(test_array.copy())
            iterative_result = merge_sort_iterative(test_array.copy())
            assert recursive_result == iterative_result


class TestHeapSort:
    """Specific tests for Heap Sort implementation."""
    
    def test_heap_property(self):
        """Test that heap property is maintained during sorting."""
        # TODO: Test heap property if heap building functions are exposed
        pass


class TestRadixSort:
    """Specific tests for Radix Sort implementation."""
    
    def test_digit_extraction(self):
        """Test digit extraction for radix sort."""
        # TODO: Test digit extraction functions if exposed
        pass
    
    def test_counting_sort_by_digit(self):
        """Test counting sort by specific digit."""
        # TODO: Test counting sort function if exposed
        pass
    
    def test_non_negative_integers_only(self):
        """Test that radix sort works only with non-negative integers."""
        with pytest.raises((ValueError, TypeError)):
            radix_sort([-1, 2, 3])


# Property-based testing using hypothesis (if available)
try:
    from hypothesis import given, strategies as st
    
    class TestSortingProperties:
        """Property-based tests for sorting algorithms."""
        
        @given(st.lists(st.integers()))
        def test_sorting_property(self, arr):
            """Test that sorting produces a sorted array."""
            for sort_func in [quick_sort, merge_sort, heap_sort]:
                result = sort_func(arr.copy())
                assert result == sorted(arr)
        
        @given(st.lists(st.integers(min_value=0, max_value=10000)))
        def test_radix_sort_property(self, arr):
            """Test radix sort with non-negative integers."""
            result = radix_sort(arr.copy())
            assert result == sorted(arr)

except ImportError:
    # Hypothesis not available, skip property-based tests
    pass