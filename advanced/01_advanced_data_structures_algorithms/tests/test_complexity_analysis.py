"""
Test suite for Algorithm Complexity Analysis exercises.

This file contains comprehensive tests to verify the correctness
of the complexity analysis exercises and solutions.
"""

import unittest
import sys
import os
import time

# Add the parent directory to the path to import exercise modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from solutions.complexity_analysis_solutions import *
except ImportError:
    print("Solutions not found. Testing exercise structure only.")


class TestComplexityAnalysis(unittest.TestCase):
    """Test cases for complexity analysis exercises."""
    
    def setUp(self):
        """Set up test data."""
        self.small_array = [1, 2, 3, 4, 5]
        self.large_array = list(range(1000))
        self.duplicate_array = [1, 2, 3, 2, 4, 5, 3, 1]
        self.sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def test_find_duplicates_correctness(self):
        """Test that find_duplicates_fast returns correct results."""
        try:
            from solutions.complexity_analysis_solutions import find_duplicates_fast
            
            # Test with duplicates
            result = find_duplicates_fast(self.duplicate_array)
            expected_duplicates = {1, 2, 3}
            self.assertEqual(set(result), expected_duplicates)
            
            # Test with no duplicates
            result = find_duplicates_fast(self.small_array)
            self.assertEqual(len(result), 0)
            
            # Test empty array
            result = find_duplicates_fast([])
            self.assertEqual(len(result), 0)
            
        except ImportError:
            self.skipTest("find_duplicates_fast not implemented")
    
    def test_two_sum_correctness(self):
        """Test that two_sum_fast returns correct results."""
        try:
            from solutions.complexity_analysis_solutions import two_sum_fast
            
            # Test basic case
            arr = [2, 7, 11, 15]
            target = 9
            result = two_sum_fast(arr, target)
            self.assertIn(result, [(0, 1), (1, 0)])
            
            # Test no solution
            result = two_sum_fast(arr, 100)
            self.assertEqual(result, (-1, -1))
            
            # Test with negative numbers
            arr = [-1, -2, -3, -4, -5]
            target = -8
            result = two_sum_fast(arr, target)
            # -3 + -5 = -8, indices 2 and 4
            self.assertIn(result, [(2, 4), (4, 2)])
            
        except ImportError:
            self.skipTest("two_sum_fast not implemented")
    
    def test_fibonacci_implementations(self):
        """Test Fibonacci implementations for correctness."""
        expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        
        try:
            from solutions.complexity_analysis_solutions import fibonacci_memoized
            
            for i, expected in enumerate(expected_values):
                result = fibonacci_memoized(i)
                self.assertEqual(result, expected, f"fibonacci_memoized({i}) should be {expected}")
                
        except ImportError:
            self.skipTest("fibonacci_memoized not implemented")
        
        try:
            from solutions.complexity_analysis_solutions import fibonacci_iterative
            
            for i, expected in enumerate(expected_values):
                result = fibonacci_iterative(i)
                self.assertEqual(result, expected, f"fibonacci_iterative({i}) should be {expected}")
                
        except ImportError:
            self.skipTest("fibonacci_iterative not implemented")
    
    def test_kth_largest_correctness(self):
        """Test kth largest element algorithm."""
        try:
            from solutions.complexity_analysis_solutions import find_kth_largest_efficient
            
            arr = [3, 2, 1, 5, 6, 4]
            
            # Test various k values
            self.assertEqual(find_kth_largest_efficient(arr, 1), 6)  # 1st largest
            self.assertEqual(find_kth_largest_efficient(arr, 2), 5)  # 2nd largest
            self.assertEqual(find_kth_largest_efficient(arr, 3), 4)  # 3rd largest
            self.assertEqual(find_kth_largest_efficient(arr, 6), 1)  # 6th largest (smallest)
            
            # Test with duplicates
            arr_with_dups = [1, 2, 2, 3, 3, 4, 5, 5]
            self.assertEqual(find_kth_largest_efficient(arr_with_dups, 1), 5)
            self.assertEqual(find_kth_largest_efficient(arr_with_dups, 3), 5)  # Second 5
            
        except ImportError:
            self.skipTest("find_kth_largest_efficient not implemented")
    
    def test_cycle_detection(self):
        """Test cycle detection algorithm."""
        try:
            from solutions.complexity_analysis_solutions import has_cycle_efficient
            
            # Test with cycle: 0->1->2->0
            cycle_array = [1, 2, 0]
            self.assertTrue(has_cycle_efficient(cycle_array))
            
            # Test without cycle: 0->1->2 (out of bounds)
            no_cycle_array = [1, 2, 3]
            self.assertFalse(has_cycle_efficient(no_cycle_array))
            
            # Test single element pointing to itself
            self_cycle = [0]
            self.assertTrue(has_cycle_efficient(self_cycle))
            
            # Test empty array
            self.assertFalse(has_cycle_efficient([]))
            
        except ImportError:
            self.skipTest("has_cycle_efficient not implemented")
    
    def test_string_matching(self):
        """Test string matching algorithm."""
        try:
            from solutions.complexity_analysis_solutions import string_match_efficient
            
            # Test basic matching
            text = "ababcababa"
            pattern = "ababa"
            result = string_match_efficient(text, pattern)
            self.assertEqual(result, [5])  # Pattern starts at index 5
            
            # Test multiple matches
            text = "aaaa"
            pattern = "aa"
            result = string_match_efficient(text, pattern)
            self.assertEqual(result, [0, 1, 2])  # Overlapping matches
            
            # Test no matches
            text = "abcdef"
            pattern = "xyz"
            result = string_match_efficient(text, pattern)
            self.assertEqual(result, [])
            
            # Test empty pattern
            result = string_match_efficient("abc", "")
            self.assertEqual(result, [])
            
        except ImportError:
            self.skipTest("string_match_efficient not implemented")
    
    def test_performance_characteristics(self):
        """Test that optimized algorithms are actually faster."""
        # This test verifies that optimized versions perform better
        # than their naive counterparts on larger inputs
        
        try:
            from solutions.complexity_analysis_solutions import (
                find_duplicates_fast, fibonacci_memoized, fibonacci_iterative
            )
            
            # Test that memoized Fibonacci is much faster than naive
            def fibonacci_naive(n):
                if n <= 1:
                    return n
                return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
            
            # Test with a moderately large value
            n = 25
            
            # Time memoized version
            start_time = time.time()
            result_memo = fibonacci_memoized(n)
            memo_time = time.time() - start_time
            
            # Time iterative version
            start_time = time.time()
            result_iter = fibonacci_iterative(n)
            iter_time = time.time() - start_time
            
            # Both should give same result
            self.assertEqual(result_memo, result_iter)
            
            # Both should be much faster than naive (we won't test naive for n=25 as it's too slow)
            # Instead, we'll just verify they complete quickly
            self.assertLess(memo_time, 0.1, "Memoized Fibonacci should be fast")
            self.assertLess(iter_time, 0.1, "Iterative Fibonacci should be fast")
            
        except ImportError:
            self.skipTest("Optimized algorithms not implemented")


class TestComplexityAnalysisStructure(unittest.TestCase):
    """Test the structure and organization of the complexity analysis module."""
    
    def test_exercise_files_exist(self):
        """Test that all required files exist."""
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Check lesson file
        lesson_path = os.path.join(base_path, "lessons", "01_algorithm_complexity.md")
        self.assertTrue(os.path.exists(lesson_path), "Lesson file should exist")
        
        # Check exercise file
        exercise_path = os.path.join(base_path, "exercises", "01_complexity_analysis.py")
        self.assertTrue(os.path.exists(exercise_path), "Exercise file should exist")
        
        # Check solution file
        solution_path = os.path.join(base_path, "solutions", "01_complexity_analysis_solutions.py")
        self.assertTrue(os.path.exists(solution_path), "Solution file should exist")
    
    def test_lesson_content_structure(self):
        """Test that the lesson file has proper structure."""
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        lesson_path = os.path.join(base_path, "lessons", "01_algorithm_complexity.md")
        
        if os.path.exists(lesson_path):
            with open(lesson_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for key sections
            self.assertIn("# Algorithm Complexity Analysis", content)
            self.assertIn("Big O Notation", content)
            self.assertIn("O(1)", content)
            self.assertIn("O(n)", content)
            self.assertIn("O(n²)", content)
            self.assertIn("Space Complexity", content)
    
    def test_exercise_structure(self):
        """Test that exercise file has proper structure."""
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        exercise_path = os.path.join(base_path, "exercises", "01_complexity_analysis.py")
        
        if os.path.exists(exercise_path):
            with open(exercise_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for exercise functions
            self.assertIn("def exercise_1_analyze_complexity", content)
            self.assertIn("def exercise_2_optimize_algorithms", content)
            self.assertIn("def exercise_3_space_time_tradeoffs", content)
            self.assertIn("def exercise_4_complexity_comparison", content)
            self.assertIn("def exercise_5_design_challenge", content)
            
            # Check for TODO comments
            self.assertIn("# TODO:", content)


def run_performance_benchmarks():
    """Run performance benchmarks to demonstrate complexity differences."""
    print("\n" + "="*60)
    print("PERFORMANCE BENCHMARKS")
    print("="*60)
    
    try:
        from solutions.complexity_analysis_solutions import (
            compare_search_algorithms, demonstrate_complexity_differences
        )
        
        print("\n1. Search Algorithm Comparison:")
        compare_search_algorithms([1000, 10000, 50000])
        
        print("\n2. Fibonacci Complexity Demonstration:")
        demonstrate_complexity_differences()
        
    except ImportError:
        print("Performance benchmarks require solution implementations.")


if __name__ == "__main__":
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run performance benchmarks
    run_performance_benchmarks()