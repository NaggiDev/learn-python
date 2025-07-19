"""
Solution: Thread Synchronization

Complete implementation of thread synchronization concepts.
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
    """Increment unsafe_counter without synchronization (demonstrates race condition)"""
    global unsafe_counter
    for _ in range(100000):
        unsafe_counter += 1


def safe_increment():
    """Safely increment safe_counter using a lock"""
    global safe_counter
    for _ in range(100000):
        with counter_lock:
            safe_counter += 1


class BankAccount:
    """Thread-safe bank account implementation"""
    
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._lock = threading.Lock()
    
    def deposit(self, amount):
        """Safely add amount to balance"""
        with self._lock:
            old_balance = self._balance
            self._balance += amount
            print(f"Deposited ${amount}. Balance: ${old_balance} -> ${self._balance}")
    
    def withdraw(self, amount):
        """Safely subtract amount from balance, prevent overdrafts"""
        with self._lock:
            if self._balance >= amount:
                old_balance = self._balance
                self._balance -= amount
                print(f"Withdrew ${amount}. Balance: ${old_balance} -> ${self._balance}")
                return True
            else:
                print(f"Insufficient funds. Cannot withdraw ${amount}. Current balance: ${self._balance}")
                return False
    
    def get_balance(self):
        """Safely return the current balance"""
        with self._lock:
            return self._balance


class ProducerConsumerBuffer:
    """Thread-safe buffer for producer-consumer pattern using Condition"""
    
    def __init__(self, max_size=5):
        self._buffer = []
        self._max_size = max_size
        self._condition = threading.Condition()
    
    def put(self, item):
        """Add item to buffer, wait if buffer is full"""
        with self._condition:
            while len(self._buffer) >= self._max_size:
                print(f"Buffer full ({len(self._buffer)}/{self._max_size}), producer waiting...")
                self._condition.wait()
            
            self._buffer.append(item)
            print(f"Produced: {item} (buffer size: {len(self._buffer)})")
            self._condition.notify_all()  # Notify consumers
    
    def get(self):
        """Remove and return item from buffer, wait if buffer is empty"""
        with self._condition:
            while len(self._buffer) == 0:
                print("Buffer empty, consumer waiting...")
                self._condition.wait()
            
            item = self._buffer.pop(0)
            print(f"Consumed: {item} (buffer size: {len(self._buffer)})")
            self._condition.notify_all()  # Notify producers
            return item
    
    def size(self):
        """Return current buffer size (thread-safe)"""
        with self._condition:
            return len(self._buffer)


def demonstrate_race_condition():
    """Demonstrate race conditions and their solution"""
    print("=== Race Condition Demo ===")
    
    # Reset counters
    global unsafe_counter, safe_counter
    unsafe_counter = 0
    safe_counter = 0
    
    # Test unsafe counter (race condition)
    print("Testing unsafe counter (race condition):")
    threads = []
    for i in range(5):
        thread = threading.Thread(target=unsafe_increment)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Unsafe counter final value: {unsafe_counter}")
    print(f"Expected value: 500000")
    print(f"Race condition occurred: {unsafe_counter != 500000}")
    
    # Test safe counter (with lock)
    print("\nTesting safe counter (with lock):")
    threads = []
    for i in range(5):
        thread = threading.Thread(target=safe_increment)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Safe counter final value: {safe_counter}")
    print(f"Expected value: 500000")
    print(f"Thread safety achieved: {safe_counter == 500000}")


def demonstrate_bank_account():
    """Demonstrate thread-safe bank account operations"""
    print("\n=== Bank Account Demo ===")
    
    account = BankAccount(1000)
    
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
    
    # Create 3 threads that perform random transactions
    threads = []
    for i in range(3):
        thread = threading.Thread(target=random_transactions, args=(account, 20))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Final balance: ${account.get_balance()}")


def demonstrate_producer_consumer():
    """Demonstrate producer-consumer pattern with condition variables"""
    print("\n=== Producer-Consumer Demo ===")
    
    buffer = ProducerConsumerBuffer(3)
    
    def producer(buffer, items, producer_id):
        """Produce items and put them in the buffer"""
        for item in items:
            buffer.put(f"Item-{item}-from-Producer-{producer_id}")
            time.sleep(random.uniform(0.1, 0.3))
    
    def consumer(buffer, num_items, consumer_id):
        """Consume items from the buffer"""
        for _ in range(num_items):
            item = buffer.get()
            time.sleep(random.uniform(0.2, 0.4))
    
    # Create 2 producer threads and 2 consumer threads
    threads = []
    
    # Producers
    for i in range(2):
        items = list(range(1, 6))  # Items 1-5
        thread = threading.Thread(target=producer, args=(buffer, items, i+1))
        threads.append(thread)
        thread.start()
    
    # Consumers
    for i in range(2):
        thread = threading.Thread(target=consumer, args=(buffer, 5, i+1))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Final buffer size: {buffer.size()}")


def demonstrate_semaphore():
    """Demonstrate semaphore for limiting concurrent access"""
    print("\n=== Semaphore Demo ===")
    
    semaphore = threading.Semaphore(2)  # Allow only 2 concurrent accesses
    
    def access_limited_resource(worker_id):
        """Use semaphore to limit access to a shared resource"""
        with semaphore:
            print(f"Worker {worker_id} accessing resource")
            time.sleep(random.uniform(1, 2))  # Simulate resource usage
            print(f"Worker {worker_id} releasing resource")
    
    # Create 5 threads that try to access the limited resource
    threads = []
    for i in range(5):
        thread = threading.Thread(target=access_limited_resource, args=(i+1,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


def demonstrate_rlock():
    """Demonstrate reentrant locks"""
    print("\n=== RLock Demo ===")
    
    class Counter:
        def __init__(self):
            self._value = 0
            self._lock = threading.RLock()  # Reentrant lock
        
        def increment(self):
            """Safely increment the counter"""
            with self._lock:
                self._value += 1
        
        def increment_twice(self):
            """Increment the counter twice using reentrant lock"""
            with self._lock:
                self.increment()  # Can acquire lock again
                self.increment()
        
        def get_value(self):
            """Safely return the counter value"""
            with self._lock:
                return self._value
    
    counter = Counter()
    
    def worker(counter, iterations):
        for _ in range(iterations):
            if random.choice([True, False]):
                counter.increment()
            else:
                counter.increment_twice()
    
    # Create 3 threads that increment the counter
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(counter, 100))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
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