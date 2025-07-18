# CSV Data Processor Mini-Project

## Overview

In this mini-project, you'll build a command-line CSV data processor that can perform various operations on CSV files. This project will combine all the concepts you've learned in this module: file I/O operations, CSV handling, and error handling.

## Learning Objectives

By completing this project, you will:
- Apply file I/O operations to read and write CSV files
- Process and transform CSV data
- Implement robust error handling
- Create a command-line interface for a Python application
- Practice working with different CSV formats and dialects

## Requirements

### Functionality

Your CSV Data Processor should be able to:

1. **Read CSV files** with different delimiters and formats
2. **Write processed data** to new CSV files
3. **Filter rows** based on column values
4. **Sort data** by specified columns
5. **Calculate statistics** (sum, average, min, max, count) on numeric columns
6. **Transform data** by applying operations to columns
7. **Merge multiple CSV files** based on a common column
8. **Handle errors gracefully** with informative error messages

### Command-Line Interface

The program should be run from the command line with the following syntax:

```
python csv_processor.py <command> [options]
```

Where `<command>` is one of:

- `info`: Display information about a CSV file (number of rows, columns, data types)
- `filter`: Filter rows based on a condition
- `sort`: Sort the CSV by one or more columns
- `stats`: Calculate statistics on numeric columns
- `transform`: Apply transformations to columns
- `merge`: Merge two or more CSV files

Each command should have appropriate options and arguments.

### Error Handling

The program should handle the following error conditions:

- File not found
- Permission errors
- Invalid CSV format
- Invalid command-line arguments
- Type conversion errors
- Memory constraints for large files

## Project Structure

```
mini_project/
├── README.md                 # Project description and instructions
├── csv_processor.py          # Main program file
├── test_csv_processor.py     # Tests for the CSV processor
├── sample_data/              # Sample CSV files for testing
│   ├── employees.csv         # Employee data
│   ├── sales.csv             # Sales data
│   └── products.csv          # Product data
└── expected_outputs/         # Expected output files for tests
    ├── filtered_employees.csv
    ├── sorted_sales.csv
    └── merged_data.csv
```

## Implementation Steps

1. Start by implementing the basic structure of the command-line interface
2. Add functionality to read and display information about CSV files
3. Implement filtering functionality
4. Add sorting capabilities
5. Implement statistical calculations
6. Add data transformation features
7. Implement file merging functionality
8. Add comprehensive error handling
9. Write tests to verify all functionality

## Sample Usage

Here are some examples of how the program should be used:

```bash
# Display information about a CSV file
python csv_processor.py info sample_data/employees.csv

# Filter employees with salary > 50000
python csv_processor.py filter sample_data/employees.csv --column salary --condition ">" --value 50000 --output filtered_employees.csv

# Sort sales by date and amount
python csv_processor.py sort sample_data/sales.csv --columns date,amount --output sorted_sales.csv

# Calculate statistics on the salary column
python csv_processor.py stats sample_data/employees.csv --column salary

# Transform the salary column by multiplying by 1.1 (10% raise)
python csv_processor.py transform sample_data/employees.csv --column salary --operation multiply --value 1.1 --output transformed_employees.csv

# Merge employees and sales data on employee_id
python csv_processor.py merge sample_data/employees.csv sample_data/sales.csv --on employee_id --output merged_data.csv
```

## Bonus Challenges

If you complete the basic requirements, try these bonus challenges:

1. Add support for different output formats (JSON, Excel, etc.)
2. Implement data visualization features (using matplotlib or another library)
3. Add support for regular expressions in filtering
4. Implement a simple query language for more complex operations
5. Add support for processing very large files that don't fit in memory

## Evaluation Criteria

Your solution will be evaluated based on:

1. Correctness: Does it work as specified?
2. Code quality: Is the code well-organized, readable, and maintainable?
3. Error handling: Does it handle errors gracefully?
4. Documentation: Is the code well-documented?
5. Testing: Are there comprehensive tests?

## Getting Started

1. Review the concepts from the module lessons
2. Examine the sample data files to understand their structure
3. Plan your approach before starting to code
4. Implement the basic functionality first, then add more features
5. Test your code thoroughly with different inputs

Good luck!