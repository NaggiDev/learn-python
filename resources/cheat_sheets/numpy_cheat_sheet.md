# NumPy Cheat Sheet

## Installation and Import
```python
# Install: pip install numpy
import numpy as np
```

## Array Creation

### Basic Array Creation
```python
# From lists
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Array with specific data type
arr_float = np.array([1, 2, 3], dtype=np.float64)
arr_int = np.array([1.5, 2.7, 3.9], dtype=np.int32)
```

### Array Generation Functions
```python
# Zeros and ones
zeros = np.zeros((3, 4))        # 3x4 array of zeros
ones = np.ones((2, 3))          # 2x3 array of ones
full = np.full((2, 2), 7)       # 2x2 array filled with 7

# Identity matrix
identity = np.eye(3)            # 3x3 identity matrix

# Range arrays
range_arr = np.arange(0, 10, 2)     # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)     # [0, 0.25, 0.5, 0.75, 1]

# Random arrays
random_arr = np.random.random((2, 3))       # Random floats [0, 1)
random_int = np.random.randint(0, 10, (2, 3))  # Random integers
normal = np.random.normal(0, 1, (2, 3))     # Normal distribution
```

## Array Properties

### Basic Properties
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)        # (2, 3) - dimensions
print(arr.size)         # 6 - total number of elements
print(arr.ndim)         # 2 - number of dimensions
print(arr.dtype)        # data type
print(arr.itemsize)     # size of each element in bytes
```

## Array Indexing and Slicing

### Basic Indexing
```python
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 1D indexing
print(arr1d[0])         # 1 (first element)
print(arr1d[-1])        # 5 (last element)
print(arr1d[1:4])       # [2, 3, 4] (slicing)

# 2D indexing
print(arr2d[0, 1])      # 2 (row 0, column 1)
print(arr2d[1])         # [4, 5, 6] (entire row 1)
print(arr2d[:, 1])      # [2, 5, 8] (entire column 1)
print(arr2d[0:2, 1:3])  # [[2, 3], [5, 6]] (subarray)
```

### Boolean Indexing
```python
arr = np.array([1, 2, 3, 4, 5])

# Boolean mask
mask = arr > 3
print(mask)             # [False, False, False, True, True]
print(arr[mask])        # [4, 5]

# Direct boolean indexing
print(arr[arr > 3])     # [4, 5]
print(arr[(arr > 2) & (arr < 5)])  # [3, 4]
```

### Fancy Indexing
```python
arr = np.array([10, 20, 30, 40, 50])

# Index with array of indices
indices = np.array([0, 2, 4])
print(arr[indices])     # [10, 30, 50]

# 2D fancy indexing
arr2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2d[[0, 2], [1, 0]])  # [2, 5] - elements at (0,1) and (2,0)
```

## Array Operations

### Arithmetic Operations
```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Element-wise operations
print(arr1 + arr2)      # [6, 8, 10, 12]
print(arr1 - arr2)      # [-4, -4, -4, -4]
print(arr1 * arr2)      # [5, 12, 21, 32]
print(arr1 / arr2)      # [0.2, 0.33, 0.43, 0.5]
print(arr1 ** 2)        # [1, 4, 9, 16]

# Operations with scalars
print(arr1 + 10)        # [11, 12, 13, 14]
print(arr1 * 2)         # [2, 4, 6, 8]
```

### Comparison Operations
```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 3, 2, 4])

print(arr1 == arr2)     # [True, False, False, True]
print(arr1 > arr2)      # [False, False, True, False]
print(arr1 >= 3)        # [False, False, True, True]
```

### Universal Functions (ufuncs)
```python
arr = np.array([1, 4, 9, 16])

# Mathematical functions
print(np.sqrt(arr))     # [1, 2, 3, 4]
print(np.exp(arr))      # Exponential
print(np.log(arr))      # Natural logarithm
print(np.sin(arr))      # Sine
print(np.cos(arr))      # Cosine

# Rounding
arr_float = np.array([1.2, 2.7, 3.1, 4.9])
print(np.round(arr_float))      # [1, 3, 3, 5]
print(np.floor(arr_float))      # [1, 2, 3, 4]
print(np.ceil(arr_float))       # [2, 3, 4, 5]
```

## Array Manipulation

### Reshaping
```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape
reshaped = arr.reshape(2, 3)    # [[1, 2, 3], [4, 5, 6]]
reshaped = arr.reshape(3, -1)   # -1 means "figure out this dimension"

# Flatten
arr2d = np.array([[1, 2], [3, 4]])
flattened = arr2d.flatten()     # [1, 2, 3, 4]
ravel = arr2d.ravel()           # [1, 2, 3, 4] (view, not copy)
```

### Joining Arrays
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate
concat = np.concatenate([arr1, arr2])       # [1, 2, 3, 4, 5, 6]

# Stack
vstack = np.vstack([arr1, arr2])            # [[1, 2, 3], [4, 5, 6]]
hstack = np.hstack([arr1, arr2])            # [1, 2, 3, 4, 5, 6]

# 2D arrays
arr2d1 = np.array([[1, 2], [3, 4]])
arr2d2 = np.array([[5, 6], [7, 8]])
concat_axis0 = np.concatenate([arr2d1, arr2d2], axis=0)  # Vertical
concat_axis1 = np.concatenate([arr2d1, arr2d2], axis=1)  # Horizontal
```

### Splitting Arrays
```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Split into equal parts
split = np.split(arr, 3)        # [array([1, 2]), array([3, 4]), array([5, 6])]

# Split at specific indices
split_at = np.split(arr, [2, 4])  # Split at indices 2 and 4

# 2D splitting
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
hsplit = np.hsplit(arr2d, 2)    # Split horizontally
vsplit = np.vsplit(arr2d, 2)    # Split vertically
```

## Statistical Operations

### Basic Statistics
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Basic stats
print(np.mean(arr))         # 3.5 (overall mean)
print(np.median(arr))       # 3.5 (overall median)
print(np.std(arr))          # Standard deviation
print(np.var(arr))          # Variance
print(np.min(arr))          # 1 (minimum)
print(np.max(arr))          # 6 (maximum)
print(np.sum(arr))          # 21 (sum of all elements)

# Along specific axis
print(np.mean(arr, axis=0)) # [2.5, 3.5, 4.5] (column means)
print(np.mean(arr, axis=1)) # [2, 5] (row means)
print(np.sum(arr, axis=0))  # [5, 7, 9] (column sums)
```

### Other Statistical Functions
```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

print(np.argmin(arr))       # 1 (index of minimum)
print(np.argmax(arr))       # 5 (index of maximum)
print(np.argsort(arr))      # [1, 3, 6, 0, 2, 7, 4, 5] (indices that sort array)
print(np.percentile(arr, 50))  # 3.5 (50th percentile)
print(np.unique(arr))       # [1, 2, 3, 4, 5, 6, 9] (unique values)
```

## Linear Algebra

### Matrix Operations
```python
# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product
dot_product = np.dot(A, B)      # Matrix multiplication
# or
dot_product = A @ B             # Python 3.5+ syntax

# Element-wise multiplication
element_wise = A * B

# Transpose
A_T = A.T                       # or np.transpose(A)
```

### Linear Algebra Functions
```python
A = np.array([[1, 2], [3, 4]])

# Determinant
det = np.linalg.det(A)

# Inverse
inv = np.linalg.inv(A)

# Eigenvalues and eigenvectors
eigenvals, eigenvecs = np.linalg.eig(A)

# Solve linear system Ax = b
b = np.array([5, 6])
x = np.linalg.solve(A, b)
```

## Broadcasting

### Broadcasting Rules
```python
# Broadcasting allows operations between arrays of different shapes
arr = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
scalar = 10                               # Shape: ()

result = arr + scalar                     # Adds 10 to each element

# Broadcasting with different shapes
arr1 = np.array([[1], [2], [3]])         # Shape: (3, 1)
arr2 = np.array([10, 20, 30])            # Shape: (3,)

result = arr1 + arr2                      # Shape: (3, 3)
# [[11, 21, 31],
#  [12, 22, 32],
#  [13, 23, 33]]
```

## Working with NaN and Infinity

### Handling Missing Data
```python
# Create array with NaN
arr = np.array([1, 2, np.nan, 4, 5])

# Check for NaN
print(np.isnan(arr))            # [False, False, True, False, False]
print(np.isfinite(arr))         # [True, True, False, True, True]

# NaN-aware functions
print(np.nanmean(arr))          # 3.0 (ignores NaN)
print(np.nansum(arr))           # 12.0 (ignores NaN)
print(np.nanmax(arr))           # 5.0 (ignores NaN)

# Remove NaN values
clean_arr = arr[~np.isnan(arr)] # [1, 2, 4, 5]
```

## File I/O

### Saving and Loading Arrays
```python
arr = np.array([1, 2, 3, 4, 5])

# Save to binary format
np.save('array.npy', arr)
loaded_arr = np.load('array.npy')

# Save multiple arrays
np.savez('arrays.npz', arr1=arr, arr2=arr*2)
loaded = np.load('arrays.npz')
print(loaded['arr1'])
print(loaded['arr2'])

# Save to text format
np.savetxt('array.txt', arr)
loaded_txt = np.loadtxt('array.txt')

# CSV format
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('array.csv', arr2d, delimiter=',')
loaded_csv = np.loadtxt('array.csv', delimiter=',')
```

## Performance Tips

### Vectorization
```python
# Slow: Python loop
def slow_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i] ** 2
    return total

# Fast: NumPy vectorized
def fast_sum(arr):
    return np.sum(arr ** 2)

# Use NumPy functions instead of Python loops
arr = np.random.random(1000000)
# fast_sum(arr) is much faster than slow_sum(arr)
```

### Memory Efficiency
```python
# Use appropriate data types
arr_int8 = np.array([1, 2, 3], dtype=np.int8)      # 1 byte per element
arr_int64 = np.array([1, 2, 3], dtype=np.int64)    # 8 bytes per element

# Use views instead of copies when possible
arr = np.array([1, 2, 3, 4, 5])
view = arr[::2]         # View (shares memory)
copy = arr[::2].copy()  # Copy (new memory)

# Check if array is a view or copy
print(view.base is arr)     # True (view)
print(copy.base is None)    # True (copy)
```

## Common Patterns

### Data Normalization
```python
# Z-score normalization
data = np.random.normal(100, 15, 1000)
normalized = (data - np.mean(data)) / np.std(data)

# Min-max normalization
min_max_norm = (data - np.min(data)) / (np.max(data) - np.min(data))
```

### Finding Elements
```python
arr = np.array([1, 5, 3, 8, 2, 7])

# Find indices where condition is true
indices = np.where(arr > 5)         # (array([1, 3, 5]),)
values = arr[arr > 5]               # [5, 8, 7]

# Find first occurrence
first_index = np.argmax(arr > 5)    # 1 (first index where condition is True)
```

### Array Comparison
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 4])

# Element-wise comparison
print(np.array_equal(arr1, arr2))   # False
print(np.allclose(arr1, arr2))      # False (within tolerance)

# Check if all/any elements satisfy condition
print(np.all(arr1 > 0))             # True (all elements > 0)
print(np.any(arr1 > 2))             # True (any element > 2)
```