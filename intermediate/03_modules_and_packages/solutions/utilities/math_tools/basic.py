"""
Basic mathematical operations.

This module provides fundamental arithmetic operations with proper
error handling and type checking.
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

def percentage(part: Number, whole: Number) -> float:
    """
    Calculate what percentage 'part' is of 'whole'.
    
    Args:
        part (Number): The part value
        whole (Number): The whole value
        
    Returns:
        float: Percentage value
        
    Raises:
        ValueError: If whole is zero
        
    Example:
        >>> percentage(25, 100)
        25.0
        >>> percentage(3, 4)
        75.0
    """
    if whole == 0:
        raise ValueError("Cannot calculate percentage with zero as whole")
    return (part / whole) * 100