"""
Solution: Basic Asyncio

Complete implementation of basic asyncio concepts.
"""

import asyncio
import time
import random


async def simple_async_task(name, duration):
    """Simple async task that demonstrates basic async/await"""
    print(f"{name} starting")
    await asyncio.sleep(duration)
    print(f"{name} completed after {duration} seconds")
    return f"Result from {name}"


async def fetch_data_simulation(source, delay):
    """Simulate fetching data from a source"""
    print(f"Fetching data from {source}")
    await asyncio.sleep(delay)
    print(f"Data fetched from {source}")
    return {"source": source, "data": f"Data from {source}", "delay": delay}


async def demonstrate_sequential_execution():
    """Demonstrate sequential async execution"""
    print("=== Sequential Async Execution ===")
    
    start_time = time.time()
    
    # Call tasks sequentially
    result1 = await simple_async_task("Alpha", 1)
    result2 = await simple_async_task("Beta", 2)
    result3 = await simple_async_task("Gamma", 1)
    
    results = [result1, result2, result3]
    print(f"Results: {results}")
    
    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time:.2f} seconds")


async def demonstrate_concurrent_execution():
    """Demonstrate concurrent async execution"""
    print("\n=== Concurrent Async Execution ===")
    
    start_time = time.time()
    
    # Run tasks concurrently using asyncio.gather()
    results = await asyncio.gather(
        simple_async_task("Alpha", 1),
        simple_async_task("Beta", 2),
        simple_async_task("Gamma", 1)
    )
    
    print(f"Results: {results}")
    
    end_time = time.time()
    print(f"Concurrent execution time: {end_time - start_time:.2f} seconds")


async def demonstrate_create_task():
    """Demonstrate using asyncio.create_task()"""
    print("\n=== Using create_task() ===")
    
    # Create tasks
    task1 = asyncio.create_task(fetch_data_simulation("API-1", 1.5))
    task2 = asyncio.create_task(fetch_data_simulation("API-2", 1.0))
    task3 = asyncio.create_task(fetch_data_simulation("API-3", 2.0))
    
    # Wait for all tasks to complete
    results = await asyncio.gather(task1, task2, task3)
    
    print("Results:")
    for result in results:
        print(f"  {result}")


async def demonstrate_as_completed():
    """Demonstrate processing results as they complete"""
    print("\n=== Processing Results as Completed ===")
    
    # Create tasks with random delays
    tasks = []
    for i in range(1, 6):
        delay = random.uniform(0.5, 2.0)
        task = asyncio.create_task(fetch_data_simulation(f"Source-{i}", delay))
        tasks.append(task)
    
    # Process results as they complete
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(f"Completed: {result['source']} (delay: {result['delay']:.2f}s)")


class AsyncCounter:
    """Async counter class with async methods"""
    
    def __init__(self):
        self.counter = 0
    
    async def increment(self):
        """Increment counter with small async delay"""
        await asyncio.sleep(0.01)  # Small delay to simulate async work
        self.counter += 1
    
    async def get_value(self):
        """Return current counter value"""
        await asyncio.sleep(0.001)  # Tiny delay to make it async
        return self.counter
    
    async def reset(self):
        """Reset counter to 0"""
        await asyncio.sleep(0.001)
        self.counter = 0


async def demonstrate_async_counter():
    """Demonstrate the AsyncCounter class"""
    print("\n=== Async Counter Demo ===")
    
    counter = AsyncCounter()
    
    # Increment 5 times concurrently
    await asyncio.gather(*[counter.increment() for _ in range(5)])
    
    value = await counter.get_value()
    print(f"Counter value after 5 increments: {value}")
    
    # Reset and verify
    await counter.reset()
    value = await counter.get_value()
    print(f"Counter value after reset: {value}")


async def async_range_generator(start, stop, delay=0.1):
    """Async generator that yields numbers with delays"""
    for i in range(start, stop):
        await asyncio.sleep(delay)
        print(f"Generated: {i}")
        yield i


async def demonstrate_async_generator():
    """Demonstrate async generator"""
    print("\n=== Async Generator Demo ===")
    
    # Use async for to iterate over async generator
    async for number in async_range_generator(1, 6):
        print(f"Received: {number}")


async def timeout_task(name, duration):
    """Task that might timeout"""
    print(f"{name} starting (will take {duration} seconds)")
    await asyncio.sleep(duration)
    print(f"{name} completed")
    return f"Success: {name}"


async def demonstrate_timeout():
    """Demonstrate asyncio timeout handling"""
    print("\n=== Timeout Demo ===")
    
    # Test successful task (within timeout)
    try:
        result = await asyncio.wait_for(timeout_task("FastTask", 1), timeout=2.0)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("FastTask timed out")
    
    # Test task that times out
    try:
        result = await asyncio.wait_for(timeout_task("SlowTask", 3), timeout=2.0)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("SlowTask timed out after 2 seconds")


async def cancellable_task(name, duration):
    """Task that can be cancelled"""
    try:
        print(f"{name} starting")
        await asyncio.sleep(duration)
        print(f"{name} completed")
        return f"Success: {name}"
    except asyncio.CancelledError:
        print(f"{name} was cancelled")
        raise  # Re-raise the cancellation


async def demonstrate_cancellation():
    """Demonstrate task cancellation"""
    print("\n=== Task Cancellation Demo ===")
    
    # Create a long-running task
    task = asyncio.create_task(cancellable_task("CancellableTask", 5))
    
    # Let it run for 2 seconds, then cancel
    await asyncio.sleep(2)
    task.cancel()
    
    try:
        result = await task
        print(f"Task result: {result}")
    except asyncio.CancelledError:
        print("Task was successfully cancelled")


async def worker_task(worker_id, work_queue):
    """Worker that processes items from a queue"""
    while True:
        item = await work_queue.get()
        if item is None:
            break
        
        # Process the item
        await asyncio.sleep(0.1)  # Simulate work
        print(f"Worker {worker_id} processed {item}")
        work_queue.task_done()


async def demonstrate_task_coordination():
    """Demonstrate coordinating multiple async tasks"""
    print("\n=== Task Coordination Demo ===")
    
    # Create queue and add work items
    work_queue = asyncio.Queue()
    items = ["task1", "task2", "task3", "task4", "task5"]
    
    # Add items to queue
    for item in items:
        await work_queue.put(item)
    
    # Add sentinel values for workers
    for _ in range(3):
        await work_queue.put(None)
    
    # Create and start workers
    workers = [
        asyncio.create_task(worker_task(i, work_queue))
        for i in range(3)
    ]
    
    # Wait for all workers to complete
    await asyncio.gather(*workers)
    print("All workers completed")


async def batch_processor(items, batch_size=3):
    """Process items in batches"""
    results = []
    
    # Split items into batches
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        
        # Process batch concurrently
        async def process_item(item):
            await asyncio.sleep(0.2)  # Simulate processing
            return f"Processed {item}"
        
        batch_results = await asyncio.gather(*[process_item(item) for item in batch])
        results.extend(batch_results)
        print(f"Completed batch: {batch}")
    
    return results


async def demonstrate_batch_processing():
    """Demonstrate batch processing"""
    print("\n=== Batch Processing Demo ===")
    
    items = list(range(1, 11))
    
    start_time = time.time()
    results = await batch_processor(items, batch_size=3)
    end_time = time.time()
    
    print(f"Processed {len(items)} items in {end_time - start_time:.2f} seconds")
    print(f"Results: {results[:3]}...")  # Show first 3 results


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