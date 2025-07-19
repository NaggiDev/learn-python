"""
Solution: Advanced Testing with Fixtures and Parametrization

This file contains the completed solutions for the advanced testing exercise.
"""

import pytest


# Classes to test (same as in exercise)
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


# Fixtures - Solutions
@pytest.fixture
def bank_account():
    """Create a bank account with initial balance of 100."""
    return BankAccount(100)


@pytest.fixture
def empty_cart():
    """Create an empty shopping cart."""
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    """Create a shopping cart with some items."""
    cart = ShoppingCart()
    cart.add_item("apple", 1.50, 3)
    cart.add_item("banana", 0.75, 2)
    return cart


# Parametrized tests - Solutions
@pytest.mark.parametrize("initial_balance,deposit_amount,expected_balance", [
    (0, 50, 50),
    (100, 25, 125),
    (50, 100, 150),
    (200, 0.01, 200.01),
])
def test_bank_account_deposit_parametrized(initial_balance, deposit_amount, expected_balance):
    """Test bank account deposit with multiple parameter sets."""
    account = BankAccount(initial_balance)
    account.deposit(deposit_amount)
    assert account.balance == expected_balance


@pytest.mark.parametrize("item,price,quantity,expected_error", [
    ("apple", -1.50, 1, ValueError),  # Negative price
    ("banana", 1.00, 0, ValueError),  # Zero quantity
    ("orange", 2.00, -1, ValueError), # Negative quantity
])
def test_shopping_cart_invalid_add_item(item, price, quantity, expected_error):
    """Test shopping cart add_item with invalid parameters."""
    cart = ShoppingCart()
    with pytest.raises(expected_error):
        cart.add_item(item, price, quantity)


# Class-based tests - Solutions
class TestBankAccount:
    """Test class for BankAccount functionality."""
    
    def test_initial_balance(self, bank_account):
        """Test that account is created with correct initial balance."""
        assert bank_account.balance == 100
    
    def test_deposit_increases_balance(self, bank_account):
        """Test that deposit increases the balance correctly."""
        bank_account.deposit(50)
        assert bank_account.balance == 150
    
    def test_withdraw_decreases_balance(self, bank_account):
        """Test that withdrawal decreases the balance correctly."""
        bank_account.withdraw(30)
        assert bank_account.balance == 70
    
    def test_withdraw_insufficient_funds(self, bank_account):
        """Test that withdrawing more than balance raises ValueError."""
        with pytest.raises(ValueError, match="Insufficient funds"):
            bank_account.withdraw(200)
    
    def test_negative_initial_balance_raises_error(self):
        """Test that creating account with negative balance raises ValueError."""
        with pytest.raises(ValueError, match="Initial balance cannot be negative"):
            BankAccount(-50)
    
    def test_deposit_negative_amount_raises_error(self, bank_account):
        """Test that depositing negative amount raises ValueError."""
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            bank_account.deposit(-10)
    
    def test_withdraw_negative_amount_raises_error(self, bank_account):
        """Test that withdrawing negative amount raises ValueError."""
        with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
            bank_account.withdraw(-10)


class TestShoppingCart:
    """Test class for ShoppingCart functionality."""
    
    def test_empty_cart_total(self, empty_cart):
        """Test that empty cart has zero total."""
        assert empty_cart.get_total() == 0
    
    def test_empty_cart_item_count(self, empty_cart):
        """Test that empty cart has zero items."""
        assert empty_cart.get_item_count() == 0
    
    def test_add_single_item(self, empty_cart):
        """Test adding a single item to cart."""
        empty_cart.add_item("book", 15.99)
        assert empty_cart.get_total() == 15.99
        assert empty_cart.get_item_count() == 1
    
    def test_add_multiple_same_item(self, empty_cart):
        """Test adding multiple quantities of the same item."""
        empty_cart.add_item("pen", 2.50, 3)
        assert empty_cart.get_total() == 7.50
        assert empty_cart.get_item_count() == 3
    
    def test_cart_with_items_total(self, cart_with_items):
        """Test total calculation with pre-loaded cart."""
        # 3 apples at 1.50 each + 2 bananas at 0.75 each = 4.50 + 1.50 = 6.00
        assert cart_with_items.get_total() == 6.00
        assert cart_with_items.get_item_count() == 5
    
    def test_remove_existing_item(self, cart_with_items):
        """Test removing an item that exists in cart."""
        original_total = cart_with_items.get_total()
        cart_with_items.remove_item("apple")
        # Should remove 3 apples at 1.50 each = 4.50
        assert cart_with_items.get_total() == original_total - 4.50
        assert cart_with_items.get_item_count() == 2
    
    def test_remove_nonexistent_item(self, empty_cart):
        """Test removing an item that doesn't exist raises ValueError."""
        with pytest.raises(ValueError, match="Item 'nonexistent' not in cart"):
            empty_cart.remove_item("nonexistent")
    
    def test_add_existing_item_increases_quantity(self, cart_with_items):
        """Test that adding an existing item increases its quantity."""
        original_count = cart_with_items.get_item_count()
        cart_with_items.add_item("apple", 1.50, 2)  # Add 2 more apples
        assert cart_with_items.get_item_count() == original_count + 2


# Additional challenge tests - Solutions
def test_multiple_operations_sequence(bank_account):
    """Test a sequence of multiple operations on bank account."""
    # Starting with 100
    bank_account.deposit(50)    # 150
    bank_account.withdraw(25)   # 125
    bank_account.deposit(100)   # 225
    bank_account.withdraw(75)   # 150
    assert bank_account.balance == 150


def test_cart_complex_scenario():
    """Test a complex shopping cart scenario."""
    cart = ShoppingCart()
    
    # Add multiple different items
    cart.add_item("laptop", 999.99, 1)
    cart.add_item("mouse", 25.50, 2)
    cart.add_item("keyboard", 75.00, 1)
    
    # Verify initial state
    assert cart.get_item_count() == 4
    assert cart.get_total() == 999.99 + (25.50 * 2) + 75.00  # 1125.99
    
    # Remove an item
    cart.remove_item("mouse")
    assert cart.get_item_count() == 2
    assert cart.get_total() == 999.99 + 75.00  # 1074.99
    
    # Add more items
    cart.add_item("headphones", 150.00, 1)
    cart.add_item("laptop", 999.99, 1)  # Add another laptop
    
    # Final verification
    assert cart.get_item_count() == 4  # 2 laptops, 1 keyboard, 1 headphones
    assert cart.get_total() == (999.99 * 2) + 75.00 + 150.00  # 2224.98


# Edge case tests
class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_bank_account_zero_operations(self):
        """Test operations with zero amounts."""
        account = BankAccount(100)
        
        with pytest.raises(ValueError):
            account.deposit(0)
        
        with pytest.raises(ValueError):
            account.withdraw(0)
    
    def test_shopping_cart_decimal_prices(self):
        """Test shopping cart with decimal prices."""
        cart = ShoppingCart()
        cart.add_item("item", 1.99, 3)
        assert cart.get_total() == 5.97
    
    def test_bank_account_exact_balance_withdrawal(self):
        """Test withdrawing exact balance."""
        account = BankAccount(50)
        account.withdraw(50)
        assert account.balance == 0


if __name__ == "__main__":
    pytest.main([__file__])