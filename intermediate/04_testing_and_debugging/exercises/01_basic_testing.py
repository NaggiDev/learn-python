"""
Exercise 1: Basic Unit Testing with pytest

In this exercise, you'll practice writing basic unit tests for simple functions.
Complete the test functions below to test the provided functions.

Instructions:
1. Install pytest: pip install pytest
2. Complete the test functions marked with TODO
3. Run the tests: pytest 01_basic_testing.py
4. All tests should pass when implemented correctly
"""

import pytest


# Functions to test
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


# Test functions - Complete these
def test_is_even_with_even_number():
    """Test is_even function with an even number."""
    # TODO: Test that is_even(4) returns True
    pass


def test_is_even_with_odd_number():
    """Test is_even function with an odd number."""
    # TODO: Test that is_even(3) returns False
    pass


def test_is_even_with_zero():
    """Test is_even function with zero."""
    # TODO: Test that is_even(0) returns True (zero is even)
    pass


def test_get_grade_a():
    """Test get_grade function for A grade."""
    # TODO: Test that get_grade(95) returns 'A'
    pass


def test_get_grade_b():
    """Test get_grade function for B grade."""
    # TODO: Test that get_grade(85) returns 'B'
    pass


def test_get_grade_f():
    """Test get_grade function for F grade."""
    # TODO: Test that get_grade(45) returns 'F'
    pass


def test_reverse_string_normal():
    """Test reverse_string with a normal string."""
    # TODO: Test that reverse_string("hello") returns "olleh"
    pass


def test_reverse_string_empty():
    """Test reverse_string with an empty string."""
    # TODO: Test that reverse_string("") returns ""
    pass


def test_find_max_normal_list():
    """Test find_max with a normal list of numbers."""
    # TODO: Test that find_max([1, 5, 3, 9, 2]) returns 9
    pass


def test_find_max_single_element():
    """Test find_max with a single element list."""
    # TODO: Test that find_max([42]) returns 42
    pass


def test_find_max_empty_list():
    """Test find_max with an empty list should raise ValueError."""
    # TODO: Test that find_max([]) raises ValueError
    # Hint: Use pytest.raises(ValueError)
    pass


if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main([__file__])