# Python Data Structures Cheat Sheet

## Lists

### Creating Lists
```python
# Empty list
empty_list = []
empty_list = list()

# With initial values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
```

### List Operations
```python
fruits = ["apple", "banana", "cherry"]

# Accessing elements
fruits[0]        # "apple" (first element)
fruits[-1]       # "cherry" (last element)
fruits[1:3]      # ["banana", "cherry"] (slicing)

# Adding elements
fruits.append("date")           # Add to end
fruits.insert(1, "blueberry")   # Insert at index
fruits.extend(["elderberry"])   # Add multiple

# Removing elements
fruits.remove("banana")    # Remove by value
popped = fruits.pop()      # Remove and return last
popped = fruits.pop(0)     # Remove and return at index
del fruits[0]              # Delete by index

# Other operations
len(fruits)               # Length
fruits.count("apple")     # Count occurrences
fruits.index("cherry")    # Find index
fruits.reverse()          # Reverse in place
fruits.sort()             # Sort in place
sorted(fruits)            # Return sorted copy
```

### List Comprehensions
```python
# Basic comprehension
squares = [x**2 for x in range(5)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]

# With function
words = ["hello", "world"]
lengths = [len(word) for word in words]
```

## Dictionaries

### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# With initial values
person = {"name": "Alice", "age": 30, "city": "New York"}
person = dict(name="Alice", age=30, city="New York")

# From lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
```

### Dictionary Operations
```python
person = {"name": "Alice", "age": 30}

# Accessing values
person["name"]           # "Alice"
person.get("name")       # "Alice"
person.get("height", 0)  # 0 (default if key doesn't exist)

# Adding/updating
person["age"] = 31       # Update existing
person["city"] = "NYC"   # Add new key

# Removing
del person["city"]       # Delete key-value pair
age = person.pop("age")  # Remove and return value
person.clear()           # Remove all items

# Dictionary methods
person.keys()            # Get all keys
person.values()          # Get all values
person.items()           # Get key-value pairs
person.update({"height": 170})  # Update with another dict
```

### Dictionary Comprehensions
```python
# Basic comprehension
squares = {x: x**2 for x in range(5)}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# From lists
words = ["hello", "world"]
word_lengths = {word: len(word) for word in words}
```

## Sets

### Creating Sets
```python
# Empty set
empty_set = set()  # Note: {} creates empty dict, not set

# With initial values
numbers = {1, 2, 3, 4, 5}
letters = set("hello")  # {'h', 'e', 'l', 'o'}
from_list = set([1, 2, 2, 3])  # {1, 2, 3} (duplicates removed)
```

### Set Operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Adding/removing elements
set1.add(5)           # Add single element
set1.update([6, 7])   # Add multiple elements
set1.remove(1)        # Remove (raises error if not found)
set1.discard(1)       # Remove (no error if not found)
popped = set1.pop()   # Remove and return arbitrary element

# Set operations
set1 | set2           # Union: {1, 2, 3, 4, 5, 6}
set1 & set2           # Intersection: {3, 4}
set1 - set2           # Difference: {1, 2}
set1 ^ set2           # Symmetric difference: {1, 2, 5, 6}

# Set methods
set1.union(set2)
set1.intersection(set2)
set1.difference(set2)
set1.symmetric_difference(set2)

# Testing membership and relationships
3 in set1             # True if 3 is in set1
set1.issubset(set2)   # True if set1 is subset of set2
set1.issuperset(set2) # True if set1 is superset of set2
```

## Tuples

### Creating Tuples
```python
# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# With values
coordinates = (3, 4)
person = ("Alice", 30, "Engineer")
single_item = (42,)  # Note the comma for single-item tuple

# From other sequences
from_list = tuple([1, 2, 3])
```

### Tuple Operations
```python
point = (3, 4, 5)

# Accessing elements
point[0]        # 3
point[-1]       # 5
point[1:3]      # (4, 5)

# Tuple methods
point.count(3)  # Count occurrences
point.index(4)  # Find index

# Unpacking
x, y, z = point
x, *rest = point  # x=3, rest=[4, 5]

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
p.x  # 3
p.y  # 4
```

## Strings (as sequences)

### String Operations
```python
text = "Hello World"

# Accessing characters
text[0]         # 'H'
text[-1]        # 'd'
text[1:5]       # 'ello'

# String methods
text.split()              # ['Hello', 'World']
text.split('l')           # ['He', '', 'o Wor', 'd']
' '.join(['Hello', 'World'])  # 'Hello World'

# Character testing
'hello'.isalpha()         # True
'123'.isdigit()           # True
'hello123'.isalnum()      # True
'   '.isspace()           # True
```

## Common Patterns

### Iterating Over Data Structures

```python
# Lists
for item in my_list:
    print(item)

for index, item in enumerate(my_list):
    print(f"{index}: {item}")

# Dictionaries
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

# Sets
for item in my_set:
    print(item)

# Tuples
for item in my_tuple:
    print(item)
```

### Checking for Empty Collections
```python
if my_list:          # True if list is not empty
if not my_list:      # True if list is empty
if len(my_list) == 0:  # Explicit length check
```

### Converting Between Types
```python
# List to set (remove duplicates)
unique_items = list(set(my_list))

# String to list
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# List to string
text = ''.join(['h', 'e', 'l', 'l', 'o'])  # 'hello'

# Dictionary keys/values to list
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
```

### Nested Data Structures
```python
# List of dictionaries
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92}
]

# Dictionary of lists
grades = {
    "math": [85, 90, 78],
    "science": [92, 88, 95]
}

# Accessing nested data
students[0]["name"]     # "Alice"
grades["math"][0]       # 85
```

## Performance Tips

- **Lists**: Good for ordered data, frequent appends, random access
- **Dictionaries**: Best for key-value mapping, fast lookups
- **Sets**: Best for membership testing, removing duplicates
- **Tuples**: Good for immutable sequences, dictionary keys

## Memory and Speed Comparison

| Operation | List | Dict | Set | Tuple |
|-----------|------|------|-----|-------|
| Access by index | O(1) | N/A | N/A | O(1) |
| Access by key | N/A | O(1) | N/A | N/A |
| Search | O(n) | O(1) | O(1) | O(n) |
| Insert | O(1)* | O(1) | O(1) | N/A |
| Delete | O(n) | O(1) | O(1) | N/A |

*O(1) for append, O(n) for insert at arbitrary position