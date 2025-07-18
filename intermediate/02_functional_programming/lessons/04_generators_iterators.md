# Generators and Iterators in Python

## Introduction

Generators and iterators are powerful Python features that allow you to create memory-efficient, lazy-evaluated sequences. They enable you to work with large datasets without loading everything into memory at once, and they provide elegant solutions for creating custom iteration patterns.

Understanding generators and iterators is crucial for writing efficient Python code, especially when dealing with large amounts of data or when you need to create custom iteration behaviors.

## Understanding Iteration in Python

Before diving into generators and iterators, let's understand how iteration works in Python.

### The Iteration Protocol

Python's iteration protocol consists of two methods:
- `__iter__()`: Returns an iterator object
- `__next__()`: Returns the next item in the sequence

```python
# Example: How a for loop works internally
numbers = [1, 2, 3, 4, 5]

# This for loop:
for num in numbers:
    print(num)

# Is equivalent to:
iterator = iter(numbers)  # calls numbers.__iter__()
while True:
    try:
        num = next(iterator)  # calls iterator.__next__()
        print(num)
    except StopIteration:
        break
```

### Iterables vs Iterators

- **Iterable**: An object that can be iterated over (has `__iter__()` method)
- **Iterator**: An object that produces values one at a time (has both `__iter__()` and `__next__()` methods)

```python
# List is iterable but not an iterator
numbers = [1, 2, 3]
print(hasattr(numbers, '__iter__'))  # True
print(hasattr(numbers, '__next__'))  # False

# Get an iterator from the list
iterator = iter(numbers)
print(hasattr(iterator, '__iter__'))  # True
print(hasattr(iterator, '__next__'))  # True

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # Would raise StopIteration
```

## Creating Custom Iterators

### Class-based Iterator

```python
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Usage
countdown = CountDown(3)
for num in countdown:
    print(num)  # Prints: 3, 2, 1
```

### Separate Iterator Class

```python
class NumberSequence:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return NumberIterator(self.start, self.end)

class NumberIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Usage
sequence = NumberSequence(1, 5)
for num in sequence:
    print(num)  # Prints: 1, 2, 3, 4

# Can create multiple independent iterators
for num in sequence:
    print(num)  # Prints: 1, 2, 3, 4 again
```

## Introduction to Generators

Generators provide a simpler way to create iterators using functions and the `yield` keyword.

### Basic Generator Function

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

# Usage
gen = simple_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # Would raise StopIteration

# Or use in a loop
for value in simple_generator():
    print(value)  # Prints: 1, 2, 3
```

### Generator vs Regular Function

```python
# Regular function - returns all values at once
def regular_function():
    return [1, 2, 3]

# Generator function - yields values one at a time
def generator_function():
    yield 1
    yield 2
    yield 3

# Memory usage comparison
regular_result = regular_function()  # Creates list in memory
generator_result = generator_function()  # Creates generator object

print(type(regular_result))    # <class 'list'>
print(type(generator_result))  # <class 'generator'>
```

## Generator Examples

### 1. Infinite Sequences

```python
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

# Usage (be careful with infinite generators!)
counter = infinite_counter(10)
for i, value in enumerate(counter):
    if i >= 5:  # Stop after 5 values
        break
    print(value)  # Prints: 10, 11, 12, 13, 14
```

### 2. Fibonacci Sequence

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fibonacci()
fibonacci_numbers = [next(fib) for _ in range(10)]
print(fibonacci_numbers)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 3. File Processing

```python
def read_large_file(file_path):
    """Generator to read large files line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage - memory efficient for large files
# for line in read_large_file('large_file.txt'):
#     process_line(line)
```

### 4. Data Transformation Pipeline

```python
def numbers():
    for i in range(1, 11):
        yield i

def squares(nums):
    for num in nums:
        yield num ** 2

def evens(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators together
pipeline = evens(squares(numbers()))
result = list(pipeline)
print(result)  # [4, 16, 36, 64, 100]
```

## Generator Expressions

Generator expressions provide a concise way to create generators, similar to list comprehensions.

```python
# List comprehension - creates list in memory
squares_list = [x**2 for x in range(10)]

# Generator expression - creates generator object
squares_gen = (x**2 for x in range(10))

print(type(squares_list))  # <class 'list'>
print(type(squares_gen))   # <class 'generator'>

# Memory usage
import sys
print(sys.getsizeof(squares_list))  # Larger memory footprint
print(sys.getsizeof(squares_gen))   # Smaller memory footprint

# Usage
for square in squares_gen:
    print(square)
```

### Generator Expressions in Functions

```python
# Efficient way to pass generators to functions
def sum_of_squares(n):
    return sum(x**2 for x in range(n))

result = sum_of_squares(1000)
print(result)

# Filtering with generator expressions
def even_squares(n):
    return (x**2 for x in range(n) if x % 2 == 0)

for square in even_squares(10):
    print(square)  # 0, 4, 16, 36, 64
```

## Advanced Generator Features

### 1. Generator Methods

Generators have methods that allow two-way communication:

```python
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")

# Usage
gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")    # Received: Hello
gen.send("World")    # Received: World
gen.close()  # Close the generator
```

### 2. Generator with Return Values

```python
def generator_with_return():
    yield 1
    yield 2
    yield 3
    return "Done!"

gen = generator_with_return()
try:
    while True:
        print(next(gen))
except StopIteration as e:
    print(f"Return value: {e.value}")  # Return value: Done!
```

### 3. yield from

The `yield from` expression allows you to delegate to another generator:

```python
def inner_generator():
    yield 1
    yield 2
    yield 3

def outer_generator():
    yield 'start'
    yield from inner_generator()
    yield 'end'

for value in outer_generator():
    print(value)  # start, 1, 2, 3, end
```

### 4. Generator Pipelines

```python
def read_data():
    """Simulate reading data"""
    for i in range(1, 11):
        yield i

def filter_even(data):
    """Filter even numbers"""
    for item in data:
        if item % 2 == 0:
            yield item

def square_numbers(data):
    """Square the numbers"""
    for item in data:
        yield item ** 2

def format_output(data):
    """Format for output"""
    for item in data:
        yield f"Result: {item}"

# Create processing pipeline
pipeline = format_output(square_numbers(filter_even(read_data())))
for result in pipeline:
    print(result)
# Output: Result: 4, Result: 16, Result: 36, Result: 64, Result: 100
```

## Practical Applications

### 1. Memory-Efficient Data Processing

```python
def process_large_dataset(data_source):
    """Process large dataset without loading everything into memory"""
    for batch in data_source:
        # Process each batch
        processed_batch = [item * 2 for item in batch]
        yield processed_batch

def data_batches():
    """Simulate large dataset in batches"""
    for i in range(5):
        yield list(range(i*10, (i+1)*10))

# Process data efficiently
for batch in process_large_dataset(data_batches()):
    print(f"Processed batch: {batch}")
```

### 2. Infinite Data Streams

```python
import random
import time

def sensor_data():
    """Simulate infinite sensor data stream"""
    while True:
        temperature = random.uniform(20, 30)
        humidity = random.uniform(40, 60)
        yield {'temperature': temperature, 'humidity': humidity, 'timestamp': time.time()}
        time.sleep(0.1)  # Simulate sensor delay

def monitor_sensors(data_stream, duration=5):
    """Monitor sensors for a specific duration"""
    start_time = time.time()
    for reading in data_stream:
        if time.time() - start_time > duration:
            break
        print(f"Temp: {reading['temperature']:.1f}°C, Humidity: {reading['humidity']:.1f}%")

# Monitor sensors for 2 seconds
# monitor_sensors(sensor_data(), duration=2)
```

### 3. Tree Traversal

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(node):
    """Generator for inorder tree traversal"""
    if node:
        yield from inorder_traversal(node.left)
        yield node.value
        yield from inorder_traversal(node.right)

# Create a binary tree
root = TreeNode(4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(6, TreeNode(5), TreeNode(7))
)

# Traverse the tree
for value in inorder_traversal(root):
    print(value)  # 1, 2, 3, 4, 5, 6, 7
```

## Performance Considerations

### Memory Efficiency

```python
import sys

# List - stores all values in memory
def create_list(n):
    return [x for x in range(n)]

# Generator - creates values on demand
def create_generator(n):
    return (x for x in range(n))

n = 1000000

# Memory comparison
list_obj = create_list(n)
gen_obj = create_generator(n)

print(f"List size: {sys.getsizeof(list_obj)} bytes")
print(f"Generator size: {sys.getsizeof(gen_obj)} bytes")
```

### Lazy Evaluation

```python
def expensive_operation(x):
    """Simulate expensive computation"""
    print(f"Processing {x}")
    return x ** 2

# Generator - lazy evaluation
def lazy_squares(n):
    for i in range(n):
        yield expensive_operation(i)

# List - eager evaluation
def eager_squares(n):
    return [expensive_operation(i) for i in range(n)]

print("Creating lazy generator:")
lazy_gen = lazy_squares(5)  # No processing happens yet

print("Creating eager list:")
eager_list = eager_squares(5)  # All processing happens immediately

print("Using lazy generator:")
for i, value in enumerate(lazy_gen):
    if i >= 2:  # Only process first 2 values
        break
    print(value)
```

## Best Practices

### 1. Use Generators for Large Datasets

```python
# Good: Memory efficient
def read_log_entries(filename):
    with open(filename, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line.strip()

# Less ideal: Loads everything into memory
def read_all_errors(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if 'ERROR' in line]
```

### 2. Chain Generators for Processing Pipelines

```python
def clean_data(raw_data):
    for item in raw_data:
        cleaned = item.strip().lower()
        if cleaned:
            yield cleaned

def filter_data(data, keyword):
    for item in data:
        if keyword in item:
            yield item

def transform_data(data):
    for item in data:
        yield item.upper()

# Chain generators
raw_data = ['  Hello  ', '  World  ', '  Python  ', '  ']
pipeline = transform_data(filter_data(clean_data(raw_data), 'o'))
result = list(pipeline)
print(result)  # ['HELLO', 'WORLD', 'PYTHON']
```

### 3. Handle StopIteration Properly

```python
def safe_next(iterator, default=None):
    try:
        return next(iterator)
    except StopIteration:
        return default

# Usage
gen = (x for x in range(3))
print(safe_next(gen))  # 0
print(safe_next(gen))  # 1
print(safe_next(gen))  # 2
print(safe_next(gen, 'End'))  # End
```

## Common Patterns and Idioms

### 1. Generator Decorators

```python
def generator_decorator(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        for item in gen:
            yield f"Processed: {item}"
    return wrapper

@generator_decorator
def number_generator(n):
    for i in range(n):
        yield i

for item in number_generator(3):
    print(item)  # Processed: 0, Processed: 1, Processed: 2
```

### 2. Generator Context Managers

```python
from contextlib import contextmanager

@contextmanager
def database_transaction():
    print("Starting transaction")
    try:
        yield "database_connection"
    except Exception:
        print("Rolling back transaction")
        raise
    else:
        print("Committing transaction")

# Usage
with database_transaction() as db:
    print(f"Using {db}")
    # Simulate database operations
```

### 3. Cooperative Multitasking

```python
def task1():
    for i in range(3):
        print(f"Task 1: {i}")
        yield

def task2():
    for i in range(3):
        print(f"Task 2: {i}")
        yield

def scheduler(tasks):
    while tasks:
        for task in tasks[:]:  # Copy list to avoid modification issues
            try:
                next(task)
            except StopIteration:
                tasks.remove(task)

# Run tasks cooperatively
tasks = [task1(), task2()]
scheduler(tasks)
```

## Debugging Generators

### 1. Generator State

```python
def debug_generator():
    print("Generator started")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")
    yield 3
    print("Generator finished")

gen = debug_generator()
print("Generator created")
print(f"First value: {next(gen)}")
print(f"Second value: {next(gen)}")
print(f"Third value: {next(gen)}")
```

### 2. Generator Inspection

```python
import inspect

def sample_generator():
    yield 1
    yield 2
    yield 3

gen = sample_generator()
print(f"Is generator: {inspect.isgenerator(gen)}")
print(f"Generator state: {inspect.getgeneratorstate(gen)}")

next(gen)
print(f"Generator state after first next(): {inspect.getgeneratorstate(gen)}")
```

## Summary

Generators and iterators are powerful Python features that enable:

- **Memory Efficiency**: Process large datasets without loading everything into memory
- **Lazy Evaluation**: Compute values only when needed
- **Infinite Sequences**: Create sequences that can theoretically go on forever
- **Pipeline Processing**: Chain operations together efficiently
- **Custom Iteration**: Create your own iteration patterns

Key concepts:
- **Iterator Protocol**: `__iter__()` and `__next__()` methods
- **Generator Functions**: Use `yield` to create generators
- **Generator Expressions**: Concise syntax for simple generators
- **yield from**: Delegate to other generators
- **Generator Methods**: `send()`, `throw()`, `close()`

Best practices:
- Use generators for large datasets and streaming data
- Chain generators for processing pipelines
- Handle `StopIteration` exceptions properly
- Consider memory and performance implications
- Use generator expressions for simple cases

Generators and iterators are essential tools for writing efficient, memory-conscious Python code, especially when dealing with large amounts of data or creating custom iteration patterns.