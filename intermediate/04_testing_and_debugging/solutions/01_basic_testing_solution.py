"""
Solution: Basic Unit Testing with pytest

This file contains the completed solutions for the basic testing exercise.
"""

import pytest


# Functions to test (same as in exercise)
def is_even(number):
    """Return True if number is even, False otherwise."""
    return number % 2 == 0


def get_grade(score):
    """
    Return letter grade based on numeric score.
    90-100: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def reverse_string(text):
    """Return the reversed version of the input string."""
    return text[::-1]


def find_max(numbers):
    """Return the maximum number from a list of numbers."""
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    return max(numbers)


# Test functions - Solutions
def test_is_even_with_even_number():
    """Test is_even function with an even number."""
    assert is_even(4) == True


def test_is_even_with_odd_number():
    """Test is_even function with an odd number."""
    assert is_even(3) == False


def test_is_even_with_zero():
    """Test is_even function with zero."""
    assert is_even(0) == True  # Zero is even


def test_get_grade_a():
    """Test get_grade function for A grade."""
    assert get_grade(95) == 'A'


def test_get_grade_b():
    """Test get_grade function for B grade."""
    assert get_grade(85) == 'B'


def test_get_grade_f():
    """Test get_grade function for F grade."""
    assert get_grade(45) == 'F'


def test_reverse_string_normal():
    """Test reverse_string with a normal string."""
    assert reverse_string("hello") == "olleh"


def test_reverse_string_empty():
    """Test reverse_string with an empty string."""
    assert reverse_string("") == ""


def test_find_max_normal_list():
    """Test find_max with a normal list of numbers."""
    assert find_max([1, 5, 3, 9, 2]) == 9


def test_find_max_single_element():
    """Test find_max with a single element list."""
    assert find_max([42]) == 42


def test_find_max_empty_list():
    """Test find_max with an empty list should raise ValueError."""
    with pytest.raises(ValueError):
        find_max([])


# Additional comprehensive tests
def test_is_even_negative_numbers():
    """Test is_even with negative numbers."""
    assert is_even(-4) == True
    assert is_even(-3) == False


def test_get_grade_boundary_values():
    """Test get_grade with boundary values."""
    assert get_grade(90) == 'A'  # Boundary for A
    assert get_grade(89) == 'B'  # Just below A
    assert get_grade(80) == 'B'  # Boundary for B
    assert get_grade(79) == 'C'  # Just below B
    assert get_grade(60) == 'D'  # Boundary for D
    assert get_grade(59) == 'F'  # Just below D


def test_reverse_string_palindrome():
    """Test reverse_string with palindromes."""
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("a") == "a"


def test_find_max_negative_numbers():
    """Test find_max with all negative numbers."""
    assert find_max([-1, -5, -3, -9, -2]) == -1


def test_find_max_duplicate_max():
    """Test find_max when maximum value appears multiple times."""
    assert find_max([5, 3, 5, 1, 5]) == 5


if __name__ == "__main__":
    pytest.main([__file__])