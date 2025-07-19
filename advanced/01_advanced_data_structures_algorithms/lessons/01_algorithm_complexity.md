# Algorithm Complexity Analysis

## Introduction

Understanding algorithm complexity is crucial for writing efficient code and making informed decisions about which algorithms to use in different situations. This lesson introduces Big O notation and teaches you how to analyze the time and space complexity of algorithms.

## What is Algorithm Complexity?

Algorithm complexity measures how the performance of an algorithm changes as the input size grows. We typically analyze two types of complexity:

1. **Time Complexity**: How execution time increases with input size
2. **Space Complexity**: How memory usage increases with input size

## Big O Notation

Big O notation describes the upper bound of an algorithm's growth rate. It tells us the worst-case scenario for how an algorithm performs as input size approaches infinity.

### Common Big O Complexities (from best to worst):

1. **O(1) - Constant Time**
   - Performance doesn't change with input size
   - Example: Accessing an array element by index

```python
def get_first_element(arr):
    return arr[0]  # Always takes the same time regardless of array size
```

2. **O(log n) - Logarithmic Time**
   - Performance increases logarithmically with input size
   - Example: Binary search in a sorted array

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

3. **O(n) - Linear Time**
   - Performance increases linearly with input size
   - Example: Finding an element in an unsorted array

```python
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1
```

4. **O(n log n) - Linearithmic Time**
   - Common in efficient sorting algorithms
   - Example: Merge sort, heap sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

5. **O(n²) - Quadratic Time**
   - Performance increases quadratically with input size
   - Example: Bubble sort, nested loops

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

6. **O(2ⁿ) - Exponential Time**
   - Performance doubles with each additional input
   - Example: Naive recursive Fibonacci

```python
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
```

7. **O(n!) - Factorial Time**
   - Performance grows factorially
   - Example: Generating all permutations

## Analyzing Algorithm Complexity

### Step-by-Step Analysis Process:

1. **Identify the basic operations** (comparisons, assignments, arithmetic operations)
2. **Count how many times each operation executes** relative to input size
3. **Focus on the dominant term** (the one that grows fastest)
4. **Drop constants and lower-order terms**

### Example Analysis:

```python
def example_algorithm(arr):
    # Step 1: O(1) - constant time operation
    n = len(arr)
    
    # Step 2: O(n) - linear loop
    for i in range(n):
        print(arr[i])
    
    # Step 3: O(n²) - nested loops
    for i in range(n):
        for j in range(n):
            if arr[i] > arr[j]:
                print(f"{arr[i]} > {arr[j]}")
    
    # Step 4: O(1) - constant time operation
    return arr[0]

# Overall complexity: O(1) + O(n) + O(n²) + O(1) = O(n²)
# We keep only the dominant term: O(n²)
```

## Best, Average, and Worst Case Analysis

Algorithms can perform differently depending on the input:

- **Best Case**: The scenario where the algorithm performs optimally
- **Average Case**: The expected performance across all possible inputs
- **Worst Case**: The scenario where the algorithm performs poorest

### Example: Linear Search

```python
def linear_search_analysis(arr, target):
    """
    Best Case: O(1) - target is the first element
    Average Case: O(n/2) = O(n) - target is in the middle on average
    Worst Case: O(n) - target is the last element or not present
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1
```

## Space Complexity

Space complexity measures how much additional memory an algorithm uses relative to input size.

### Types of Space Usage:

1. **Input Space**: Memory used to store the input (usually not counted)
2. **Auxiliary Space**: Extra memory used by the algorithm
3. **Total Space**: Input space + Auxiliary space

### Examples:

```python
# O(1) space - only uses a constant amount of extra memory
def find_max_constant_space(arr):
    max_val = arr[0]
    for element in arr:
        if element > max_val:
            max_val = element
    return max_val

# O(n) space - creates a new array of the same size
def reverse_array_linear_space(arr):
    return arr[::-1]

# O(n) space - recursive calls use stack space
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
```

## Practical Tips for Algorithm Analysis

1. **Focus on large inputs**: Big O describes behavior as n approaches infinity
2. **Ignore constants**: O(2n) is the same as O(n)
3. **Drop lower-order terms**: O(n² + n) becomes O(n²)
4. **Consider both time and space**: Sometimes you can trade one for the other
5. **Think about real-world constraints**: Sometimes O(n²) is fine for small, fixed inputs

## Common Mistakes to Avoid

1. **Confusing best case with average case**
2. **Forgetting about space complexity**
3. **Not considering the actual operations being performed**
4. **Assuming all O(n) algorithms are equally fast**
5. **Ignoring constant factors when they matter in practice**

## Optimization Strategies

1. **Use appropriate data structures**: Hash tables for O(1) lookups
2. **Avoid unnecessary nested loops**: Look for ways to reduce complexity
3. **Use divide-and-conquer**: Break problems into smaller subproblems
4. **Consider caching/memoization**: Trade space for time
5. **Profile your code**: Measure actual performance, not just theoretical complexity

## Real-World Applications

Understanding complexity helps you:

- **Choose the right algorithm** for your specific use case
- **Predict performance** as your data grows
- **Identify bottlenecks** in your code
- **Make informed trade-offs** between time and space
- **Optimize critical paths** in your applications

## Summary

Algorithm complexity analysis is a fundamental skill for any programmer. By understanding Big O notation and how to analyze algorithms, you can:

- Write more efficient code
- Make better algorithmic choices
- Predict how your programs will scale
- Communicate effectively about performance trade-offs

In the next lesson, we'll apply these concepts to analyze recursive algorithms and learn optimization techniques like memoization.