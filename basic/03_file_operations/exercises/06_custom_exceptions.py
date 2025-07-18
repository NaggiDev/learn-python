"""
Exercise: Custom Exceptions and Context Managers

Instructions:
1. Complete the classes and functions below according to their docstrings
2. Run the tests to verify your implementation

This exercise covers:
- Creating custom exception classes
- Implementing context managers
- Using try/except/else/finally blocks
"""

class InvalidAgeError(Exception):
    """
    Custom exception for invalid age values.
    """
    # TODO: Implement this class
    pass


class NegativeBalanceError(Exception):
    """
    Custom exception for negative account balance.
    """
    # TODO: Implement this class
    pass


def validate_age(age):
    """
    Validate that an age is reasonable (between 0 and 120).
    
    Args:
        age (int): Age to validate
        
    Returns:
        int: The validated age
        
    Raises:
        InvalidAgeError: If age is negative or unreasonably high
        TypeError: If age is not an integer
    """
    # TODO: Implement this function
    pass


class BankAccount:
    """
    Simple bank account class with custom exception handling.
    """
    
    def __init__(self, account_number, initial_balance=0):
        """
        Initialize a bank account.
        
        Args:
            account_number (str): Account number
            initial_balance (float): Initial balance
            
        Raises:
            NegativeBalanceError: If initial_balance is negative
        """
        # TODO: Implement this method
        pass
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            float: New balance
            
        Raises:
            ValueError: If amount is negative or zero
        """
        # TODO: Implement this method
        pass
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            float: New balance
            
        Raises:
            ValueError: If amount is negative or zero
            NegativeBalanceError: If withdrawal would result in negative balance
        """
        # TODO: Implement this method
        pass


class FileManager:
    """
    Context manager for file operations.
    """
    
    def __init__(self, filename, mode="r"):
        """
        Initialize the FileManager.
        
        Args:
            filename (str): Name of the file to open
            mode (str): Mode to open the file in
        """
        # TODO: Implement this method
        pass
    
    def __enter__(self):
        """
        Enter the context manager.
        
        Returns:
            file: The opened file object
            
        Raises:
            FileNotFoundError: If the file doesn't exist (in read mode)
        """
        # TODO: Implement this method
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context manager.
        
        Args:
            exc_type: Exception type if an exception was raised
            exc_val: Exception value if an exception was raised
            exc_tb: Exception traceback if an exception was raised
            
        Returns:
            bool: True if the exception should be suppressed, False otherwise
        """
        # TODO: Implement this method
        pass


def process_data_file(file_path):
    """
    Process a data file safely using a context manager.
    
    The file should contain one integer per line.
    Calculate the sum of all valid integers in the file.
    Skip lines that don't contain valid integers.
    
    Args:
        file_path (str): Path to the data file
        
    Returns:
        tuple: (sum of valid integers, count of valid integers, count of invalid lines)
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    # TODO: Implement this function
    pass


# Test functions
def test_custom_exceptions():
    # Test InvalidAgeError
    try:
        validate_age(-5)
        assert False, "Expected InvalidAgeError for negative age"
    except InvalidAgeError as e:
        assert "negative" in str(e).lower(), f"Expected error message to mention 'negative', got '{e}'"
    
    try:
        validate_age(150)
        assert False, "Expected InvalidAgeError for unreasonable age"
    except InvalidAgeError as e:
        assert "high" in str(e).lower() or "unreasonable" in str(e).lower(), f"Expected error message to mention 'high' or 'unreasonable', got '{e}'"
    
    try:
        validate_age("twenty")
        assert False, "Expected TypeError for non-integer age"
    except TypeError:
        pass  # This is expected
    
    # Valid age should return the age
    assert validate_age(25) == 25, "Expected validate_age(25) to return 25"
    
    # Test BankAccount
    try:
        account = BankAccount("12345", -100)
        assert False, "Expected NegativeBalanceError for negative initial balance"
    except NegativeBalanceError:
        pass  # This is expected
    
    account = BankAccount("12345", 100)
    
    # Test deposit
    try:
        account.deposit(-50)
        assert False, "Expected ValueError for negative deposit"
    except ValueError:
        pass  # This is expected
    
    new_balance = account.deposit(50)
    assert new_balance == 150, f"Expected balance 150, got {new_balance}"
    
    # Test withdraw
    try:
        account.withdraw(-50)
        assert False, "Expected ValueError for negative withdrawal"
    except ValueError:
        pass  # This is expected
    
    try:
        account.withdraw(200)
        assert False, "Expected NegativeBalanceError for excessive withdrawal"
    except NegativeBalanceError:
        pass  # This is expected
    
    new_balance = account.withdraw(50)
    assert new_balance == 100, f"Expected balance 100, got {new_balance}"
    
    print("All custom exception tests passed!")


def test_context_manager():
    import os
    
    # Test FileManager
    # Create a test file
    with open("test_file.txt", "w") as f:
        f.write("Hello, World!")
    
    # Test reading with context manager
    with FileManager("test_file.txt") as f:
        content = f.read()
        assert content == "Hello, World!", f"Expected 'Hello, World!', got '{content}'"
    
    # Test writing with context manager
    with FileManager("test_file2.txt", "w") as f:
        f.write("Testing, 1, 2, 3")
    
    # Verify the file was written
    with open("test_file2.txt", "r") as f:
        content = f.read()
        assert content == "Testing, 1, 2, 3", f"Expected 'Testing, 1, 2, 3', got '{content}'"
    
    # Test with non-existent file
    try:
        with FileManager("nonexistent_file.txt") as f:
            content = f.read()
        assert False, "Expected FileNotFoundError for nonexistent file"
    except FileNotFoundError:
        pass  # This is expected
    
    # Clean up
    os.remove("test_file.txt")
    os.remove("test_file2.txt")
    
    print("All context manager tests passed!")


def test_process_data_file():
    import os
    
    # Create a test data file
    with open("test_data.txt", "w") as f:
        f.write("10\n20\nthirty\n40\n\n50\n")
    
    # Test process_data_file
    result = process_data_file("test_data.txt")
    assert len(result) == 3, f"Expected tuple of length 3, got {len(result)}"
    
    total_sum, valid_count, invalid_count = result
    assert total_sum == 120, f"Expected sum 120, got {total_sum}"
    assert valid_count == 4, f"Expected 4 valid integers, got {valid_count}"
    assert invalid_count == 2, f"Expected 2 invalid lines, got {invalid_count}"
    
    # Test with non-existent file
    try:
        process_data_file("nonexistent_file.txt")
        assert False, "Expected FileNotFoundError for nonexistent file"
    except FileNotFoundError:
        pass  # This is expected
    
    # Clean up
    os.remove("test_data.txt")
    
    print("All process_data_file tests passed!")


if __name__ == "__main__":
    test_custom_exceptions()
    test_context_manager()
    test_process_data_file()