# Searching and Sorting Algorithms

## Introduction

Searching and sorting are fundamental operations in computer science. Efficient algorithms for these operations are crucial for building performant applications. This lesson covers the most important searching and sorting algorithms, their implementations, complexity analysis, and when to use each one.

## Searching Algorithms

Searching algorithms find the location of a specific element in a data structure. The choice of algorithm depends on whether the data is sorted and the specific requirements of your application.

### 1. Linear Search

Linear search examines each element sequentially until the target is found or the end is reached.

```python
def linear_search(arr, target):
    """
    Search for target in array using linear search.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
index = linear_search(numbers, 22)
print(f"Element found at index: {index}")  # Output: 4
```

**Characteristics:**
- Works on both sorted and unsorted arrays
- Simple to implement
- Best case: O(1) - element is first
- Average case: O(n/2) = O(n)
- Worst case: O(n) - element is last or not present

### 2. Binary Search

Binary search works on sorted arrays by repeatedly dividing the search space in half.

```python
def binary_search(arr, target):
    """
    Search for target in sorted array using binary search.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
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

# Example usage
sorted_numbers = [11, 12, 22, 25, 34, 64, 90]
index = binary_search(sorted_numbers, 25)
print(f"Element found at index: {index}")  # Output: 3
```

**Characteristics:**
- Requires sorted array
- Much faster than linear search for large datasets
- All cases: O(log n)

### 3. Interpolation Search

An improvement over binary search for uniformly distributed sorted arrays.

```python
def interpolation_search(arr, target):
    """
    Search using interpolation search (for uniformly distributed data).
    Time Complexity: O(log log n) average, O(n) worst case
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        # If array has only one element
        if left == right:
            return left if arr[left] == target else -1
        
        # Calculate position using interpolation formula
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1
```

## Sorting Algorithms

Sorting algorithms arrange elements in a specific order (usually ascending or descending). Different algorithms have different trade-offs in terms of time complexity, space complexity, and stability.

### 1. Bubble Sort

Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.

```python
def bubble_sort(arr):
    """
    Sort array using bubble sort.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    """
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize - if no swaps occur, array is sorted
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers.copy())
print(f"Sorted array: {sorted_numbers}")
```

**Characteristics:**
- Simple to understand and implement
- Stable (maintains relative order of equal elements)
- Inefficient for large datasets
- Best case: O(n) when array is already sorted

### 2. Selection Sort

Selection sort finds the minimum element and places it at the beginning, then repeats for the remaining elements.

```python
def selection_sort(arr):
    """
    Sort array using selection sort.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: No
    """
    n = len(arr)
    
    for i in range(n):
        # Find minimum element in remaining array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum element with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
```

**Characteristics:**
- Simple implementation
- Not stable
- Always O(n²) regardless of input
- Minimizes number of swaps

### 3. Insertion Sort

Insertion sort builds the sorted array one element at a time by inserting each element into its correct position.

```python
def insertion_sort(arr):
    """
    Sort array using insertion sort.
    Time Complexity: O(n²) worst case, O(n) best case
    Space Complexity: O(1)
    Stable: Yes
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert key at correct position
        arr[j + 1] = key
    
    return arr
```

**Characteristics:**
- Efficient for small datasets
- Stable
- Adaptive (efficient for nearly sorted arrays)
- Online (can sort as it receives data)

### 4. Merge Sort

Merge sort uses divide-and-conquer: divide the array into halves, sort each half, then merge them.

```python
def merge_sort(arr):
    """
    Sort array using merge sort.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Stable: Yes
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left_half, right_half)

def merge(left, right):
    """Helper function to merge two sorted arrays."""
    result = []
    i = j = 0
    
    # Merge elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

**Characteristics:**
- Consistent O(n log n) performance
- Stable
- Requires additional space
- Good for large datasets

### 5. Quick Sort

Quick sort picks a pivot element and partitions the array around it, then recursively sorts the partitions.

```python
def quick_sort(arr, low=0, high=None):
    """
    Sort array using quick sort.
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) average
    Stable: No
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array and get pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    """Partition function for quick sort."""
    # Choose rightmost element as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Characteristics:**
- Fast average case performance
- In-place sorting (low space complexity)
- Not stable
- Performance depends on pivot selection

### 6. Heap Sort

Heap sort uses a binary heap data structure to sort elements.

```python
def heap_sort(arr):
    """
    Sort array using heap sort.
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    Stable: No
    """
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call heapify on reduced heap
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """Maintain heap property."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

**Characteristics:**
- Consistent O(n log n) performance
- In-place sorting
- Not stable
- Good worst-case performance

## Algorithm Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | Notes |
|-----------|-----------|--------------|------------|-------|--------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Simple, inefficient |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No | Minimizes swaps |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Good for small/nearly sorted |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Consistent performance |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Fast average case |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Good worst case |

## Advanced Sorting Techniques

### 1. Counting Sort

Counting sort works well when the range of input values is small.

```python
def counting_sort(arr, max_val=None):
    """
    Sort array using counting sort.
    Time Complexity: O(n + k) where k is range of input
    Space Complexity: O(k)
    Stable: Yes
    """
    if not arr:
        return arr
    
    if max_val is None:
        max_val = max(arr)
    
    # Create count array
    count = [0] * (max_val + 1)
    
    # Count occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Reconstruct sorted array
    result = []
    for i, freq in enumerate(count):
        result.extend([i] * freq)
    
    return result
```

### 2. Radix Sort

Radix sort sorts numbers digit by digit, starting from the least significant digit.

```python
def radix_sort(arr):
    """
    Sort array using radix sort.
    Time Complexity: O(d * (n + k)) where d is number of digits
    Space Complexity: O(n + k)
    Stable: Yes
    """
    if not arr:
        return arr
    
    # Find maximum number to know number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    """Helper function for radix sort."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences of each digit
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    # Change count[i] to actual position
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # Copy output array to arr
    for i in range(n):
        arr[i] = output[i]
```

## Choosing the Right Algorithm

### For Searching:
- **Small datasets**: Linear search is fine
- **Large sorted datasets**: Binary search
- **Uniformly distributed data**: Interpolation search
- **Unsorted data**: Linear search or sort first then binary search

### For Sorting:
- **Small datasets (< 50 elements)**: Insertion sort
- **Nearly sorted data**: Insertion sort
- **General purpose**: Quick sort or merge sort
- **Guaranteed O(n log n)**: Merge sort or heap sort
- **Memory constrained**: Heap sort or quick sort
- **Stability required**: Merge sort or insertion sort
- **Integer data with small range**: Counting sort or radix sort

## Optimization Techniques

### 1. Hybrid Approaches

Many real-world implementations use hybrid approaches:

```python
def hybrid_sort(arr, threshold=10):
    """
    Hybrid sort: Quick sort for large arrays, insertion sort for small ones.
    """
    if len(arr) <= threshold:
        return insertion_sort(arr)
    else:
        return quick_sort(arr)
```

### 2. Pivot Selection Strategies

For quick sort, better pivot selection improves performance:

```python
def median_of_three_pivot(arr, low, high):
    """Choose median of first, middle, and last elements as pivot."""
    mid = (low + high) // 2
    
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Place median at end
    arr[mid], arr[high] = arr[high], arr[mid]
    return arr[high]
```

### 3. Iterative Implementations

Convert recursive algorithms to iterative to avoid stack overflow:

```python
def quick_sort_iterative(arr):
    """Iterative implementation of quick sort."""
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_index = partition(arr, low, high)
            
            # Push left and right subarrays to stack
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    
    return arr
```

## Performance Analysis and Testing

### Benchmarking Different Algorithms

```python
import time
import random

def benchmark_sorting_algorithms(sizes=[100, 1000, 5000]):
    """Benchmark different sorting algorithms."""
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': lambda arr: quick_sort(arr.copy()),
        'Heap Sort': heap_sort
    }
    
    print(f"{'Algorithm':<15} {'Size':<8} {'Time (ms)':<12}")
    print("-" * 40)
    
    for size in sizes:
        # Generate random data
        data = [random.randint(1, 1000) for _ in range(size)]
        
        for name, algorithm in algorithms.items():
            test_data = data.copy()
            
            start_time = time.time()
            algorithm(test_data)
            end_time = time.time()
            
            elapsed_ms = (end_time - start_time) * 1000
            print(f"{name:<15} {size:<8} {elapsed_ms:<12.2f}")
        
        print()
```

## Real-World Applications

### 1. Database Indexing
- B-trees use sorting for efficient data retrieval
- Binary search on sorted indexes

### 2. Search Engines
- Sorting search results by relevance
- Merge sorted lists from different sources

### 3. Data Processing
- Sorting large datasets for analysis
- External sorting for data that doesn't fit in memory

### 4. Graphics and Games
- Sorting objects by depth for rendering
- Pathfinding algorithms use sorted priority queues

## Best Practices

1. **Know your data**: Choose algorithms based on data characteristics
2. **Consider stability**: Use stable sorts when order of equal elements matters
3. **Memory constraints**: Consider space complexity for large datasets
4. **Hybrid approaches**: Combine algorithms for optimal performance
5. **Profile and measure**: Always benchmark with real data
6. **Use library implementations**: Built-in sorts are usually optimized

## Summary

Understanding searching and sorting algorithms is crucial for:
- Writing efficient code
- Making informed algorithmic choices
- Optimizing application performance
- Solving complex computational problems

Key takeaways:
- Binary search is much faster than linear search for sorted data
- No single sorting algorithm is best for all situations
- Consider time complexity, space complexity, and stability
- Real-world implementations often use hybrid approaches
- Always profile with your actual data

In the next lesson, we'll explore tree and graph data structures, which build upon these fundamental algorithms.