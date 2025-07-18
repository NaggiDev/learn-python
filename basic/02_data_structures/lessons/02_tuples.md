# Tuples

## Introduction

Tuples are ordered, immutable collections of items in Python. Like lists, tuples can contain elements of different data types, but unlike lists, tuples cannot be modified after creation. This immutability makes tuples useful for representing fixed collections of data and provides certain performance advantages.

In this lesson, you will learn how to create and use tuples, understand their immutability, and explore common tuple operations and use cases.

## Creating Tuples

There are several ways to create tuples in Python:

### Using parentheses

```python
# Empty tuple
empty_tuple = ()

# Tuple with one element (note the comma)
singleton = (42,)  # Without the comma, it would be an integer in parentheses

# Tuple with multiple elements
numbers = (1, 2, 3, 4, 5)

# Tuple with mixed data types
mixed = (1, "Hello", 3.14, True)

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
```

### Using the tuple() constructor

```python
# Creating a tuple from a list
list_to_tuple = tuple([1, 2, 3])  # (1, 2, 3)

# Creating a tuple from a string
string_to_tuple = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')

# Creating a tuple from a range
range_to_tuple = tuple(range(5))  # (0, 1, 2, 3, 4)
```

### Tuple packing

You can create a tuple by simply separating values with commas, even without parentheses:

```python
# Tuple packing
coordinates = 3, 4  # This is a tuple (3, 4)
person = "John", 25, "Developer"  # This is a tuple ("John", 25, "Developer")
```

## Accessing Tuple Elements

Tuples use zero-based indexing, just like lists:

```python
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Accessing by positive index (from the beginning)
print(fruits[0])  # "apple"
print(fruits[2])  # "cherry"

# Accessing by negative index (from the end)
print(fruits[-1])  # "elderberry"
print(fruits[-3])  # "cherry"
```

## Tuple Slicing

You can access a range of items in a tuple using slicing, similar to lists:

```python
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Basic slicing [start:stop] (stop is exclusive)
print(fruits[1:4])  # ("banana", "cherry", "date")

# Omitting start (defaults to 0)
print(fruits[:3])  # ("apple", "banana", "cherry")

# Omitting stop (defaults to length of tuple)
print(fruits[2:])  # ("cherry", "date", "elderberry")

# Negative indices in slicing
print(fruits[-3:-1])  # ("cherry", "date")

# Step parameter [start:stop:step]
print(fruits[::2])  # ("apple", "cherry", "elderberry")

# Reversing a tuple
print(fruits[::-1])  # ("elderberry", "date", "cherry", "banana", "apple")
```

## Tuple Immutability

The key characteristic of tuples is that they are immutable, meaning their elements cannot be changed after creation:

```python
coordinates = (3, 4)

# This will raise a TypeError
try:
    coordinates[0] = 5
except TypeError as e:
    print(f"Error: {e}")  # Error: 'tuple' object does not support item assignment
```

However, if a tuple contains mutable objects like lists, the contents of those objects can be modified:

```python
data = ([1, 2], [3, 4])

# This is allowed because we're modifying the list, not the tuple
data[0].append(5)
print(data)  # ([1, 2, 5], [3, 4])

# But this will raise a TypeError
try:
    data[0] = [6, 7]
except TypeError as e:
    print(f"Error: {e}")  # Error: 'tuple' object does not support item assignment
```

## Common Tuple Operations

### Concatenation

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenating tuples
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)
```

### Repetition

```python
# Repeating a tuple
repeated = tuple1 * 3
print(repeated)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### Finding Elements

```python
fruits = ("apple", "banana", "cherry", "banana", "elderberry")

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

### Length, Min, and Max

```python
numbers = (3, 1, 4, 1, 5, 9, 2)

# Length: number of items
length = len(numbers)
print(length)  # 7

# Min and Max: smallest and largest values
minimum = min(numbers)
maximum = max(numbers)
print(minimum)  # 1
print(maximum)  # 9
```

## Tuple Unpacking

Tuple unpacking is a powerful feature that allows you to assign the elements of a tuple to multiple variables in a single statement:

```python
# Basic unpacking
coordinates = (3, 4)
x, y = coordinates
print(x)  # 3
print(y)  # 4

# Unpacking with more elements
person = ("John", 25, "Developer")
name, age, occupation = person
print(name)       # "John"
print(age)        # 25
print(occupation) # "Developer"
```

### Extended unpacking (Python 3.x)

```python
# Using * to collect multiple elements
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Using * with fewer variables
first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*beginning, last = numbers
print(beginning)  # [1, 2, 3, 4]
print(last)       # 5
```

## Named Tuples

Python's `collections` module provides a factory function called `namedtuple` that creates tuple subclasses with named fields:

```python
from collections import namedtuple

# Creating a named tuple class
Point = namedtuple('Point', ['x', 'y'])

# Creating instances
p1 = Point(3, 4)
p2 = Point(x=5, y=6)  # Can use keyword arguments

# Accessing by name or index
print(p1.x)    # 3
print(p1[0])   # 3
print(p2.y)    # 6
print(p2[1])   # 6

# Converting to dictionary
p1_dict = p1._asdict()
print(p1_dict)  # {'x': 3, 'y': 4}

# Creating a new instance with updated values
p3 = p1._replace(x=10)
print(p3)  # Point(x=10, y=4)
```

Named tuples provide a convenient way to define simple classes for storing data, with the benefits of tuples (immutability, lightweight) and the readability of accessing fields by name.

## When to Use Tuples

Tuples are ideal when you need:

1. **Immutable data**: When you want to ensure data cannot be modified
2. **Heterogeneous data**: When you have a fixed collection of different types of data
3. **Dictionary keys**: Tuples can be used as dictionary keys (unlike lists)
4. **Function returns**: When returning multiple values from a function
5. **Data integrity**: When you want to protect data from accidental modification

## Tuples vs. Lists

| Feature | Tuples | Lists |
|---------|--------|-------|
| Syntax | `()` | `[]` |
| Mutability | Immutable | Mutable |
| Performance | Generally faster | Slightly slower |
| Use as dictionary keys | Yes | No |
| Methods | Few (count, index) | Many (append, remove, sort, etc.) |
| Memory usage | Slightly less | Slightly more |
| Use case | Fixed data collections | Dynamic data collections |

## Performance Considerations

- Tuples are generally more memory-efficient than lists
- Operations on tuples can be faster than equivalent operations on lists
- Creating a tuple is slightly faster than creating a list
- Accessing elements in a tuple is slightly faster than in a list

## Common Patterns and Idioms

### Returning multiple values from a function

```python
def get_coordinates():
    # Calculate some values
    return (3, 4)  # Return as tuple

x, y = get_coordinates()  # Unpack the returned tuple
```

### Swapping variables

```python
a = 5
b = 10

# Swap values using tuple packing and unpacking
a, b = b, a

print(a)  # 10
print(b)  # 5
```

### Using tuples as dictionary keys

```python
# Coordinates as dictionary keys
distances = {
    (0, 0): 0,
    (1, 0): 1,
    (0, 1): 1,
    (1, 1): 1.414
}

print(distances[(1, 0)])  # 1
```

### Tuple as a data record

```python
# Representing a person as a tuple
person = ("John", "Doe", 30, "Developer")
first_name, last_name, age, occupation = person
```

## Summary

- Tuples are ordered, immutable collections that can store items of different types
- Tuples are created using parentheses `()` or the `tuple()` constructor
- Tuples support indexing, slicing, and many of the same operations as lists
- Tuple unpacking allows assigning tuple elements to multiple variables
- Named tuples provide a way to create simple classes with named fields
- Tuples are ideal for representing fixed collections of data where immutability is desired

In the next lesson, we'll explore dictionaries, which are unordered collections of key-value pairs that provide fast lookups by key.