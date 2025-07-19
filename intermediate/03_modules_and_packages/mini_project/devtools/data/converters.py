"""Data conversion utilities."""

import json
import csv
from typing import Any, Dict, List, Union
from io import StringIO
from ..exceptions import ProcessingError

def convert_to_json(data: Any, indent: int = 2) -> str:
    """
    Convert data to JSON string.
    
    Args:
        data: Data to convert
        indent (int): JSON indentation
        
    Returns:
        str: JSON string
        
    Example:
        >>> convert_to_json({"name": "John", "age": 30})
        '{\\n  "name": "John",\\n  "age": 30\\n}'
    """
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except (TypeError, ValueError) as e:
        raise ProcessingError(f"Cannot convert to JSON: {e}")

def convert_from_json(json_str: str) -> Any:
    """
    Convert JSON string to Python object.
    
    Args:
        json_str (str): JSON string
        
    Returns:
        Any: Parsed Python object
        
    Example:
        >>> convert_from_json('{"name": "John", "age": 30}')
        {'name': 'John', 'age': 30}
    """
    if not isinstance(json_str, str):
        raise ProcessingError("Input must be a string")
    
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, ValueError) as e:
        raise ProcessingError(f"Invalid JSON: {e}")

def dict_to_csv(data: List[Dict[str, Any]], delimiter: str = ",") -> str:
    """
    Convert list of dictionaries to CSV string.
    
    Args:
        data (List[Dict]): List of dictionaries
        delimiter (str): CSV delimiter
        
    Returns:
        str: CSV string
        
    Example:
        >>> data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        >>> csv_str = dict_to_csv(data)
        >>> "name,age" in csv_str
        True
    """
    if not isinstance(data, list) or not data:
        raise ProcessingError("Data must be a non-empty list")
    
    if not all(isinstance(item, dict) for item in data):
        raise ProcessingError("All items must be dictionaries")
    
    output = StringIO()
    fieldnames = list(data[0].keys())
    
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()
    writer.writerows(data)
    
    return output.getvalue()

def csv_to_dict(csv_str: str, delimiter: str = ",") -> List[Dict[str, str]]:
    """
    Convert CSV string to list of dictionaries.
    
    Args:
        csv_str (str): CSV string
        delimiter (str): CSV delimiter
        
    Returns:
        List[Dict[str, str]]: List of dictionaries
        
    Example:
        >>> csv_str = "name,age\\nJohn,30\\nJane,25"
        >>> result = csv_to_dict(csv_str)
        >>> len(result)
        2
    """
    if not isinstance(csv_str, str):
        raise ProcessingError("Input must be a string")
    
    input_stream = StringIO(csv_str)
    reader = csv.DictReader(input_stream, delimiter=delimiter)
    
    try:
        return list(reader)
    except csv.Error as e:
        raise ProcessingError(f"CSV parsing error: {e}")

def xml_to_dict(xml_str: str) -> Dict[str, Any]:
    """
    Convert simple XML to dictionary (basic implementation).
    
    Args:
        xml_str (str): XML string
        
    Returns:
        Dict[str, Any]: Dictionary representation
        
    Note:
        This is a simplified implementation for basic XML structures.
    """
    import re
    
    if not isinstance(xml_str, str):
        raise ProcessingError("Input must be a string")
    
    # This is a very basic XML parser - for production use xml.etree.ElementTree
    result = {}
    
    # Find all tags and their content
    pattern = r'<(\w+)>(.*?)</\1>'
    matches = re.findall(pattern, xml_str, re.DOTALL)
    
    for tag, content in matches:
        # Check if content contains nested tags
        if '<' in content and '>' in content:
            result[tag] = xml_to_dict(content)
        else:
            result[tag] = content.strip()
    
    return result

def bytes_to_string(data: bytes, encoding: str = 'utf-8') -> str:
    """
    Convert bytes to string with specified encoding.
    
    Args:
        data (bytes): Bytes data
        encoding (str): Text encoding
        
    Returns:
        str: Decoded string
        
    Example:
        >>> bytes_to_string(b'Hello World')
        'Hello World'
    """
    if not isinstance(data, bytes):
        raise ProcessingError("Input must be bytes")
    
    try:
        return data.decode(encoding)
    except UnicodeDecodeError as e:
        raise ProcessingError(f"Decoding error: {e}")

def string_to_bytes(text: str, encoding: str = 'utf-8') -> bytes:
    """
    Convert string to bytes with specified encoding.
    
    Args:
        text (str): Text string
        encoding (str): Text encoding
        
    Returns:
        bytes: Encoded bytes
        
    Example:
        >>> string_to_bytes('Hello World')
        b'Hello World'
    """
    if not isinstance(text, str):
        raise ProcessingError("Input must be a string")
    
    try:
        return text.encode(encoding)
    except UnicodeEncodeError as e:
        raise ProcessingError(f"Encoding error: {e}")