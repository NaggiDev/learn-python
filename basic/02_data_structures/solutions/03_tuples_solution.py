"""
Solution: Tuples

This file contains solutions to the tuples exercises.
"""

from collections import namedtuple

def create_tuple():
    """
    Create and return a tuple containing the following items in order:
    'apple', 'banana', 'cherry', 'date', 'elderberry'
    
    Returns:
        tuple: A tuple of fruit names
    """
    return ('apple', 'banana', 'cherry', 'date', 'elderberry')


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
    try:
        return my_tuple[index]
    except IndexError:
        return None


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
    return my_tuple[start:end]


def count_occurrences(my_tuple, element):
    """
    Count and return the number of occurrences of the element in the tuple.
    
    Args:
        my_tuple (tuple): The input tuple
        element (any): The element to count
        
    Returns:
        int: The number of occurrences of the element
    """
    return my_tuple.count(element)


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
    try:
        return my_tuple.index(element)
    except ValueError:
        return -1


def concatenate_tuples(tuple1, tuple2):
    """
    Concatenate two tuples and return the result.
    
    Args:
        tuple1 (tuple): The first tuple
        tuple2 (tuple): The second tuple
        
    Returns:
        tuple: A new tuple containing elements from both input tuples
    """
    return tuple1 + tuple2


def tuple_to_list(my_tuple):
    """
    Convert a tuple to a list and return the result.
    
    Args:
        my_tuple (tuple): The input tuple
        
    Returns:
        list: A list containing the same elements as the input tuple
    """
    return list(my_tuple)


def unpack_tuple(person_info):
    """
    Unpack the tuple containing (name, age, occupation) and return them as separate values.
    
    Args:
        person_info (tuple): A tuple containing (name, age, occupation)
        
    Returns:
        tuple: A tuple containing the unpacked values (name, age, occupation)
    """
    name, age, occupation = person_info
    return (name, age, occupation)


def swap_values(a, b):
    """
    Swap the values of a and b using tuple packing and unpacking.
    
    Args:
        a (any): First value
        b (any): Second value
        
    Returns:
        tuple: A tuple containing the swapped values (b, a)
    """
    a, b = b, a
    return (a, b)


def create_named_tuple():
    """
    Create and return a named tuple type called 'Point' with fields 'x' and 'y',
    and create an instance with x=3 and y=4.
    
    Returns:
        namedtuple: An instance of the 'Point' named tuple with x=3 and y=4
    """
    Point = namedtuple('Point', ['x', 'y'])
    return Point(3, 4)


def extract_coordinates(point):
    """
    Extract the x and y coordinates from a named tuple and return them as a regular tuple.
    
    Args:
        point (namedtuple): A named tuple with 'x' and 'y' attributes
        
    Returns:
        tuple: A tuple containing (x, y)
    """
    return (point.x, point.y)