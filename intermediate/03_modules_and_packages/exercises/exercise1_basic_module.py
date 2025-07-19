"""
Exercise 1: Create a Basic Calculator Module

Instructions:
1. Create a module called 'calculator.py' with basic arithmetic functions
2. Include functions for add, subtract, multiply, divide, and power
3. Add proper error handling for division by zero
4. Include module documentation and function docstrings
5. Add a main function to test the calculator
6. Use the if __name__ == "__main__": pattern

Requirements:
- All functions should accept two parameters (except power which is optional)
- Include type hints where appropriate
- Handle edge cases (like division by zero)
- Add comprehensive docstrings
"""

# TODO: Create the calculator.py module in this directory
# The module should include:

def add(a, b):
    """
    Add two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of a and b
    """
    # TODO: Implement addition
    pass

def subtract(a, b):
    """
    Subtract second number from first number.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Difference of a and b
    """
    # TODO: Implement subtraction
    pass

def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Product of a and b
    """
    # TODO: Implement multiplication
    pass

def divide(a, b):
    """
    Divide first number by second number.
    
    Args:
        a (float): Dividend
        b (float): Divisor
        
    Returns:
        float: Quotient of a and b
        
    Raises:
        ValueError: If b is zero
    """
    # TODO: Implement division with error handling
    pass

def power(a, b=2):
    """
    Raise first number to the power of second number.
    
    Args:
        a (float): Base number
        b (float, optional): Exponent. Defaults to 2.
        
    Returns:
        float: a raised to the power of b
    """
    # TODO: Implement power function
    pass

def main():
    """Test the calculator functions."""
    print("Testing Calculator Module:")
    
    # TODO: Add test cases for all functions
    # Include edge cases like division by zero
    
    pass

if __name__ == "__main__":
    main()

# Test your module by running: python exercise1_basic_module.py
# Then test importing it in another file