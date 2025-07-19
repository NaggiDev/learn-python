"""
File writing utilities.

This module provides safe and convenient functions for writing
various file formats with proper error handling and directory creation.
"""

import json
import csv
import os
import shutil
from pathlib import Path
from typing import List, Dict, Any, Union
from datetime import datetime

def write_text_file(filepath: str, content: str, encoding: str = 'utf-8') -> None:
    """
    Write content to a text file.
    
    Args:
        filepath (str): Path to the file
        content (str): Content to write
        encoding (str): File encoding (default: utf-8)
        
    Raises:
        IOError: If file cannot be written
        
    Example:
        >>> write_text_file("output.txt", "Hello, World!")
    """
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding=encoding) as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Error writing file {filepath}: {e}")

def write_json_file(filepath: str, data: Union[Dict, List], 
                   encoding: str = 'utf-8', indent: int = 2) -> None:
    """
    Write data to a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        data (Union[Dict, List]): Data to write
        encoding (str): File encoding (default: utf-8)
        indent (int): JSON indentation (default: 2)
        
    Raises:
        IOError: If file cannot be written
        TypeError: If data is not JSON serializable
        
    Example:
        >>> data = {"name": "John", "age": 30}
        >>> write_json_file("person.json", data)
    """
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=indent, ensure_ascii=False)
    except TypeError as e:
        raise TypeError(f"Data is not JSON serializable: {e}")
    except IOError as e:
        raise IOError(f"Error writing file {filepath}: {e}")

def write_csv_file(filepath: str, data: List[Dict[str, Any]], 
                  encoding: str = 'utf-8') -> None:
    """
    Write data to a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        data (List[Dict[str, Any]]): List of dictionaries to write
        encoding (str): File encoding (default: utf-8)
        
    Raises:
        IOError: If file cannot be written
        ValueError: If data is empty or inconsistent
        
    Example:
        >>> data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        >>> write_csv_file("people.csv", data)
    """
    if not data:
        raise ValueError("Cannot write empty data to CSV")
    
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        # Get fieldnames from first dictionary
        fieldnames = list(data[0].keys())
        
        with open(filepath, 'w', encoding=encoding, newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        raise IOError(f"Error writing file {filepath}: {e}")

def append_to_file(filepath: str, content: str, encoding: str = 'utf-8') -> None:
    """
    Append content to a file.
    
    Args:
        filepath (str): Path to the file
        content (str): Content to append
        encoding (str): File encoding (default: utf-8)
        
    Raises:
        IOError: If file cannot be written
        
    Example:
        >>> append_to_file("log.txt", "New log entry\\n")
    """
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'a', encoding=encoding) as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Error appending to file {filepath}: {e}")

def create_backup(filepath: str) -> str:
    """
    Create a backup copy of a file with timestamp.
    
    Args:
        filepath (str): Path to the file to backup
        
    Returns:
        str: Path to the backup file
        
    Raises:
        FileNotFoundError: If original file doesn't exist
        IOError: If backup cannot be created
        
    Example:
        >>> backup_path = create_backup("important.txt")
        >>> print(f"Backup created: {backup_path}")
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    try:
        # Create backup filename with timestamp
        path = Path(filepath)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{path.stem}_backup_{timestamp}{path.suffix}"
        backup_path = path.parent / backup_name
        
        # Copy the file
        shutil.copy2(filepath, backup_path)
        
        return str(backup_path)
    except IOError as e:
        raise IOError(f"Error creating backup of {filepath}: {e}")