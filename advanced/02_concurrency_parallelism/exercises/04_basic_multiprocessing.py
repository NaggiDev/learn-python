"""
Exercise 4: Basic Multiprocessing

Learn the fundamentals of creating and managing processes in Python.

Instructions:
1. Complete the functions below to demonstrate basic multiprocessing concepts
2. Run the script to see the output and understand process execution
3. Compare performance between sequential and parallel execution

Note: Always include the 'if __name__ == "__main__":' guard when using multiprocessing!
"""

import multiprocessing
import time
import os
import math


def cpu_intensive_task(n, task_id):
    """
    TODO: Create a CPU-intensive function that:
    1. Prints "Task {task_id} (PID: {process_id}) starting with n={n}"
    2. Calculates the sum of squares from 1 to n
    3. Prints "Task {task_id} (PID: {process_id}) finished, result: {result}"
    4. Returns the result
    
    Use os.getpid() to get the current process ID
    """
    # Your code here
    pass


def io_simulation_task(task_id, duration):
    """
    TODO: Create a function that simulates I/O work:
    1. Print "I/O Task {task_id} (PID: {process_id}) starting"
    2. Sleep for {duration} seconds
    3. Print "I/O Task {task_id} (PID: {process_id}) completed"
    4. Return f"Result from I/O task {task_id}"
    """
    # Your code here
    pass


class CalculatorProcess(multiprocessing.Process):
    """
    TODO: Create a custom process class that performs calculations.
    
    The class should:
    1. Accept operation ('square', 'factorial', 'fibonacci') and number in __init__
    2. Override the run() method to perform the calculation
    3. Store the result in an instance variable
    4. Print the process ID and calculation details
    """
    
    def __init__(self, operation, number):
        # TODO: Initialize the process and store parameters
        pass
    
    def run(self):
        # TODO: Implement the calculation logic
        pass
    
    def calculate_square(self, n):
        """TODO: Calculate n squared"""
        pass
    
    def calculate_factorial(self, n):
        """TODO: Calculate n factorial"""
        pass
    
    def calculate_fibonacci(self, n):
        """TODO: Calculate nth Fibonacci number"""
        pass


def demonstrate_basic_processes():
    """Demonstrate basic process creation and execution"""
    print("=== Basic Process Demo ===")
    print(f"Main process PID: {os.getpid()}")
    
    # TODO: Create two processes using cpu_intensive_task
    # Process 1: n=100000, task_id=1
    # Process 2: n=150000, task_id=2
    # Start both processes and wait for completion
    # Measure and print the total execution time
    
    start_time = time.time()
    
    # Your code here
    
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")


def demonstrate_multiple_processes():
    """Demonstrate creating multiple processes with different tasks"""
    print("\n=== Multiple Processes Demo ===")
    
    # TODO: Create 4 processes:
    # 2 CPU-intensive tasks with different n values
    # 2 I/O simulation tasks with different durations
    # Start all processes and wait for completion
    
    processes = []
    
    # Your code here
    
    print("All processes completed")


def demonstrate_process_class():
    """Demonstrate custom process class"""
    print("\n=== Custom Process Class Demo ===")
    
    # TODO: Create 3 CalculatorProcess instances:
    # 1. Square of 25
    # 2. Factorial of 10
    # 3. Fibonacci of 20
    # Start all processes and wait for completion
    
    # Your code here
    
    print("All calculations completed")


def sequential_vs_parallel_cpu():
    """Compare sequential vs parallel execution for CPU-bound tasks"""
    print("\n=== Sequential vs Parallel CPU Tasks ===")
    
    def calculate_primes(limit):
        """Calculate prime numbers up to limit"""
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        primes = [i for i in range(2, limit) if is_prime(i)]
        return len(primes)
    
    limits = [10000, 15000, 20000, 25000]
    
    # Sequential execution
    print("Sequential execution:")
    start_time = time.time()
    
    # TODO: Run calculate_primes for each limit sequentially
    # Store results and print them
    
    # Your code here
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Parallel execution
    print("\nParallel execution:")
    start_time = time.time()
    
    # TODO: Run calculate_primes for each limit in parallel using processes
    # Create a process for each limit, start them, and collect results
    # Note: You'll need a way to collect results from processes
    
    # Your code here
    
    parallel_time = time.time() - start_time
    print(f"Parallel time: {parallel_time:.2f} seconds")
    
    if sequential_time > 0 and parallel_time > 0:
        print(f"Speedup: {sequential_time / parallel_time:.2f}x")


def demonstrate_process_communication():
    """Demonstrate basic process communication using return values"""
    print("\n=== Process Communication Demo ===")
    
    def worker_with_result(n, process_id):
        """Worker that returns a result"""
        result = sum(i * i for i in range(n))
        print(f"Process {process_id}: Calculated sum of squares up to {n} = {result}")
        return result
    
    # TODO: This is tricky with basic Process class since it doesn't return values
    # For now, just demonstrate that processes run independently
    # We'll learn about proper communication methods in the next exercise
    
    processes = []
    for i in range(3):
        process = multiprocessing.Process(
            target=worker_with_result, 
            args=(1000 * (i + 1), i + 1)
        )
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print("Note: Basic Process class doesn't return values directly.")
    print("We'll learn about proper inter-process communication in the next exercise.")


def demonstrate_process_properties():
    """Demonstrate process properties and methods"""
    print("\n=== Process Properties Demo ===")
    
    def long_running_task(duration):
        """A task that runs for a specified duration"""
        print(f"Long running task starting (PID: {os.getpid()})")
        time.sleep(duration)
        print(f"Long running task completed (PID: {os.getpid()})")
    
    # TODO: Create a process that runs for 3 seconds
    # Demonstrate process properties:
    # - name
    # - pid (after starting)
    # - is_alive()
    # Check these properties before starting, after starting, and after completion
    
    process = multiprocessing.Process(target=long_running_task, args=(3,), name="LongTask")
    
    # Your code here - check properties before starting
    
    process.start()
    
    # Your code here - check properties after starting
    
    # Wait a bit and check if still alive
    time.sleep(1)
    # Your code here - check if process is still alive
    
    process.join()
    
    # Your code here - check properties after completion


if __name__ == "__main__":
    print("Starting multiprocessing demonstrations...")
    print(f"Available CPU cores: {multiprocessing.cpu_count()}")
    
    demonstrate_basic_processes()
    demonstrate_multiple_processes()
    demonstrate_process_class()
    sequential_vs_parallel_cpu()
    demonstrate_process_communication()
    demonstrate_process_properties()
    
    print("\n=== Exercise Complete ===")
    print("Key observations:")
    print("1. Each process has its own Process ID (PID)")
    print("2. Processes run independently with separate memory spaces")
    print("3. CPU-bound tasks can benefit significantly from multiprocessing")
    print("4. Process creation has more overhead than thread creation")
    print("5. The 'if __name__ == \"__main__\":' guard is essential")