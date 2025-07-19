"""
Sorting Algorithms Demonstration

This script demonstrates the usage of various sorting algorithms
and compares their performance on different types of input data.
"""

import random
import time
from typing import List, Callable
from algorithms.sorting import (
    quick_sort, quick_sort_optimized,
    merge_sort, merge_sort_iterative,
    heap_sort, radix_sort
)
from algorithms.utils import ComplexityAnalyzer


def generate_random_array(size: int) -> List[int]:
    """Generate a random array of given size."""
    return [random.randint(1, 1000) for _ in range(size)]


def generate_sorted_array(size: int) -> List[int]:
    """Generate a sorted array of given size."""
    return list(range(1, size + 1))


def generate_reverse_sorted_array(size: int) -> List[int]:
    """Generate a reverse sorted array of given size."""
    return list(range(size, 0, -1))


def generate_nearly_sorted_array(size: int, swaps: int = 10) -> List[int]:
    """Generate a nearly sorted array with a few random swaps."""
    arr = list(range(1, size + 1))
    for _ in range(swaps):
        i, j = random.randint(0, size - 1), random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def demonstrate_sorting_algorithms():
    """Demonstrate all sorting algorithms with sample data."""
    print("=== Sorting Algorithms Demonstration ===\n")
    
    # Sample data
    sample_data = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"Original array: {sample_data}")
    print()
    
    # Test each sorting algorithm
    algorithms = [
        ("Quick Sort", quick_sort),
        ("Quick Sort (Optimized)", quick_sort_optimized),
        ("Merge Sort", merge_sort),
        ("Merge Sort (Iterative)", merge_sort_iterative),
        ("Heap Sort", heap_sort),
        ("Radix Sort", radix_sort),
    ]
    
    for name, algorithm in algorithms:
        try:
            start_time = time.perf_counter()
            result = algorithm(sample_data.copy())
            end_time = time.perf_counter()
            
            print(f"{name}:")
            print(f"  Result: {result}")
            print(f"  Time: {(end_time - start_time) * 1000:.3f} ms")
            print(f"  Correct: {result == sorted(sample_data)}")
            print()
        except Exception as e:
            print(f"{name}: Error - {e}")
            print()


def performance_comparison():
    """Compare performance of sorting algorithms on different input types."""
    print("=== Performance Comparison ===\n")
    
    sizes = [100, 500, 1000, 2000]
    input_types = [
        ("Random", generate_random_array),
        ("Sorted", generate_sorted_array),
        ("Reverse Sorted", generate_reverse_sorted_array),
        ("Nearly Sorted", generate_nearly_sorted_array),
    ]
    
    algorithms = [
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort),
        ("Heap Sort", heap_sort),
    ]
    
    for input_name, input_generator in input_types:
        print(f"\n{input_name} Input:")
        print("-" * 50)
        
        for size in sizes:
            print(f"\nSize: {size}")
            test_data = input_generator(size)
            
            for alg_name, algorithm in algorithms:
                try:
                    # Measure time over multiple runs
                    times = []
                    for _ in range(3):
                        start_time = time.perf_counter()
                        algorithm(test_data.copy())
                        end_time = time.perf_counter()
                        times.append(end_time - start_time)
                    
                    avg_time = sum(times) / len(times)
                    print(f"  {alg_name}: {avg_time * 1000:.2f} ms")
                    
                except Exception as e:
                    print(f"  {alg_name}: Error - {e}")


def complexity_analysis_demo():
    """Demonstrate complexity analysis using the ComplexityAnalyzer."""
    print("\n=== Complexity Analysis Demo ===\n")
    
    # TODO: Uncomment when ComplexityAnalyzer is implemented
    # analyzer = ComplexityAnalyzer()
    # 
    # # Analyze quick sort
    # print("Analyzing Quick Sort complexity...")
    # analyzer.analyze_time_complexity(
    #     quick_sort, 
    #     generate_random_array, 
    #     [100, 200, 500, 1000, 2000],
    #     "Quick Sort"
    # )
    # 
    # # Compare multiple algorithms
    # print("Comparing sorting algorithms...")
    # algorithms = {
    #     "Quick Sort": quick_sort,
    #     "Merge Sort": merge_sort,
    #     "Heap Sort": heap_sort,
    # }
    # analyzer.compare_algorithms(algorithms, generate_random_array, [100, 500, 1000])
    # 
    # # Generate plots
    # analyzer.plot_time_complexity(
    #     theoretical_complexities={
    #         "Quick Sort": "O(n log n)",
    #         "Merge Sort": "O(n log n)",
    #         "Heap Sort": "O(n log n)",
    #     }
    # )
    
    print("Complexity analysis requires implementation of ComplexityAnalyzer")


def edge_cases_demo():
    """Demonstrate sorting algorithms on edge cases."""
    print("\n=== Edge Cases Demonstration ===\n")
    
    edge_cases = [
        ("Empty array", []),
        ("Single element", [42]),
        ("Two elements (sorted)", [1, 2]),
        ("Two elements (reverse)", [2, 1]),
        ("All identical", [5, 5, 5, 5, 5]),
        ("Large numbers", [1000000, 999999, 1000001, 500000]),
    ]
    
    for case_name, test_data in edge_cases:
        print(f"{case_name}: {test_data}")
        
        try:
            result = quick_sort(test_data.copy())
            expected = sorted(test_data)
            print(f"  Result: {result}")
            print(f"  Correct: {result == expected}")
        except Exception as e:
            print(f"  Error: {e}")
        print()


def main():
    """Main function to run all demonstrations."""
    print("Algorithm Implementation Challenge - Sorting Demo")
    print("=" * 60)
    
    demonstrate_sorting_algorithms()
    performance_comparison()
    complexity_analysis_demo()
    edge_cases_demo()
    
    print("\nDemo completed! Try implementing the algorithms to see them in action.")


if __name__ == "__main__":
    main()