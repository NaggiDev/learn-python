"""
Exercise: List Basics

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

Learning objectives:
- Create and initialize lists
- Access list elements by index
- Modify list elements
- Use common list methods
"""

def create_list():
    """
    Create and return a list containing the following items in order:
    'apple', 'banana', 'cherry', 'date', 'elderberry'
    
    Returns:
        list: A list of fruit names
    """
    # TODO: Implement this function
    pass


def access_element(my_list, index):
    """
    Access and return an element from the list at the specified index.
    If the index is out of range, return None instead of raising an error.
    
    Args:
        my_list (list): The input list
        index (int): The index to access
        
    Returns:
        any: The element at the specified index or None if index is out of range
    """
    # TODO: Implement this function
    pass


def modify_list(my_list, index, new_value):
    """
    Modify the list by replacing the element at the specified index with the new value.
    If the index is out of range, the list should remain unchanged.
    
    Args:
        my_list (list): The input list
        index (int): The index to modify
        new_value (any): The new value to insert
        
    Returns:
        list: The modified list, or the original list if index was out of range
    """
    # TODO: Implement this function
    pass


def append_element(my_list, element):
    """
    Append the element to the end of the list and return the modified list.
    
    Args:
        my_list (list): The input list
        element (any): The element to append
        
    Returns:
        list: The modified list with the new element appended
    """
    # TODO: Implement this function
    pass


def insert_element(my_list, index, element):
    """
    Insert the element at the specified index in the list and return the modified list.
    If the index is out of range, insert the element at the end of the list.
    
    Args:
        my_list (list): The input list
        index (int): The index at which to insert
        element (any): The element to insert
        
    Returns:
        list: The modified list with the new element inserted
    """
    # TODO: Implement this function
    pass


def remove_element(my_list, element):
    """
    Remove the first occurrence of the element from the list and return the modified list.
    If the element is not in the list, return the list unchanged.
    
    Args:
        my_list (list): The input list
        element (any): The element to remove
        
    Returns:
        list: The modified list with the element removed, or the original list if element not found
    """
    # TODO: Implement this function
    pass


def pop_element(my_list, index=-1):
    """
    Remove and return the element at the specified index.
    If no index is specified, remove and return the last element.
    If the index is out of range, return None and leave the list unchanged.
    
    Args:
        my_list (list): The input list
        index (int, optional): The index of the element to remove. Defaults to -1 (last element).
        
    Returns:
        any: The removed element, or None if index is out of range
    """
    # TODO: Implement this function
    pass


def find_index(my_list, element):
    """
    Find and return the index of the first occurrence of the element in the list.
    If the element is not in the list, return -1.
    
    Args:
        my_list (list): The input list
        element (any): The element to find
        
    Returns:
        int: The index of the element, or -1 if not found
    """
    # TODO: Implement this function
    pass


def count_occurrences(my_list, element):
    """
    Count and return the number of occurrences of the element in the list.
    
    Args:
        my_list (list): The input list
        element (any): The element to count
        
    Returns:
        int: The number of occurrences of the element
    """
    # TODO: Implement this function
    pass


def sort_list(my_list, reverse=False):
    """
    Sort the list in-place and return the sorted list.
    If reverse is True, sort in descending order.
    
    Args:
        my_list (list): The input list
        reverse (bool, optional): Whether to sort in descending order. Defaults to False.
        
    Returns:
        list: The sorted list
    """
    # TODO: Implement this function
    pass


# Tests
def test_create_list():
    result = create_list()
    expected = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_create_list passed")


def test_access_element():
    test_list = ['a', 'b', 'c', 'd', 'e']
    
    # Test valid index
    result = access_element(test_list, 2)
    expected = 'c'
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test negative index
    result = access_element(test_list, -1)
    expected = 'e'
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test out of range index
    result = access_element(test_list, 10)
    expected = None
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_access_element passed")


def test_modify_list():
    # Test valid index
    test_list = [1, 2, 3, 4, 5]
    result = modify_list(test_list, 2, 30)
    expected = [1, 2, 30, 4, 5]
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test out of range index
    test_list = [1, 2, 3, 4, 5]
    result = modify_list(test_list, 10, 30)
    expected = [1, 2, 3, 4, 5]  # List should remain unchanged
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_modify_list passed")


def test_append_element():
    test_list = [1, 2, 3]
    result = append_element(test_list, 4)
    expected = [1, 2, 3, 4]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_append_element passed")


def test_insert_element():
    # Test valid index
    test_list = [1, 2, 3, 4]
    result = insert_element(test_list, 2, 'x')
    expected = [1, 2, 'x', 3, 4]
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test out of range index
    test_list = [1, 2, 3, 4]
    result = insert_element(test_list, 10, 'y')
    expected = [1, 2, 3, 4, 'y']  # Should insert at the end
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_insert_element passed")


def test_remove_element():
    # Test element in list
    test_list = ['a', 'b', 'c', 'b', 'd']
    result = remove_element(test_list, 'b')
    expected = ['a', 'c', 'b', 'd']  # Only first 'b' should be removed
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test element not in list
    test_list = ['a', 'b', 'c']
    result = remove_element(test_list, 'z')
    expected = ['a', 'b', 'c']  # List should remain unchanged
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_remove_element passed")


def test_pop_element():
    # Test default (last element)
    test_list = [1, 2, 3, 4]
    original_list = test_list.copy()
    result = pop_element(test_list)
    expected_element = 4
    expected_list = [1, 2, 3]
    assert result == expected_element, f"Expected {expected_element}, but got {result}"
    assert test_list == expected_list, f"Expected list to be {expected_list}, but got {test_list}"
    
    # Test specific index
    test_list = [1, 2, 3, 4]
    result = pop_element(test_list, 1)
    expected_element = 2
    expected_list = [1, 3, 4]
    assert result == expected_element, f"Expected {expected_element}, but got {result}"
    assert test_list == expected_list, f"Expected list to be {expected_list}, but got {test_list}"
    
    # Test out of range index
    test_list = [1, 2, 3, 4]
    original_list = test_list.copy()
    result = pop_element(test_list, 10)
    expected_element = None
    assert result == expected_element, f"Expected {expected_element}, but got {result}"
    assert test_list == original_list, f"Expected list to remain unchanged, but got {test_list}"
    
    print("✓ test_pop_element passed")


def test_find_index():
    test_list = ['a', 'b', 'c', 'b', 'd']
    
    # Test element in list
    result = find_index(test_list, 'b')
    expected = 1  # First occurrence
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test element not in list
    result = find_index(test_list, 'z')
    expected = -1
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_find_index passed")


def test_count_occurrences():
    test_list = [1, 2, 3, 2, 4, 2, 5]
    
    # Test multiple occurrences
    result = count_occurrences(test_list, 2)
    expected = 3
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test single occurrence
    result = count_occurrences(test_list, 5)
    expected = 1
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test no occurrences
    result = count_occurrences(test_list, 6)
    expected = 0
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_count_occurrences passed")


def test_sort_list():
    # Test ascending sort
    test_list = [3, 1, 4, 1, 5, 9, 2]
    result = sort_list(test_list)
    expected = [1, 1, 2, 3, 4, 5, 9]
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_list == expected, "The list should be sorted in-place"
    
    # Test descending sort
    test_list = [3, 1, 4, 1, 5, 9, 2]
    result = sort_list(test_list, reverse=True)
    expected = [9, 5, 4, 3, 2, 1, 1]
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_list == expected, "The list should be sorted in-place"
    
    print("✓ test_sort_list passed")


if __name__ == "__main__":
    print("Running tests for list basics...")
    test_create_list()
    test_access_element()
    test_modify_list()
    test_append_element()
    test_insert_element()
    test_remove_element()
    test_pop_element()
    test_find_index()
    test_count_occurrences()
    test_sort_list()
    print("All tests passed!")