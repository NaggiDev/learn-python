# Dictionaries

## Introduction

Dictionaries are one of Python's most powerful and flexible data structures. A dictionary is an unordered collection of key-value pairs, where each key is unique. Dictionaries are optimized for retrieving data when you know the key, making them extremely efficient for lookups, insertions, and deletions.

In this lesson, you will learn how to create, access, and manipulate dictionaries, as well as common dictionary operations and use cases.

## Creating Dictionaries

There are several ways to create dictionaries in Python:

### Using curly braces

```python
# Empty dictionary
empty_dict = {}

# Dictionary with string keys
person = {
    "name": "John",
    "age": 30,
    "occupation": "Developer"
}

# Dictionary with mixed key types
mixed_keys = {
    "name": "Product",
    42: "Answer",
    (1, 2): "Coordinate"
}

# Nested dictionaries
nested = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
```

### Using the `dict()` constructor

```python
# Empty dictionary
empty_dict = dict()

# From a list of tuples
items = [("name", "John"), ("age", 30), ("occupation", "Developer")]
person = dict(items)

# Using keyword arguments (keys must be valid Python identifiers)
person = dict(name="John", age=30, occupation="Developer")
```

### Dictionary comprehensions

```python
# Creating a dictionary of squares
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtering with a condition
even_squares = {x: x**2 for x in range(6) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16}
```

## Accessing Dictionary Values

You can access dictionary values using their keys:

```python
person = {
    "name": "John",
    "age": 30,
    "occupation": "Developer"
}

# Accessing by key
print(person["name"])  # "John"
print(person["age"])   # 30

# Using get() method (safer, returns None or a default value if key doesn't exist)
print(person.get("occupation"))  # "Developer"
print(person.get("salary"))      # None
print(person.get("salary", 0))   # 0 (default value)
```

## Modifying Dictionaries

Dictionaries are mutable, so you can add, update, or remove key-value pairs:

### Adding or updating items

```python
person = {"name": "John", "age": 30}

# Adding a new key-value pair
person["occupation"] = "Developer"
print(person)  # {'name': 'John', 'age': 30, 'occupation': 'Developer'}

# Updating an existing value
person["age"] = 31
print(person)  # {'name': 'John', 'age': 31, 'occupation': 'Developer'}

# Using update() to add or update multiple items
person.update({"email": "john@example.com", "age": 32})
print(person)  # {'name': 'John', 'age': 32, 'occupation': 'Developer', 'email': 'john@example.com'}
```

### Removing items

```python
person = {
    "name": "John",
    "age": 30,
    "occupation": "Developer",
    "email": "john@example.com"
}

# pop(): removes item with specified key and returns its value
age = person.pop("age")
print(age)     # 30
print(person)  # {'name': 'John', 'occupation': 'Developer', 'email': 'john@example.com'}

# popitem(): removes and returns the last inserted key-value pair as a tuple
last_item = person.popitem()
print(last_item)  # ('email', 'john@example.com')
print(person)     # {'name': 'John', 'occupation': 'Developer'}

# del statement: removes item with specified key
del person["occupation"]
print(person)  # {'name': 'John'}

# clear(): removes all items
person.clear()
print(person)  # {}
```

## Dictionary Methods

Python dictionaries come with several useful methods:

### keys(), values(), and items()

```python
person = {
    "name": "John",
    "age": 30,
    "occupation": "Developer"
}

# keys(): returns a view object containing all keys
keys = person.keys()
print(keys)  # dict_keys(['name', 'age', 'occupation'])

# values(): returns a view object containing all values
values = person.values()
print(values)  # dict_values(['John', 30, 'Developer'])

# items(): returns a view object containing all key-value pairs as tuples
items = person.items()
print(items)  # dict_items([('name', 'John'), ('age', 30), ('occupation', 'Developer')])

# These views are dynamic - they reflect changes to the dictionary
person["email"] = "john@example.com"
print(keys)    # dict_keys(['name', 'age', 'occupation', 'email'])
print(values)  # dict_values(['John', 30, 'Developer', 'john@example.com'])
print(items)   # dict_items([('name', 'John'), ('age', 30), ('occupation', 'Developer'), ('email', 'john@example.com')])
```

### copy()

```python
# Creating a shallow copy of a dictionary
original = {"name": "John", "age": 30, "scores": [85, 90, 95]}
copy_dict = original.copy()

# Modifying the copy doesn't affect the original for simple values
copy_dict["name"] = "Jane"
print(original["name"])  # "John"
print(copy_dict["name"])  # "Jane"

# But for mutable values like lists, changes to the value affect both dictionaries
copy_dict["scores"].append(100)
print(original["scores"])  # [85, 90, 95, 100]
print(copy_dict["scores"])  # [85, 90, 95, 100]
```

### setdefault()

```python
person = {"name": "John", "age": 30}

# setdefault(): returns the value of a key if it exists,
# otherwise inserts the key with a specified default value and returns that value
occupation = person.setdefault("occupation", "Developer")
print(occupation)  # "Developer"
print(person)      # {'name': 'John', 'age': 30, 'occupation': 'Developer'}

# If the key already exists, the original value is returned and not changed
name = person.setdefault("name", "Jane")
print(name)        # "John" (not changed to "Jane")
print(person)      # {'name': 'John', 'age': 30, 'occupation': 'Developer'}
```

### fromkeys()

```python
# Creating a dictionary with the same value for multiple keys
keys = ["name", "age", "occupation"]
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # {'name': None, 'age': None, 'occupation': None}

# If no value is specified, None is used
another_dict = dict.fromkeys(keys)
print(another_dict)  # {'name': None, 'age': None, 'occupation': None}
```

## Iterating Through Dictionaries

There are several ways to iterate through a dictionary:

```python
person = {
    "name": "John",
    "age": 30,
    "occupation": "Developer"
}

# Iterating through keys (default)
for key in person:
    print(key, person[key])

# Iterating through keys explicitly
for key in person.keys():
    print(key, person[key])

# Iterating through values
for value in person.values():
    print(value)

# Iterating through key-value pairs
for key, value in person.items():
    print(key, value)
```

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries:

```python
# Basic dictionary comprehension
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With a condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Creating a dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_to_age = {name: age for name, age in zip(names, ages)}
print(name_to_age)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Swapping keys and values (assuming values are unique)
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

## Nested Dictionaries

Dictionaries can contain other dictionaries as values, creating nested structures:

```python
# Creating a nested dictionary
employees = {
    "john": {
        "id": 1,
        "age": 30,
        "department": "Engineering"
    },
    "alice": {
        "id": 2,
        "age": 28,
        "department": "Marketing"
    }
}

# Accessing nested values
print(employees["john"]["department"])  # "Engineering"

# Adding a new nested dictionary
employees["bob"] = {
    "id": 3,
    "age": 35,
    "department": "Finance"
}

# Modifying a value in a nested dictionary
employees["alice"]["age"] = 29

# Iterating through a nested dictionary
for name, details in employees.items():
    print(f"{name}: {details['department']}, {details['age']} years old")
```

## Dictionary Use Cases

Dictionaries are versatile and can be used in many scenarios:

### Counting occurrences

```python
# Count the occurrences of each character in a string
text = "hello world"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# More concise way using get()
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Even more concise using Counter from collections
from collections import Counter
char_count = Counter(text)
print(dict(char_count))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### Grouping data

```python
# Group people by their age
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 25}
]

age_groups = {}
for person in people:
    age = person["age"]
    if age in age_groups:
        age_groups[age].append(person["name"])
    else:
        age_groups[age] = [person["name"]]

print(age_groups)  # {30: ['Alice', 'Charlie'], 25: ['Bob', 'David']}

# Using setdefault
age_groups = {}
for person in people:
    age_groups.setdefault(person["age"], []).append(person["name"])

print(age_groups)  # {30: ['Alice', 'Charlie'], 25: ['Bob', 'David']}
```

### Caching/memoization

```python
# Using a dictionary to cache expensive function results
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

print(fibonacci(10))  # 55 (calculated efficiently using caching)
```

### Representing objects

```python
# Using dictionaries to represent objects
car = {
    "make": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "features": ["Bluetooth", "Backup Camera", "Lane Assist"]
}

# Accessing object properties
print(f"{car['year']} {car['make']} {car['model']}")  # "2020 Toyota Corolla"
```

## Dictionary Performance

Dictionaries in Python are implemented as hash tables, which provide very efficient operations:

- Accessing a value by key: O(1) average case
- Inserting a key-value pair: O(1) average case
- Deleting a key-value pair: O(1) average case
- Checking if a key exists: O(1) average case

This makes dictionaries ideal for lookups and data retrieval when you know the key.

## Dictionary Key Requirements

Not all Python objects can be used as dictionary keys. A key must be hashable, which means:

1. It has a hash value that doesn't change during its lifetime (immutable)
2. It can be compared to other objects
3. If two objects compare equal, they must have the same hash value

Common hashable types that can be used as dictionary keys:
- Strings
- Numbers (int, float, complex)
- Tuples (if they contain only hashable types)
- Frozen sets

Common unhashable types that cannot be used as dictionary keys:
- Lists
- Dictionaries
- Sets
- Any mutable object

```python
# Valid dictionary keys
valid_dict = {
    "string_key": "value1",
    42: "value2",
    3.14: "value3",
    (1, 2): "value4",
    frozenset([1, 2, 3]): "value5"
}

# Invalid dictionary keys (will raise TypeError)
try:
    invalid_dict = {[1, 2, 3]: "value"}
except TypeError as e:
    print(f"Error: {e}")  # Error: unhashable type: 'list'

try:
    invalid_dict = {{1: 2}: "value"}
except TypeError as e:
    print(f"Error: {e}")  # Error: unhashable type: 'dict'
```

## Common Pitfalls

### Modifying a dictionary while iterating

```python
# Incorrect way - RuntimeError
my_dict = {"a": 1, "b": 2, "c": 3}
try:
    for key in my_dict:
        if key == "a":
            my_dict["d"] = 4  # This modifies the dictionary during iteration
except RuntimeError as e:
    print(f"Error: {e}")

# Correct way - create a copy for iteration
my_dict = {"a": 1, "b": 2, "c": 3}
for key in list(my_dict.keys()):
    if key == "a":
        my_dict["d"] = 4
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Dictionary references vs. copies

```python
# Dictionaries are reference types
dict1 = {"name": "John", "age": 30}
dict2 = dict1  # dict2 references the same dictionary as dict1
dict2["age"] = 31
print(dict1)  # {'name': 'John', 'age': 31} - dict1 is also modified!

# Creating a copy
dict1 = {"name": "John", "age": 30}
dict2 = dict1.copy()  # or dict2 = dict(dict1)
dict2["age"] = 31
print(dict1)  # {'name': 'John', 'age': 30} - dict1 is unchanged
print(dict2)  # {'name': 'John', 'age': 31}
```

### Deep vs. shallow copy

```python
import copy

# Shallow copy doesn't create copies of nested objects
original = {"name": "John", "scores": [85, 90, 95]}
shallow = original.copy()
shallow["scores"].append(100)
print(original["scores"])  # [85, 90, 95, 100] - original is affected!

# Deep copy creates copies of all nested objects
original = {"name": "John", "scores": [85, 90, 95]}
deep = copy.deepcopy(original)
deep["scores"].append(100)
print(original["scores"])  # [85, 90, 95] - original is unchanged
print(deep["scores"])      # [85, 90, 95, 100]
```

## Dictionary vs. Other Data Structures

| Feature | Dictionary | List | Tuple | Set |
|---------|------------|------|-------|-----|
| Ordering | Ordered (Python 3.7+) | Ordered | Ordered | Unordered |
| Mutability | Mutable | Mutable | Immutable | Mutable |
| Indexing | By key | By position | By position | No indexing |
| Duplicates | No duplicate keys | Allows duplicates | Allows duplicates | No duplicates |
| Use case | Key-value mapping | Ordered collection | Fixed collection | Unique items |
| Lookup | O(1) average | O(n) | O(n) | O(1) average |

## Advanced Dictionary Features

### Dictionary unpacking

```python
# Unpacking dictionaries with **
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = {**dict1, **dict2}
print(combined)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Unpacking with overlapping keys (later dictionaries override earlier ones)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
combined = {**dict1, **dict2}
print(combined)  # {'a': 1, 'b': 3, 'c': 4}
```

### Dictionary merge and update operators (Python 3.9+)

```python
# Merge operator |
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = dict1 | dict2
print(combined)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Update operator |=
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1 |= dict2
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### defaultdict

```python
from collections import defaultdict

# defaultdict automatically creates a default value for missing keys
# This is useful to avoid checking if a key exists before using it
word_count = defaultdict(int)  # Default value is 0 for int
text = "the quick brown fox jumps over the lazy dog"
for word in text.split():
    word_count[word] += 1  # No need to check if word exists first

print(dict(word_count))  # {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

# defaultdict with list as default factory
groups = defaultdict(list)
people = [("Alice", "HR"), ("Bob", "IT"), ("Charlie", "HR"), ("David", "IT")]
for name, department in people:
    groups[department].append(name)  # No need to check if department exists first

print(dict(groups))  # {'HR': ['Alice', 'Charlie'], 'IT': ['Bob', 'David']}
```

### OrderedDict

```python
from collections import OrderedDict

# In Python 3.7+, regular dictionaries maintain insertion order,
# but OrderedDict still has some special features

# Creating an OrderedDict
ordered = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Moving an item to the end
ordered.move_to_end('a')
print(ordered)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Moving an item to the beginning
ordered.move_to_end('a', last=False)
print(ordered)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Popping the first item (FIFO)
first_item = ordered.popitem(last=False)
print(first_item)  # ('a', 1)
print(ordered)     # OrderedDict([('b', 2), ('c', 3)])
```

## Summary

- Dictionaries are key-value mappings that provide fast lookups by key
- Dictionary keys must be hashable (immutable)
- Dictionaries support various operations like adding, updating, and removing items
- Common methods include keys(), values(), items(), get(), and update()
- Dictionary comprehensions provide a concise way to create dictionaries
- Dictionaries can be nested to represent complex data structures
- Dictionaries are ideal for representing objects, counting occurrences, and caching results

In the next lesson, we'll explore sets, which are unordered collections of unique elements with powerful set operations.