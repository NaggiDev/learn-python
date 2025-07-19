# Asyncio and Asynchronous Programming

## Introduction

Asyncio is Python's built-in library for writing asynchronous, concurrent code using the async/await syntax. It's particularly well-suited for I/O-bound and high-level structured network code, allowing you to handle thousands of concurrent connections efficiently.

## Key Concepts

### What is Asynchronous Programming?

**Asynchronous programming** allows a program to handle multiple operations concurrently without using multiple threads or processes. Instead of blocking on I/O operations, the program can switch to other tasks while waiting for I/O to complete.

### When to Use Asyncio

Asyncio is most effective for:
- **I/O-bound tasks**: Network requests, file operations, database queries
- **High-concurrency applications**: Web servers, chat applications, real-time systems
- **Event-driven programming**: GUI applications, game loops, reactive systems
- **Coordinating multiple async operations**: Gathering results from multiple APIs

### Asyncio vs Threading vs Multiprocessing

| Aspect | Asyncio | Threading | Multiprocessing |
|--------|---------|-----------|-----------------|
| **Concurrency Model** | Cooperative | Preemptive | Parallel |
| **Memory Usage** | Low | Medium | High |
| **Context Switching** | Explicit (await) | Automatic | OS-managed |
| **Best for** | I/O-bound, high concurrency | I/O-bound, moderate concurrency | CPU-bound |
| **Debugging** | Easier | Moderate | Complex |
| **Scalability** | Excellent for I/O | Limited by GIL | Limited by cores |

## Basic Asyncio Concepts

### Coroutines and async/await

```python
import asyncio
import time

# Traditional synchronous function
def sync_function():
    print("Sync function starting")
    time.sleep(2)  # Blocking operation
    print("Sync function completed")
    return "Sync result"

# Asynchronous coroutine
async def async_function():
    print("Async function starting")
    await asyncio.sleep(2)  # Non-blocking operation
    print("Async function completed")
    return "Async result"

# Running async code
async def main():
    # This runs sequentially (one after another)
    result1 = await async_function()
    result2 = await async_function()
    print(f"Results: {result1}, {result2}")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
```

### Running Multiple Coroutines Concurrently

```python
import asyncio
import time

async def fetch_data(name, delay):
    """Simulate fetching data from an API"""
    print(f"Starting to fetch {name}")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"Finished fetching {name}")
    return f"Data from {name}"

async def main():
    # Sequential execution (slow)
    print("=== Sequential Execution ===")
    start_time = time.time()
    
    result1 = await fetch_data("API-1", 2)
    result2 = await fetch_data("API-2", 1)
    result3 = await fetch_data("API-3", 3)
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Concurrent execution (fast)
    print("\n=== Concurrent Execution ===")
    start_time = time.time()
    
    # Create tasks for concurrent execution
    task1 = asyncio.create_task(fetch_data("API-1", 2))
    task2 = asyncio.create_task(fetch_data("API-2", 1))
    task3 = asyncio.create_task(fetch_data("API-3", 3))
    
    # Wait for all tasks to complete
    results = await asyncio.gather(task1, task2, task3)
    
    concurrent_time = time.time() - start_time
    print(f"Concurrent time: {concurrent_time:.2f} seconds")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Working with Tasks

### Creating and Managing Tasks

```python
import asyncio
import random

async def worker(name, work_time):
    """A worker coroutine that simulates work"""
    print(f"Worker {name} starting")
    await asyncio.sleep(work_time)
    print(f"Worker {name} completed")
    return f"Result from {name}"

async def main():
    # Method 1: Using asyncio.create_task()
    print("=== Using create_task() ===")
    tasks = []
    for i in range(5):
        work_time = random.uniform(1, 3)
        task = asyncio.create_task(worker(f"Worker-{i}", work_time))
        tasks.append(task)
    
    # Wait for all tasks
    results = await asyncio.gather(*tasks)
    print(f"All workers completed: {results}")
    
    # Method 2: Using asyncio.gather() directly
    print("\n=== Using gather() directly ===")
    results = await asyncio.gather(
        worker("Alpha", 1),
        worker("Beta", 2),
        worker("Gamma", 1.5)
    )
    print(f"Results: {results}")
    
    # Method 3: Using asyncio.as_completed()
    print("\n=== Using as_completed() ===")
    tasks = [
        asyncio.create_task(worker(f"Task-{i}", random.uniform(0.5, 2)))
        for i in range(4)
    ]
    
    # Process results as they complete
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(f"Completed: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Task Cancellation and Timeouts

```python
import asyncio

async def long_running_task(name, duration):
    """A task that takes a long time"""
    try:
        print(f"{name} starting (duration: {duration}s)")
        await asyncio.sleep(duration)
        print(f"{name} completed")
        return f"Result from {name}"
    except asyncio.CancelledError:
        print(f"{name} was cancelled")
        raise

async def demonstrate_cancellation():
    """Demonstrate task cancellation"""
    print("=== Task Cancellation Demo ===")
    
    # Create a long-running task
    task = asyncio.create_task(long_running_task("LongTask", 5))
    
    # Let it run for 2 seconds, then cancel
    await asyncio.sleep(2)
    task.cancel()
    
    try:
        result = await task
        print(f"Task result: {result}")
    except asyncio.CancelledError:
        print("Task was successfully cancelled")

async def demonstrate_timeout():
    """Demonstrate timeouts"""
    print("\n=== Timeout Demo ===")
    
    try:
        # This will timeout after 3 seconds
        result = await asyncio.wait_for(
            long_running_task("TimeoutTask", 5), 
            timeout=3.0
        )
        print(f"Task completed: {result}")
    except asyncio.TimeoutError:
        print("Task timed out after 3 seconds")

async def main():
    await demonstrate_cancellation()
    await demonstrate_timeout()

if __name__ == "__main__":
    asyncio.run(main())
```

## Async Context Managers and Iterators

### Async Context Managers

```python
import asyncio
import aiofiles  # pip install aiofiles

class AsyncResource:
    """Example async context manager"""
    
    def __init__(self, name):
        self.name = name
    
    async def __aenter__(self):
        print(f"Acquiring resource: {self.name}")
        await asyncio.sleep(0.1)  # Simulate async setup
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing resource: {self.name}")
        await asyncio.sleep(0.1)  # Simulate async cleanup
    
    async def do_work(self):
        print(f"Working with resource: {self.name}")
        await asyncio.sleep(1)
        return f"Work completed with {self.name}"

async def demonstrate_async_context_manager():
    """Demonstrate async context managers"""
    print("=== Async Context Manager Demo ===")
    
    async with AsyncResource("Database") as resource:
        result = await resource.do_work()
        print(result)
    
    # Multiple async context managers
    async with AsyncResource("Cache") as cache, \
               AsyncResource("Logger") as logger:
        await cache.do_work()
        await logger.do_work()

# Example with file operations
async def demonstrate_async_file_operations():
    """Demonstrate async file operations"""
    print("\n=== Async File Operations Demo ===")
    
    # Write to file asynchronously
    async with aiofiles.open('async_example.txt', 'w') as f:
        await f.write("Hello from async file operations!\n")
        await f.write("This is written asynchronously.\n")
    
    # Read from file asynchronously
    async with aiofiles.open('async_example.txt', 'r') as f:
        content = await f.read()
        print(f"File content:\n{content}")

if __name__ == "__main__":
    asyncio.run(demonstrate_async_context_manager())
    # asyncio.run(demonstrate_async_file_operations())  # Requires aiofiles
```

### Async Iterators and Generators

```python
import asyncio
import random

class AsyncRange:
    """Async iterator that yields numbers with delays"""
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.start >= self.stop:
            raise StopAsyncIteration
        
        current = self.start
        self.start += 1
        
        # Simulate async work
        await asyncio.sleep(0.1)
        return current

async def async_generator(n):
    """Async generator function"""
    for i in range(n):
        await asyncio.sleep(0.1)  # Simulate async work
        yield f"Item {i}"

async def demonstrate_async_iteration():
    """Demonstrate async iteration"""
    print("=== Async Iterator Demo ===")
    
    # Using async iterator
    async for number in AsyncRange(1, 6):
        print(f"Got number: {number}")
    
    print("\n=== Async Generator Demo ===")
    
    # Using async generator
    async for item in async_generator(5):
        print(f"Generated: {item}")

if __name__ == "__main__":
    asyncio.run(demonstrate_async_iteration())
```

## Synchronization Primitives

### Async Locks and Semaphores

```python
import asyncio
import random

# Shared resource
shared_counter = 0

async def worker_with_lock(lock, worker_id, iterations):
    """Worker that uses async lock"""
    global shared_counter
    
    for i in range(iterations):
        async with lock:
            # Critical section
            current = shared_counter
            await asyncio.sleep(0.01)  # Simulate work
            shared_counter = current + 1
            print(f"Worker {worker_id}: Counter = {shared_counter}")

async def demonstrate_async_lock():
    """Demonstrate async lock"""
    print("=== Async Lock Demo ===")
    global shared_counter
    shared_counter = 0
    
    lock = asyncio.Lock()
    
    # Create multiple workers
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker_with_lock(lock, i, 5))
        tasks.append(task)
    
    await asyncio.gather(*tasks)
    print(f"Final counter value: {shared_counter}")

async def limited_resource_worker(semaphore, worker_id):
    """Worker that uses semaphore to limit concurrent access"""
    async with semaphore:
        print(f"Worker {worker_id} accessing limited resource")
        await asyncio.sleep(random.uniform(1, 2))
        print(f"Worker {worker_id} releasing limited resource")

async def demonstrate_async_semaphore():
    """Demonstrate async semaphore"""
    print("\n=== Async Semaphore Demo ===")
    
    # Allow only 2 concurrent accesses
    semaphore = asyncio.Semaphore(2)
    
    # Create 5 workers
    tasks = []
    for i in range(5):
        task = asyncio.create_task(limited_resource_worker(semaphore, i))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

async def main():
    await demonstrate_async_lock()
    await demonstrate_async_semaphore()

if __name__ == "__main__":
    asyncio.run(main())
```

### Async Queues

```python
import asyncio
import random

async def producer(queue, items, producer_id):
    """Async producer that puts items in queue"""
    for item in items:
        await asyncio.sleep(random.uniform(0.1, 0.3))
        await queue.put(f"Item-{item}-from-Producer-{producer_id}")
        print(f"Producer {producer_id} produced: Item-{item}")
    
    # Signal completion
    await queue.put(None)

async def consumer(queue, consumer_id):
    """Async consumer that gets items from queue"""
    while True:
        item = await queue.get()
        
        if item is None:
            # Re-queue sentinel for other consumers
            await queue.put(None)
            break
        
        print(f"Consumer {consumer_id} processing: {item}")
        await asyncio.sleep(random.uniform(0.2, 0.4))
        queue.task_done()

async def demonstrate_async_queue():
    """Demonstrate async queue for producer-consumer pattern"""
    print("=== Async Queue Demo ===")
    
    # Create queue
    queue = asyncio.Queue(maxsize=3)
    
    # Create tasks
    tasks = []
    
    # Producer tasks
    for i in range(2):
        items = list(range(1, 6))  # Items 1-5
        task = asyncio.create_task(producer(queue, items, i))
        tasks.append(task)
    
    # Consumer tasks
    for i in range(3):
        task = asyncio.create_task(consumer(queue, i))
        tasks.append(task)
    
    # Wait for all tasks
    await asyncio.gather(*tasks)
    
    print("All producers and consumers finished")

if __name__ == "__main__":
    asyncio.run(demonstrate_async_queue())
```

## Real-World Examples

### HTTP Client with aiohttp

```python
import asyncio
import aiohttp  # pip install aiohttp
import time

async def fetch_url(session, url):
    """Fetch a single URL"""
    try:
        async with session.get(url) as response:
            content = await response.text()
            return {
                'url': url,
                'status': response.status,
                'length': len(content)
            }
    except Exception as e:
        return {
            'url': url,
            'status': None,
            'error': str(e)
        }

async def fetch_multiple_urls(urls):
    """Fetch multiple URLs concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

async def demonstrate_http_client():
    """Demonstrate async HTTP client"""
    print("=== Async HTTP Client Demo ===")
    
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/status/200",
        "https://httpbin.org/json",
        "https://httpbin.org/headers"
    ]
    
    start_time = time.time()
    results = await fetch_multiple_urls(urls)
    end_time = time.time()
    
    print(f"Fetched {len(urls)} URLs in {end_time - start_time:.2f} seconds")
    
    for result in results:
        if 'error' in result:
            print(f"  {result['url']}: ERROR - {result['error']}")
        else:
            print(f"  {result['url']}: {result['status']} ({result['length']} bytes)")

# Note: This requires aiohttp to be installed
# if __name__ == "__main__":
#     asyncio.run(demonstrate_http_client())
```

### Async Web Server

```python
import asyncio
from aiohttp import web  # pip install aiohttp

async def hello_handler(request):
    """Simple hello world handler"""
    name = request.query.get('name', 'World')
    await asyncio.sleep(0.1)  # Simulate some async work
    return web.Response(text=f"Hello, {name}!")

async def slow_handler(request):
    """Handler that simulates slow processing"""
    delay = int(request.query.get('delay', 1))
    await asyncio.sleep(delay)
    return web.Response(text=f"Processed after {delay} seconds")

async def json_handler(request):
    """Handler that returns JSON"""
    data = {
        'message': 'Hello from async server',
        'timestamp': time.time(),
        'method': request.method,
        'path': request.path
    }
    return web.json_response(data)

def create_app():
    """Create and configure the web application"""
    app = web.Application()
    
    # Add routes
    app.router.add_get('/', hello_handler)
    app.router.add_get('/slow', slow_handler)
    app.router.add_get('/json', json_handler)
    
    return app

async def run_server():
    """Run the async web server"""
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    
    print("Server started at http://localhost:8080")
    print("Try these endpoints:")
    print("  http://localhost:8080/")
    print("  http://localhost:8080/?name=Alice")
    print("  http://localhost:8080/slow?delay=3")
    print("  http://localhost:8080/json")
    
    # Keep the server running
    try:
        await asyncio.Future()  # Run forever
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        await runner.cleanup()

# Note: This requires aiohttp to be installed
# if __name__ == "__main__":
#     asyncio.run(run_server())
```

## Best Practices

### 1. Always Use async/await Consistently

```python
# Good: Consistent async/await usage
async def good_example():
    result1 = await async_operation1()
    result2 = await async_operation2(result1)
    return result2

# Bad: Mixing sync and async incorrectly
async def bad_example():
    result1 = async_operation1()  # Missing await!
    result2 = await async_operation2(result1)  # Will fail
    return result2
```

### 2. Use asyncio.gather() for Concurrent Operations

```python
# Good: Concurrent execution
async def concurrent_operations():
    results = await asyncio.gather(
        fetch_data("source1"),
        fetch_data("source2"),
        fetch_data("source3")
    )
    return results

# Less efficient: Sequential execution
async def sequential_operations():
    results = []
    results.append(await fetch_data("source1"))
    results.append(await fetch_data("source2"))
    results.append(await fetch_data("source3"))
    return results
```

### 3. Handle Exceptions Properly

```python
async def robust_async_function():
    tasks = [
        asyncio.create_task(risky_operation(i))
        for i in range(5)
    ]
    
    results = []
    for task in asyncio.as_completed(tasks):
        try:
            result = await task
            results.append(result)
        except Exception as e:
            print(f"Task failed: {e}")
            results.append(None)
    
    return results
```

### 4. Use Proper Resource Management

```python
# Good: Proper resource cleanup
async def good_resource_usage():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://example.com') as response:
            return await response.text()

# Bad: Resource leaks
async def bad_resource_usage():
    session = aiohttp.ClientSession()
    response = await session.get('http://example.com')
    return await response.text()
    # Session and response not properly closed!
```

## Common Pitfalls

### 1. Forgetting await

```python
# Wrong: Missing await
async def wrong_way():
    result = async_function()  # This returns a coroutine, not the result!
    return result

# Correct: Using await
async def correct_way():
    result = await async_function()  # This waits for the result
    return result
```

### 2. Using Blocking Operations in Async Code

```python
import time

# Wrong: Blocking the event loop
async def blocking_async():
    time.sleep(1)  # This blocks the entire event loop!
    return "Done"

# Correct: Using async alternatives
async def non_blocking_async():
    await asyncio.sleep(1)  # This doesn't block the event loop
    return "Done"
```

### 3. Not Handling CancelledError

```python
# Good: Proper cancellation handling
async def cancellable_task():
    try:
        await long_running_operation()
    except asyncio.CancelledError:
        # Clean up resources
        await cleanup_resources()
        raise  # Re-raise the cancellation
```

## Performance Considerations

### Event Loop Optimization

```python
import asyncio
import time

async def measure_performance():
    """Measure async performance"""
    
    # Test concurrent vs sequential
    async def io_task(delay):
        await asyncio.sleep(delay)
        return delay
    
    delays = [0.1, 0.2, 0.1, 0.3, 0.1]
    
    # Sequential
    start = time.time()
    sequential_results = []
    for delay in delays:
        result = await io_task(delay)
        sequential_results.append(result)
    sequential_time = time.time() - start
    
    # Concurrent
    start = time.time()
    concurrent_results = await asyncio.gather(*[io_task(delay) for delay in delays])
    concurrent_time = time.time() - start
    
    print(f"Sequential: {sequential_time:.2f}s")
    print(f"Concurrent: {concurrent_time:.2f}s")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")

if __name__ == "__main__":
    asyncio.run(measure_performance())
```

## Summary

Asyncio provides powerful tools for asynchronous programming in Python. Key takeaways:

1. **Use asyncio for I/O-bound, high-concurrency applications**
2. **Always use async/await consistently** throughout your async code
3. **Leverage asyncio.gather() and asyncio.create_task()** for concurrent execution
4. **Use async context managers and proper resource management**
5. **Handle exceptions and cancellations properly**
6. **Avoid blocking operations** in async code
7. **Consider asyncio for applications that need to handle many concurrent connections**

In the next lesson, we'll explore common concurrency patterns and how to choose the right approach for different scenarios.