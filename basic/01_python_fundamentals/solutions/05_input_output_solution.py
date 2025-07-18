"""
Solution: Working with Input and Output Operations

This file contains the solution to the input/output operations exercise.
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
    
    # Ask for the user's name
    name = input("Please enter your name: ")
    
    # Greet the user
    print(f"Hello, {name}! Welcome to the Python learning path.")
    
    # Ask for the user's age and convert to integer
    age_str = input("Please enter your age: ")
    age = int(age_str)
    
    # Tell the user how old they will be in 10 years
    print(f"In 10 years, you will be {age + 10} years old.")
    
    # Test the basic input/output
    assert name == "John Doe", f"Expected name to be 'John Doe', got '{name}'"
    assert age == 25, f"Expected age to be 25, got {age}"
    print("Basic input and output working correctly!")
    
    # ========================================
    # Task 2: Print Function Features
    # ========================================
    print("\n--- Task 2: Print Function Features ---")
    
    # Ask for the user's city and favorite programming language
    city = input("What city do you live in? ")
    language = input("What is your favorite programming language? ")
    
    # Print information on separate lines
    print("User Information:")
    print(name)
    print(age)
    print(city)
    print(language)
    
    # Print information on a single line with commas
    print(name, age, city, language)
    
    # Print information with custom separators
    print(name, age, city, language, sep=" | ", end="")
    
    # Test the print function features
    assert city == "New York", f"Expected city to be 'New York', got '{city}'"
    assert language == "Python", f"Expected language to be 'Python', got '{language}'"
    print("\nPrint function features working correctly!")
    
    # ========================================
    # Task 3: String Formatting
    # ========================================
    print("\n--- Task 3: String Formatting ---")
    
    # Create formatted string using % operator
    old_style_format = "User Profile: Name - %s, Age - %d" % (name, age)
    
    # Create formatted string using format() method
    format_method = "User Profile: Name - {}, Age - {}".format(name, age)
    
    # Create formatted string using f-strings
    f_string_format = f"User Profile: Name - {name}, Age - {age}"
    
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
    
    # Format pi to show only 3 decimal places
    formatted_pi = f"{pi:.3f}"
    
    # Format large_number to include commas as thousand separators
    formatted_large_number = f"{large_number:,}"
    
    # Format percentage as a percentage with 1 decimal place
    formatted_percentage = f"{percentage:.1%}"
    
    # Create a formatted table
    table_header = "Item     | Length"
    separator_line = "--------|-------"
    table_rows = []
    
    for item in items:
        # Left-align item name in 8 characters, right-align length in 7 characters
        row = f"{item:<8}| {len(item):>7}"
        table_rows.append(row)
    
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
        try:
            # Try to convert to integer
            age = int(age_str)
            
            # Check if age is in valid range
            if 0 <= age <= 120:
                return age
            else:
                return None
        except ValueError:
            # Return None if conversion fails
            return None
    
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
        user_data = {}
        
        # Collect full name (non-empty string)
        while True:
            full_name = input("Enter your full name: ")
            if full_name.strip():  # Check if non-empty after stripping whitespace
                user_data["full_name"] = full_name
                break
            print("Name cannot be empty. Please try again.")
        
        # Collect age (integer between 18 and 100)
        while True:
            try:
                age = int(input("Enter your age (18-100): "))
                if 18 <= age <= 100:
                    user_data["age"] = age
                    break
                print("Age must be between 18 and 100. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Collect occupation (non-empty string)
        while True:
            occupation = input("Enter your occupation: ")
            if occupation.strip():
                user_data["occupation"] = occupation
                break
            print("Occupation cannot be empty. Please try again.")
        
        # Collect salary (positive number)
        while True:
            try:
                salary = float(input("Enter your annual salary: "))
                if salary >= 0:
                    user_data["salary"] = int(salary) if salary.is_integer() else salary
                    break
                print("Salary must be a positive number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Collect confirmation (y or n)
        while True:
            confirm = input("Confirm submission (y/n): ").lower()
            if confirm in ['y', 'n']:
                user_data["confirm"] = confirm
                break
            print("Please enter 'y' or 'n'.")
        
        return user_data
    
    # Collect the user data
    user_data = collect_user_data()
    
    # Create a formatted summary of the user data
    user_summary = f"""
Full Name: {user_data['full_name']}
Age: {user_data['age']}
Occupation: {user_data['occupation']}
Annual Salary: ${user_data['salary']:,.2f}
Submission Confirmed: {'Yes' if user_data['confirm'] == 'y' else 'No'}
"""
    
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