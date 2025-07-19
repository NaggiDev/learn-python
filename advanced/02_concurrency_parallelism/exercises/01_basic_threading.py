"""
Exercise 1: Basic Threading

Learn the fundamentals of creating and managing threads in Python.

Instructions:
1. Complete the functions below to demonstrate basic threading concepts
2. Run the script to see the output and understand thread execution
3. Experiment with different sleep times to see how threads run concurrently
"""

import threading
import time
import random


def task_1():
    """
    TODO: Create a simple function that:
    1. Prints "Task 1 starting"
    2. Sleeps for 2 seconds
    3. Prints "Task 1 completed"
    """
    # Your code here
    pass


def task_2():
    """
    TODO: Create a simple function that:
    1. Prints "Task 2 starting"
    2. Sleeps for 1 second
    3. Prints "Task 2 completed"
    """
    # Your code here
    pass


def worker_with_id(worker_id, duration):
    """
    TODO: Create a worker function that:
    1. Prints "Worker {worker_id} starting"
    2. Sleeps for {duration} seconds
    3. Prints "Worker {worker_id} finished after {duration} seconds"
    """
    # Your code here
    pass


class CountdownThread(threading.Thread):
    """
    TODO: Create a thread class that counts down from a given number.
    
    The class should:
    1. Accept a starting number and name in __init__
    2. Override the run() method to count down from the starting number to 1
    3. Print each number with a 1-second delay
    4. Print "Thread {name} finished countdown" when done
    """
    
    def __init__(self, start_number, name):
        # TODO: Initialize the thread and store parameters
        pass
    
    def run(self):
        # TODO: Implement the countdown logic
        pass


def demonstrate_basic_threading():
    """Demonstrate basic thread creation and execution"""
    print("=== Basic Threading Demo ===")
    
    # TODO: Create two threads using task_1 and task_2
    # Start both threads and wait for them to complete
    # Measure and print the total execution time
    
    start_time = time.time()
    
    # Your code here
    
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")


def demonstrate_multiple_workers():
    """Demonstrate creating multiple worker threads"""
    print("\n=== Multiple Workers Demo ===")
    
    # TODO: Create 5 worker threads with different IDs and random durations (1-3 seconds)
    # Start all threads and wait for completion
    # Print "All workers completed" when done
    
    # Your code here
    pass


def demonstrate_thread_class():
    """Demonstrate custom thread class"""
    print("\n=== Custom Thread Class Demo ===")
    
    # TODO: Create 3 CountdownThread instances with different starting numbers
    # Start all threads and wait for completion
    
    # Your code here
    pass


def sequential_vs_concurrent():
    """Compare sequential vs concurrent execution"""
    print("\n=== Sequential vs Concurrent Comparison ===")
    
    def simulate_io_task(task_id):
        """Simulate an I/O bound task"""
        print(f"Task {task_id} starting")
        time.sleep(1)  # Simulate I/O delay
        print(f"Task {task_id} completed")
        return f"Result from task {task_id}"
    
    # Sequential execution
    print("Sequential execution:")
    start_time = time.time()
    
    # TODO: Run simulate_io_task for task IDs 1, 2, 3 sequentially
    # Your code here
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Concurrent execution
    print("\nConcurrent execution:")
    start_time = time.time()
    
    # TODO: Run simulate_io_task for task IDs 1, 2, 3 concurrently using threads
    # Your code here
    
    concurrent_time = time.time() - start_time
    print(f"Concurrent time: {concurrent_time:.2f} seconds")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")


if __name__ == "__main__":
    demonstrate_basic_threading()
    demonstrate_multiple_workers()
    demonstrate_thread_class()
    sequential_vs_concurrent()
    
    print("\n=== Exercise Complete ===")
    print("Key observations:")
    print("1. Threads run concurrently, not necessarily in the order they were started")
    print("2. Total execution time is less than the sum of individual task times")
    print("3. Thread scheduling is handled by the operating system")
    print("4. I/O-bound tasks benefit significantly from threading")