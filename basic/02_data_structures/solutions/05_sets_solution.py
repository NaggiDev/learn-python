"""
Solution: Sets

This file contains solutions to the sets exercises.
"""

def create_set():
    """
    Create and return a set containing the following elements:
    'apple', 'banana', 'cherry', 'date', 'elderberry'
    
    Returns:
        set: A set with the specified elements
    """
    return {'apple', 'banana', 'cherry', 'date', 'elderberry'}


def add_elements(my_set, elements):
    """
    Add multiple elements to the set and return the modified set.
    
    Args:
        my_set (set): The input set
        elements (list): A list of elements to add
        
    Returns:
        set: The modified set with new elements added
    """
    my_set.update(elements)
    return my_set


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
    my_set.discard(element)  # discard() doesn't raise an error if element doesn't exist
    return my_set


def is_element_in_set(my_set, element):
    """
    Check if an element exists in the set.
    
    Args:
        my_set (set): The input set
        element (any): The element to check
        
    Returns:
        bool: True if the element is in the set, False otherwise
    """
    return element in my_set


def get_set_union(set1, set2):
    """
    Return the union of two sets (all elements that are in either set).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        set: A new set containing all elements from both sets
    """
    return set1.union(set2)  # or set1 | set2


def get_set_intersection(set1, set2):
    """
    Return the intersection of two sets (elements that are in both sets).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        set: A new set containing only elements that are in both sets
    """
    return set1.intersection(set2)  # or set1 & set2


def get_set_difference(set1, set2):
    """
    Return the difference between set1 and set2 (elements in set1 but not in set2).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        set: A new set containing elements that are in set1 but not in set2
    """
    return set1.difference(set2)  # or set1 - set2


def get_symmetric_difference(set1, set2):
    """
    Return the symmetric difference between two sets (elements in either set, but not in both).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        set: A new set containing elements that are in either set, but not in both
    """
    return set1.symmetric_difference(set2)  # or set1 ^ set2


def is_subset(set1, set2):
    """
    Check if set1 is a subset of set2 (all elements of set1 are in set2).
    
    Args:
        set1 (set): The potential subset
        set2 (set): The potential superset
        
    Returns:
        bool: True if set1 is a subset of set2, False otherwise
    """
    return set1.issubset(set2)  # or set1 <= set2


def is_superset(set1, set2):
    """
    Check if set1 is a superset of set2 (all elements of set2 are in set1).
    
    Args:
        set1 (set): The potential superset
        set2 (set): The potential subset
        
    Returns:
        bool: True if set1 is a superset of set2, False otherwise
    """
    return set1.issuperset(set2)  # or set1 >= set2


def are_disjoint(set1, set2):
    """
    Check if two sets are disjoint (have no elements in common).
    
    Args:
        set1 (set): The first set
        set2 (set): The second set
        
    Returns:
        bool: True if the sets are disjoint, False otherwise
    """
    return set1.isdisjoint(set2)


def create_set_of_squares(n):
    """
    Create a set of squares of numbers from 1 to n using a set comprehension.
    
    Args:
        n (int): The upper limit (inclusive)
        
    Returns:
        set: A set containing squares of numbers from 1 to n
    """
    return {i**2 for i in range(1, n+1)}


def filter_even_numbers(numbers):
    """
    Create a set containing only the even numbers from the input list.
    
    Args:
        numbers (list): A list of integers
        
    Returns:
        set: A set containing only the even numbers from the input list
    """
    return {num for num in numbers if num % 2 == 0}


def find_unique_elements(list1, list2):
    """
    Find elements that are unique to either list (not in both).
    
    Args:
        list1 (list): The first list
        list2 (list): The second list
        
    Returns:
        set: A set containing elements that are in either list, but not in both
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.symmetric_difference(set2)  # or set1 ^ set2


def find_common_elements(list1, list2):
    """
    Find elements that are common to both lists.
    
    Args:
        list1 (list): The first list
        list2 (list): The second list
        
    Returns:
        set: A set containing elements that are in both lists
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)  # or set1 & set2


def remove_duplicates(items):
    """
    Remove duplicates from a list while preserving the order.
    
    Args:
        items (list): A list that may contain duplicates
        
    Returns:
        list: A new list with duplicates removed, preserving the original order
    """
    # Using dict.fromkeys() preserves order in Python 3.7+
    return list(dict.fromkeys(items))