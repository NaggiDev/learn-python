# Multiprocessing in Python

## Introduction

Multiprocessing allows your Python program to run multiple processes simultaneously, achieving true parallelism by utilizing multiple CPU cores. Unlike threading, which is limited by Python's Global Interpreter Lock (GIL), multiprocessing can provide significant performance improvements for CPU-bound tasks.

## Key Concepts

### What is Multiprocessing?

**Multiprocessing** creates separate Python interpreter processes, each with its own memory space and Python interpreter. This allows true parallel execution of Python code across multiple CPU cores.

### When to Use Multiprocessing

Multiprocessing is most effective for:
- **CPU-bound tasks**: Mathematical computations, data processing, image/video processing
- **Parallel algorithms**: Tasks that can be divided into independent subtasks
- **Embarrassingly parallel problems**: Tasks with little or no dependency between subtasks

### Multiprocessing vs Threading

| Aspect | Threading | Multiprocessing |
|--------|-----------|-----------------|
| **Parallelism** | Concurrent (GIL limitation) | True parallel execution |
| **Memory** | Shared memory space | Separate memory spaces |
| **Communication** | Direct variable access | IPC mechanisms required |
| **Overhead** | Low | Higher (process creation) |
| **Best for** | I/O-bound tasks | CPU-bound tasks |
| **Debugging** | Easier | More complex |

## Basic Multiprocessing

### Creating and Starting Processes

```python
import multiprocessing
import time
import os

def worker_function(name, duration):
    """A simple worker function that simulates work"""
    process_id = os.getpid()
    print(f"Worker {name} (PID: {process_id}) starting")
    time.sleep(duration)  # Simulate work
    print(f"Worker {name} (PID: {process_id}) finished")

if __name__ == "__main__":
    # Create processes
    process1 = multiprocessing.Process(target=worker_function, args=("A", 2))
    process2 = multiprocessing.Process(target=worker_function, args=("B", 3))
    
    # Start processes
    process1.start()
    process2.start()
    
    # Wait for processes to complete
    process1.join()
    process2.join()
    
    print("All workers finished")
```

### Process Class Inheritance

```python
import multiprocessing
import time
import os

class WorkerProcess(multiprocessing.Process):
    def __init__(self, name, duration):
        super().__init__()
        self.worker_name = name
        self.duration = duration
    
    def run(self):
        process_id = os.getpid()
        print(f"Worker {self.worker_name} (PID: {process_id}) starting")
        time.sleep(self.duration)
        print(f"Worker {self.worker_name} (PID: {process_id}) finished")

if __name__ == "__main__":
    # Create and start processes
    workers = [
        WorkerProcess("Alpha", 2),
        WorkerProcess("Beta", 1),
        WorkerProcess("Gamma", 3)
    ]
    
    for worker in workers:
        worker.start()
    
    for worker in workers:
        worker.join()
```

## Inter-Process Communication (IPC)

### Using Queue for Communication

```python
import multiprocessing
import time
import random

def producer(queue, items):
    """Produce items and put them in the queue"""
    for item in items:
        time.sleep(random.uniform(0.1, 0.3))
        queue.put(item)
        print(f"Produced: {item}")
    
    # Signal completion
    queue.put(None)

def consumer(queue, consumer_id):
    """Consume items from the queue"""
    while True:
        item = queue.get()
        if item is None:
            queue.put(None)  # Re-queue sentinel for other consumers
            break
        
        print(f"Consumer {consumer_id} processing: {item}")
        time.sleep(random.uniform(0.2, 0.4))

if __name__ == "__main__":
    # Create a multiprocessing queue
    work_queue = multiprocessing.Queue()
    items = list(range(10))
    
    # Start producer process
    producer_process = multiprocessing.Process(target=producer, args=(work_queue, items))
    producer_process.start()
    
    # Start multiple consumer processes
    consumers = []
    for i in range(3):
        consumer_process = multiprocessing.Process(target=consumer, args=(work_queue, i))
        consumers.append(consumer_process)
        consumer_process.start()
    
    # Wait for completion
    producer_process.join()
    
    for consumer_process in consumers:
        consumer_process.join()
```

### Using Pipe for Communication

```python
import multiprocessing
import time

def sender(conn, messages):
    """Send messages through the pipe"""
    for message in messages:
        conn.send(message)
        print(f"Sent: {message}")
        time.sleep(0.5)
    
    conn.send("DONE")  # Signal completion
    conn.close()

def receiver(conn):
    """Receive messages from the pipe"""
    while True:
        message = conn.recv()
        if message == "DONE":
            break
        print(f"Received: {message}")
    
    conn.close()

if __name__ == "__main__":
    # Create a pipe
    parent_conn, child_conn = multiprocessing.Pipe()
    
    messages = ["Hello", "World", "From", "Multiprocessing"]
    
    # Start processes
    sender_process = multiprocessing.Process(target=sender, args=(parent_conn, messages))
    receiver_process = multiprocessing.Process(target=receiver, args=(child_conn,))
    
    sender_process.start()
    receiver_process.start()
    
    sender_process.join()
    receiver_process.join()
```

## Shared Memory

### Using Value and Array

```python
import multiprocessing
import time

def worker(shared_value, shared_array, worker_id):
    """Worker that modifies shared memory"""
    for i in range(5):
        # Modify shared value
        with shared_value.get_lock():
            shared_value.value += 1
            print(f"Worker {worker_id}: Incremented shared value to {shared_value.value}")
        
        # Modify shared array
        with shared_array.get_lock():
            shared_array[worker_id] += 1
            print(f"Worker {worker_id}: Array element {worker_id} = {shared_array[worker_id]}")
        
        time.sleep(0.1)

if __name__ == "__main__":
    # Create shared memory objects
    shared_value = multiprocessing.Value('i', 0)  # 'i' for integer
    shared_array = multiprocessing.Array('i', [0, 0, 0])  # Array of 3 integers
    
    # Create processes
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=worker, args=(shared_value, shared_array, i))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print(f"Final shared value: {shared_value.value}")
    print(f"Final shared array: {list(shared_array)}")
```

### Using Manager for Complex Shared Objects

```python
import multiprocessing
import time

def worker(shared_dict, shared_list, worker_id):
    """Worker that modifies shared objects through Manager"""
    shared_dict[f'worker_{worker_id}'] = f'Process {worker_id} was here'
    shared_list.append(f'Item from worker {worker_id}')
    
    print(f"Worker {worker_id} updated shared objects")
    time.sleep(1)

if __name__ == "__main__":
    # Create a manager for shared objects
    with multiprocessing.Manager() as manager:
        shared_dict = manager.dict()
        shared_list = manager.list()
        
        # Create processes
        processes = []
        for i in range(4):
            process = multiprocessing.Process(target=worker, args=(shared_dict, shared_list, i))
            processes.append(process)
            process.start()
        
        for process in processes:
            process.join()
        
        print(f"Final shared dict: {dict(shared_dict)}")
        print(f"Final shared list: {list(shared_list)}")
```

## Process Pools

### Using ProcessPoolExecutor

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import math

def cpu_intensive_task(n):
    """CPU-intensive task: calculate prime numbers up to n"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = [i for i in range(2, n) if is_prime(i)]
    return f"Found {len(primes)} primes up to {n}"

def demonstrate_process_pool():
    """Demonstrate ProcessPoolExecutor for CPU-bound tasks"""
    numbers = [10000, 15000, 20000, 25000, 30000]
    
    # Sequential execution
    print("Sequential execution:")
    start_time = time.time()
    sequential_results = []
    for n in numbers:
        result = cpu_intensive_task(n)
        sequential_results.append(result)
        print(f"  {result}")
    sequential_time = time.time() - start_time
    
    # Parallel execution
    print("\nParallel execution:")
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        future_to_n = {executor.submit(cpu_intensive_task, n): n for n in numbers}
        
        parallel_results = []
        for future in as_completed(future_to_n):
            n = future_to_n[future]
            result = future.result()
            parallel_results.append(result)
            print(f"  {result}")
    
    parallel_time = time.time() - start_time
    
    print(f"\nSequential time: {sequential_time:.2f} seconds")
    print(f"Parallel time: {parallel_time:.2f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")

if __name__ == "__main__":
    demonstrate_process_pool()
```

### Using multiprocessing.Pool

```python
import multiprocessing
import time
import math

def calculate_square(n):
    """Simple CPU task: calculate square"""
    time.sleep(0.1)  # Simulate some work
    return n * n

def calculate_factorial(n):
    """CPU-intensive task: calculate factorial"""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    numbers = list(range(1, 21))  # Numbers 1 to 20
    
    # Using Pool.map()
    print("Using Pool.map():")
    with multiprocessing.Pool(processes=4) as pool:
        start_time = time.time()
        squares = pool.map(calculate_square, numbers)
        end_time = time.time()
        
        print(f"Squares: {squares[:10]}...")  # Show first 10
        print(f"Time taken: {end_time - start_time:.2f} seconds")
    
    # Using Pool.map() with different function
    print("\nUsing Pool.map() for factorials:")
    small_numbers = list(range(1, 11))  # Smaller numbers for factorial
    
    with multiprocessing.Pool(processes=4) as pool:
        start_time = time.time()
        factorials = pool.map(calculate_factorial, small_numbers)
        end_time = time.time()
        
        for i, fact in enumerate(factorials, 1):
            print(f"{i}! = {fact}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
    
    # Using Pool.starmap() for functions with multiple arguments
    print("\nUsing Pool.starmap():")
    def power(base, exponent):
        return base ** exponent
    
    power_args = [(2, 3), (3, 4), (4, 2), (5, 3), (6, 2)]
    
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(power, power_args)
        
        for args, result in zip(power_args, results):
            print(f"{args[0]}^{args[1]} = {result}")
```

## Synchronization in Multiprocessing

### Using Lock

```python
import multiprocessing
import time

def worker_with_lock(lock, shared_resource, worker_id):
    """Worker that uses a lock to access shared resource safely"""
    for i in range(3):
        with lock:
            print(f"Worker {worker_id} acquired lock")
            current_value = shared_resource.value
            time.sleep(0.1)  # Simulate work
            shared_resource.value = current_value + 1
            print(f"Worker {worker_id} incremented value to {shared_resource.value}")
        
        time.sleep(0.1)  # Work outside critical section

if __name__ == "__main__":
    # Create shared resource and lock
    shared_resource = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    
    # Create processes
    processes = []
    for i in range(3):
        process = multiprocessing.Process(
            target=worker_with_lock, 
            args=(lock, shared_resource, i)
        )
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print(f"Final value: {shared_resource.value}")
```

### Using Semaphore

```python
import multiprocessing
import time
import random

def access_limited_resource(semaphore, resource_id, worker_id):
    """Access a limited resource using semaphore"""
    with semaphore:
        print(f"Worker {worker_id} accessing resource {resource_id}")
        time.sleep(random.uniform(1, 3))  # Simulate resource usage
        print(f"Worker {worker_id} releasing resource {resource_id}")

if __name__ == "__main__":
    # Create semaphore that allows 2 concurrent accesses
    semaphore = multiprocessing.Semaphore(2)
    
    # Create processes
    processes = []
    for i in range(6):
        process = multiprocessing.Process(
            target=access_limited_resource,
            args=(semaphore, "Database", i)
        )
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
```

## Advanced Patterns

### Map-Reduce Pattern

```python
import multiprocessing
from functools import reduce
import operator

def map_function(chunk):
    """Map function: process a chunk of data"""
    # Example: count words in a chunk of text
    word_count = {}
    for word in chunk:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def reduce_function(dict1, dict2):
    """Reduce function: combine two dictionaries"""
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

def parallel_word_count(text_data, num_processes=4):
    """Parallel word counting using map-reduce pattern"""
    # Split data into chunks
    chunk_size = len(text_data) // num_processes
    chunks = [
        text_data[i:i + chunk_size] 
        for i in range(0, len(text_data), chunk_size)
    ]
    
    # Map phase: process chunks in parallel
    with multiprocessing.Pool(processes=num_processes) as pool:
        mapped_results = pool.map(map_function, chunks)
    
    # Reduce phase: combine results
    final_result = reduce(reduce_function, mapped_results, {})
    return final_result

if __name__ == "__main__":
    # Sample data
    text_data = [
        "hello", "world", "hello", "python", "world", "multiprocessing",
        "hello", "parallel", "processing", "python", "is", "awesome",
        "multiprocessing", "enables", "parallel", "execution", "python"
    ] * 1000  # Make it larger for demonstration
    
    # Sequential word count
    start_time = time.time()
    sequential_result = {}
    for word in text_data:
        sequential_result[word] = sequential_result.get(word, 0) + 1
    sequential_time = time.time() - start_time
    
    # Parallel word count
    start_time = time.time()
    parallel_result = parallel_word_count(text_data)
    parallel_time = time.time() - start_time
    
    print(f"Sequential time: {sequential_time:.4f} seconds")
    print(f"Parallel time: {parallel_time:.4f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")
    print(f"Results match: {sequential_result == parallel_result}")
```

## Best Practices

### 1. Always Use `if __name__ == "__main__":`

```python
import multiprocessing

def worker():
    print("Worker running")

# This is REQUIRED for multiprocessing on Windows
if __name__ == "__main__":
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()
```

### 2. Minimize Data Transfer Between Processes

```python
# Bad: Passing large data structures
def bad_approach(large_data):
    # Process large_data
    return processed_data

# Good: Process data in chunks or use shared memory
def good_approach(data_chunk):
    # Process smaller chunk
    return processed_chunk
```

### 3. Handle Exceptions Properly

```python
import multiprocessing
import traceback

def worker_with_exception_handling(task_id):
    try:
        # Simulate work that might fail
        if task_id == 3:
            raise ValueError(f"Task {task_id} failed!")
        
        print(f"Task {task_id} completed successfully")
        return f"Result from task {task_id}"
    
    except Exception as e:
        print(f"Task {task_id} failed: {e}")
        traceback.print_exc()
        return None

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        tasks = list(range(1, 6))
        results = pool.map(worker_with_exception_handling, tasks)
        
        print(f"Results: {results}")
```

### 4. Clean Resource Management

```python
import multiprocessing
import atexit

class ResourceManager:
    def __init__(self):
        self.processes = []
    
    def create_process(self, target, args):
        process = multiprocessing.Process(target=target, args=args)
        self.processes.append(process)
        return process
    
    def cleanup(self):
        """Clean up all processes"""
        for process in self.processes:
            if process.is_alive():
                process.terminate()
                process.join(timeout=5)
                if process.is_alive():
                    process.kill()

# Register cleanup function
manager = ResourceManager()
atexit.register(manager.cleanup)
```

## Common Pitfalls

### 1. Forgetting `if __name__ == "__main__":`

This is required on Windows and recommended on all platforms to prevent infinite recursion.

### 2. Sharing Complex Objects Without Manager

```python
# Wrong: This won't work as expected
shared_list = []

def worker(shared_list):
    shared_list.append("item")  # Won't be visible to other processes

# Correct: Use Manager
if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_list = manager.list()
        # Now modifications are visible across processes
```

### 3. Not Handling Process Cleanup

```python
# Bad: Processes might become zombies
process = multiprocessing.Process(target=worker)
process.start()
# Missing process.join()

# Good: Always join processes
process = multiprocessing.Process(target=worker)
process.start()
process.join()  # Wait for completion
```

## Performance Considerations

### CPU Core Utilization

```python
import multiprocessing
import psutil

def get_optimal_process_count():
    """Get optimal number of processes based on CPU cores"""
    cpu_count = multiprocessing.cpu_count()
    print(f"CPU cores: {cpu_count}")
    
    # For CPU-bound tasks, use number of cores
    # For I/O-bound tasks, you might use more
    return cpu_count

def monitor_cpu_usage():
    """Monitor CPU usage during multiprocessing"""
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")

if __name__ == "__main__":
    optimal_processes = get_optimal_process_count()
    print(f"Recommended process count: {optimal_processes}")
```

## Summary

Multiprocessing in Python provides true parallelism for CPU-bound tasks. Key takeaways:

1. **Use multiprocessing for CPU-bound tasks** where you need true parallelism
2. **Processes have separate memory spaces** - use IPC mechanisms for communication
3. **Always include `if __name__ == "__main__":` guard** for cross-platform compatibility
4. **Use ProcessPoolExecutor or Pool** for managing multiple processes efficiently
5. **Be mindful of overhead** - process creation is more expensive than thread creation
6. **Handle exceptions and cleanup properly** to avoid zombie processes

In the next lesson, we'll explore asyncio for asynchronous programming and high-concurrency I/O operations.