#!/usr/bin/env python3
"""
CSV Data Processor

A command-line tool for processing CSV files.
"""

import argparse
import csv
import os
import sys
from collections import defaultdict


class CSVProcessor:
    """
    A class for processing CSV files.
    """
    
    def __init__(self):
        """Initialize the CSV processor."""
        self.delimiter = ','
        self.quotechar = '"'
    
    def detect_dialect(self, file_path):
        """
        Detect the dialect of a CSV file.
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            dict: Dictionary with detected dialect properties
        """
        try:
            with open(file_path, 'r', newline='') as file:
                sample = file.read(4096)
                
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(sample)
                has_header = sniffer.has_header(sample)
                
                self.delimiter = dialect.delimiter
                self.quotechar = dialect.quotechar
                
                return {
                    'delimiter': dialect.delimiter,
                    'quotechar': dialect.quotechar,
                    'has_header': has_header
                }
        except Exception as e:
            print(f"Error detecting CSV dialect: {e}", file=sys.stderr)
            return {
                'delimiter': ',',
                'quotechar': '"',
                'has_header': True
            }    
    d
ef read_csv(self, file_path):
        """
        Read a CSV file into a list of dictionaries.
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            tuple: (list of dictionaries, list of column names)
        """
        try:
            # Detect dialect
            self.detect_dialect(file_path)
            
            with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file, delimiter=self.delimiter, quotechar=self.quotechar)
                data = list(reader)
                columns = reader.fieldnames
                
                return data, columns
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.", file=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied when accessing '{file_path}'.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error reading CSV file: {e}", file=sys.stderr)
            sys.exit(1)
    
    def write_csv(self, data, columns, output_path):
        """
        Write data to a CSV file.
        
        Args:
            data (list): List of dictionaries to write
            columns (list): List of column names
            output_path (str): Path to the output file
        """
        try:
            with open(output_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=columns, delimiter=self.delimiter, quotechar=self.quotechar)
                writer.writeheader()
                writer.writerows(data)
                
            print(f"Data written to '{output_path}'")
        except PermissionError:
            print(f"Error: Permission denied when writing to '{output_path}'.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error writing CSV file: {e}", file=sys.stderr)
            sys.exit(1)    
   
 def get_file_info(self, file_path):
        """
        Get information about a CSV file.
        
        Args:
            file_path (str): Path to the CSV file
        """
        try:
            # Detect dialect
            dialect = self.detect_dialect(file_path)
            
            # Read data
            data, columns = self.read_csv(file_path)
            
            # Get file size
            file_size = os.path.getsize(file_path)
            
            # Determine column types
            column_types = {}
            for column in columns:
                types = set()
                for row in data:
                    value = row[column]
                    # Try to determine the type
                    if value.strip() == '':
                        types.add('empty')
                    elif value.lower() in ('true', 'false'):
                        types.add('boolean')
                    else:
                        try:
                            int(value)
                            types.add('integer')
                        except ValueError:
                            try:
                                float(value)
                                types.add('float')
                            except ValueError:
                                types.add('string')
                
                # Determine the most specific type
                if 'string' in types:
                    column_types[column] = 'string'
                elif 'float' in types:
                    column_types[column] = 'float'
                elif 'integer' in types:
                    column_types[column] = 'integer'
                elif 'boolean' in types:
                    column_types[column] = 'boolean'
                else:
                    column_types[column] = 'empty'
            
            # Print information
            print(f"File: {file_path}")
            print(f"Size: {file_size} bytes")
            print(f"Delimiter: '{dialect['delimiter']}'")
            print(f"Quote character: '{dialect['quotechar']}'")
            print(f"Has header: {dialect['has_header']}")
            print(f"Number of rows: {len(data)}")
            print(f"Number of columns: {len(columns)}")
            print("\nColumns:")
            for column in columns:
                print(f"  {column} ({column_types[column]})")
            
        except Exception as e:
            print(f"Error getting file info: {e}", file=sys.stderr)
            sys.exit(1)    
   
 def filter_data(self, file_path, column, condition, value, output_path):
        """
        Filter rows based on a condition.
        
        Args:
            file_path (str): Path to the CSV file
            column (str): Column to filter on
            condition (str): Condition to apply (=, !=, >, <, >=, <=)
            value (str): Value to compare against
            output_path (str): Path to the output file
        """
        try:
            # Read data
            data, columns = self.read_csv(file_path)
            
            # Check if column exists
            if column not in columns:
                print(f"Error: Column '{column}' not found in the CSV file.", file=sys.stderr)
                sys.exit(1)
            
            # Convert value to appropriate type
            try:
                numeric_value = float(value)
                is_numeric = True
            except ValueError:
                numeric_value = None
                is_numeric = False
            
            # Filter data
            filtered_data = []
            for row in data:
                row_value = row[column]
                
                # Convert row value to appropriate type for comparison
                if is_numeric:
                    try:
                        row_numeric = float(row_value)
                    except ValueError:
                        # Skip rows where numeric comparison is not possible
                        continue
                    
                    # Apply numeric condition
                    if condition == '=' and row_numeric == numeric_value:
                        filtered_data.append(row)
                    elif condition == '!=' and row_numeric != numeric_value:
                        filtered_data.append(row)
                    elif condition == '>' and row_numeric > numeric_value:
                        filtered_data.append(row)
                    elif condition == '<' and row_numeric < numeric_value:
                        filtered_data.append(row)
                    elif condition == '>=' and row_numeric >= numeric_value:
                        filtered_data.append(row)
                    elif condition == '<=' and row_numeric <= numeric_value:
                        filtered_data.append(row)
                else:
                    # Apply string condition
                    if condition == '=' and row_value == value:
                        filtered_data.append(row)
                    elif condition == '!=' and row_value != value:
                        filtered_data.append(row)
                    elif condition == 'contains' and value in row_value:
                        filtered_data.append(row)
                    elif condition == 'startswith' and row_value.startswith(value):
                        filtered_data.append(row)
                    elif condition == 'endswith' and row_value.endswith(value):
                        filtered_data.append(row)
            
            # Write filtered data
            self.write_csv(filtered_data, columns, output_path)
            print(f"Filtered {len(filtered_data)} rows out of {len(data)}")
            
        except Exception as e:
            print(f"Error filtering data: {e}", file=sys.stderr)
            sys.exit(1) 
   
    def sort_data(self, file_path, columns, output_path, reverse=False):
        """
        Sort data by specified columns.
        
        Args:
            file_path (str): Path to the CSV file
            columns (list): List of columns to sort by
            output_path (str): Path to the output file
            reverse (bool): Whether to sort in reverse order
        """
        try:
            # Read data
            data, all_columns = self.read_csv(file_path)
            
            # Check if all sort columns exist
            for column in columns:
                if column not in all_columns:
                    print(f"Error: Column '{column}' not found in the CSV file.", file=sys.stderr)
                    sys.exit(1)
            
            # Determine if columns are numeric
            numeric_columns = set()
            for column in columns:
                is_numeric = True
                for row in data:
                    try:
                        float(row[column])
                    except ValueError:
                        is_numeric = False
                        break
                
                if is_numeric:
                    numeric_columns.add(column)
            
            # Sort data
            for column in reversed(columns):
                if column in numeric_columns:
                    data.sort(key=lambda x: float(x[column]), reverse=reverse)
                else:
                    data.sort(key=lambda x: x[column], reverse=reverse)
            
            # Write sorted data
            self.write_csv(data, all_columns, output_path)
            print(f"Sorted {len(data)} rows by {', '.join(columns)}")
            
        except Exception as e:
            print(f"Error sorting data: {e}", file=sys.stderr)
            sys.exit(1)    
 
   def calculate_stats(self, file_path, column):
        """
        Calculate statistics on a numeric column.
        
        Args:
            file_path (str): Path to the CSV file
            column (str): Column to calculate statistics on
        """
        try:
            # Read data
            data, columns = self.read_csv(file_path)
            
            # Check if column exists
            if column not in columns:
                print(f"Error: Column '{column}' not found in the CSV file.", file=sys.stderr)
                sys.exit(1)
            
            # Extract numeric values
            values = []
            for row in data:
                try:
                    value = float(row[column])
                    values.append(value)
                except ValueError:
                    # Skip non-numeric values
                    continue
            
            if not values:
                print(f"No numeric values found in column '{column}'")
                return
            
            # Calculate statistics
            count = len(values)
            total = sum(values)
            minimum = min(values)
            maximum = max(values)
            average = total / count
            
            # Print statistics
            print(f"Statistics for column '{column}':")
            print(f"  Count: {count}")
            print(f"  Sum: {total}")
            print(f"  Minimum: {minimum}")
            print(f"  Maximum: {maximum}")
            print(f"  Average: {average}")
            
        except Exception as e:
            print(f"Error calculating statistics: {e}", file=sys.stderr)
            sys.exit(1)    

    def transform_data(self, file_path, column, operation, value, output_path):
        """
        Transform data by applying an operation to a column.
        
        Args:
            file_path (str): Path to the CSV file
            column (str): Column to transform
            operation (str): Operation to apply (add, subtract, multiply, divide, replace)
            value (str): Value to use in the operation
            output_path (str): Path to the output file
        """
        try:
            # Read data
            data, columns = self.read_csv(file_path)
            
            # Check if column exists
            if column not in columns:
                print(f"Error: Column '{column}' not found in the CSV file.", file=sys.stderr)
                sys.exit(1)
            
            # Convert value to appropriate type for numeric operations
            numeric_value = None
            if operation in ('add', 'subtract', 'multiply', 'divide'):
                try:
                    numeric_value = float(value)
                except ValueError:
                    print(f"Error: Value '{value}' is not a valid number for operation '{operation}'.", file=sys.stderr)
                    sys.exit(1)
            
            # Transform data
            for row in data:
                if operation in ('add', 'subtract', 'multiply', 'divide'):
                    try:
                        row_value = float(row[column])
                        
                        if operation == 'add':
                            result = row_value + numeric_value
                        elif operation == 'subtract':
                            result = row_value - numeric_value
                        elif operation == 'multiply':
                            result = row_value * numeric_value
                        elif operation == 'divide':
                            if numeric_value == 0:
                                print(f"Warning: Division by zero in row. Skipping transformation.")
                                continue
                            result = row_value / numeric_value
                        
                        # Convert back to string with appropriate formatting
                        if result.is_integer():
                            row[column] = str(int(result))
                        else:
                            row[column] = str(result)
                            
                    except ValueError:
                        # Skip non-numeric values
                        continue
                elif operation == 'replace':
                    old_value = row[column]
                    new_value = value
                    row[column] = old_value.replace(old_value, new_value)
                elif operation == 'uppercase':
                    row[column] = row[column].upper()
                elif operation == 'lowercase':
                    row[column] = row[column].lower()
                elif operation == 'trim':
                    row[column] = row[column].strip()
            
            # Write transformed data
            self.write_csv(data, columns, output_path)
            print(f"Transformed column '{column}' in {len(data)} rows")
            
        except Exception as e:
            print(f"Error transforming data: {e}", file=sys.stderr)
            sys.exit(1)    
    
def merge_files(self, file_paths, on_column, output_path):
        """
        Merge multiple CSV files based on a common column.
        
        Args:
            file_paths (list): List of paths to the CSV files
            on_column (str): Column to join on
            output_path (str): Path to the output file
        """
        try:
            if len(file_paths) < 2:
                print("Error: At least two files are required for merging.", file=sys.stderr)
                sys.exit(1)
            
            # Read the first file
            primary_data, primary_columns = self.read_csv(file_paths[0])
            
            # Check if join column exists in the first file
            if on_column not in primary_columns:
                print(f"Error: Column '{on_column}' not found in file '{file_paths[0]}'.", file=sys.stderr)
                sys.exit(1)
            
            # Create a dictionary to store merged data
            merged_data = {}
            for row in primary_data:
                key = row[on_column]
                merged_data[key] = {k: v for k, v in row.items()}
            
            # Process subsequent files
            all_columns = set(primary_columns)
            
            for file_path in file_paths[1:]:
                secondary_data, secondary_columns = self.read_csv(file_path)
                
                # Check if join column exists in this file
                if on_column not in secondary_columns:
                    print(f"Error: Column '{on_column}' not found in file '{file_path}'.", file=sys.stderr)
                    sys.exit(1)
                
                # Update all_columns
                all_columns.update(secondary_columns)
                
                # Create a dictionary for faster lookups
                secondary_dict = {}
                for row in secondary_data:
                    key = row[on_column]
                    if key not in secondary_dict:
                        secondary_dict[key] = []
                    secondary_dict[key].append(row)
                
                # Merge data
                new_merged_data = {}
                for key, primary_row in merged_data.items():
                    if key in secondary_dict:
                        for secondary_row in secondary_dict[key]:
                            # Create a new merged row
                            merged_row = {k: v for k, v in primary_row.items()}
                            
                            # Add columns from secondary row
                            for k, v in secondary_row.items():
                                if k != on_column:  # Don't duplicate the join column
                                    merged_row[k] = v
                            
                            # Add to new merged data
                            if key not in new_merged_data:
                                new_merged_data[key] = []
                            new_merged_data[key].append(merged_row)
                
                # Replace merged_data with the new merged data
                merged_data = {}
                for key, rows in new_merged_data.items():
                    for i, row in enumerate(rows):
                        merged_data[f"{key}_{i}"] = row
            
            # Convert merged data to a list
            merged_list = list(merged_data.values())
            
            # Ensure all columns are present in all rows
            for row in merged_list:
                for column in all_columns:
                    if column not in row:
                        row[column] = ""
            
            # Sort columns to ensure consistent order
            sorted_columns = sorted(all_columns)
            
            # Move the join column to the front
            if on_column in sorted_columns:
                sorted_columns.remove(on_column)
                sorted_columns.insert(0, on_column)
            
            # Write merged data
            self.write_csv(merged_list, sorted_columns, output_path)
            print(f"Merged {len(merged_list)} rows from {len(file_paths)} files")
            
        except Exception as e:
            print(f"Error merging files: {e}", file=sys.stderr)
            sys.exit(1)

def 
main():
    """Main function to parse arguments and execute commands."""
    parser = argparse.ArgumentParser(description='CSV Data Processor')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Display information about a CSV file')
    info_parser.add_argument('file', help='Path to the CSV file')
    
    # Filter command
    filter_parser = subparsers.add_parser('filter', help='Filter rows based on a condition')
    filter_parser.add_argument('file', help='Path to the CSV file')
    filter_parser.add_argument('--column', required=True, help='Column to filter on')
    filter_parser.add_argument('--condition', required=True, choices=['=', '!=', '>', '<', '>=', '<=', 'contains', 'startswith', 'endswith'], help='Condition to apply')
    filter_parser.add_argument('--value', required=True, help='Value to compare against')
    filter_parser.add_argument('--output', required=True, help='Path to the output file')
    
    # Sort command
    sort_parser = subparsers.add_parser('sort', help='Sort the CSV by one or more columns')
    sort_parser.add_argument('file', help='Path to the CSV file')
    sort_parser.add_argument('--columns', required=True, help='Comma-separated list of columns to sort by')
    sort_parser.add_argument('--reverse', action='store_true', help='Sort in reverse order')
    sort_parser.add_argument('--output', required=True, help='Path to the output file')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Calculate statistics on numeric columns')
    stats_parser.add_argument('file', help='Path to the CSV file')
    stats_parser.add_argument('--column', required=True, help='Column to calculate statistics on')
    
    # Transform command
    transform_parser = subparsers.add_parser('transform', help='Apply transformations to columns')
    transform_parser.add_argument('file', help='Path to the CSV file')
    transform_parser.add_argument('--column', required=True, help='Column to transform')
    transform_parser.add_argument('--operation', required=True, choices=['add', 'subtract', 'multiply', 'divide', 'replace', 'uppercase', 'lowercase', 'trim'], help='Operation to apply')
    transform_parser.add_argument('--value', help='Value to use in the operation (required for add, subtract, multiply, divide, replace)')
    transform_parser.add_argument('--output', required=True, help='Path to the output file')
    
    # Merge command
    merge_parser = subparsers.add_parser('merge', help='Merge two or more CSV files')
    merge_parser.add_argument('files', nargs='+', help='Paths to the CSV files to merge')
    merge_parser.add_argument('--on', required=True, help='Column to join on')
    merge_parser.add_argument('--output', required=True, help='Path to the output file')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create CSV processor
    processor = CSVProcessor()
    
    # Execute command
    if args.command == 'info':
        processor.get_file_info(args.file)
    elif args.command == 'filter':
        processor.filter_data(args.file, args.column, args.condition, args.value, args.output)
    elif args.command == 'sort':
        columns = [c.strip() for c in args.columns.split(',')]
        processor.sort_data(args.file, columns, args.output, args.reverse)
    elif args.command == 'stats':
        processor.calculate_stats(args.file, args.column)
    elif args.command == 'transform':
        if args.operation in ('add', 'subtract', 'multiply', 'divide', 'replace') and args.value is None:
            print(f"Error: --value is required for operation '{args.operation}'.", file=sys.stderr)
            sys.exit(1)
        processor.transform_data(args.file, args.column, args.operation, args.value, args.output)
    elif args.command == 'merge':
        processor.merge_files(args.files, args.on, args.output)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()