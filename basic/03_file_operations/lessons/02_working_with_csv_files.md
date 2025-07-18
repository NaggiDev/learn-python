# Working with CSV Files in Python

## Introduction

CSV (Comma-Separated Values) is one of the most common formats for storing and exchanging tabular data. It's a simple text format where each line represents a row of data, and values within a row are separated by commas (or other delimiters). CSV files are widely used for data exchange between different applications and systems because of their simplicity and universal support.

In this lesson, you'll learn how to:
- Read data from CSV files
- Write data to CSV files
- Process and manipulate CSV data
- Handle different CSV formats and dialects
- Work with the Python `csv` module

## CSV File Basics

A simple CSV file might look like this:

```
Name,Age,City
Alice,28,New York
Bob,35,San Francisco
Charlie,42,Chicago
```

This represents a table with three columns (Name, Age, City) and three rows of data.

### CSV Format Variations

While the basic concept is simple, CSV files can vary in their format:

- **Different delimiters**: While commas are common, some files use tabs (`\t`), semicolons (`;`), or other characters
- **Quoting**: Values containing the delimiter or newlines are typically enclosed in quotes
- **Headers**: Some CSV files include a header row with column names, others don't
- **Escaping**: Special characters might be escaped with backslashes or doubled quotes
- **Line endings**: Different operating systems use different line ending characters

Python's `csv` module handles these variations through the concept of "dialects."

## The Python CSV Module

Python's built-in `csv` module provides tools for reading and writing CSV files while handling the various format complexities.

### Reading CSV Files

The basic pattern for reading CSV files is:

```python
import csv

with open('data.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)  # row is a list of strings
```

#### Reading with Headers

If your CSV file has headers, you can use `csv.DictReader` to read rows as dictionaries:

```python
import csv

with open('data.csv', 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        print(row['Name'], row['Age'])  # Access by column name
```

### Writing CSV Files

To write data to a CSV file:

```python
import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', '28', 'New York'],
    ['Bob', '35', 'San Francisco'],
    ['Charlie', '42', 'Chicago']
]

with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in data:
        csv_writer.writerow(row)
```

#### Writing with Headers

To write dictionaries to a CSV file:

```python
import csv

data = [
    {'Name': 'Alice', 'Age': '28', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '35', 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': '42', 'City': 'Chicago'}
]

with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'City']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    csv_writer.writeheader()  # Write the header row
    for row in data:
        csv_writer.writerow(row)
```

### CSV Dialects

To handle different CSV formats, you can specify a dialect:

```python
import csv

# Define a custom dialect
csv.register_dialect('semicolon', delimiter=';', quoting=csv.QUOTE_MINIMAL)

# Use the dialect when reading
with open('data.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, dialect='semicolon')
    for row in csv_reader:
        print(row)
```

Common dialect parameters include:
- `delimiter`: The character used to separate fields (default is ',')
- `quotechar`: The character used for quoting fields (default is '"')
- `quoting`: Controls when quotes are recognized (e.g., `csv.QUOTE_MINIMAL`, `csv.QUOTE_ALL`)
- `escapechar`: The character used to escape special characters
- `lineterminator`: The string used to terminate lines (default depends on the platform)

## Data Processing with CSV

### Converting Data Types

CSV files store all data as text, so you'll often need to convert values to appropriate types:

```python
import csv

with open('data.csv', 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        name = row['Name']
        age = int(row['Age'])  # Convert to integer
        print(f"{name} is {age} years old")
```

### Filtering and Transforming Data

You can filter and transform CSV data as you read it:

```python
import csv

with open('data.csv', 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    # Filter rows where age > 30
    filtered_data = [row for row in csv_reader if int(row['Age']) > 30]
    
    # Transform data
    transformed_data = [{
        'full_name': row['Name'],
        'age_in_months': int(row['Age']) * 12,
        'location': row['City']
    } for row in filtered_data]
    
    print(transformed_data)
```

### Aggregating Data

You can perform aggregations on CSV data:

```python
import csv
from collections import defaultdict

with open('sales.csv', 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    # Group sales by region
    sales_by_region = defaultdict(float)
    for row in csv_reader:
        region = row['Region']
        amount = float(row['Amount'])
        sales_by_region[region] += amount
    
    print(sales_by_region)
```

## Working with Large CSV Files

For large CSV files, reading the entire file into memory might not be feasible. Process the file row by row instead:

```python
import csv

def process_large_csv(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        # Process one row at a time
        for row in csv_reader:
            process_row(row)

def process_row(row):
    # Process a single row
    pass
```

## CSV with Pandas

For more advanced CSV processing, consider using the pandas library, which provides powerful data manipulation capabilities:

```python
import pandas as pd

# Read CSV into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows
print(df.head())

# Filter data
filtered_df = df[df['Age'] > 30]

# Group and aggregate
grouped = df.groupby('City')['Age'].mean()

# Write to CSV
filtered_df.to_csv('filtered_data.csv', index=False)
```

## Best Practices

1. **Always use the `newline=''` parameter** when opening CSV files to handle line endings correctly
2. **Use `csv.DictReader` and `csv.DictWriter`** for more readable code when working with headers
3. **Handle potential errors** like missing files, malformed CSV data, or type conversion issues
4. **Consider using pandas** for complex data manipulation tasks
5. **Be careful with large files** to avoid memory issues
6. **Always close files** by using the `with` statement
7. **Validate CSV data** before processing to catch issues early

## Common Pitfalls

1. **Forgetting to specify `newline=''`** can cause issues with line endings
2. **Not handling different CSV dialects** correctly
3. **Assuming all CSV files have headers**
4. **Not handling quoted fields** properly
5. **Memory issues with large files**
6. **Type conversion errors** when processing numeric or date fields

## Summary

In this lesson, you've learned:
- The basics of CSV file format
- How to read and write CSV files using Python's `csv` module
- Working with headers using `DictReader` and `DictWriter`
- Handling different CSV dialects
- Processing, filtering, and transforming CSV data
- Best practices for working with CSV files

In the next lesson, you'll learn about error handling in Python, which is essential for building robust file processing applications.

## Additional Resources

- [Python Documentation: CSV Module](https://docs.python.org/3/library/csv.html)
- [Pandas Documentation: CSV I/O](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [RFC 4180: Common Format and MIME Type for CSV Files](https://tools.ietf.org/html/rfc4180)