"""
Solution: List Basics

This file contains solutions to the list basics exercises.
"""

def create_list():
    """
    Create and return a list containing the following items in order:
    'apple', 'banana', 'cherry', 'date', 'elderberry'
    
    Returns:
        list: A list of fruit names
    """
    return ['apple', 'banana', 'cherry', 'date', 'elderberry']


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
    try:
        return my_list[index]
    except IndexError:
        return None


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
    try:
        my_list[index] = new_value
    except IndexError:
        pass  # List remains unchanged if index is out of range
    return my_list


def append_element(my_list, element):
    """
    Append the element to the end of the list and return the modified list.
    
    Args:
        my_list (list): The input list
        element (any): The element to append
        
    Returns:
        list: The modified list with the new element appended
    """
    my_list.append(element)
    return my_list


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
    try:
        my_list.insert(index, element)
    except IndexError:
        my_list.append(element)
    return my_list


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
    try:
        my_list.remove(element)
    except ValueError:
        pass  # Element not in list, so list remains unchanged
    return my_list


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
    try:
        return my_list.pop(index)
    except IndexError:
        return None


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
    try:
        return my_list.index(element)
    except ValueError:
        return -1


def count_occurrences(my_list, element):
    """
    Count and return the number of occurrences of the element in the list.
    
    Args:
        my_list (list): The input list
        element (any): The element to count
        
    Returns:
        int: The number of occurrences of the element
    """
    return my_list.count(element)


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
    my_list.sort(reverse=reverse)
    return my_list