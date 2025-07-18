"""
Exercise: Encapsulation and Abstraction in Python

Instructions:
1. Complete the exercises below by implementing the required classes and methods
2. Run this file to test your implementation
3. All tests should pass with no errors

Learning objectives:
- Implement encapsulation using Python's conventions
- Use properties for controlled attribute access
- Create abstract base classes
- Apply encapsulation and abstraction principles together
"""

from abc import ABC, abstractmethod

# Exercise 1: Basic Encapsulation
# Create a BankAccount class with:
# - Private attributes for _account_number and _balance
# - A constructor that initializes these attributes
# - Properties for account_number (read-only) and balance (read-only)
# - Methods deposit(amount) and withdraw(amount) that modify the balance
# - withdraw should prevent the balance from going below 0 and return True if successful, False otherwise
# TODO: Implement the BankAccount class


# Exercise 2: Properties with Validation
# Create a Person class with:
# - Private attributes for _name, _age, and _email
# - Properties for each attribute with appropriate getters and setters
# - Validation in the setters:
#   - name must be a non-empty string
#   - age must be a positive integer
#   - email must contain '@' (simple validation)
# - A read-only property full_info that returns "Name: {name}, Age: {age}, Email: {email}"
# TODO: Implement the Person class


# Exercise 3: Abstract Base Class
# Create an abstract Vehicle class with:
# - An __init__ method that takes make, model, and year parameters
# - Abstract methods start_engine() and stop_engine()
# - An abstract property fuel_type
# - A concrete method get_info() that returns "{year} {make} {model}"
# Then create two concrete subclasses:
# 1. Car with:
#    - An additional parameter num_doors in __init__
#    - Implementations of start_engine(), stop_engine(), and fuel_type
# 2. Motorcycle with:
#    - An additional parameter has_sidecar in __init__
#    - Implementations of start_engine(), stop_engine(), and fuel_type
# TODO: Implement the Vehicle abstract class and Car and Motorcycle subclasses


# Exercise 4: Encapsulation with Private Methods
# Create a PasswordManager class with:
# - A private attribute _passwords (a dictionary mapping service names to passwords)
# - A private method __encrypt_password(password) that "encrypts" a password (just reverse it for this exercise)
# - A private method __decrypt_password(encrypted) that "decrypts" a password
# - Methods add_password(service, password), get_password(service), and remove_password(service)
# - The add_password method should store the encrypted password
# - The get_password method should return the decrypted password
# TODO: Implement the PasswordManager class


# Exercise 5: Combining Encapsulation and Abstraction
# Create an abstract DataProcessor class with:
# - An __init__ method that takes a data parameter (a list)
# - A private attribute _data to store the data
# - A property data that returns a copy of _data (to prevent direct modification)
# - Abstract methods process() and get_result()
# - A concrete method reset(data) that updates _data
# Then create two concrete subclasses:
# 1. SortProcessor that:
#    - Implements process() to sort the data
#    - Implements get_result() to return the sorted data
# 2. FilterProcessor that:
#    - Takes an additional parameter filter_func in __init__
#    - Implements process() to filter the data using filter_func
#    - Implements get_result() to return the filtered data
# TODO: Implement the DataProcessor abstract class and SortProcessor and FilterProcessor subclasses


# Test code - DO NOT MODIFY
def run_tests():
    print("Running tests...")
    
    # Test Exercise 1: Basic Encapsulation
    try:
        account = BankAccount("12345", 1000)
        
        # Test properties
        assert account.account_number == "12345"
        assert account.balance == 1000
        
        # Test deposit
        account.deposit(500)
        assert account.balance == 1500
        
        # Test successful withdrawal
        result = account.withdraw(800)
        assert result == True
        assert account.balance == 700
        
        # Test withdrawal with insufficient funds
        result = account.withdraw(1000)
        assert result == False
        assert account.balance == 700
        
        # Test encapsulation
        try:
            account.balance = 2000
            assert False, "Should not be able to set balance directly"
        except AttributeError:
            pass
        
        try:
            account.account_number = "67890"
            assert False, "Should not be able to set account_number directly"
        except AttributeError:
            pass
        
        print("✓ Exercise 1 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 1 failed: {e}")
    
    # Test Exercise 2: Properties with Validation
    try:
        person = Person("Alice", 30, "alice@example.com")
        
        # Test properties
        assert person.name == "Alice"
        assert person.age == 30
        assert person.email == "alice@example.com"
        assert person.full_info == "Name: Alice, Age: 30, Email: alice@example.com"
        
        # Test setters with valid values
        person.name = "Bob"
        person.age = 25
        person.email = "bob@example.com"
        assert person.name == "Bob"
        assert person.age == 25
        assert person.email == "bob@example.com"
        
        # Test setters with invalid values
        try:
            person.name = ""
            assert False, "Should raise ValueError for empty name"
        except ValueError:
            pass
        
        try:
            person.age = -5
            assert False, "Should raise ValueError for negative age"
        except ValueError:
            pass
        
        try:
            person.email = "invalid-email"
            assert False, "Should raise ValueError for invalid email"
        except ValueError:
            pass
        
        # Test read-only property
        try:
            person.full_info = "Some info"
            assert False, "Should not be able to set full_info directly"
        except AttributeError:
            pass
        
        print("✓ Exercise 2 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 2 failed: {e}")
    
    # Test Exercise 3: Abstract Base Class
    try:
        # Verify Vehicle is abstract
        try:
            vehicle = Vehicle("Generic", "Model", 2022)
            assert False, "Should not be able to instantiate abstract class"
        except TypeError:
            pass
        
        car = Car("Toyota", "Camry", 2022, 4)
        motorcycle = Motorcycle("Honda", "CBR", 2022, False)
        
        # Test concrete method
        assert car.get_info() == "2022 Toyota Camry"
        assert motorcycle.get_info() == "2022 Honda CBR"
        
        # Test implemented abstract methods
        assert car.start_engine() == "The car engine starts"
        assert car.stop_engine() == "The car engine stops"
        assert motorcycle.start_engine() == "The motorcycle engine starts"
        assert motorcycle.stop_engine() == "The motorcycle engine stops"
        
        # Test implemented abstract properties
        assert car.fuel_type == "Gasoline"
        assert motorcycle.fuel_type == "Gasoline"
        
        # Test additional attributes
        assert car.num_doors == 4
        assert motorcycle.has_sidecar == False
        
        print("✓ Exercise 3 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 3 failed: {e}")
    
    # Test Exercise 4: Encapsulation with Private Methods
    try:
        pm = PasswordManager()
        
        # Test adding and retrieving passwords
        pm.add_password("gmail", "password123")
        pm.add_password("facebook", "secure456")
        
        assert pm.get_password("gmail") == "password123"
        assert pm.get_password("facebook") == "secure456"
        
        # Test removing passwords
        pm.remove_password("gmail")
        assert pm.get_password("gmail") is None
        
        # Test encapsulation of _passwords
        assert not hasattr(pm, "passwords"), "passwords should be private"
        
        # Test that passwords are actually encrypted
        # This is implementation-specific, but we can check that _passwords doesn't
        # contain the plain text passwords
        if hasattr(pm, "_passwords"):
            for service, encrypted in pm._passwords.items():
                assert encrypted != "password123", "Password should be encrypted"
                assert encrypted != "secure456", "Password should be encrypted"
        
        print("✓ Exercise 4 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 4 failed: {e}")
    
    # Test Exercise 5: Combining Encapsulation and Abstraction
    try:
        # Verify DataProcessor is abstract
        try:
            processor = DataProcessor([1, 2, 3])
            assert False, "Should not be able to instantiate abstract class"
        except TypeError:
            pass
        
        # Test SortProcessor
        sort_processor = SortProcessor([3, 1, 4, 1, 5, 9, 2, 6])
        
        # Test data property returns a copy
        initial_data = sort_processor.data
        initial_data.append(100)  # This should not affect the internal data
        assert 100 not in sort_processor.data
        
        # Test process and get_result
        sort_processor.process()
        assert sort_processor.get_result() == [1, 1, 2, 3, 4, 5, 6, 9]
        
        # Test reset
        sort_processor.reset([9, 8, 7])
        sort_processor.process()
        assert sort_processor.get_result() == [7, 8, 9]
        
        # Test FilterProcessor
        filter_processor = FilterProcessor([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
        
        # Test process and get_result
        filter_processor.process()
        assert filter_processor.get_result() == [2, 4, 6]
        
        # Test with a different filter
        filter_processor.reset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        filter_processor = FilterProcessor(filter_processor.data, lambda x: x > 5)
        filter_processor.process()
        assert filter_processor.get_result() == [6, 7, 8, 9, 10]
        
        print("✓ Exercise 5 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 5 failed: {e}")
    
    print("Tests completed!")

if __name__ == "__main__":
    run_tests()