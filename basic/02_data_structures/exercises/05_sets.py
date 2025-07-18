"""
Exercise: Sets

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

Learning objectives:
- Create and initialize sets
- Add and remove elements from sets
- Perform set operations (union, intersection, difference)
- Use set comprehensions
- Apply sets to solve common problems
"""

def create_set():
    """
    Create and return a set containing the following elements:
    'apple', 'banana', 'cherry', 'date', 'elderberry'
    
    Returns:
        set: A set with the specified elements
    """
    # TODO: Implement this function
    pass


def add_elements(my_set, elements):
    """
    Add multiple elements to the set and return the modified set.
    
    Args:
        my_set (set): The input set
        elements (list): A list of elements to add
        
    Returns:
        set: The modified set with new elements added
    """
    # TODO: Implement this function
    pass


def remove_element(my_set, element):
    """
    Remove an element from the set if it exists and return the modified set.
    If the element doesn't exist, return the set unchanged.
    
    Args:
        my_set (set): The input set
        element (any): The element to remove
        
    Returns:
        set: The modified set with the element removed (if it existed)
    """
    # TODO: Implement this function
    pass


def is_element_in_set(my_set, element):
    """
    Check if an element exists in the set.
    
    Args:
        my_set (set): The input set
        element (any): The element to check
        
    Returns:
        bool: True if the element is in the set, False otherwise
    """
    # TODO: Implement this function
    pass


def get_set_union(set1, set2):
    """
    Return the union of two sets (all elements that are in either set).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        set: A new set containing all elements from both sets
    """
    # TODO: Implement this function
    pass


def get_set_intersection(set1, set2):
    """
    Return the intersection of two sets (elements that are in both sets).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        set: A new set containing only elements that are in both sets
    """
    # TODO: Implement this function
    pass


def get_set_difference(set1, set2):
    """
    Return the difference between set1 and set2 (elements in set1 but not in set2).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        set: A new set containing elements that are in set1 but not in set2
    """
    # TODO: Implement this function
    pass


def get_symmetric_difference(set1, set2):
    """
    Return the symmetric difference between two sets (elements in either set, but not in both).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        set: A new set containing elements that are in either set, but not in both
    """
    # TODO: Implement this function
    pass


def is_subset(set1, set2):
    """
    Check if set1 is a subset of set2 (all elements of set1 are in set2).
    
    Args:
        set1 (set): The potential subset
        set2 (set): The potential superset
        
    Returns:
        bool: True if set1 is a subset of set2, False otherwise
    """
    # TODO: Implement this function
    pass


def is_superset(set1, set2):
    """
    Check if set1 is a superset of set2 (all elements of set2 are in set1).
    
    Args:
        set1 (set): The potential superset
        set2 (set): The potential subset
        
    Returns:
        bool: True if set1 is a superset of set2, False otherwise
    """
    # TODO: Implement this function
    pass


def are_disjoint(set1, set2):
    """
    Check if two sets are disjoint (have no elements in common).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        bool: True if the sets are disjoint, False otherwise
    """
    # TODO: Implement this function
    pass


def create_set_of_squares(n):
    """
    Create a set of squares of numbers from 1 to n using a set comprehension.
    
    Args:
        n (int): The upper limit (inclusive)
        
    Returns:
        set: A set containing squares of numbers from 1 to n
    """
    # TODO: Implement this function using a set comprehension
    pass


def filter_even_numbers(numbers):
    """
    Create a set containing only the even numbers from the input list.
    
    Args:
        numbers (list): A list of integers
        
    Returns:
        set: A set containing only the even numbers from the input list
    """
    # TODO: Implement this function using a set comprehension
    pass


def find_unique_elements(list1, list2):
    """
    Find elements that are unique to either list (not in both).
    
    Args:
        list1 (list): The first list
        list2 (list): The second list
        
    Returns:
        set: A set containing elements that are in either list, but not in both
    """
    # TODO: Implement this function
    pass


def find_common_elements(list1, list2):
    """
    Find elements that are common to both lists.
    
    Args:
        list1 (list): The first list
        list2 (list): The second list
        
    Returns:
        set: A set containing elements that are in both lists
    """
    # TODO: Implement this function
    pass


def remove_duplicates(items):
    """
    Remove duplicates from a list while preserving the order.
    
    Args:
        items (list): A list that may contain duplicates
        
    Returns:
        list: A new list with duplicates removed, preserving the original order
    """
    # TODO: Implement this function
    pass


# Tests
def test_create_set():
    result = create_set()
    expected = {'apple', 'banana', 'cherry', 'date', 'elderberry'}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, set), f"Expected a set, but got {type(result)}"
    print("✓ test_create_set passed")


def test_add_elements():
    test_set = {'a', 'b', 'c'}
    elements = ['d', 'e', 'f']
    
    result = add_elements(test_set, elements)
    expected = {'a', 'b', 'c', 'd', 'e', 'f'}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_set == expected, "The original set should be modified"
    
    print("✓ test_add_elements passed")


def test_remove_element():
    # Test removing an existing element
    test_set = {'a', 'b', 'c', 'd'}
    result = remove_element(test_set, 'b')
    expected = {'a', 'c', 'd'}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_set == expected, "The original set should be modified"
    
    # Test removing a non-existing element
    test_set = {'a', 'c', 'd'}
    result = remove_element(test_set, 'z')
    expected = {'a', 'c', 'd'}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert test_set == expected, "The set should remain unchanged"
    
    print("✓ test_remove_element passed")


def test_is_element_in_set():
    test_set = {'a', 'b', 'c', 'd'}
    
    # Test element in set
    result = is_element_in_set(test_set, 'c')
    assert result is True, f"Expected True, but got {result}"
    
    # Test element not in set
    result = is_element_in_set(test_set, 'z')
    assert result is False, f"Expected False, but got {result}"
    
    print("✓ test_is_element_in_set passed")


def test_get_set_union():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    result = get_set_union(set1, set2)
    expected = {1, 2, 3, 4, 5, 6}
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Check that the original sets are unchanged
    assert set1 == {1, 2, 3, 4}, "set1 should remain unchanged"
    assert set2 == {3, 4, 5, 6}, "set2 should remain unchanged"
    
    print("✓ test_get_set_union passed")


def test_get_set_intersection():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    result = get_set_intersection(set1, set2)
    expected = {3, 4}
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Check that the original sets are unchanged
    assert set1 == {1, 2, 3, 4}, "set1 should remain unchanged"
    assert set2 == {3, 4, 5, 6}, "set2 should remain unchanged"
    
    print("✓ test_get_set_intersection passed")


def test_get_set_difference():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    result = get_set_difference(set1, set2)
    expected = {1, 2}
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Check that the original sets are unchanged
    assert set1 == {1, 2, 3, 4}, "set1 should remain unchanged"
    assert set2 == {3, 4, 5, 6}, "set2 should remain unchanged"
    
    print("✓ test_get_set_difference passed")


def test_get_symmetric_difference():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    result = get_symmetric_difference(set1, set2)
    expected = {1, 2, 5, 6}
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Check that the original sets are unchanged
    assert set1 == {1, 2, 3, 4}, "set1 should remain unchanged"
    assert set2 == {3, 4, 5, 6}, "set2 should remain unchanged"
    
    print("✓ test_get_symmetric_difference passed")


def test_is_subset():
    # Test true subset
    set1 = {1, 2}
    set2 = {1, 2, 3, 4}
    result = is_subset(set1, set2)
    assert result is True, f"Expected True, but got {result}"
    
    # Test equal sets (still a subset)
    set1 = {1, 2, 3}
    set2 = {1, 2, 3}
    result = is_subset(set1, set2)
    assert result is True, f"Expected True, but got {result}"
    
    # Test not a subset
    set1 = {1, 2, 5}
    set2 = {1, 2, 3, 4}
    result = is_subset(set1, set2)
    assert result is False, f"Expected False, but got {result}"
    
    print("✓ test_is_subset passed")


def test_is_superset():
    # Test true superset
    set1 = {1, 2, 3, 4}
    set2 = {1, 2}
    result = is_superset(set1, set2)
    assert result is True, f"Expected True, but got {result}"
    
    # Test equal sets (still a superset)
    set1 = {1, 2, 3}
    set2 = {1, 2, 3}
    result = is_superset(set1, set2)
    assert result is True, f"Expected True, but got {result}"
    
    # Test not a superset
    set1 = {1, 2, 3}
    set2 = {1, 2, 4}
    result = is_superset(set1, set2)
    assert result is False, f"Expected False, but got {result}"
    
    print("✓ test_is_superset passed")


def test_are_disjoint():
    # Test disjoint sets
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    result = are_disjoint(set1, set2)
    assert result is True, f"Expected True, but got {result}"
    
    # Test non-disjoint sets
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    result = are_disjoint(set1, set2)
    assert result is False, f"Expected False, but got {result}"
    
    print("✓ test_are_disjoint passed")


def test_create_set_of_squares():
    result = create_set_of_squares(5)
    expected = {1, 4, 9, 16, 25}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, set), f"Expected a set, but got {type(result)}"
    print("✓ test_create_set_of_squares passed")


def test_filter_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = filter_even_numbers(numbers)
    expected = {2, 4, 6, 8}
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, set), f"Expected a set, but got {type(result)}"
    print("✓ test_filter_even_numbers passed")


def test_find_unique_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    
    result = find_unique_elements(list1, list2)
    expected = {1, 2, 3, 6, 7, 8}
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_find_unique_elements passed")


def test_find_common_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    
    result = find_common_elements(list1, list2)
    expected = {4, 5}
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_find_common_elements passed")


def test_remove_duplicates():
    items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
    
    result = remove_duplicates(items)
    expected = ['apple', 'banana', 'cherry', 'date']
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, list), f"Expected a list, but got {type(result)}"
    print("✓ test_remove_duplicates passed")


if __name__ == "__main__":
    print("Running tests for sets...")
    test_create_set()
    test_add_elements()
    test_remove_element()
    test_is_element_in_set()
    test_get_set_union()
    test_get_set_intersection()
    test_get_set_difference()
    test_get_symmetric_difference()
    test_is_subset()
    test_is_superset()
    test_are_disjoint()
    test_create_set_of_squares()
    test_filter_even_numbers()
    test_find_unique_elements()
    test_find_common_elements()
    test_remove_duplicates()
    print("All tests passed!")