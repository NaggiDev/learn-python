# Encapsulation and Abstraction in Python

## Introduction

Encapsulation and abstraction are two fundamental principles of object-oriented programming that help create more maintainable, secure, and well-structured code. In this lesson, we'll explore how to implement these concepts in Python and understand their benefits.

## Encapsulation

Encapsulation is the bundling of data (attributes) and methods that operate on that data within a single unit (a class), and restricting access to some of the object's components. It's about hiding the internal state and requiring all interaction to be performed through an object's methods.

### Why Encapsulation Matters

1. **Data Protection**: Prevents accidental modification of data
2. **Controlled Access**: Provides controlled ways to modify data
3. **Flexibility**: Allows changing implementation without affecting the interface
4. **Maintainability**: Makes code easier to maintain and understand

### Access Modifiers in Python

Unlike many other OOP languages, Python doesn't have strict access modifiers (like `private`, `protected`, `public`). Instead, it follows a convention-based approach:

1. **Public**: Regular attributes and methods (no special prefix)
2. **Protected**: Attributes and methods prefixed with a single underscore (`_`)
3. **Private**: Attributes and methods prefixed with double underscores (`__`)

Let's see how these work:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner           # Public attribute
        self._balance = balance      # Protected attribute
        self.__transaction_log = []  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction("deposit", amount)
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__log_transaction("withdrawal", amount)
            return True
        return False
    
    def get_balance(self):
        return self._balance
    
    def __log_transaction(self, transaction_type, amount):
        import datetime
        self.__transaction_log.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.datetime.now()
        })
    
    def get_transaction_history(self):
        # Return a copy to prevent modification
        return self.__transaction_log.copy()
```

In this example:
- `owner` is public and can be accessed directly
- `_balance` is protected, suggesting it should not be accessed directly (though it can be)
- `__transaction_log` is private and cannot be accessed directly from outside the class
- `__log_transaction` is a private method that can only be called from within the class

### Name Mangling for Private Attributes

When you use double underscores (`__`), Python performs "name mangling" to make the attribute harder to access from outside the class. The attribute is renamed to `_ClassName__attribute`:

```python
account = BankAccount("Alice", 1000)
print(account.owner)                # Works: Alice
print(account._balance)             # Works (but shouldn't do this): 1000
# print(account.__transaction_log)  # Error: attribute doesn't exist

# But you can still access it if you know the mangled name
print(account._BankAccount__transaction_log)  # Works: []
```

This isn't true privacy but makes accidental access less likely.

### Properties for Controlled Access

A better way to implement encapsulation in Python is to use properties. Properties allow you to define methods that behave like attributes, giving you control over getting, setting, and deleting values:

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    @property
    def is_adult(self):
        return self._age >= 18
```

Using properties:

```python
person = Person("Alice", 30)

# Accessing properties
print(person.name)    # Alice
print(person.age)     # 30
print(person.is_adult)  # True

# Setting properties
person.name = "Bob"   # Uses the setter
person.age = 25       # Uses the setter

# Validation
try:
    person.age = -5   # Raises ValueError
except ValueError as e:
    print(e)          # Age cannot be negative

# Read-only property
# person.is_adult = False  # AttributeError: can't set attribute
```

Properties provide several benefits:
1. They look like attributes but act like methods
2. They allow for validation when setting values
3. They can compute values on-the-fly
4. They maintain backward compatibility if implementation changes

### Property Decorators

The `@property` decorator is a shorthand for using the `property()` function. Here's how the decorators work:

1. `@property`: Defines a getter method
2. `@attribute.setter`: Defines a setter method
3. `@attribute.deleter`: Defines a deleter method

```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        self.celsius = value - 273.15
```

This class encapsulates temperature conversion logic and ensures valid temperatures.

## Abstraction

Abstraction is the concept of hiding complex implementation details and showing only the necessary features of an object. It helps manage complexity by hiding unnecessary details from the user.

### Why Abstraction Matters

1. **Simplicity**: Users only need to know what an object does, not how it does it
2. **Reduced Complexity**: Hides implementation details, making the interface simpler
3. **Modularity**: Allows changing implementation without affecting users
4. **Focus**: Lets you focus on what an object does rather than how it works

### Implementing Abstraction in Python

There are several ways to implement abstraction in Python:

1. **Abstract Base Classes (ABCs)**: Define interfaces that derived classes must implement
2. **Encapsulation**: Hide implementation details through private methods and attributes
3. **Interfaces**: Define what methods a class should have without specifying implementation

### Abstract Base Classes

Python's `abc` module provides tools for defining Abstract Base Classes:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return f"This shape has an area of {self.area()} and a perimeter of {self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
```

Key points about ABCs:
- You cannot instantiate an abstract class
- Subclasses must implement all abstract methods
- Abstract methods are defined with the `@abstractmethod` decorator
- ABCs can have concrete methods (like `describe` above)

### Abstract Properties

You can also define abstract properties:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @property
    @abstractmethod
    def max_speed(self):
        pass
    
    @abstractmethod
    def start(self):
        pass
    
    def describe(self):
        return f"This vehicle has a maximum speed of {self.max_speed} km/h"

class Car(Vehicle):
    @property
    def max_speed(self):
        return 200
    
    def start(self):
        return "Car engine started"
```

### Interfaces in Python

Python doesn't have a formal interface concept like Java, but ABCs effectively serve the same purpose. An interface in Python is typically an ABC with only abstract methods:

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Resizable(ABC):
    @abstractmethod
    def resize(self, width, height):
        pass

class UIElement(Drawable, Resizable):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        return f"Drawing element at ({self.x}, {self.y}) with size {self.width}x{self.height}"
    
    def resize(self, width, height):
        self.width = width
        self.height = height
        return f"Resized to {width}x{height}"
```

In this example, `Drawable` and `Resizable` are interfaces that `UIElement` implements.

### Duck Typing and Informal Interfaces

Python often relies on "duck typing" rather than formal interfaces. If an object has the methods and attributes you need, you can use it regardless of its class:

```python
def draw_elements(elements):
    for element in elements:
        print(element.draw())  # Works for any object with a draw() method

class Button:
    def draw(self):
        return "Drawing a button"

class Image:
    def draw(self):
        return "Drawing an image"

draw_elements([Button(), Image()])  # Works fine without formal interfaces
```

This approach is more flexible but provides fewer guarantees at compile time.

### Protocol Classes (Python 3.8+)

Python 3.8 introduced Protocol classes in the `typing` module, which provide a way to define interfaces for static type checking:

```python
from typing import Protocol, List

class Drawable(Protocol):
    def draw(self) -> str:
        ...

def draw_elements(elements: List[Drawable]) -> None:
    for element in elements:
        print(element.draw())

class Button:
    def draw(self) -> str:
        return "Drawing a button"

draw_elements([Button()])  # Type checker will verify Button implements draw()
```

Protocols are checked by static type checkers like mypy but don't enforce anything at runtime.

## Combining Encapsulation and Abstraction

Encapsulation and abstraction work together to create well-designed classes:

```python
from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self, connection_string):
        self._connection_string = connection_string
        self._connection = None
    
    def connect(self):
        if self._connection is None:
            self._connection = self._create_connection()
        return self._connection
    
    @abstractmethod
    def _create_connection(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    def __del__(self):
        if self._connection:
            self._close_connection()
    
    @abstractmethod
    def _close_connection(self):
        pass

class SQLiteDatabase(Database):
    def _create_connection(self):
        import sqlite3
        return sqlite3.connect(self._connection_string)
    
    def execute_query(self, query):
        cursor = self.connect().cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def _close_connection(self):
        if self._connection:
            self._connection.close()

class PostgreSQLDatabase(Database):
    def _create_connection(self):
        import psycopg2
        return psycopg2.connect(self._connection_string)
    
    def execute_query(self, query):
        cursor = self.connect().cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def _close_connection(self):
        if self._connection:
            self._connection.close()
```

In this example:
- `Database` is an abstract class that defines the interface
- Implementation details are encapsulated in private methods
- Concrete classes implement the abstract methods
- Users only need to know about `connect()` and `execute_query()`

## Best Practices for Encapsulation and Abstraction

### Encapsulation Best Practices

1. **Use properties instead of direct attribute access** for attributes that need validation or computation
2. **Make attributes private or protected** if they shouldn't be accessed directly
3. **Provide public methods** for interacting with the object's state
4. **Document the intended access level** of attributes and methods
5. **Don't expose implementation details** in your public interface

### Abstraction Best Practices

1. **Define clear interfaces** using abstract base classes
2. **Keep interfaces minimal** - only include what's necessary
3. **Separate interface from implementation** - users should only need to know the interface
4. **Use meaningful method names** that describe what they do, not how they do it
5. **Document the expected behavior** of abstract methods

## Example: A Complete Implementation

Here's a more complete example demonstrating encapsulation and abstraction:

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class PaymentProcessor(ABC):
    """Abstract base class for payment processing."""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process a payment.
        
        Args:
            amount: The payment amount
            
        Returns:
            bool: True if payment was successful, False otherwise
        """
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> bool:
        """Refund a payment.
        
        Args:
            transaction_id: The ID of the transaction to refund
            amount: The amount to refund
            
        Returns:
            bool: True if refund was successful, False otherwise
        """
        pass
    
    @property
    @abstractmethod
    def payment_method(self) -> str:
        """Get the payment method name."""
        pass

class CreditCardProcessor(PaymentProcessor):
    """Payment processor for credit cards."""
    
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._transactions: List[Dict[str, Any]] = []
    
    @property
    def payment_method(self) -> str:
        return "Credit Card"
    
    def process_payment(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
        
        # In a real implementation, this would call a payment gateway API
        success = self._call_payment_gateway(amount)
        
        if success:
            transaction_id = self._generate_transaction_id()
            self._transactions.append({
                "id": transaction_id,
                "amount": amount,
                "type": "payment",
                "status": "completed"
            })
        
        return success
    
    def refund_payment(self, transaction_id: str, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Refund amount must be positive")
        
        transaction = self._find_transaction(transaction_id)
        if not transaction:
            return False
        
        if transaction["amount"] < amount:
            raise ValueError("Refund amount cannot exceed original payment")
        
        # In a real implementation, this would call a payment gateway API
        success = self._call_refund_gateway(transaction_id, amount)
        
        if success:
            self._transactions.append({
                "id": self._generate_transaction_id(),
                "original_transaction_id": transaction_id,
                "amount": amount,
                "type": "refund",
                "status": "completed"
            })
        
        return success
    
    def get_transaction_history(self) -> List[Dict[str, Any]]:
        """Get a copy of the transaction history.
        
        Returns:
            List[Dict[str, Any]]: A list of transaction records
        """
        return self._transactions.copy()
    
    def _find_transaction(self, transaction_id: str) -> Optional[Dict[str, Any]]:
        """Find a transaction by ID.
        
        Args:
            transaction_id: The transaction ID to find
            
        Returns:
            Optional[Dict[str, Any]]: The transaction if found, None otherwise
        """
        for transaction in self._transactions:
            if transaction["id"] == transaction_id:
                return transaction
        return None
    
    def _call_payment_gateway(self, amount: float) -> bool:
        """Call the payment gateway API to process a payment.
        
        Args:
            amount: The payment amount
            
        Returns:
            bool: True if payment was successful, False otherwise
        """
        # Simulate API call
        print(f"Calling payment gateway with API key {self._api_key[:4]}... to process ${amount}")
        return True  # Assume success
    
    def _call_refund_gateway(self, transaction_id: str, amount: float) -> bool:
        """Call the payment gateway API to process a refund.
        
        Args:
            transaction_id: The original transaction ID
            amount: The refund amount
            
        Returns:
            bool: True if refund was successful, False otherwise
        """
        # Simulate API call
        print(f"Calling refund gateway with API key {self._api_key[:4]}... to refund ${amount} for transaction {transaction_id}")
        return True  # Assume success
    
    def _generate_transaction_id(self) -> str:
        """Generate a unique transaction ID.
        
        Returns:
            str: A unique transaction ID
        """
        import uuid
        return str(uuid.uuid4())

class PayPalProcessor(PaymentProcessor):
    """Payment processor for PayPal."""
    
    def __init__(self, client_id: str, client_secret: str):
        self._client_id = client_id
        self._client_secret = client_secret
        self._transactions: List[Dict[str, Any]] = []
    
    @property
    def payment_method(self) -> str:
        return "PayPal"
    
    def process_payment(self, amount: float) -> bool:
        # Implementation similar to CreditCardProcessor but using PayPal API
        # ...
        return True
    
    def refund_payment(self, transaction_id: str, amount: float) -> bool:
        # Implementation similar to CreditCardProcessor but using PayPal API
        # ...
        return True

class Order:
    """A class representing a customer order."""
    
    def __init__(self, order_id: str, customer_name: str, amount: float):
        self._order_id = order_id
        self._customer_name = customer_name
        self._amount = amount
        self._status = "pending"
        self._payment_processor: Optional[PaymentProcessor] = None
        self._transaction_id: Optional[str] = None
    
    @property
    def order_id(self) -> str:
        return self._order_id
    
    @property
    def customer_name(self) -> str:
        return self._customer_name
    
    @property
    def amount(self) -> float:
        return self._amount
    
    @property
    def status(self) -> str:
        return self._status
    
    def set_payment_processor(self, processor: PaymentProcessor) -> None:
        """Set the payment processor for this order.
        
        Args:
            processor: The payment processor to use
        """
        self._payment_processor = processor
    
    def process(self) -> bool:
        """Process the order payment.
        
        Returns:
            bool: True if payment was successful, False otherwise
            
        Raises:
            ValueError: If no payment processor has been set
        """
        if not self._payment_processor:
            raise ValueError("Payment processor not set")
        
        success = self._payment_processor.process_payment(self._amount)
        
        if success:
            self._status = "paid"
            # In a real implementation, we would store the transaction ID
            self._transaction_id = "tx_123456"
        
        return success
    
    def refund(self) -> bool:
        """Refund the order payment.
        
        Returns:
            bool: True if refund was successful, False otherwise
            
        Raises:
            ValueError: If the order is not in 'paid' status or no transaction ID exists
        """
        if self._status != "paid":
            raise ValueError("Cannot refund an order that is not paid")
        
        if not self._transaction_id:
            raise ValueError("No transaction ID available for refund")
        
        if not self._payment_processor:
            raise ValueError("Payment processor not set")
        
        success = self._payment_processor.refund_payment(self._transaction_id, self._amount)
        
        if success:
            self._status = "refunded"
        
        return success
```

## Conclusion

Encapsulation and abstraction are powerful principles in object-oriented programming that help create more maintainable, flexible, and robust code. Python provides several mechanisms for implementing these principles, including property decorators, name mangling, and abstract base classes.

By properly encapsulating your data and providing clear abstractions, you can create classes that are easier to use, maintain, and extend. These principles are essential for building complex systems that can evolve over time without breaking existing code.

In the next lesson, we'll explore Python's magic methods, which allow you to customize how your objects behave in various contexts.

## Further Reading

- [Python Documentation: Property Decorators](https://docs.python.org/3/library/functions.html#property)
- [Python Documentation: Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Python Documentation: Protocol Classes](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [Real Python: Object-Oriented Programming in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Python's @property Decorator](https://realpython.com/python-property/)