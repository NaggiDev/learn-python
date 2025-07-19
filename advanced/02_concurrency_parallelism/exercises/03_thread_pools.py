"""
Exercise 3: Thread Pools and Advanced Threading

Learn to use ThreadPoolExecutor and advanced threading patterns.

Instructions:
1. Complete the functions below to work with thread pools
2. Implement common threading patterns
3. Compare different approaches to concurrent execution
"""

import threading
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from queue import Queue, Empty
import json


def simulate_io_task(task_id, duration=None):
    """Simulate an I/O-bound task like file reading or network request"""
    if duration is None:
        duration = random.uniform(0.5, 2.0)
    
    print(f"Task {task_id} starting (duration: {duration:.1f}s)")
    time.sleep(duration)
    result = f"Result from task {task_id}"
    print(f"Task {task_id} completed")
    return result


def simulate_cpu_task(n):
    """Simulate a CPU-bound task (calculating sum of squares)"""
    print(f"CPU task starting: sum of squares up to {n}")
    result = sum(i * i for i in range(n))
    print(f"CPU task completed: sum of squares up to {n} = {result}")
    return result


def fetch_url_info(url):
    """
    TODO: Implement a function that fetches URL information.
    
    The function should:
    1. Make a GET request to the URL with a 5-second timeout
    2. Return a dictionary with: url, status_code, response_time, content_length
    3. Handle exceptions and return error information
    """
    start_time = time.time()
    
    try:
        # Your code here
        pass
    except Exception as e:
        # Your code here
        pass


def demonstrate_basic_thread_pool():
    """Demonstrate basic ThreadPoolExecutor usage"""
    print("=== Basic Thread Pool Demo ===")
    
    # TODO: Use ThreadPoolExecutor to run 5 I/O tasks concurrently
    # Use max_workers=3
    # Collect and print all results
    
    tasks = list(range(1, 6))
    
    # Your code here
    pass


def demonstrate_thread_pool_with_different_args():
    """Demonstrate thread pool with different arguments for each task"""
    print("\n=== Thread Pool with Different Arguments ===")
    
    # TODO: Create tasks with different durations
    # Use ThreadPoolExecutor.submit() to submit individual tasks
    # Use as_completed() to process results as they finish
    
    task_configs = [
        (1, 1.0),
        (2, 0.5),
        (3, 1.5),
        (4, 0.8),
        (5, 1.2)
    ]
    
    # Your code here
    pass


def demonstrate_url_fetching():
    """Demonstrate concurrent URL fetching"""
    print("\n=== Concurrent URL Fetching ===")
    
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
        "https://httpbin.org/json",
        "https://httpbin.org/headers"
    ]
    
    # Sequential fetching
    print("Sequential fetching:")
    start_time = time.time()
    
    # TODO: Fetch URLs sequentially and measure time
    # Your code here
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Concurrent fetching
    print("\nConcurrent fetching:")
    start_time = time.time()
    
    # TODO: Fetch URLs concurrently using ThreadPoolExecutor
    # Use max_workers=3
    # Print results as they complete
    
    # Your code here
    
    concurrent_time = time.time() - start_time
    print(f"Concurrent time: {concurrent_time:.2f} seconds")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")


class WorkerPool:
    """
    TODO: Implement a custom worker pool using Queue and threads.
    
    This demonstrates how ThreadPoolExecutor works internally.
    """
    
    def __init__(self, num_workers=3):
        # TODO: Initialize the worker pool
        # Create a queue for tasks
        # Create and start worker threads
        # Keep track of workers for cleanup
        pass
    
    def _worker(self):
        """
        TODO: Worker thread function
        1. Continuously get tasks from the queue
        2. Execute the task function with its arguments
        3. Handle the special shutdown sentinel
        """
        pass
    
    def submit(self, func, *args, **kwargs):
        """
        TODO: Submit a task to the worker pool
        Put the task (function and arguments) in the queue
        """
        pass
    
    def shutdown(self):
        """
        TODO: Shutdown the worker pool
        1. Send shutdown signals to all workers
        2. Wait for all workers to finish
        """
        pass


def demonstrate_custom_worker_pool():
    """Demonstrate custom worker pool implementation"""
    print("\n=== Custom Worker Pool Demo ===")
    
    # TODO: Create a WorkerPool instance with 3 workers
    pool = None  # Replace with WorkerPool(3)
    
    # TODO: Submit 8 I/O tasks to the pool
    # Wait a bit for tasks to complete
    # Shutdown the pool
    
    # Your code here
    
    print("Custom worker pool demo completed")


class TaskScheduler:
    """
    TODO: Implement a task scheduler that can run tasks at specific intervals.
    
    Features to implement:
    1. Schedule one-time tasks
    2. Schedule recurring tasks
    3. Cancel scheduled tasks
    4. Shutdown scheduler
    """
    
    def __init__(self):
        # TODO: Initialize scheduler components
        pass
    
    def schedule_once(self, func, delay, *args, **kwargs):
        """
        TODO: Schedule a function to run once after a delay
        Return a task ID that can be used to cancel the task
        """
        pass
    
    def schedule_recurring(self, func, interval, *args, **kwargs):
        """
        TODO: Schedule a function to run repeatedly at intervals
        Return a task ID that can be used to cancel the task
        """
        pass
    
    def cancel_task(self, task_id):
        """TODO: Cancel a scheduled task"""
        pass
    
    def shutdown(self):
        """TODO: Shutdown the scheduler and all running tasks"""
        pass


def demonstrate_task_scheduler():
    """Demonstrate custom task scheduler"""
    print("\n=== Task Scheduler Demo ===")
    
    def print_message(message):
        print(f"[{time.strftime('%H:%M:%S')}] {message}")
    
    # TODO: Create a TaskScheduler instance
    scheduler = None  # Replace with TaskScheduler()
    
    # TODO: Schedule some tasks:
    # 1. One-time task after 1 second
    # 2. Recurring task every 2 seconds
    # 3. Let it run for 8 seconds
    # 4. Cancel the recurring task
    # 5. Shutdown the scheduler
    
    # Your code here
    
    print("Task scheduler demo completed")


def demonstrate_thread_local_storage():
    """Demonstrate thread-local storage"""
    print("\n=== Thread-Local Storage Demo ===")
    
    # TODO: Create a threading.local() object
    thread_local_data = None  # Replace with threading.local()
    
    def worker(worker_id):
        """
        TODO: Each worker should:
        1. Set a unique value in thread_local_data
        2. Sleep for a random time
        3. Read and print the value from thread_local_data
        4. Verify the value is still the same
        """
        # Your code here
        pass
    
    # TODO: Create 5 threads running the worker function
    # Start all threads and wait for completion
    
    # Your code here


def performance_comparison():
    """Compare different threading approaches"""
    print("\n=== Performance Comparison ===")
    
    def run_tasks_sequential(tasks):
        """Run tasks sequentially"""
        results = []
        for task_id in tasks:
            result = simulate_io_task(task_id, 0.5)
            results.append(result)
        return results
    
    def run_tasks_manual_threads(tasks):
        """Run tasks using manual thread creation"""
        # TODO: Implement using manual thread creation
        # Create a thread for each task
        # Collect results (hint: use a shared list with lock)
        pass
    
    def run_tasks_thread_pool(tasks):
        """Run tasks using ThreadPoolExecutor"""
        # TODO: Implement using ThreadPoolExecutor
        pass
    
    tasks = list(range(1, 11))  # 10 tasks
    
    # Test each approach
    approaches = [
        ("Sequential", run_tasks_sequential),
        ("Manual Threads", run_tasks_manual_threads),
        ("Thread Pool", run_tasks_thread_pool)
    ]
    
    for name, func in approaches:
        print(f"\nTesting {name}:")
        start_time = time.time()
        
        try:
            results = func(tasks)
            end_time = time.time()
            print(f"{name} completed in {end_time - start_time:.2f} seconds")
            print(f"Results: {len(results) if results else 0} tasks completed")
        except Exception as e:
            print(f"{name} failed: {e}")


if __name__ == "__main__":
    demonstrate_basic_thread_pool()
    demonstrate_thread_pool_with_different_args()
    demonstrate_url_fetching()
    demonstrate_custom_worker_pool()
    demonstrate_task_scheduler()
    demonstrate_thread_local_storage()
    performance_comparison()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. ThreadPoolExecutor simplifies concurrent task execution")
    print("2. as_completed() allows processing results as they finish")
    print("3. Thread pools are more efficient than creating threads manually")
    print("4. Thread-local storage provides per-thread data isolation")
    print("5. Different threading patterns suit different use cases")