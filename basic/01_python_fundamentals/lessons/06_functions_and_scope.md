# Functions and Scope in Python

Welcome to the sixth lesson in your Python journey! In this lesson, you'll learn about functions and scope in Python. Functions are reusable blocks of code that perform specific tasks, while scope determines where variables are accessible in your program. Understanding these concepts is crucial for writing organized, maintainable, and efficient Python code.

## Table of Contents
1. [Introduction to Functions](#introduction-to-functions)
2. [Defining and Calling Functions](#defining-and-calling-functions)
3. [Function Parameters and Arguments](#function-parameters-and-arguments)
   - [Positional Arguments](#positional-arguments)
   - [Keyword Arguments](#keyword-arguments)
   - [Default Parameter Values](#default-parameter-values)
   - [Variable-Length Arguments](#variable-length-arguments)
4. [Return Values](#return-values)
   - [Returning Multiple Values](#returning-multiple-values)
5. [Variable Scope](#variable-scope)
   - [Local Scope](#local-scope)
   - [Global Scope](#global-scope)
   - [Nonlocal Variables](#nonlocal-variables)
6. [Function Documentation](#function-documentation)
7. [Lambda Functions](#lambda-functions)
8. [Best Practices](#best-practices)
9. [Common Pitfalls](#common-pitfalls)

## Introduction to Functions

Functions are blocks of organized, reusable code designed to perform a specific task. They allow you to:

- Break down complex problems into smaller, manageable pieces
- Avoid repeating code by encapsulating operations that are performed multiple times
- Make your code more readable and maintainable
- Test individual components of your program separately

Think of functions as mini-programs within your program. They take inputs (though not always), perform operations, and can provide outputs.

## Defining and Calling Functions

In Python, you define a function using the `def` keyword, followed by the function name, parentheses, and a colon. The function body is indented below.

```python
# Defining a simple function
def greet():
    print("Hello, world!")

# Calling the function
greet()  # Output: Hello, world!
```

The function definition creates the function but doesn't execute its code. To execute (or "call") the function, you use the function name followed by parentheses.

## Function Parameters and Arguments

Functions can accept inputs called parameters, which are specified in the parentheses during function definition. When you call a function and provide values for these parameters, those values are called arguments.

### Positional Arguments

The simplest way to pass arguments to a function is by position:

```python
# Function with parameters
def greet_person(name, greeting):
    print(f"{greeting}, {name}!")

# Calling with positional arguments
greet_person("Alice", "Hello")  # Output: Hello, Alice!
greet_person("Bob", "Hi")       # Output: Hi, Bob!
```

### Keyword Arguments

You can also specify arguments by parameter name, which allows you to provide them in any order:

```python
# Using keyword arguments
greet_person(greeting="Good morning", name="Charlie")  # Output: Good morning, Charlie!
```

You can mix positional and keyword arguments, but positional arguments must come before keyword arguments:

```python
# Mixed positional and keyword arguments
greet_person("David", greeting="Welcome")  # Output: Welcome, David!

# This would cause an error:
# greet_person(name="Eve", "Welcome")  # SyntaxError
```

### Default Parameter Values

You can provide default values for parameters, which are used when the caller doesn't provide a value for that parameter:

```python
# Function with default parameter value
def greet_person(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_person("Frank")             # Output: Hello, Frank!
greet_person("Grace", "Welcome")  # Output: Welcome, Grace!
```

Parameters with default values must come after parameters without default values:

```python
# Correct:
def function(a, b=1, c=2):
    pass

# Incorrect - would cause a SyntaxError:
# def function(a=1, b, c=2):
#     pass
```

### Variable-Length Arguments

Sometimes you want a function to accept any number of arguments. Python provides two special syntaxes for this:

1. `*args` - Collects extra positional arguments as a tuple:

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2))          # Output: 3
print(sum_all(1, 2, 3, 4, 5)) # Output: 15
```

2. `**kwargs` - Collects extra keyword arguments as a dictionary:

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```

You can use both in the same function:

```python
def combined_example(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

combined_example(1, 2, 3, 4, 5, x=10, y=20)
# Output:
# a: 1, b: 2
# args: (3, 4, 5)
# kwargs: {'x': 10, 'y': 20}
```

## Return Values

Functions can send data back to the caller using the `return` statement:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

If a function doesn't have a `return` statement, or has a `return` statement without a value, it returns `None`:

```python
def no_return():
    print("This function doesn't return anything")

result = no_return()
print(result)  # Output: None
```

A `return` statement immediately exits the function, even if there's more code after it:

```python
def early_return(x):
    if x < 0:
        return "Negative"
    print("This will only print if x is not negative")
    return "Non-negative"

print(early_return(-5))  # Output: Negative
print(early_return(5))   # Output: Non-negative (and prints the message)
```

### Returning Multiple Values

Python functions can return multiple values as a tuple:

```python
def get_dimensions():
    return 100, 50  # Returns a tuple (100, 50)

width, height = get_dimensions()  # Unpacking the tuple
print(f"Width: {width}, Height: {height}")  # Output: Width: 100, Height: 50
```

## Variable Scope

Scope refers to the region of a program where a variable is accessible. Python has several levels of scope:

### Local Scope

Variables defined inside a function are in the local scope and can only be accessed within that function:

```python
def my_function():
    x = 10  # Local variable
    print(f"Inside function: x = {x}")

my_function()  # Output: Inside function: x = 10
# print(x)  # This would raise a NameError because x is not defined in this scope
```

### Global Scope

Variables defined at the top level of a script are in the global scope and can be accessed throughout the program:

```python
y = 20  # Global variable

def print_global():
    print(f"Inside function: y = {y}")  # Can access global variable

print_global()  # Output: Inside function: y = 20
print(f"Outside function: y = {y}")  # Output: Outside function: y = 20
```

If you want to modify a global variable from within a function, you need to use the `global` keyword:

```python
z = 30  # Global variable

def modify_global():
    global z
    z = 40  # Modifies the global variable

print(f"Before function call: z = {z}")  # Output: Before function call: z = 30
modify_global()
print(f"After function call: z = {z}")   # Output: After function call: z = 40
```

Without the `global` keyword, assigning to a variable inside a function creates a new local variable, even if there's a global variable with the same name:

```python
count = 0  # Global variable

def increment_without_global():
    count = 0  # Creates a new local variable, doesn't affect the global one
    count += 1
    print(f"Local count: {count}")

increment_without_global()  # Output: Local count: 1
print(f"Global count: {count}")  # Output: Global count: 0 (unchanged)
```

### Nonlocal Variables

For nested functions, Python has a third scope called nonlocal. The `nonlocal` keyword is similar to `global`, but it refers to variables in the nearest enclosing scope that isn't global:

```python
def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x = 20  # Modifies the variable in the outer function's scope
        print(f"Inner: x = {x}")
    
    print(f"Before inner call: x = {x}")  # Output: Before inner call: x = 10
    inner_function()  # Output: Inner: x = 20
    print(f"After inner call: x = {x}")   # Output: After inner call: x = 20

outer_function()
```

Without the `nonlocal` keyword, assigning to a variable in a nested function would create a new local variable:

```python
def outer_function():
    x = 10
    
    def inner_function():
        x = 20  # Creates a new local variable, doesn't affect the outer one
        print(f"Inner: x = {x}")
    
    print(f"Before inner call: x = {x}")  # Output: Before inner call: x = 10
    inner_function()  # Output: Inner: x = 20
    print(f"After inner call: x = {x}")   # Output: After inner call: x = 10 (unchanged)

outer_function()
```

## Function Documentation

It's good practice to document your functions using docstrings, which are string literals that appear as the first statement in a function:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    """
    return length * width
```

Docstrings can be accessed using the `help()` function or the `.__doc__` attribute:

```python
help(calculate_area)
# Output:
# Help on function calculate_area in module __main__:
#
# calculate_area(length, width)
#     Calculate the area of a rectangle.
#    
#     Args:
#         length (float): The length of the rectangle.
#         width (float): The width of the rectangle.
#    
#     Returns:
#         float: The area of the rectangle.

print(calculate_area.__doc__)
# Output: (same as above)
```

## Lambda Functions

Lambda functions are small, anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression:

```python
# Regular function
def add(a, b):
    return a + b

# Equivalent lambda function
add_lambda = lambda a, b: a + b

print(add(3, 5))       # Output: 8
print(add_lambda(3, 5))  # Output: 8
```

Lambda functions are often used with functions like `map()`, `filter()`, and `sorted()`:

```python
# Using lambda with map() to square each number
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Using lambda with filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using lambda with sorted() to sort by the second element of each tuple
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
```

## Best Practices

1. **Use descriptive function names** that indicate what the function does:
   ```python
   # Good
   def calculate_total_price(price, tax_rate):
       return price * (1 + tax_rate)
   
   # Less clear
   def calc(p, t):
       return p * (1 + t)
   ```

2. **Keep functions focused on a single task**:
   ```python
   # Better: Two functions with clear responsibilities
   def validate_user_input(input_string):
       # Validation logic here
       return is_valid
   
   def process_valid_input(input_string):
       # Processing logic here
       return result
   
   # Instead of one function that does both:
   def handle_input(input_string):
       # Validation and processing mixed together
       pass
   ```

3. **Use default parameter values** to make functions more flexible:
   ```python
   def connect_to_database(host="localhost", port=5432, user="admin"):
       # Connection logic here
       pass
   ```

4. **Return early** to avoid deep nesting:
   ```python
   # Better
   def process_item(item):
       if not item:
           return None
       
       if not is_valid(item):
           return None
       
       # Process the item
       return processed_item
   
   # Instead of
   def process_item_nested(item):
       if item:
           if is_valid(item):
               # Process the item
               return processed_item
       return None
   ```

5. **Document your functions** with docstrings:
   ```python
   def divide(a, b):
       """
       Divide two numbers and return the result.
       
       Args:
           a (float): The numerator
           b (float): The denominator
           
       Returns:
           float: The result of a/b
           
       Raises:
           ZeroDivisionError: If b is zero
       """
       return a / b
   ```

## Common Pitfalls

1. **Mutable default arguments** can cause unexpected behavior:
   ```python
   # Problematic: The list is created once when the function is defined
   def add_to_list(item, my_list=[]):
       my_list.append(item)
       return my_list
   
   print(add_to_list(1))  # Output: [1]
   print(add_to_list(2))  # Output: [1, 2] (not [2] as you might expect)
   
   # Better approach
   def add_to_list_fixed(item, my_list=None):
       if my_list is None:
           my_list = []
       my_list.append(item)
       return my_list
   ```

2. **Forgetting to return a value** when one is expected:
   ```python
   def multiply(a, b):
       result = a * b
       # Missing return statement
   
   product = multiply(3, 4)
   print(product)  # Output: None (not 12 as expected)
   ```

3. **Variable scope confusion**:
   ```python
   x = 10
   
   def update_x():
       x = 20  # Creates a new local variable, doesn't modify the global x
   
   update_x()
   print(x)  # Output: 10 (not 20 as might be expected)
   ```

4. **Overusing global variables**:
   ```python
   # Not recommended: Using global variables for function communication
   total = 0
   
   def add_to_total(value):
       global total
       total += value
   
   # Better: Pass and return values explicitly
   def add_value(current_total, value):
       return current_total + value
   ```

5. **Ignoring function return values**:
   ```python
   # The return value is ignored
   process_data(my_data)
   
   # Better: Capture and use the return value
   result = process_data(my_data)
   if result:
       # Do something with the result
       pass
   ```

## Summary

In this lesson, you've learned:

- How to define and call functions in Python
- How to work with function parameters and arguments
- How to return values from functions
- How variable scope works in Python
- How to document functions with docstrings
- How to use lambda functions for simple operations
- Best practices and common pitfalls when working with functions

Functions are a fundamental building block in Python programming. They allow you to organize your code into reusable, logical units, making your programs more modular, readable, and maintainable. Understanding variable scope is equally important, as it determines where variables can be accessed and modified in your program.

## Practice Exercises

To reinforce your understanding, try the following exercises:

1. Write a function that calculates the factorial of a number
2. Create a function that checks if a number is prime
3. Write a function that takes a variable number of arguments and returns their average
4. Create a function that uses a lambda function to filter a list
5. Write nested functions that demonstrate the use of nonlocal variables

## Next Steps

In the next module, we'll explore data structures in Python, starting with lists and list comprehensions. You'll learn how to store, manipulate, and process collections of data efficiently.