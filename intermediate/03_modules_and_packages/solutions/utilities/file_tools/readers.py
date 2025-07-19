"""
File reading utilities.

This module provides safe and convenient functions for reading
various file formats with proper error handling.
"""

import json
import csv
import os
from typing import List, Dict, Any, Union

def read_text_file(filepath: str, encoding: str = 'utf-8') -> str:
    """
    Read a text file and return its contents.
    
    Args:
        filepath (str): Path to the file
        encoding (str): File encoding (default: utf-8)
        
    Returns:
        str: File contents
        
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file cannot be read
        
    Example:
        >>> content = read_text_file("example.txt")
        >>> print(len(content))
    """
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading file {filepath}: {e}")

def read_json_file(filepath: str, encoding: str = 'utf-8') -> Union[Dict, List]:
    """
    Read a JSON file and return parsed data.
    
    Args:
        filepath (str): Path to the JSON file
        encoding (str): File encoding (default: utf-8)
        
    Returns:
        Union[Dict, List]: Parsed JSON data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
        IOError: If file cannot be read
        
    Example:
        >>> data = read_json_file("config.json")
        >>> print(data["version"])
    """
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file {filepath}: {e}")
    except IOError as e:
        raise IOError(f"Error reading file {filepath}: {e}")

def read_csv_file(filepath: str, encoding: str = 'utf-8', 
                  has_header: bool = True) -> List[Dict[str, str]]:
    """
    Read a CSV file and return data as list of dictionaries.
    
    Args:
        filepath (str): Path to the CSV file
        encoding (str): File encoding (default: utf-8)
        has_header (bool): Whether the first row contains headers
        
    Returns:
        List[Dict[str, str]]: List of dictionaries representing rows
        
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file cannot be read
        
    Example:
        >>> data = read_csv_file("data.csv")
        >>> print(data[0]["name"])
    """
    try:
        with open(filepath, 'r', encoding=encoding, newline='') as file:
            if has_header:
                reader = csv.DictReader(file)
                return list(reader)
            else:
                reader = csv.reader(file)
                rows = list(reader)
                # Create generic column names
                if rows:
                    headers = [f"col_{i}" for i in range(len(rows[0]))]
                    return [dict(zip(headers, row)) for row in rows]
                return []
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading file {filepath}: {e}")

def count_lines(filepath: str, encoding: str = 'utf-8') -> int:
    """
    Count the number of lines in a file.
    
    Args:
        filepath (str): Path to the file
        encoding (str): File encoding (default: utf-8)
        
    Returns:
        int: Number of lines in the file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file cannot be read
        
    Example:
        >>> line_count = count_lines("data.txt")
        >>> print(f"File has {line_count} lines")
    """
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading file {filepath}: {e}")

def get_file_size(filepath: str) -> int:
    """
    Get the size of a file in bytes.
    
    Args:
        filepath (str): Path to the file
        
    Returns:
        int: File size in bytes
        
    Raises:
        FileNotFoundError: If file doesn't exist
        
    Example:
        >>> size = get_file_size("document.pdf")
        >>> print(f"File size: {size} bytes")
    """
    try:
        return os.path.getsize(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except OSError as e:
        raise OSError(f"Error getting file size for {filepath}: {e}")