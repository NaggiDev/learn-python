"""
Calculator Module - Solution

A simple calculator module with basic arithmetic operations.
Demonstrates proper module structure, documentation, and error handling.

Author: Python Learning Path
Version: 1.0
"""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Add two numbers.
    
    Args:
        a (Number): First number
        b (Number): Second number
        
    Returns:
        Number: Sum of a and b
        
    Example:
        >>> add(5, 3)
        8
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """
    Subtract second number from first number.
    
    Args:
        a (Number): First number (minuend)
        b (Number): Second number (subtrahend)
        
    Returns:
        Number: Difference of a and b
        
    Example:
        >>> subtract(10, 3)
        7
        >>> subtract(5.5, 2.2)
        3.3
    """
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.
    
    Args:
        a (Number): First number
        b (Number): Second number
        
    Returns:
        Number: Product of a and b
        
    Example:
        >>> multiply(4, 5)
        20
        >>> multiply(2.5, 3)
        7.5
    """
    return a * b

def divide(a: Number, b: Number) -> float:
    """
    Divide first number by second number.
    
    Args:
        a (Number): Dividend
        b (Number): Divisor
        
    Returns:
        float: Quotient of a and b
        
    Raises:
        ValueError: If b is zero
        
    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 3)
        2.3333333333333335
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a: Number, b: Number = 2) -> Number:
    """
    Raise first number to the power of second number.
    
    Args:
        a (Number): Base number
        b (Number, optional): Exponent. Defaults to 2.
        
    Returns:
        Number: a raised to the power of b
        
    Example:
        >>> power(3, 2)
        9
        >>> power(2, 3)
        8
        >>> power(5)  # Default exponent is 2
        25
    """
    return a ** b

def main():
    """Test the calculator functions."""
    print("Calculator Module Test:")
    print("=" * 30)
    
    # Test addition
    result = add(5, 3)
    print(f"add(5, 3) = {result}")
    
    # Test subtraction
    result = subtract(10, 4)
    print(f"subtract(10, 4) = {result}")
    
    # Test multiplication
    result = multiply(6, 7)
    print(f"multiply(6, 7) = {result}")
    
    # Test division
    result = divide(15, 3)
    print(f"divide(15, 3) = {result}")
    
    # Test division by zero
    try:
        result = divide(10, 0)
        print(f"divide(10, 0) = {result}")
    except ValueError as e:
        print(f"divide(10, 0) raised ValueError: {e}")
    
    # Test power function
    result = power(2, 3)
    print(f"power(2, 3) = {result}")
    
    # Test power with default exponent
    result = power(4)
    print(f"power(4) = {result}")
    
    # Test with floating point numbers
    result = add(2.5, 3.7)
    print(f"add(2.5, 3.7) = {result}")
    
    result = divide(7, 3)
    print(f"divide(7, 3) = {result:.2f}")
    
    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    main()