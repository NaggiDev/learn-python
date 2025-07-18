"""
Exercise: Working with Control Flow

Instructions:
1. Complete the tasks in each section below
2. Run the script to check your work
3. Each task has a TODO comment indicating what you need to do
4. Some tasks have tests that will verify your solution

Learning objectives:
- Practice using if/else statements for decision making
- Use elif for multiple conditions
- Work with for loops to iterate over sequences
- Use while loops for condition-based iteration
- Apply loop control statements (break, continue)
- Combine conditionals and loops to solve problems
"""

def main():
    print("=" * 50)
    print("CONTROL FLOW EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Basic Conditionals
    # ========================================
    print("\n--- Task 1: Basic Conditionals ---")
    
    # TODO: Write a function that takes a temperature value and returns a description
    # If temp is below 0, return "Freezing"
    # If temp is 0-10, return "Cold"
    # If temp is 11-20, return "Cool"
    # If temp is 21-30, return "Warm"
    # If temp is above 30, return "Hot"
    def describe_temperature(temp):
        # Your code here
        pass
    
    # Test the function with different temperatures
    test_temps = [-5, 0, 5, 15, 25, 35]
    expected_results = ["Freezing", "Cold", "Cold", "Cool", "Warm", "Hot"]
    
    for i, temp in enumerate(test_temps):
        result = describe_temperature(temp)
        expected = expected_results[i]
        print(f"Temperature {temp}°C is described as: {result}")
        assert result == expected, f"For {temp}°C, expected '{expected}', got '{result}'"
    
    print("Temperature description function is working correctly!")
    
    # ========================================
    # Task 2: For Loops
    # ========================================
    print("\n--- Task 2: For Loops ---")
    
    # TODO: Write a function that takes a list of numbers and returns a new list
    # containing only the even numbers from the original list
    def filter_even_numbers(numbers):
        # Your code here
        pass
    
    # Test the function with different lists
    test_lists = [
        [1, 2, 3, 4, 5, 6],
        [7, 9, 11, 13],
        [2, 4, 6, 8],
        []
    ]
    expected_results = [
        [2, 4, 6],
        [],
        [2, 4, 6, 8],
        []
    ]
    
    for i, numbers in enumerate(test_lists):
        result = filter_even_numbers(numbers)
        expected = expected_results[i]
        print(f"Even numbers in {numbers}: {result}")
        assert result == expected, f"For {numbers}, expected {expected}, got {result}"
    
    print("Even number filter function is working correctly!")
    
    # ========================================
    # Task 3: While Loops
    # ========================================
    print("\n--- Task 3: While Loops ---")
    
    # TODO: Write a function that calculates the sum of digits for a given number
    # For example, sum_of_digits(123) should return 6 (1+2+3)
    def sum_of_digits(number):
        # Your code here
        pass
    
    # Test the function with different numbers
    test_numbers = [123, 9, 987654, 0, 111]
    expected_results = [6, 9, 39, 0, 3]
    
    for i, number in enumerate(test_numbers):
        result = sum_of_digits(number)
        expected = expected_results[i]
        print(f"Sum of digits for {number}: {result}")
        assert result == expected, f"For {number}, expected {expected}, got {result}"
    
    print("Sum of digits function is working correctly!")
    
    # ========================================
    # Task 4: Loop Control Statements
    # ========================================
    print("\n--- Task 4: Loop Control Statements ---")
    
    # TODO: Write a function that finds the first prime number greater than a given number
    # A prime number is only divisible by 1 and itself
    def find_next_prime(number):
        # Your code here
        pass
    
    # Test the function with different numbers
    test_numbers = [10, 20, 97, 13, 1]
    expected_results = [11, 23, 101, 17, 2]
    
    for i, number in enumerate(test_numbers):
        result = find_next_prime(number)
        expected = expected_results[i]
        print(f"Next prime after {number}: {result}")
        assert result == expected, f"For {number}, expected {expected}, got {result}"
    
    print("Next prime function is working correctly!")
    
    # ========================================
    # Task 5: Nested Loops
    # ========================================
    print("\n--- Task 5: Nested Loops ---")
    
    # TODO: Write a function that generates a multiplication table for numbers 1 to n
    # The function should return a list of lists, where each inner list represents a row
    # For example, multiplication_table(3) should return:
    # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    def multiplication_table(n):
        # Your code here
        pass
    
    # Test the function with different values of n
    test_ns = [3, 1, 5]
    expected_results = [
        [[1, 2, 3], [2, 4, 6], [3, 6, 9]],
        [[1]],
        [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
    ]
    
    for i, n in enumerate(test_ns):
        result = multiplication_table(n)
        expected = expected_results[i]
        print(f"Multiplication table for n={n}:")
        for row in result:
            print(row)
        assert result == expected, f"For n={n}, expected {expected}, got {result}"
    
    print("Multiplication table function is working correctly!")
    
    # ========================================
    # Task 6: Combining Conditionals and Loops
    # ========================================
    print("\n--- Task 6: Combining Conditionals and Loops ---")
    
    # TODO: Write a function that implements the FizzBuzz game
    # For numbers 1 to n:
    # - If the number is divisible by 3, add "Fizz" to the result list
    # - If the number is divisible by 5, add "Buzz" to the result list
    # - If the number is divisible by both 3 and 5, add "FizzBuzz" to the result list
    # - Otherwise, add the number itself to the result list
    def fizzbuzz(n):
        # Your code here
        pass
    
    # Test the function with different values of n
    test_ns = [15, 5, 3]
    expected_results = [
        [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"],
        [1, 2, "Fizz", 4, "Buzz"],
        [1, 2, "Fizz"]
    ]
    
    for i, n in enumerate(test_ns):
        result = fizzbuzz(n)
        expected = expected_results[i]
        print(f"FizzBuzz for n={n}: {result}")
        assert result == expected, f"For n={n}, expected {expected}, got {result}"
    
    print("FizzBuzz function is working correctly!")
    
    # ========================================
    # Task 7: Challenge - Password Validator
    # ========================================
    print("\n--- Task 7: Challenge - Password Validator ---")
    
    # TODO: Write a function that validates a password based on the following rules:
    # 1. At least 8 characters long
    # 2. Contains at least one uppercase letter
    # 3. Contains at least one lowercase letter
    # 4. Contains at least one digit
    # 5. Contains at least one special character from !@#$%^&*()
    # The function should return a list of failed rules (empty list if all rules pass)
    def validate_password(password):
        # Your code here
        pass
    
    # Test the function with different passwords
    test_passwords = [
        "Abc123!@",  # Valid
        "abc123!@",  # No uppercase
        "ABC123!@",  # No lowercase
        "AbcDef!@",  # No digit
        "Abcd1234",  # No special character
        "Ab1!",      # Too short
        "Ab1!@Cd2"   # Valid
    ]
    expected_results = [
        [],
        ["Contains at least one uppercase letter"],
        ["Contains at least one lowercase letter"],
        ["Contains at least one digit"],
        ["Contains at least one special character from !@#$%^&*()"],
        ["At least 8 characters long"],
        []
    ]
    
    for i, password in enumerate(test_passwords):
        result = validate_password(password)
        expected = expected_results[i]
        if result:
            print(f"Password '{password}' failed validation: {result}")
        else:
            print(f"Password '{password}' is valid")
        assert result == expected, f"For '{password}', expected {expected}, got {result}"
    
    print("Password validator function is working correctly!")
    
    print("\nCongratulations! You've completed the control flow exercise.")

if __name__ == "__main__":
    main()