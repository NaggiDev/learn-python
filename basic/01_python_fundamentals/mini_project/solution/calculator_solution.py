"""
Command-Line Calculator - Solution

This program implements a simple command-line calculator that can perform
basic arithmetic operations.

Usage:
    Run this script and follow the on-screen instructions to perform calculations.
"""


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b and return the result."""
    return a ** b


def modulus(a, b):
    """Return the remainder of a divided by b.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot perform modulus by zero")
    return a % b


def get_number_input(prompt):
    """Get numeric input from the user.
    
    Args:
        prompt: The message to display to the user
        
    Returns:
        A number (float)
        
    Raises:
        ValueError: If the input cannot be converted to a float
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def format_calculation(operation, a, b, result):
    """Format a calculation for display and history.
    
    Args:
        operation: String representing the operation (e.g., "+", "-")
        a: First operand
        b: Second operand
        result: Result of the operation
        
    Returns:
        A formatted string representing the calculation
    """
    return f"{a} {operation} {b} = {result}"


def display_menu():
    """Display the calculator menu options."""
    print("\n==== Python Calculator ====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulus (%)")
    print("7. View calculation history")
    print("8. Clear calculation history")
    print("9. Memory functions")
    print("0. Exit")
    print("=========================")


def display_memory_menu():
    """Display the memory function menu options."""
    print("\n==== Memory Functions ====")
    print("1. Store current result in memory")
    print("2. Recall value from memory")
    print("3. Clear memory")
    print("0. Return to main menu")
    print("=========================")


def main():
    """Main function to run the calculator program."""
    history = []
    memory = 0
    current_result = None
    
    print("Welcome to the Python Calculator!")
    print("This calculator allows you to perform basic arithmetic operations.")
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-9): ")
        
        if choice == '0':
            print("Thank you for using the Python Calculator. Goodbye!")
            break
            
        elif choice == '1':  # Addition
            try:
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = add(a, b)
                calc = format_calculation("+", a, b, result)
                print(calc)
                history.append(calc)
                current_result = result
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '2':  # Subtraction
            try:
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = subtract(a, b)
                calc = format_calculation("-", a, b, result)
                print(calc)
                history.append(calc)
                current_result = result
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '3':  # Multiplication
            try:
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = multiply(a, b)
                calc = format_calculation("*", a, b, result)
                print(calc)
                history.append(calc)
                current_result = result
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '4':  # Division
            try:
                a = get_number_input("Enter first number: ")
                b = get_number_input("Enter second number: ")
                result = divide(a, b)
                calc = format_calculation("/", a, b, result)
                print(calc)
                history.append(calc)
                current_result = result
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '5':  # Exponentiation
            try:
                a = get_number_input("Enter base: ")
                b = get_number_input("Enter exponent: ")
                result = power(a, b)
                calc = format_calculation("**", a, b, result)
                print(calc)
                history.append(calc)
                current_result = result
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '6':  # Modulus
            try:
                a = get_number_input("Enter dividend: ")
                b = get_number_input("Enter divisor: ")
                result = modulus(a, b)
                calc = format_calculation("%", a, b, result)
                print(calc)
                history.append(calc)
                current_result = result
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '7':  # View history
            if not history:
                print("No calculations in history.")
            else:
                print("\nCalculation History:")
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")
                    
        elif choice == '8':  # Clear history
            history = []
            print("Calculation history cleared.")
            
        elif choice == '9':  # Memory functions
            while True:
                display_memory_menu()
                memory_choice = input("Enter your choice (0-3): ")
                
                if memory_choice == '0':
                    break
                    
                elif memory_choice == '1':  # Store in memory
                    if current_result is not None:
                        memory = current_result
                        print(f"Stored {memory} in memory.")
                    else:
                        print("No result to store. Perform a calculation first.")
                        
                elif memory_choice == '2':  # Recall from memory
                    print(f"Memory: {memory}")
                    
                elif memory_choice == '3':  # Clear memory
                    memory = 0
                    print("Memory cleared.")
                    
                else:
                    print("Invalid choice. Please try again.")
                    
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()