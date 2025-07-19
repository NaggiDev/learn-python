"""
Exercise 6: Process Pools and Advanced Multiprocessing

Learn to use ProcessPoolExecutor and multiprocessing.Pool for efficient parallel processing.

Instructions:
1. Complete the functions below to work with process pools
2. Implement map-reduce patterns and advanced multiprocessing techniques
3. Compare different approaches to parallel processing
"""

import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import math
import random
from functools import reduce
import operator


def cpu_bound_task(n):
    """CPU-intensive task for testing"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = [i for i in range(2, n) if is_prime(i)]
    return len(primes)


def calculate_factorial(n):
    """
    TODO: Implement factorial calculation
    Return the factorial of n
    """
    # Your code here
    pass


def calculate_fibonacci(n):
    """
    TODO: Implement Fibonacci calculation
    Return the nth Fibonacci number
    """
    # Your code here
    pass


def matrix_multiply_row(args):
    """
    TODO: Multiply a row of matrix A with matrix B
    args is a tuple: (row_index, row_data, matrix_b)
    Return (row_index, result_row)
    """
    # Your code here
    pass


def demonstrate_process_pool_executor():
    """Demonstrate ProcessPoolExecutor for CPU-bound tasks"""
    print("=== ProcessPoolExecutor Demo ===")
    
    numbers = [10000, 15000, 20000, 25000, 30000]
    
    # Sequential execution
    print("Sequential execution:")
    start_time = time.time()
    
    # TODO: Calculate cpu_bound_task for each number sequentially
    # Store and print results
    
    # Your code here
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Parallel execution with ProcessPoolExecutor
    print("\nParallel execution with ProcessPoolExecutor:")
    start_time = time.time()
    
    # TODO: Use ProcessPoolExecutor with max_workers=4
    # Submit all tasks and collect results
    # Print results as they complete using as_completed()
    
    # Your code here
    
    parallel_time = time.time() - start_time
    print(f"Parallel time: {parallel_time:.2f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")


def demonstrate_multiprocessing_pool():
    """Demonstrate multiprocessing.Pool methods"""
    print("\n=== Multiprocessing Pool Demo ===")
    
    # Test data
    numbers = list(range(1, 16))  # 1 to 15
    
    # TODO: Use multiprocessing.Pool with 4 processes
    # Demonstrate different Pool methods:
    
    # 1. pool.map() with calculate_factorial
    print("Using pool.map() for factorials:")
    # Your code here
    
    # 2. pool.map() with calculate_fibonacci  
    print("\nUsing pool.map() for Fibonacci:")
    # Your code here
    
    # 3. pool.starmap() for functions with multiple arguments
    print("\nUsing pool.starmap() for power calculations:")
    def power(base, exponent):
        return base ** exponent
    
    power_args = [(2, 3), (3, 4), (4, 2), (5, 3), (6, 2)]
    # TODO: Use pool.starmap() with power function and power_args
    # Your code here


def demonstrate_map_reduce():
    """Demonstrate map-reduce pattern with multiprocessing"""
    print("\n=== Map-Reduce Demo ===")
    
    def map_word_count(text_chunk):
        """
        TODO: Map function for word counting
        Count words in a chunk of text
        Return a dictionary of word counts
        """
        # Your code here
        pass
    
    def reduce_word_counts(count1, count2):
        """
        TODO: Reduce function for combining word counts
        Combine two word count dictionaries
        Return the merged dictionary
        """
        # Your code here
        pass
    
    # Sample text data
    text_data = [
        "hello world python programming",
        "python is great for programming",
        "multiprocessing enables parallel programming",
        "hello python world of programming",
        "parallel processing with python multiprocessing"
    ] * 1000  # Make it larger
    
    # Split into chunks for parallel processing
    num_processes = 4
    chunk_size = len(text_data) // num_processes
    chunks = [
        text_data[i:i + chunk_size] 
        for i in range(0, len(text_data), chunk_size)
    ]
    
    # TODO: Implement map-reduce pattern:
    # 1. Use multiprocessing.Pool to map word counting across chunks
    # 2. Use reduce() to combine the results
    # 3. Compare with sequential word counting
    
    # Sequential approach
    start_time = time.time()
    # Your code here for sequential word counting
    sequential_time = time.time() - start_time
    
    # Parallel map-reduce approach
    start_time = time.time()
    # Your code here for parallel map-reduce
    parallel_time = time.time() - start_time
    
    print(f"Sequential time: {sequential_time:.4f} seconds")
    print(f"Parallel time: {parallel_time:.4f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")


def demonstrate_matrix_multiplication():
    """Demonstrate parallel matrix multiplication"""
    print("\n=== Parallel Matrix Multiplication Demo ===")
    
    def create_random_matrix(rows, cols):
        """Create a random matrix"""
        return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    
    def sequential_matrix_multiply(A, B):
        """Sequential matrix multiplication"""
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])
        
        if cols_A != rows_B:
            raise ValueError("Matrix dimensions don't match")
        
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        
        return result
    
    def parallel_matrix_multiply(A, B):
        """
        TODO: Implement parallel matrix multiplication
        1. Use multiprocessing.Pool to process rows in parallel
        2. Each process handles one row of the result matrix
        3. Use the matrix_multiply_row function
        4. Combine results to form the final matrix
        """
        # Your code here
        pass
    
    # Create test matrices
    size = 100  # 100x100 matrices
    print(f"Creating {size}x{size} random matrices...")
    
    A = create_random_matrix(size, size)
    B = create_random_matrix(size, size)
    
    # Sequential multiplication
    print("Sequential matrix multiplication:")
    start_time = time.time()
    result_sequential = sequential_matrix_multiply(A, B)
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Parallel multiplication
    print("Parallel matrix multiplication:")
    start_time = time.time()
    result_parallel = parallel_matrix_multiply(A, B)
    parallel_time = time.time() - start_time
    print(f"Parallel time: {parallel_time:.2f} seconds")
    
    # Verify results are the same
    if result_sequential == result_parallel:
        print("Results match!")
        print(f"Speedup: {sequential_time / parallel_time:.2f}x")
    else:
        print("Results don't match - check implementation")


def demonstrate_async_processing():
    """Demonstrate asynchronous result processing"""
    print("\n=== Async Result Processing Demo ===")
    
    def variable_duration_task(task_id):
        """Task with variable duration"""
        duration = random.uniform(1, 3)
        print(f"Task {task_id} starting (duration: {duration:.1f}s)")
        time.sleep(duration)
        result = f"Result from task {task_id}"
        print(f"Task {task_id} completed")
        return result
    
    # TODO: Use ProcessPoolExecutor to submit 8 tasks
    # Process results as they complete using as_completed()
    # Print results in completion order, not submission order
    
    # Your code here


def demonstrate_error_handling():
    """Demonstrate error handling in process pools"""
    print("\n=== Error Handling Demo ===")
    
    def potentially_failing_task(task_id):
        """
        TODO: Implement a task that sometimes fails
        1. If task_id is divisible by 3, raise ValueError
        2. Otherwise, return f"Success: Task {task_id}"
        3. Add some processing time with sleep()
        """
        # Your code here
        pass
    
    # TODO: Use ProcessPoolExecutor to run 10 tasks
    # Handle exceptions properly and continue processing other tasks
    # Print both successful results and error messages
    
    # Your code here


class ParallelDataProcessor:
    """
    TODO: Implement a class for parallel data processing
    
    Features to implement:
    1. Process data in chunks using multiple processes
    2. Support different processing functions
    3. Handle errors gracefully
    4. Provide progress reporting
    """
    
    def __init__(self, num_processes=None):
        # TODO: Initialize with number of processes
        pass
    
    def process_data(self, data, processing_func, chunk_size=None):
        """
        TODO: Process data in parallel
        1. Split data into chunks
        2. Process chunks in parallel using ProcessPoolExecutor
        3. Combine results
        4. Handle errors
        """
        pass
    
    def _split_data(self, data, chunk_size):
        """TODO: Split data into chunks"""
        pass


def demonstrate_parallel_data_processor():
    """Demonstrate the ParallelDataProcessor class"""
    print("\n=== Parallel Data Processor Demo ===")
    
    def square_numbers(numbers):
        """Process a chunk of numbers by squaring them"""
        return [x * x for x in numbers]
    
    def sum_numbers(numbers):
        """Process a chunk of numbers by summing them"""
        return sum(numbers)
    
    # TODO: Create a ParallelDataProcessor instance
    # Test it with different processing functions:
    # 1. Square all numbers from 1 to 1000
    # 2. Sum numbers in chunks from 1 to 10000
    
    # Your code here


def performance_comparison():
    """Compare different multiprocessing approaches"""
    print("\n=== Performance Comparison ===")
    
    def cpu_task(n):
        """Simple CPU task for comparison"""
        return sum(i * i for i in range(n))
    
    numbers = [5000] * 20  # 20 identical tasks
    
    # TODO: Compare performance of:
    # 1. Sequential processing
    # 2. multiprocessing.Pool
    # 3. ProcessPoolExecutor
    # 4. Manual process creation
    
    approaches = [
        ("Sequential", lambda: [cpu_task(n) for n in numbers]),
        # Add your parallel approaches here
    ]
    
    for name, func in approaches:
        print(f"\nTesting {name}:")
        start_time = time.time()
        try:
            results = func()
            end_time = time.time()
            print(f"{name} completed in {end_time - start_time:.2f} seconds")
            print(f"Results: {len(results)} tasks completed")
        except Exception as e:
            print(f"{name} failed: {e}")


if __name__ == "__main__":
    print("Starting process pool demonstrations...")
    print(f"Available CPU cores: {multiprocessing.cpu_count()}")
    
    demonstrate_process_pool_executor()
    demonstrate_multiprocessing_pool()
    demonstrate_map_reduce()
    demonstrate_matrix_multiplication()
    demonstrate_async_processing()
    demonstrate_error_handling()
    demonstrate_parallel_data_processor()
    performance_comparison()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. ProcessPoolExecutor provides a high-level interface for process pools")
    print("2. multiprocessing.Pool offers various methods for parallel processing")
    print("3. Map-reduce patterns are powerful for data processing")
    print("4. as_completed() allows processing results as they finish")
    print("5. Proper error handling is crucial in parallel processing")
    print("6. Different approaches have different performance characteristics")