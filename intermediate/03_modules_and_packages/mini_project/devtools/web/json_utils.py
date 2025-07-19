"""JSON processing utilities."""

import json
from typing import Any, Dict, Optional
from ..exceptions import WebError

def parse_json(json_str: str) -> Any:
    """
    Parse JSON string to Python object.
    
    Args:
        json_str (str): JSON string to parse
        
    Returns:
        Any: Parsed Python object
        
    Example:
        >>> data = parse_json('{"name": "John", "age": 30}')
        >>> data['name']
        'John'
    """
    if not isinstance(json_str, str):
        raise WebError("Input must be a string")
    
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, ValueError) as e:
        raise WebError(f"Invalid JSON: {e}")

def format_json(data: Any, indent: int = 2, sort_keys: bool = False) -> str:
    """
    Format Python object as JSON string.
    
    Args:
        data: Python object to format
        indent (int): JSON indentation
        sort_keys (bool): Whether to sort keys
        
    Returns:
        str: Formatted JSON string
        
    Example:
        >>> json_str = format_json({"name": "John", "age": 30})
        >>> '"name"' in json_str
        True
    """
    try:
        return json.dumps(data, indent=indent, sort_keys=sort_keys, 
                         ensure_ascii=False, separators=(',', ': '))
    except (TypeError, ValueError) as e:
        raise WebError(f"Cannot format as JSON: {e}")

def minify_json(json_str: str) -> str:
    """
    Minify JSON string by removing whitespace.
    
    Args:
        json_str (str): JSON string to minify
        
    Returns:
        str: Minified JSON string
        
    Example:
        >>> minified = minify_json('{"name": "John", "age": 30}')
        >>> ' ' not in minified or minified.count(' ') < 3
        True
    """
    data = parse_json(json_str)
    return json.dumps(data, separators=(',', ':'))

def prettify_json(json_str: str, indent: int = 2) -> str:
    """
    Prettify JSON string with proper formatting.
    
    Args:
        json_str (str): JSON string to prettify
        indent (int): Indentation level
        
    Returns:
        str: Prettified JSON string
        
    Example:
        >>> pretty = prettify_json('{"name":"John","age":30}')
        >>> '\\n' in pretty
        True
    """
    data = parse_json(json_str)
    return format_json(data, indent=indent, sort_keys=True)

def validate_json_schema(data: Any, schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Basic JSON schema validation (simplified implementation).
    
    Args:
        data: Data to validate
        schema (Dict): Simple schema definition
        
    Returns:
        Dict[str, Any]: Validation result
        
    Note:
        This is a basic implementation. For full JSON Schema validation,
        use the jsonschema library.
        
    Example:
        >>> schema = {"type": "object", "required": ["name"]}
        >>> result = validate_json_schema({"name": "John"}, schema)
        >>> result['valid']
        True
    """
    errors = []
    
    # Check type
    if 'type' in schema:
        expected_type = schema['type']
        actual_type = _get_json_type(data)
        
        if actual_type != expected_type:
            errors.append(f"Expected type {expected_type}, got {actual_type}")
    
    # Check required fields (for objects)
    if isinstance(data, dict) and 'required' in schema:
        for field in schema['required']:
            if field not in data:
                errors.append(f"Required field '{field}' is missing")
    
    # Check properties (for objects)
    if isinstance(data, dict) and 'properties' in schema:
        for prop, prop_schema in schema['properties'].items():
            if prop in data:
                prop_result = validate_json_schema(data[prop], prop_schema)
                if not prop_result['valid']:
                    errors.extend([f"{prop}: {error}" for error in prop_result['errors']])
    
    # Check array items
    if isinstance(data, list) and 'items' in schema:
        item_schema = schema['items']
        for i, item in enumerate(data):
            item_result = validate_json_schema(item, item_schema)
            if not item_result['valid']:
                errors.extend([f"Item {i}: {error}" for error in item_result['errors']])
    
    return {
        'valid': len(errors) == 0,
        'errors': errors
    }

def extract_json_paths(data: Any, path: str = "") -> Dict[str, Any]:
    """
    Extract all JSON paths and their values.
    
    Args:
        data: JSON data
        path (str): Current path (for recursion)
        
    Returns:
        Dict[str, Any]: Dictionary of paths and values
        
    Example:
        >>> data = {"user": {"name": "John", "age": 30}}
        >>> paths = extract_json_paths(data)
        >>> paths["user.name"]
        'John'
    """
    paths = {}
    
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            if isinstance(value, (dict, list)):
                paths.update(extract_json_paths(value, new_path))
            else:
                paths[new_path] = value
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            if isinstance(item, (dict, list)):
                paths.update(extract_json_paths(item, new_path))
            else:
                paths[new_path] = item
    else:
        paths[path] = data
    
    return paths

def merge_json(json1: Dict[str, Any], json2: Dict[str, Any], 
               deep: bool = True) -> Dict[str, Any]:
    """
    Merge two JSON objects.
    
    Args:
        json1 (Dict): First JSON object
        json2 (Dict): Second JSON object
        deep (bool): Whether to perform deep merge
        
    Returns:
        Dict[str, Any]: Merged JSON object
        
    Example:
        >>> obj1 = {"a": 1, "b": {"c": 2}}
        >>> obj2 = {"b": {"d": 3}, "e": 4}
        >>> merged = merge_json(obj1, obj2)
        >>> merged["b"]["d"]
        3
    """
    if not isinstance(json1, dict) or not isinstance(json2, dict):
        raise WebError("Both inputs must be dictionaries")
    
    result = json1.copy()
    
    for key, value in json2.items():
        if key in result and deep and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_json(result[key], value, deep)
        else:
            result[key] = value
    
    return result

def filter_json(data: Dict[str, Any], keys: list, include: bool = True) -> Dict[str, Any]:
    """
    Filter JSON object by keys.
    
    Args:
        data (Dict): JSON object to filter
        keys (list): List of keys to include/exclude
        include (bool): Whether to include (True) or exclude (False) keys
        
    Returns:
        Dict[str, Any]: Filtered JSON object
        
    Example:
        >>> data = {"name": "John", "age": 30, "email": "john@example.com"}
        >>> filtered = filter_json(data, ["name", "age"], include=True)
        >>> len(filtered)
        2
    """
    if not isinstance(data, dict):
        raise WebError("Data must be a dictionary")
    
    if include:
        return {k: v for k, v in data.items() if k in keys}
    else:
        return {k: v for k, v in data.items() if k not in keys}

def _get_json_type(value: Any) -> str:
    """Get JSON type name for a Python value."""
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "number"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, list):
        return "array"
    elif isinstance(value, dict):
        return "object"
    else:
        return "unknown"