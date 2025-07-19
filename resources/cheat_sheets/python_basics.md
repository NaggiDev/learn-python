# Python Basics Cheat Sheet

## Variables and Data Types

### Variable Assignment
```python
# Basic assignment
name = "Alice"
age = 25
height = 5.6
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0
```

### Data Types
```python
# Numbers
integer = 42
float_num = 3.14
complex_num = 2 + 3j

# Strings
single_quote = 'Hello'
double_quote = "World"
multiline = """This is a
multiline string"""

# Boolean
is_true = True
is_false = False

# None
empty_value = None
```

### Type Checking and Conversion
```python
# Check type
type(42)          # <class 'int'>
isinstance(42, int)  # True

# Type conversion
int("123")        # 123
float("3.14")     # 3.14
str(42)           # "42"
bool(1)           # True
```

## Operators

### Arithmetic Operators
```python
# Basic operations
10 + 3    # 13 (addition)
10 - 3    # 7  (subtraction)
10 * 3    # 30 (multiplication)
10 / 3    # 3.333... (division)
10 // 3   # 3  (floor division)
10 % 3    # 1  (modulus)
10 ** 3   # 1000 (exponentiation)
```

### Comparison Operators
```python
# Comparisons
10 == 10  # True (equal)
10 != 3   # True (not equal)
10 > 3    # True (greater than)
10 < 3    # False (less than)
10 >= 10  # True (greater than or equal)
10 <= 3   # False (less than or equal)
```

### Logical Operators
```python
# Logical operations
True and False   # False
True or False    # True
not True         # False

# With variables
x = 5
y = 10
x > 0 and y > 0  # True
x > 10 or y > 5  # True
not (x > 10)     # True
```

## String Operations

### String Methods
```python
text = "Hello World"

# Case methods
text.upper()        # "HELLO WORLD"
text.lower()        # "hello world"
text.title()        # "Hello World"
text.capitalize()   # "Hello world"

# Search and replace
text.find("World")     # 6
text.replace("World", "Python")  # "Hello Python"
text.startswith("Hello")  # True
text.endswith("World")    # True

# Split and join
text.split()           # ["Hello", "World"]
"-".join(["a", "b"])   # "a-b"

# Strip whitespace
"  hello  ".strip()    # "hello"
```

### String Formatting
```python
name = "Alice"
age = 25

# f-strings (Python 3.6+)
f"My name is {name} and I'm {age} years old"

# .format() method
"My name is {} and I'm {} years old".format(name, age)
"My name is {name} and I'm {age} years old".format(name=name, age=age)

# % formatting (older style)
"My name is %s and I'm %d years old" % (name, age)
```

## Control Flow

### If Statements
```python
x = 10

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Ternary operator
result = "Positive" if x > 0 else "Not positive"
```

### Loops

#### For Loops
```python
# Iterate over sequence
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Enumerate for index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

#### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1

# While with else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed normally")
```

### Loop Control
```python
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 7:
        break     # Exit loop
    print(i)
```

## Input/Output

### Input
```python
# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

### Output
```python
# Print statements
print("Hello, World!")
print("Name:", name, "Age:", age)
print(f"Hello, {name}!")

# Print with separators and endings
print("A", "B", "C", sep="-")      # A-B-C
print("Hello", end=" ")
print("World")                     # Hello World
```

## Common Built-in Functions

```python
# Math functions
abs(-5)        # 5
min(1, 2, 3)   # 1
max(1, 2, 3)   # 3
sum([1, 2, 3]) # 6
round(3.14159, 2)  # 3.14

# Sequence functions
len("hello")   # 5
sorted([3, 1, 2])  # [1, 2, 3]
reversed([1, 2, 3])  # [3, 2, 1]

# Type functions
int(3.14)      # 3
float(5)       # 5.0
str(123)       # "123"
list("abc")    # ['a', 'b', 'c']
```

## List Comprehensions

```python
# Basic list comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# With transformation
words = ["hello", "world"]
upper_words = [word.upper() for word in words]  # ["HELLO", "WORLD"]
```

## Common Patterns

### Swapping Variables
```python
a, b = b, a
```

### Checking Multiple Conditions
```python
# Check if value is in range
if 0 <= x <= 100:
    print("In range")

# Check membership
if x in [1, 2, 3, 4, 5]:
    print("Found")
```

### Default Values
```python
# Using or for default values
name = user_input or "Anonymous"

# Using get() for dictionaries
value = my_dict.get("key", "default_value")
```

## Quick Tips

- Use `help(function_name)` to get help on any function
- Use `dir(object)` to see available methods
- Python is case-sensitive: `Name` ≠ `name`
- Indentation matters - use 4 spaces per level
- Use meaningful variable names
- Comments start with `#`
- Use `_` for unused variables: `for _ in range(5):`