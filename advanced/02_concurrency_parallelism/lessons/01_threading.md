# Threading in Python

## Introduction

Threading allows your Python program to run multiple operations concurrently within a single process. This is particularly useful for I/O-bound tasks where your program spends time waiting for file operations, network requests, or user input.

## Key Concepts

### What is Threading?

A **thread** is a separate flow of execution within a program. Multiple threads can run concurrently, sharing the same memory space and resources of the parent process.

### When to Use Threading

Threading is most effective for:
- **I/O-bound tasks**: File operations, network requests, database queries
- **User interface responsiveness**: Keeping UI responsive while background tasks run
- **Producer-consumer scenarios**: One thread produces data while another consumes it

### The Global Interpreter Lock (GIL)

Python's GIL ensures that only one thread executes Python bytecode at a time. This means:
- Threading doesn't provide true parallelism for CPU-bound tasks
- Threading is excellent for I/O-bound tasks (GIL is released during I/O operations)
- For CPU-bound parallelism, use multiprocessing instead

## Basic Threading

### Creating and Starting Threads

```python
import threading
import time

def worker_function(name, duration):
    """A simple worker function that simulates work"""
    print(f"Worker {name} starting")
    time.sleep(duration)  # Simulate work
    print(f"Worker {name} finished")

# Create threads
thread1 = threading.Thread(target=worker_function, args=("A", 2))
thread2 = threading.Thread(target=worker_function, args=("B", 3))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All workers finished")
```

### Thread Class Inheritance

```python
import threading
import time

class WorkerThread(threading.Thread):
    def __init__(self, name, duration):
        super().__init__()
        self.name = name
        self.duration = duration
    
    def run(self):
        print(f"Worker {self.name} starting")
        time.sleep(self.duration)
        print(f"Worker {self.name} finished")

# Create and start threads
workers = [
    WorkerThread("Alpha", 2),
    WorkerThread("Beta", 1),
    WorkerThread("Gamma", 3)
]

for worker in workers:
    worker.start()

for worker in workers:
    worker.join()
```

## Thread Synchronization

### The Problem: Race Conditions

When multiple threads access shared data, race conditions can occur:

```python
import threading
import time

# Shared resource
counter = 0

def increment_counter():
    global counter
    for _ in range(100000):
        counter += 1  # This is not atomic!

# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")  # May not be 500000!
```

### Solution: Locks

```python
import threading

counter = 0
counter_lock = threading.Lock()

def safe_increment_counter():
    global counter
    for _ in range(100000):
        with counter_lock:  # Acquire lock
            counter += 1    # Critical section
        # Lock automatically released

# Now the counter will be accurate
threads = []
for i in range(5):
    thread = threading.Thread(target=safe_increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")  # Will be 500000
```

## Advanced Synchronization Primitives

### RLock (Reentrant Lock)

```python
import threading

class Counter:
    def __init__(self):
        self._value = 0
        self._lock = threading.RLock()  # Reentrant lock
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def increment_twice(self):
        with self._lock:
            self.increment()  # Can acquire lock again
            self.increment()
    
    @property
    def value(self):
        with self._lock:
            return self._value
```

### Semaphore

```python
import threading
import time

# Limit concurrent access to a resource
semaphore = threading.Semaphore(2)  # Allow 2 concurrent accesses

def access_resource(worker_id):
    with semaphore:
        print(f"Worker {worker_id} accessing resource")
        time.sleep(2)  # Simulate resource usage
        print(f"Worker {worker_id} releasing resource")

# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

### Condition Variables

```python
import threading
import time
import random

class Buffer:
    def __init__(self, size):
        self.buffer = []
        self.size = size
        self.condition = threading.Condition()
    
    def put(self, item):
        with self.condition:
            while len(self.buffer) >= self.size:
                print("Buffer full, producer waiting...")
                self.condition.wait()  # Wait for space
            
            self.buffer.append(item)
            print(f"Produced: {item}")
            self.condition.notify_all()  # Notify consumers
    
    def get(self):
        with self.condition:
            while len(self.buffer) == 0:
                print("Buffer empty, consumer waiting...")
                self.condition.wait()  # Wait for items
            
            item = self.buffer.pop(0)
            print(f"Consumed: {item}")
            self.condition.notify_all()  # Notify producers
            return item

def producer(buffer, items):
    for item in items:
        buffer.put(item)
        time.sleep(random.uniform(0.1, 0.5))

def consumer(buffer, count):
    for _ in range(count):
        buffer.get()
        time.sleep(random.uniform(0.1, 0.5))

# Example usage
buffer = Buffer(3)
items = list(range(10))

producer_thread = threading.Thread(target=producer, args=(buffer, items))
consumer_thread = threading.Thread(target=consumer, args=(buffer, len(items)))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
```

## Thread Communication

### Using Queue

```python
import threading
import queue
import time
import random

def producer(q, items):
    """Produce items and put them in the queue"""
    for item in items:
        time.sleep(random.uniform(0.1, 0.3))
        q.put(item)
        print(f"Produced: {item}")
    
    # Signal completion
    q.put(None)

def consumer(q, consumer_id):
    """Consume items from the queue"""
    while True:
        item = q.get()
        if item is None:
            q.put(None)  # Re-queue sentinel for other consumers
            break
        
        print(f"Consumer {consumer_id} processing: {item}")
        time.sleep(random.uniform(0.2, 0.4))
        q.task_done()

# Create queue and start threads
work_queue = queue.Queue()
items = list(range(10))

# Start producer
producer_thread = threading.Thread(target=producer, args=(work_queue, items))
producer_thread.start()

# Start multiple consumers
consumers = []
for i in range(3):
    consumer_thread = threading.Thread(target=consumer, args=(work_queue, i))
    consumers.append(consumer_thread)
    consumer_thread.start()

# Wait for completion
producer_thread.join()
work_queue.join()  # Wait for all tasks to be processed

# Stop consumers
for consumer_thread in consumers:
    consumer_thread.join()
```

## Thread Pools

### Using ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests

def fetch_url(url):
    """Fetch a URL and return the status code"""
    try:
        response = requests.get(url, timeout=5)
        return f"{url}: {response.status_code}"
    except Exception as e:
        return f"{url}: Error - {e}"

# List of URLs to fetch
urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404"
]

# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit all tasks
    future_to_url = {executor.submit(fetch_url, url): url for url in urls}
    
    # Process completed tasks
    for future in as_completed(future_to_url):
        result = future.result()
        print(result)
```

## Best Practices

### 1. Always Use Context Managers

```python
# Good
with lock:
    # Critical section
    pass

# Avoid
lock.acquire()
try:
    # Critical section
    pass
finally:
    lock.release()
```

### 2. Avoid Shared Mutable State

```python
# Better: Use immutable data and message passing
import threading
import queue

def worker(input_queue, output_queue):
    while True:
        item = input_queue.get()
        if item is None:
            break
        
        # Process item (create new data, don't modify existing)
        result = process_item(item)
        output_queue.put(result)
        input_queue.task_done()
```

### 3. Use Daemon Threads Carefully

```python
import threading
import time

def background_task():
    while True:
        print("Background task running...")
        time.sleep(1)

# Daemon thread will exit when main program exits
daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

# Main program
time.sleep(5)
print("Main program ending")
# Daemon thread will be terminated automatically
```

## Common Pitfalls

### 1. Deadlocks

```python
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print("Thread 1: Acquired lock1")
        time.sleep(0.1)
        with lock2:  # May deadlock if thread2 has lock2
            print("Thread 1: Acquired lock2")

def thread2():
    with lock2:
        print("Thread 2: Acquired lock2")
        time.sleep(0.1)
        with lock1:  # May deadlock if thread1 has lock1
            print("Thread 2: Acquired lock1")

# Solution: Always acquire locks in the same order
def safe_thread1():
    with lock1:
        with lock2:
            print("Safe thread 1: Both locks acquired")

def safe_thread2():
    with lock1:  # Same order as thread1
        with lock2:
            print("Safe thread 2: Both locks acquired")
```

### 2. Resource Leaks

```python
import threading

# Bad: Thread may not be properly cleaned up
def create_worker():
    def worker():
        while True:
            # Do work
            pass
    
    thread = threading.Thread(target=worker)
    thread.start()
    return thread

# Good: Provide a way to stop the thread
class StoppableWorker:
    def __init__(self):
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._work)
    
    def start(self):
        self._thread.start()
    
    def stop(self):
        self._stop_event.set()
        self._thread.join()
    
    def _work(self):
        while not self._stop_event.is_set():
            # Do work
            time.sleep(0.1)
```

## Summary

Threading in Python is powerful for I/O-bound tasks and improving application responsiveness. Key takeaways:

1. **Use threading for I/O-bound tasks**, not CPU-bound tasks (due to GIL)
2. **Always synchronize access to shared data** using locks, semaphores, or queues
3. **Prefer higher-level abstractions** like ThreadPoolExecutor and Queue
4. **Be aware of common pitfalls** like deadlocks and race conditions
5. **Design for thread safety** from the beginning

In the next lesson, we'll explore multiprocessing for true parallelism in CPU-bound tasks.