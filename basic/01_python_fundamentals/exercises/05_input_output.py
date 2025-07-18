"""
Exercise: Working with Input and Output Operations

Instructions:
1. Complete the tasks in each section below
2. Run the script to check your work
3. Each task has a TODO comment indicating what you need to do
4. Some tasks have tests that will verify your solution

Learning objectives:
- Practice getting user input with input()
- Convert input to appropriate data types
- Use different print() function features
- Apply various string formatting techniques
"""

def main():
    print("=" * 50)
    print("INPUT/OUTPUT OPERATIONS EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Basic Input and Output
    # ========================================
    print("\n--- Task 1: Basic Input and Output ---")
    
    # NOTE: For testing purposes, we'll simulate user input
    # In a real program, you would use input() without these overrides
    
    # This is just for the automated testing - you can ignore this part
    global input_values
    input_values = ["John Doe", "25", "New York", "Python"]
    global input_index
    input_index = 0
    
    def mock_input(prompt=""):
        global input_index
        print(prompt + input_values[input_index])  # Print the prompt and simulated input
        value = input_values[input_index]
        input_index += 1
        return value
    
    # Replace the built-in input function with our mock version
    original_input = __builtins__.input
    __builtins__.input = mock_input
    
    # TODO: Write code to ask for the user's name and store it in a variable called 'name'
    
    
    # TODO: Write code to greet the user using their name
    
    
    # TODO: Ask for the user's age as a string, then convert it to an integer and store in 'age'
    
    
    # TODO: Print a message telling the user how old they will be in 10 years
    
    
    # Test the basic input/output
    assert name == "John Doe", f"Expected name to be 'John Doe', got '{name}'"
    assert age == 25, f"Expected age to be 25, got {age}"
    print("Basic input and output working correctly!")
    
    # ========================================
    # Task 2: Print Function Features
    # ========================================
    print("\n--- Task 2: Print Function Features ---")
    
    # TODO: Ask for the user's city and favorite programming language
    
    
    
    # TODO: Print the user's name, age, city, and favorite language on separate lines
    
    
    # TODO: Print the same information on a single line with commas between each piece of information
    
    
    # TODO: Print the same information with custom separators: " | " between items and no newline at the end
    
    
    # Test the print function features
    assert city == "New York", f"Expected city to be 'New York', got '{city}'"
    assert language == "Python", f"Expected language to be 'Python', got '{language}'"
    print("\nPrint function features working correctly!")
    
    # ========================================
    # Task 3: String Formatting
    # ========================================
    print("\n--- Task 3: String Formatting ---")
    
    # TODO: Create a formatted string using the % operator that includes the user's name and age
    # Format: "User Profile: Name - [name], Age - [age]"
    old_style_format = ""
    
    
    # TODO: Create the same formatted string using the format() method
    format_method = ""
    
    
    # TODO: Create the same formatted string using f-strings (Python 3.6+)
    f_string_format = ""
    
    
    # Print all three formatted strings
    print(old_style_format)
    print(format_method)
    print(f_string_format)
    
    # Test the string formatting
    expected = "User Profile: Name - John Doe, Age - 25"
    assert old_style_format == expected, f"Expected old style format to be '{expected}', got '{old_style_format}'"
    assert format_method == expected, f"Expected format method to be '{expected}', got '{format_method}'"
    assert f_string_format == expected, f"Expected f-string format to be '{expected}', got '{f_string_format}'"
    print("String formatting working correctly!")
    
    # ========================================
    # Task 4: Advanced String Formatting
    # ========================================
    print("\n--- Task 4: Advanced String Formatting ---")
    
    # Sample data for formatting
    pi = 3.14159265359
    large_number = 1000000
    percentage = 0.75
    items = ["apple", "banana", "cherry"]
    
    # TODO: Format pi to show only 3 decimal places using f-strings
    formatted_pi = ""
    
    
    # TODO: Format large_number to include commas as thousand separators using f-strings
    formatted_large_number = ""
    
    
    # TODO: Format percentage as a percentage with 1 decimal place using f-strings
    formatted_percentage = ""
    
    
    # TODO: Create a formatted table header and row for the items list
    # The header should be "Item | Length" with a line of dashes below
    # Each row should show the item name and its length, properly aligned
    table_header = ""
    separator_line = ""
    table_rows = []
    
    
    
    
    # Print the formatted values
    print(f"Formatted pi: {formatted_pi}")
    print(f"Formatted large number: {formatted_large_number}")
    print(f"Formatted percentage: {formatted_percentage}")
    print("\nFormatted table:")
    print(table_header)
    print(separator_line)
    for row in table_rows:
        print(row)
    
    # Test the advanced formatting
    assert formatted_pi == "3.142", f"Expected formatted pi to be '3.142', got '{formatted_pi}'"
    assert formatted_large_number == "1,000,000", f"Expected formatted large number to be '1,000,000', got '{formatted_large_number}'"
    assert formatted_percentage == "75.0%", f"Expected formatted percentage to be '75.0%', got '{formatted_percentage}'"
    assert table_header == "Item     | Length", f"Expected table header to be 'Item     | Length', got '{table_header}'"
    assert separator_line == "--------|-------", f"Expected separator line to be '--------|-------', got '{separator_line}'"
    assert len(table_rows) == 3, f"Expected 3 table rows, got {len(table_rows)}"
    print("Advanced string formatting working correctly!")
    
    # ========================================
    # Task 5: Input Validation
    # ========================================
    print("\n--- Task 5: Input Validation ---")
    
    # For this task, we'll restore the original input function and provide test cases
    __builtins__.input = original_input
    
    def validate_age(age_str):
        """
        Validates if the input string is a valid age (positive integer less than 120)
        Returns the age as an integer if valid, or None if invalid
        """
        # TODO: Implement the validation function
        # 1. Try to convert age_str to an integer
        # 2. Check if the age is between 0 and 120
        # 3. Return the age as an integer if valid, or None if invalid
        
        
        
        
        
        
    
    # Test the validation function with various inputs
    test_cases = [
        ("25", 25),
        ("0", 0),
        ("120", 120),
        ("-5", None),
        ("150", None),
        ("abc", None),
        ("18.5", None)
    ]
    
    for input_str, expected_result in test_cases:
        result = validate_age(input_str)
        if result == expected_result:
            print(f"✓ validate_age('{input_str}') returned {result}")
        else:
            print(f"✗ validate_age('{input_str}') returned {result}, expected {expected_result}")
            assert result == expected_result, f"validate_age('{input_str}') failed"
    
    print("Input validation working correctly!")
    
    # ========================================
    # Task 6: Challenge - Interactive Form
    # ========================================
    print("\n--- Task 6: Challenge - Interactive Form ---")
    
    # For this challenge, we'll simulate user input again
    input_values = ["Jane Smith", "30", "Software Engineer", "42000", "y"]
    input_index = 0
    __builtins__.input = mock_input
    
    def collect_user_data():
        """
        Collects and validates user data for a simple form
        Returns a dictionary with the user's information
        """
        # TODO: Implement the function to collect and validate the following user data:
        # - full_name: non-empty string
        # - age: integer between 18 and 100
        # - occupation: non-empty string
        # - salary: positive number
        # - confirm: 'y' or 'n'
        # 
        # Return the data as a dictionary
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    # Collect the user data
    user_data = collect_user_data()
    
    # TODO: Create a formatted summary of the user data using f-strings
    # The summary should be a multi-line string with each piece of information on its own line
    user_summary = ""
    
    
    
    
    
    
    # Print the user summary
    print("\nUser Information Summary:")
    print(user_summary)
    
    # Test the user data collection and summary
    expected_data = {
        "full_name": "Jane Smith",
        "age": 30,
        "occupation": "Software Engineer",
        "salary": 42000,
        "confirm": "y"
    }
    
    for key, value in expected_data.items():
        assert key in user_data, f"Missing key '{key}' in user_data"
        assert user_data[key] == value, f"Expected user_data['{key}'] to be {value}, got {user_data[key]}"
    
    assert "Jane Smith" in user_summary, "User summary should contain the user's name"
    assert "30" in user_summary, "User summary should contain the user's age"
    assert "Software Engineer" in user_summary, "User summary should contain the user's occupation"
    assert "42000" in user_summary, "User summary should contain the user's salary"
    
    print("Interactive form challenge completed successfully!")
    
    # Restore the original input function
    __builtins__.input = original_input
    
    print("\nCongratulations! You've completed the input/output operations exercise.")

if __name__ == "__main__":
    main()