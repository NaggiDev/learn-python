# Recursion and Recursive Algorithms

## Introduction

Recursion is a powerful programming technique where a function calls itself to solve smaller instances of the same problem. It's particularly useful for problems that have a recursive structure, such as tree traversals, mathematical sequences, and divide-and-conquer algorithms.

## Understanding Recursion

### What is Recursion?

Recursion occurs when a function calls itself with modified parameters, gradually working toward a base case that stops the recursive calls. Every recursive solution has two essential components:

1. **Base Case**: The condition that stops the recursion
2. **Recursive Case**: The function calling itself with a simpler version of the problem

### Simple Example: Factorial

```python
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
print(factorial(5))  # Output: 120
```

### How Recursion Works: The Call Stack

When a recursive function is called, each call is added to the call stack:

```
factorial(5)
├── 5 * factorial(4)
    ├── 4 * factorial(3)
        ├── 3 * factorial(2)
            ├── 2 * factorial(1)
                └── 1 (base case)
```

The stack unwinds as each call returns:
- factorial(1) returns 1
- factorial(2) returns 2 * 1 = 2
- factorial(3) returns 3 * 2 = 6
- factorial(4) returns 4 * 6 = 24
- factorial(5) returns 5 * 24 = 120

## Types of Recursion

### 1. Linear Recursion

Each function makes at most one recursive call:

```python
def sum_array(arr, index=0):
    # Base case: reached end of array
    if index >= len(arr):
        return 0
    
    # Recursive case: current element + sum of rest
    return arr[index] + sum_array(arr, index + 1)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(sum_array(numbers))  # Output: 15
```

### 2. Binary Recursion

Each function makes two recursive calls:

```python
def fibonacci(n):
    # Base cases
    if n <= 1:
        return n
    
    # Two recursive calls
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(fibonacci(6))  # Output: 8
```

### 3. Tail Recursion

The recursive call is the last operation in the function:

```python
def factorial_tail_recursive(n, accumulator=1):
    # Base case
    if n <= 1:
        return accumulator
    
    # Tail recursive call
    return factorial_tail_recursive(n - 1, n * accumulator)

# Example usage
print(factorial_tail_recursive(5))  # Output: 120
```

### 4. Mutual Recursion

Two or more functions call each other:

```python
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

# Example usage
print(is_even(4))  # Output: True
print(is_odd(4))   # Output: False
```

## Classic Recursive Problems

### 1. Tree Traversal

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """Left -> Root -> Right"""
    if not root:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))   # Left subtree
    result.append(root.val)                       # Root
    result.extend(inorder_traversal(root.right))  # Right subtree
    
    return result
```

### 2. Binary Search

```python
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    
    # Recursive cases
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)
```

### 3. Merge Sort

```python
def merge_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Conquer
    return merge(left_half, right_half)

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
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

## Recursion Optimization Techniques

### 1. Memoization

Store results of expensive function calls to avoid redundant calculations:

```python
def fibonacci_memoized(n, memo=None):
    if memo is None:
        memo = {}
    
    # Check if result is already computed
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 1:
        return n
    
    # Compute and store result
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Much faster than naive fibonacci for large n
print(fibonacci_memoized(50))  # Computes quickly
```

### 2. Dynamic Programming (Bottom-Up)

Build solutions from smaller subproblems:

```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    
    # Build solution bottom-up
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

### 3. Tail Recursion Optimization

Convert to iterative form to avoid stack overflow:

```python
def factorial_iterative(n):
    """Convert tail recursion to iteration"""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
```

## Common Recursion Patterns

### 1. Divide and Conquer

Break problem into smaller subproblems, solve recursively, combine results:

```python
def max_subarray_sum(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    # Base case
    if left == right:
        return arr[left]
    
    # Divide
    mid = (left + right) // 2
    
    # Conquer
    left_sum = max_subarray_sum(arr, left, mid)
    right_sum = max_subarray_sum(arr, mid + 1, right)
    
    # Combine: find max crossing sum
    left_cross_sum = float('-inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]
        left_cross_sum = max(left_cross_sum, current_sum)
    
    right_cross_sum = float('-inf')
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += arr[i]
        right_cross_sum = max(right_cross_sum, current_sum)
    
    cross_sum = left_cross_sum + right_cross_sum
    
    return max(left_sum, right_sum, cross_sum)
```

### 2. Backtracking

Explore all possible solutions, backtrack when hitting dead ends:

```python
def generate_permutations(nums):
    def backtrack(current_permutation):
        # Base case: permutation is complete
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])
            return
        
        # Try each remaining number
        for num in nums:
            if num not in current_permutation:
                current_permutation.append(num)
                backtrack(current_permutation)
                current_permutation.pop()  # Backtrack
    
    result = []
    backtrack([])
    return result

# Example usage
print(generate_permutations([1, 2, 3]))
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

### 3. Tree Recursion

Process tree-like structures:

```python
def tree_height(root):
    # Base case: empty tree
    if not root:
        return 0
    
    # Recursive case: 1 + max height of subtrees
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)
```

## Debugging Recursive Functions

### 1. Add Print Statements

```python
def factorial_debug(n, depth=0):
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    
    if n <= 1:
        print(f"{indent}Base case: returning 1")
        return 1
    
    result = n * factorial_debug(n - 1, depth + 1)
    print(f"{indent}factorial({n}) returning {result}")
    return result
```

### 2. Trace Execution

```python
def trace_fibonacci(n, call_stack=None):
    if call_stack is None:
        call_stack = []
    
    call_stack.append(f"fib({n})")
    print(" -> ".join(call_stack))
    
    if n <= 1:
        call_stack.pop()
        return n
    
    result = (trace_fibonacci(n - 1, call_stack) + 
              trace_fibonacci(n - 2, call_stack))
    
    call_stack.pop()
    return result
```

## When to Use Recursion

### Good Use Cases:
- **Tree and graph traversals**
- **Divide-and-conquer algorithms**
- **Mathematical sequences and formulas**
- **Backtracking problems**
- **Problems with recursive structure**

### When to Avoid:
- **Simple iterative solutions exist**
- **Deep recursion causing stack overflow**
- **Excessive redundant calculations**
- **Performance-critical code**

## Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| **Readability** | Often cleaner for recursive problems | Can be more verbose |
| **Performance** | Function call overhead | Generally faster |
| **Memory** | Uses call stack | Uses less memory |
| **Stack Overflow** | Risk with deep recursion | No risk |
| **Debugging** | Can be harder to trace | Easier to debug |

## Best Practices

1. **Always define base cases clearly**
2. **Ensure progress toward base case**
3. **Consider iterative alternatives for performance**
4. **Use memoization for overlapping subproblems**
5. **Be mindful of stack depth limits**
6. **Test with small inputs first**
7. **Document the recursive relationship**

## Common Mistakes

1. **Missing or incorrect base case**
2. **Infinite recursion (no progress toward base case)**
3. **Stack overflow from deep recursion**
4. **Inefficient recursive solutions (like naive Fibonacci)**
5. **Not considering iterative alternatives**

## Summary

Recursion is a powerful technique that can elegantly solve problems with recursive structure. Key points to remember:

- Every recursive function needs a base case and recursive case
- Recursion uses the call stack, which has memory implications
- Many recursive problems can benefit from optimization techniques
- Consider both recursive and iterative approaches
- Practice with classic problems to build intuition

Understanding recursion deeply will help you tackle complex algorithmic problems and write more elegant solutions for naturally recursive problems.

In the next lesson, we'll explore searching and sorting algorithms, many of which use recursive techniques like divide-and-conquer.