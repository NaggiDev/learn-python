# Lists and List Comprehensions

## Introduction

Lists are one of the most versatile and commonly used data structures in Python. A list is an ordered collection of items that can be of different types. Lists are mutable, which means you can change their content without changing their identity.

In this lesson, you will learn how to create, access, and manipulate lists, as well as how to use list comprehensions for concise and efficient data transformation.

## Creating Lists

There are several ways to create lists in Python:

### Using square brackets

```python
# Empty list
empty_list = []

# List of integers
numbers = [1, 2, 3, 4, 5]

# List of mixed data types
mixed = [1, "Hello", 3.14, True]

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Using the `list()` constructor

```python
# Creating a list from a string
chars = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']

# Creating a list from a tuple
tuple_to_list = list((1, 2, 3))  # [1, 2, 3]

# Creating a list from a range
range_to_list = list(range(5))  # [0, 1, 2, 3, 4]
```

## Accessing List Elements

Lists are indexed starting from 0 for the first element.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Accessing by positive index (from the beginning)
print(fruits[0])  # "apple"
print(fruits[2])  # "cherry"

# Accessing by negative index (from the end)
print(fruits[-1])  # "elderberry"
print(fruits[-3])  # "cherry"
```

## List Slicing

You can access a range of items in a list using slicing.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Basic slicing [start:stop] (stop is exclusive)
print(fruits[1:4])  # ["banana", "cherry", "date"]

# Omitting start (defaults to 0)
print(fruits[:3])  # ["apple", "banana", "cherry"]

# Omitting stop (defaults to length of list)
print(fruits[2:])  # ["cherry", "date", "elderberry"]

# Negative indices in slicing
print(fruits[-3:-1])  # ["cherry", "date"]

# Step parameter [start:stop:step]
print(fruits[::2])  # ["apple", "cherry", "elderberry"]

# Reversing a list
print(fruits[::-1])  # ["elderberry", "date", "cherry", "banana", "apple"]
```

## Common List Operations

### Modifying Elements

```python
numbers = [1, 2, 3, 4, 5]

# Changing a single element
numbers[2] = 30
print(numbers)  # [1, 2, 30, 4, 5]

# Changing multiple elements using slicing
numbers[1:4] = [20, 30, 40]
print(numbers)  # [1, 20, 30, 40, 5]

# Changing with a different number of elements
numbers[1:4] = [200]
print(numbers)  # [1, 200, 5]
```

### Adding Elements

```python
fruits = ["apple", "banana"]

# Append: add an item to the end
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# Insert: add an item at a specific position
fruits.insert(1, "blueberry")
print(fruits)  # ["apple", "blueberry", "banana", "cherry"]

# Extend: add multiple items to the end
fruits.extend(["date", "elderberry"])
print(fruits)  # ["apple", "blueberry", "banana", "cherry", "date", "elderberry"]

# Concatenation: combine lists with +
more_fruits = fruits + ["fig", "grape"]
print(more_fruits)  # ["apple", "blueberry", "banana", "cherry", "date", "elderberry", "fig", "grape"]
```

### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "date", "banana", "elderberry"]

# Remove: removes the first occurrence of a value
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "date", "banana", "elderberry"]

# Pop: removes and returns an item at a given position (default is last)
popped = fruits.pop(1)
print(popped)  # "cherry"
print(fruits)  # ["apple", "date", "banana", "elderberry"]

# Del statement: removes items or slices
del fruits[0]
print(fruits)  # ["date", "banana", "elderberry"]

del fruits[1:]
print(fruits)  # ["date"]

# Clear: removes all items
fruits.clear()
print(fruits)  # []
```

### Finding Elements

```python
fruits = ["apple", "banana", "cherry", "date", "banana", "elderberry"]

# Index: finds the position of the first occurrence
position = fruits.index("banana")
print(position)  # 1

# Count: counts occurrences of a value
banana_count = fruits.count("banana")
print(banana_count)  # 2

# In operator: checks if an item exists
has_cherry = "cherry" in fruits
print(has_cherry)  # True

has_fig = "fig" in fruits
print(has_fig)  # False
```

### Other Common Operations

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort: arranges items in ascending order
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse: reverses the order of items
numbers.reverse()
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Sorted: returns a new sorted list without modifying the original
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5] (unchanged)
print(sorted_list)  # [1, 1, 3, 4, 5]

# Length: number of items
length = len(original)
print(length)  # 5

# Min and Max: smallest and largest values
minimum = min(original)
maximum = max(original)
print(minimum)  # 1
print(maximum)  # 5

# Sum: total of all values (numeric lists only)
total = sum(original)
print(total)  # 14
```

## Nested Lists

Lists can contain other lists, creating multi-dimensional structures.

```python
# Creating a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in nested lists
print(matrix[1][2])  # 6 (row 1, column 2)

# Modifying elements in nested lists
matrix[0][1] = 20
print(matrix)  # [[1, 20, 3], [4, 5, 6], [7, 8, 9]]

# Iterating through a matrix
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row
# Output:
# 1 20 3
# 4 5 6
# 7 8 9
```

## List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists or other iterable objects.

### Basic Syntax

```
[expression for item in iterable]
```

### Simple Examples

```python
# Creating a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Converting strings to uppercase
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)  # ["APPLE", "BANANA", "CHERRY"]
```

### With Conditional Filtering

```
[expression for item in iterable if condition]
```

```python
# Only even numbers
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Only fruits with more than 5 characters
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(long_fruits)  # ["banana", "cherry", "elderberry"]
```

### Nested List Comprehensions

```python
# Flattening a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creating a matrix of multiplication table
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in multiplication_table:
    print(row)
# Output:
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
# [5, 10, 15, 20, 25]
```

### If-Else in List Comprehensions

```
[expression_if_true if condition else expression_if_false for item in iterable]
```

```python
# Replace negative numbers with zero
numbers = [1, -2, 3, -4, 5]
non_negative = [num if num >= 0 else 0 for num in numbers]
print(non_negative)  # [1, 0, 3, 0, 5]

# Categorize numbers as 'even' or 'odd'
numbers = [1, 2, 3, 4, 5]
categorized = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(categorized)  # ["odd", "even", "odd", "even", "odd"]
```

## When to Use Lists

Lists are ideal when you need:

1. An ordered collection of items
2. A mutable sequence that can be modified
3. To store items of different types
4. To access elements by position
5. To perform operations like sorting, reversing, or appending

## Performance Considerations

- Lists are efficient for most operations, but some operations have specific performance characteristics:
  - Accessing by index: O(1) - constant time
  - Appending to the end: O(1) - constant time (amortized)
  - Inserting or deleting at the beginning or middle: O(n) - linear time
  - Searching for an element: O(n) - linear time
  - Sorting: O(n log n) - linearithmic time

## Common Pitfalls

### Modifying a List While Iterating

```python
# Incorrect way - unpredictable results
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # This modifies the list during iteration!
print(numbers)  # Result may not be as expected

# Correct way - create a new list
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)  # [1, 3, 5]
```

### List References vs. Copies

```python
# Lists are reference types
list1 = [1, 2, 3]
list2 = list1  # list2 references the same list as list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - list1 is also modified!

# Creating a copy
list1 = [1, 2, 3]
list2 = list1.copy()  # or list2 = list1[:]
list2.append(4)
print(list1)  # [1, 2, 3] - list1 is unchanged
print(list2)  # [1, 2, 3, 4]
```

## Summary

- Lists are ordered, mutable collections that can store items of different types
- Lists support indexing, slicing, and various methods for manipulation
- List comprehensions provide a concise way to create and transform lists
- Lists are versatile but have specific performance characteristics to consider

In the next lesson, we'll explore tuples, which are similar to lists but with some important differences in terms of mutability and use cases.