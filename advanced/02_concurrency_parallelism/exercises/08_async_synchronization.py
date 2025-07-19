"""
Exercise 8: Async Synchronization and Communication

Learn about synchronization primitives and communication patterns in asyncio.

Instructions:
1. Complete the async functions and classes below
2. Implement various async synchronization mechanisms
3. Understand async queues, locks, and semaphores
"""

import asyncio
import random
import time


# Shared resource for demonstration
shared_resource = {"counter": 0, "data": []}


async def unsafe_worker(worker_id, iterations):
    """
    TODO: Create an unsafe worker that demonstrates race conditions:
    1. Perform {iterations} iterations
    2. In each iteration:
       - Read shared_resource["counter"]
       - Sleep briefly (0.01 seconds)
       - Increment and write back to shared_resource["counter"]
       - Print the worker ID and new counter value
    """
    # Your code here
    pass


async def safe_worker(lock, worker_id, iterations):
    """
    TODO: Create a safe worker that uses async lock:
    1. Perform {iterations} iterations
    2. In each iteration:
       - Acquire the async lock
       - Read, increment, and write back shared_resource["counter"]
       - Print the worker ID and new counter value
       - Release the lock (use async with)
    """
    # Your code here
    pass


async def demonstrate_race_condition():
    """Demonstrate race conditions and their solution"""
    print("=== Race Condition Demo ===")
    
    # Reset shared resource
    shared_resource["counter"] = 0
    
    # TODO: Test unsafe workers (race condition)
    print("Testing unsafe workers (race condition):")
    
    # Create 3 unsafe workers, each doing 5 iterations
    # Run them concurrently and observe the race condition
    
    # Your code here
    
    print(f"Unsafe final counter: {shared_resource['counter']}")
    print(f"Expected: 15, Actual: {shared_resource['counter']}")
    
    # Reset for safe test
    shared_resource["counter"] = 0
    
    # TODO: Test safe workers (with lock)
    print("\nTesting safe workers (with lock):")
    
    # Create an async lock
    # Create 3 safe workers, each doing 5 iterations
    # Run them concurrently with the lock
    
    # Your code here
    
    print(f"Safe final counter: {shared_resource['counter']}")
    print(f"Expected: 15, Actual: {shared_resource['counter']}")


async def limited_resource_worker(semaphore, worker_id, work_time):
    """
    TODO: Create a worker that uses semaphore for limited resource access:
    1. Acquire the semaphore
    2. Print "Worker {worker_id} accessing limited resource"
    3. Sleep for {work_time} seconds
    4. Print "Worker {worker_id} releasing limited resource"
    5. Release the semaphore (use async with)
    """
    # Your code here
    pass


async def demonstrate_semaphore():
    """Demonstrate async semaphore for limiting concurrent access"""
    print("\n=== Async Semaphore Demo ===")
    
    # TODO: Create a semaphore that allows only 2 concurrent accesses
    # Create 6 workers with different work times
    # Run them concurrently and observe that only 2 can access the resource at once
    
    # Your code here


async def producer(queue, items, producer_id):
    """
    TODO: Create an async producer:
    1. For each item in items:
       - Sleep for a random time (0.1-0.3 seconds)
       - Put f"Item-{item}-from-Producer-{producer_id}" into the queue
       - Print what was produced
    2. Put None into the queue to signal completion
    """
    # Your code here
    pass


async def consumer(queue, consumer_id):
    """
    TODO: Create an async consumer:
    1. Loop continuously:
       - Get an item from the queue
       - If item is None, re-queue it for other consumers and break
       - Process the item (print and sleep 0.2-0.4 seconds)
       - Mark the task as done (queue.task_done())
    """
    # Your code here
    pass


async def demonstrate_async_queue():
    """Demonstrate async queue for producer-consumer pattern"""
    print("\n=== Async Queue Demo ===")
    
    # TODO: Create an async queue with maxsize=3
    # Create 2 producers (each producing items 1-5)
    # Create 3 consumers
    # Run all tasks concurrently
    # Wait for the queue to be empty (queue.join())
    
    # Your code here


class AsyncBankAccount:
    """
    TODO: Implement an async thread-safe bank account.
    
    The class should:
    1. Store a balance and use an async lock
    2. Have async deposit() and withdraw() methods
    3. Have async get_balance() method
    4. Prevent overdrafts in withdraw()
    5. Add small async delays to simulate processing time
    """
    
    def __init__(self, initial_balance=0):
        # TODO: Initialize balance and async lock
        pass
    
    async def deposit(self, amount):
        """TODO: Safely deposit amount to balance"""
        pass
    
    async def withdraw(self, amount):
        """TODO: Safely withdraw amount, prevent overdrafts"""
        pass
    
    async def get_balance(self):
        """TODO: Safely return current balance"""
        pass


async def bank_customer(account, customer_id, transactions):
    """
    TODO: Simulate a bank customer performing transactions:
    1. For each transaction in transactions:
       - If transaction > 0, deposit the amount
       - If transaction < 0, try to withdraw the absolute amount
       - Print the transaction and resulting balance
       - Sleep briefly between transactions
    """
    # Your code here
    pass


async def demonstrate_async_bank_account():
    """Demonstrate async bank account with multiple customers"""
    print("\n=== Async Bank Account Demo ===")
    
    # TODO: Create an AsyncBankAccount with initial balance 1000
    # Create 3 customers with different transaction patterns:
    # Customer 1: [100, -50, 200, -30]
    # Customer 2: [-100, 150, -75, 25]  
    # Customer 3: [50, -200, 100, -25]
    # Run all customers concurrently
    # Print final balance
    
    # Your code here


class AsyncEventManager:
    """
    TODO: Implement an async event manager using asyncio.Event.
    
    The class should:
    1. Manage multiple named events
    2. Allow waiting for events to be set
    3. Allow setting and clearing events
    4. Support waiting for multiple events
    """
    
    def __init__(self):
        # TODO: Initialize event storage
        pass
    
    async def wait_for_event(self, event_name):
        """TODO: Wait for a specific event to be set"""
        pass
    
    async def set_event(self, event_name):
        """TODO: Set a specific event"""
        pass
    
    async def clear_event(self, event_name):
        """TODO: Clear a specific event"""
        pass
    
    async def wait_for_all_events(self, event_names):
        """TODO: Wait for all specified events to be set"""
        pass


async def event_waiter(event_manager, event_name, waiter_id):
    """
    TODO: Create a task that waits for an event:
    1. Print "Waiter {waiter_id} waiting for event {event_name}"
    2. Wait for the event
    3. Print "Waiter {waiter_id} received event {event_name}"
    """
    # Your code here
    pass


async def event_setter(event_manager, event_name, delay):
    """
    TODO: Create a task that sets an event after a delay:
    1. Sleep for {delay} seconds
    2. Set the event
    3. Print "Event {event_name} has been set"
    """
    # Your code here
    pass


async def demonstrate_async_events():
    """Demonstrate async event coordination"""
    print("\n=== Async Event Demo ===")
    
    # TODO: Create an AsyncEventManager
    # Create multiple waiters for different events
    # Create setters that set events after different delays
    # Demonstrate event coordination
    
    # Your code here


class AsyncBuffer:
    """
    TODO: Implement an async buffer with condition variables.
    
    The buffer should:
    1. Have a maximum size
    2. Use asyncio.Condition for coordination
    3. Block producers when full
    4. Block consumers when empty
    5. Notify waiting tasks when state changes
    """
    
    def __init__(self, max_size=5):
        # TODO: Initialize buffer, condition, and size tracking
        pass
    
    async def put(self, item):
        """TODO: Put item in buffer, wait if full"""
        pass
    
    async def get(self):
        """TODO: Get item from buffer, wait if empty"""
        pass
    
    async def size(self):
        """TODO: Return current buffer size"""
        pass


async def buffer_producer(buffer, items, producer_id):
    """TODO: Produce items and put them in the buffer"""
    # Your code here
    pass


async def buffer_consumer(buffer, num_items, consumer_id):
    """TODO: Consume items from the buffer"""
    # Your code here
    pass


async def demonstrate_async_buffer():
    """Demonstrate async buffer with condition variables"""
    print("\n=== Async Buffer Demo ===")
    
    # TODO: Create an AsyncBuffer with size 3
    # Create 2 producers and 2 consumers
    # Producers create 5 items each
    # Consumers consume 5 items each
    # Run all tasks concurrently
    
    # Your code here


async def rate_limited_worker(semaphore, worker_id, tasks):
    """
    TODO: Create a rate-limited worker:
    1. For each task in tasks:
       - Acquire semaphore (rate limiting)
       - Process the task (print and sleep)
       - Release semaphore after a delay
    """
    # Your code here
    pass


async def demonstrate_rate_limiting():
    """Demonstrate rate limiting with semaphores"""
    print("\n=== Rate Limiting Demo ===")
    
    # TODO: Create a semaphore that allows 2 operations per second
    # Create 5 workers, each with 3 tasks
    # Observe how the semaphore limits the rate of execution
    
    # Your code here


async def main():
    """Main function to run all demonstrations"""
    print("Starting async synchronization demonstrations...")
    
    await demonstrate_race_condition()
    await demonstrate_semaphore()
    await demonstrate_async_queue()
    await demonstrate_async_bank_account()
    await demonstrate_async_events()
    await demonstrate_async_buffer()
    await demonstrate_rate_limiting()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. Async locks prevent race conditions in async code")
    print("2. Async semaphores limit concurrent access to resources")
    print("3. Async queues enable producer-consumer patterns")
    print("4. Async events coordinate between tasks")
    print("5. Async condition variables provide fine-grained coordination")
    print("6. Rate limiting can be implemented with semaphores and delays")


if __name__ == "__main__":
    asyncio.run(main())