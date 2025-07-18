# Reading and Writing Files in Python

## Introduction

File input/output (I/O) operations are essential for working with persistent data in Python. Whether you're reading configuration settings, processing data files, or saving program output, understanding how to work with files is a fundamental skill for any Python programmer.

In this lesson, you'll learn how to:
- Open and close files properly
- Read data from files using different methods
- Write data to files
- Work with file paths
- Use context managers for safer file handling

## File Basics

### File Paths

Before working with files, you need to understand file paths:

- **Absolute paths** start from the root directory of the file system
  - Windows: `C:\Users\username\Documents\file.txt`
  - Unix/Mac: `/home/username/Documents/file.txt`

- **Relative paths** are relative to the current working directory
  - `data/file.txt` (a subdirectory of the current directory)
  - `../data/file.txt` (a subdirectory of the parent directory)

Python's `os` and `pathlib` modules provide tools for working with paths in a platform-independent way:

```python
# Using os.path (traditional approach)
import os
file_path = os.path.join('data', 'file.txt')  # Creates 'data/file.txt' or 'data\\file.txt' depending on OS

# Using pathlib (modern approach, Python 3.4+)
from pathlib import Path
file_path = Path('data') / 'file.txt'  # Creates a Path object representing 'data/file.txt'
```

### File Modes

When opening a file, you specify a mode that determines how the file will be used:

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) - Open for reading |
| `'w'` | Write - Open for writing (creates new file or truncates existing file) |
| `'a'` | Append - Open for writing, appending to the end of file |
| `'x'` | Exclusive creation - Open for writing, fail if file already exists |
| `'b'` | Binary mode (added to other modes) |
| `'t'` | Text mode (default, added to other modes) |
| `'+'` | Update mode - Open for reading and writing |

## Reading Files

### Opening and Closing Files

The basic pattern for working with files is:

```python
# Open a file
file = open('example.txt', 'r')

# Work with the file
content = file.read()
print(content)

# Close the file
file.close()
```

However, this approach has a problem: if an error occurs between opening and closing, the file might remain open. This can lead to resource leaks or file corruption.

### Using Context Managers (with statement)

The recommended way to work with files is using the `with` statement, which ensures proper file closure:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed when the block ends
```

### Reading Methods

Python provides several methods for reading file content:

```python
# Read the entire file as a single string
with open('example.txt', 'r') as file:
    content = file.read()

# Read line by line
with open('example.txt', 'r') as file:
    line = file.readline()  # Read a single line
    
# Read all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()  # Returns a list of lines

# Iterate through lines (memory efficient for large files)
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character
```

## Writing Files

### Basic Writing

To write to a file, open it in write mode (`'w'`) or append mode (`'a'`):

```python
# Write mode (creates new file or overwrites existing file)
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.')

# Append mode (adds to the end of the file)
with open('output.txt', 'a') as file:
    file.write('\nThis line is appended.')
```

### Writing Multiple Lines

You can write multiple lines at once using a list and the `writelines()` method:

```python
lines = ['First line\n', 'Second line\n', 'Third line\n']

with open('output.txt', 'w') as file:
    file.writelines(lines)
```

Note that `writelines()` doesn't add newline characters automatically; you need to include them in your strings.

## Working with Binary Files

For non-text files (images, audio, etc.), use binary mode:

```python
# Reading binary data
with open('image.jpg', 'rb') as file:
    binary_data = file.read()

# Writing binary data
with open('copy.jpg', 'wb') as file:
    file.write(binary_data)
```

## File Properties and Operations

Python provides functions to check file properties and perform operations:

```python
import os

# Check if a file exists
if os.path.exists('file.txt'):
    print('File exists')

# Get file size
size = os.path.getsize('file.txt')  # Size in bytes

# Delete a file
os.remove('file.txt')

# Rename a file
os.rename('old_name.txt', 'new_name.txt')
```

With `pathlib`, these operations can be more intuitive:

```python
from pathlib import Path

file_path = Path('file.txt')

# Check if a file exists
if file_path.exists():
    print('File exists')

# Get file size
size = file_path.stat().st_size

# Delete a file
file_path.unlink()

# Rename a file
file_path.rename('new_name.txt')
```

## Best Practices

1. **Always use the `with` statement** to ensure files are properly closed
2. **Handle exceptions** that might occur during file operations
3. **Use appropriate modes** (text vs. binary) based on file content
4. **Consider using `pathlib`** for more readable and platform-independent path handling
5. **Be careful with write mode (`'w'`)** as it will overwrite existing files
6. **For large files, process them line by line** rather than reading the entire file into memory

## Common Pitfalls

1. **Forgetting to close files** when not using `with` statement
2. **Using the wrong path separator** (use `os.path.join()` or `pathlib` to avoid this)
3. **Not handling file not found errors**
4. **Reading large files entirely into memory**
5. **Using text mode for binary files** or vice versa

## Summary

In this lesson, you've learned:
- How to open and close files properly using the `with` statement
- Different file modes for reading, writing, and appending
- Methods for reading file content (read, readline, readlines)
- How to write data to files
- Working with binary files
- File operations like checking existence, getting size, and deleting
- Best practices for file handling in Python

In the next lesson, you'll learn about working with CSV files, a common format for structured data.

## Additional Resources

- [Python Documentation: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python pathlib Module](https://docs.python.org/3/library/pathlib.html)
- [Python os.path Module](https://docs.python.org/3/library/os.path.html)