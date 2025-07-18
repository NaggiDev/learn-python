# String Manipulation

## Introduction

Strings are one of the most commonly used data types in Python. They represent sequences of characters and are used for storing and manipulating text. Python provides a rich set of operations and methods for string manipulation, making it a powerful language for text processing.

In this lesson, you will learn how to create, access, and manipulate strings, as well as common string operations and methods for text processing.

## Creating Strings

Strings in Python can be created using single quotes, double quotes, or triple quotes:

```python
# Using single quotes
single_quoted = 'Hello, World!'

# Using double quotes
double_quoted = "Hello, World!"

# Using triple quotes (for multi-line strings)
multi_line = """This is a
multi-line string
in Python."""

# Triple quotes with single quotes
triple_single = '''Another
multi-line string
with 'single quotes' inside.'''
```

## String Indexing and Slicing

Like other sequence types in Python, strings support indexing and slicing:

### Indexing

```python
text = "Python"

# Accessing by positive index (from the beginning)
print(text[0])   # "P"
print(text[2])   # "t"

# Accessing by negative index (from the end)
print(text[-1])  # "n"
print(text[-3])  # "h"
```

### Slicing

```python
text = "Python Programming"

# Basic slicing [start:stop] (stop is exclusive)
print(text[0:6])    # "Python"
print(text[7:18])   # "Programming"

# Omitting start (defaults to 0)
print(text[:6])     # "Python"

# Omitting stop (defaults to length of string)
print(text[7:])     # "Programming"

# Negative indices in slicing
print(text[-11:-1])  # "Programmin"

# Step parameter [start:stop:step]
print(text[::2])     # "Pto rgamn"

# Reversing a string
print(text[::-1])    # "gnimmargorP nohtyP"
```

## String Immutability

Strings in Python are immutable, which means they cannot be changed after creation:

```python
text = "Python"

# This will raise a TypeError
try:
    text[0] = "J"
except TypeError as e:
    print(f"Error: {e}")  # Error: 'str' object does not support item assignment

# To modify a string, create a new one
new_text = "J" + text[1:]
print(new_text)  # "Jython"
```

## String Concatenation

Strings can be concatenated (combined) using the `+` operator:

```python
first_name = "John"
last_name = "Doe"

# Using + operator
full_name = first_name + " " + last_name
print(full_name)  # "John Doe"

# Using += operator
greeting = "Hello, "
greeting += "World!"
print(greeting)  # "Hello, World!"
```

## String Repetition

Strings can be repeated using the `*` operator:

```python
word = "Python "
repeated = word * 3
print(repeated)  # "Python Python Python "
```

## String Methods

Python provides numerous built-in methods for string manipulation:

### Case Conversion

```python
text = "Python Programming"

# Converting to uppercase
print(text.upper())  # "PYTHON PROGRAMMING"

# Converting to lowercase
print(text.lower())  # "python programming"

# Capitalizing (first character uppercase, rest lowercase)
print("hello world".capitalize())  # "Hello world"

# Title case (first character of each word uppercase)
print("hello world".title())  # "Hello World"

# Swapping case
print("Hello World".swapcase())  # "hELLO wORLD"
```

### Checking String Content

```python
# Checking if a string starts with a prefix
print("Python".startswith("Py"))  # True
print("Python".startswith("py"))  # False (case-sensitive)

# Checking if a string ends with a suffix
print("Python".endswith("on"))  # True
print("Python".endswith("ON"))  # False (case-sensitive)

# Checking if a string contains only alphabetic characters
print("Python".isalpha())  # True
print("Python3".isalpha())  # False (contains a number)

# Checking if a string contains only digits
print("123".isdigit())  # True
print("123a".isdigit())  # False (contains a letter)

# Checking if a string contains only alphanumeric characters
print("Python3".isalnum())  # True
print("Python 3".isalnum())  # False (contains a space)

# Checking if a string is lowercase
print("python".islower())  # True
print("Python".islower())  # False

# Checking if a string is uppercase
print("PYTHON".isupper())  # True
print("Python".isupper())  # False

# Checking if a string is a valid identifier
print("variable_name".isidentifier())  # True
print("123variable".isidentifier())  # False (starts with a digit)

# Checking if a string is whitespace
print("   \t\n".isspace())  # True
print("   a   ".isspace())  # False (contains a non-whitespace character)
```

### Finding and Counting

```python
text = "Python is a programming language. Python is easy to learn."

# Finding the position of a substring (first occurrence)
print(text.find("Python"))  # 0 (index of first occurrence)
print(text.find("Java"))    # -1 (not found)

# Finding the position of a substring (last occurrence)
print(text.rfind("Python"))  # 33 (index of last occurrence)

# Finding the position with error for not found
try:
    print(text.index("Java"))  # Raises ValueError if not found
except ValueError as e:
    print(f"Error: {e}")  # Error: substring not found

# Counting occurrences of a substring
print(text.count("Python"))  # 2
```

### Stripping Whitespace

```python
text = "   Python Programming   "

# Removing whitespace from both ends
print(text.strip())  # "Python Programming"

# Removing whitespace from the left end
print(text.lstrip())  # "Python Programming   "

# Removing whitespace from the right end
print(text.rstrip())  # "   Python Programming"

# Stripping specific characters
text = "###Python###"
print(text.strip("#"))  # "Python"
```

### Replacing Substrings

```python
text = "Python is a programming language. Python is easy to learn."

# Replacing all occurrences
new_text = text.replace("Python", "Java")
print(new_text)  # "Java is a programming language. Java is easy to learn."

# Replacing with a limit
new_text = text.replace("Python", "Java", 1)
print(new_text)  # "Java is a programming language. Python is easy to learn."
```

### Splitting and Joining

```python
# Splitting a string into a list
text = "Python,Java,C++,JavaScript"
languages = text.split(",")
print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']

# Splitting with a maximum number of splits
text = "Python,Java,C++,JavaScript"
languages = text.split(",", 2)
print(languages)  # ['Python', 'Java', 'C++,JavaScript']

# Splitting by whitespace (default)
text = "Python Java C++ JavaScript"
languages = text.split()
print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']

# Splitting by lines
text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# Joining a list into a string
languages = ['Python', 'Java', 'C++', 'JavaScript']
text = ", ".join(languages)
print(text)  # "Python, Java, C++, JavaScript"

# Joining with an empty string
chars = ['H', 'e', 'l', 'l', 'o']
word = "".join(chars)
print(word)  # "Hello"
```

### Alignment and Padding

```python
text = "Python"

# Center alignment with padding
print(text.center(20))        # "       Python       "
print(text.center(20, "-"))   # "-------Python-------"

# Left alignment with padding
print(text.ljust(20))         # "Python              "
print(text.ljust(20, "-"))    # "Python--------------"

# Right alignment with padding
print(text.rjust(20))         # "              Python"
print(text.rjust(20, "-"))    # "--------------Python"

# Zero padding for numbers
num = "42"
print(num.zfill(5))           # "00042"
```

### String Formatting

Python offers several ways to format strings:

#### %-formatting (older style)

```python
name = "Alice"
age = 30

# Using % operator
message = "My name is %s and I am %d years old." % (name, age)
print(message)  # "My name is Alice and I am 30 years old."

# Formatting numbers
pi = 3.14159
formatted = "Pi is approximately %.2f" % pi
print(formatted)  # "Pi is approximately 3.14"
```

#### str.format() method

```python
name = "Bob"
age = 25

# Basic formatting
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # "My name is Bob and I am 25 years old."

# Positional arguments
message = "My name is {0} and I am {1} years old. {0} is my name.".format(name, age)
print(message)  # "My name is Bob and I am 25 years old. Bob is my name."

# Named arguments
message = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(message)  # "My name is Bob and I am 25 years old."

# Formatting numbers
pi = 3.14159
formatted = "Pi is approximately {:.2f}".format(pi)
print(formatted)  # "Pi is approximately 3.14"
```

#### f-strings (Python 3.6+)

```python
name = "Charlie"
age = 35

# Basic f-string
message = f"My name is {name} and I am {age} years old."
print(message)  # "My name is Charlie and I am 35 years old."

# Expressions in f-strings
message = f"In 5 years, I will be {age + 5} years old."
print(message)  # "In 5 years, I will be 40 years old."

# Formatting in f-strings
pi = 3.14159
formatted = f"Pi is approximately {pi:.2f}"
print(formatted)  # "Pi is approximately 3.14"
```

## String Formatting Specification

Both `str.format()` and f-strings support a mini-language for formatting values:

```python
# Number formatting
value = 12345.6789

# Width and precision
print(f"{value:10.2f}")  # "  12345.68" (width 10, 2 decimal places)

# Left alignment
print(f"{value:<10.2f}")  # "12345.68  " (left aligned)

# Right alignment
print(f"{value:>10.2f}")  # "  12345.68" (right aligned)

# Center alignment
print(f"{value:^10.2f}")  # " 12345.68 " (center aligned)

# Zero padding
print(f"{value:010.2f}")  # "0012345.68" (zero padded)

# With thousands separator
print(f"{value:,.2f}")    # "12,345.68" (with comma as separator)

# Percentage
print(f"{0.25:.1%}")      # "25.0%" (as percentage)

# Different bases
value = 42
print(f"{value:b}")       # "101010" (binary)
print(f"{value:o}")       # "52" (octal)
print(f"{value:x}")       # "2a" (hexadecimal lowercase)
print(f"{value:X}")       # "2A" (hexadecimal uppercase)
```

## Raw Strings

Raw strings are prefixed with `r` and treat backslashes as literal characters, which is useful for regular expressions and file paths:

```python
# Normal string (backslash is an escape character)
path = "C:\\Users\\John\\Documents"
print(path)  # "C:\Users\John\Documents"

# Raw string (backslash is treated as a literal character)
path = r"C:\Users\John\Documents"
print(path)  # "C:\Users\John\Documents"
```

## String Escape Sequences

Python supports various escape sequences in strings:

```python
# Newline
print("Line 1\nLine 2")  # Prints on two lines

# Tab
print("Name:\tJohn")  # "Name:   John"

# Backslash
print("This is a backslash: \\")  # "This is a backslash: \"

# Single and double quotes
print("He said, \"Hello!\"")  # "He said, "Hello!""
print('She said, \'Hi!\'')    # "She said, 'Hi!'"

# Unicode characters
print("\u03C0")  # "π" (Greek letter pi)
print("\U0001F600")  # "😀" (grinning face emoji)

# Hexadecimal character
print("\x41")  # "A" (ASCII value 65 in hex)
```

## String Comparison

Strings in Python can be compared using comparison operators:

```python
# Equality
print("apple" == "apple")  # True
print("apple" == "Apple")  # False (case-sensitive)

# Inequality
print("apple" != "banana")  # True

# Lexicographical comparison
print("apple" < "banana")   # True (a comes before b)
print("apple" > "Apple")    # True (lowercase comes after uppercase in ASCII)

# Case-insensitive comparison
print("apple".lower() == "Apple".lower())  # True
```

## Common String Operations

### Checking if a String Contains a Substring

```python
text = "Python Programming"

# Using the 'in' operator
contains_python = "Python" in text
print(contains_python)  # True

contains_java = "Java" in text
print(contains_java)    # False

# Case-insensitive check
contains_python_case_insensitive = "python" in text.lower()
print(contains_python_case_insensitive)  # True
```

### Reversing a String

```python
text = "Python"

# Using slicing
reversed_text = text[::-1]
print(reversed_text)  # "nohtyP"

# Using reversed() and join()
reversed_text = "".join(reversed(text))
print(reversed_text)  # "nohtyP"
```

### Removing Prefix and Suffix (Python 3.9+)

```python
# In Python 3.9 and later
text = "prefix_content_suffix"

# Remove prefix
without_prefix = text.removeprefix("prefix_")
print(without_prefix)  # "content_suffix"

# Remove suffix
without_suffix = text.removesuffix("_suffix")
print(without_suffix)  # "prefix_content"
```

### Translating Characters

```python
# Using str.maketrans() and translate()
text = "Hello, World!"

# Create a translation table
translation_table = str.maketrans({
    "H": "J",
    "W": "P",
    ",": "!",
    "!": "?"
})

# Apply the translation
translated = text.translate(translation_table)
print(translated)  # "Jello! Porld?"

# Creating a translation table from two strings
translation_table = str.maketrans("aeiou", "12345")
translated = "Hello, World!".translate(translation_table)
print(translated)  # "H2ll4, W4rld!"

# With a third argument to specify characters to delete
translation_table = str.maketrans("aeiou", "12345", "!, ")
translated = "Hello, World!".translate(translation_table)
print(translated)  # "H2ll4W4rld"
```

## Regular Expressions

For more complex string pattern matching and manipulation, Python provides the `re` module for regular expressions:

```python
import re

text = "The quick brown fox jumps over the lazy dog"

# Searching for a pattern
match = re.search(r"fox", text)
if match:
    print(f"Found 'fox' at position {match.start()}")  # Found 'fox' at position 16

# Finding all occurrences
matches = re.findall(r"\b\w{4}\b", text)  # Find all 4-letter words
print(matches)  # ['quick', 'over', 'lazy']

# Replacing with a pattern
new_text = re.sub(r"\b\w{4}\b", "XXXX", text)
print(new_text)  # "The XXXX brown fox jumps XXXX the XXXX dog"

# Splitting with a pattern
parts = re.split(r"\s+", text)  # Split by whitespace
print(parts)  # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

## String Performance Considerations

- String concatenation with `+` creates a new string each time, which can be inefficient for many operations
- For building strings from many pieces, use `join()` or `io.StringIO`
- String methods create new strings (due to immutability)
- Regular expressions are powerful but can be slower than string methods for simple operations

```python
# Inefficient string building
result = ""
for i in range(1000):
    result += str(i)  # Creates 1000 intermediate strings

# More efficient string building
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)  # Creates only one final string

# Using StringIO for building strings
from io import StringIO
buffer = StringIO()
for i in range(1000):
    buffer.write(str(i))
result = buffer.getvalue()
```

## Common String Patterns

### Parsing CSV Data

```python
csv_line = "John,Doe,30,Developer"

# Simple parsing
fields = csv_line.split(",")
print(fields)  # ['John', 'Doe', '30', 'Developer']

# Handling quoted fields with regex
import re
csv_line = 'John,"Doe, Jr.",30,Developer'
fields = re.findall(r'(?:[^,"]|"(?:[^"])*")+', csv_line)
print(fields)  # ['John', '"Doe, Jr."', '30', 'Developer']
```

### Extracting Information

```python
# Extracting email addresses
text = "Contact us at info@example.com or support@example.org"
import re
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)  # ['info@example.com', 'support@example.org']

# Extracting dates
text = "Meeting on 2023-07-15 and deadline on 2023-08-30"
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print(dates)  # ['2023-07-15', '2023-08-30']
```

### Validating Input

```python
# Validating email format
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid-email"))     # False

# Validating password strength
def is_strong_password(password):
    # At least 8 characters, one uppercase, one lowercase, one digit
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.match(pattern, password))

print(is_strong_password("Passw0rd"))  # True
print(is_strong_password("password"))  # False
```

## Summary

- Strings in Python are immutable sequences of characters
- Python provides numerous methods for string manipulation
- String formatting can be done using %-formatting, str.format(), or f-strings
- Regular expressions offer powerful pattern matching capabilities
- Efficient string operations are important for performance
- Common string operations include searching, replacing, splitting, and joining

In the next module, we'll explore file operations, which will allow you to read from and write to files using the string manipulation techniques you've learned.