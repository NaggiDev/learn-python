"""Data transformation utilities."""

from typing import Any, Dict, List, Union
from ..exceptions import ProcessingError

def normalize_data(data: Union[str, List[str]], method: str = "lower") -> Union[str, List[str]]:
    """
    Normalize text data using specified method.
    
    Args:
        data: String or list of strings to normalize
        method (str): Normalization method ('lower', 'upper', 'title', 'strip')
        
    Returns:
        Normalized data in same format as input
        
    Example:
        >>> normalize_data("  Hello World  ", "lower")
        'hello world'
        >>> normalize_data(["Hello", "WORLD"], "lower")
        ['hello', 'world']
    """
    if isinstance(data, str):
        return _normalize_string(data, method)
    elif isinstance(data, list):
        return [_normalize_string(item, method) for item in data if isinstance(item, str)]
    else:
        raise ProcessingError("Data must be string or list of strings")

def _normalize_string(text: str, method: str) -> str:
    """Helper function to normalize a single string."""
    if method == "lower":
        return text.lower().strip()
    elif method == "upper":
        return text.upper().strip()
    elif method == "title":
        return text.title().strip()
    elif method == "strip":
        return text.strip()
    else:
        raise ProcessingError(f"Unknown normalization method: {method}")

def flatten_dict(data: Dict[str, Any], separator: str = ".") -> Dict[str, Any]:
    """
    Flatten nested dictionary.
    
    Args:
        data (Dict): Dictionary to flatten
        separator (str): Separator for nested keys
        
    Returns:
        Dict: Flattened dictionary
        
    Example:
        >>> data = {"a": {"b": {"c": 1}}, "d": 2}
        >>> flatten_dict(data)
        {'a.b.c': 1, 'd': 2}
    """
    if not isinstance(data, dict):
        raise ProcessingError("Input must be a dictionary")
    
    def _flatten(obj, parent_key=""):
        items = []
        for key, value in obj.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key
            if isinstance(value, dict):
                items.extend(_flatten(value, new_key).items())
            else:
                items.append((new_key, value))
        return dict(items)
    
    return _flatten(data)

def unflatten_dict(data: Dict[str, Any], separator: str = ".") -> Dict[str, Any]:
    """
    Unflatten dictionary with nested keys.
    
    Args:
        data (Dict): Flattened dictionary
        separator (str): Separator used in keys
        
    Returns:
        Dict: Nested dictionary
        
    Example:
        >>> data = {'a.b.c': 1, 'd': 2}
        >>> unflatten_dict(data)
        {'a': {'b': {'c': 1}}, 'd': 2}
    """
    if not isinstance(data, dict):
        raise ProcessingError("Input must be a dictionary")
    
    result = {}
    for key, value in data.items():
        keys = key.split(separator)
        current = result
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    return result

def group_by(data: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
    """
    Group list of dictionaries by specified key.
    
    Args:
        data (List[Dict]): List of dictionaries
        key (str): Key to group by
        
    Returns:
        Dict: Grouped data
        
    Example:
        >>> data = [{"type": "A", "value": 1}, {"type": "B", "value": 2}, {"type": "A", "value": 3}]
        >>> result = group_by(data, "type")
        >>> len(result["A"])
        2
    """
    if not isinstance(data, list):
        raise ProcessingError("Data must be a list")
    
    if not all(isinstance(item, dict) for item in data):
        raise ProcessingError("All items must be dictionaries")
    
    groups = {}
    for item in data:
        if key not in item:
            continue
        
        group_key = str(item[key])
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(item)
    
    return groups

def aggregate_data(data: List[Dict[str, Any]], group_key: str, agg_key: str, operation: str = "sum") -> Dict[str, float]:
    """
    Aggregate numeric data by group.
    
    Args:
        data (List[Dict]): List of dictionaries
        group_key (str): Key to group by
        agg_key (str): Key to aggregate
        operation (str): Aggregation operation ('sum', 'avg', 'min', 'max', 'count')
        
    Returns:
        Dict[str, float]: Aggregated results
        
    Example:
        >>> data = [{"type": "A", "value": 10}, {"type": "A", "value": 20}, {"type": "B", "value": 15}]
        >>> aggregate_data(data, "type", "value", "sum")
        {'A': 30.0, 'B': 15.0}
    """
    if not isinstance(data, list):
        raise ProcessingError("Data must be a list")
    
    groups = group_by(data, group_key)
    results = {}
    
    for group, items in groups.items():
        values = []
        for item in items:
            if agg_key in item:
                try:
                    values.append(float(item[agg_key]))
                except (ValueError, TypeError):
                    continue
        
        if not values:
            results[group] = 0.0
            continue
        
        if operation == "sum":
            results[group] = sum(values)
        elif operation == "avg":
            results[group] = sum(values) / len(values)
        elif operation == "min":
            results[group] = min(values)
        elif operation == "max":
            results[group] = max(values)
        elif operation == "count":
            results[group] = float(len(values))
        else:
            raise ProcessingError(f"Unknown operation: {operation}")
    
    return results

def sort_data(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sort list of dictionaries by specified key.
    
    Args:
        data (List[Dict]): List of dictionaries
        key (str): Key to sort by
        reverse (bool): Sort in descending order
        
    Returns:
        List[Dict]: Sorted data
        
    Example:
        >>> data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        >>> sorted_data = sort_data(data, "age")
        >>> sorted_data[0]["name"]
        'Jane'
    """
    if not isinstance(data, list):
        raise ProcessingError("Data must be a list")
    
    if not all(isinstance(item, dict) for item in data):
        raise ProcessingError("All items must be dictionaries")
    
    try:
        return sorted(data, key=lambda x: x.get(key, 0), reverse=reverse)
    except TypeError as e:
        raise ProcessingError(f"Cannot sort data: {e}")

def filter_data(data: List[Dict[str, Any]], filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Filter list of dictionaries based on criteria.
    
    Args:
        data (List[Dict]): List of dictionaries
        filters (Dict): Filter criteria
        
    Returns:
        List[Dict]: Filtered data
        
    Example:
        >>> data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        >>> filtered = filter_data(data, {"age": 30})
        >>> len(filtered)
        1
    """
    if not isinstance(data, list):
        raise ProcessingError("Data must be a list")
    
    if not isinstance(filters, dict):
        raise ProcessingError("Filters must be a dictionary")
    
    result = []
    for item in data:
        if not isinstance(item, dict):
            continue
        
        match = True
        for filter_key, filter_value in filters.items():
            if filter_key not in item or item[filter_key] != filter_value:
                match = False
                break
        
        if match:
            result.append(item)
    
    return result