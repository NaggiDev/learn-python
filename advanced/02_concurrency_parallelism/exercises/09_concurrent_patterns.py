"""
Exercise 9: Concurrent Execution Patterns

Learn common patterns for concurrent programming and when to apply them.

Instructions:
1. Complete the pattern implementations below
2. Compare different approaches for the same problem
3. Understand when to use each concurrency model
"""

import threading
import multiprocessing
import asyncio
import queue
import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from typing import List, Callable, Any


def cpu_intensive_task(n: int) -> int:
    """CPU-intensive task for testing"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return sum(1 for i in range(2, n) if is_prime(i))


def io_simulation_task(task_id: int, delay: float) -> str:
    """I/O simulation task for testing"""
    time.sleep(delay)
    return f"Task {task_id} completed after {delay:.2f}s"


async def async_io_task(task_id: int, delay: float) -> str:
    """Async I/O task for testing"""
    await asyncio.sleep(delay)
    return f"Async task {task_id} completed after {delay:.2f}s"


class ProducerConsumerSystem:
    """
    TODO: Implement a producer-consumer system using threading.
    
    The system should:
    1. Support multiple producers and consumers
    2. Use a bounded queue for communication
    3. Handle graceful shutdown
    4. Track statistics (items produced/consumed)
    """
    
    def __init__(self, buffer_size=10):
        # TODO: Initialize queue, shutdown event, and statistics
        pass
    
    def producer(self, producer_id: int, item_count: int):
        """
        TODO: Producer that generates items
        1. Generate {item_count} items
        2. Put items in the queue with format "Item-{i}-from-Producer-{producer_id}"
        3. Add random delays between items (0.1-0.3 seconds)
        4. Update statistics
        """
        pass
    
    def consumer(self, consumer_id: int):
        """
        TODO: Consumer that processes items
        1. Continuously get items from queue
        2. Process items (print and add delay 0.2-0.4 seconds)
        3. Stop when shutdown is signaled and queue is empty
        4. Update statistics
        """
        pass
    
    def run_system(self, num_producers=2, num_consumers=3, items_per_producer=5):
        """
        TODO: Run the producer-consumer system
        1. Start all producer and consumer threads
        2. Wait for producers to finish
        3. Signal shutdown to consumers
        4. Wait for consumers to finish
        5. Print statistics
        """
        pass


def demonstrate_producer_consumer():
    """Demonstrate the producer-consumer pattern"""
    print("=== Producer-Consumer Pattern Demo ===")
    
    # TODO: Create and run a ProducerConsumerSystem
    # Use 2 producers, 3 consumers, 5 items per producer
    
    # Your code here


class WorkerPoolManager:
    """
    TODO: Implement a custom worker pool manager.
    
    The manager should:
    1. Maintain a fixed number of worker threads
    2. Accept tasks through a queue
    3. Return results through another queue
    4. Handle task failures gracefully
    5. Support different types of tasks
    """
    
    def __init__(self, num_workers=4):
        # TODO: Initialize queues, workers, and shutdown mechanism
        pass
    
    def worker(self, worker_id: int):
        """
        TODO: Worker function that processes tasks
        1. Get tasks from task queue
        2. Execute task function with arguments
        3. Put result in result queue
        4. Handle exceptions gracefully
        """
        pass
    
    def start_workers(self):
        """TODO: Start all worker threads"""
        pass
    
    def submit_task(self, func: Callable, *args, **kwargs) -> str:
        """
        TODO: Submit a task to the worker pool
        Return a task ID for tracking
        """
        pass
    
    def get_result(self, timeout=None):
        """
        TODO: Get a result from the result queue
        Return (task_id, status, result/error)
        """
        pass
    
    def shutdown(self):
        """TODO: Shutdown all workers gracefully"""
        pass


def demonstrate_worker_pool():
    """Demonstrate the worker pool pattern"""
    print("\n=== Worker Pool Pattern Demo ===")
    
    # TODO: Create a WorkerPoolManager with 3 workers
    # Submit 10 different tasks (mix of CPU and I/O tasks)
    # Collect and print results
    # Shutdown the pool
    
    # Your code here


class PipelineProcessor:
    """
    TODO: Implement a data processing pipeline.
    
    The pipeline should:
    1. Support multiple processing stages
    2. Each stage can have multiple workers
    3. Data flows from one stage to the next
    4. Handle backpressure (slow stages don't overwhelm fast ones)
    """
    
    def __init__(self):
        # TODO: Initialize pipeline stages
        pass
    
    def add_stage(self, name: str, process_func: Callable, num_workers=2):
        """
        TODO: Add a processing stage to the pipeline
        Each stage should have its own input/output queues and workers
        """
        pass
    
    def start_pipeline(self):
        """TODO: Start all pipeline stages"""
        pass
    
    def feed_data(self, data_items: List[Any]):
        """TODO: Feed data into the first stage of the pipeline"""
        pass
    
    def get_results(self, timeout=1) -> List[Any]:
        """TODO: Get processed results from the final stage"""
        pass
    
    def stop_pipeline(self):
        """TODO: Stop all pipeline stages gracefully"""
        pass


def stage1_validator(data):
    """Pipeline stage 1: Validate and clean data"""
    time.sleep(0.05)  # Simulate processing
    if isinstance(data, (int, float)) and data > 0:
        return f"valid_{data}"
    return None  # Invalid data


def stage2_transformer(data):
    """Pipeline stage 2: Transform data"""
    time.sleep(0.1)  # Simulate processing
    if data and data.startswith("valid_"):
        number = float(data.split("_")[1])
        return f"transformed_{number * 2}"
    return None


def stage3_aggregator(data):
    """Pipeline stage 3: Aggregate results"""
    time.sleep(0.03)  # Simulate processing
    if data and data.startswith("transformed_"):
        return f"final_{data}"
    return None


def demonstrate_pipeline():
    """Demonstrate the pipeline pattern"""
    print("\n=== Pipeline Pattern Demo ===")
    
    # TODO: Create a PipelineProcessor
    # Add three stages using the functions above
    # Feed test data: [1, 2, -1, 3.5, "invalid", 4, 0, 5.5]
    # Start pipeline, wait for processing, get results
    # Stop pipeline
    
    # Your code here


class ConcurrencyComparator:
    """
    TODO: Compare different concurrency approaches for the same task.
    
    Implement methods to run the same workload using:
    1. Sequential processing
    2. Threading
    3. Multiprocessing
    4. Asyncio (for I/O tasks)
    """
    
    def __init__(self):
        self.results = {}
    
    def run_sequential(self, tasks: List[tuple], task_type="cpu"):
        """
        TODO: Run tasks sequentially
        tasks: List of (function, args) tuples
        Return: (results, execution_time)
        """
        pass
    
    def run_threading(self, tasks: List[tuple], max_workers=4):
        """
        TODO: Run tasks using ThreadPoolExecutor
        Return: (results, execution_time)
        """
        pass
    
    def run_multiprocessing(self, tasks: List[tuple], max_workers=4):
        """
        TODO: Run tasks using ProcessPoolExecutor
        Return: (results, execution_time)
        """
        pass
    
    async def run_asyncio(self, async_tasks: List[tuple]):
        """
        TODO: Run async tasks using asyncio.gather()
        async_tasks: List of (async_function, args) tuples
        Return: (results, execution_time)
        """
        pass
    
    def compare_approaches(self, tasks: List[tuple], task_type="cpu"):
        """
        TODO: Compare all approaches and print results
        Show execution times and speedup factors
        """
        pass


def demonstrate_concurrency_comparison():
    """Demonstrate comparison of different concurrency approaches"""
    print("\n=== Concurrency Approach Comparison ===")
    
    comparator = ConcurrencyComparator()
    
    # Test with CPU-bound tasks
    print("CPU-bound tasks:")
    cpu_tasks = [(cpu_intensive_task, (5000 + i * 1000,)) for i in range(6)]
    # TODO: Use comparator to compare approaches for CPU tasks
    
    # Test with I/O-bound tasks  
    print("\nI/O-bound tasks:")
    io_tasks = [(io_simulation_task, (i, random.uniform(0.5, 1.5))) for i in range(8)]
    # TODO: Use comparator to compare approaches for I/O tasks
    
    # Test with async I/O tasks
    print("\nAsync I/O tasks:")
    async_tasks = [(async_io_task, (i, random.uniform(0.5, 1.5))) for i in range(8)]
    # TODO: Use comparator to test asyncio approach
    
    # Your code here


class ResourcePool:
    """
    TODO: Implement a generic resource pool.
    
    The pool should:
    1. Create resources on demand up to a maximum
    2. Reuse resources when available
    3. Provide context manager interface
    4. Handle resource cleanup
    """
    
    def __init__(self, create_func: Callable, destroy_func: Callable = None, max_size=5):
        # TODO: Initialize pool with creation/destruction functions
        pass
    
    def get_resource(self, timeout=None):
        """TODO: Get a resource from the pool"""
        pass
    
    def return_resource(self, resource):
        """TODO: Return a resource to the pool"""
        pass
    
    def __enter__(self):
        """TODO: Context manager entry"""
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """TODO: Context manager exit"""
        pass
    
    def cleanup(self):
        """TODO: Clean up all resources"""
        pass


class MockDatabaseConnection:
    """Mock database connection for testing resource pool"""
    
    def __init__(self, connection_id):
        self.id = connection_id
        self.queries_executed = 0
        print(f"Created DB connection {self.id}")
    
    def execute_query(self, query):
        """Execute a database query"""
        time.sleep(0.1)  # Simulate query execution
        self.queries_executed += 1
        return f"Query '{query}' executed on connection {self.id}"
    
    def close(self):
        """Close the database connection"""
        print(f"Closed DB connection {self.id} (executed {self.queries_executed} queries)")


def create_db_connection():
    """Factory function for creating database connections"""
    return MockDatabaseConnection(threading.current_thread().ident)


def destroy_db_connection(conn):
    """Cleanup function for database connections"""
    conn.close()


def demonstrate_resource_pool():
    """Demonstrate the resource pool pattern"""
    print("\n=== Resource Pool Pattern Demo ===")
    
    # TODO: Create a ResourcePool for database connections
    # Use 5 worker threads that each execute 3 queries
    # Each worker should get a connection from the pool, use it, and return it
    # Show that connections are reused
    
    # Your code here


class CircuitBreaker:
    """
    TODO: Implement a circuit breaker pattern for fault tolerance.
    
    The circuit breaker should:
    1. Track failure rate of function calls
    2. Open circuit when failure threshold is exceeded
    3. Allow limited calls in half-open state
    4. Close circuit when calls succeed again
    """
    
    def __init__(self, failure_threshold=3, timeout=5):
        # TODO: Initialize circuit breaker state
        pass
    
    def call(self, func, *args, **kwargs):
        """
        TODO: Execute function with circuit breaker protection
        Raise exception if circuit is open
        Track success/failure and update state
        """
        pass
    
    def _on_success(self):
        """TODO: Handle successful function call"""
        pass
    
    def _on_failure(self):
        """TODO: Handle failed function call"""
        pass


def unreliable_service(fail_rate=0.5):
    """Simulate an unreliable service for testing circuit breaker"""
    if random.random() < fail_rate:
        raise Exception("Service temporarily unavailable")
    return "Service call successful"


def demonstrate_circuit_breaker():
    """Demonstrate the circuit breaker pattern"""
    print("\n=== Circuit Breaker Pattern Demo ===")
    
    # TODO: Create a CircuitBreaker with threshold=3, timeout=3
    # Make 15 calls to unreliable_service with high failure rate
    # Show how circuit breaker opens and eventually closes
    # Add delays between calls to demonstrate timeout behavior
    
    # Your code here


async def main():
    """Main function to run all demonstrations"""
    print("Starting concurrent patterns demonstrations...")
    
    demonstrate_producer_consumer()
    demonstrate_worker_pool()
    demonstrate_pipeline()
    demonstrate_concurrency_comparison()
    demonstrate_resource_pool()
    demonstrate_circuit_breaker()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. Producer-consumer pattern decouples data generation from processing")
    print("2. Worker pools provide efficient task distribution")
    print("3. Pipelines enable staged data processing")
    print("4. Different concurrency models suit different workload types")
    print("5. Resource pools prevent resource exhaustion")
    print("6. Circuit breakers provide fault tolerance")


if __name__ == "__main__":
    # Run the main function
    # Note: Some parts may need to be run separately due to mixing sync/async code
    
    # Run synchronous demonstrations
    demonstrate_producer_consumer()
    demonstrate_worker_pool()
    demonstrate_pipeline()
    demonstrate_concurrency_comparison()
    demonstrate_resource_pool()
    demonstrate_circuit_breaker()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. Producer-consumer pattern decouples data generation from processing")
    print("2. Worker pools provide efficient task distribution")
    print("3. Pipelines enable staged data processing")
    print("4. Different concurrency models suit different workload types")
    print("5. Resource pools prevent resource exhaustion")
    print("6. Circuit breakers provide fault tolerance")