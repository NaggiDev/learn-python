"""
Solution: Type Conversion in Python

This file contains the solution to the type conversion exercise.
"""

import math

def main():
    print("=" * 50)
    print("TYPE CONVERSION EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Basic Type Conversions
    # ========================================
    print("\n--- Task 1: Basic Type Conversions ---")
    
    # Convert between different types
    num_from_str = int("42")
    str_from_num = str(42)
    float_from_str = float("3.14")
    int_from_float = int(3.14)
    
    # Print the results and their types
    print(f"String '42' to integer: {num_from_str}, type: {type(num_from_str)}")
    print(f"Integer 42 to string: '{str_from_num}', type: {type(str_from_num)}")
    print(f"String '3.14' to float: {float_from_str}, type: {type(float_from_str)}")
    print(f"Float 3.14 to integer: {int_from_float}, type: {type(int_from_float)}")
    
    # Test the conversions
    assert num_from_str == 42, f"Expected 42, got {num_from_str}"
    assert str_from_num == "42", f"Expected '42', got '{str_from_num}'"
    assert float_from_str == 3.14, f"Expected 3.14, got {float_from_str}"
    assert int_from_float == 3, f"Expected 3, got {int_from_float}"
    print("All basic conversions are correct!")
    
    # ========================================
    # Task 2: Boolean Conversions
    # ========================================
    print("\n--- Task 2: Boolean Conversions ---")
    
    # Convert values to booleans
    bool_from_zero = bool(0)
    bool_from_num = bool(42)
    bool_from_empty_str = bool("")
    bool_from_hello = bool("Hello")
    bool_from_empty_list = bool([])
    bool_from_zero_float = bool(0.0)
    
    # Print the results
    print(f"bool(0): {bool_from_zero}")
    print(f"bool(42): {bool_from_num}")
    print(f"bool(''): {bool_from_empty_str}")
    print(f"bool('Hello'): {bool_from_hello}")
    print(f"bool([]): {bool_from_empty_list}")
    print(f"bool(0.0): {bool_from_zero_float}")
    
    # Test the boolean conversions
    assert bool_from_zero == False, f"Expected False, got {bool_from_zero}"
    assert bool_from_num == True, f"Expected True, got {bool_from_num}"
    assert bool_from_empty_str == False, f"Expected False, got {bool_from_empty_str}"
    assert bool_from_hello == True, f"Expected True, got {bool_from_hello}"
    assert bool_from_empty_list == False, f"Expected False, got {bool_from_empty_list}"
    assert bool_from_zero_float == False, f"Expected False, got {bool_from_zero_float}"
    print("All boolean conversions are correct!")
    
    # ========================================
    # Task 3: Handling Conversion Errors
    # ========================================
    print("\n--- Task 3: Handling Conversion Errors ---")
    
    def convert_to_int(input_string):
        try:
            return int(input_string)
        except ValueError:
            return "Conversion failed"
    
    # Test the function with different inputs
    test_cases = ["42", "3.14", "hello", "42hello"]
    for test in test_cases:
        result = convert_to_int(test)
        print(f"convert_to_int('{test}') = {result}, type: {type(result)}")
    
    # Test the function behavior
    assert convert_to_int("42") == 42, f"Expected 42, got {convert_to_int('42')}"
    assert convert_to_int("hello") == "Conversion failed", f"Expected 'Conversion failed', got {convert_to_int('hello')}"
    print("Conversion error handling is correct!")
    
    # ========================================
    # Task 4: Practical Application - User Input
    # ========================================
    print("\n--- Task 4: Practical Application - User Input ---")
    
    def calculate_area(radius_str):
        try:
            radius = float(radius_str)
            if radius < 0:
                return "Invalid input"
            area = math.pi * radius ** 2
            return round(area, 2)
        except ValueError:
            return "Invalid input"
    
    # For testing purposes, we'll use predefined inputs instead of actual user input
    test_radii = ["5", "2.5", "-1", "hello"]
    for radius in test_radii:
        area = calculate_area(radius)
        print(f"Area of circle with radius '{radius}': {area}")
    
    # Test the function behavior
    assert calculate_area("5") == 78.54, f"Expected 78.54, got {calculate_area('5')}"
    assert calculate_area("2.5") == 19.63, f"Expected 19.63, got {calculate_area('2.5')}"
    assert calculate_area("-1") == "Invalid input", f"Expected 'Invalid input', got {calculate_area('-1')}"
    assert calculate_area("hello") == "Invalid input", f"Expected 'Invalid input', got {calculate_area('hello')}"
    print("Area calculation function works correctly!")
    
    # ========================================
    # Task 5: Challenge - Complex Type Conversions
    # ========================================
    print("\n--- Task 5: Challenge - Complex Type Conversions ---")
    
    def process_data(string_list):
        result = []
        for item in string_list:
            try:
                # Try to convert to int first
                num = int(item)
                result.append(num)
            except ValueError:
                try:
                    # If int conversion fails, try float
                    num = float(item)
                    result.append(num)
                except ValueError:
                    # If both conversions fail, skip this item
                    pass
        return result
    
    # Test the function
    test_data = ["42", "3.14", "hello", "99.9", "0", "-5"]
    processed = process_data(test_data)
    print(f"Original data: {test_data}")
    print(f"Processed data: {processed}")
    
    # Test the function behavior
    expected = [42, 3.14, 99.9, 0, -5]
    assert processed == expected, f"Expected {expected}, got {processed}"
    print("Data processing function works correctly!")
    
    print("\nCongratulations! You've completed the type conversion exercise.")

if __name__ == "__main__":
    main()