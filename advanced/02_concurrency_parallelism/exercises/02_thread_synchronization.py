"""
Exercise 2: Thread Synchronization

Learn how to safely share data between threads using synchronization primitives.

Instructions:
1. Complete the functions and classes below
2. Observe the race condition problem and its solution
3. Experiment with different synchronization primitives
"""

import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor


# Global variables for demonstration
unsafe_counter = 0
safe_counter = 0
counter_lock = threading.Lock()


def unsafe_increment():
    """
    TODO: Implement a function that increments unsafe_counter 100,000 times.
    This will demonstrate race conditions.
    """
    global unsafe_counter
    # Your code here
    pass


def safe_increment():
    """
    TODO: Implement a function that safely increments safe_counter 100,000 times
    using the counter_lock to prevent race conditions.
    """
    global safe_counter
    # Your code here
    pass


class BankAccount:
    """
    TODO: Implement a thread-safe bank account class.
    
    The class should:
    1. Store a balance
    2. Have deposit() and withdraw() methods
    3. Use a lock to ensure thread safety
    4. Prevent overdrafts (balance going negative)
    """
    
    def __init__(self, initial_balance=0):
        # TODO: Initialize balance and lock
        pass
    
    def deposit(self, amount):
        """
        TODO: Safely add amount to balance
        Print deposit information
        """
        pass
    
    def withdraw(self, amount):
        """
        TODO: Safely subtract amount from balance
        Prevent overdrafts (return False if insufficient funds)
        Print withdrawal information
        Return True if successful, False otherwise
        """
        pass
    
    def get_balance(self):
        """
        TODO: Safely return the current balance
        """
        pass


class ProducerConsumerBuffer:
    """
    TODO: Implement a thread-safe buffer for producer-consumer pattern.
    
    Use threading.Condition for coordination between producers and consumers.
    """
    
    def __init__(self, max_size=5):
        # TODO: Initialize buffer, condition, and max_size
        pass
    
    def put(self, item):
        """
        TODO: Add item to buffer
        Wait if buffer is full
        Notify consumers when item is added
        """
        pass
    
    def get(self):
        """
        TODO: Remove and return item from buffer
        Wait if buffer is empty
        Notify producers when item is removed
        """
        pass
    
    def size(self):
        """TODO: Return current buffer size (thread-safe)"""
        pass


def demonstrate_race_condition():
    """Demonstrate race conditions and their solution"""
    print("=== Race Condition Demo ===")
    
    # Reset counters
    global unsafe_counter, safe_counter
    unsafe_counter = 0
    safe_counter = 0
    
    # TODO: Create 5 threads that call unsafe_increment()
    # Start all threads and wait for completion
    # Print the final value of unsafe_counter
    print("Testing unsafe counter (race condition):")
    
    # Your code here
    
    print(f"Unsafe counter final value: {unsafe_counter}")
    print(f"Expected value: 500000")
    print(f"Race condition occurred: {unsafe_counter != 500000}")
    
    # TODO: Create 5 threads that call safe_increment()
    # Start all threads and wait for completion
    # Print the final value of safe_counter
    print("\nTesting safe counter (with lock):")
    
    # Your code here
    
    print(f"Safe counter final value: {safe_counter}")
    print(f"Expected value: 500000")
    print(f"Thread safety achieved: {safe_counter == 500000}")


def demonstrate_bank_account():
    """Demonstrate thread-safe bank account operations"""
    print("\n=== Bank Account Demo ===")
    
    # TODO: Create a bank account with initial balance of 1000
    account = None  # Replace with your BankAccount instance
    
    def random_transactions(account, num_transactions):
        """Perform random deposits and withdrawals"""
        for _ in range(num_transactions):
            if random.choice([True, False]):
                # Deposit random amount (10-100)
                amount = random.randint(10, 100)
                account.deposit(amount)
            else:
                # Withdraw random amount (10-50)
                amount = random.randint(10, 50)
                account.withdraw(amount)
            time.sleep(0.01)  # Small delay to increase chance of race conditions
    
    print(f"Initial balance: ${account.get_balance()}")
    
    # TODO: Create 3 threads that perform random transactions
    # Each thread should perform 20 transactions
    # Start all threads and wait for completion
    
    # Your code here
    
    print(f"Final balance: ${account.get_balance()}")


def demonstrate_producer_consumer():
    """Demonstrate producer-consumer pattern with condition variables"""
    print("\n=== Producer-Consumer Demo ===")
    
    # TODO: Create a ProducerConsumerBuffer instance
    buffer = None  # Replace with your ProducerConsumerBuffer instance
    
    def producer(buffer, items, producer_id):
        """Produce items and put them in the buffer"""
        for item in items:
            buffer.put(f"Item-{item}-from-Producer-{producer_id}")
            print(f"Producer {producer_id} produced: Item-{item}")
            time.sleep(random.uniform(0.1, 0.3))
    
    def consumer(buffer, num_items, consumer_id):
        """Consume items from the buffer"""
        for _ in range(num_items):
            item = buffer.get()
            print(f"Consumer {consumer_id} consumed: {item}")
            time.sleep(random.uniform(0.2, 0.4))
    
    # TODO: Create 2 producer threads and 2 consumer threads
    # Producers should produce items 1-5 each
    # Consumers should consume 5 items each
    # Start all threads and wait for completion
    
    # Your code here
    
    print(f"Final buffer size: {buffer.size()}")


def demonstrate_semaphore():
    """Demonstrate semaphore for limiting concurrent access"""
    print("\n=== Semaphore Demo ===")
    
    # TODO: Create a semaphore that allows only 2 concurrent accesses
    semaphore = None  # Replace with threading.Semaphore(2)
    
    def access_limited_resource(worker_id):
        """
        TODO: Use the semaphore to limit access to a shared resource
        1. Acquire the semaphore
        2. Print "Worker {worker_id} accessing resource"
        3. Sleep for 1-2 seconds (simulate resource usage)
        4. Print "Worker {worker_id} releasing resource"
        5. Release the semaphore
        """
        # Your code here
        pass
    
    # TODO: Create 5 threads that try to access the limited resource
    # Start all threads and wait for completion
    # Observe that only 2 threads can access the resource simultaneously
    
    # Your code here


def demonstrate_rlock():
    """Demonstrate reentrant locks"""
    print("\n=== RLock Demo ===")
    
    class Counter:
        def __init__(self):
            self._value = 0
            # TODO: Use threading.RLock() instead of threading.Lock()
            self._lock = None  # Replace with threading.RLock()
        
        def increment(self):
            """TODO: Safely increment the counter"""
            pass
        
        def increment_twice(self):
            """
            TODO: Increment the counter twice by calling increment() twice
            This demonstrates reentrant lock capability
            """
            pass
        
        def get_value(self):
            """TODO: Safely return the counter value"""
            pass
    
    # TODO: Create a Counter instance and test reentrant locking
    counter = Counter()
    
    def worker(counter, iterations):
        for _ in range(iterations):
            if random.choice([True, False]):
                counter.increment()
            else:
                counter.increment_twice()
    
    # TODO: Create 3 threads that increment the counter
    # Each thread should perform 100 iterations
    # Start all threads and wait for completion
    
    # Your code here
    
    print(f"Final counter value: {counter.get_value()}")


if __name__ == "__main__":
    demonstrate_race_condition()
    demonstrate_bank_account()
    demonstrate_producer_consumer()
    demonstrate_semaphore()
    demonstrate_rlock()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. Race conditions occur when multiple threads access shared data")
    print("2. Locks ensure mutual exclusion for critical sections")
    print("3. Condition variables coordinate producer-consumer scenarios")
    print("4. Semaphores limit the number of concurrent accesses")
    print("5. RLocks can be acquired multiple times by the same thread")