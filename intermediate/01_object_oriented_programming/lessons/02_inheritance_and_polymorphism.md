# Inheritance and Polymorphism in Python

## Introduction

Inheritance and polymorphism are two fundamental concepts in object-oriented programming that allow for code reuse, extensibility, and flexibility. In this lesson, we'll explore how to implement these concepts in Python and understand their benefits.

## Inheritance

Inheritance is a mechanism that allows a class to inherit attributes and methods from another class. The class that inherits is called a **subclass** (or derived class, child class), and the class being inherited from is called a **superclass** (or base class, parent class).

### Basic Inheritance

To create a subclass in Python, you specify the parent class in parentheses after the class name:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # This will be overridden by subclasses

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        return f"{self.name} says Meow!"
```

In this example:
- `Animal` is the parent class
- `Dog` and `Cat` are subclasses that inherit from `Animal`
- All classes have a `speak` method, but each implements it differently

### The `super()` Function

The `super()` function allows you to call methods from the parent class. This is particularly useful in the `__init__` method to ensure the parent's initialization code runs:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent's __init__ method
        self.breed = breed  # Add Dog-specific attribute
    
    def info(self):
        return f"{super().info()} and is a {self.breed}"
```

Using `super()` ensures that:
1. The parent class's initialization code runs
2. You don't have to repeat code that's already in the parent class
3. If the parent class changes, your subclass automatically inherits those changes

### Method Overriding

Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its parent class:

```python
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):  # This overrides Animal.make_sound
        return "Woof!"
```

When you call `make_sound()` on a `Dog` object, it uses the `Dog` implementation, not the `Animal` implementation.

### Extending Methods

Sometimes you want to extend a parent method rather than completely replace it. You can do this by calling the parent method using `super()` and then adding your own functionality:

```python
class Vehicle:
    def start(self):
        return "Engine starting"

class ElectricCar(Vehicle):
    def start(self):
        parent_result = super().start()
        return f"{parent_result} silently"
```

### Method Resolution Order (MRO)

When a class inherits from multiple classes, Python needs to determine the order in which to search for methods and attributes. This is called the Method Resolution Order (MRO).

Python uses the C3 linearization algorithm to determine the MRO. You can view the MRO of a class using the `__mro__` attribute or the `mro()` method:

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

The MRO determines which method gets called when you use `super()`.

## Multiple Inheritance

Python supports multiple inheritance, which means a class can inherit from more than one parent class:

```python
class Swimmer:
    def swim(self):
        return "Swimming"

class Flyer:
    def fly(self):
        return "Flying"

class Duck(Swimmer, Flyer):
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"{self.name} can {self.swim()} and {self.fly()}"
```

While multiple inheritance is powerful, it can lead to complexity and the "diamond problem" (when a class inherits from two classes that both inherit from a common base class). Python's MRO resolves this, but it's best to use multiple inheritance judiciously.

### Mixins

A common use case for multiple inheritance is the "mixin" pattern. A mixin is a class that provides methods to other classes but isn't meant to be instantiated on its own:

```python
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JSONSerializableMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print(user.to_json())  # Output: {"name": "Alice", "email": "alice@example.com"}
```

Mixins are a way to add functionality to a class without using inheritance for the "is-a" relationship.

## Polymorphism

Polymorphism means "many forms" and refers to the ability to use a single interface for different data types or classes. In Python, polymorphism is achieved through method overriding and duck typing.

### Method Overriding as Polymorphism

When different classes implement the same method, you can use objects of these classes interchangeably:

```python
def animal_sound(animal):
    return animal.speak()

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(animal_sound(dog))  # Output: Buddy says Woof!
print(animal_sound(cat))  # Output: Whiskers says Meow!
```

The `animal_sound` function works with any object that has a `speak` method, regardless of its class.

### Duck Typing

Python uses "duck typing" - if it walks like a duck and quacks like a duck, it's a duck. This means that the class of an object is less important than the methods and attributes it has:

```python
class Duck:
    def swim(self):
        return "Duck swimming"
    
    def quack(self):
        return "Quack!"

class Person:
    def swim(self):
        return "Person swimming"
    
    def quack(self):
        return "I'm imitating a duck!"

def make_it_quack(thing):
    return thing.quack()

duck = Duck()
person = Person()

print(make_it_quack(duck))    # Output: Quack!
print(make_it_quack(person))  # Output: I'm imitating a duck!
```

The `make_it_quack` function doesn't care about the class of the object, only that it has a `quack` method.

### Abstract Base Classes

Sometimes you want to define a common interface that subclasses must implement. Python provides Abstract Base Classes (ABCs) for this purpose:

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
- ABCs enforce a common interface across subclasses

To use ABCs, you need to:
1. Import `ABC` and `abstractmethod` from the `abc` module
2. Make your class inherit from `ABC`
3. Decorate methods that must be implemented with `@abstractmethod`

## Inheritance vs. Composition

While inheritance is powerful, it's not always the best solution. The principle "favor composition over inheritance" suggests that you should consider using composition (having objects as attributes) instead of inheritance when appropriate:

```python
# Inheritance approach
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying"

# Composition approach
class Movement:
    def fly(self):
        return "flying"
    
    def walk(self):
        return "walking"
    
    def swim(self):
        return "swimming"

class Animal:
    def __init__(self, name, movement):
        self.name = name
        self.movement = movement
    
    def move(self):
        return f"{self.name} is {self.movement()}"

bird = Animal("Sparrow", Movement().fly)
print(bird.move())  # Output: Sparrow is flying
```

Composition is more flexible because:
- It allows for changing behavior at runtime
- It avoids the complexity of deep inheritance hierarchies
- It doesn't suffer from the fragile base class problem

## Best Practices for Inheritance and Polymorphism

1. **Follow the Liskov Substitution Principle**: Subclasses should be substitutable for their base classes without altering the correctness of the program.

2. **Keep inheritance hierarchies shallow**: Deep inheritance hierarchies can be hard to understand and maintain.

3. **Use composition for "has-a" relationships**: If a class "has" something rather than "is" something, use composition instead of inheritance.

4. **Use mixins for reusable functionality**: Mixins are great for adding behavior without creating an "is-a" relationship.

5. **Document the expected interface**: When using polymorphism, document what methods and attributes are expected.

6. **Use abstract base classes to define interfaces**: ABCs make the required interface explicit.

7. **Avoid multiple inheritance when possible**: If you use multiple inheritance, keep it simple and be aware of the MRO.

## Example: A Complete Inheritance Hierarchy

Here's a more complete example demonstrating inheritance and polymorphism:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return f"{self.make} {self.model} started"
    
    def stop(self):
        self.is_running = False
        return f"{self.make} {self.model} stopped"
    
    @abstractmethod
    def fuel_type(self):
        pass
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class GasPoweredVehicle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency  # miles per gallon
    
    def fuel_type(self):
        return "Gasoline"
    
    def calculate_range(self, gallons):
        return self.fuel_efficiency * gallons

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity  # kWh
    
    def fuel_type(self):
        return "Electricity"
    
    def calculate_range(self, charge_percentage):
        # Simplified calculation
        return self.battery_capacity * charge_percentage * 3.5

class HybridVehicle(GasPoweredVehicle, ElectricVehicle):
    def __init__(self, make, model, year, fuel_efficiency, battery_capacity):
        Vehicle.__init__(self, make, model, year)  # Explicitly call Vehicle's __init__
        self.fuel_efficiency = fuel_efficiency
        self.battery_capacity = battery_capacity
    
    def fuel_type(self):
        return f"{GasPoweredVehicle.fuel_type(self)} and {ElectricVehicle.fuel_type(self)}"
    
    def calculate_range(self, gallons, charge_percentage):
        gas_range = self.fuel_efficiency * gallons
        electric_range = self.battery_capacity * charge_percentage * 3.5
        return gas_range + electric_range

# Usage
def print_vehicle_info(vehicle):
    print(f"Vehicle: {vehicle}")
    print(f"Fuel Type: {vehicle.fuel_type()}")
    
    if isinstance(vehicle, GasPoweredVehicle) and not isinstance(vehicle, HybridVehicle):
        print(f"Range with 10 gallons: {vehicle.calculate_range(10)} miles")
    elif isinstance(vehicle, ElectricVehicle) and not isinstance(vehicle, HybridVehicle):
        print(f"Range with 80% charge: {vehicle.calculate_range(0.8)} miles")
    elif isinstance(vehicle, HybridVehicle):
        print(f"Range with 10 gallons and 80% charge: {vehicle.calculate_range(10, 0.8)} miles")

# Create vehicles
sedan = GasPoweredVehicle("Toyota", "Camry", 2022, 32)
electric_car = ElectricVehicle("Tesla", "Model 3", 2022, 75)
hybrid_car = HybridVehicle("Toyota", "Prius", 2022, 50, 8.8)

# Print info using polymorphism
for vehicle in [sedan, electric_car, hybrid_car]:
    print_vehicle_info(vehicle)
    print()
```

## Conclusion

Inheritance and polymorphism are powerful tools in object-oriented programming that allow for code reuse, extensibility, and flexibility. Python's implementation of these concepts is particularly flexible, supporting multiple inheritance, mixins, and duck typing.

When used appropriately, inheritance creates clean, hierarchical relationships between classes, while polymorphism allows for writing code that works with different types in a uniform way. However, it's important to use these tools judiciously and consider alternatives like composition when appropriate.

In the next lesson, we'll explore encapsulation and abstraction, which are the other two fundamental principles of object-oriented programming.

## Further Reading

- [Python Documentation: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Python Documentation: Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Python's super() explained](https://realpython.com/python-super/)
- [Abstract Base Classes in Python](https://docs.python.org/3/library/abc.html)
- [Liskov Substitution Principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle)