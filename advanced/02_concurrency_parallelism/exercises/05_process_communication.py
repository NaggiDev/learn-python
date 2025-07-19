"""
Exercise 5: Process Communication and Synchronization

Learn how to communicate between processes and synchronize their execution.

Instructions:
1. Complete the functions and classes below
2. Implement various inter-process communication mechanisms
3. Understand shared memory and synchronization primitives
"""

import multiprocessing
import time
import random
import os


def demonstrate_queue_communication():
    """Demonstrate process communication using Queue"""
    print("=== Queue Communication Demo ===")
    
    def producer(queue, items, producer_id):
        """
        TODO: Implement a producer that:
        1. Puts each item from the items list into the queue
        2. Prints "Producer {producer_id} produced: {item}"
        3. Sleeps for a random time (0.1-0.3 seconds) between items
        4. Puts None into the queue to signal completion
        """
        # Your code here
        pass
    
    def consumer(queue, consumer_id):
        """
        TODO: Implement a consumer that:
        1. Gets items from the queue in a loop
        2. Breaks the loop when it receives None
        3. Re-queues None for other consumers
        4. Prints "Consumer {consumer_id} consumed: {item}"
        5. Sleeps for a random time (0.2-0.4 seconds) after processing
        """
        # Your code here
        pass
    
    # TODO: Create a multiprocessing Queue
    # Create 1 producer process with items [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Create 2 consumer processes
    # Start all processes and wait for completion
    
    # Your code here


def demonstrate_pipe_communication():
    """Demonstrate process communication using Pipe"""
    print("\n=== Pipe Communication Demo ===")
    
    def sender(conn, messages):
        """
        TODO: Implement a sender that:
        1. Sends each message through the connection
        2. Prints "Sent: {message}"
        3. Sleeps for 0.5 seconds between messages
        4. Sends "DONE" to signal completion
        5. Closes the connection
        """
        # Your code here
        pass
    
    def receiver(conn):
        """
        TODO: Implement a receiver that:
        1. Receives messages from the connection in a loop
        2. Breaks when it receives "DONE"
        3. Prints "Received: {message}"
        4. Closes the connection
        """
        # Your code here
        pass
    
    # TODO: Create a pipe using multiprocessing.Pipe()
    # Create sender and receiver processes
    # Use messages: ["Hello", "from", "multiprocessing", "pipe"]
    # Start both processes and wait for completion
    
    # Your code here


def demonstrate_shared_memory():
    """Demonstrate shared memory using Value and Array"""
    print("\n=== Shared Memory Demo ===")
    
    def worker_shared_memory(shared_value, shared_array, worker_id, iterations):
        """
        TODO: Implement a worker that:
        1. Performs {iterations} iterations
        2. In each iteration:
           - Safely increments shared_value by 1
           - Safely increments shared_array[worker_id] by 1
           - Prints current values
           - Sleeps for 0.1 seconds
        3. Use locks to ensure thread safety
        """
        # Your code here
        pass
    
    # TODO: Create shared memory objects:
    # - shared_value: multiprocessing.Value('i', 0) for integer
    # - shared_array: multiprocessing.Array('i', [0, 0, 0]) for 3 integers
    # Create 3 worker processes, each doing 5 iterations
    # Start all processes and wait for completion
    # Print final values
    
    # Your code here


def demonstrate_manager():
    """Demonstrate Manager for complex shared objects"""
    print("\n=== Manager Demo ===")
    
    def worker_with_manager(shared_dict, shared_list, worker_id):
        """
        TODO: Implement a worker that:
        1. Adds an entry to shared_dict: {f'worker_{worker_id}': f'Process {worker_id} data'}
        2. Appends f'Item from worker {worker_id}' to shared_list
        3. Prints what it added
        4. Sleeps for 1 second
        """
        # Your code here
        pass
    
    # TODO: Use multiprocessing.Manager() context manager
    # Create shared_dict and shared_list using the manager
    # Create 4 worker processes
    # Start all processes and wait for completion
    # Print final shared objects
    
    # Your code here


class SharedCounter:
    """
    TODO: Implement a thread-safe shared counter using multiprocessing primitives.
    
    The class should:
    1. Use multiprocessing.Value for the counter
    2. Use multiprocessing.Lock for synchronization
    3. Provide increment(), decrement(), and get_value() methods
    4. Ensure all operations are thread-safe
    """
    
    def __init__(self, initial_value=0):
        # TODO: Initialize shared value and lock
        pass
    
    def increment(self):
        """TODO: Safely increment the counter"""
        pass
    
    def decrement(self):
        """TODO: Safely decrement the counter"""
        pass
    
    def get_value(self):
        """TODO: Safely get the current value"""
        pass


def demonstrate_shared_counter():
    """Demonstrate the SharedCounter class"""
    print("\n=== Shared Counter Demo ===")
    
    def counter_worker(counter, worker_id, operations):
        """
        TODO: Implement a worker that:
        1. Performs random increment/decrement operations
        2. Does {operations} total operations
        3. Prints each operation and current counter value
        4. Sleeps briefly between operations
        """
        # Your code here
        pass
    
    # TODO: Create a SharedCounter instance
    # Create 3 worker processes, each doing 5 operations
    # Start all processes and wait for completion
    # Print final counter value
    
    # Your code here


def demonstrate_process_synchronization():
    """Demonstrate process synchronization using Lock and Semaphore"""
    print("\n=== Process Synchronization Demo ===")
    
    def critical_section_worker(lock, shared_resource, worker_id):
        """
        TODO: Implement a worker that:
        1. Uses the lock to safely access shared_resource
        2. Reads the current value
        3. Sleeps for 0.2 seconds (simulate work)
        4. Increments the value
        5. Prints the operation
        6. Does this 3 times
        """
        # Your code here
        pass
    
    def limited_resource_worker(semaphore, worker_id):
        """
        TODO: Implement a worker that:
        1. Uses semaphore to limit concurrent access
        2. Prints "Worker {worker_id} accessing limited resource"
        3. Sleeps for 1-2 seconds (simulate resource usage)
        4. Prints "Worker {worker_id} releasing limited resource"
        """
        # Your code here
        pass
    
    # Test Lock
    print("Testing Lock:")
    # TODO: Create shared_resource (Value) and lock
    # Create 3 processes using critical_section_worker
    # Start and wait for completion
    
    # Your code here
    
    # Test Semaphore
    print("\nTesting Semaphore (max 2 concurrent):")
    # TODO: Create semaphore with value 2
    # Create 5 processes using limited_resource_worker
    # Start and wait for completion
    
    # Your code here


class ProducerConsumerBuffer:
    """
    TODO: Implement a producer-consumer buffer using multiprocessing primitives.
    
    Features to implement:
    1. Fixed-size buffer using multiprocessing.Array
    2. Synchronization using multiprocessing.Condition
    3. Thread-safe put() and get() operations
    4. Proper blocking when buffer is full/empty
    """
    
    def __init__(self, size=5):
        # TODO: Initialize buffer, condition, and tracking variables
        pass
    
    def put(self, item):
        """
        TODO: Add item to buffer
        Block if buffer is full
        Notify consumers when item is added
        """
        pass
    
    def get(self):
        """
        TODO: Remove and return item from buffer
        Block if buffer is empty
        Notify producers when item is removed
        """
        pass
    
    def size(self):
        """TODO: Return current buffer size (thread-safe)"""
        pass


def demonstrate_producer_consumer():
    """Demonstrate producer-consumer pattern with custom buffer"""
    print("\n=== Producer-Consumer Buffer Demo ===")
    
    def producer(buffer, items, producer_id):
        """TODO: Produce items and put them in buffer"""
        # Your code here
        pass
    
    def consumer(buffer, num_items, consumer_id):
        """TODO: Consume items from buffer"""
        # Your code here
        pass
    
    # TODO: Create ProducerConsumerBuffer with size 3
    # Create 2 producers (each producing 5 items)
    # Create 2 consumers (each consuming 5 items)
    # Start all processes and wait for completion
    
    # Your code here


if __name__ == "__main__":
    print("Starting process communication demonstrations...")
    
    demonstrate_queue_communication()
    demonstrate_pipe_communication()
    demonstrate_shared_memory()
    demonstrate_manager()
    demonstrate_shared_counter()
    demonstrate_process_synchronization()
    demonstrate_producer_consumer()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. Queue is excellent for producer-consumer patterns")
    print("2. Pipe provides bidirectional communication between two processes")
    print("3. Value and Array provide simple shared memory")
    print("4. Manager enables sharing of complex Python objects")
    print("5. Locks and semaphores work similarly to threading but for processes")
    print("6. Always use synchronization when accessing shared resources")