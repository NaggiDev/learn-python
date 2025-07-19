# Debugging Techniques

## Introduction

Debugging is the process of finding and fixing errors (bugs) in your code. It's an essential skill for any programmer, as bugs are an inevitable part of software development. Effective debugging can save you hours of frustration and help you become a more efficient developer.

## Types of Bugs

Understanding different types of bugs helps you choose the right debugging approach:

### 1. Syntax Errors
These prevent your code from running at all:
```python
# Missing colon
if x > 5
    print("Greater than 5")

# Mismatched parentheses
print("Hello world"
```

### 2. Runtime Errors (Exceptions)
These occur while your program is running:
```python
# Division by zero
result = 10 / 0

# Index out of range
my_list = [1, 2, 3]
print(my_list[5])

# Key error
my_dict = {"a": 1}
print(my_dict["b"])
```

### 3. Logic Errors
These are the trickiest - your code runs but produces incorrect results:
```python
# Incorrect condition
def is_adult(age):
    return age >= 17  # Should be 18

# Off-by-one error
def sum_range(n):
    total = 0
    for i in range(n):  # Should be range(1, n+1)
        total += i
    return total
```

## Debugging Strategies

### 1. Read the Error Message
Python provides detailed error messages - learn to read them:

```python
Traceback (most recent call last):
  File "example.py", line 10, in <module>
    result = divide_numbers(10, 0)
  File "example.py", line 5, in divide_numbers
    return a / b
ZeroDivisionError: division by zero
```

Key information:
- **File and line number**: Where the error occurred
- **Function name**: Which function was executing
- **Error type**: What kind of error it is
- **Error message**: Description of the problem

### 2. The Scientific Method
Approach debugging systematically:

1. **Observe**: What is the actual behavior?
2. **Hypothesize**: What might be causing the issue?
3. **Test**: Create a minimal test case
4. **Analyze**: Examine the results
5. **Repeat**: If hypothesis is wrong, form a new one

### 3. Rubber Duck Debugging
Explain your code line by line to a rubber duck (or any inanimate object). Often, the act of explaining reveals the bug.

## Debugging Tools and Techniques

### 1. Print Statements
The simplest debugging technique:

```python
def calculate_average(numbers):
    print(f"Input: {numbers}")  # Debug print
    
    total = sum(numbers)
    print(f"Total: {total}")    # Debug print
    
    count = len(numbers)
    print(f"Count: {count}")    # Debug print
    
    if count == 0:
        return 0
    
    average = total / count
    print(f"Average: {average}")  # Debug print
    
    return average
```

**Best Practices for Print Debugging:**
- Use descriptive messages
- Include variable names and values
- Remove debug prints before production
- Consider using a debug flag

```python
DEBUG = True

def debug_print(message):
    if DEBUG:
        print(f"DEBUG: {message}")

def my_function(x):
    debug_print(f"Function called with x={x}")
    result = x * 2
    debug_print(f"Result: {result}")
    return result
```

### 2. Python Debugger (pdb)
The built-in Python debugger provides powerful debugging capabilities:

```python
import pdb

def problematic_function(data):
    pdb.set_trace()  # Execution will pause here
    
    result = []
    for item in data:
        processed = item * 2
        result.append(processed)
    
    return result

# Usage
numbers = [1, 2, 3, 4, 5]
result = problematic_function(numbers)
```

**Common pdb Commands:**
- `n` (next): Execute next line
- `s` (step): Step into function calls
- `c` (continue): Continue execution
- `l` (list): Show current code
- `p <variable>`: Print variable value
- `pp <variable>`: Pretty-print variable
- `h` (help): Show help
- `q` (quit): Quit debugger

### 3. Using breakpoint() (Python 3.7+)
Modern Python provides a built-in breakpoint function:

```python
def calculate_factorial(n):
    if n < 0:
        breakpoint()  # Pause execution here
        raise ValueError("Negative numbers not allowed")
    
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
        breakpoint()  # Pause in each iteration
    
    return result
```

### 4. IDE Debuggers
Most IDEs provide graphical debuggers with features like:
- Visual breakpoints
- Variable inspection
- Call stack visualization
- Step-through execution

### 5. Logging for Debugging
Use the logging module for more sophisticated debugging:

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_data(data):
    logging.debug(f"Processing data: {data}")
    
    if not data:
        logging.warning("Empty data received")
        return []
    
    result = []
    for i, item in enumerate(data):
        logging.debug(f"Processing item {i}: {item}")
        
        try:
            processed = item.upper()
            result.append(processed)
            logging.debug(f"Successfully processed: {processed}")
        except AttributeError:
            logging.error(f"Item {i} is not a string: {item}")
            continue
    
    logging.info(f"Processed {len(result)} items successfully")
    return result
```

## Common Debugging Scenarios

### 1. Infinite Loops
```python
# Problematic code
def count_down(n):
    while n > 0:
        print(n)
        # Bug: forgot to decrement n
        # n -= 1  # This line is missing

# Debugging approach
def count_down_debug(n):
    iteration = 0
    while n > 0:
        print(f"Iteration {iteration}: n = {n}")
        if iteration > 10:  # Safety check
            print("Breaking to prevent infinite loop")
            break
        n -= 1
        iteration += 1
```

### 2. Variable Scope Issues
```python
# Problematic code
def modify_list(lst):
    lst = [1, 2, 3]  # This creates a new local variable
    return lst

original = [4, 5, 6]
result = modify_list(original)
print(original)  # Still [4, 5, 6] - not modified!

# Debugging with print statements
def modify_list_debug(lst):
    print(f"Input list id: {id(lst)}")
    lst = [1, 2, 3]
    print(f"New list id: {id(lst)}")
    return lst
```

### 3. Mutable Default Arguments
```python
# Problematic code
def add_item(item, target_list=[]):
    target_list.append(item)
    return target_list

# This causes unexpected behavior
list1 = add_item("a")
list2 = add_item("b")
print(list1)  # ['a', 'b'] - unexpected!

# Debugging version
def add_item_debug(item, target_list=None):
    if target_list is None:
        print("Creating new list")
        target_list = []
    else:
        print(f"Using existing list: {target_list}")
    
    target_list.append(item)
    print(f"List after append: {target_list}")
    return target_list
```

## Advanced Debugging Techniques

### 1. Binary Search Debugging
For large codebases, use binary search to isolate bugs:

1. Comment out half of the suspicious code
2. Run the program
3. If bug persists, the problem is in the remaining half
4. If bug disappears, the problem is in the commented half
5. Repeat until you find the exact line

### 2. Minimal Reproducible Example
Create the smallest possible code that reproduces the bug:

```python
# Original complex code with bug
class DataProcessor:
    def __init__(self, config):
        self.config = config
        self.data = []
    
    def load_data(self, filename):
        # Complex file loading logic
        pass
    
    def process(self):
        # Complex processing with bug somewhere
        pass

# Minimal example
def process_item(item):
    # Isolated the specific problematic operation
    return item.split(",")[2]  # IndexError if less than 3 parts

# Test with minimal data
test_data = "a,b"  # This will cause the bug
result = process_item(test_data)
```

### 3. Assertion-Based Debugging
Use assertions to catch bugs early:

```python
def calculate_percentage(part, total):
    assert total > 0, f"Total must be positive, got {total}"
    assert part >= 0, f"Part must be non-negative, got {part}"
    assert part <= total, f"Part ({part}) cannot be greater than total ({total})"
    
    percentage = (part / total) * 100
    
    assert 0 <= percentage <= 100, f"Percentage should be 0-100, got {percentage}"
    
    return percentage
```

### 4. Exception Handling for Debugging
Use try/except blocks to gather more information:

```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print(f"Division by zero: {a} / {b}")
        print(f"Type of a: {type(a)}, Type of b: {type(b)}")
        raise
    except TypeError as e:
        print(f"Type error in division: {e}")
        print(f"a = {a} (type: {type(a)})")
        print(f"b = {b} (type: {type(b)})")
        raise
```

## Debugging Best Practices

### 1. Version Control for Debugging
Use git to help with debugging:

```bash
# Find when a bug was introduced
git bisect start
git bisect bad HEAD
git bisect good <last-known-good-commit>

# Git will help you find the problematic commit
```

### 2. Test-Driven Debugging
Write a test that reproduces the bug:

```python
def test_bug_reproduction():
    """Test that reproduces the reported bug."""
    # This test should fail initially
    result = problematic_function(test_input)
    assert result == expected_output

# Fix the bug, then the test should pass
```

### 3. Documentation During Debugging
Keep notes of what you've tried:

```python
# Bug: Function returns wrong result for negative inputs
# Tried: Checking input validation - not the issue
# Tried: Checking calculation logic - found the problem here
# Fix: Changed condition from > to >= on line 15

def my_function(x):
    # Fixed: was if x > 0, should be if x >= 0
    if x >= 0:
        return x * 2
    else:
        return x * -2
```

### 4. Debugging Checklist
Before diving deep into debugging:

- [ ] Can you reproduce the bug consistently?
- [ ] Do you have the exact error message?
- [ ] What was the expected vs. actual behavior?
- [ ] What changed recently that might have caused this?
- [ ] Have you checked the documentation?
- [ ] Have you searched for similar issues online?

## Tools and Resources

### IDE Debuggers
- **PyCharm**: Full-featured debugger with GUI
- **VS Code**: Python extension with debugging support
- **Sublime Text**: Various debugging plugins

### Command Line Tools
- **pdb**: Built-in Python debugger
- **ipdb**: Enhanced pdb with IPython features
- **pudb**: Full-screen console debugger

### Online Resources
- Stack Overflow for common error patterns
- Python documentation for understanding behavior
- GitHub issues for library-specific problems

## Common Pitfalls to Avoid

1. **Changing too much at once**: Make small, incremental changes
2. **Not reading error messages carefully**: They often contain the solution
3. **Debugging in production**: Always debug in a safe environment
4. **Not removing debug code**: Clean up before committing
5. **Giving up too quickly**: Debugging requires patience and persistence

## Summary

Effective debugging is a skill that improves with practice. Key takeaways:

- **Read error messages carefully** - they're your first clue
- **Use systematic approaches** - don't debug randomly
- **Start simple** - print statements are often sufficient
- **Use the right tools** - pdb for complex issues, IDE debuggers for visual debugging
- **Create minimal examples** - isolate the problem
- **Document your process** - learn from each debugging session
- **Practice defensive programming** - use assertions and proper error handling

Remember: every bug is an opportunity to learn something new about your code and improve your debugging skills.

---

**Next**: [Logging](03_logging.md)