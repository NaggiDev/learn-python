"""
Exercise: Working with Variables and Data Types

Instructions:
1. Complete the tasks in each section below
2. Run the script to check your work
3. Each task has a TODO comment indicating what you need to do
4. Some tasks have tests that will verify your solution

Learning objectives:
- Create and use variables of different data types
- Understand basic operations with different data types
- Practice string formatting and manipulation
- Learn how to check and work with data types
"""

def main():
    print("=" * 50)
    print("VARIABLES AND DATA TYPES EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Create variables of different types
    # ========================================
    print("\n--- Task 1: Creating Variables ---")
    
    # TODO: Create an integer variable named 'age' with a value of your choice
    
    
    # TODO: Create a float variable named 'height' with a value of your choice (in meters)
    
    
    # TODO: Create a string variable named 'name' with your name as the value
    
    
    # TODO: Create a boolean variable named 'is_python_fun' and set it to True
    
    
    # Print the variables and their types
    print(f"Variable 'age' has value: {age} and type: {type(age)}")
    print(f"Variable 'height' has value: {height} and type: {type(height)}")
    print(f"Variable 'name' has value: {name} and type: {type(name)}")
    print(f"Variable 'is_python_fun' has value: {is_python_fun} and type: {type(is_python_fun)}")
    
    # ========================================
    # Task 2: Basic operations with numbers
    # ========================================
    print("\n--- Task 2: Basic Operations with Numbers ---")
    
    # TODO: Create two number variables: num1 and num2, with values 10 and 3
    
    
    # TODO: Calculate and store the following operations:
    # - sum_result: The sum of num1 and num2
    # - difference_result: The difference of num1 and num2
    # - product_result: The product of num1 and num2
    # - division_result: The division of num1 by num2
    # - floor_division_result: The floor division of num1 by num2
    # - modulus_result: The remainder when num1 is divided by num2
    # - power_result: num1 raised to the power of num2
    
    
    
    
    
    
    
    
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
    
    # TODO: Create a string variable 'greeting' with the value "Hello, World!"
    
    
    # TODO: Create the following variables using string operations:
    # - first_five: The first 5 characters of greeting
    # - last_five: The last 5 characters of greeting
    # - all_caps: The greeting in all uppercase
    # - replacement: Replace "Hello" with "Goodbye" in the greeting
    # - repetition: The string "Python! " repeated 3 times
    
    
    
    
    
    
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
    
    # TODO: Create variables for a person's name, age, and favorite programming language
    # person_name = "Alice"
    # person_age = 25
    # language = "Python"
    
    
    
    
    # TODO: Create formatted strings using different methods:
    # 1. Using string concatenation
    # 2. Using the .format() method
    # 3. Using f-strings (if using Python 3.6+)
    # Each should create a sentence like: "Hello, my name is Alice, I'm 25 years old, and my favorite programming language is Python."
    
    
    
    
    # Print the formatted strings
    print("Using concatenation:", concat_format)
    print("Using .format():", format_method)
    print("Using f-string:", f_string)
    
    # ========================================
    # Task 5: Working with None and Boolean values
    # ========================================
    print("\n--- Task 5: None and Boolean Values ---")
    
    # TODO: Create a variable 'empty_value' and set it to None
    
    
    # TODO: Create boolean variables for the following conditions:
    # - is_adult: Check if the age variable from Task 1 is greater than or equal to 18
    # - is_tall: Check if the height variable from Task 1 is greater than 1.75
    # - has_long_name: Check if the length of the name variable from Task 1 is greater than 6 characters
    
    
    
    
    # Print the results
    print(f"empty_value: {empty_value}, type: {type(empty_value)}")
    print(f"Is adult? {is_adult}")
    print(f"Is tall? {is_tall}")
    print(f"Has long name? {has_long_name}")
    
    # ========================================
    # Task 6: Challenge - Complex Expression
    # ========================================
    print("\n--- Task 6: Challenge - Complex Expression ---")
    
    # TODO: Calculate the result of this complex expression:
    # ((num1 + num2) * 2 - 5) / 2.5
    # Use the num1 and num2 variables from Task 2
    
    
    # Print the result
    print(f"Result of ((num1 + num2) * 2 - 5) / 2.5 = {complex_result}")
    
    # Test the result
    expected_result = ((num1 + num2) * 2 - 5) / 2.5
    assert complex_result == expected_result, f"Expected {expected_result}, got {complex_result}"
    print("Complex expression calculated correctly!")
    
    print("\nCongratulations! You've completed the variables and data types exercise.")

if __name__ == "__main__":
    main()