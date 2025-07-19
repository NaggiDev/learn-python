# Functions and Classes Cheat Sheet

## Functions

### Basic Function Definition
```python
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)  # Hello, Alice!
```

### Function Parameters

#### Default Parameters
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
```

#### Keyword Arguments
```python
def create_profile(name, age, city="Unknown"):
    return f"{name}, {age} years old, from {city}"

# Positional arguments
create_profile("Alice", 30, "NYC")

# Keyword arguments
create_profile(name="Alice", age=30, city="NYC")
create_profile("Alice", city="NYC", age=30)  # Order doesn't matter
```

#### Variable Arguments
```python
# *args for variable positional arguments
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# **kwargs for variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")

# Combining all parameter types
def complex_function(required, default="default", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
```

### Lambda Functions
```python
# Basic lambda
square = lambda x: x**2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

### Function Decorators
```python
# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
```

## Classes

### Basic Class Definition
```python
class Person:
    """A simple Person class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        self.age += 1

# Creating and using objects
person = Person("Alice", 30)
print(person.introduce())  # Hi, I'm Alice and I'm 30 years old.
person.have_birthday()
print(person.age)  # 31
```

### Class and Instance Variables
```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis lupus"
    
    def __init__(self, name, breed):
        # Instance variables (unique to each instance)
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.species)  # Canis lupus (same for all dogs)
print(dog1.name)     # Buddy (unique to this dog)
```

### Inheritance
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # To be overridden by subclasses

# Child classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
```

### Multiple Inheritance
```python
class Flyable:
    def fly(self):
        return "Flying high!"

class Swimmable:
    def swim(self):
        return "Swimming fast!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(duck.speak())  # Donald says Quack!
print(duck.fly())    # Flying high!
print(duck.swim())   # Swimming fast!
```

### Special Methods (Magic Methods)
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for users"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Point(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Addition operator"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """Equality operator"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Length (distance from origin)"""
        return (self.x**2 + self.y**2)**0.5

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)           # Point(1, 2)
print(p1 + p2)      # Point(4, 6)
print(p1 == p2)     # False
print(len(p1))      # 2.23606797749979
```

### Property Decorators
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Get the radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set the radius with validation"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Calculate area (read-only property)"""
        return 3.14159 * self._radius**2

circle = Circle(5)
print(circle.radius)  # 5
print(circle.area)    # 78.53975
circle.radius = 10    # Uses setter
print(circle.area)    # 314.159
```

### Class Methods and Static Methods
```python
class MathUtils:
    pi = 3.14159
    
    @classmethod
    def circle_area(cls, radius):
        """Class method - has access to class variables"""
        return cls.pi * radius**2
    
    @staticmethod
    def add(x, y):
        """Static method - independent utility function"""
        return x + y

# Can call on class or instance
print(MathUtils.circle_area(5))  # 78.53975
print(MathUtils.add(3, 4))       # 7

math = MathUtils()
print(math.circle_area(5))       # 78.53975
print(math.add(3, 4))            # 7
```

### Abstract Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot instantiate abstract class
# shape = Shape()  # TypeError

# Can instantiate concrete subclass
rect = Rectangle(5, 3)
print(rect.area())      # 15
print(rect.perimeter()) # 16
```

## Advanced Concepts

### Context Managers
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using the context manager
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
# File is automatically closed
```

### Generators
```python
def fibonacci(n):
    """Generator function for Fibonacci sequence"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34

# Generator expression
squares = (x**2 for x in range(10))
print(list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Best Practices

### Function Design
```python
# Good: Single responsibility, clear name, docstring
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius**2
```

### Class Design
```python
class BankAccount:
    """A simple bank account class demonstrating good practices."""
    
    def __init__(self, account_number, initial_balance=0):
        self._account_number = account_number  # Protected attribute
        self._balance = initial_balance
        self._transaction_history = []
    
    @property
    def balance(self):
        """Get current balance (read-only)"""
        return self._balance
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transaction_history.append(f"Deposited ${amount}")
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transaction_history.append(f"Withdrew ${amount}")
    
    def __str__(self):
        return f"Account {self._account_number}: ${self._balance}"
```

## Common Patterns

### Factory Pattern
```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
animal = AnimalFactory.create_animal("dog", "Buddy")
```

### Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Observer Pattern
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received: {message}")
```