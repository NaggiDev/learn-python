"""
Advanced mathematical operations.

This module provides more complex mathematical functions including
number theory operations and recursive algorithms.
"""

import math
from typing import Union

Number = Union[int, float]

def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
        
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    return math.factorial(n)

def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        
    Example:
        >>> fibonacci(10)
        55
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    
    if n <= 1:
        return n
    
    # Iterative approach for efficiency
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is prime, False otherwise
        
    Example:
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
        >>> is_prime(2)
        True
    """
    if not isinstance(n, int):
        return False
    
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest common divisor of a and b
        
    Example:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
    """
    return math.gcd(abs(a), abs(b))

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Least common multiple of a and b
        
    Raises:
        ValueError: If either number is zero
        
    Example:
        >>> lcm(12, 18)
        36
        >>> lcm(7, 5)
        35
    """
    if a == 0 or b == 0:
        raise ValueError("LCM is not defined for zero")
    
    return abs(a * b) // gcd(a, b)