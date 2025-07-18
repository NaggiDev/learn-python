# Classes and Objects in Python

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects rather than functions and logic. Python is a multi-paradigm language that fully supports OOP principles. In this lesson, we'll explore the fundamentals of classes and objects in Python.

## What are Classes and Objects?

- A **class** is a blueprint for creating objects. It defines attributes (data) and methods (functions) that will be common to all objects of that type.
- An **object** is an instance of a class - a concrete entity based on the class blueprint.

Think of a class as a cookie cutter, and objects as the cookies made from that cutter. Each cookie has the same shape (defined by the class) but can have different characteristics (instance attributes).

## Defining a Class in Python

In Python, we define a class using the `class` keyword:

```python
class Dog:
    # Class body
    pass
```

This creates a simple class named `Dog` with no attributes or methods.

## Class Constructor: `__init__` Method

The `__init__` method is a special method that Python calls when you create a new instance of a class. It's used to initialize the object's attributes:

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
```

The `self` parameter refers to the instance being created and is automatically passed when you call the method.

## Creating Objects (Instances)

Once a class is defined, you can create objects (instances) of that class:

```python
# Create a Dog object
buddy = Dog("Buddy", "Golden Retriever", 3)
max = Dog("Max", "German Shepherd", 5)
```

Each object has its own copy of the attributes defined in the class.

## Instance Attributes vs. Class Attributes

- **Instance attributes** are specific to each object. They're defined inside methods using `self`.
- **Class attributes** are shared by all instances of the class. They're defined directly in the class body.

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, breed, age):
        # Instance attributes
        self.name = name
        self.breed = breed
        self.age = age
```

You can access class attributes through the class itself or through any instance:

```python
print(Dog.species)  # Accessing through the class
print(buddy.species)  # Accessing through an instance
```

## Instance Methods

Instance methods are functions defined within a class that operate on instances of that class:

```python
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is a {self.age} year old {self.breed}"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
```

To call an instance method:

```python
buddy = Dog("Buddy", "Golden Retriever", 3)
print(buddy.description())  # Output: Buddy is a 3 year old Golden Retriever
print(buddy.speak("Woof"))  # Output: Buddy says Woof
```

## Class Methods

Class methods are methods that are bound to the class rather than its instances. They can access and modify class state but not instance state. They're defined using the `@classmethod` decorator:

```python
class Dog:
    count = 0  # Class attribute to track number of dogs
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        Dog.count += 1  # Increment the count when a new dog is created
    
    @classmethod
    def get_count(cls):
        return cls.count
```

To call a class method:

```python
buddy = Dog("Buddy", "Golden Retriever", 3)
max = Dog("Max", "German Shepherd", 5)
print(Dog.get_count())  # Output: 2
```

## Static Methods

Static methods are methods that don't operate on instance or class data. They're defined using the `@staticmethod` decorator:

```python
class Dog:
    # ... other code ...
    
    @staticmethod
    def is_adult(age):
        return age >= 2
```

To call a static method:

```python
print(Dog.is_adult(1))  # Output: False
print(Dog.is_adult(3))  # Output: True
```

## The `self` Parameter

The `self` parameter is a reference to the current instance of the class. It's used to access variables and methods belonging to the instance:

- It's always the first parameter in instance methods
- It's automatically passed when you call an instance method
- You can name it something else, but `self` is the convention

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")
```

## Modifying Attributes

You can modify an object's attributes after creation:

```python
buddy = Dog("Buddy", "Golden Retriever", 3)
print(buddy.age)  # Output: 3

# Modify the age
buddy.age = 4
print(buddy.age)  # Output: 4
```

## Adding Attributes Dynamically

In Python, you can add new attributes to an object after it's created:

```python
buddy = Dog("Buddy", "Golden Retriever", 3)

# Add a new attribute
buddy.favorite_toy = "Tennis Ball"
print(buddy.favorite_toy)  # Output: Tennis Ball
```

However, this is generally not recommended as it can make code harder to understand and maintain.

## Deleting Attributes and Objects

You can delete attributes and objects using the `del` keyword:

```python
# Delete an attribute
del buddy.favorite_toy

# Delete an object
del buddy
```

## Best Practices for Classes

1. **Use CamelCase for class names**: `Dog`, `Person`, `BankAccount`
2. **Use descriptive names** for classes, methods, and attributes
3. **Keep classes focused** on a single responsibility
4. **Document your classes** with docstrings
5. **Initialize all instance attributes** in the `__init__` method
6. **Use properties** instead of direct attribute access when you need validation

## Example: A Complete Class

Here's a more complete example of a Python class:

```python
class BankAccount:
    """A class representing a bank account."""
    
    interest_rate = 0.02  # Class attribute - annual interest rate
    
    def __init__(self, account_number, owner_name, balance=0):
        """Initialize a new bank account.
        
        Args:
            account_number (str): The account number
            owner_name (str): The name of the account owner
            balance (float, optional): Initial balance. Defaults to 0.
        """
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.transactions = []
        self._record_transaction("Initial deposit", balance)
    
    def deposit(self, amount):
        """Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit
            
        Returns:
            float: The new balance
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self._record_transaction("Deposit", amount)
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from the account.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            float: The new balance
            
        Raises:
            ValueError: If amount is negative or exceeds balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        self._record_transaction("Withdrawal", -amount)
        return self.balance
    
    def _record_transaction(self, transaction_type, amount):
        """Record a transaction (private method).
        
        Args:
            transaction_type (str): The type of transaction
            amount (float): The transaction amount
        """
        import datetime
        timestamp = datetime.datetime.now()
        self.transactions.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": timestamp,
            "balance": self.balance
        })
    
    def get_balance(self):
        """Get the current balance.
        
        Returns:
            float: The current balance
        """
        return self.balance
    
    def print_statement(self):
        """Print the account statement."""
        print(f"Account Statement for {self.account_number} ({self.owner_name})")
        print(f"Current Balance: ${self.balance:.2f}")
        print("\nTransaction History:")
        for t in self.transactions:
            print(f"{t['timestamp']}: {t['type']} ${abs(t['amount']):.2f} - Balance: ${t['balance']:.2f}")
    
    @classmethod
    def calculate_interest(cls, principal, years):
        """Calculate interest on a principal over a number of years.
        
        Args:
            principal (float): The principal amount
            years (int): Number of years
            
        Returns:
            float: The interest earned
        """
        return principal * cls.interest_rate * years
    
    @staticmethod
    def validate_account_number(account_number):
        """Validate an account number format.
        
        Args:
            account_number (str): The account number to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Simple validation: 10 digits
        return len(account_number) == 10 and account_number.isdigit()
```

## Conclusion

Classes and objects are fundamental concepts in object-oriented programming. They allow you to create reusable, modular code by grouping related data and functionality together. In Python, classes provide a flexible way to define new types that can model real-world entities or abstract concepts.

In the next lessons, we'll explore more advanced OOP concepts like inheritance, polymorphism, encapsulation, and abstraction.

## Further Reading

- [Python Documentation: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Object-Oriented Programming in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Python's Instance, Class, and Static Methods Demystified](https://realpython.com/instance-class-and-static-methods-demystified/)