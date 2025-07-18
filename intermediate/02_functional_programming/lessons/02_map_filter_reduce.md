# Map, Filter, and Reduce in Python

## Introduction

Map, filter, and reduce are three fundamental higher-order functions in functional programming. They allow you to process collections of data in a declarative way, making your code more readable and often more efficient. These functions take other functions as arguments and apply them to sequences of data.

## The map() Function

The `map()` function applies a given function to each item in an iterable (like a list) and returns a map object (which can be converted to a list).

### Syntax
```python
map(function, iterable)
```

### Basic Examples

```python
# Example 1: Square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Example 2: Convert strings to uppercase
words = ['hello', 'world', 'python']
uppercase = list(map(str.upper, words))
print(uppercase)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Example 3: Convert temperatures from Celsius to Fahrenheit
celsius = [0, 20, 30, 40, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)  # Output: [32.0, 68.0, 86.0, 104.0, 212.0]
```

### Using map() with Multiple Iterables

```python
# Add corresponding elements from two lists
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # Output: [11, 22, 33, 44]

# Calculate distance between points
x_coords = [1, 2, 3]
y_coords = [4, 5, 6]
distances = list(map(lambda x, y: (x**2 + y**2)**0.5, x_coords, y_coords))
print(distances)  # Output: [4.123..., 5.385..., 6.708...]
```

### Real-world Examples

```python
# Example 1: Processing user data
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]

# Extract names
names = list(map(lambda user: user['name'], users))
print(names)  # Output: ['Alice', 'Bob', 'Charlie']

# Create email addresses
emails = list(map(lambda user: f"{user['name'].lower()}@company.com", users))
print(emails)  # Output: ['alice@company.com', 'bob@company.com', 'charlie@company.com']

# Example 2: Data type conversion
string_numbers = ['1', '2', '3', '4', '5']
integers = list(map(int, string_numbers))
print(integers)  # Output: [1, 2, 3, 4, 5]
```

## The filter() Function

The `filter()` function creates an iterator from elements of an iterable for which a function returns True.

### Syntax
```python
filter(function, iterable)
```

### Basic Examples

```python
# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Example 2: Filter strings by length
words = ['cat', 'elephant', 'dog', 'hippopotamus', 'ant']
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  # Output: ['elephant', 'hippopotamus']

# Example 3: Filter positive numbers
numbers = [-5, -2, 0, 3, 8, -1, 7]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)  # Output: [3, 8, 7]
```

### Using filter() with None

When you pass `None` as the function, `filter()` removes all falsy values:

```python
mixed_data = [1, 0, 'hello', '', None, 'world', False, True, [1, 2], []]
truthy_values = list(filter(None, mixed_data))
print(truthy_values)  # Output: [1, 'hello', 'world', True, [1, 2]]
```

### Real-world Examples

```python
# Example 1: Filter products by criteria
products = [
    {'name': 'Laptop', 'price': 999, 'in_stock': True},
    {'name': 'Mouse', 'price': 25, 'in_stock': False},
    {'name': 'Keyboard', 'price': 75, 'in_stock': True},
    {'name': 'Monitor', 'price': 300, 'in_stock': True}
]

# Filter available products under $500
affordable_available = list(filter(
    lambda p: p['price'] < 500 and p['in_stock'], 
    products
))
print(affordable_available)

# Example 2: Filter valid email addresses
emails = ['user@example.com', 'invalid-email', 'test@domain.org', 'no-at-sign']
valid_emails = list(filter(
    lambda email: '@' in email and '.' in email.split('@')[1], 
    emails
))
print(valid_emails)  # Output: ['user@example.com', 'test@domain.org']
```

## The reduce() Function

The `reduce()` function applies a function cumulatively to the items in an iterable, reducing the iterable to a single value. It's part of the `functools` module.

### Syntax
```python
from functools import reduce
reduce(function, iterable[, initializer])
```

### Basic Examples

```python
from functools import reduce

# Example 1: Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Example 2: Find the maximum value
numbers = [3, 7, 2, 9, 1, 5]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # Output: 9

# Example 3: Calculate factorial
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)  # Output: 120

# Example 4: Concatenate strings
words = ['Hello', ' ', 'World', '!']
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # Output: Hello World!
```

### Using reduce() with Initial Value

```python
# Sum with initial value
numbers = [1, 2, 3, 4, 5]
total_with_initial = reduce(lambda x, y: x + y, numbers, 100)
print(total_with_initial)  # Output: 115 (100 + 15)

# Product with initial value
numbers = [2, 3, 4]
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # Output: 24
```

### Real-world Examples

```python
# Example 1: Flatten a list of lists
lists = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, lists)
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

# Example 2: Find the longest string
words = ['cat', 'elephant', 'dog', 'hippopotamus']
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest)  # Output: hippopotamus

# Example 3: Combine dictionaries
dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
combined = reduce(lambda x, y: {**x, **y}, dicts)
print(combined)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

## Combining map(), filter(), and reduce()

These functions can be chained together for powerful data processing:

```python
# Example 1: Process a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square even numbers and sum them
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)
print(result)  # Output: 220 (4 + 16 + 36 + 64 + 100)

# Example 2: Process sales data
sales_data = [
    {'product': 'Laptop', 'quantity': 2, 'price': 999},
    {'product': 'Mouse', 'quantity': 5, 'price': 25},
    {'product': 'Keyboard', 'quantity': 3, 'price': 75},
    {'product': 'Monitor', 'quantity': 1, 'price': 300}
]

# Calculate total revenue for products with quantity > 1
total_revenue = reduce(
    lambda x, y: x + y,
    map(
        lambda item: item['quantity'] * item['price'],
        filter(lambda item: item['quantity'] > 1, sales_data)
    )
)
print(total_revenue)  # Output: 2223 (1998 + 225)
```

## Performance Considerations

### Memory Efficiency
Map and filter return iterators, not lists. This is memory-efficient for large datasets:

```python
# Memory efficient - creates iterator
large_numbers = range(1000000)
squared_evens = map(lambda x: x**2, filter(lambda x: x % 2 == 0, large_numbers))

# Only convert to list when needed
first_10 = list(squared_evens)[:10]  # This won't work as expected!

# Better approach for partial consumption
squared_evens = map(lambda x: x**2, filter(lambda x: x % 2 == 0, large_numbers))
first_10 = []
for i, value in enumerate(squared_evens):
    if i >= 10:
        break
    first_10.append(value)
```

### List Comprehensions vs map/filter

List comprehensions are often more readable and sometimes faster:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map and filter
result1 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# Using list comprehension (often preferred)
result2 = [x**2 for x in numbers if x % 2 == 0]

print(result1 == result2)  # Output: True
```

## Best Practices

### 1. Choose the Right Tool
- Use `map()` when you need to transform every element
- Use `filter()` when you need to select elements based on criteria
- Use `reduce()` when you need to combine elements into a single value
- Consider list comprehensions for simple transformations

### 2. Function Clarity
```python
# Good: Clear function purpose
def is_adult(person):
    return person['age'] >= 18

adults = list(filter(is_adult, people))

# Also good: Simple lambda
adults = list(filter(lambda p: p['age'] >= 18, people))

# Avoid: Complex lambda
# complex_filter = lambda p: p['age'] >= 18 and p['income'] > 50000 and len(p['name']) > 5
```

### 3. Error Handling
```python
# Handle potential errors in transformations
def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return float('inf')

numerators = [10, 20, 30]
denominators = [2, 0, 5]
results = list(map(safe_divide, numerators, denominators))
print(results)  # Output: [5.0, inf, 6.0]
```

## Common Patterns and Idioms

### 1. Data Cleaning
```python
# Clean and process text data
raw_data = ['  Hello  ', 'WORLD', '  python  ', 'Programming']
cleaned = list(map(str.strip, map(str.lower, raw_data)))
print(cleaned)  # Output: ['hello', 'world', 'python', 'programming']
```

### 2. Type Conversion
```python
# Convert and validate data
string_numbers = ['1', '2', 'invalid', '4', '5']

# Filter valid numbers and convert
valid_numbers = list(map(int, filter(str.isdigit, string_numbers)))
print(valid_numbers)  # Output: [1, 2, 4, 5]
```

### 3. Aggregation
```python
# Calculate statistics
grades = [85, 92, 78, 96, 88, 73, 91]

# Calculate average using reduce
average = reduce(lambda x, y: x + y, grades) / len(grades)
print(f"Average: {average}")

# Find grade distribution
grade_counts = reduce(
    lambda acc, grade: {**acc, grade//10*10: acc.get(grade//10*10, 0) + 1},
    grades,
    {}
)
print(grade_counts)  # Output: {80: 2, 90: 3, 70: 2}
```

## Summary

Map, filter, and reduce are powerful tools for functional programming in Python:

- **map()**: Transforms each element in a collection
- **filter()**: Selects elements based on a condition
- **reduce()**: Combines elements into a single value

Key benefits:
- More declarative and readable code
- Memory efficient (return iterators)
- Composable and chainable
- Encourage functional programming patterns

Remember to consider list comprehensions as an alternative for simple cases, and always prioritize code readability and maintainability.