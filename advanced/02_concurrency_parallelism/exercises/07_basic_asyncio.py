"""
Exercise 7: Basic Asyncio

Learn the fundamentals of asynchronous programming with asyncio.

Instructions:
1. Complete the async functions below
2. Run the script to understand async/await behavior
3. Compare sequential vs concurrent execution patterns

Note: This exercise focuses on the core concepts of asyncio.
"""

import asyncio
import time
import random


async def simple_async_task(name, duration):
    """
    TODO: Create a simple async task that:
    1. Prints "{name} starting"
    2. Sleeps asynchronously for {duration} seconds
    3. Prints "{name} completed after {duration} seconds"
    4. Returns f"Result from {name}"
    """
    # Your code here
    pass


async def fetch_data_simulation(source, delay):
    """
    TODO: Simulate fetching data from a source:
    1. Print "Fetching data from {source}"
    2. Sleep for {delay} seconds (use asyncio.sleep)
    3. Print "Data fetched from {source}"
    4. Return {"source": source, "data": f"Data from {source}", "delay": delay}
    """
    # Your code here
    pass


async def demonstrate_sequential_execution():
    """Demonstrate sequential async execution"""
    print("=== Sequential Async Execution ===")
    
    start_time = time.time()
    
    # TODO: Call simple_async_task three times sequentially:
    # - Task "Alpha" with duration 1
    # - Task "Beta" with duration 2  
    # - Task "Gamma" with duration 1
    # Store results and print them
    
    # Your code here
    
    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time:.2f} seconds")


async def demonstrate_concurrent_execution():
    """Demonstrate concurrent async execution"""
    print("\n=== Concurrent Async Execution ===")
    
    start_time = time.time()
    
    # TODO: Run the same three tasks concurrently using asyncio.gather():
    # - Task "Alpha" with duration 1
    # - Task "Beta" with duration 2
    # - Task "Gamma" with duration 1
    # Store results and print them
    
    # Your code here
    
    end_time = time.time()
    print(f"Concurrent execution time: {end_time - start_time:.2f} seconds")


async def demonstrate_create_task():
    """Demonstrate using asyncio.create_task()"""
    print("\n=== Using create_task() ===")
    
    # TODO: Create tasks using asyncio.create_task() for:
    # - fetch_data_simulation("API-1", 1.5)
    # - fetch_data_simulation("API-2", 1.0)
    # - fetch_data_simulation("API-3", 2.0)
    # Wait for all tasks to complete and print results
    
    # Your code here


async def demonstrate_as_completed():
    """Demonstrate processing results as they complete"""
    print("\n=== Processing Results as Completed ===")
    
    # TODO: Create a list of tasks with different durations:
    # Use fetch_data_simulation with sources "Source-1" through "Source-5"
    # and random delays between 0.5 and 2.0 seconds
    # Use asyncio.as_completed() to process results as they finish
    
    # Your code here


class AsyncCounter:
    """
    TODO: Implement an async counter class.
    
    The class should:
    1. Have an internal counter starting at 0
    2. Have an async increment() method that increments and sleeps briefly
    3. Have an async get_value() method that returns the current value
    4. Have an async reset() method that resets to 0
    """
    
    def __init__(self):
        # TODO: Initialize the counter
        pass
    
    async def increment(self):
        """TODO: Increment counter with small async delay"""
        pass
    
    async def get_value(self):
        """TODO: Return current counter value"""
        pass
    
    async def reset(self):
        """TODO: Reset counter to 0"""
        pass


async def demonstrate_async_counter():
    """Demonstrate the AsyncCounter class"""
    print("\n=== Async Counter Demo ===")
    
    # TODO: Create an AsyncCounter instance
    # Increment it 5 times concurrently
    # Print the final value
    # Reset it and verify it's 0
    
    # Your code here


async def async_range_generator(start, stop, delay=0.1):
    """
    TODO: Create an async generator that:
    1. Yields numbers from start to stop-1
    2. Sleeps for {delay} seconds between each yield
    3. Prints "Generated: {number}" for each number
    """
    # Your code here
    pass


async def demonstrate_async_generator():
    """Demonstrate async generator"""
    print("\n=== Async Generator Demo ===")
    
    # TODO: Use the async_range_generator to generate numbers 1-5
    # Print each number as it's generated using "async for"
    
    # Your code here


async def timeout_task(name, duration):
    """
    TODO: Create a task that might timeout:
    1. Print "{name} starting (will take {duration} seconds)"
    2. Sleep for {duration} seconds
    3. Print "{name} completed"
    4. Return f"Success: {name}"
    """
    # Your code here
    pass


async def demonstrate_timeout():
    """Demonstrate asyncio timeout handling"""
    print("\n=== Timeout Demo ===")
    
    # TODO: Test timeout behavior:
    # 1. Run timeout_task("FastTask", 1) with timeout of 2 seconds (should succeed)
    # 2. Run timeout_task("SlowTask", 3) with timeout of 2 seconds (should timeout)
    # Use asyncio.wait_for() and handle TimeoutError
    
    # Your code here


async def cancellable_task(name, duration):
    """
    TODO: Create a task that can be cancelled:
    1. Print "{name} starting"
    2. Try to sleep for {duration} seconds
    3. Handle asyncio.CancelledError and print "{name} was cancelled"
    4. Re-raise the CancelledError
    5. If not cancelled, print "{name} completed" and return result
    """
    # Your code here
    pass


async def demonstrate_cancellation():
    """Demonstrate task cancellation"""
    print("\n=== Task Cancellation Demo ===")
    
    # TODO: Create a cancellable_task that runs for 5 seconds
    # Let it run for 2 seconds, then cancel it
    # Handle the CancelledError appropriately
    
    # Your code here


async def worker_task(worker_id, work_queue):
    """
    TODO: Create a worker that processes items from a queue:
    1. Loop continuously getting items from work_queue
    2. If item is None, break the loop
    3. Process the item (print and sleep briefly)
    4. Print "Worker {worker_id} processed {item}"
    """
    # Your code here
    pass


async def demonstrate_task_coordination():
    """Demonstrate coordinating multiple async tasks"""
    print("\n=== Task Coordination Demo ===")
    
    # TODO: Create a scenario with:
    # 1. A queue with items ["task1", "task2", "task3", "task4", "task5", None]
    # 2. Three worker tasks that process items from the queue
    # 3. Wait for all workers to complete
    
    # Your code here


async def batch_processor(items, batch_size=3):
    """
    TODO: Process items in batches:
    1. Split items into batches of {batch_size}
    2. Process each batch concurrently
    3. For each item in a batch, simulate processing with async sleep
    4. Return all results
    """
    # Your code here
    pass


async def demonstrate_batch_processing():
    """Demonstrate batch processing"""
    print("\n=== Batch Processing Demo ===")
    
    # TODO: Use batch_processor to process items 1-10 in batches of 3
    # Measure and print the processing time
    
    items = list(range(1, 11))
    
    # Your code here


async def main():
    """Main function to run all demonstrations"""
    print("Starting asyncio demonstrations...")
    
    await demonstrate_sequential_execution()
    await demonstrate_concurrent_execution()
    await demonstrate_create_task()
    await demonstrate_as_completed()
    await demonstrate_async_counter()
    await demonstrate_async_generator()
    await demonstrate_timeout()
    await demonstrate_cancellation()
    await demonstrate_task_coordination()
    await demonstrate_batch_processing()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. async/await enables non-blocking asynchronous programming")
    print("2. asyncio.gather() runs coroutines concurrently")
    print("3. asyncio.create_task() creates tasks that run in the background")
    print("4. asyncio.as_completed() processes results as they finish")
    print("5. Proper exception handling is crucial in async code")
    print("6. Task cancellation and timeouts provide control over execution")


if __name__ == "__main__":
    asyncio.run(main())