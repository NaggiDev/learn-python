"""
Generators and Iterators - Solutions

This file contains the solutions for the generators and iterators exercises.
"""

import sys
import time

# Exercise 1: Basic Iterator Class
class CountDown:
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Exercise 2: Basic Generator Function
def number_generator(n):
    for i in range(1, n + 1):
        yield i

# Exercise 3: Fibonacci Generator
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Exercise 4: Even Numbers Generator
def even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

# Exercise 5: Generator Expression
def squares_generator(n):
    return (i**2 for i in range(1, n + 1))

# Exercise 6: File Line Generator
def file_lines(lines_list):
    for line in lines_list:
        yield line

# Exercise 7: Infinite Generator
def cycle_generator(items):
    while True:
        for item in items:
            yield item

# Exercise 8: Generator Pipeline
def data_source():
    """Generate numbers 1-10"""
    for i in range(1, 11):
        yield i

def filter_evens(data):
    """Filter even numbers from data generator"""
    for item in data:
        if item % 2 == 0:
            yield item

def square_numbers(data):
    """Square numbers from data generator"""
    for item in data:
        yield item ** 2

# Exercise 9: Generator with Send
def accumulator_generator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

# Exercise 10: Tree Traversal Generator
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root:
        yield from inorder_traversal(root.left)
        yield root.value
        yield from inorder_traversal(root.right)

# Exercise 11: Batch Generator
def batch_generator(items, batch_size):
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:  # Yield remaining items
        yield batch

# Exercise 12: Prime Numbers Generator
def prime_generator():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Exercise 13: Generator Decorator
def make_generator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(result, '__iter__') and not isinstance(result, (str, bytes)):
            for item in result:
                yield item
        else:
            yield result
    return wrapper

# Exercise 14: Memory-Efficient Data Processing
def process_large_data(data_size):
    """
    Simulate processing large dataset without loading everything into memory
    Generate data_size number of processed items
    """
    for i in range(data_size):
        # Simulate some processing
        processed_item = f"processed_item_{i}"
        yield processed_item

# Exercise 15: Custom Range Generator
def custom_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step
    else:
        raise ValueError("step argument must not be zero")

def demonstrate_solutions():
    """Demonstrate all the solutions"""
    print("Generators and Iterators Solutions Demonstration\n")
    
    # Exercise 1: CountDown Iterator
    print("1. CountDown Iterator:")
    countdown = CountDown(3)
    for num in countdown:
        print(f"   {num}")
    
    # Exercise 2: Number Generator
    print("\n2. Number Generator:")
    for num in number_generator(5):
        print(f"   {num}")
    
    # Exercise 3: Fibonacci Generator
    print("\n3. Fibonacci Generator (first 8 numbers):")
    fib_gen = fibonacci_generator()
    for i in range(8):
        print(f"   {next(fib_gen)}")
    
    # Exercise 4: Even Numbers Generator
    print("\n4. Even Numbers (1-10):")
    for num in even_numbers(1, 10):
        print(f"   {num}")
    
    # Exercise 5: Squares Generator
    print("\n5. Squares Generator (1-5):")
    for square in squares_generator(5):
        print(f"   {square}")
    
    # Exercise 6: File Lines Generator
    print("\n6. File Lines Generator:")
    lines = ["First line", "Second line", "Third line"]
    for line in file_lines(lines):
        print(f"   {line}")
    
    # Exercise 7: Cycle Generator
    print("\n7. Cycle Generator (first 7 items):")
    cycle_gen = cycle_generator(['A', 'B', 'C'])
    for i in range(7):
        print(f"   {next(cycle_gen)}")
    
    # Exercise 8: Generator Pipeline
    print("\n8. Generator Pipeline (even squares):")
    pipeline = square_numbers(filter_evens(data_source()))
    for result in pipeline:
        print(f"   {result}")
    
    # Exercise 9: Accumulator Generator
    print("\n9. Accumulator Generator:")
    acc_gen = accumulator_generator()
    next(acc_gen)  # Prime the generator
    print(f"   Send 5: {acc_gen.send(5)}")
    print(f"   Send 3: {acc_gen.send(3)}")
    print(f"   Send 2: {acc_gen.send(2)}")
    
    # Exercise 10: Tree Traversal
    print("\n10. Tree Traversal (inorder):")
    root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(6, TreeNode(5), TreeNode(7))
    )
    for value in inorder_traversal(root):
        print(f"   {value}")
    
    # Exercise 11: Batch Generator
    print("\n11. Batch Generator:")
    items = list(range(1, 11))
    for batch in batch_generator(items, 3):
        print(f"   {batch}")
    
    # Exercise 12: Prime Generator
    print("\n12. Prime Generator (first 10 primes):")
    prime_gen = prime_generator()
    for i in range(10):
        print(f"   {next(prime_gen)}")
    
    # Exercise 13: Generator Decorator
    print("\n13. Generator Decorator:")
    @make_generator
    def get_numbers():
        return [1, 2, 3, 4, 5]
    
    for num in get_numbers():
        print(f"   {num}")
    
    # Exercise 14: Memory-Efficient Processing
    print("\n14. Memory-Efficient Processing:")
    for item in process_large_data(3):
        print(f"   {item}")
    
    # Exercise 15: Custom Range
    print("\n15. Custom Range:")
    print("   Range(5):", list(custom_range(5)))
    print("   Range(2, 7):", list(custom_range(2, 7)))
    print("   Range(0, 10, 2):", list(custom_range(0, 10, 2)))

def advanced_generator_examples():
    """Show additional advanced generator examples"""
    print("\n" + "="*60)
    print("Advanced Generator Examples")
    print("="*60)
    
    # Example 1: Generator with cleanup
    print("\n1. Generator with Cleanup:")
    def resource_generator():
        print("   Acquiring resource...")
        try:
            for i in range(3):
                yield f"Resource data {i}"
        finally:
            print("   Releasing resource...")
    
    gen = resource_generator()
    for data in gen:
        print(f"   Got: {data}")
    
    # Example 2: Coroutine-style generator
    print("\n2. Coroutine-style Generator:")
    def logger_generator():
        while True:
            message = yield
            if message:
                timestamp = time.strftime("%H:%M:%S")
                print(f"   [{timestamp}] {message}")
    
    logger = logger_generator()
    next(logger)  # Prime the generator
    logger.send("Starting application")
    logger.send("Processing data")
    logger.send("Application finished")
    logger.close()
    
    # Example 3: Generator for streaming data
    print("\n3. Streaming Data Generator:")
    def data_stream(count):
        for i in range(count):
            # Simulate data generation
            data = {'id': i, 'value': i * 2, 'timestamp': time.time()}
            yield data
            time.sleep(0.01)  # Simulate delay
    
    print("   Streaming 3 data points:")
    for data_point in data_stream(3):
        print(f"   {data_point}")
    
    # Example 4: Generator composition
    print("\n4. Generator Composition:")
    def numbers():
        for i in range(1, 6):
            yield i
    
    def letters():
        for letter in 'ABCDE':
            yield letter
    
    def combine_generators(*generators):
        for gen in generators:
            yield from gen
    
    print("   Combined generators:")
    for item in combine_generators(numbers(), letters()):
        print(f"   {item}")
    
    # Example 5: Generator for pagination
    print("\n5. Pagination Generator:")
    def paginate(data, page_size):
        for i in range(0, len(data), page_size):
            yield data[i:i + page_size]
    
    large_dataset = list(range(1, 21))  # 20 items
    print("   Paginated data (page size 7):")
    for page_num, page in enumerate(paginate(large_dataset, 7), 1):
        print(f"   Page {page_num}: {page}")
    
    # Example 6: Generator for recursive structures
    print("\n6. Directory Tree Generator:")
    def directory_tree():
        """Simulate directory structure traversal"""
        directories = [
            "/root",
            "/root/documents",
            "/root/documents/file1.txt",
            "/root/documents/file2.txt",
            "/root/images",
            "/root/images/photo1.jpg"
        ]
        for path in directories:
            yield path
    
    print("   Directory structure:")
    for path in directory_tree():
        print(f"   {path}")
    
    # Example 7: Performance comparison
    print("\n7. Performance Comparison:")
    def memory_comparison():
        # List approach - all in memory
        def create_large_list(n):
            return [x**2 for x in range(n)]
        
        # Generator approach - lazy evaluation
        def create_large_generator(n):
            return (x**2 for x in range(n))
        
        n = 10000
        
        # Memory usage
        large_list = create_large_list(n)
        large_gen = create_large_generator(n)
        
        list_size = sys.getsizeof(large_list)
        gen_size = sys.getsizeof(large_gen)
        
        print(f"   List size ({n} items): {list_size} bytes")
        print(f"   Generator size: {gen_size} bytes")
        print(f"   Memory savings: {list_size - gen_size} bytes")
        
        # Processing time for partial consumption
        start_time = time.time()
        first_100_list = large_list[:100]
        list_time = time.time() - start_time
        
        start_time = time.time()
        large_gen = create_large_generator(n)  # Recreate generator
        first_100_gen = [next(large_gen) for _ in range(100)]
        gen_time = time.time() - start_time
        
        print(f"   Time to get first 100 items from list: {list_time:.6f}s")
        print(f"   Time to get first 100 items from generator: {gen_time:.6f}s")
    
    memory_comparison()

if __name__ == "__main__":
    demonstrate_solutions()
    advanced_generator_examples()