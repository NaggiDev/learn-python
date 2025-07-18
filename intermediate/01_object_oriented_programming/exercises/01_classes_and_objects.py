"""
Exercise: Classes and Objects in Python

Instructions:
1. Complete the exercises below by implementing the required classes and methods
2. Run this file to test your implementation
3. All tests should pass with no errors

Learning objectives:
- Define classes with appropriate attributes and methods
- Create and use class instances (objects)
- Understand instance vs. class attributes and methods
- Practice implementing constructors and methods
"""

# Exercise 1: Create a basic class
# Define a Person class with the following:
# - An __init__ method that takes name and age parameters
# - A greet method that returns "Hello, my name is {name} and I am {age} years old."
# TODO: Implement the Person class


# Exercise 2: Class and Instance Attributes
# Define a Rectangle class with the following:
# - A class attribute 'shape_type' set to "Rectangle"
# - An __init__ method that takes width and height parameters
# - An area method that returns the area (width * height)
# - A perimeter method that returns the perimeter (2 * (width + height))
# TODO: Implement the Rectangle class


# Exercise 3: Class Methods and Static Methods
# Define a MathOperations class with the following:
# - A class attribute 'pi' set to 3.14159
# - A static method 'add' that takes two parameters and returns their sum
# - A static method 'subtract' that takes two parameters and returns their difference
# - A class method 'circle_area' that takes a radius parameter and returns the area of a circle (pi * radius^2)
# - A class method 'circle_circumference' that takes a radius parameter and returns the circumference (2 * pi * radius)
# TODO: Implement the MathOperations class


# Exercise 4: A More Complex Class
# Define a BankAccount class with the following:
# - An __init__ method that takes account_holder and initial_balance (default 0) parameters
# - A deposit method that adds to the balance and returns the new balance
# - A withdraw method that subtracts from the balance and returns the new balance
#   - If the withdrawal amount is greater than the balance, it should raise a ValueError with the message "Insufficient funds"
# - A get_balance method that returns the current balance
# - A transfer method that takes another BankAccount object and an amount as parameters
#   - It should withdraw the amount from the current account and deposit it to the other account
#   - It should return True if the transfer was successful
#   - If there are insufficient funds, it should raise a ValueError
# TODO: Implement the BankAccount class


# Exercise 5: Creating and Using Objects
# TODO: 
# 1. Create two Person objects with different names and ages
# 2. Print the result of calling the greet method on each person
# 3. Create a Rectangle object with width=5 and height=10
# 4. Print the rectangle's area and perimeter
# 5. Print the rectangle's shape_type class attribute
# 6. Use the MathOperations class to:
#    - Calculate and print the sum of 15 and 7
#    - Calculate and print the difference between 20 and 8
#    - Calculate and print the area of a circle with radius 4
#    - Calculate and print the circumference of a circle with radius 4
# 7. Create two BankAccount objects:
#    - One for "Alice" with an initial balance of 1000
#    - One for "Bob" with an initial balance of 500
# 8. Deposit 300 into Alice's account and print the new balance
# 9. Withdraw 100 from Bob's account and print the new balance
# 10. Transfer 200 from Alice's account to Bob's account
# 11. Print both account balances to verify the transfer worked


# Test code - DO NOT MODIFY
def run_tests():
    print("Running tests...")
    
    # Test Exercise 1: Person class
    try:
        p1 = Person("John", 30)
        p2 = Person("Jane", 25)
        assert p1.greet() == "Hello, my name is John and I am 30 years old."
        assert p2.greet() == "Hello, my name is Jane and I am 25 years old."
        print("✓ Exercise 1 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 1 failed: {e}")
    
    # Test Exercise 2: Rectangle class
    try:
        r = Rectangle(5, 10)
        assert Rectangle.shape_type == "Rectangle"
        assert r.shape_type == "Rectangle"
        assert r.area() == 50
        assert r.perimeter() == 30
        print("✓ Exercise 2 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 2 failed: {e}")
    
    # Test Exercise 3: MathOperations class
    try:
        assert abs(MathOperations.pi - 3.14159) < 0.00001
        assert MathOperations.add(5, 3) == 8
        assert MathOperations.subtract(10, 4) == 6
        assert abs(MathOperations.circle_area(2) - 12.56636) < 0.00001
        assert abs(MathOperations.circle_circumference(3) - 18.84954) < 0.00001
        print("✓ Exercise 3 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 3 failed: {e}")
    
    # Test Exercise 4: BankAccount class
    try:
        acc1 = BankAccount("Alice", 1000)
        acc2 = BankAccount("Bob", 500)
        
        assert acc1.get_balance() == 1000
        assert acc2.get_balance() == 500
        
        assert acc1.deposit(300) == 1300
        assert acc1.get_balance() == 1300
        
        assert acc2.withdraw(100) == 400
        assert acc2.get_balance() == 400
        
        try:
            acc2.withdraw(500)
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert str(e) == "Insufficient funds"
        
        assert acc1.transfer(acc2, 200) == True
        assert acc1.get_balance() == 1100
        assert acc2.get_balance() == 600
        
        print("✓ Exercise 4 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 4 failed: {e}")
    
    print("Tests completed!")

if __name__ == "__main__":
    run_tests()