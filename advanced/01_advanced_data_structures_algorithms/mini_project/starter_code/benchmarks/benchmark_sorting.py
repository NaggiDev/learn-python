"""
Sorting Algorithms Benchmarking

This script provides comprehensive benchmarking of sorting algorithms
with detailed performance analysis and reporting.
"""

import time
import random
import statistics
import csv
from typing import List, Dict, Callable, Tuple
from dataclasses import dataclass
from algorithms.sorting import (
    quick_sort, quick_sort_optimized,
    merge_sort, merge_sort_iterative,
    heap_sort, radix_sort
)


@dataclass
class BenchmarkResult:
    """Data class to store benchmark results."""
    algorithm_name: str
    input_type: str
    input_size: int
    avg_time: float
    min_time: float
    max_time: float
    std_dev: float
    iterations: int


class SortingBenchmark:
    """Comprehensive benchmarking suite for sorting algorithms."""
    
    def __init__(self):
        """Initialize the benchmark suite."""
        self.results: List[BenchmarkResult] = []
        self.algorithms = {
            "Quick Sort": quick_sort,
            "Quick Sort (Optimized)": quick_sort_optimized,
            "Merge Sort": merge_sort,
            "Merge Sort (Iterative)": merge_sort_iterative,
            "Heap Sort": heap_sort,
        }
        self.integer_algorithms = {
            "Radix Sort": radix_sort,
        }
    
    def generate_test_data(self, size: int, data_type: str) -> List[int]:
        """
        Generate test data of specified type and size.
        
        Args:
            size: Size of the array to generate
            data_type: Type of data ('random', 'sorted', 'reverse', 'nearly_sorted', 'duplicates')
            
        Returns:
            Generated test array
        """
        if data_type == "random":
            return [random.randint(1, size * 10) for _ in range(size)]
        elif data_type == "sorted":
            return list(range(1, size + 1))
        elif data_type == "reverse":
            return list(range(size, 0, -1))
        elif data_type == "nearly_sorted":
            arr = list(range(1, size + 1))
            # Make 5% of elements out of order
            swaps = max(1, size // 20)
            for _ in range(swaps):
                i, j = random.randint(0, size - 1), random.randint(0, size - 1)
                arr[i], arr[j] = arr[j], arr[i]
            return arr
        elif data_type == "duplicates":
            # Array with many duplicate values
            unique_values = max(1, size // 10)
            return [random.randint(1, unique_values) for _ in range(size)]
        else:
            raise ValueError(f"Unknown data type: {data_type}")
    
    def benchmark_algorithm(self, algorithm: Callable, test_data: List[int], 
                          iterations: int = 5) -> Tuple[float, float, float, float]:
        """
        Benchmark a single algorithm on given test data.
        
        Args:
            algorithm: Sorting algorithm to benchmark
            test_data: Test data to sort
            iterations: Number of iterations to run
            
        Returns:
            Tuple of (avg_time, min_time, max_time, std_dev)
        """
        times = []
        
        for _ in range(iterations):
            data_copy = test_data.copy()
            start_time = time.perf_counter()
            
            try:
                result = algorithm(data_copy)
                end_time = time.perf_counter()
                
                # Verify correctness
                if result != sorted(test_data):
                    raise ValueError("Algorithm produced incorrect result")
                
                times.append(end_time - start_time)
                
            except Exception as e:
                print(f"Error in {algorithm.__name__}: {e}")
                return float('inf'), float('inf'), float('inf'), float('inf')
        
        if not times:
            return float('inf'), float('inf'), float('inf'), float('inf')
        
        avg_time = statistics.mean(times)
        min_time = min(times)
        max_time = max(times)
        std_dev = statistics.stdev(times) if len(times) > 1 else 0.0
        
        return avg_time, min_time, max_time, std_dev
    
    def run_comprehensive_benchmark(self, sizes: List[int] = None, 
                                  data_types: List[str] = None,
                                  iterations: int = 5) -> None:
        """
        Run comprehensive benchmark across multiple algorithms, sizes, and data types.
        
        Args:
            sizes: List of input sizes to test
            data_types: List of data types to test
            iterations: Number of iterations per test
        """
        if sizes is None:
            sizes = [100, 500, 1000, 2000, 5000]
        
        if data_types is None:
            data_types = ["random", "sorted", "reverse", "nearly_sorted", "duplicates"]
        
        print("Running comprehensive sorting algorithm benchmark...")
        print(f"Sizes: {sizes}")
        print(f"Data types: {data_types}")
        print(f"Iterations per test: {iterations}")
        print("-" * 60)
        
        total_tests = len(self.algorithms) * len(sizes) * len(data_types)
        current_test = 0
        
        # Test general sorting algorithms
        for alg_name, algorithm in self.algorithms.items():
            for size in sizes:
                for data_type in data_types:
                    current_test += 1
                    print(f"Progress: {current_test}/{total_tests} - {alg_name} on {data_type} data (size {size})")
                    
                    test_data = self.generate_test_data(size, data_type)
                    avg_time, min_time, max_time, std_dev = self.benchmark_algorithm(
                        algorithm, test_data, iterations
                    )
                    
                    result = BenchmarkResult(
                        algorithm_name=alg_name,
                        input_type=data_type,
                        input_size=size,
                        avg_time=avg_time,
                        min_time=min_time,
                        max_time=max_time,
                        std_dev=std_dev,
                        iterations=iterations
                    )
                    self.results.append(result)
        
        # Test integer-specific algorithms (radix sort)
        for alg_name, algorithm in self.integer_algorithms.items():
            for size in sizes:
                for data_type in data_types:
                    current_test += 1
                    print(f"Progress: {current_test}/{total_tests} - {alg_name} on {data_type} data (size {size})")
                    
                    # Generate non-negative integers for radix sort
                    if data_type == "random":
                        test_data = [random.randint(0, size * 10) for _ in range(size)]
                    else:
                        test_data = self.generate_test_data(size, data_type)
                        # Ensure non-negative
                        test_data = [max(0, x) for x in test_data]
                    
                    avg_time, min_time, max_time, std_dev = self.benchmark_algorithm(
                        algorithm, test_data, iterations
                    )
                    
                    result = BenchmarkResult(
                        algorithm_name=alg_name,
                        input_type=data_type,
                        input_size=size,
                        avg_time=avg_time,
                        min_time=min_time,
                        max_time=max_time,
                        std_dev=std_dev,
                        iterations=iterations
                    )
                    self.results.append(result)
        
        print("\nBenchmark completed!")
    
    def generate_report(self) -> str:
        """
        Generate a comprehensive benchmark report.
        
        Returns:
            Formatted report string
        """
        if not self.results:
            return "No benchmark results available."
        
        report = []
        report.append("SORTING ALGORITHMS BENCHMARK REPORT")
        report.append("=" * 50)
        report.append("")
        
        # Summary statistics
        report.append("SUMMARY")
        report.append("-" * 20)
        
        algorithms = set(r.algorithm_name for r in self.results)
        input_types = set(r.input_type for r in self.results)
        sizes = sorted(set(r.input_size for r in self.results))
        
        report.append(f"Algorithms tested: {len(algorithms)}")
        report.append(f"Input types: {len(input_types)}")
        report.append(f"Input sizes: {sizes}")
        report.append(f"Total tests: {len(self.results)}")
        report.append("")
        
        # Performance by algorithm
        report.append("PERFORMANCE BY ALGORITHM")
        report.append("-" * 30)
        
        for algorithm in sorted(algorithms):
            alg_results = [r for r in self.results if r.algorithm_name == algorithm]
            avg_times = [r.avg_time for r in alg_results if r.avg_time != float('inf')]
            
            if avg_times:
                report.append(f"{algorithm}:")
                report.append(f"  Average time: {statistics.mean(avg_times):.6f}s")
                report.append(f"  Best time: {min(avg_times):.6f}s")
                report.append(f"  Worst time: {max(avg_times):.6f}s")
                report.append("")
        
        # Performance by input type
        report.append("PERFORMANCE BY INPUT TYPE")
        report.append("-" * 30)
        
        for input_type in sorted(input_types):
            type_results = [r for r in self.results if r.input_type == input_type]
            report.append(f"{input_type.title()} Input:")
            
            for algorithm in sorted(algorithms):
                alg_type_results = [r for r in type_results if r.algorithm_name == algorithm]
                if alg_type_results:
                    avg_times = [r.avg_time for r in alg_type_results if r.avg_time != float('inf')]
                    if avg_times:
                        report.append(f"  {algorithm}: {statistics.mean(avg_times):.6f}s avg")
            report.append("")
        
        # Detailed results table
        report.append("DETAILED RESULTS")
        report.append("-" * 20)
        report.append(f"{'Algorithm':<20} {'Input Type':<15} {'Size':<8} {'Avg Time (s)':<12} {'Std Dev':<10}")
        report.append("-" * 75)
        
        for result in sorted(self.results, key=lambda x: (x.algorithm_name, x.input_type, x.input_size)):
            if result.avg_time != float('inf'):
                report.append(f"{result.algorithm_name:<20} {result.input_type:<15} "
                            f"{result.input_size:<8} {result.avg_time:<12.6f} {result.std_dev:<10.6f}")
        
        return "\n".join(report)
    
    def save_results_csv(self, filename: str) -> None:
        """
        Save benchmark results to CSV file.
        
        Args:
            filename: Output CSV filename
        """
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['algorithm_name', 'input_type', 'input_size', 'avg_time', 
                         'min_time', 'max_time', 'std_dev', 'iterations']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for result in self.results:
                writer.writerow({
                    'algorithm_name': result.algorithm_name,
                    'input_type': result.input_type,
                    'input_size': result.input_size,
                    'avg_time': result.avg_time,
                    'min_time': result.min_time,
                    'max_time': result.max_time,
                    'std_dev': result.std_dev,
                    'iterations': result.iterations
                })
        
        print(f"Results saved to {filename}")
    
    def find_best_algorithm(self, input_type: str = None, size: int = None) -> Dict[str, str]:
        """
        Find the best performing algorithm for given conditions.
        
        Args:
            input_type: Specific input type to consider (None for all)
            size: Specific size to consider (None for all)
            
        Returns:
            Dictionary with best algorithm information
        """
        filtered_results = self.results
        
        if input_type:
            filtered_results = [r for r in filtered_results if r.input_type == input_type]
        
        if size:
            filtered_results = [r for r in filtered_results if r.input_size == size]
        
        if not filtered_results:
            return {"error": "No results match the criteria"}
        
        # Find algorithm with best average time
        valid_results = [r for r in filtered_results if r.avg_time != float('inf')]
        if not valid_results:
            return {"error": "No valid results found"}
        
        best_result = min(valid_results, key=lambda x: x.avg_time)
        
        return {
            "algorithm": best_result.algorithm_name,
            "avg_time": best_result.avg_time,
            "input_type": best_result.input_type,
            "input_size": best_result.input_size
        }


def main():
    """Main function to run the benchmark."""
    print("Sorting Algorithms Benchmark Suite")
    print("=" * 40)
    
    benchmark = SortingBenchmark()
    
    # Run benchmark with smaller sizes for demo
    benchmark.run_comprehensive_benchmark(
        sizes=[100, 500, 1000],
        data_types=["random", "sorted", "reverse"],
        iterations=3
    )
    
    # Generate and display report
    report = benchmark.generate_report()
    print("\n" + report)
    
    # Save results
    benchmark.save_results_csv("sorting_benchmark_results.csv")
    
    # Find best algorithms
    print("\nBEST ALGORITHMS:")
    print("-" * 20)
    
    for input_type in ["random", "sorted", "reverse"]:
        best = benchmark.find_best_algorithm(input_type=input_type)
        if "error" not in best:
            print(f"{input_type.title()} input: {best['algorithm']} ({best['avg_time']:.6f}s)")


if __name__ == "__main__":
    main()