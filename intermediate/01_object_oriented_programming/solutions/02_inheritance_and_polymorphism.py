"""
Solution: Inheritance and Polymorphism in Python

This file contains solutions to the exercises in 02_inheritance_and_polymorphism.py
"""

from abc import ABC, abstractmethod
import math

# Exercise 1: Basic Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


# Exercise 2: Using super()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def introduce(self):
        return f"{super().introduce()} I'm a student with ID: {self.student_id}."


# Exercise 3: Multiple Inheritance
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


# Exercise 4: Polymorphism
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
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

def calculate_total_area(shapes):
    return sum(shape.area() for shape in shapes)


# Exercise 5: Method Resolution Order
class A:
    def who_am_i(self):
        return "I am A"

class B(A):
    def who_am_i(self):
        return "I am B"

class C(A):
    def who_am_i(self):
        return "I am C"

class D(B, C):
    pass  # D inherits who_am_i from B due to MRO

def what_am_i(obj):
    return obj.who_am_i()


# Main execution and testing
if __name__ == "__main__":
    # Exercise 1 demo
    animal = Animal("Generic Animal")
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    print(f"Animal says: {animal.speak()}")
    print(f"{dog.name} says: {dog.speak()}")
    print(f"{cat.name} says: {cat.speak()}")
    
    # Exercise 2 demo
    person = Person("John", 30)
    student = Student("Alice", 20, "A12345")
    
    print(person.introduce())
    print(student.introduce())
    
    # Exercise 3 demo
    duck = Duck("Donald")
    print(duck.describe())
    
    # Exercise 4 demo
    rect = Rectangle(5, 10)
    circle = Circle(7)
    
    print(f"Rectangle area: {rect.area()}, perimeter: {rect.perimeter()}")
    print(f"Circle area: {circle.area():.2f}, perimeter: {circle.perimeter():.2f}")
    
    shapes = [rect, circle, Rectangle(3, 4), Circle(5)]
    print(f"Total area of all shapes: {calculate_total_area(shapes):.2f}")
    
    # Exercise 5 demo
    a = A()
    b = B()
    c = C()
    d = D()
    
    print(f"A says: {what_am_i(a)}")
    print(f"B says: {what_am_i(b)}")
    print(f"C says: {what_am_i(c)}")
    print(f"D says: {what_am_i(d)}")
    
    # Show MRO for D
    print(f"Method Resolution Order for D: {[cls.__name__ for cls in D.__mro__]}")
    
    # Run the tests
    from importlib import reload
    import sys
    
    # Add the exercises directory to the path so we can import the test function
    sys.path.append('../exercises')
    
    try:
        import exercises.02_inheritance_and_polymorphism as exercises
        reload(exercises)  # Reload to get the latest version
        exercises.run_tests()
    except ImportError:
        print("Could not import the exercises module. Make sure you're running this from the solutions directory.")