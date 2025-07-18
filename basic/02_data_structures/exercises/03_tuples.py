"""
Exercise: Tuples

Instructions:
1. Complete the functions below according to their docstrings
2. Run the tests to verify your implementation

Learning objectives:
- Create and initialize tuples
- Access tuple elements by index
- Use tuple packing and unpacking
- Understand tuple immutability
- Work with named tuples
"""

from collections import namedtuple

def create_tuple():
    """
    Create and return a tuple containing the following items in order:
    'apple', 'banana', 'cherry', 'date', 'elderberry'
    
    Returns:
        tuple: A tuple of fruit names
    """
    # TODO: Implement this function
    pass


def access_element(my_tuple, index):
    """
    Access and return an element from the tuple at the specified index.
    If the index is out of range, return None instead of raising an error.
    
    Args:
        my_tuple (tuple): The input tuple
        index (int): The index to access
        
    Returns:
        any: The element at the specified index or None if index is out of range
    """
    # TODO: Implement this function
    pass


def get_slice(my_tuple, start, end):
    """
    Return a slice of the tuple from start index to end index (exclusive).
    
    Args:
        my_tuple (tuple): The input tuple
        start (int): The start index
        end (int): The end index (exclusive)
        
    Returns:
        tuple: A slice of the original tuple
    """
    # TODO: Implement this function
    pass


def count_occurrences(my_tuple, element):
    """
    Count and return the number of occurrences of the element in the tuple.
    
    Args:
        my_tuple (tuple): The input tuple
        element (any): The element to count
        
    Returns:
        int: The number of occurrences of the element
    """
    # TODO: Implement this function
    pass


def find_index(my_tuple, element):
    """
    Find and return the index of the first occurrence of the element in the tuple.
    If the element is not in the tuple, return -1.
    
    Args:
        my_tuple (tuple): The input tuple
        element (any): The element to find
        
    Returns:
        int: The index of the element, or -1 if not found
    """
    # TODO: Implement this function
    pass


def concatenate_tuples(tuple1, tuple2):
    """
    Concatenate two tuples and return the result.
    
    Args:
        tuple1 (tuple): The first tuple
        tuple2 (tuple): The second tuple
        
    Returns:
        tuple: A new tuple containing elements from both input tuples
    """
    # TODO: Implement this function
    pass


def tuple_to_list(my_tuple):
    """
    Convert a tuple to a list and return the result.
    
    Args:
        my_tuple (tuple): The input tuple
        
    Returns:
        list: A list containing the same elements as the input tuple
    """
    # TODO: Implement this function
    pass


def unpack_tuple(person_info):
    """
    Unpack the tuple containing (name, age, occupation) and return them as separate values.
    
    Args:
        person_info (tuple): A tuple containing (name, age, occupation)
        
    Returns:
        tuple: A tuple containing the unpacked values (name, age, occupation)
    """
    # TODO: Implement this function
    pass


def swap_values(a, b):
    """
    Swap the values of a and b using tuple packing and unpacking.
    
    Args:
        a (any): First value
        b (any): Second value
        
    Returns:
        tuple: A tuple containing the swapped values (b, a)
    """
    # TODO: Implement this function
    pass


def create_named_tuple():
    """
    Create and return a named tuple type called 'Point' with fields 'x' and 'y',
    and create an instance with x=3 and y=4.
    
    Returns:
        namedtuple: An instance of the 'Point' named tuple with x=3 and y=4
    """
    # TODO: Implement this function
    pass


def extract_coordinates(point):
    """
    Extract the x and y coordinates from a named tuple and return them as a regular tuple.
    
    Args:
        point (namedtuple): A named tuple with 'x' and 'y' attributes
        
    Returns:
        tuple: A tuple containing (x, y)
    """
    # TODO: Implement this function
    pass


# Tests
def test_create_tuple():
    result = create_tuple()
    expected = ('apple', 'banana', 'cherry', 'date', 'elderberry')
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, tuple), f"Expected a tuple, but got {type(result)}"
    print("✓ test_create_tuple passed")


def test_access_element():
    test_tuple = ('a', 'b', 'c', 'd', 'e')
    
    # Test valid index
    result = access_element(test_tuple, 2)
    expected = 'c'
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test negative index
    result = access_element(test_tuple, -1)
    expected = 'e'
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test out of range index
    result = access_element(test_tuple, 10)
    expected = None
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_access_element passed")


def test_get_slice():
    test_tuple = ('a', 'b', 'c', 'd', 'e')
    
    # Test regular slice
    result = get_slice(test_tuple, 1, 4)
    expected = ('b', 'c', 'd')
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test slice with negative indices
    result = get_slice(test_tuple, -3, -1)
    expected = ('c', 'd')
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_get_slice passed")


def test_count_occurrences():
    test_tuple = (1, 2, 3, 2, 4, 2, 5)
    
    # Test multiple occurrences
    result = count_occurrences(test_tuple, 2)
    expected = 3
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test single occurrence
    result = count_occurrences(test_tuple, 5)
    expected = 1
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test no occurrences
    result = count_occurrences(test_tuple, 6)
    expected = 0
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_count_occurrences passed")


def test_find_index():
    test_tuple = ('a', 'b', 'c', 'b', 'd')
    
    # Test element in tuple
    result = find_index(test_tuple, 'b')
    expected = 1  # First occurrence
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test element not in tuple
    result = find_index(test_tuple, 'z')
    expected = -1
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_find_index passed")


def test_concatenate_tuples():
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    result = concatenate_tuples(tuple1, tuple2)
    expected = (1, 2, 3, 4, 5, 6)
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, tuple), f"Expected a tuple, but got {type(result)}"
    
    print("✓ test_concatenate_tuples passed")


def test_tuple_to_list():
    test_tuple = (1, 2, 3, 4, 5)
    
    result = tuple_to_list(test_tuple)
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, list), f"Expected a list, but got {type(result)}"
    
    print("✓ test_tuple_to_list passed")


def test_unpack_tuple():
    person = ("Alice", 30, "Engineer")
    
    result = unpack_tuple(person)
    expected = ("Alice", 30, "Engineer")
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Check that the function actually unpacked the tuple
    try:
        name, age, occupation = unpack_tuple(person)
        assert name == "Alice", f"Expected name to be 'Alice', but got {name}"
        assert age == 30, f"Expected age to be 30, but got {age}"
        assert occupation == "Engineer", f"Expected occupation to be 'Engineer', but got {occupation}"
    except ValueError:
        assert False, "Failed to unpack the tuple returned by unpack_tuple"
    
    print("✓ test_unpack_tuple passed")


def test_swap_values():
    a = 5
    b = 10
    
    result = swap_values(a, b)
    expected = (10, 5)
    assert result == expected, f"Expected {expected}, but got {result}"
    
    print("✓ test_swap_values passed")


def test_create_named_tuple():
    point = create_named_tuple()
    
    # Check that it's a named tuple with the right attributes
    assert hasattr(point, 'x'), "Point should have an 'x' attribute"
    assert hasattr(point, 'y'), "Point should have a 'y' attribute"
    assert point.x == 3, f"Expected x to be 3, but got {point.x}"
    assert point.y == 4, f"Expected y to be 4, but got {point.y}"
    
    # Check that it's a named tuple
    assert type(point).__bases__[0] is tuple, "Point should be a subclass of tuple"
    
    print("✓ test_create_named_tuple passed")


def test_extract_coordinates():
    # Create a Point named tuple for testing
    Point = namedtuple('Point', ['x', 'y'])
    test_point = Point(5, 6)
    
    result = extract_coordinates(test_point)
    expected = (5, 6)
    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, tuple), f"Expected a tuple, but got {type(result)}"
    
    print("✓ test_extract_coordinates passed")


if __name__ == "__main__":
    print("Running tests for tuples...")
    test_create_tuple()
    test_access_element()
    test_get_slice()
    test_count_occurrences()
    test_find_index()
    test_concatenate_tuples()
    test_tuple_to_list()
    test_unpack_tuple()
    test_swap_values()
    test_create_named_tuple()
    test_extract_coordinates()
    print("All tests passed!")