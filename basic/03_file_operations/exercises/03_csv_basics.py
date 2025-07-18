"""
Exercise: CSV Basics

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

This exercise covers:
- Reading CSV files
- Writing CSV files
- Processing CSV data
"""

import csv
import os


def read_csv_to_list(file_path):
    """
    Read a CSV file and return its contents as a list of lists.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: List of lists, where each inner list represents a row
    """
    # TODO: Implement this function
    pass


def read_csv_to_dict(file_path):
    """
    Read a CSV file with headers and return its contents as a list of dictionaries.
    Each dictionary represents a row with keys from the header.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: List of dictionaries, where each dictionary represents a row
    """
    # TODO: Implement this function
    pass


def write_list_to_csv(file_path, data, headers=None):
    """
    Write a list of lists to a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        data (list): List of lists to write
        headers (list, optional): List of headers to write as the first row
        
    Returns:
        int: Number of rows written
    """
    # TODO: Implement this function
    pass


def write_dict_to_csv(file_path, data):
    """
    Write a list of dictionaries to a CSV file.
    The keys of the first dictionary will be used as headers.
    
    Args:
        file_path (str): Path to the CSV file
        data (list): List of dictionaries to write
        
    Returns:
        int: Number of rows written
    """
    # TODO: Implement this function
    pass


def filter_csv_rows(input_path, output_path, filter_func):
    """
    Read a CSV file, filter rows based on the filter_func, and write the result to a new CSV file.
    
    Args:
        input_path (str): Path to the input CSV file
        output_path (str): Path to the output CSV file
        filter_func (function): Function that takes a row (as dict) and returns True if the row should be included
        
    Returns:
        int: Number of rows written to the output file
    """
    # TODO: Implement this function
    pass


def transform_csv_data(input_path, output_path, transform_func):
    """
    Read a CSV file, transform each row using transform_func, and write the result to a new CSV file.
    
    Args:
        input_path (str): Path to the input CSV file
        output_path (str): Path to the output CSV file
        transform_func (function): Function that takes a row (as dict) and returns a transformed row (as dict)
        
    Returns:
        int: Number of rows written to the output file
    """
    # TODO: Implement this function
    pass


# Test functions
def test_csv_operations():
    # Create test data
    test_data = [
        ['Name', 'Age', 'City'],
        ['Alice', '28', 'New York'],
        ['Bob', '35', 'San Francisco'],
        ['Charlie', '42', 'Chicago'],
        ['Diana', '31', 'Boston']
    ]
    
    # Test file paths
    test_csv = "test_data.csv"
    output_csv = "output_data.csv"
    filtered_csv = "filtered_data.csv"
    transformed_csv = "transformed_data.csv"
    
    # Create a test CSV file
    with open(test_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(test_data)
    
    # Test read_csv_to_list
    data_list = read_csv_to_list(test_csv)
    assert len(data_list) == 5, f"Expected 5 rows, got {len(data_list)}"
    assert data_list[0] == ['Name', 'Age', 'City'], f"Expected header row ['Name', 'Age', 'City'], got {data_list[0]}"
    assert data_list[1] == ['Alice', '28', 'New York'], f"Expected ['Alice', '28', 'New York'], got {data_list[1]}"
    
    # Test read_csv_to_dict
    data_dict = read_csv_to_dict(test_csv)
    assert len(data_dict) == 4, f"Expected 4 rows (excluding header), got {len(data_dict)}"
    assert data_dict[0]['Name'] == 'Alice', f"Expected Name 'Alice', got {data_dict[0]['Name']}"
    assert data_dict[0]['Age'] == '28', f"Expected Age '28', got {data_dict[0]['Age']}"
    assert data_dict[0]['City'] == 'New York', f"Expected City 'New York', got {data_dict[0]['City']}"
    
    # Test write_list_to_csv
    new_data = [
        ['Eve', '25', 'Miami'],
        ['Frank', '39', 'Seattle']
    ]
    rows_written = write_list_to_csv(output_csv, new_data, headers=['Name', 'Age', 'City'])
    assert rows_written == 3, f"Expected 3 rows written (including header), got {rows_written}"
    
    # Verify write_list_to_csv
    with open(output_csv, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert len(rows) == 3, f"Expected 3 rows in output file, got {len(rows)}"
        assert rows[0] == ['Name', 'Age', 'City'], f"Expected header row ['Name', 'Age', 'City'], got {rows[0]}"
        assert rows[1] == ['Eve', '25', 'Miami'], f"Expected ['Eve', '25', 'Miami'], got {rows[1]}"
    
    # Test write_dict_to_csv
    dict_data = [
        {'Name': 'Grace', 'Age': '45', 'City': 'Dallas'},
        {'Name': 'Henry', 'Age': '52', 'City': 'Phoenix'}
    ]
    rows_written = write_dict_to_csv(output_csv, dict_data)
    assert rows_written == 3, f"Expected 3 rows written (including header), got {rows_written}"
    
    # Test filter_csv_rows
    def filter_age_over_30(row):
        return int(row['Age']) > 30
    
    rows_filtered = filter_csv_rows(test_csv, filtered_csv, filter_age_over_30)
    assert rows_filtered == 3, f"Expected 3 rows written (including header), got {rows_filtered}"
    
    # Verify filter_csv_rows
    filtered_data = read_csv_to_dict(filtered_csv)
    assert len(filtered_data) == 2, f"Expected 2 rows after filtering, got {len(filtered_data)}"
    assert all(int(row['Age']) > 30 for row in filtered_data), "Filtering failed"
    
    # Test transform_csv_data
    def transform_row(row):
        return {
            'FullName': row['Name'],
            'AgeInMonths': str(int(row['Age']) * 12),
            'Location': row['City']
        }
    
    rows_transformed = transform_csv_data(test_csv, transformed_csv, transform_row)
    assert rows_transformed == 5, f"Expected 5 rows written (including header), got {rows_transformed}"
    
    # Verify transform_csv_data
    transformed_data = read_csv_to_dict(transformed_csv)
    assert len(transformed_data) == 4, f"Expected 4 rows after transformation, got {len(transformed_data)}"
    assert 'FullName' in transformed_data[0], "Transformation failed: 'FullName' key not found"
    assert transformed_data[0]['AgeInMonths'] == '336', f"Expected AgeInMonths '336', got {transformed_data[0]['AgeInMonths']}"
    
    # Clean up
    for file in [test_csv, output_csv, filtered_csv, transformed_csv]:
        if os.path.exists(file):
            os.remove(file)
    
    print("All tests passed!")


if __name__ == "__main__":
    test_csv_operations()