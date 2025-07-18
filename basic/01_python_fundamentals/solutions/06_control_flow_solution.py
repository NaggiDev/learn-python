"""
Solution: Working with Control Flow

This file contains the solution to the control flow exercise.
"""

def main():
    print("=" * 50)
    print("CONTROL FLOW EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Basic Conditionals
    # ========================================
    print("\n--- Task 1: Basic Conditionals ---")
    
    def describe_temperature(temp):
        """
        Returns a description of the temperature.
        """
        if temp < 0:
            return "Freezing"
        elif temp <= 10:  # 0-10
            return "Cold"
        elif temp <= 20:  # 11-20
            return "Cool"
        elif temp <= 30:  # 21-30
            return "Warm"
        else:  # > 30
            return "Hot"
    
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
    
    def filter_even_numbers(numbers):
        """
        Returns a list containing only the even numbers from the input list.
        """
        even_numbers = []
        for num in numbers:
            if num % 2 == 0:
                even_numbers.append(num)
        return even_numbers
    
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
    
    def sum_of_digits(number):
        """
        Calculates the sum of digits for a given number.
        """
        total = 0
        # Convert to positive if negative
        number = abs(number)
        
        while number > 0:
            digit = number % 10  # Get the last digit
            total += digit
            number //= 10  # Remove the last digit
        
        return total
    
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
    
    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        
        return True
    
    def find_next_prime(number):
        """
        Finds the first prime number greater than the given number.
        """
        # Start checking from the next number
        candidate = number + 1
        
        while True:
            if is_prime(candidate):
                return candidate
            candidate += 1
    
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
    
    def multiplication_table(n):
        """
        Generates a multiplication table for numbers 1 to n.
        Returns a list of lists, where each inner list represents a row.
        """
        table = []
        for i in range(1, n + 1):
            row = []
            for j in range(1, n + 1):
                row.append(i * j)
            table.append(row)
        return table
    
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
    
    def fizzbuzz(n):
        """
        Implements the FizzBuzz game for numbers 1 to n.
        """
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(i)
        return result
    
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
    
    def validate_password(password):
        """
        Validates a password based on multiple rules.
        Returns a list of failed rules (empty list if all rules pass).
        """
        failed_rules = []
        
        # Rule 1: At least 8 characters long
        if len(password) < 8:
            failed_rules.append("At least 8 characters long")
        
        # Rule 2: Contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            failed_rules.append("Contains at least one uppercase letter")
        
        # Rule 3: Contains at least one lowercase letter
        if not any(char.islower() for char in password):
            failed_rules.append("Contains at least one lowercase letter")
        
        # Rule 4: Contains at least one digit
        if not any(char.isdigit() for char in password):
            failed_rules.append("Contains at least one digit")
        
        # Rule 5: Contains at least one special character
        special_chars = "!@#$%^&*()"
        if not any(char in special_chars for char in password):
            failed_rules.append("Contains at least one special character from !@#$%^&*()")
        
        return failed_rules
    
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