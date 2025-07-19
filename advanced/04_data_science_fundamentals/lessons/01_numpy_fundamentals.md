# NumPy Fundamentals: Array Operations and Numerical Computing

## Introduction

NumPy (Numerical Python) is the foundation of the Python data science ecosystem. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. Understanding NumPy is crucial for data science, machine learning, and scientific computing.

## Why NumPy?

### Performance
- NumPy arrays are stored in contiguous memory locations
- Operations are implemented in C, making them much faster than pure Python
- Vectorized operations eliminate the need for explicit loops

### Memory Efficiency
- NumPy arrays use less memory than Python lists
- Homogeneous data types allow for compact storage
- Broadcasting enables efficient operations without copying data

### Ecosystem Integration
- Foundation for Pandas, Matplotlib, Scikit-learn, and other libraries
- Interoperability with other scientific computing tools
- Standard for numerical computing in Python

## Core Concepts

### 1. NumPy Arrays (ndarray)

NumPy's main object is the homogeneous multidimensional array (ndarray). Key characteristics:

- **Homogeneous**: All elements have the same data type
- **Multidimensional**: Can have any number of dimensions
- **Fixed Size**: Size is determined at creation time
- **Efficient**: Optimized for numerical operations

```python
import numpy as np

# Creating arrays
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"1D array: {arr_1d}")
print(f"2D array:\n{arr_2d}")
print(f"3D array:\n{arr_3d}")
```

### 2. Array Attributes

Understanding array properties is essential for effective NumPy usage:

```python
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(f"Shape: {arr.shape}")        # (2, 4) - dimensions
print(f"Size: {arr.size}")          # 8 - total elements
print(f"Dimensions: {arr.ndim}")    # 2 - number of axes
print(f"Data type: {arr.dtype}")    # int64 - element type
print(f"Item size: {arr.itemsize}") # 8 - bytes per element
```

### 3. Array Creation Methods

NumPy provides various ways to create arrays:

```python
# From Python sequences
arr_list = np.array([1, 2, 3, 4])
arr_tuple = np.array((1, 2, 3, 4))

# Built-in creation functions
zeros = np.zeros((3, 4))           # Array of zeros
ones = np.ones((2, 3))             # Array of ones
empty = np.empty((2, 2))           # Uninitialized array
full = np.full((3, 3), 7)          # Array filled with value

# Range functions
arange = np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)    # [0, 0.25, 0.5, 0.75, 1]

# Random arrays
random = np.random.random((2, 3))   # Random values [0, 1)
randint = np.random.randint(0, 10, (2, 3))  # Random integers

# Identity and diagonal
identity = np.eye(3)               # Identity matrix
diag = np.diag([1, 2, 3])         # Diagonal matrix
```

### 4. Data Types

NumPy supports various data types for memory efficiency:

```python
# Integer types
int8_arr = np.array([1, 2, 3], dtype=np.int8)     # 8-bit integer
int32_arr = np.array([1, 2, 3], dtype=np.int32)   # 32-bit integer

# Float types
float32_arr = np.array([1.0, 2.0], dtype=np.float32)  # 32-bit float
float64_arr = np.array([1.0, 2.0], dtype=np.float64)  # 64-bit float

# Boolean and complex
bool_arr = np.array([True, False, True], dtype=bool)
complex_arr = np.array([1+2j, 3+4j], dtype=complex)

# Type conversion
arr = np.array([1.7, 2.3, 3.9])
int_arr = arr.astype(int)          # Convert to integer
```

## Array Operations

### 1. Indexing and Slicing

NumPy arrays support powerful indexing and slicing operations:

```python
# 1D array indexing
arr_1d = np.array([0, 1, 2, 3, 4, 5])
print(arr_1d[0])        # First element: 0
print(arr_1d[-1])       # Last element: 5
print(arr_1d[1:4])      # Slice: [1, 2, 3]
print(arr_1d[::2])      # Every second: [0, 2, 4]

# 2D array indexing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[0, 1])     # Element at row 0, col 1: 2
print(arr_2d[1])        # Entire row 1: [4, 5, 6]
print(arr_2d[:, 1])     # Entire column 1: [2, 5, 8]
print(arr_2d[0:2, 1:3]) # Subarray: [[2, 3], [5, 6]]

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
print(arr[mask])        # Elements > 3: [4, 5]
print(arr[arr % 2 == 0]) # Even elements: [2, 4]
```

### 2. Array Reshaping

Changing array dimensions without changing data:

```python
arr = np.arange(12)
print(f"Original: {arr}")

# Reshape to 2D
reshaped = arr.reshape(3, 4)
print(f"3x4:\n{reshaped}")

# Reshape to 3D
reshaped_3d = arr.reshape(2, 2, 3)
print(f"2x2x3:\n{reshaped_3d}")

# Flatten back to 1D
flattened = reshaped.flatten()
print(f"Flattened: {flattened}")

# Transpose
transposed = reshaped.T
print(f"Transposed:\n{transposed}")
```

### 3. Mathematical Operations

NumPy provides vectorized mathematical operations:

```python
# Element-wise operations
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"Addition: {a + b}")        # [6, 8, 10, 12]
print(f"Subtraction: {a - b}")     # [-4, -4, -4, -4]
print(f"Multiplication: {a * b}")  # [5, 12, 21, 32]
print(f"Division: {b / a}")        # [5.0, 3.0, 2.33, 2.0]
print(f"Power: {a ** 2}")          # [1, 4, 9, 16]

# Mathematical functions
arr = np.array([1, 4, 9, 16])
print(f"Square root: {np.sqrt(arr)}")      # [1, 2, 3, 4]
print(f"Logarithm: {np.log(arr)}")         # Natural log
print(f"Exponential: {np.exp([1, 2, 3])}")  # e^x

# Trigonometric functions
angles = np.array([0, np.pi/2, np.pi])
print(f"Sine: {np.sin(angles)}")
print(f"Cosine: {np.cos(angles)}")
```

### 4. Aggregation Functions

Computing statistics across arrays:

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Basic statistics
print(f"Sum: {np.sum(arr)}")           # 45
print(f"Mean: {np.mean(arr)}")         # 5.0
print(f"Standard deviation: {np.std(arr)}")
print(f"Min: {np.min(arr)}")           # 1
print(f"Max: {np.max(arr)}")           # 9

# Along specific axes
print(f"Sum along rows: {np.sum(arr, axis=0)}")    # [12, 15, 18]
print(f"Sum along columns: {np.sum(arr, axis=1)}") # [6, 15, 24]
print(f"Mean along rows: {np.mean(arr, axis=0)}")  # [4, 5, 6]
```

## Broadcasting

Broadcasting allows NumPy to perform operations on arrays with different shapes:

```python
# Scalar and array
arr = np.array([1, 2, 3, 4])
result = arr + 10  # Adds 10 to each element
print(f"Scalar broadcast: {result}")

# Arrays with different shapes
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_1d = np.array([10, 20, 30])
result = arr_2d + arr_1d  # Adds [10, 20, 30] to each row
print(f"Array broadcast:\n{result}")

# Broadcasting rules example
a = np.array([[1], [2], [3]])  # Shape: (3, 1)
b = np.array([10, 20, 30])     # Shape: (3,)
result = a + b                 # Result shape: (3, 3)
print(f"Broadcasting result:\n{result}")
```

## Linear Algebra

NumPy provides comprehensive linear algebra operations:

```python
# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
matrix_mult = np.dot(A, B)  # or A @ B
print(f"Matrix multiplication:\n{matrix_mult}")

# Transpose
print(f"Transpose of A:\n{A.T}")

# Determinant and inverse
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
print(f"Determinant: {det_A}")
print(f"Inverse:\n{inv_A}")

# Eigenvalues and eigenvectors
eigenvals, eigenvecs = np.linalg.eig(A)
print(f"Eigenvalues: {eigenvals}")
print(f"Eigenvectors:\n{eigenvecs}")
```

## Advanced Indexing

NumPy supports sophisticated indexing techniques:

```python
# Fancy indexing
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(f"Fancy indexing: {arr[indices]}")  # [10, 30, 50]

# Boolean indexing with conditions
arr_2d = np.random.randint(0, 10, (4, 4))
print(f"Original array:\n{arr_2d}")

# Multiple conditions
mask = (arr_2d > 3) & (arr_2d < 7)
print(f"Elements between 3 and 7: {arr_2d[mask]}")

# Where function
result = np.where(arr_2d > 5, arr_2d, 0)  # Replace values <= 5 with 0
print(f"Conditional replacement:\n{result}")
```

## Performance Considerations

### Vectorization vs. Loops

```python
import time

# Inefficient: Python loop
def python_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

# Efficient: NumPy vectorized operation
def numpy_sum(arr):
    return np.sum(arr)

# Performance comparison
large_array = np.random.random(1000000)

start = time.time()
python_result = python_sum(large_array)
python_time = time.time() - start

start = time.time()
numpy_result = numpy_sum(large_array)
numpy_time = time.time() - start

print(f"Python loop time: {python_time:.4f} seconds")
print(f"NumPy vectorized time: {numpy_time:.4f} seconds")
print(f"Speedup: {python_time / numpy_time:.1f}x")
```

## Best Practices

1. **Use vectorized operations** instead of explicit loops
2. **Choose appropriate data types** to save memory
3. **Avoid unnecessary array copies** when possible
4. **Use broadcasting** instead of reshaping when possible
5. **Preallocate arrays** when size is known
6. **Use views instead of copies** when you don't need to modify data

## Common Pitfalls

1. **Array vs. Matrix multiplication**: Use `@` or `np.dot()` for matrix multiplication
2. **Integer division**: Be aware of integer vs. float division
3. **Array copying**: Understand when NumPy creates copies vs. views
4. **Broadcasting errors**: Ensure array shapes are compatible
5. **Memory usage**: Large arrays can consume significant memory

## Real-World Applications

NumPy is used in:
- **Image processing**: Representing images as arrays
- **Signal processing**: Analyzing time-series data
- **Scientific computing**: Numerical simulations
- **Machine learning**: Feature matrices and computations
- **Financial analysis**: Time-series analysis and risk calculations

## Summary

NumPy provides:
- Efficient multidimensional arrays
- Vectorized mathematical operations
- Broadcasting for flexible computations
- Linear algebra capabilities
- Foundation for the Python data science ecosystem

Mastering NumPy is essential for effective data science work in Python. The concepts learned here will be directly applicable when working with Pandas, Matplotlib, and machine learning libraries.

## Next Steps

In the next lesson, we'll explore Pandas, which builds on NumPy to provide high-level data manipulation and analysis capabilities. You'll see how NumPy arrays form the foundation of Pandas DataFrames and Series.