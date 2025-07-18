# Sets

## Introduction

Sets are unordered collections of unique elements in Python. They are mutable, iterable, and can contain only hashable objects (immutable types like strings, numbers, and tuples containing only hashable objects). Sets are particularly useful for membership testing, removing duplicates from a sequence, and performing mathematical set operations like unions, intersections, and differences.

In this lesson, you will learn how to create and manipulate sets, understand their properties, and explore common set operations and use cases.

## Creating Sets

There are several ways to create sets in Python:

### Using curly braces

```python
# Empty set (Note: {} creates an empty dictionary, not a set)
empty_set = set()

# Set with elements
fruits = {"apple", "banana", "cherry"}

# Set with mixed data types
mixed = {1, "Hello", 3.14, True}
```

### Using the `set()` constructor

```python
# Creating a set from a list
numbers = set([1, 2, 3, 4, 5])

# Creating a set from a string
chars = set("Python")  # {'P', 'y', 't', 'h', 'o', 'n'}

# Creating a set from a tuple
tuple_to_set = set((1, 2, 3, 2, 1))  # {1, 2, 3}
```

### Set comprehensions

```python
# Creating a set of squares
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Creating a set with a condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}
```

## Set Properties

Sets have several important properties:

1. **Unordered**: Elements in a set have no defined order. You cannot access elements by index.
2. **Unique Elements**: Sets automatically eliminate duplicates.
3. **Mutable**: You can add or remove elements after creation.
4. **Hashable Elements**: Set elements must be immutable (hashable).

```python
# Demonstrating uniqueness
numbers = {1, 2, 3, 2, 1, 4, 5, 4}
print(numbers)  # {1, 2, 3, 4, 5}

# Demonstrating unordered nature
print({3, 1, 2} == {1, 2, 3})  # True (order doesn't matter)

# Demonstrating mutability
fruits = {"apple", "banana", "cherry"}
fruits.add("date")
print(fruits)  # {'apple', 'banana', 'cherry', 'date'}

# Demonstrating hashable elements requirement
try:
    invalid_set = {[1, 2], 3}  # Lists are mutable, so not hashable
except TypeError as e:
    print(f"Error: {e}")  # Error: unhashable type: 'list'
```

## Basic Set Operations

### Adding Elements

```python
fruits = {"apple", "banana", "cherry"}

# add(): adds a single element
fruits.add("date")
print(fruits)  # {'apple', 'banana', 'cherry', 'date'}

# update(): adds multiple elements
fruits.update(["elderberry", "fig"])
print(fruits)  # {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'}

# update() can take any iterable
fruits.update("grape")  # Adds each character as an element
print(fruits)  # {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'g', 'r', 'a', 'p', 'e'}
```

### Removing Elements

```python
fruits = {"apple", "banana", "cherry", "date", "elderberry"}

# remove(): removes an element, raises KeyError if not found
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry', 'date', 'elderberry'}

try:
    fruits.remove("fig")  # 'fig' is not in the set
except KeyError as e:
    print(f"Error: {e}")  # Error: 'fig'

# discard(): removes an element if present, does nothing if not found
fruits.discard("cherry")
print(fruits)  # {'apple', 'date', 'elderberry'}
fruits.discard("fig")  # No error

# pop(): removes and returns an arbitrary element
element = fruits.pop()
print(element)  # Could be any element from the set
print(fruits)   # Set without the popped element

# clear(): removes all elements
fruits.clear()
print(fruits)  # set()
```

## Set Operations (Mathematical)

Sets support mathematical operations that correspond to set theory operations:

### Union

The union of two sets is a set containing all elements from both sets.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using the | operator
union = set1 | set2
print(union)  # {1, 2, 3, 4, 5, 6}

# Using the union() method
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5, 6}

# union() can take multiple arguments
set3 = {5, 6, 7, 8}
union = set1.union(set2, set3)
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}
```

### Intersection

The intersection of two sets is a set containing only elements that are in both sets.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using the & operator
intersection = set1 & set2
print(intersection)  # {3, 4}

# Using the intersection() method
intersection = set1.intersection(set2)
print(intersection)  # {3, 4}

# intersection() can take multiple arguments
set3 = {4, 5, 6, 7}
intersection = set1.intersection(set2, set3)
print(intersection)  # {4}
```

### Difference

The difference between two sets is a set containing elements that are in the first set but not in the second.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using the - operator
difference = set1 - set2
print(difference)  # {1, 2}

# Using the difference() method
difference = set1.difference(set2)
print(difference)  # {1, 2}

# difference() can take multiple arguments
set3 = {2, 3, 4, 5}
difference = set1.difference(set2, set3)
print(difference)  # {1}
```

### Symmetric Difference

The symmetric difference between two sets is a set containing elements that are in either of the sets, but not in both.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using the ^ operator
sym_diff = set1 ^ set2
print(sym_diff)  # {1, 2, 5, 6}

# Using the symmetric_difference() method
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # {1, 2, 5, 6}
```

## Set Comparison Operations

Sets support comparison operations to check for subset, superset, and disjoint relationships:

### Subset and Superset

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Checking if set1 is a subset of set2
is_subset = set1 <= set2
print(is_subset)  # True

# Using the issubset() method
is_subset = set1.issubset(set2)
print(is_subset)  # True

# Checking if set1 is a proper subset of set2 (subset but not equal)
is_proper_subset = set1 < set2
print(is_proper_subset)  # True

# Checking if set2 is a superset of set1
is_superset = set2 >= set1
print(is_superset)  # True

# Using the issuperset() method
is_superset = set2.issuperset(set1)
print(is_superset)  # True

# Checking if set2 is a proper superset of set1 (superset but not equal)
is_proper_superset = set2 > set1
print(is_proper_superset)  # True
```

### Disjoint Sets

Two sets are disjoint if they have no elements in common.

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

# Checking if set1 and set2 are disjoint
are_disjoint = set1.isdisjoint(set2)
print(are_disjoint)  # True

# Checking if set1 and set3 are disjoint
are_disjoint = set1.isdisjoint(set3)
print(are_disjoint)  # False (they share element 3)
```

## Frozen Sets

Python also provides an immutable version of sets called `frozenset`. Once created, a frozen set cannot be modified.

```python
# Creating a frozen set
frozen = frozenset([1, 2, 3, 4])
print(frozen)  # frozenset({1, 2, 3, 4})

# Attempting to modify a frozen set
try:
    frozen.add(5)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")  # Error: 'frozenset' object has no attribute 'add'

# Frozen sets can be used as dictionary keys or elements of another set
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(set_of_sets)  # {frozenset({1, 2}), frozenset({3, 4})}
```

## Common Set Use Cases

### Removing Duplicates from a List

```python
# Converting a list to a set removes duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5] (order may vary)

# To preserve order in Python 3.7+, use dict.fromkeys()
unique_ordered = list(dict.fromkeys(numbers))
print(unique_ordered)  # [1, 2, 3, 4, 5]
```

### Membership Testing

```python
fruits = {"apple", "banana", "cherry"}

# Checking if an element is in a set
has_apple = "apple" in fruits
print(has_apple)  # True

has_date = "date" in fruits
print(has_date)  # False
```

### Finding Unique Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Elements unique to list1
unique_to_list1 = set(list1) - set(list2)
print(unique_to_list1)  # {1, 2, 3}

# Elements unique to list2
unique_to_list2 = set(list2) - set(list1)
print(unique_to_list2)  # {6, 7, 8}

# Elements unique to either list (not in both)
unique_elements = set(list1) ^ set(list2)
print(unique_elements)  # {1, 2, 3, 6, 7, 8}
```

### Finding Common Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Elements common to both lists
common_elements = set(list1) & set(list2)
print(common_elements)  # {4, 5}
```

## Set Performance

Sets are implemented using hash tables, which provide very efficient operations:

- Membership testing (`x in s`): O(1) average case
- Adding an element (`s.add(x)`): O(1) average case
- Removing an element (`s.remove(x)`): O(1) average case
- Set operations (union, intersection, etc.): O(len(s) + len(t)) average case

This makes sets ideal for operations that involve frequent membership testing or elimination of duplicates.

## When to Use Sets

Sets are ideal when you need:

1. **Unique elements**: Automatically eliminate duplicates
2. **Fast membership testing**: Check if an element exists in O(1) time
3. **Mathematical set operations**: Perform unions, intersections, differences
4. **Removing duplicates from a sequence**: Convert to a set and back
5. **Tracking visited items**: Keep track of items you've already processed

## Sets vs. Other Data Structures

| Feature | Set | List | Dictionary | Tuple |
|---------|-----|------|------------|-------|
| Ordering | Unordered | Ordered | Ordered (Python 3.7+) | Ordered |
| Mutability | Mutable | Mutable | Mutable | Immutable |
| Duplicates | No duplicates | Allows duplicates | No duplicate keys | Allows duplicates |
| Indexing | No indexing | By position | By key | By position |
| Use case | Unique items | Ordered collection | Key-value mapping | Fixed collection |
| Membership testing | O(1) average | O(n) | O(1) average | O(n) |

## Common Pitfalls

### Modifying a Set While Iterating

```python
# Incorrect way - RuntimeError
numbers = {1, 2, 3, 4, 5}
try:
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)  # This modifies the set during iteration!
except RuntimeError as e:
    print(f"Error: {e}")

# Correct way - create a copy for iteration
numbers = {1, 2, 3, 4, 5}
for num in numbers.copy():
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # {1, 3, 5}

# Alternative way - create a new set
numbers = {1, 2, 3, 4, 5}
odd_numbers = {num for num in numbers if num % 2 != 0}
print(odd_numbers)  # {1, 3, 5}
```

### Assuming Order in Sets

```python
# Sets are unordered
colors = {"red", "green", "blue"}
print(colors)  # Order is not guaranteed

# If order matters, use a list or maintain a separate ordered structure
colors_list = ["red", "green", "blue"]
colors_set = set(colors_list)  # For fast membership testing
```

### Using Mutable Objects as Set Elements

```python
# This will raise a TypeError
try:
    invalid_set = {[1, 2], (3, 4)}
except TypeError as e:
    print(f"Error: {e}")  # Error: unhashable type: 'list'

# Use tuples instead of lists for set elements
valid_set = {(1, 2), (3, 4)}
print(valid_set)  # {(1, 2), (3, 4)}
```

## Advanced Set Features

### Set Comprehensions

```python
# Basic set comprehension
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Set comprehension with a condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}

# Set comprehension with multiple conditions
complex_set = {x for x in range(100) if x % 2 == 0 if x % 5 == 0}
print(complex_set)  # {0, 10, 20, 30, 40, 50, 60, 70, 80, 90}
```

### Set Operations with Update Methods

Sets provide methods that perform operations and update the set in-place:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# update(): union in-place
set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5, 6}

# intersection_update(): intersection in-place
set1 = {1, 2, 3, 4}
set1.intersection_update(set2)
print(set1)  # {3, 4}

# difference_update(): difference in-place
set1 = {1, 2, 3, 4}
set1.difference_update(set2)
print(set1)  # {1, 2}

# symmetric_difference_update(): symmetric difference in-place
set1 = {1, 2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)  # {1, 2, 5, 6}
```

## Summary

- Sets are unordered collections of unique, hashable elements
- Sets are mutable and support adding and removing elements
- Sets provide efficient membership testing and elimination of duplicates
- Sets support mathematical operations like union, intersection, and difference
- Sets are ideal for tasks involving unique elements and frequent membership testing
- Frozen sets provide an immutable alternative to regular sets

In the next lesson, we'll explore string manipulation, which involves working with text data using Python's powerful string methods and operations.