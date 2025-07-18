# Basic Operators in Python

Welcome to the third lesson in your Python journey! In this lesson, you'll learn about Python's operators, which are symbols that perform operations on variables and values. Understanding operators is essential for writing expressions and making decisions in your code.

## Table of Contents
1. [Introduction to Operators](#introduction-to-operators)
2. [Arithmetic Operators](#arithmetic-operators)
   - [Basic Arithmetic](#basic-arithmetic)
   - [Advanced Arithmetic](#advanced-arithmetic)
3. [Comparison Operators](#comparison-operators)
   - [Equality and Inequality](#equality-and-inequality)
   - [Relational Operators](#relational-operators)
4. [Logical Operators](#logical-operators)
   - [and, or, not](#and-or-not)
   - [Short-Circuit Evaluation](#short-circuit-evaluation)
5. [Assignment Operators](#assignment-operators)
   - [Simple Assignment](#simple-assignment)
   - [Compound Assignment](#compound-assignment)
6. [Bitwise Operators](#bitwise-operators)
7. [Identity and Membership Operators](#identity-and-membership-operators)
   - [Identity Operators: is, is not](#identity-operators-is-is-not)
   - [Membership Operators: in, not in](#membership-operators-in-not-in)
8. [Operator Precedence](#operator-precedence)
   - [Precedence Rules](#precedence-rules)
   - [Using Parentheses](#using-parentheses)
9. [Best Practices](#best-practices)

## Introduction to Operators

Operators in Python are special symbols that perform operations on variables and values. They are the building blocks of expressions, which are combinations of values, variables, and operators that evaluate to a single value.

Python has several types of operators:
- Arithmetic operators for mathematical calculations
- Comparison operators for comparing values
- Logical operators for combining boolean expressions
- Assignment operators for assigning values to variables
- Bitwise operators for bit-level operations
- Identity and membership operators for object comparisons

## Arithmetic Operators

### Basic Arithmetic

Python provides all the standard arithmetic operators:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1.6666...` |
| `//` | Floor Division | `5 // 3` | `1` |
| `%` | Modulus (Remainder) | `5 % 3` | `2` |
| `**` | Exponentiation | `5 ** 3` | `125` |

Examples:

```python
# Basic arithmetic operations
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333333333333335
print(a // b)   # 3 (floor division discards the fractional part)
print(a % b)    # 1 (remainder of the division)
print(a ** b)   # 1000 (10 raised to the power of 3)
```

### Advanced Arithmetic

Python's arithmetic operators work with different numeric types:

```python
# Integer operations
print(10 + 5)      # 15

# Float operations
print(10.5 + 5.2)  # 15.7

# Mixed operations (result is float)
print(10 + 5.5)    # 15.5

# String repetition with *
print("Python " * 3)  # "Python Python Python "

# List repetition with *
print([1, 2] * 3)     # [1, 2, 1, 2, 1, 2]
```

## Comparison Operators

Comparison operators are used to compare values. They return boolean values: `True` or `False`.

### Equality and Inequality

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |

### Relational Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

Examples:

```python
a = 10
b = 5
c = 10

# Equality operators
print(a == b)    # False
print(a == c)    # True
print(a != b)    # True

# Relational operators
print(a > b)     # True
print(a < b)     # False
print(a >= c)    # True
print(a <= c)    # True

# Comparing different types
print(10 == 10.0)  # True (value comparison)
print("10" == 10)  # False (different types)

# Chaining comparisons
print(1 < 2 < 3)   # True (equivalent to 1 < 2 and 2 < 3)
print(5 > 3 < 10)  # True (equivalent to 5 > 3 and 3 < 10)
```

## Logical Operators

Logical operators are used to combine conditional statements.

### and, or, not

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Returns True if both statements are true | `a and b` |
| `or` | Returns True if one of the statements is true | `a or b` |
| `not` | Reverses the result, returns False if the result is true | `not a` |

Examples:

```python
a = True
b = False

# Logical AND
print(a and b)  # False
print(a and True)  # True
print(False and b)  # False

# Logical OR
print(a or b)  # True
print(False or b)  # False
print(a or True)  # True

# Logical NOT
print(not a)  # False
print(not b)  # True

# Complex logical expressions
print((a or b) and not (a and b))  # True
```

### Short-Circuit Evaluation

Python uses short-circuit evaluation for logical operators:
- For `and`, if the first operand is False, the second operand is not evaluated
- For `or`, if the first operand is True, the second operand is not evaluated

This can be useful for efficiency and for conditional execution:

```python
# Short-circuit with and
x = 5
if x > 0 and 10 / x > 1:  # Safe because 10/x only happens if x > 0
    print("x is positive and 10/x is greater than 1")

# Short-circuit with or
def expensive_function():
    print("Expensive function called")
    return False

# This will call expensive_function
result = False or expensive_function()  # Prints "Expensive function called"

# This will not call expensive_function
result = True or expensive_function()   # expensive_function is not called
```

## Assignment Operators

### Simple Assignment

The basic assignment operator is `=`, which assigns the value on the right to the variable on the left:

```python
x = 10  # Assigns 10 to x
```

### Compound Assignment

Python provides compound assignment operators that combine an arithmetic operation with assignment:

| Operator | Example | Equivalent to |
|----------|---------|---------------|
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 5` | `x = x ** 5` |

Examples:

```python
x = 10

# Compound assignment
x += 5      # x is now 15
print(x)

x -= 3      # x is now 12
print(x)

x *= 2      # x is now 24
print(x)

x /= 4      # x is now 6.0 (note: becomes float)
print(x)

# Compound assignment with strings
s = "Hello"
s += " World"  # s is now "Hello World"
print(s)

# Compound assignment with lists
my_list = [1, 2]
my_list += [3, 4]  # my_list is now [1, 2, 3, 4]
print(my_list)
```

## Bitwise Operators

Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

| Operator | Description | Example |
|----------|-------------|---------|
| `&` | Bitwise AND | `a & b` |
| `\|` | Bitwise OR | `a \| b` |
| `^` | Bitwise XOR | `a ^ b` |
| `~` | Bitwise NOT | `~a` |
| `<<` | Left shift | `a << n` |
| `>>` | Right shift | `a >> n` |

Examples:

```python
a = 60  # 60 = 0011 1100 in binary
b = 13  # 13 = 0000 1101 in binary

print(a & b)   # 12 = 0000 1100 (Bitwise AND)
print(a | b)   # 61 = 0011 1101 (Bitwise OR)
print(a ^ b)   # 49 = 0011 0001 (Bitwise XOR)
print(~a)      # -61 (Bitwise NOT, inverts all bits)
print(a << 2)  # 240 = 1111 0000 (Left shift by 2 bits)
print(a >> 2)  # 15 = 0000 1111 (Right shift by 2 bits)
```

## Identity and Membership Operators

### Identity Operators: is, is not

Identity operators check if two variables refer to the same object in memory:

| Operator | Description | Example |
|----------|-------------|---------|
| `is` | Returns True if both variables are the same object | `a is b` |
| `is not` | Returns True if both variables are not the same object | `a is not b` |

Examples:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)    # True (a and c refer to the same object)
print(a is b)    # False (a and b are equal but different objects)
print(a == b)    # True (a and b have the same value)

# Common use with None
x = None
print(x is None)  # True (preferred way to check for None)
```

### Membership Operators: in, not in

Membership operators test if a sequence (like a string, list, or tuple) contains a specific value:

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Returns True if a sequence contains the specified value | `x in y` |
| `not in` | Returns True if a sequence does not contain the specified value | `x not in y` |

Examples:

```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)       # True
print("orange" in fruits)      # False
print("orange" not in fruits)  # True

text = "Hello, World!"
print("Hello" in text)         # True
print("Python" in text)        # False

# Checking keys in dictionaries
person = {"name": "John", "age": 30}
print("name" in person)        # True (checks keys)
print("John" in person)        # False (not a key)
print("John" in person.values())  # True (checks values)
```

## Operator Precedence

### Precedence Rules

Python follows specific rules for the order in which operators are evaluated. Here's a simplified precedence table (from highest to lowest):

1. Parentheses `()`
2. Exponentiation `**`
3. Unary plus and minus `+x`, `-x`
4. Multiplication, division, floor division, modulus `*`, `/`, `//`, `%`
5. Addition and subtraction `+`, `-`
6. Bitwise shifts `<<`, `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
9. Bitwise OR `|`
10. Comparison operators `==`, `!=`, `>`, `>=`, `<`, `<=`
11. Identity and membership operators `is`, `is not`, `in`, `not in`
12. Logical operators `not`, `and`, `or`

### Using Parentheses

When in doubt about operator precedence, use parentheses to make your intentions clear:

```python
# Without parentheses (follows precedence rules)
result = 2 + 3 * 4    # 14 (multiplication happens first)

# With parentheses (explicitly defines order)
result = (2 + 3) * 4  # 20 (addition happens first)

# Complex expression with parentheses
result = (2 + 3) * (4 + 5)  # 5 * 9 = 45

# Logical operators with parentheses
a = True
b = False
c = True
result = a and (b or c)  # True (equivalent to a and (b or c))
```

## Best Practices

1. **Use parentheses for clarity**: Even when not strictly necessary, parentheses can make your code more readable by explicitly showing the intended order of operations.

2. **Be careful with comparison chaining**: While `a < b < c` is a convenient shorthand, be aware that it's equivalent to `a < b and b < c`.

3. **Use identity operators appropriately**: Use `is` and `is not` for comparing with `None` or when you specifically want to check if two variables refer to the same object. Use `==` and `!=` for value comparisons.

4. **Leverage short-circuit evaluation**: Take advantage of short-circuit evaluation with `and` and `or` for conditional execution and to avoid unnecessary computations.

5. **Be cautious with bitwise operators**: Bitwise operators are powerful but can be confusing. Use comments to explain bit manipulations for better code readability.

6. **Use compound assignment operators**: They make your code more concise and often more readable.

## Summary

In this lesson, you've learned about:

- Arithmetic operators for mathematical calculations
- Comparison operators for comparing values
- Logical operators for combining boolean expressions
- Assignment operators for assigning values to variables
- Bitwise operators for bit-level operations
- Identity and membership operators for object comparisons
- Operator precedence rules and the importance of parentheses

Understanding operators is crucial for writing expressions and making decisions in your Python programs. They are the building blocks that allow you to manipulate data and control the flow of your code.

## Practice Exercises

To reinforce your understanding, try the following exercises:

1. Experiment with different arithmetic operations and observe the results
2. Practice using comparison operators with various data types
3. Create complex logical expressions and predict their outcomes
4. Use compound assignment operators to modify variables
5. Explore operator precedence with and without parentheses

## Next Steps

In the next lesson, we'll explore input/output operations in Python, including how to get input from users and display output in different formats.