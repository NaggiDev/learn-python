"""
Solution: Working with Variables and Data Types

This file contains the solution to the variables and data types exercise.
"""

def main():
    print("=" * 50)
    print("VARIABLES AND DATA TYPES EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Create variables of different types
    # ========================================
    print("\n--- Task 1: Creating Variables ---")
    
    # Create variables of different types
    age = 25
    height = 1.75
    name = "John Doe"
    is_python_fun = True
    
    # Print the variables and their types
    print(f"Variable 'age' has value: {age} and type: {type(age)}")
    print(f"Variable 'height' has value: {height} and type: {type(height)}")
    print(f"Variable 'name' has value: {name} and type: {type(name)}")
    print(f"Variable 'is_python_fun' has value: {is_python_fun} and type: {type(is_python_fun)}")
    
    # ========================================
    # Task 2: Basic operations with numbers
    # ========================================
    print("\n--- Task 2: Basic Operations with Numbers ---")
    
    # Create two number variables
    num1 = 10
    num2 = 3
    
    # Calculate various operations
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    division_result = num1 / num2
    floor_division_result = num1 // num2
    modulus_result = num1 % num2
    power_result = num1 ** num2
    
    # Print the results
    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference_result}")
    print(f"Product: {num1} * {num2} = {product_result}")
    print(f"Division: {num1} / {num2} = {division_result}")
    print(f"Floor Division: {num1} // {num2} = {floor_division_result}")
    print(f"Modulus: {num1} % {num2} = {modulus_result}")
    print(f"Power: {num1} ** {num2} = {power_result}")
    
    # Test the calculations
    assert sum_result == 13, f"Expected sum to be 13, got {sum_result}"
    assert difference_result == 7, f"Expected difference to be 7, got {difference_result}"
    assert product_result == 30, f"Expected product to be 30, got {product_result}"
    assert division_result == 3.3333333333333335, f"Expected division to be approximately 3.33, got {division_result}"
    assert floor_division_result == 3, f"Expected floor division to be 3, got {floor_division_result}"
    assert modulus_result == 1, f"Expected modulus to be 1, got {modulus_result}"
    assert power_result == 1000, f"Expected power to be 1000, got {power_result}"
    print("All number operations are correct!")
    
    # ========================================
    # Task 3: String operations
    # ========================================
    print("\n--- Task 3: String Operations ---")
    
    # Create a string variable
    greeting = "Hello, World!"
    
    # Perform string operations
    first_five = greeting[:5]
    last_five = greeting[-5:]
    all_caps = greeting.upper()
    replacement = greeting.replace("Hello", "Goodbye")
    repetition = "Python! " * 3
    
    # Print the results
    print(f"Original greeting: {greeting}")
    print(f"First 5 characters: {first_five}")
    print(f"Last 5 characters: {last_five}")
    print(f"All caps: {all_caps}")
    print(f"Replacement: {replacement}")
    print(f"Repetition: {repetition}")
    
    # Test the string operations
    assert first_five == "Hello", f"Expected 'Hello', got '{first_five}'"
    assert last_five == "orld!", f"Expected 'orld!', got '{last_five}'"
    assert all_caps == "HELLO, WORLD!", f"Expected 'HELLO, WORLD!', got '{all_caps}'"
    assert replacement == "Goodbye, World!", f"Expected 'Goodbye, World!', got '{replacement}'"
    assert repetition == "Python! Python! Python! ", f"Expected 'Python! Python! Python! ', got '{repetition}'"
    print("All string operations are correct!")
    
    # ========================================
    # Task 4: String formatting
    # ========================================
    print("\n--- Task 4: String Formatting ---")
    
    # Create variables for a person
    person_name = "Alice"
    person_age = 25
    language = "Python"
    
    # Create formatted strings using different methods
    concat_format = "Hello, my name is " + person_name + ", I'm " + str(person_age) + " years old, and my favorite programming language is " + language + "."
    format_method = "Hello, my name is {}, I'm {} years old, and my favorite programming language is {}.".format(person_name, person_age, language)
    f_string = f"Hello, my name is {person_name}, I'm {person_age} years old, and my favorite programming language is {language}."
    
    # Print the formatted strings
    print("Using concatenation:", concat_format)
    print("Using .format():", format_method)
    print("Using f-string:", f_string)
    
    # ========================================
    # Task 5: Working with None and Boolean values
    # ========================================
    print("\n--- Task 5: None and Boolean Values ---")
    
    # Create a None variable
    empty_value = None
    
    # Create boolean variables based on conditions
    is_adult = age >= 18
    is_tall = height > 1.75
    has_long_name = len(name) > 6
    
    # Print the results
    print(f"empty_value: {empty_value}, type: {type(empty_value)}")
    print(f"Is adult? {is_adult}")
    print(f"Is tall? {is_tall}")
    print(f"Has long name? {has_long_name}")
    
    # ========================================
    # Task 6: Challenge - Complex Expression
    # ========================================
    print("\n--- Task 6: Challenge - Complex Expression ---")
    
    # Calculate the complex expression
    complex_result = ((num1 + num2) * 2 - 5) / 2.5
    
    # Print the result
    print(f"Result of ((num1 + num2) * 2 - 5) / 2.5 = {complex_result}")
    
    # Test the result
    expected_result = ((num1 + num2) * 2 - 5) / 2.5
    assert complex_result == expected_result, f"Expected {expected_result}, got {complex_result}"
    print("Complex expression calculated correctly!")
    
    print("\nCongratulations! You've completed the variables and data types exercise.")

if __name__ == "__main__":
    main()