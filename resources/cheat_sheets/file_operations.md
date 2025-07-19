# File Operations Cheat Sheet

## Basic File Operations

### Opening and Closing Files
```python
# Basic file opening
file = open('filename.txt', 'r')  # Open for reading
content = file.read()
file.close()  # Always close files

# Using context manager (recommended)
with open('filename.txt', 'r') as file:
    content = file.read()
# File is automatically closed
```

### File Modes
```python
# Reading modes
'r'   # Read (default)
'rb'  # Read binary
'rt'  # Read text (explicit)

# Writing modes
'w'   # Write (overwrites existing file)
'wb'  # Write binary
'wt'  # Write text (explicit)

# Appending modes
'a'   # Append
'ab'  # Append binary
'at'  # Append text

# Read/Write modes
'r+'  # Read and write
'w+'  # Write and read (overwrites)
'a+'  # Append and read

# Examples
with open('file.txt', 'w') as f:    # Write mode
    f.write('Hello, World!')

with open('file.txt', 'a') as f:    # Append mode
    f.write('\nNew line')

with open('file.bin', 'rb') as f:   # Binary read mode
    data = f.read()
```

## Reading Files

### Reading Entire File
```python
# Read all content as string
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# Read all lines as list
with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(lines)  # ['line1\n', 'line2\n', ...]
```

### Reading Line by Line
```python
# Method 1: Using readline()
with open('file.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line.strip())  # strip() removes newline
        line = f.readline()

# Method 2: Iterating over file object (recommended)
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Method 3: Using readlines()
with open('file.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())
```

### Reading Specific Amount
```python
with open('file.txt', 'r') as f:
    # Read first 10 characters
    chunk = f.read(10)
    
    # Read next 5 characters
    next_chunk = f.read(5)
```

## Writing Files

### Writing Text
```python
# Write string to file
with open('output.txt', 'w') as f:
    f.write('Hello, World!')
    f.write('\nSecond line')

# Write multiple lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)

# Using print() to write to file
with open('output.txt', 'w') as f:
    print('Hello, World!', file=f)
    print('Second line', file=f)
```

### Appending to Files
```python
# Append to existing file
with open('existing_file.txt', 'a') as f:
    f.write('\nAppended line')

# Append with timestamp
import datetime
with open('log.txt', 'a') as f:
    timestamp = datetime.datetime.now()
    f.write(f'{timestamp}: Log entry\n')
```

## Working with CSV Files

### Reading CSV
```python
import csv

# Basic CSV reading
with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)  # Each row is a list

# Reading CSV with headers
with open('data.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        print(row)  # Each row is a dictionary

# Reading specific columns
with open('data.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        print(f"Name: {row['name']}, Age: {row['age']}")
```

### Writing CSV
```python
import csv

# Basic CSV writing
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('output.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data)

# Writing CSV with DictWriter
fieldnames = ['name', 'age', 'city']
data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
]

with open('output.csv', 'w', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)
```

## Working with JSON Files

### Reading JSON
```python
import json

# Read JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# Read JSON string
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)
print(data['name'])  # Alice
```

### Writing JSON
```python
import json

# Write to JSON file
data = {
    'name': 'Alice',
    'age': 30,
    'hobbies': ['reading', 'swimming']
}

with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
```

## File and Directory Operations

### Using os module
```python
import os

# Current working directory
current_dir = os.getcwd()
print(current_dir)

# Change directory
os.chdir('/path/to/directory')

# List directory contents
files = os.listdir('.')
print(files)

# Check if file/directory exists
if os.path.exists('file.txt'):
    print('File exists')

if os.path.isfile('file.txt'):
    print('It is a file')

if os.path.isdir('directory'):
    print('It is a directory')

# Create directory
os.mkdir('new_directory')
os.makedirs('path/to/nested/directory')  # Create nested directories

# Remove files and directories
os.remove('file.txt')        # Remove file
os.rmdir('directory')        # Remove empty directory
os.removedirs('path/to/dir') # Remove nested directories
```

### Using pathlib (Python 3.4+)
```python
from pathlib import Path

# Create Path object
path = Path('data/file.txt')

# Check if exists
if path.exists():
    print('Path exists')

# Read file
content = path.read_text()

# Write file
path.write_text('Hello, World!')

# Get file info
print(path.name)        # file.txt
print(path.stem)        # file
print(path.suffix)      # .txt
print(path.parent)      # data

# Create directory
path.mkdir(parents=True, exist_ok=True)

# List directory contents
for item in path.iterdir():
    print(item)

# Find files with pattern
for txt_file in path.glob('*.txt'):
    print(txt_file)
```

## Error Handling with Files

### Common File Exceptions
```python
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')
except IOError:
    print('I/O error occurred')

# More specific error handling
try:
    with open('file.txt', 'r') as f:
        content = f.read()
        # Process content
except FileNotFoundError:
    print('File does not exist')
    # Create default file or ask user for correct path
except PermissionError:
    print('No permission to read file')
    # Handle permission issue
except UnicodeDecodeError:
    print('File encoding issue')
    # Try different encoding
    with open('file.txt', 'r', encoding='latin-1') as f:
        content = f.read()
```

### Safe File Operations
```python
def safe_read_file(filename):
    """Safely read a file with error handling."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {e}")
        return None

def safe_write_file(filename, content):
    """Safely write to a file with error handling."""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return True
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'")
        return False
    except Exception as e:
        print(f"Unexpected error writing to '{filename}': {e}")
        return False
```

## Working with Different Encodings

### Handling Text Encodings
```python
# Specify encoding when opening files
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Common encodings
encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']

def read_with_fallback_encoding(filename):
    """Try multiple encodings to read a file."""
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Could not decode {filename} with any encoding")
```

## Binary Files

### Reading Binary Files
```python
# Read binary file
with open('image.jpg', 'rb') as f:
    binary_data = f.read()

# Read binary in chunks
def read_binary_chunks(filename, chunk_size=1024):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage
for chunk in read_binary_chunks('large_file.bin'):
    # Process chunk
    pass
```

### Writing Binary Files
```python
# Write binary data
binary_data = b'\x00\x01\x02\x03'
with open('output.bin', 'wb') as f:
    f.write(binary_data)

# Copy binary file
def copy_binary_file(source, destination):
    with open(source, 'rb') as src, open(destination, 'wb') as dst:
        dst.write(src.read())
```

## Temporary Files

### Using tempfile module
```python
import tempfile
import os

# Create temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write('Temporary content')
    temp_filename = temp_file.name

# Use the temporary file
with open(temp_filename, 'r') as f:
    content = f.read()

# Clean up
os.unlink(temp_filename)

# Create temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    # Use temp_dir
    temp_file_path = os.path.join(temp_dir, 'temp_file.txt')
    with open(temp_file_path, 'w') as f:
        f.write('Content in temporary directory')
# Directory is automatically cleaned up
```

## Common Patterns and Best Practices

### File Processing Template
```python
def process_file(input_filename, output_filename, process_function):
    """Template for file processing operations."""
    try:
        with open(input_filename, 'r') as infile, \
             open(output_filename, 'w') as outfile:
            
            for line in infile:
                processed_line = process_function(line)
                outfile.write(processed_line)
                
    except FileNotFoundError:
        print(f"Input file '{input_filename}' not found")
    except Exception as e:
        print(f"Error processing file: {e}")

# Usage
def uppercase_line(line):
    return line.upper()

process_file('input.txt', 'output.txt', uppercase_line)
```

### Configuration File Handling
```python
import configparser

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Access configuration values
database_host = config['database']['host']
database_port = config.getint('database', 'port')

# Write configuration file
config['database'] = {
    'host': 'localhost',
    'port': '5432',
    'name': 'mydb'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)
```

### Log File Handling
```python
import logging
from datetime import datetime

# Set up logging to file
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log messages
logging.info('Application started')
logging.warning('This is a warning')
logging.error('An error occurred')

# Rotate log files
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    'app.log', 
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)
```

## Performance Tips

- Use context managers (`with` statement) for automatic file closing
- Read large files line by line instead of loading everything into memory
- Use appropriate buffer sizes for binary file operations
- Consider using `pathlib` for modern path operations
- Handle encoding explicitly to avoid issues
- Use generators for processing large files
- Close files properly to avoid resource leaks