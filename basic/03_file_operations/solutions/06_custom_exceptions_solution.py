"""
Solution: Custom Exceptions and Context Managers

This file contains solutions to the custom exceptions and context managers exercise.
"""

class InvalidAgeError(Exception):
    """
    Custom exception for invalid age values.
    """
    def __init__(self, message="Invalid age"):
        self.message = message
        super().__init__(self.message)


class NegativeBalanceError(Exception):
    """
    Custom exception for negative account balance.
    """
    def __init__(self, message="Account balance cannot be negative", balance=None):
        self.message = message
        self.balance = balance
        super().__init__(self.message)


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
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    
    if age > 120:
        raise InvalidAgeError("Age is unreasonably high")
    
    return age


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
        self.account_number = account_number
        
        if initial_balance < 0:
            raise NegativeBalanceError("Initial balance cannot be negative", initial_balance)
        
        self.balance = initial_balance
    
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
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return self.balance
    
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
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise NegativeBalanceError(
                f"Withdrawal of {amount} would exceed balance of {self.balance}",
                self.balance - amount
            )
        
        self.balance -= amount
        return self.balance


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
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """
        Enter the context manager.
        
        Returns:
            file: The opened file object
            
        Raises:
            FileNotFoundError: If the file doesn't exist (in read mode)
        """
        self.file = open(self.filename, self.mode)
        return self.file
    
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
        if self.file:
            self.file.close()
        
        # Don't suppress exceptions
        return False


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
    total_sum = 0
    valid_count = 0
    invalid_count = 0
    
    with FileManager(file_path) as file:
        for line in file:
            line = line.strip()
            
            if not line:  # Skip empty lines
                invalid_count += 1
                continue
            
            try:
                value = int(line)
                total_sum += value
                valid_count += 1
            except ValueError:
                invalid_count += 1
    
    return (total_sum, valid_count, invalid_count)


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