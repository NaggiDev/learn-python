"""
Exercise: Dictionaries

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

Learning objectives:
- Create and initialize dictionaries
- Access and modify dictionary values
- Use common dictionary methods
- Iterate through dictionaries
- Work with nested dictionaries
- Use dictionary comprehensions
"""

def create_dictionary():
    """
    Create and return a dictionary with the following key-value pairs:
    'name': 'Python', 'version': 3.9, 'is_awesome': True
    
    Returns:
        dict: A dictionary with the specified key-value pairs
    """
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


def get_keys(my_dict):
    """
    Return a list of all keys in the dictionary.
    
    Args:
        my_dict (dict): The input dictionary
        
    Returns:
        list: A list of all keys in the dictionary
    """
    # TODO: Implement this function
    pass


def get_values(my_dict):
    """
    Return a list of all values in the dictionary.
    
    Args:
        my_dict (dict): The input dictionary
        
    Returns:
        list: A list of all values in the dictionary
    """
    # TODO: Implement this function
    pass


def get_items(my_dict):
    """
    Return a list of all key-value pairs in the dictionary as tuples.
    
    Args:
        my_dict (dict): The input dictionary
        
    Returns:
        list: A list of tuples containing key-value pairs
    """
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


def count_occurrences(items):
    """
    Count the occurrences of each item in the list and return a dictionary
    where keys are items and values are their counts.
    
    Args:
        items (list): A list of items (strings, numbers, etc.)
        
    Returns:
        dict: A dictionary with items as keys and their counts as values
    """
    # TODO: Implement this function
    pass


def filter_by_value(my_dict, min_value):
    """
    Filter a dictionary to include only key-value pairs where the value is greater than or equal to min_value.
    
    Args:
        my_dict (dict): The input dictionary
        min_value (int or float): The minimum value threshold
        
    Returns:
        dict: A new dictionary with filtered key-value pairs
    """
    # TODO: Implement this function
    pass


def dict_comprehension_squares(n):
    """
    Use a dictionary comprehension to create a dictionary where keys are numbers from 1 to n,
    and values are their squares.
    
    Args:
        n (int): The upper limit (inclusive)
        
    Returns:
        dict: A dictionary mapping numbers to their squares
    """
    # TODO: Implement this function using a dictionary comprehension
    pass


def invert_dictionary(my_dict):
    """
    Invert a dictionary by swapping keys and values.
    Assume all values in the input dictionary are unique and hashable.
    
    Args:
        my_dict (dict): The input dictionary
        
    Returns:
        dict: A new dictionary with keys and values swapped
    """
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


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
    # TODO: Implement this function
    pass


# Tests
def test_create_dictionary():
    result = create_dictionary()
    expected = {'name': 'Python', 'version': 3.9, 'is_awesome': True}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, dict), f"Expected a dictionary, but got {type(result)}"
    print("✓ test_create_dictionary passed")


def test_access_value():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    
    # Test existing key
    result = access_value(test_dict, 'b')
    expected = 2
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test non-existing key with default
    result = access_value(test_dict, 'd', 0)
    expected = 0
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test non-existing key without default
    result = access_value(test_dict, 'd')
    expected = None
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_access_value passed")


def test_add_or_update():
    # Test adding a new key
    test_dict = {'a': 1, 'b': 2}
    result = add_or_update(test_dict, 'c', 3)
    expected = {'a': 1, 'b': 2, 'c': 3}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_dict == expected, "The original dictionary should be modified"
    
    # Test updating an existing key
    test_dict = {'a': 1, 'b': 2}
    result = add_or_update(test_dict, 'b', 20)
    expected = {'a': 1, 'b': 20}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_dict == expected, "The original dictionary should be modified"
    
    print("✓ test_add_or_update passed")


def test_remove_key():
    # Test removing an existing key
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    result = remove_key(test_dict, 'b')
    expected = {'a': 1, 'c': 3}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_dict == expected, "The original dictionary should be modified"
    
    # Test removing a non-existing key
    test_dict = {'a': 1, 'c': 3}
    result = remove_key(test_dict, 'd')
    expected = {'a': 1, 'c': 3}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_dict == expected, "The dictionary should remain unchanged"
    
    print("✓ test_remove_key passed")


def test_get_keys():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_keys(test_dict)
    expected = ['a', 'b', 'c']
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"
    print("✓ test_get_keys passed")


def test_get_values():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_values(test_dict)
    expected = [1, 2, 3]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"
    print("✓ test_get_values passed")


def test_get_items():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_items(test_dict)
    expected = [('a', 1), ('b', 2), ('c', 3)]
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"
    print("✓ test_get_items passed")


def test_merge_dictionaries():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'c': 30, 'd': 4, 'e': 5}
    
    result = merge_dictionaries(dict1, dict2)
    expected = {'a': 1, 'b': 2, 'c': 30, 'd': 4, 'e': 5}
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Check that the original dictionaries are unchanged
    assert dict1 == {'a': 1, 'b': 2, 'c': 3}, "dict1 should remain unchanged"
    assert dict2 == {'c': 30, 'd': 4, 'e': 5}, "dict2 should remain unchanged"
    
    print("✓ test_merge_dictionaries passed")


def test_count_occurrences():
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = count_occurrences(items)
    expected = {'apple': 3, 'banana': 2, 'orange': 1}
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_count_occurrences passed")


def test_filter_by_value():
    test_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 3}
    
    result = filter_by_value(test_dict, 10)
    expected = {'a': 10, 'c': 15}
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Check that the original dictionary is unchanged
    assert test_dict == {'a': 10, 'b': 5, 'c': 15, 'd': 3}, "Original dictionary should remain unchanged"
    
    print("✓ test_filter_by_value passed")


def test_dict_comprehension_squares():
    result = dict_comprehension_squares(5)
    expected = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_dict_comprehension_squares passed")


def test_invert_dictionary():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    result = invert_dictionary(test_dict)
    expected = {1: 'a', 2: 'b', 3: 'c'}
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_invert_dictionary passed")


def test_nested_dictionary_access():
    data = {
        'user': {
            'name': 'John',
            'address': {
                'city': 'New York',
                'zip': '10001'
            }
        }
    }
    
    # Test valid path
    result = nested_dictionary_access(data, ['user', 'address', 'city'])
    expected = 'New York'
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test invalid path
    result = nested_dictionary_access(data, ['user', 'email'])
    expected = None
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_nested_dictionary_access passed")


def test_update_nested_dictionary():
    # Test updating an existing path
    data = {
        'user': {
            'name': 'John',
            'address': {
                'city': 'New York',
                'zip': '10001'
            }
        }
    }
    
    result = update_nested_dictionary(data, ['user', 'address', 'city'], 'Boston')
    expected = {
        'user': {
            'name': 'John',
            'address': {
                'city': 'Boston',
                'zip': '10001'
            }
        }
    }
    assert result == expected, f"Expected {expected}, but got {result}"
    assert data == expected, "The original dictionary should be modified"
    
    # Test creating a new path
    data = {
        'user': {
            'name': 'John'
        }
    }
    
    result = update_nested_dictionary(data, ['user', 'contact', 'email'], 'john@example.com')
    expected = {
        'user': {
            'name': 'John',
            'contact': {
                'email': 'john@example.com'
            }
        }
    }
    assert result == expected, f"Expected {expected}, but got {result}"
    assert data == expected, "The original dictionary should be modified"
    
    print("✓ test_update_nested_dictionary passed")


if __name__ == "__main__":
    print("Running tests for dictionaries...")
    test_create_dictionary()
    test_access_value()
    test_add_or_update()
    test_remove_key()
    test_get_keys()
    test_get_values()
    test_get_items()
    test_merge_dictionaries()
    test_count_occurrences()
    test_filter_by_value()
    test_dict_comprehension_squares()
    test_invert_dictionary()
    test_nested_dictionary_access()
    test_update_nested_dictionary()
    print("All tests passed!")