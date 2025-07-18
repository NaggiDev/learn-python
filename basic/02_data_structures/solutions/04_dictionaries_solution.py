"""
Solution: Dictionaries

This file contains solutions to the dictionaries exercises.
"""

def create_dictionary():
    """
    Create and return a dictionary with the following key-value pairs:
    'name': 'Python', 'version': 3.9, 'is_awesome': True
    
    Returns:
        dict: A dictionary with the specified key-value pairs
    """
    return {'name': 'Python', 'version': 3.9, 'is_awesome': True}


def access_value(my_dict, key, default=None):
    """
    Access and return a value from the dictionary using the given key.
    If the key doesn't exist, return the default value.
    
    Args:
        my_dict (dict): The input dictionary
        key (hashable): The key to access
        default (any, optional): The default value to return if key doesn't exist
        
    Returns:
        any: The value associated with the key, or the default value
    """
    return my_dict.get(key, default)


def add_or_update(my_dict, key, value):
    """
    Add a new key-value pair to the dictionary or update an existing key with a new value.
    Return the modified dictionary.
    
    Args:
        my_dict (dict): The input dictionary
        key (hashable): The key to add or update
        value (any): The value to set
        
    Returns:
        dict: The modified dictionary
    """
    my_dict[key] = value
    return my_dict


def remove_key(my_dict, key):
    """
    Remove a key-value pair from the dictionary and return the modified dictionary.
    If the key doesn't exist, return the dictionary unchanged.
    
    Args:
        my_dict (dict): The input dictionary
        key (hashable): The key to remove
        
    Returns:
        dict: The modified dictionary
    """
    if key in my_dict:
        del my_dict[key]
    return my_dict


def get_keys(my_dict):
    """
    Return a list of all keys in the dictionary.
    
    Args:
        my_dict (dict): The input dictionary
        
    Returns:
        list: A list of all keys in the dictionary
    """
    return list(my_dict.keys())


def get_values(my_dict):
    """
    Return a list of all values in the dictionary.
    
    Args:
        my_dict (dict): The input dictionary
        
    Returns:
        list: A list of all values in the dictionary
    """
    return list(my_dict.values())


def get_items(my_dict):
    """
    Return a list of all key-value pairs in the dictionary as tuples.
    
    Args:
        my_dict (dict): The input dictionary
        
    Returns:
        list: A list of tuples containing key-value pairs
    """
    return list(my_dict.items())


def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries and return the result.
    If there are duplicate keys, values from dict2 should overwrite values from dict1.
    
    Args:
        dict1 (dict): The first dictionary
        dict2 (dict): The second dictionary
        
    Returns:
        dict: A new dictionary containing all key-value pairs from both input dictionaries
    """
    result = dict1.copy()
    result.update(dict2)
    return result


def count_occurrences(items):
    """
    Count the occurrences of each item in the list and return a dictionary
    where keys are items and values are their counts.
    
    Args:
        items (list): A list of items (strings, numbers, etc.)
        
    Returns:
        dict: A dictionary with items as keys and their counts as values
    """
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def filter_by_value(my_dict, min_value):
    """
    Filter a dictionary to include only key-value pairs where the value is greater than or equal to min_value.
    
    Args:
        my_dict (dict): The input dictionary
        min_value (int or float): The minimum value threshold
        
    Returns:
        dict: A new dictionary with filtered key-value pairs
    """
    return {key: value for key, value in my_dict.items() if value >= min_value}


def dict_comprehension_squares(n):
    """
    Use a dictionary comprehension to create a dictionary where keys are numbers from 1 to n,
    and values are their squares.
    
    Args:
        n (int): The upper limit (inclusive)
        
    Returns:
        dict: A dictionary mapping numbers to their squares
    """
    return {i: i**2 for i in range(1, n+1)}


def invert_dictionary(my_dict):
    """
    Invert a dictionary by swapping keys and values.
    Assume all values in the input dictionary are unique and hashable.
    
    Args:
        my_dict (dict): The input dictionary
        
    Returns:
        dict: A new dictionary with keys and values swapped
    """
    return {value: key for key, value in my_dict.items()}


def nested_dictionary_access(data, keys):
    """
    Access a value in a nested dictionary using a list of keys.
    If any key in the path doesn't exist, return None.
    
    Args:
        data (dict): The nested dictionary
        keys (list): A list of keys representing the path to the value
        
    Returns:
        any: The value at the specified path, or None if the path doesn't exist
    """
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current


def update_nested_dictionary(data, keys, value):
    """
    Update a value in a nested dictionary at the specified path.
    If any key in the path doesn't exist, create the necessary dictionaries.
    
    Args:
        data (dict): The nested dictionary
        keys (list): A list of keys representing the path to update
        value (any): The new value to set
        
    Returns:
        dict: The updated nested dictionary
    """
    current = data
    for i, key in enumerate(keys[:-1]):
        if key not in current:
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value
    return data