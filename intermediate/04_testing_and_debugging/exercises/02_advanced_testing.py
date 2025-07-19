"""
Exercise 2: Advanced Testing with Fixtures and Parametrization

This exercise covers more advanced pytest features including fixtures,
parametrized tests, and testing classes.

Instructions:
1. Complete the fixture functions
2. Complete the parametrized tests
3. Complete the class-based tests
4. Run tests: pytest 02_advanced_testing.py
"""

import pytest


# Classes to test
class BankAccount:
    """A simple bank account class."""
    
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance


class ShoppingCart:
    """A simple shopping cart class."""
    
    def __init__(self):
        self._items = {}
    
    def add_item(self, item, price, quantity=1):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if item in self._items:
            self._items[item]['quantity'] += quantity
        else:
            self._items[item] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, item):
        if item not in self._items:
            raise ValueError(f"Item '{item}' not in cart")
        del self._items[item]
    
    def get_total(self):
        return sum(item['price'] * item['quantity'] for item in self._items.values())
    
    def get_item_count(self):
        return sum(item['quantity'] for item in self._items.values())


# Fixtures - Complete these
@pytest.fixture
def bank_account():
    """Create a bank account with initial balance of 100."""
    # TODO: Return a BankAccount instance with balance 100
    pass


@pytest.fixture
def empty_cart():
    """Create an empty shopping cart."""
    # TODO: Return a new ShoppingCart instance
    pass


@pytest.fixture
def cart_with_items():
    """Create a shopping cart with some items."""
    # TODO: Create a cart and add some items to it
    # Add: "apple" (price=1.50, quantity=3), "banana" (price=0.75, quantity=2)
    pass


# Parametrized tests - Complete these
@pytest.mark.parametrize("initial_balance,deposit_amount,expected_balance", [
    # TODO: Add test cases for different initial balances and deposit amounts
    # Format: (initial_balance, deposit_amount, expected_final_balance)
    # Add at least 3 test cases
])
def test_bank_account_deposit_parametrized(initial_balance, deposit_amount, expected_balance):
    """Test bank account deposit with multiple parameter sets."""
    # TODO: Create account, make deposit, assert final balance
    pass


@pytest.mark.parametrize("item,price,quantity,expected_error", [
    # TODO: Add test cases that should raise ValueError
    # Format: (item_name, price, quantity, expected_exception_type)
    # Test negative price, zero quantity, negative quantity
])
def test_shopping_cart_invalid_add_item(item, price, quantity, expected_error):
    """Test shopping cart add_item with invalid parameters."""
    # TODO: Create cart, attempt to add item, assert ValueError is raised
    pass


# Class-based tests
class TestBankAccount:
    """Test class for BankAccount functionality."""
    
    def test_initial_balance(self, bank_account):
        """Test that account is created with correct initial balance."""
        # TODO: Assert that bank_account.balance equals 100
        pass
    
    def test_deposit_increases_balance(self, bank_account):
        """Test that deposit increases the balance correctly."""
        # TODO: Deposit 50, assert balance is 150
        pass
    
    def test_withdraw_decreases_balance(self, bank_account):
        """Test that withdrawal decreases the balance correctly."""
        # TODO: Withdraw 30, assert balance is 70
        pass
    
    def test_withdraw_insufficient_funds(self, bank_account):
        """Test that withdrawing more than balance raises ValueError."""
        # TODO: Attempt to withdraw 200, assert ValueError is raised
        pass
    
    def test_negative_initial_balance_raises_error(self):
        """Test that creating account with negative balance raises ValueError."""
        # TODO: Attempt to create BankAccount(-50), assert ValueError is raised
        pass


class TestShoppingCart:
    """Test class for ShoppingCart functionality."""
    
    def test_empty_cart_total(self, empty_cart):
        """Test that empty cart has zero total."""
        # TODO: Assert that empty_cart.get_total() equals 0
        pass
    
    def test_empty_cart_item_count(self, empty_cart):
        """Test that empty cart has zero items."""
        # TODO: Assert that empty_cart.get_item_count() equals 0
        pass
    
    def test_add_single_item(self, empty_cart):
        """Test adding a single item to cart."""
        # TODO: Add item "book" with price 15.99, assert total and count
        pass
    
    def test_add_multiple_same_item(self, empty_cart):
        """Test adding multiple quantities of the same item."""
        # TODO: Add "pen" with price 2.50 and quantity 3
        # Assert total is 7.50 and item count is 3
        pass
    
    def test_cart_with_items_total(self, cart_with_items):
        """Test total calculation with pre-loaded cart."""
        # TODO: Assert the total matches expected value
        # (3 apples at 1.50 each + 2 bananas at 0.75 each = 4.50 + 1.50 = 6.00)
        pass
    
    def test_remove_existing_item(self, cart_with_items):
        """Test removing an item that exists in cart."""
        # TODO: Remove "apple", assert it's no longer affecting total
        pass
    
    def test_remove_nonexistent_item(self, empty_cart):
        """Test removing an item that doesn't exist raises ValueError."""
        # TODO: Attempt to remove "nonexistent", assert ValueError is raised
        pass


# Additional challenge tests
def test_multiple_operations_sequence(bank_account):
    """Test a sequence of multiple operations on bank account."""
    # TODO: Perform multiple deposits and withdrawals, verify final balance
    # Example: deposit 50, withdraw 25, deposit 100, withdraw 75
    # Starting with 100, final balance should be 150
    pass


def test_cart_complex_scenario():
    """Test a complex shopping cart scenario."""
    # TODO: Create cart, add multiple different items with different quantities
    # Remove some items, add more items, verify final total and count
    pass


if __name__ == "__main__":
    pytest.main([__file__])