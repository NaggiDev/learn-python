# Magic Methods in Python

## Introduction

Magic methods (also called dunder methods, short for "double underscore") are special methods in Python that start and end with double underscores (`__`). They allow you to define how objects of your classes behave in various contexts, such as when they're used with operators, converted to strings, or accessed like containers.

Magic methods are what make Python's built-in types (like lists, dictionaries, and numbers) work so intuitively. By implementing these methods in your own classes, you can make your objects behave like built-in types, leading to more intuitive and Pythonic code.

## Common Magic Methods

### Object Creation and Destruction

#### `__init__(self, ...)` - Constructor

The `__init__` method is called when an object is created. It's used to initialize the object's attributes:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

#### `__new__(cls, ...)` - Instance Creation

The `__new__` method is called before `__init__` and is responsible for creating and returning a new instance of the class:

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name):
        # This will be called every time, but the instance is only created once
        self.name = name
```

This example implements the Singleton pattern, ensuring only one instance of the class exists.

#### `__del__(self)` - Destructor

The `__del__` method is called when an object is about to be destroyed (garbage collected):

```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w')
    
    def __del__(self):
        print(f"Closing file {self.filename}")
        self.file.close()
```

Note: You should not rely on `__del__` for critical cleanup because it's not guaranteed to be called in all situations (e.g., when the program exits abruptly).

### String Representation

#### `__str__(self)` - String Representation for Users

The `__str__` method is called by the `str()` function and by the `print()` function. It should return a string that is suitable for end users:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
```

Usage:
```python
person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old
```

#### `__repr__(self)` - String Representation for Developers

The `__repr__` method is called by the `repr()` function and is used when displaying objects in the interactive console. It should return a string that, ideally, could be used to recreate the object:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
```

Usage:
```python
person = Person("Alice", 30)
print(repr(person))  # Output: Person('Alice', 30)
```

If `__str__` is not defined, Python will use `__repr__` as a fallback.

### Comparison Operators

#### `__eq__(self, other)` - Equality (==)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
```

#### `__ne__(self, other)` - Inequality (!=)

```python
def __ne__(self, other):
    if not isinstance(other, Point):
        return NotImplemented
    return self.x != other.x or self.y != other.y
```

#### `__lt__(self, other)` - Less Than (<)

```python
def __lt__(self, other):
    if not isinstance(other, Point):
        return NotImplemented
    return (self.x, self.y) < (other.x, other.y)
```

#### `__le__(self, other)` - Less Than or Equal (<=)

```python
def __le__(self, other):
    if not isinstance(other, Point):
        return NotImplemented
    return (self.x, self.y) <= (other.x, other.y)
```

#### `__gt__(self, other)` - Greater Than (>)

```python
def __gt__(self, other):
    if not isinstance(other, Point):
        return NotImplemented
    return (self.x, self.y) > (other.x, other.y)
```

#### `__ge__(self, other)` - Greater Than or Equal (>=)

```python
def __ge__(self, other):
    if not isinstance(other, Point):
        return NotImplemented
    return (self.x, self.y) >= (other.x, other.y)
```

### Arithmetic Operators

#### `__add__(self, other)` - Addition (+)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
```

#### `__sub__(self, other)` - Subtraction (-)

```python
def __sub__(self, other):
    if isinstance(other, Vector):
        return Vector(self.x - other.x, self.y - other.y)
    return NotImplemented
```

#### `__mul__(self, other)` - Multiplication (*)

```python
def __mul__(self, other):
    if isinstance(other, (int, float)):
        return Vector(self.x * other, self.y * other)
    return NotImplemented
```

#### `__truediv__(self, other)` - Division (/)

```python
def __truediv__(self, other):
    if isinstance(other, (int, float)):
        return Vector(self.x / other, self.y / other)
    return NotImplemented
```

#### `__floordiv__(self, other)` - Floor Division (//)

```python
def __floordiv__(self, other):
    if isinstance(other, (int, float)):
        return Vector(self.x // other, self.y // other)
    return NotImplemented
```

#### `__mod__(self, other)` - Modulo (%)

```python
def __mod__(self, other):
    if isinstance(other, (int, float)):
        return Vector(self.x % other, self.y % other)
    return NotImplemented
```

#### `__pow__(self, other)` - Power (**)

```python
def __pow__(self, other):
    if isinstance(other, (int, float)):
        return Vector(self.x ** other, self.y ** other)
    return NotImplemented
```

### Reflected Arithmetic Operators

Reflected operators are called when the left operand doesn't support the operation and the right operand is an instance of your class. For example, `5 * v` would call `v.__rmul__(5)` if `5.__mul__(v)` returns `NotImplemented`.

#### `__radd__(self, other)` - Reflected Addition

```python
def __radd__(self, other):
    return self.__add__(other)
```

#### `__rsub__(self, other)` - Reflected Subtraction

```python
def __rsub__(self, other):
    # Note: order matters for subtraction
    if isinstance(other, (int, float)):
        return Vector(other - self.x, other - self.y)
    return NotImplemented
```

#### `__rmul__(self, other)` - Reflected Multiplication

```python
def __rmul__(self, other):
    return self.__mul__(other)
```

And so on for other arithmetic operators.

### Augmented Assignment Operators

These methods are called for augmented assignment operations like `+=`, `-=`, etc.

#### `__iadd__(self, other)` - In-place Addition (+=)

```python
def __iadd__(self, other):
    if isinstance(other, Vector):
        self.x += other.x
        self.y += other.y
        return self
    return NotImplemented
```

Similar methods exist for other augmented assignments: `__isub__`, `__imul__`, `__itruediv__`, etc.

### Container Methods

#### `__len__(self)` - Length

```python
class Deck:
    def __init__(self):
        self.cards = []
    
    def __len__(self):
        return len(self.cards)
```

#### `__getitem__(self, key)` - Item Access

```python
def __getitem__(self, key):
    return self.cards[key]
```

#### `__setitem__(self, key, value)` - Item Assignment

```python
def __setitem__(self, key, value):
    self.cards[key] = value
```

#### `__delitem__(self, key)` - Item Deletion

```python
def __delitem__(self, key):
    del self.cards[key]
```

#### `__contains__(self, item)` - Membership Test (in)

```python
def __contains__(self, item):
    return item in self.cards
```

#### `__iter__(self)` - Iteration

```python
def __iter__(self):
    return iter(self.cards)
```

### Context Manager Methods

#### `__enter__(self)` - Enter Context

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
```

Usage:
```python
with FileManager('file.txt', 'w') as f:
    f.write('Hello, world!')
```

#### `__exit__(self, exc_type, exc_val, exc_tb)` - Exit Context

The `__exit__` method is called when exiting the context manager. It receives information about any exception that occurred:
- `exc_type`: The exception type, or None if no exception occurred
- `exc_val`: The exception value, or None
- `exc_tb`: The traceback, or None

If `__exit__` returns True, any exception is suppressed.

### Callable Objects

#### `__call__(self, ...)` - Call as Function

```python
class Adder:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return self.n + x
```

Usage:
```python
add5 = Adder(5)
print(add5(10))  # Output: 15
```

### Attribute Access

#### `__getattr__(self, name)` - Attribute Access Fallback

```python
class DynamicAttributes:
    def __init__(self):
        self.existing = "I exist"
    
    def __getattr__(self, name):
        return f"You tried to access {name}, but it doesn't exist"
```

`__getattr__` is called when an attribute lookup fails (i.e., the attribute doesn't exist).

#### `__getattribute__(self, name)` - All Attribute Access

```python
def __getattribute__(self, name):
    print(f"Getting {name}")
    return super().__getattribute__(name)
```

`__getattribute__` is called for all attribute access, even for attributes that exist. Be careful with this one, as it's easy to create infinite recursion.

#### `__setattr__(self, name, value)` - Attribute Assignment

```python
def __setattr__(self, name, value):
    print(f"Setting {name} to {value}")
    super().__setattr__(name, value)
```

#### `__delattr__(self, name)` - Attribute Deletion

```python
def __delattr__(self, name):
    print(f"Deleting {name}")
    super().__delattr__(name)
```

### Descriptors

Descriptors are objects that define how attribute access works. They implement one or more of the following methods:

#### `__get__(self, instance, owner)` - Get Attribute

```python
class Descriptor:
    def __get__(self, instance, owner):
        return f"Getting from {instance} with class {owner}"
```

#### `__set__(self, instance, value)` - Set Attribute

```python
def __set__(self, instance, value):
    print(f"Setting on {instance} to {value}")
```

#### `__delete__(self, instance)` - Delete Attribute

```python
def __delete__(self, instance):
    print(f"Deleting from {instance}")
```

### Type Conversion

#### `__int__(self)` - Convert to int

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __int__(self):
        return int(self.value)
```

Similar methods exist for other types: `__float__`, `__complex__`, `__bool__`, etc.

## Practical Examples

### Example 1: A Custom Number Class

```python
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Simplify the fraction
        gcd = self._gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        
        # Ensure denominator is positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def _gcd(self, a, b):
        """Calculate the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a
    
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator + 
                             other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self + Fraction(other, 1)
        return NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator - 
                             other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self - Fraction(other, 1)
        return NotImplemented
    
    def __rsub__(self, other):
        if isinstance(other, int):
            return Fraction(other, 1) - self
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator,
                           self.denominator * other.denominator)
        elif isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator,
                           self.denominator * other.numerator)
        elif isinstance(other, int):
            return Fraction(self.numerator, self.denominator * other)
        return NotImplemented
    
    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(other * self.denominator, self.numerator)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator == other.numerator and 
                    self.denominator == other.denominator)
        elif isinstance(other, int):
            return self == Fraction(other, 1)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator < 
                    other.numerator * self.denominator)
        elif isinstance(other, int):
            return self < Fraction(other, 1)
        return NotImplemented
    
    def __float__(self):
        return self.numerator / self.denominator
```

### Example 2: A Custom Container Class

```python
class SortedList:
    def __init__(self, items=None):
        self._items = []
        if items:
            self._items = sorted(items)
    
    def add(self, item):
        """Add an item and maintain sorted order."""
        # Find the insertion point
        i = 0
        while i < len(self._items) and self._items[i] < item:
            i += 1
        self._items.insert(i, item)
    
    def __str__(self):
        return str(self._items)
    
    def __repr__(self):
        return f"SortedList({self._items})"
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, key):
        return self._items[key]
    
    def __contains__(self, item):
        # We could use binary search for better performance
        return item in self._items
    
    def __iter__(self):
        return iter(self._items)
    
    def __add__(self, other):
        if isinstance(other, SortedList):
            # Merge two sorted lists
            result = SortedList()
            i, j = 0, 0
            while i < len(self) and j < len(other):
                if self[i] < other[j]:
                    result.add(self[i])
                    i += 1
                else:
                    result.add(other[j])
                    j += 1
            
            # Add remaining items
            while i < len(self):
                result.add(self[i])
                i += 1
            while j < len(other):
                result.add(other[j])
                j += 1
            
            return result
        return NotImplemented
```

### Example 3: A Context Manager for Database Connections

```python
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        # In a real implementation, this would connect to a database
        print(f"Connecting to database: {self.connection_string}")
        self.connection = {"connected": True}
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # In a real implementation, this would close the connection
        print("Closing database connection")
        self.connection = None
        
        # If we return True, any exception will be suppressed
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")
            # Return False to propagate the exception, True to suppress it
            return False
```

## Best Practices for Magic Methods

1. **Follow the principle of least surprise**: Make your objects behave as users would expect based on the operations you implement.

2. **Return NotImplemented for unsupported operations**: This allows Python to try the reflected operation or raise an appropriate error.

3. **Be consistent with built-in types**: If you implement `__eq__`, consider implementing `__hash__` as well, especially if your objects should be usable as dictionary keys.

4. **Document your magic methods**: Make it clear how your objects behave when used with various operations.

5. **Be careful with `__getattribute__` and `__setattr__`**: These are called for all attribute access, so it's easy to create infinite recursion.

6. **Implement related methods together**: If you implement `__eq__`, consider implementing other comparison methods. If you implement `__add__`, consider implementing `__radd__` as well.

7. **Use appropriate type checking**: Check that operands are of compatible types before performing operations.

8. **Keep magic methods simple and focused**: Each method should do one thing well.

## Conclusion

Magic methods are a powerful feature of Python that allow you to customize how your objects behave in various contexts. By implementing these methods, you can make your classes more intuitive and Pythonic, integrating seamlessly with Python's built-in functions and operators.

Understanding and using magic methods effectively is a key part of mastering object-oriented programming in Python. They allow you to create classes that behave like built-in types, making your code more readable and maintainable.

In the next lesson, we'll explore how to apply all the OOP concepts we've learned to build a comprehensive mini-project: a library management system.

## Further Reading

- [Python Documentation: Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Python Magic Methods](https://rszalski.github.io/magicmethods/)
- [Real Python: Operator and Function Overloading in Custom Python Classes](https://realpython.com/operator-function-overloading/)
- [Fluent Python](https://www.oreilly.com/library/view/fluent-python/9781491946237/) by Luciano Ramalho (book)