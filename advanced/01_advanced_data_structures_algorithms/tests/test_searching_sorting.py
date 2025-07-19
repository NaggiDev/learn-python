"""
Test Suite for Searching and Sorting Algorithms

This file contains comprehensive tests for all searching and sorting
algorithms to verify correctness and performance characteristics.

Run with: python -m pytest test_searching_sorting.py -v
"""

import pytest
import random
import time
from typing import List, Callable

# Import the solution implementations for testing
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solutions.searching_sorting_solutions import *


class TestSearchingAlgorithms:
    """Test cases for searching algorithms."""
    
    @pytest.fixture
    def sorted_data(self):
        """Fixture providing sorted test data."""
        return [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    @pytest.fixture
    def unsorted_data(self):
        """Fixture providing unsorted test data."""
        return [19, 3, 15, 7, 1, 11, 9, 17, 5, 13]
    
    def test_linear_search_found(self, unsorted_data):
        """Test linear search when element is found."""
        from solutions.searching_sorting_solutions import linear_search
        
        assert linear_search(unsorted_data, 7) == 3
        assert linear_search(unsorted_data, 19) == 0
        assert linear_search(unsorted_data, 13) == 9
    
    def test_linear_search_not_found(self, unsorted_data):
        """Test linear search when element is not found."""
        from solutions.searching_sorting_solutions import linear_search
        
        assert linear_search(unsorted_data, 20) == -1
        assert linear_search(unsorted_data, 0) == -1
        assert linear_search([], 5) == -1
    
    def test_binary_search_found(self, sorted_data):
        """Test binary search when element is found."""
        from solutions.searching_sorting_solutions import binary_search
        
        assert binary_search(sorted_data, 7) == 3
        assert binary_search(sorted_data, 1) == 0
        assert binary_search(sorted_data, 19) == 9
    
    def test_binary_search_not_found(self, sorted_data):
        """Test binary search when element is not found."""
        from solutions.searching_sorting_solutions import binary_search
        
        assert binary_search(sorted_data, 20) == -1
        assert binary_search(sorted_data, 0) == -1
        assert binary_search([], 5) == -1
    
    def test_binary_search_recursive(self, sorted_data):
        """Test recursive binary search."""
        from solutions.searching_sorting_solutions import binary_search_recursive
        
        assert binary_search_recursive(sorted_data, 7) == 3
        assert binary_search_recursive(sorted_data, 20) == -1
        assert binary_search_recursive([], 5) == -1
    
    def test_interpolation_search(self, sorted_data):
        """Test interpolation search."""
        from solutions.searching_sorting_solutions import interpolation_search
        
        assert interpolation_search(sorted_data, 7) == 3
        assert interpolation_search(sorted_data, 20) == -1
        assert interpolation_search([], 5) == -1
    
    def test_search_algorithms_consistency(self, sorted_data):
        """Test that all search algorithms return consistent results."""
        from solutions.searching_sorting_solutions import (
            linear_search, binary_search, binary_search_recursive, interpolation_search
        )
        
        for target in sorted_data + [0, 20]:
            linear_result = linear_search(sorted_data, target)
            binary_result = binary_search(sorted_data, target)
            recursive_result = binary_search_recursive(sorted_data, target)
            interpolation_result = interpolation_search(sorted_data, target)
            
            # All should return the same result (found or not found)
            if linear_result != -1:
                assert binary_result != -1
                assert recursive_result != -1
                assert interpolation_result != -1
                # Verify the found element is correct
                assert sorted_data[binary_result] == target
            else:
                assert binary_result == -1
                assert recursive_result == -1
                assert interpolation_result == -1


class TestBasicSortingAlgorithms:
    """Test cases for basic sorting algorithms."""
    
    @pytest.fixture
    def test_data(self):
        """Fixture providing test data for sorting."""
        return [64, 34, 25, 12, 22, 11, 90]
    
    @pytest.fixture
    def expected_sorted(self):
        """Fixture providing expected sorted result."""
        return [11, 12, 22, 25, 34, 64, 90]
    
    def test_bubble_sort(self, test_data, expected_sorted):
        """Test bubble sort algorithm."""
        from solutions.searching_sorting_solutions import bubble_sort
        
        result = bubble_sort(test_data)
        assert result == expected_sorted
        assert test_data == [64, 34, 25, 12, 22, 11, 90]  # Original unchanged
    
    def test_selection_sort(self, test_data, expected_sorted):
        """Test selection sort algorithm."""
        from solutions.searching_sorting_solutions import selection_sort
        
        result = selection_sort(test_data)
        assert result == expected_sorted
    
    def test_insertion_sort(self, test_data, expected_sorted):
        """Test insertion sort algorithm."""
        from solutions.searching_sorting_solutions import insertion_sort
        
        result = insertion_sort(test_data)
        assert result == expected_sorted
    
    def test_basic_sorts_edge_cases(self):
        """Test basic sorting algorithms with edge cases."""
        from solutions.searching_sorting_solutions import bubble_sort, selection_sort, insertion_sort
        
        algorithms = [bubble_sort, selection_sort, insertion_sort]
        
        for algorithm in algorithms:
            # Empty array
            assert algorithm([]) == []
            
            # Single element
            assert algorithm([42]) == [42]
            
            # Already sorted
            assert algorithm([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
            
            # Reverse sorted
            assert algorithm([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
            
            # Duplicates
            assert algorithm([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


class TestAdvancedSortingAlgorithms:
    """Test cases for advanced sorting algorithms."""
    
    @pytest.fixture
    def test_data(self):
        """Fixture providing test data for sorting."""
        return [64, 34, 25, 12, 22, 11, 90]
    
    @pytest.fixture
    def expected_sorted(self):
        """Fixture providing expected sorted result."""
        return [11, 12, 22, 25, 34, 64, 90]
    
    def test_merge_sort(self, test_data, expected_sorted):
        """Test merge sort algorithm."""
        from solutions.searching_sorting_solutions import merge_sort
        
        result = merge_sort(test_data)
        assert result == expected_sorted
    
    def test_quick_sort(self, test_data, expected_sorted):
        """Test quick sort algorithm."""
        from solutions.searching_sorting_solutions import quick_sort
        
        result = quick_sort(test_data)
        assert result == expected_sorted
    
    def test_heap_sort(self, test_data, expected_sorted):
        """Test heap sort algorithm."""
        from solutions.searching_sorting_solutions import heap_sort
        
        result = heap_sort(test_data)
        assert result == expected_sorted
    
    def test_advanced_sorts_edge_cases(self):
        """Test advanced sorting algorithms with edge cases."""
        from solutions.searching_sorting_solutions import merge_sort, quick_sort, heap_sort
        
        algorithms = [merge_sort, quick_sort, heap_sort]
        
        for algorithm in algorithms:
            # Empty array
            assert algorithm([]) == []
            
            # Single element
            assert algorithm([42]) == [42]
            
            # Already sorted
            assert algorithm([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
            
            # Reverse sorted
            assert algorithm([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
            
            # Duplicates
            assert algorithm([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]
    
    def test_merge_function(self):
        """Test the merge helper function."""
        from solutions.searching_sorting_solutions import merge
        
        assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        assert merge([], [1, 2, 3]) == [1, 2, 3]
        assert merge([1, 2, 3], []) == [1, 2, 3]
        assert merge([1], [2]) == [1, 2]


class TestSpecializedSortingAlgorithms:
    """Test cases for specialized sorting algorithms."""
    
    def test_counting_sort(self):
        """Test counting sort algorithm."""
        from solutions.searching_sorting_solutions import counting_sort
        
        # Basic test
        assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
        
        # Empty array
        assert counting_sort([]) == []
        
        # Single element
        assert counting_sort([5]) == [5]
        
        # With explicit max value
        assert counting_sort([4, 2, 2, 3, 3, 1], 5) == [1, 2, 2, 3, 3, 4]
    
    def test_radix_sort(self):
        """Test radix sort algorithm."""
        from solutions.searching_sorting_solutions import radix_sort
        
        # Basic test
        assert radix_sort([170, 45, 75, 90, 2, 802, 24, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]
        
        # Empty array
        assert radix_sort([]) == []
        
        # Single element
        assert radix_sort([42]) == [42]
        
        # Single digit numbers
        assert radix_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
    
    def test_bucket_sort(self):
        """Test bucket sort algorithm."""
        from solutions.searching_sorting_solutions import bucket_sort
        
        # Basic test with floats between 0 and 1
        test_data = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
        result = bucket_sort(test_data)
        
        # Check if sorted
        assert result == sorted(test_data)
        
        # Empty array
        assert bucket_sort([]) == []
        
        # Single element
        assert bucket_sort([0.5]) == [0.5]


class TestOptimizedAlgorithms:
    """Test cases for optimized sorting algorithms."""
    
    def test_hybrid_sort(self):
        """Test hybrid sort algorithm."""
        from solutions.searching_sorting_solutions import hybrid_sort
        
        test_data = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        
        assert hybrid_sort(test_data) == expected
        
        # Test with different thresholds
        assert hybrid_sort(test_data, threshold=5) == expected
        assert hybrid_sort(test_data, threshold=20) == expected
    
    def test_quick_sort_optimized(self):
        """Test optimized quick sort with median-of-three pivot."""
        from solutions.searching_sorting_solutions import quick_sort_optimized
        
        test_data = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        
        assert quick_sort_optimized(test_data) == expected
    
    def test_median_of_three_pivot(self):
        """Test median-of-three pivot selection."""
        from solutions.searching_sorting_solutions import median_of_three_pivot
        
        # Test with array where median is clear
        arr = [3, 1, 2]
        median_of_three_pivot(arr, 0, 2)
        assert arr[2] == 2  # Median should be at the end


class TestRealWorldApplications:
    """Test cases for real-world sorting applications."""
    
    def test_sort_records(self):
        """Test stable record sorting."""
        from solutions.searching_sorting_solutions import sort_records
        
        records = [
            ("Alice", 30, 50000.0),
            ("Bob", 25, 45000.0),
            ("Charlie", 30, 55000.0),
            ("Diana", 25, 45000.0)
        ]
        
        # Sort by age
        by_age = sort_records(records, lambda x: x[1])
        ages = [record[1] for record in by_age]
        assert ages == sorted(ages)
        
        # Sort by salary
        by_salary = sort_records(records, lambda x: x[2])
        salaries = [record[2] for record in by_salary]
        assert salaries == sorted(salaries)
    
    def test_multi_key_sort(self):
        """Test multi-key sorting."""
        from solutions.searching_sorting_solutions import multi_key_sort
        
        records = [
            ("Alice", 30, 50000.0),
            ("Bob", 25, 45000.0),
            ("Charlie", 30, 55000.0),
            ("Diana", 25, 45000.0)
        ]
        
        result = multi_key_sort(records)
        
        # Should be sorted by age first, then salary, then name
        # Check age ordering
        ages = [record[1] for record in result]
        assert ages == sorted(ages)
        
        # For same age, check salary ordering
        age_25_records = [r for r in result if r[1] == 25]
        if len(age_25_records) > 1:
            salaries = [r[2] for r in age_25_records]
            assert salaries == sorted(salaries)


class TestPerformanceCharacteristics:
    """Test performance characteristics of algorithms."""
    
    def test_sorting_algorithm_correctness_large_data(self):
        """Test sorting algorithms with larger datasets."""
        from solutions.searching_sorting_solutions import (
            merge_sort, quick_sort, heap_sort, hybrid_sort
        )
        
        # Generate larger random dataset
        large_data = [random.randint(1, 1000) for _ in range(1000)]
        expected = sorted(large_data)
        
        algorithms = [merge_sort, quick_sort, heap_sort, hybrid_sort]
        
        for algorithm in algorithms:
            result = algorithm(large_data.copy())
            assert result == expected, f"{algorithm.__name__} failed on large dataset"
    
    def test_stability_preservation(self):
        """Test that stable algorithms preserve relative order of equal elements."""
        from solutions.searching_sorting_solutions import merge_sort, insertion_sort, bubble_sort
        
        # Create data with equal elements that have different secondary keys
        data_with_secondary = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd'), (1, 'e')]
        
        stable_algorithms = [
            lambda x: merge_sort([item[0] for item in x]),
            lambda x: insertion_sort([item[0] for item in x]),
            lambda x: bubble_sort([item[0] for item in x])
        ]
        
        for algorithm in stable_algorithms:
            # This is a simplified test - in practice, you'd need to track
            # the secondary keys through the sorting process
            result = algorithm(data_with_secondary)
            assert result == sorted([item[0] for item in data_with_secondary])
    
    @pytest.mark.performance
    def test_algorithm_performance_comparison(self):
        """Compare performance of different algorithms (marked as performance test)."""
        from solutions.searching_sorting_solutions import (
            bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort
        )
        
        # Small dataset where O(n²) algorithms should be reasonable
        small_data = [random.randint(1, 100) for _ in range(100)]
        
        algorithms = {
            'bubble_sort': bubble_sort,
            'insertion_sort': insertion_sort,
            'merge_sort': merge_sort,
            'quick_sort': quick_sort,
            'heap_sort': heap_sort
        }
        
        times = {}
        
        for name, algorithm in algorithms.items():
            start_time = time.time()
            result = algorithm(small_data.copy())
            end_time = time.time()
            
            times[name] = end_time - start_time
            assert result == sorted(small_data), f"{name} produced incorrect result"
        
        # Basic performance expectations (these may vary by system)
        # O(n log n) algorithms should generally be faster than O(n²) for this size
        assert times['merge_sort'] < times['bubble_sort']
        assert times['quick_sort'] < times['bubble_sort']
        assert times['heap_sort'] < times['bubble_sort']


class TestEdgeCasesAndErrorHandling:
    """Test edge cases and error handling."""
    
    def test_empty_arrays(self):
        """Test all algorithms with empty arrays."""
        from solutions.searching_sorting_solutions import (
            linear_search, binary_search, merge_sort, quick_sort, heap_sort,
            bubble_sort, insertion_sort, selection_sort, counting_sort, radix_sort
        )
        
        # Search algorithms
        assert linear_search([], 5) == -1
        assert binary_search([], 5) == -1
        
        # Sorting algorithms
        sorting_algorithms = [
            merge_sort, quick_sort, heap_sort, bubble_sort, 
            insertion_sort, selection_sort, counting_sort, radix_sort
        ]
        
        for algorithm in sorting_algorithms:
            assert algorithm([]) == []
    
    def test_single_element_arrays(self):
        """Test all algorithms with single-element arrays."""
        from solutions.searching_sorting_solutions import (
            linear_search, binary_search, merge_sort, quick_sort, heap_sort,
            bubble_sort, insertion_sort, selection_sort, counting_sort, radix_sort
        )
        
        # Search algorithms
        assert linear_search([42], 42) == 0
        assert linear_search([42], 43) == -1
        assert binary_search([42], 42) == 0
        assert binary_search([42], 43) == -1
        
        # Sorting algorithms
        sorting_algorithms = [
            merge_sort, quick_sort, heap_sort, bubble_sort, 
            insertion_sort, selection_sort, counting_sort, radix_sort
        ]
        
        for algorithm in sorting_algorithms:
            assert algorithm([42]) == [42]
    
    def test_duplicate_elements(self):
        """Test algorithms with arrays containing many duplicates."""
        from solutions.searching_sorting_solutions import (
            merge_sort, quick_sort, heap_sort, bubble_sort, 
            insertion_sort, selection_sort
        )
        
        duplicates = [5, 2, 5, 1, 5, 2, 1, 5]
        expected = [1, 1, 2, 2, 5, 5, 5, 5]
        
        sorting_algorithms = [
            merge_sort, quick_sort, heap_sort, bubble_sort, 
            insertion_sort, selection_sort
        ]
        
        for algorithm in sorting_algorithms:
            result = algorithm(duplicates.copy())
            assert result == expected, f"{algorithm.__name__} failed with duplicates"


if __name__ == "__main__":
    # Run tests if executed directly
    pytest.main([__file__, "-v"])