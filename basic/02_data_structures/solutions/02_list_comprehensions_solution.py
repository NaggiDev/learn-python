"""
Solution: List Comprehensions

This file contains solutions to the list comprehensions exercises.
"""

def squares(n):
    """
    Create a list of squares of numbers from 0 to n-1 using a list comprehension.
    
    Args:
        n (int): The upper limit (exclusive)
        
    Returns:
        list: A list of squares [0^2, 1^2, 2^2, ..., (n-1)^2]
    """
    return [i**2 for i in range(n)]


def even_numbers(numbers):
    """
    Filter a list to include only even numbers using a list comprehension.
    
    Args:
        numbers (list): A list of integers
        
    Returns:
        list: A list containing only the even numbers from the input list
    """
    return [num for num in numbers if num % 2 == 0]


def uppercase_strings(strings):
    """
    Convert all strings in a list to uppercase using a list comprehension.
    
    Args:
        strings (list): A list of strings
        
    Returns:
        list: A list with all strings converted to uppercase
    """
    return [s.upper() for s in strings]


def word_lengths(sentence):
    """
    Calculate the length of each word in a sentence using a list comprehension.
    
    Args:
        sentence (str): A string containing words separated by spaces
        
    Returns:
        list: A list of integers representing the length of each word
    """
    return [len(word) for word in sentence.split()]


def filter_by_length(strings, min_length):
    """
    Filter a list of strings to include only those with length >= min_length.
    
    Args:
        strings (list): A list of strings
        min_length (int): The minimum length threshold
        
    Returns:
        list: A list of strings with length >= min_length
    """
    return [s for s in strings if len(s) >= min_length]


def extract_product_names(products):
    """
    Extract the 'name' field from a list of product dictionaries.
    
    Args:
        products (list): A list of dictionaries, each with a 'name' key
        
    Returns:
        list: A list of product names
    """
    return [product['name'] for product in products]


def conditional_values(numbers):
    """
    Replace each number with 'even' if it's even, and 'odd' if it's odd.
    
    Args:
        numbers (list): A list of integers
        
    Returns:
        list: A list of strings ('even' or 'odd')
    """
    return ["even" if num % 2 == 0 else "odd" for num in numbers]


def matrix_to_flat_list(matrix):
    """
    Convert a 2D matrix (list of lists) to a flat 1D list using a nested list comprehension.
    
    Args:
        matrix (list): A 2D list (list of lists)
        
    Returns:
        list: A flattened 1D list containing all elements
    """
    return [element for row in matrix for element in row]


def create_coordinate_pairs(x_values, y_values):
    """
    Create all possible (x, y) coordinate pairs from two lists.
    
    Args:
        x_values (list): A list of x-coordinates
        y_values (list): A list of y-coordinates
        
    Returns:
        list: A list of tuples representing all possible (x, y) pairs
    """
    return [(x, y) for x in x_values for y in y_values]


def filter_and_transform(numbers):
    """
    Filter out negative numbers and square the positive numbers.
    
    Args:
        numbers (list): A list of integers (positive and negative)
        
    Returns:
        list: A list of squares of the positive numbers
    """
    return [num**2 for num in numbers if num >= 0]