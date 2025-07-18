"""
Solution: Classes and Objects in Python

This file contains solutions to the exercises in 01_classes_and_objects.py
"""

# Exercise 1: Create a basic class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Exercise 2: Class and Instance Attributes
class Rectangle:
    shape_type = "Rectangle"
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


# Exercise 3: Class Methods and Static Methods
class MathOperations:
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius * radius
    
    @classmethod
    def circle_circumference(cls, radius):
        return 2 * cls.pi * radius


# Exercise 4: A More Complex Class
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance
    
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance
    
    def get_balance(self):
        return self._balance
    
    def transfer(self, other_account, amount):
        self.withdraw(amount)  # This will raise ValueError if insufficient funds
        other_account.deposit(amount)
        return True


# Exercise 5: Creating and Using Objects
if __name__ == "__main__":
    # 1. Create two Person objects
    person1 = Person("John", 30)
    person2 = Person("Jane", 25)
    
    # 2. Print greetings
    print(person1.greet())
    print(person2.greet())
    
    # 3. Create Rectangle
    rect = Rectangle(5, 10)
    
    # 4. Print area and perimeter
    print(f"Rectangle area: {rect.area()}")
    print(f"Rectangle perimeter: {rect.perimeter()}")
    
    # 5. Print shape_type
    print(f"Shape type: {Rectangle.shape_type}")
    
    # 6. Use MathOperations
    print(f"15 + 7 = {MathOperations.add(15, 7)}")
    print(f"20 - 8 = {MathOperations.subtract(20, 8)}")
    print(f"Circle area (r=4): {MathOperations.circle_area(4)}")
    print(f"Circle circumference (r=4): {MathOperations.circle_circumference(4)}")
    
    # 7. Create BankAccount objects
    alice_account = BankAccount("Alice", 1000)
    bob_account = BankAccount("Bob", 500)
    
    # 8. Deposit to Alice's account
    new_balance = alice_account.deposit(300)
    print(f"Alice's balance after deposit: ${new_balance}")
    
    # 9. Withdraw from Bob's account
    new_balance = bob_account.withdraw(100)
    print(f"Bob's balance after withdrawal: ${new_balance}")
    
    # 10. Transfer from Alice to Bob
    alice_account.transfer(bob_account, 200)
    
    # 11. Print both balances
    print(f"Alice's final balance: ${alice_account.get_balance()}")
    print(f"Bob's final balance: ${bob_account.get_balance()}")
    
    # Run the tests
    from importlib import reload
    import sys
    
    # Add the exercises directory to the path so we can import the test function
    sys.path.append('../exercises')
    
    try:
        import exercises.01_classes_and_objects as exercises
        reload(exercises)  # Reload to get the latest version
        exercises.run_tests()
    except ImportError:
        print("Could not import the exercises module. Make sure you're running this from the solutions directory.")