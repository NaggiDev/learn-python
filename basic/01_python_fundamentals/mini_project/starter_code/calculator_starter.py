"""
Command-Line Calculator - Starter Code

This program implements a simple command-line calculator that can perform
basic arithmetic operations.

Usage:
    Run this script and follow the on-screen instructions to perform calculations.
"""


def add(a, b):
    """Add two numbers and return the result."""
    # TODO: Implement this function
    pass


def subtract(a, b):
    """Subtract b from a and return the result."""
    # TODO: Implement this function
    pass


def multiply(a, b):
    """Multiply two numbers and return the result."""
    # TODO: Implement this function
    pass


def divide(a, b):
    """Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    # TODO: Implement this function
    # Remember to handle division by zero
    pass


def power(a, b):
    """Raise a to the power of b and return the result."""
    # TODO: Implement this function
    pass


def modulus(a, b):
    """Return the remainder of a divided by b.
    
    Raises:
        ValueError: If b is zero
    """
    # TODO: Implement this function
    # Remember to handle modulus by zero
    pass


def get_number_input(prompt):
    """Get numeric input from the user.
    
    Args:
        prompt: The message to display to the user
        
    Returns:
        A number (float)
        
    Raises:
        ValueError: If the input cannot be converted to a float
    """
    # TODO: Implement this function
    # Make sure to handle invalid input
    pass


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


def main():
    """Main function to run the calculator program."""
    history = []
    memory = 0
    
    print("Welcome to the Python Calculator!")
    print("This calculator allows you to perform basic arithmetic operations.")
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-9): ")
        
        # TODO: Implement the calculator logic based on user choice
        # Remember to:
        # - Handle invalid choices
        # - Get appropriate inputs for the selected operation
        # - Call the appropriate function
        # - Display the result
        # - Add the calculation to history
        # - Implement memory functions (store/recall)
        # - Allow the user to exit the program
        
        # Example structure (you need to complete this):
        if choice == '0':
            print("Thank you for using the Python Calculator. Goodbye!")
            break
        # elif choice == '1':
        #     # Handle addition
        #     ...
        # elif ...
        #     ...
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()