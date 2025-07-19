"""
Solution: Basic Threading

Complete implementation of basic threading concepts.
"""

import threading
import time
import random


def task_1():
    """Simple function that demonstrates basic thread execution"""
    print("Task 1 starting")
    time.sleep(2)
    print("Task 1 completed")


def task_2():
    """Simple function that demonstrates basic thread execution"""
    print("Task 2 starting")
    time.sleep(1)
    print("Task 2 completed")


def worker_with_id(worker_id, duration):
    """Worker function that takes parameters"""
    print(f"Worker {worker_id} starting")
    time.sleep(duration)
    print(f"Worker {worker_id} finished after {duration} seconds")


class CountdownThread(threading.Thread):
    """Custom thread class that counts down from a given number"""
    
    def __init__(self, start_number, name):
        super().__init__()
        self.start_number = start_number
        self.name = name
    
    def run(self):
        for i in range(self.start_number, 0, -1):
            print(f"Thread {self.name}: {i}")
            time.sleep(1)
        print(f"Thread {self.name} finished countdown")


def demonstrate_basic_threading():
    """Demonstrate basic thread creation and execution"""
    print("=== Basic Threading Demo ===")
    
    start_time = time.time()
    
    # Create two threads
    thread1 = threading.Thread(target=task_1)
    thread2 = threading.Thread(target=task_2)
    
    # Start both threads
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")


def demonstrate_multiple_workers():
    """Demonstrate creating multiple worker threads"""
    print("\n=== Multiple Workers Demo ===")
    
    threads = []
    
    # Create 5 worker threads with random durations
    for i in range(5):
        duration = random.uniform(1, 3)
        thread = threading.Thread(target=worker_with_id, args=(i+1, duration))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("All workers completed")


def demonstrate_thread_class():
    """Demonstrate custom thread class"""
    print("\n=== Custom Thread Class Demo ===")
    
    # Create 3 CountdownThread instances
    threads = [
        CountdownThread(3, "Alpha"),
        CountdownThread(5, "Beta"),
        CountdownThread(2, "Gamma")
    ]
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()


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
    
    results = []
    for task_id in [1, 2, 3]:
        result = simulate_io_task(task_id)
        results.append(result)
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Concurrent execution
    print("\nConcurrent execution:")
    start_time = time.time()
    
    threads = []
    results = []
    
    def task_wrapper(task_id, results_list):
        result = simulate_io_task(task_id)
        results_list.append(result)
    
    # Create and start threads
    for task_id in [1, 2, 3]:
        thread = threading.Thread(target=task_wrapper, args=(task_id, results))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
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