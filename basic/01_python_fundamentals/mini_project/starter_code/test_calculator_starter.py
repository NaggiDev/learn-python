"""
Tests for the command-line calculator functions.

Run these tests using:
    python test_calculator_starter.py
"""

import unittest
from calculator_starter import add, subtract, multiply, divide, power, modulus


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test the add function with various inputs."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.5, 3.5), 6.0)
    
    def test_subtract(self):
        """Test the subtract function with various inputs."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(5.5, 2.5), 3.0)
    
    def test_multiply(self):
        """Test the multiply function with various inputs."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 2), 5.0)
    
    def test_divide(self):
        """Test the divide function with various inputs."""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(0, 5), 0)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power(self):
        """Test the power function with various inputs."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(2, -1), 0.5)
    
    def test_modulus(self):
        """Test the modulus function with various inputs."""
        self.assertEqual(modulus(7, 3), 1)
        self.assertEqual(modulus(5, 5), 0)
        self.assertEqual(modulus(0, 5), 0)
        
        # Test modulus by zero
        with self.assertRaises(ValueError):
            modulus(5, 0)


if __name__ == "__main__":
    unittest.main()