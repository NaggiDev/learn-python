# Concurrent Execution Patterns

## Introduction

This lesson covers common patterns and best practices for concurrent programming in Python. We'll explore when to use threading, multiprocessing, or asyncio, and examine real-world patterns that solve common concurrency challenges.

## Choosing the Right Concurrency Model

### Decision Matrix

| Task Type | Characteristics | Best Choice | Why |
|-----------|----------------|-------------|-----|
| **I/O-bound, Low concurrency** | File operations, database queries | Threading | Simple, low overhead |
| **I/O-bound, High concurrency** | Web scraping, API calls | Asyncio | Excellent scalability |
| **CPU-bound** | Mathematical computations, data processing | Multiprocessing | True parallelism |
| **Mixed workload** | Both I/O and CPU intensive | Hybrid approach | Combine multiple models |

### Performance Comparison Example

```python
import time
import threading
import multiprocessing
import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def io_bound_task(url):
    """I/O-bound task: HTTP request"""
    response = requests.get(url, timeout=5)
    return len(response.content)

def cpu_bound_task(n):
    """CPU-bound task: Prime calculation"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return sum(1 for i in range(2, n) if is_prime(i))

async def async_io_task(session, url):
    """Async I/O-bound task"""
    async with session.get(url) as response:
        content = await response.read()
        return len(content)

def compare_approaches():
    """Compare different concurrency approaches"""
    urls = ["https://httpbin.org/delay/1"] * 5
    numbers = [10000] * 5
    
    # I/O-bound comparison
    print("=== I/O-bound Task Comparison ===")
    
    # Sequential
    start = time.time()
    results = [io_bound_task(url) for url in urls]
    print(f"Sequential I/O: {time.time() - start:.2f}s")
    
    # Threading
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(io_bound_task, urls))
    print(f"Threading I/O: {time.time() - start:.2f}s")
    
    # Asyncio (would require aiohttp)
    # async def async_comparison():
    #     async with aiohttp.ClientSession() as session:
    #         tasks = [async_io_task(session, url) for url in urls]
    #         return await asyncio.gather(*tasks)
    
    # CPU-bound comparison
    print("\n=== CPU-bound Task Comparison ===")
    
    # Sequential
    start = time.time()
    results = [cpu_bound_task(n) for n in numbers]
    print(f"Sequential CPU: {time.time() - start:.2f}s")
    
    # Multiprocessing
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, numbers))
    print(f"Multiprocessing CPU: {time.time() - start:.2f}s")

if __name__ == "__main__":
    compare_approaches()
```

## Common Concurrency Patterns

### 1. Producer-Consumer Pattern

The producer-consumer pattern is fundamental in concurrent programming, where producers generate data and consumers process it.

#### Threading Implementation

```python
import threading
import queue
import time
import random

class ThreadedProducerConsumer:
    def __init__(self, buffer_size=10):
        self.buffer = queue.Queue(maxsize=buffer_size)
        self.shutdown = threading.Event()
    
    def producer(self, producer_id, item_count):
        """Producer that generates items"""
        for i in range(item_count):
            if self.shutdown.is_set():
                break
            
            item = f"Item-{i}-from-Producer-{producer_id}"
            self.buffer.put(item)
            print(f"Produced: {item}")
            time.sleep(random.uniform(0.1, 0.3))
        
        print(f"Producer {producer_id} finished")
    
    def consumer(self, consumer_id):
        """Consumer that processes items"""
        while not self.shutdown.is_set():
            try:
                item = self.buffer.get(timeout=1)
                print(f"Consumer {consumer_id} processing: {item}")
                time.sleep(random.uniform(0.2, 0.5))
                self.buffer.task_done()
            except queue.Empty:
                continue
        
        print(f"Consumer {consumer_id} finished")
    
    def run(self, num_producers=2, num_consumers=3, items_per_producer=5):
        """Run the producer-consumer system"""
        threads = []
        
        # Start producers
        for i in range(num_producers):
            thread = threading.Thread(
                target=self.producer, 
                args=(i, items_per_producer)
            )
            threads.append(thread)
            thread.start()
        
        # Start consumers
        for i in range(num_consumers):
            thread = threading.Thread(target=self.consumer, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Wait for producers to finish
        for thread in threads[:num_producers]:
            thread.join()
        
        # Wait for queue to be empty
        self.buffer.join()
        
        # Shutdown consumers
        self.shutdown.set()
        
        # Wait for consumers to finish
        for thread in threads[num_producers:]:
            thread.join()

# Usage
if __name__ == "__main__":
    system = ThreadedProducerConsumer()
    system.run()
```

#### Asyncio Implementation

```python
import asyncio
import random

class AsyncProducerConsumer:
    def __init__(self, buffer_size=10):
        self.buffer = asyncio.Queue(maxsize=buffer_size)
        self.shutdown = asyncio.Event()
    
    async def producer(self, producer_id, item_count):
        """Async producer that generates items"""
        for i in range(item_count):
            if self.shutdown.is_set():
                break
            
            item = f"Item-{i}-from-Producer-{producer_id}"
            await self.buffer.put(item)
            print(f"Produced: {item}")
            await asyncio.sleep(random.uniform(0.1, 0.3))
        
        print(f"Producer {producer_id} finished")
    
    async def consumer(self, consumer_id):
        """Async consumer that processes items"""
        while not self.shutdown.is_set():
            try:
                item = await asyncio.wait_for(self.buffer.get(), timeout=1.0)
                print(f"Consumer {consumer_id} processing: {item}")
                await asyncio.sleep(random.uniform(0.2, 0.5))
                self.buffer.task_done()
            except asyncio.TimeoutError:
                continue
        
        print(f"Consumer {consumer_id} finished")
    
    async def run(self, num_producers=2, num_consumers=3, items_per_producer=5):
        """Run the async producer-consumer system"""
        tasks = []
        
        # Start producers
        for i in range(num_producers):
            task = asyncio.create_task(self.producer(i, items_per_producer))
            tasks.append(task)
        
        # Start consumers
        for i in range(num_consumers):
            task = asyncio.create_task(self.consumer(i))
            tasks.append(task)
        
        # Wait for producers to finish
        await asyncio.gather(*tasks[:num_producers])
        
        # Wait for queue to be empty
        await self.buffer.join()
        
        # Shutdown consumers
        self.shutdown.set()
        
        # Wait for consumers to finish
        await asyncio.gather(*tasks[num_producers:])

# Usage
async def main():
    system = AsyncProducerConsumer()
    await system.run()

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Worker Pool Pattern

The worker pool pattern maintains a fixed number of workers that process tasks from a shared queue.

```python
import threading
import queue
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

class WorkerPool:
    def __init__(self, num_workers=4):
        self.num_workers = num_workers
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.workers = []
        self.shutdown = threading.Event()
    
    def worker(self, worker_id):
        """Worker function that processes tasks"""
        while not self.shutdown.is_set():
            try:
                task_func, args, kwargs = self.task_queue.get(timeout=1)
                
                if task_func is None:  # Shutdown signal
                    break
                
                try:
                    result = task_func(*args, **kwargs)
                    self.result_queue.put(('success', result))
                except Exception as e:
                    self.result_queue.put(('error', str(e)))
                finally:
                    self.task_queue.task_done()
                    
            except queue.Empty:
                continue
        
        print(f"Worker {worker_id} shutting down")
    
    def start(self):
        """Start all worker threads"""
        for i in range(self.num_workers):
            worker_thread = threading.Thread(target=self.worker, args=(i,))
            worker_thread.start()
            self.workers.append(worker_thread)
    
    def submit_task(self, func, *args, **kwargs):
        """Submit a task to the worker pool"""
        self.task_queue.put((func, args, kwargs))
    
    def get_results(self, timeout=None):
        """Get results from completed tasks"""
        results = []
        while True:
            try:
                result = self.result_queue.get(timeout=timeout)
                results.append(result)
            except queue.Empty:
                break
        return results
    
    def shutdown_pool(self):
        """Shutdown the worker pool"""
        # Send shutdown signals
        for _ in range(self.num_workers):
            self.task_queue.put((None, (), {}))
        
        # Wait for workers to finish
        for worker in self.workers:
            worker.join()

# Example usage
def example_task(n):
    """Example task that calculates factorial"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    time.sleep(0.1)  # Simulate work
    return result

def demonstrate_worker_pool():
    pool = WorkerPool(num_workers=3)
    pool.start()
    
    # Submit tasks
    for i in range(1, 11):
        pool.submit_task(example_task, i)
    
    # Wait for tasks to complete
    pool.task_queue.join()
    
    # Get results
    results = pool.get_results()
    print(f"Completed {len(results)} tasks")
    
    # Shutdown
    pool.shutdown_pool()

if __name__ == "__main__":
    demonstrate_worker_pool()
```

### 3. Pipeline Pattern

The pipeline pattern processes data through a series of stages, where each stage can run concurrently.

```python
import threading
import queue
import time

class PipelineStage:
    def __init__(self, name, process_func, num_workers=2):
        self.name = name
        self.process_func = process_func
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()
        self.workers = []
        self.num_workers = num_workers
        self.shutdown = threading.Event()
    
    def worker(self, worker_id):
        """Worker for this pipeline stage"""
        while not self.shutdown.is_set():
            try:
                item = self.input_queue.get(timeout=1)
                
                if item is None:  # Shutdown signal
                    break
                
                # Process the item
                result = self.process_func(item)
                
                # Pass to next stage
                if self.output_queue:
                    self.output_queue.put(result)
                
                self.input_queue.task_done()
                
            except queue.Empty:
                continue
        
        print(f"Stage {self.name} worker {worker_id} finished")
    
    def start(self):
        """Start workers for this stage"""
        for i in range(self.num_workers):
            worker = threading.Thread(target=self.worker, args=(i,))
            worker.start()
            self.workers.append(worker)
    
    def stop(self):
        """Stop this stage"""
        # Send shutdown signals
        for _ in range(self.num_workers):
            self.input_queue.put(None)
        
        # Wait for workers
        for worker in self.workers:
            worker.join()
    
    def connect_to(self, next_stage):
        """Connect this stage's output to next stage's input"""
        self.output_queue = next_stage.input_queue

class Pipeline:
    def __init__(self):
        self.stages = []
    
    def add_stage(self, stage):
        """Add a stage to the pipeline"""
        if self.stages:
            self.stages[-1].connect_to(stage)
        self.stages.append(stage)
    
    def start(self):
        """Start all stages"""
        for stage in self.stages:
            stage.start()
    
    def stop(self):
        """Stop all stages"""
        for stage in reversed(self.stages):
            stage.stop()
    
    def feed_data(self, data_items):
        """Feed data into the pipeline"""
        if self.stages:
            for item in data_items:
                self.stages[0].input_queue.put(item)
    
    def get_results(self, timeout=1):
        """Get results from the final stage"""
        results = []
        if self.stages:
            final_stage = self.stages[-1]
            while True:
                try:
                    result = final_stage.output_queue.get(timeout=timeout)
                    results.append(result)
                except queue.Empty:
                    break
        return results

# Example pipeline stages
def stage1_process(data):
    """First stage: data validation and cleaning"""
    time.sleep(0.1)  # Simulate processing
    return f"cleaned_{data}"

def stage2_process(data):
    """Second stage: data transformation"""
    time.sleep(0.15)  # Simulate processing
    return f"transformed_{data}"

def stage3_process(data):
    """Third stage: data aggregation"""
    time.sleep(0.1)  # Simulate processing
    return f"aggregated_{data}"

def demonstrate_pipeline():
    # Create pipeline stages
    stage1 = PipelineStage("Cleaning", stage1_process, num_workers=2)
    stage2 = PipelineStage("Transform", stage2_process, num_workers=3)
    stage3 = PipelineStage("Aggregate", stage3_process, num_workers=2)
    
    # Create and configure pipeline
    pipeline = Pipeline()
    pipeline.add_stage(stage1)
    pipeline.add_stage(stage2)
    pipeline.add_stage(stage3)
    
    # Start pipeline
    pipeline.start()
    
    # Feed data
    data_items = [f"data_{i}" for i in range(10)]
    pipeline.feed_data(data_items)
    
    # Wait for processing
    time.sleep(2)
    
    # Get results
    results = pipeline.get_results()
    print(f"Pipeline processed {len(results)} items")
    for result in results:
        print(f"  {result}")
    
    # Stop pipeline
    pipeline.stop()

if __name__ == "__main__":
    demonstrate_pipeline()
```

### 4. Map-Reduce Pattern

The map-reduce pattern is excellent for processing large datasets in parallel.

```python
import multiprocessing
from functools import reduce
import operator
import time

class MapReduceFramework:
    def __init__(self, num_processes=None):
        self.num_processes = num_processes or multiprocessing.cpu_count()
    
    def map_reduce(self, data, map_func, reduce_func, chunk_size=None):
        """Execute map-reduce on the data"""
        
        # Determine chunk size
        if chunk_size is None:
            chunk_size = max(1, len(data) // self.num_processes)
        
        # Split data into chunks
        chunks = [
            data[i:i + chunk_size] 
            for i in range(0, len(data), chunk_size)
        ]
        
        print(f"Processing {len(data)} items in {len(chunks)} chunks")
        
        # Map phase: process chunks in parallel
        with multiprocessing.Pool(processes=self.num_processes) as pool:
            mapped_results = pool.map(map_func, chunks)
        
        # Reduce phase: combine results
        if len(mapped_results) == 1:
            return mapped_results[0]
        
        final_result = reduce(reduce_func, mapped_results)
        return final_result

# Example: Word count using map-reduce
def map_word_count(text_chunk):
    """Map function: count words in a chunk"""
    word_count = {}
    for text in text_chunk:
        words = text.lower().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def reduce_word_count(count1, count2):
    """Reduce function: merge word counts"""
    result = count1.copy()
    for word, count in count2.items():
        result[word] = result.get(word, 0) + count
    return result

# Example: Sum of squares using map-reduce
def map_sum_squares(numbers):
    """Map function: calculate sum of squares for a chunk"""
    return sum(x * x for x in numbers)

def reduce_sum(a, b):
    """Reduce function: add two numbers"""
    return a + b

def demonstrate_map_reduce():
    framework = MapReduceFramework()
    
    # Word count example
    print("=== Word Count Example ===")
    texts = [
        "hello world python programming",
        "python is great for data processing",
        "map reduce pattern is powerful",
        "parallel processing with python",
        "hello python world"
    ] * 1000  # Make it larger for demonstration
    
    start_time = time.time()
    word_counts = framework.map_reduce(
        texts, 
        map_word_count, 
        reduce_word_count
    )
    end_time = time.time()
    
    print(f"Word count completed in {end_time - start_time:.2f} seconds")
    print("Top 5 words:")
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words[:5]:
        print(f"  {word}: {count}")
    
    # Sum of squares example
    print("\n=== Sum of Squares Example ===")
    numbers = list(range(1, 100001))  # 1 to 100,000
    
    start_time = time.time()
    total_sum = framework.map_reduce(
        numbers,
        map_sum_squares,
        reduce_sum
    )
    end_time = time.time()
    
    print(f"Sum of squares: {total_sum}")
    print(f"Completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    demonstrate_map_reduce()
```

### 5. Scatter-Gather Pattern

The scatter-gather pattern distributes work to multiple workers and collects results.

```python
import asyncio
import aiohttp
import time
from typing import List, Dict, Any

class AsyncScatterGather:
    def __init__(self, max_concurrent=10):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
    
    async def scatter_gather(self, tasks: List[tuple], timeout=None):
        """
        Execute tasks concurrently and gather results
        tasks: List of (function, args, kwargs) tuples
        """
        async def execute_task(task_info):
            func, args, kwargs = task_info
            async with self.semaphore:
                try:
                    if asyncio.iscoroutinefunction(func):
                        result = await func(*args, **kwargs)
                    else:
                        result = func(*args, **kwargs)
                    return {'status': 'success', 'result': result}
                except Exception as e:
                    return {'status': 'error', 'error': str(e)}
        
        # Execute all tasks concurrently
        if timeout:
            results = await asyncio.wait_for(
                asyncio.gather(*[execute_task(task) for task in tasks]),
                timeout=timeout
            )
        else:
            results = await asyncio.gather(*[execute_task(task) for task in tasks])
        
        return results

# Example: Fetch multiple URLs
async def fetch_url(session, url):
    """Fetch a single URL"""
    async with session.get(url) as response:
        content = await response.text()
        return {
            'url': url,
            'status_code': response.status,
            'content_length': len(content)
        }

async def demonstrate_scatter_gather():
    """Demonstrate scatter-gather pattern with HTTP requests"""
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/json",
        "https://httpbin.org/headers",
        "https://httpbin.org/user-agent"
    ]
    
    scatter_gather = AsyncScatterGather(max_concurrent=3)
    
    async with aiohttp.ClientSession() as session:
        # Prepare tasks
        tasks = [(fetch_url, (session, url), {}) for url in urls]
        
        start_time = time.time()
        results = await scatter_gather.scatter_gather(tasks, timeout=10)
        end_time = time.time()
        
        print(f"Fetched {len(urls)} URLs in {end_time - start_time:.2f} seconds")
        
        for i, result in enumerate(results):
            if result['status'] == 'success':
                data = result['result']
                print(f"  {data['url']}: {data['status_code']} ({data['content_length']} bytes)")
            else:
                print(f"  {urls[i]}: ERROR - {result['error']}")

# Note: This requires aiohttp
# if __name__ == "__main__":
#     asyncio.run(demonstrate_scatter_gather())
```

## Best Practices and Patterns

### 1. Resource Pool Pattern

```python
import threading
import queue
import contextlib

class ResourcePool:
    """Generic resource pool with automatic cleanup"""
    
    def __init__(self, create_resource, destroy_resource=None, max_size=10):
        self.create_resource = create_resource
        self.destroy_resource = destroy_resource
        self.max_size = max_size
        self.pool = queue.Queue(maxsize=max_size)
        self.created_count = 0
        self.lock = threading.Lock()
    
    def get_resource(self, timeout=None):
        """Get a resource from the pool"""
        try:
            # Try to get existing resource
            return self.pool.get(block=False)
        except queue.Empty:
            # Create new resource if under limit
            with self.lock:
                if self.created_count < self.max_size:
                    resource = self.create_resource()
                    self.created_count += 1
                    return resource
            
            # Wait for available resource
            return self.pool.get(timeout=timeout)
    
    def return_resource(self, resource):
        """Return a resource to the pool"""
        try:
            self.pool.put(resource, block=False)
        except queue.Full:
            # Pool is full, destroy the resource
            if self.destroy_resource:
                self.destroy_resource(resource)
            with self.lock:
                self.created_count -= 1
    
    @contextlib.contextmanager
    def resource(self, timeout=None):
        """Context manager for automatic resource management"""
        resource = self.get_resource(timeout)
        try:
            yield resource
        finally:
            self.return_resource(resource)
    
    def cleanup(self):
        """Clean up all resources in the pool"""
        while not self.pool.empty():
            try:
                resource = self.pool.get(block=False)
                if self.destroy_resource:
                    self.destroy_resource(resource)
            except queue.Empty:
                break

# Example usage with database connections
class MockConnection:
    def __init__(self, connection_id):
        self.id = connection_id
        print(f"Created connection {self.id}")
    
    def execute(self, query):
        return f"Executed '{query}' on connection {self.id}"
    
    def close(self):
        print(f"Closed connection {self.id}")

def create_connection():
    """Factory function to create connections"""
    return MockConnection(threading.current_thread().ident)

def destroy_connection(conn):
    """Cleanup function for connections"""
    conn.close()

def demonstrate_resource_pool():
    # Create connection pool
    pool = ResourcePool(
        create_resource=create_connection,
        destroy_resource=destroy_connection,
        max_size=3
    )
    
    def worker(worker_id):
        for i in range(3):
            with pool.resource() as conn:
                result = conn.execute(f"SELECT * FROM table_{i}")
                print(f"Worker {worker_id}: {result}")
                time.sleep(0.1)
    
    # Create multiple workers
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for completion
    for thread in threads:
        thread.join()
    
    # Cleanup
    pool.cleanup()

if __name__ == "__main__":
    demonstrate_resource_pool()
```

### 2. Circuit Breaker Pattern

```python
import time
import threading
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    """Circuit breaker pattern for fault tolerance"""
    
    def __init__(self, failure_threshold=5, timeout=60, expected_exception=Exception):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
        self.lock = threading.Lock()
    
    def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        with self.lock:
            if self.state == CircuitState.OPEN:
                if time.time() - self.last_failure_time >= self.timeout:
                    self.state = CircuitState.HALF_OPEN
                    print("Circuit breaker: HALF_OPEN")
                else:
                    raise Exception("Circuit breaker is OPEN")
            
            try:
                result = func(*args, **kwargs)
                self._on_success()
                return result
            except self.expected_exception as e:
                self._on_failure()
                raise e
    
    def _on_success(self):
        """Handle successful execution"""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            print("Circuit breaker: CLOSED")
    
    def _on_failure(self):
        """Handle failed execution"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            print(f"Circuit breaker: OPEN (failures: {self.failure_count})")

# Example usage
def unreliable_service(fail_probability=0.3):
    """Simulate an unreliable service"""
    import random
    if random.random() < fail_probability:
        raise Exception("Service temporarily unavailable")
    return "Service response: OK"

def demonstrate_circuit_breaker():
    breaker = CircuitBreaker(failure_threshold=3, timeout=5)
    
    for i in range(20):
        try:
            result = breaker.call(unreliable_service, fail_probability=0.7)
            print(f"Call {i}: {result}")
        except Exception as e:
            print(f"Call {i}: Failed - {e}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    demonstrate_circuit_breaker()
```

## Performance Monitoring and Debugging

### Concurrent Performance Monitor

```python
import time
import threading
import psutil
from collections import defaultdict

class ConcurrencyMonitor:
    """Monitor performance of concurrent operations"""
    
    def __init__(self):
        self.metrics = defaultdict(list)
        self.lock = threading.Lock()
        self.start_time = time.time()
    
    def record_metric(self, name, value):
        """Record a performance metric"""
        with self.lock:
            self.metrics[name].append({
                'timestamp': time.time() - self.start_time,
                'value': value
            })
    
    def get_system_metrics(self):
        """Get current system metrics"""
        return {
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'active_threads': threading.active_count()
        }
    
    def print_summary(self):
        """Print performance summary"""
        print("\n=== Performance Summary ===")
        for metric_name, values in self.metrics.items():
            if values:
                avg_value = sum(v['value'] for v in values) / len(values)
                max_value = max(v['value'] for v in values)
                min_value = min(v['value'] for v in values)
                
                print(f"{metric_name}:")
                print(f"  Count: {len(values)}")
                print(f"  Average: {avg_value:.2f}")
                print(f"  Min: {min_value:.2f}")
                print(f"  Max: {max_value:.2f}")
        
        system_metrics = self.get_system_metrics()
        print(f"\nSystem Metrics:")
        for key, value in system_metrics.items():
            print(f"  {key}: {value}")

# Global monitor instance
monitor = ConcurrencyMonitor()

def monitored_task(task_id, duration):
    """Task that records performance metrics"""
    start_time = time.time()
    
    # Simulate work
    time.sleep(duration)
    
    execution_time = time.time() - start_time
    monitor.record_metric('task_execution_time', execution_time)
    monitor.record_metric('task_completed', 1)
    
    return f"Task {task_id} completed in {execution_time:.2f}s"

def demonstrate_monitoring():
    """Demonstrate performance monitoring"""
    import random
    from concurrent.futures import ThreadPoolExecutor
    
    print("Running monitored concurrent tasks...")
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        
        # Submit tasks with random durations
        for i in range(20):
            duration = random.uniform(0.1, 1.0)
            future = executor.submit(monitored_task, i, duration)
            futures.append(future)
        
        # Wait for completion
        for future in futures:
            result = future.result()
            print(result)
    
    # Print performance summary
    monitor.print_summary()

if __name__ == "__main__":
    demonstrate_monitoring()
```

## Summary

Concurrent execution patterns provide powerful tools for building efficient, scalable applications. Key takeaways:

1. **Choose the right concurrency model** based on your workload characteristics
2. **Use established patterns** like producer-consumer, worker pool, and map-reduce
3. **Implement proper resource management** with pools and context managers
4. **Add fault tolerance** with patterns like circuit breakers
5. **Monitor performance** to identify bottlenecks and optimization opportunities
6. **Consider hybrid approaches** for complex applications with mixed workloads

The next lesson will put these concepts together in a practical mini-project that demonstrates real-world application of concurrency patterns.