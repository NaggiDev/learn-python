# Python Standard Library Cheat Sheet

## os - Operating System Interface

### File and Directory Operations
```python
import os

# Current directory
current_dir = os.getcwd()
os.chdir('/path/to/directory')

# Directory listing
files = os.listdir('.')
for root, dirs, files in os.walk('.'):
    for file in files:
        print(os.path.join(root, file))

# File/directory checks
os.path.exists('file.txt')
os.path.isfile('file.txt')
os.path.isdir('directory')
os.path.getsize('file.txt')

# Create/remove directories
os.mkdir('new_dir')
os.makedirs('path/to/nested/dir')
os.rmdir('empty_dir')
os.removedirs('path/to/nested/dir')

# Environment variables
home = os.environ.get('HOME')
os.environ['MY_VAR'] = 'value'
```

## sys - System-specific Parameters

### Command Line and System Info
```python
import sys

# Command line arguments
script_name = sys.argv[0]
arguments = sys.argv[1:]

# Python path
sys.path.append('/custom/path')
print(sys.path)

# Exit program
sys.exit(0)  # Exit with status code

# System information
print(sys.version)
print(sys.platform)
print(sys.executable)

# Standard streams
sys.stdout.write('Hello\n')
sys.stderr.write('Error\n')
```

## datetime - Date and Time

### Creating Dates and Times
```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
today = date.today()
current_time = datetime.now().time()

# Creating specific dates
birthday = date(1990, 5, 15)
meeting = datetime(2023, 12, 25, 14, 30, 0)

# Parsing strings
date_str = "2023-12-25"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")

# Formatting dates
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2023-12-25 14:30:45
```

### Date Arithmetic
```python
from datetime import timedelta

# Time differences
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)

# Calculate differences
age = today - birthday
print(age.days)  # Days since birthday
```

## json - JSON Data

### Reading and Writing JSON
```python
import json

# Python to JSON
data = {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'swimming']}
json_string = json.dumps(data, indent=2)

# JSON to Python
parsed_data = json.loads(json_string)

# File operations
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('data.json', 'r') as f:
    loaded_data = json.load(f)
```

## re - Regular Expressions

### Pattern Matching
```python
import re

text = "Contact us at support@example.com or sales@company.org"

# Find all matches
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Search for pattern
match = re.search(r'(\w+)@(\w+\.\w+)', text)
if match:
    username = match.group(1)
    domain = match.group(2)

# Replace patterns
censored = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 
                  '[EMAIL]', text)

# Split by pattern
parts = re.split(r'[,.]', "apple,banana.cherry")
```

### Common Patterns
```python
# Phone numbers
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'

# URLs
url_pattern = r'https?://[^\s]+'

# IP addresses
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Validate input
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

## collections - Specialized Container Types

### Counter
```python
from collections import Counter

# Count occurrences
text = "hello world"
char_count = Counter(text)
print(char_count)  # Counter({'l': 3, 'o': 2, 'h': 1, ...})

# Most common
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = Counter(words)
print(word_count.most_common(2))  # [('apple', 3), ('banana', 2)]
```

### defaultdict
```python
from collections import defaultdict

# Dictionary with default values
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')

# Group items
from collections import defaultdict
students = [('Alice', 'Math'), ('Bob', 'Science'), ('Alice', 'English')]
subjects = defaultdict(list)
for student, subject in students:
    subjects[student].append(subject)
```

### namedtuple
```python
from collections import namedtuple

# Create named tuple class
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')

# Create instances
p = Point(3, 4)
person = Person('Alice', 30, 'NYC')

# Access fields
print(p.x, p.y)  # 3 4
print(person.name)  # Alice
```

## itertools - Iterator Functions

### Infinite Iterators
```python
import itertools

# Count
for i in itertools.count(10, 2):  # Start at 10, step by 2
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20

# Cycle
colors = ['red', 'green', 'blue']
color_cycle = itertools.cycle(colors)
for _ in range(7):
    print(next(color_cycle))  # red, green, blue, red, green, blue, red

# Repeat
for item in itertools.repeat('hello', 3):
    print(item)  # hello, hello, hello
```

### Combinatorial Functions
```python
# Permutations
letters = ['A', 'B', 'C']
perms = list(itertools.permutations(letters, 2))
print(perms)  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Combinations
combs = list(itertools.combinations(letters, 2))
print(combs)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Product (Cartesian product)
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = list(itertools.product(colors, sizes))
print(products)  # [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

## random - Generate Random Numbers

### Basic Random Operations
```python
import random

# Random float between 0 and 1
rand_float = random.random()

# Random integer
rand_int = random.randint(1, 10)  # 1 to 10 inclusive
rand_range = random.randrange(0, 10, 2)  # 0, 2, 4, 6, 8

# Random choice
colors = ['red', 'green', 'blue']
chosen_color = random.choice(colors)

# Multiple random choices
chosen_colors = random.choices(colors, k=3)  # With replacement
sample_colors = random.sample(colors, 2)  # Without replacement

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
```

### Random with Seed
```python
# Set seed for reproducible results
random.seed(42)
print(random.random())  # Always same result with same seed
```

## urllib - URL Handling

### Making HTTP Requests
```python
from urllib.request import urlopen
from urllib.parse import urlencode, urlparse

# Simple GET request
with urlopen('https://httpbin.org/json') as response:
    data = response.read().decode('utf-8')

# Parse URLs
url = 'https://example.com/path?param=value'
parsed = urlparse(url)
print(parsed.scheme)  # https
print(parsed.netloc)  # example.com
print(parsed.path)    # /path

# Encode parameters
params = {'name': 'Alice', 'age': 30}
query_string = urlencode(params)  # name=Alice&age=30
```

## pathlib - Object-oriented File Paths

### Path Operations
```python
from pathlib import Path

# Create path objects
home = Path.home()
current = Path.cwd()
file_path = Path('data/file.txt')

# Path properties
print(file_path.name)      # file.txt
print(file_path.stem)      # file
print(file_path.suffix)    # .txt
print(file_path.parent)    # data

# Path operations
new_path = file_path.with_suffix('.csv')
absolute_path = file_path.resolve()

# File operations
if file_path.exists():
    content = file_path.read_text()
    file_path.write_text('New content')

# Directory operations
for txt_file in Path('.').glob('*.txt'):
    print(txt_file)
```

## math - Mathematical Functions

### Basic Math Operations
```python
import math

# Constants
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045

# Basic functions
math.sqrt(16)      # 4.0
math.pow(2, 3)     # 8.0
math.factorial(5)  # 120
math.gcd(12, 8)    # 4

# Trigonometry
math.sin(math.pi/2)  # 1.0
math.cos(0)          # 1.0
math.tan(math.pi/4)  # 1.0

# Logarithms
math.log(10)         # Natural log
math.log10(100)      # Base 10 log: 2.0
math.log(8, 2)       # Log base 2: 3.0

# Rounding
math.ceil(4.3)   # 5
math.floor(4.7)  # 4
```

## functools - Higher-order Functions

### Useful Decorators and Functions
```python
from functools import lru_cache, partial, reduce

# Memoization with lru_cache
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Partial functions
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))  # 10

# Reduce
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)  # 15
```

## argparse - Command Line Parsing

### Basic Argument Parsing
```python
import argparse

parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('filename', help='Input filename')
parser.add_argument('--output', '-o', help='Output filename')
parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
parser.add_argument('--count', type=int, default=1, help='Number of times to process')

args = parser.parse_args()

print(f"Processing {args.filename}")
if args.verbose:
    print("Verbose mode enabled")
```

## logging - Logging Facility

### Basic Logging
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create logger
logger = logging.getLogger(__name__)

# Log messages
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')

# Log to file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)
```

## csv - CSV File Reading and Writing

### Reading CSV
```python
import csv

# Read CSV file
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Read as dictionary
with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['column_name'])
```

### Writing CSV
```python
# Write CSV file
data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Write dictionary to CSV
fieldnames = ['name', 'age']
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)
```

## Common Usage Patterns

### Configuration Management
```python
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

database_host = config['database']['host']
database_port = config.getint('database', 'port')
```

### Temporary Files
```python
import tempfile

# Temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write('Temporary data')
    temp_filename = temp_file.name

# Temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    # Use temp_dir
    pass  # Directory automatically cleaned up
```

### Threading
```python
import threading
import time

def worker(name):
    for i in range(5):
        print(f"Worker {name}: {i}")
        time.sleep(1)

# Create and start threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
```