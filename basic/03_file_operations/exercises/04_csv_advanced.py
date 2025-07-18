"""
Exercise: Advanced CSV Operations

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

This exercise covers:
- Working with different CSV dialects
- Handling CSV files with different formats
- Aggregating and analyzing CSV data
"""

import csv
import os
from collections import defaultdict


def read_csv_with_dialect(file_path, delimiter=',', quotechar='"'):
    """
    Read a CSV file using a specific dialect.
    
    Args:
        file_path (str): Path to the CSV file
        delimiter (str): Character used to separate fields
        quotechar (str): Character used for quoting fields
        
    Returns:
        list: List of dictionaries representing the CSV data
    """
    # TODO: Implement this function
    pass


def detect_csv_dialect(file_path):
    """
    Detect the dialect of a CSV file and return its properties.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        dict: Dictionary with detected dialect properties:
            - 'delimiter': The detected delimiter
            - 'quotechar': The detected quote character
            - 'has_header': Boolean indicating if the file has a header row
    """
    # TODO: Implement this function
    pass


def aggregate_csv_data(file_path, group_by_column, aggregate_column, aggregate_func='sum'):
    """
    Group CSV data by a column and aggregate another column.
    
    Args:
        file_path (str): Path to the CSV file
        group_by_column (str): Column name to group by
        aggregate_column (str): Column name to aggregate
        aggregate_func (str): Aggregation function ('sum', 'avg', 'min', 'max', 'count')
        
    Returns:
        dict: Dictionary with group values as keys and aggregated values as values
    """
    # TODO: Implement this function
    pass


def merge_csv_files(file_paths, output_path, merge_on_column=None):
    """
    Merge multiple CSV files into a single file.
    If merge_on_column is provided, perform an inner join on that column.
    Otherwise, concatenate the files (assuming they have the same structure).
    
    Args:
        file_paths (list): List of paths to the CSV files
        output_path (str): Path to the output CSV file
        merge_on_column (str, optional): Column name to join on
        
    Returns:
        int: Number of rows in the merged file
    """
    # TODO: Implement this function
    pass


def pivot_csv_data(file_path, index_column, column_column, value_column):
    """
    Create a pivot table from CSV data.
    
    Args:
        file_path (str): Path to the CSV file
        index_column (str): Column to use as index
        column_column (str): Column to use as columns
        value_column (str): Column to use as values
        
    Returns:
        dict: Nested dictionary representing the pivot table
    """
    # TODO: Implement this function
    pass


# Test functions
def test_advanced_csv_operations():
    # Create test data with comma delimiter
    comma_data = [
        ['Name', 'Age', 'City'],
        ['Alice', '28', 'New York'],
        ['Bob', '35', 'San Francisco'],
        ['Charlie', '42', 'Chicago'],
        ['Diana', '31', 'Boston']
    ]
    
    # Create test data with semicolon delimiter
    semicolon_data = [
        ['Name', 'Department', 'Salary'],
        ['Alice', 'HR', '60000'],
        ['Bob', 'Engineering', '85000'],
        ['Charlie', 'Marketing', '55000'],
        ['Diana', 'Engineering', '78000']
    ]
    
    # Create test data for merging
    merge_data1 = [
        ['ID', 'Name', 'Department'],
        ['1', 'Alice', 'HR'],
        ['2', 'Bob', 'Engineering'],
        ['3', 'Charlie', 'Marketing'],
        ['4', 'Diana', 'Engineering']
    ]
    
    merge_data2 = [
        ['ID', 'Salary', 'Start Date'],
        ['1', '60000', '2020-01-15'],
        ['2', '85000', '2019-05-20'],
        ['3', '55000', '2021-03-10'],
        ['5', '72000', '2020-11-05']  # Note: ID 5 is not in merge_data1, ID 4 is missing
    ]
    
    # Create test data for pivot
    pivot_data = [
        ['Date', 'Product', 'Sales'],
        ['2023-01-01', 'ProductA', '100'],
        ['2023-01-01', 'ProductB', '150'],
        ['2023-01-02', 'ProductA', '120'],
        ['2023-01-02', 'ProductB', '130'],
        ['2023-01-03', 'ProductA', '90'],
        ['2023-01-03', 'ProductB', '160']
    ]
    
    # Test file paths
    comma_csv = "comma_data.csv"
    semicolon_csv = "semicolon_data.csv"
    merge_csv1 = "merge_data1.csv"
    merge_csv2 = "merge_data2.csv"
    merged_csv = "merged_data.csv"
    pivot_csv = "pivot_data.csv"
    
    # Create test CSV files
    with open(comma_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(comma_data)
    
    with open(semicolon_csv, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(semicolon_data)
    
    with open(merge_csv1, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(merge_data1)
    
    with open(merge_csv2, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(merge_data2)
    
    with open(pivot_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(pivot_data)
    
    # Test read_csv_with_dialect
    comma_result = read_csv_with_dialect(comma_csv)
    assert len(comma_result) == 4, f"Expected 4 rows, got {len(comma_result)}"
    assert comma_result[0]['Name'] == 'Alice', f"Expected Name 'Alice', got {comma_result[0]['Name']}"
    
    semicolon_result = read_csv_with_dialect(semicolon_csv, delimiter=';')
    assert len(semicolon_result) == 4, f"Expected 4 rows, got {len(semicolon_result)}"
    assert semicolon_result[0]['Name'] == 'Alice', f"Expected Name 'Alice', got {semicolon_result[0]['Name']}"
    assert semicolon_result[0]['Salary'] == '60000', f"Expected Salary '60000', got {semicolon_result[0]['Salary']}"
    
    # Test detect_csv_dialect
    comma_dialect = detect_csv_dialect(comma_csv)
    assert comma_dialect['delimiter'] == ',', f"Expected delimiter ',', got {comma_dialect['delimiter']}"
    assert comma_dialect['has_header'] == True, f"Expected has_header True, got {comma_dialect['has_header']}"
    
    semicolon_dialect = detect_csv_dialect(semicolon_csv)
    assert semicolon_dialect['delimiter'] == ';', f"Expected delimiter ';', got {semicolon_dialect['delimiter']}"
    
    # Test aggregate_csv_data
    city_count = aggregate_csv_data(comma_csv, 'City', 'Name', 'count')
    assert len(city_count) == 4, f"Expected 4 cities, got {len(city_count)}"
    assert city_count['New York'] == 1, f"Expected 1 person in New York, got {city_count['New York']}"
    
    dept_avg_salary = aggregate_csv_data(semicolon_csv, 'Department', 'Salary', 'avg')
    assert len(dept_avg_salary) == 3, f"Expected 3 departments, got {len(dept_avg_salary)}"
    assert dept_avg_salary['Engineering'] == 81500, f"Expected avg salary 81500 for Engineering, got {dept_avg_salary['Engineering']}"
    
    # Test merge_csv_files
    # Test concatenation
    concat_rows = merge_csv_files([comma_csv, semicolon_csv], merged_csv)
    assert concat_rows > 8, f"Expected more than 8 rows, got {concat_rows}"
    
    # Test join
    join_rows = merge_csv_files([merge_csv1, merge_csv2], merged_csv, merge_on_column='ID')
    assert join_rows == 4, f"Expected 4 rows (3 data + 1 header), got {join_rows}"
    
    # Verify join
    with open(merged_csv, 'r', newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 3, f"Expected 3 data rows after join, got {len(rows)}"
        assert 'Salary' in rows[0], "Join failed: 'Salary' column not found"
        assert 'Department' in rows[0], "Join failed: 'Department' column not found"
    
    # Test pivot_csv_data
    pivot_result = pivot_csv_data(pivot_csv, 'Date', 'Product', 'Sales')
    assert len(pivot_result) == 3, f"Expected 3 dates in pivot, got {len(pivot_result)}"
    assert 'ProductA' in pivot_result['2023-01-01'], "Pivot failed: 'ProductA' not found for date 2023-01-01"
    assert pivot_result['2023-01-01']['ProductA'] == '100', f"Expected sales 100, got {pivot_result['2023-01-01']['ProductA']}"
    assert pivot_result['2023-01-02']['ProductB'] == '130', f"Expected sales 130, got {pivot_result['2023-01-02']['ProductB']}"
    
    # Clean up
    for file in [comma_csv, semicolon_csv, merge_csv1, merge_csv2, merged_csv, pivot_csv]:
        if os.path.exists(file):
            os.remove(file)
    
    print("All tests passed!")


if __name__ == "__main__":
    test_advanced_csv_operations()