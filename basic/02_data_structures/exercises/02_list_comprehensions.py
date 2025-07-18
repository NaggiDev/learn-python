"""
Exercise: List Comprehensions

Instructions:
1. Complete the functions below according to their docstrings
2. Use list comprehensions to solve each problem
3. Run the tests to verify your implementation

Learning objectives:
- Create lists using list comprehensions
- Filter elements using conditional expressions
- Transform data using list comprehensions
- Use nested list comprehensions
"""

def squares(n):
    """
    Create a list of squares of numbers from 0 to n-1 using a list comprehension.
    
    Args:
        n (int): The upper limit (exclusive)
        
    Returns:
        list: A list of squares [0^2, 1^2, 2^2, ..., (n-1)^2]
    """
    # TODO: Implement this function using a list comprehension
    pass


def even_numbers(numbers):
    """
    Filter a list to include only even numbers using a list comprehension.
    
    Args:
        numbers (list): A list of integers
        
    Returns:
        list: A list containing only the even numbers from the input list
    """
    # TODO: Implement this function using a list comprehension
    pass


def uppercase_strings(strings):
    """
    Convert all strings in a list to uppercase using a list comprehension.
    
    Args:
        strings (list): A list of strings
        
    Returns:
        list: A list with all strings converted to uppercase
    """
    # TODO: Implement this function using a list comprehension
    pass


def word_lengths(sentence):
    """
    Calculate the length of each word in a sentence using a list comprehension.
    
    Args:
        sentence (str): A string containing words separated by spaces
        
    Returns:
        list: A list of integers representing the length of each word
    """
    # TODO: Implement this function using a list comprehension
    pass


def filter_by_length(strings, min_length):
    """
    Filter a list of strings to include only those with length >= min_length.
    
    Args:
        strings (list): A list of strings
        min_length (int): The minimum length threshold
        
    Returns:
        list: A list of strings with length >= min_length
    """
    # TODO: Implement this function using a list comprehension
    pass


def extract_product_names(products):
    """
    Extract the 'name' field from a list of product dictionaries.
    
    Args:
        products (list): A list of dictionaries, each with a 'name' key
        
    Returns:
        list: A list of product names
    """
    # TODO: Implement this function using a list comprehension
    pass


def conditional_values(numbers):
    """
    Replace each number with 'even' if it's even, and 'odd' if it's odd.
    
    Args:
        numbers (list): A list of integers
        
    Returns:
        list: A list of strings ('even' or 'odd')
    """
    # TODO: Implement this function using a list comprehension with a conditional expression
    pass


def matrix_to_flat_list(matrix):
    """
    Convert a 2D matrix (list of lists) to a flat 1D list using a nested list comprehension.
    
    Args:
        matrix (list): A 2D list (list of lists)
        
    Returns:
        list: A flattened 1D list containing all elements
    """
    # TODO: Implement this function using a nested list comprehension
    pass


def create_coordinate_pairs(x_values, y_values):
    """
    Create all possible (x, y) coordinate pairs from two lists.
    
    Args:
        x_values (list): A list of x-coordinates
        y_values (list): A list of y-coordinates
        
    Returns:
        list: A list of tuples representing all possible (x, y) pairs
    """
    # TODO: Implement this function using a nested list comprehension
    pass


def filter_and_transform(numbers):
    """
    Filter out negative numbers and square the positive numbers.
    
    Args:
        numbers (list): A list of integers (positive and negative)
        
    Returns:
        list: A list of squares of the positive numbers
    """
    # TODO: Implement this function using a list comprehension with filtering
    pass


# Tests
def test_squares():
    result = squares(5)
    expected = [0, 1, 4, 9, 16]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_squares passed")


def test_even_numbers():
    result = even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    expected = [2, 4, 6, 8]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_even_numbers passed")


def test_uppercase_strings():
    result = uppercase_strings(["hello", "world", "python"])
    expected = ["HELLO", "WORLD", "PYTHON"]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_uppercase_strings passed")


def test_word_lengths():
    result = word_lengths("The quick brown fox jumps over the lazy dog")
    expected = [3, 5, 5, 3, 5, 4, 3, 4, 3]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_word_lengths passed")


def test_filter_by_length():
    result = filter_by_length(["apple", "banana", "cherry", "date", "elderberry"], 6)
    expected = ["banana", "cherry", "elderberry"]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_filter_by_length passed")


def test_extract_product_names():
    products = [
        {"id": 1, "name": "Laptop", "price": 999},
        {"id": 2, "name": "Mouse", "price": 25},
        {"id": 3, "name": "Keyboard", "price": 75}
    ]
    result = extract_product_names(products)
    expected = ["Laptop", "Mouse", "Keyboard"]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_extract_product_names passed")


def test_conditional_values():
    result = conditional_values([1, 2, 3, 4, 5])
    expected = ["odd", "even", "odd", "even", "odd"]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_conditional_values passed")


def test_matrix_to_flat_list():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_to_flat_list(matrix)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_matrix_to_flat_list passed")


def test_create_coordinate_pairs():
    result = create_coordinate_pairs([1, 2], [3, 4])
    expected = [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_create_coordinate_pairs passed")


def test_filter_and_transform():
    result = filter_and_transform([-3, -2, -1, 0, 1, 2, 3])
    expected = [0, 1, 4, 9]
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ test_filter_and_transform passed")


if __name__ == "__main__":
    print("Running tests for list comprehensions...")
    test_squares()
    test_even_numbers()
    test_uppercase_strings()
    test_word_lengths()
    test_filter_by_length()
    test_extract_product_names()
    test_conditional_values()
    test_matrix_to_flat_list()
    test_create_coordinate_pairs()
    test_filter_and_transform()
    print("All tests passed!")