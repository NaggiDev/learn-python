# Variables and Data Types in Python

Welcome to the second lesson in your Python journey! In this lesson, you'll learn about variables and the fundamental data types in Python. Understanding these concepts is essential for writing any Python program.

## Table of Contents
1. [Introduction to Variables](#introduction-to-variables)
   - [What is a Variable?](#what-is-a-variable)
   - [Variable Naming Rules](#variable-naming-rules)
   - [Variable Assignment](#variable-assignment)
2. [Python's Basic Data Types](#pythons-basic-data-types)
   - [Numbers](#numbers)
   - [Strings](#strings)
   - [Booleans](#booleans)
   - [None Type](#none-type)
3. [Type Checking and Conversion](#type-checking-and-conversion)
   - [Checking Data Types](#checking-data-types)
   - [Converting Between Types](#converting-between-types)
4. [Variables in Memory](#variables-in-memory)
   - [How Python Stores Variables](#how-python-stores-variables)
   - [Variable References](#variable-references)
5. [Best Practices](#best-practices)
   - [Naming Conventions](#naming-conventions)
   - [Using Meaningful Names](#using-meaningful-names)
   - [Constants](#constants)

## Introduction to Variables

### What is a Variable?

In Python, a variable is a named location in memory that stores a value. Think of variables as labeled containers that hold data which can be changed throughout your program.

Variables allow you to:
- Store and retrieve data
- Manipulate values
- Keep track of information
- Make your code more readable and maintainable

### Variable Naming Rules

When naming variables in Python, you must follow these rules:

1. Variable names can contain letters, numbers, and underscores (_)
2. Variable names must start with a letter or underscore, not a number
3. Variable names are case-sensitive (`age`, `Age`, and `AGE` are three different variables)
4. Variable names cannot be Python keywords (like `if`, `for`, `while`, etc.)

Valid variable names:
```python
age = 25
user_name = "John"
_private = "Hidden"
camelCase = "Also valid but not preferred in Python"
```

Invalid variable names:
```python
2fast = "Invalid: starts with a number"  # Syntax error
user-name = "Invalid: contains hyphen"   # Syntax error
if = "Invalid: Python keyword"           # Syntax error
```

### Variable Assignment

In Python, you assign values to variables using the equal sign (`=`):

```python
# Simple assignment
name = "Alice"
age = 30
is_student = True

# Multiple assignment
x, y, z = 10, 20, 30

# Assigning the same value to multiple variables
a = b = c = 0
```

Variables in Python are dynamically typed, which means you don't need to declare the type of a variable when you create it, and you can change the type later:

```python
# Dynamic typing in action
x = 10       # x is an integer
print(x)     # Output: 10

x = "hello"  # Now x is a string
print(x)     # Output: hello
```

## Python's Basic Data Types

Python has several built-in data types. Let's explore the most fundamental ones:

### Numbers

Python has three main numeric types:

1. **Integers (`int`)**: Whole numbers without a decimal point
   ```python
   age = 25
   negative_num = -10
   zero = 0
   big_num = 1_000_000  # Underscores for readability (Python 3.6+)
   ```

2. **Floating-point numbers (`float`)**: Numbers with a decimal point
   ```python
   height = 1.75
   pi = 3.14159
   scientific = 1.5e3  # Scientific notation: 1.5 × 10³ = 1500.0
   ```

3. **Complex numbers (`complex`)**: Numbers with a real and imaginary part
   ```python
   c = 3 + 4j  # j represents the imaginary part
   ```

Basic operations with numbers:
```python
# Arithmetic operations
addition = 5 + 3        # 8
subtraction = 10 - 4    # 6
multiplication = 6 * 7  # 42
division = 20 / 4       # 5.0 (always returns a float)
floor_division = 20 // 4  # 5 (discards the decimal part)
modulus = 10 % 3        # 1 (remainder of division)
exponentiation = 2 ** 3  # 8 (2 raised to the power of 3)

# Order of operations follows mathematical conventions (PEMDAS)
result = 10 + 3 * 2     # 16, not 26
result = (10 + 3) * 2   # 26, parentheses change the order
```

### Strings

Strings (`str`) are sequences of characters enclosed in quotes. Python allows single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`) for strings.

```python
# String creation
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string
in Python"""
```

String operations and methods:
```python
# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # "John Doe"

# String repetition
separator = "-" * 10  # "----------"

# String indexing (zero-based)
message = "Hello"
first_char = message[0]   # "H"
last_char = message[-1]   # "o"

# String slicing
message = "Hello, World!"
substring = message[0:5]  # "Hello"
from_index = message[7:]  # "World!"
to_index = message[:5]    # "Hello"

# Common string methods
text = "  Python Programming  "
print(text.upper())         # "  PYTHON PROGRAMMING  "
print(text.lower())         # "  python programming  "
print(text.strip())         # "Python Programming"
print(text.replace("P", "J"))  # "  Jython Jrogramming  "
print(len(text))            # 23 (length of the string)
print("Python" in text)     # True (substring check)
```

String formatting:
```python
# Old-style formatting
name = "Alice"
age = 30
message = "My name is %s and I am %d years old." % (name, age)

# str.format() method
message = "My name is {} and I am {} years old.".format(name, age)
message = "My name is {0} and I am {1} years old.".format(name, age)
message = "My name is {n} and I am {a} years old.".format(n=name, a=age)

# f-strings (Python 3.6+) - recommended
message = f"My name is {name} and I am {age} years old."
```

### Booleans

Boolean (`bool`) values represent truth values: `True` or `False`. They are often used in conditional statements and logical operations.

```python
# Boolean values
is_active = True
is_complete = False

# Comparison operators produce boolean results
x = 5
y = 10
print(x < y)   # True
print(x == y)  # False
print(x >= 3)  # True

# Logical operators
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Truthy and falsy values
# Empty values and zero are considered False, most other values are True
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(None))   # False
print(bool(42))     # True
print(bool("Hello"))  # True
```

### None Type

`None` is a special constant in Python that represents the absence of a value or a null value. It is often used to signify that a variable has no value assigned to it.

```python
# Using None
result = None
print(result)  # None
print(result is None)  # True

# Common use case: default function parameter
def greet(name=None):
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"

print(greet())         # "Hello, stranger!"
print(greet("Alice"))  # "Hello, Alice!"
```

## Type Checking and Conversion

### Checking Data Types

You can check the type of a variable using the `type()` function:

```python
x = 10
y = "Hello"
z = True

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'bool'>
```

You can also check if a variable is of a specific type using the `isinstance()` function:

```python
x = 10
print(isinstance(x, int))    # True
print(isinstance(x, float))  # False
print(isinstance(x, (int, float)))  # True (checks if x is either int or float)
```

### Converting Between Types

Python provides built-in functions to convert between different data types:

```python
# String to number
num_str = "42"
num_int = int(num_str)    # 42
num_float = float(num_str)  # 42.0

# Number to string
x = 42
x_str = str(x)  # "42"

# Float to integer (truncates decimal part)
pi = 3.14159
pi_int = int(pi)  # 3

# String to boolean
print(bool(""))    # False (empty string)
print(bool("0"))   # True (non-empty string)

# Integer to boolean
print(bool(0))     # False
print(bool(42))    # True

# Common type conversion errors
try:
    int("hello")  # ValueError: invalid literal for int() with base 10
except ValueError as e:
    print(f"Error: {e}")
```

Type conversion is particularly important when working with user input, as the `input()` function always returns a string:

```python
# Getting numeric input from user
age_str = input("Enter your age: ")  # Returns a string
age = int(age_str)  # Convert to integer

# Better approach with error handling
try:
    age_str = input("Enter your age: ")
    age = int(age_str)
    print(f"In 5 years, you'll be {age + 5} years old.")
except ValueError:
    print("Please enter a valid number for age.")
```

## Variables in Memory

### How Python Stores Variables

In Python, variables don't store values directly. Instead, they store references to objects in memory. When you create a variable, Python:

1. Creates an object to represent the value
2. Stores the object in memory
3. Associates the variable name with the memory location

This is important to understand when working with mutable objects (like lists) versus immutable objects (like numbers and strings).

### Variable References

Multiple variables can reference the same object:

```python
a = [1, 2, 3]  # Create a list
b = a          # b references the same list as a

# Modifying the list through either variable affects both
b.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

# For immutable objects, this behavior is different
x = 10
y = x
y = 20  # Creates a new object, doesn't affect x
print(x)  # 10
print(y)  # 20
```

You can check if two variables reference the same object using the `is` operator:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]  # Same value but different object

print(a is b)  # True (same object)
print(a is c)  # False (different objects)
print(a == c)  # True (same value)
```

## Best Practices

### Naming Conventions

Python has established naming conventions that help make code more readable:

- Use `snake_case` for variable names (words separated by underscores)
- Use descriptive names that indicate the purpose of the variable
- Avoid single-letter names except for counters or temporary variables
- Use `UPPERCASE` for constants

```python
# Good variable names
user_name = "John"
item_count = 42
is_active = True
MAX_ATTEMPTS = 3  # Constant

# Less ideal variable names
u = "John"  # Too short, not descriptive
UserName = "John"  # CamelCase is typically used for classes in Python
x1 = 42  # Not descriptive
```

### Using Meaningful Names

Choose variable names that clearly describe what the variable represents:

```python
# Less clear
x = 86400
for i in range(x):
    # do something

# More clear
seconds_in_day = 86400
for second in range(seconds_in_day):
    # do something
```

### Constants

Python doesn't have built-in constant types, but by convention, constants are named with all uppercase letters:

```python
PI = 3.14159
MAX_USERS = 100
DATABASE_URL = "postgresql://localhost/mydb"

# These should not be changed throughout the program
```

## Summary

In this lesson, you've learned about:

- Variables and how to create them in Python
- Python's basic data types: numbers, strings, booleans, and None
- How to check and convert between different data types
- How Python stores variables in memory
- Best practices for naming and using variables

Understanding variables and data types is fundamental to Python programming. These concepts will be used in every Python program you write, so make sure you're comfortable with them before moving on.

## Practice Exercises

To reinforce your understanding, try the following exercises:

1. Create variables of different types and print their values and types
2. Practice string operations and formatting
3. Experiment with type conversions
4. Try to predict the output of code involving variable references

## Next Steps

In the next lesson, we'll explore Python's basic operators in more detail, including arithmetic, comparison, and logical operators. We'll also learn about operator precedence and how to use operators effectively in your programs.