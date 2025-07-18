# Control Flow in Python

Welcome to the fifth lesson in your Python journey! In this lesson, you'll learn about control flow in Python, which allows you to make decisions and repeat actions in your code. Control flow is a fundamental concept in programming that gives your programs the ability to respond to different conditions and automate repetitive tasks.

## Table of Contents
1. [Introduction to Control Flow](#introduction-to-control-flow)
2. [Conditional Statements](#conditional-statements)
   - [if Statements](#if-statements)
   - [if-else Statements](#if-else-statements)
   - [if-elif-else Statements](#if-elif-else-statements)
   - [Nested Conditionals](#nested-conditionals)
   - [Conditional Expressions (Ternary Operator)](#conditional-expressions-ternary-operator)
3. [Loops](#loops)
   - [for Loops](#for-loops)
   - [while Loops](#while-loops)
   - [Loop Control Statements](#loop-control-statements)
   - [Nested Loops](#nested-loops)
4. [Combining Conditionals and Loops](#combining-conditionals-and-loops)
5. [Best Practices](#best-practices)
6. [Common Pitfalls](#common-pitfalls)

## Introduction to Control Flow

Control flow refers to the order in which statements are executed in a program. By default, Python executes statements sequentially, from top to bottom. However, control flow structures allow you to:

- Execute code only when certain conditions are met (conditional statements)
- Repeat code multiple times (loops)
- Jump to different parts of your code (control statements)

These capabilities are essential for creating dynamic, responsive programs that can handle different situations and process varying amounts of data.

## Conditional Statements

Conditional statements allow your program to make decisions based on whether certain conditions are true or false.

### if Statements

The simplest form of conditional statement is the `if` statement, which executes a block of code only if a condition is true:

```python
# Basic if statement
age = 18

if age >= 18:
    print("You are an adult.")
    print("You can vote.")

print("This will always be printed.")
```

In this example:
1. The condition `age >= 18` is evaluated
2. Since it's true (18 is greater than or equal to 18), the indented code block is executed
3. The program continues with the non-indented code

If the condition were false, the indented code block would be skipped entirely.

### if-else Statements

The `if-else` statement provides an alternative block of code to execute when the condition is false:

```python
# if-else statement
age = 15

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
else:
    print("You are not yet an adult.")
    print("You cannot vote yet.")

print("This will always be printed.")
```

In this example:
1. The condition `age >= 18` is evaluated
2. Since it's false (15 is less than 18), the code block under `else` is executed
3. The program continues with the non-indented code

### if-elif-else Statements

When you need to check multiple conditions, you can use the `elif` (short for "else if") statement:

```python
# if-elif-else statement
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

In this example:
1. Each condition is checked in order
2. The first condition that evaluates to true has its code block executed
3. All other conditions are skipped
4. If none of the conditions are true, the `else` block is executed

Important notes about `if-elif-else`:
- Python checks conditions from top to bottom and stops at the first true condition
- Only one block of code will be executed, even if multiple conditions are true
- The `else` block is optional

### Nested Conditionals

You can place conditional statements inside other conditional statements, creating nested conditionals:

```python
# Nested conditionals
age = 25
has_license = True

if age >= 18:
    print("You are old enough to drive.")
    if has_license:
        print("You have a license. You can drive.")
    else:
        print("You don't have a license. You cannot drive yet.")
else:
    print("You are not old enough to drive.")
```

While nested conditionals are sometimes necessary, they can make code harder to read if overused. Consider refactoring complex nested conditionals into separate functions or using compound conditions.

### Conditional Expressions (Ternary Operator)

Python offers a concise way to write simple if-else statements using conditional expressions, sometimes called the ternary operator:

```python
# Regular if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Equivalent conditional expression
age = 20
status = "adult" if age >= 18 else "minor"
```

The syntax is: `value_if_true if condition else value_if_false`

Conditional expressions are useful for simple assignments based on conditions, but they should be used sparingly to maintain readability.

## Loops

Loops allow you to execute a block of code multiple times. Python provides two main types of loops: `for` loops and `while` loops.

### for Loops

The `for` loop is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code for each item in the sequence:

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)

# Iterating over a range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Using range with start and stop
for i in range(2, 6):  # 2, 3, 4, 5
    print(i)

# Using range with start, stop, and step
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)
```

The `range()` function is commonly used with `for` loops to execute code a specific number of times:
- `range(stop)`: Generates numbers from 0 to stop-1
- `range(start, stop)`: Generates numbers from start to stop-1
- `range(start, stop, step)`: Generates numbers from start to stop-1, incrementing by step

### while Loops

The `while` loop executes a block of code as long as a condition is true:

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count to avoid an infinite loop

# while loop with user input
response = ""
while response.lower() != "quit":
    response = input("Enter a command (type 'quit' to exit): ")
    print(f"You entered: {response}")
```

Important: Always ensure that the condition in a `while` loop will eventually become false, or you'll create an infinite loop that never terminates.

### Loop Control Statements

Python provides statements to alter the normal flow of loops:

1. **break**: Exits the loop completely

```python
# Using break to exit a loop early
for i in range(10):
    if i == 5:
        print("Breaking the loop")
        break
    print(i)
# Output: 0, 1, 2, 3, 4, Breaking the loop
```

2. **continue**: Skips the current iteration and moves to the next one

```python
# Using continue to skip certain iterations
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)
# Output: 1, 3, 5, 7, 9
```

3. **else clause**: Executes after the loop completes normally (not if the loop is exited with `break`)

```python
# Loop with else clause
for i in range(5):
    print(i)
else:
    print("Loop completed normally")

# Loop with break and else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't be printed because the loop was broken")
```

### Nested Loops

You can place loops inside other loops, creating nested loops:

```python
# Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

Output:
```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

Nested loops are useful for working with multi-dimensional data structures or generating combinations, but they can be computationally expensive if the sequences are large.

## Combining Conditionals and Loops

Conditionals and loops are often used together to create more complex control flow:

```python
# Finding prime numbers
for num in range(2, 20):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime")
```

This example uses a nested loop with conditionals and a `break` statement to find prime numbers.

Another common pattern is filtering items in a collection:

```python
# Filtering even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)  # [2, 4, 6, 8, 10]
```

## Best Practices

1. **Keep conditions simple and readable**:
   ```python
   # Hard to read
   if age >= 18 and (status == "student" or status == "employee") and not is_restricted:
       # ...
   
   # Better: Break it down
   is_adult = age >= 18
   is_eligible_status = status == "student" or status == "employee"
   if is_adult and is_eligible_status and not is_restricted:
       # ...
   ```

2. **Use meaningful variable names in loops**:
   ```python
   # Less clear
   for x in data:
       # ...
   
   # More clear
   for customer in customers:
       # ...
   ```

3. **Avoid deep nesting** of conditionals and loops when possible:
   ```python
   # Deeply nested (hard to follow)
   if condition1:
       if condition2:
           for item in items:
               if condition3:
                   # ...
   
   # Better: Use early returns or separate functions
   if not condition1:
       return
   if not condition2:
       return
   for item in items:
       process_item(item)  # Move complex logic to a function
   ```

4. **Use `enumerate()` when you need both index and value** in a for loop:
   ```python
   fruits = ["apple", "banana", "cherry"]
   
   # Without enumerate
   for i in range(len(fruits)):
       print(f"{i}: {fruits[i]}")
   
   # With enumerate (cleaner)
   for i, fruit in enumerate(fruits):
       print(f"{i}: {fruit}")
   ```

5. **Use list comprehensions** for simple transformations instead of for loops:
   ```python
   # Traditional for loop
   squares = []
   for x in range(10):
       squares.append(x ** 2)
   
   # List comprehension (more concise)
   squares = [x ** 2 for x in range(10)]
   ```

## Common Pitfalls

1. **Infinite loops** - Always ensure your while loops have a way to terminate:
   ```python
   # Infinite loop (bad)
   while True:
       print("This will run forever")
   
   # Proper loop with exit condition
   count = 0
   while count < 5:
       print(count)
       count += 1  # Don't forget to update the condition variable
   ```

2. **Off-by-one errors** in ranges and loops:
   ```python
   # Common mistake: Forgetting that range(n) goes up to n-1
   for i in range(5):
       print(i)  # Prints 0, 1, 2, 3, 4 (not 5)
   
   # If you want to include 5:
   for i in range(6):  # or range(0, 6)
       print(i)  # Prints 0, 1, 2, 3, 4, 5
   ```

3. **Indentation errors** - Python uses indentation to define code blocks:
   ```python
   # Incorrect indentation
   if x > 0:
       print("x is positive")
   print("This will always run")  # Not part of the if block
   
   # Correct indentation
   if x > 0:
       print("x is positive")
       print("This will only run if x is positive")  # Part of the if block
   ```

4. **Confusing `=` (assignment) with `==` (comparison)**:
   ```python
   # Common mistake
   if x = 5:  # This is a syntax error
       print("x is 5")
   
   # Correct usage
   if x == 5:  # This is a comparison
       print("x is 5")
   ```

5. **Forgetting that `and` and `or` short-circuit**:
   ```python
   # Short-circuit evaluation
   if x > 0 and some_function():  # some_function() won't be called if x <= 0
       # ...
   
   if x > 0 or some_function():  # some_function() won't be called if x > 0
       # ...
   ```

## Summary

In this lesson, you've learned:

- How to use conditional statements (`if`, `elif`, `else`) to make decisions in your code
- How to use loops (`for`, `while`) to repeat code execution
- How to control loop execution with `break`, `continue`, and `else`
- How to combine conditionals and loops for more complex control flow
- Best practices and common pitfalls when working with control flow

Control flow is a fundamental concept in programming that allows you to create dynamic, responsive programs. With conditionals and loops, you can write code that makes decisions and automates repetitive tasks, making your programs more powerful and flexible.

## Practice Exercises

To reinforce your understanding, try the following exercises:

1. Write a program that checks if a number is positive, negative, or zero
2. Create a program that finds all numbers divisible by 3 and 5 between 1 and 100
3. Write a program that prints the Fibonacci sequence up to a given number
4. Create a simple guessing game where the user tries to guess a random number

## Next Steps

In the next lesson, we'll explore functions and scope in Python, which will allow you to organize your code into reusable blocks and manage variable visibility.