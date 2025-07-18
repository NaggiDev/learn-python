"""
Exercise: Inheritance and Polymorphism in Python

Instructions:
1. Complete the exercises below by implementing the required classes and methods
2. Run this file to test your implementation
3. All tests should pass with no errors

Learning objectives:
- Implement inheritance hierarchies
- Override methods in derived classes
- Use super() to call parent class methods
- Apply polymorphic behavior through method overriding
- Work with abstract base classes
"""

from abc import ABC, abstractmethod

# Exercise 1: Basic Inheritance
# Create a base class 'Animal' with:
# - An __init__ method that takes a name parameter
# - A speak method that returns "Animal sound"
# Then create two subclasses, 'Dog' and 'Cat', that:
# - Inherit from Animal
# - Override the speak method to return "Woof!" for Dog and "Meow!" for Cat
# TODO: Implement the Animal, Dog, and Cat classes


# Exercise 2: Using super()
# Create a base class 'Person' with:
# - An __init__ method that takes name and age parameters
# - A introduce method that returns "Hi, I'm {name} and I'm {age} years old."
# Then create a subclass 'Student' that:
# - Inherits from Person
# - Adds a student_id parameter to __init__
# - Uses super() to call the parent's __init__ method
# - Overrides the introduce method to return the parent's introduction plus " I'm a student with ID: {student_id}."
# TODO: Implement the Person and Student classes


# Exercise 3: Multiple Inheritance
# Create three classes:
# 1. 'Swimmer' with a swim method that returns "Swimming"
# 2. 'Flyer' with a fly method that returns "Flying"
# 3. 'Duck' that inherits from both Swimmer and Flyer and has:
#    - An __init__ method that takes a name parameter
#    - A describe method that returns "{name} can {swim()} and {fly()}"
# TODO: Implement the Swimmer, Flyer, and Duck classes


# Exercise 4: Polymorphism
# Create a base class 'Shape' with:
# - An abstract method area()
# - An abstract method perimeter()
# Then create two subclasses:
# 1. 'Rectangle' with:
#    - An __init__ method that takes width and height parameters
#    - Implementations of area() and perimeter()
# 2. 'Circle' with:
#    - An __init__ method that takes a radius parameter
#    - Implementations of area() and perimeter()
# Also create a function calculate_total_area that:
# - Takes a list of shapes
# - Returns the sum of all their areas
# TODO: Implement the Shape, Rectangle, and Circle classes and the calculate_total_area function


# Exercise 5: Method Resolution Order
# Create the following classes:
# 1. 'A' with a method who_am_i() that returns "I am A"
# 2. 'B' that inherits from A and overrides who_am_i() to return "I am B"
# 3. 'C' that inherits from A and overrides who_am_i() to return "I am C"
# 4. 'D' that inherits from B and C (in that order) and does not override who_am_i()
# Then create a function what_am_i that:
# - Takes an instance of any of these classes
# - Returns the result of calling who_am_i() on that instance
# TODO: Implement the A, B, C, and D classes and the what_am_i function


# Test code - DO NOT MODIFY
def run_tests():
    import math
    print("Running tests...")
    
    # Test Exercise 1: Basic Inheritance
    try:
        animal = Animal("Generic Animal")
        dog = Dog("Buddy")
        cat = Cat("Whiskers")
        
        assert animal.speak() == "Animal sound"
        assert dog.speak() == "Woof!"
        assert cat.speak() == "Meow!"
        assert isinstance(dog, Animal)
        assert isinstance(cat, Animal)
        
        print("✓ Exercise 1 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 1 failed: {e}")
    
    # Test Exercise 2: Using super()
    try:
        person = Person("John", 30)
        student = Student("Alice", 20, "A12345")
        
        assert person.introduce() == "Hi, I'm John and I'm 30 years old."
        assert student.introduce() == "Hi, I'm Alice and I'm 20 years old. I'm a student with ID: A12345."
        assert isinstance(student, Person)
        
        print("✓ Exercise 2 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 2 failed: {e}")
    
    # Test Exercise 3: Multiple Inheritance
    try:
        swimmer = Swimmer()
        flyer = Flyer()
        duck = Duck("Donald")
        
        assert swimmer.swim() == "Swimming"
        assert flyer.fly() == "Flying"
        assert duck.swim() == "Swimming"
        assert duck.fly() == "Flying"
        assert duck.describe() == "Donald can Swimming and Flying"
        assert isinstance(duck, Swimmer)
        assert isinstance(duck, Flyer)
        
        print("✓ Exercise 3 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 3 failed: {e}")
    
    # Test Exercise 4: Polymorphism
    try:
        # Verify Shape is abstract
        try:
            shape = Shape()
            assert False, "Should not be able to instantiate abstract class"
        except TypeError:
            pass
        
        rect = Rectangle(5, 10)
        circle = Circle(7)
        
        assert rect.area() == 50
        assert rect.perimeter() == 30
        assert abs(circle.area() - 153.93804) < 0.00001
        assert abs(circle.perimeter() - 43.9822971) < 0.00001
        
        shapes = [rect, circle, Rectangle(3, 4), Circle(5)]
        total_area = calculate_total_area(shapes)
        expected_area = 50 + 153.93804 + 12 + 78.53981633974483
        assert abs(total_area - expected_area) < 0.00001
        
        print("✓ Exercise 4 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 4 failed: {e}")
    
    # Test Exercise 5: Method Resolution Order
    try:
        a = A()
        b = B()
        c = C()
        d = D()
        
        assert a.who_am_i() == "I am A"
        assert b.who_am_i() == "I am B"
        assert c.who_am_i() == "I am C"
        assert d.who_am_i() == "I am B"  # Should follow MRO: D -> B -> C -> A
        
        assert what_am_i(a) == "I am A"
        assert what_am_i(b) == "I am B"
        assert what_am_i(c) == "I am C"
        assert what_am_i(d) == "I am B"
        
        print("✓ Exercise 5 passed!")
    except (AssertionError, AttributeError, NameError) as e:
        print(f"✗ Exercise 5 failed: {e}")
    
    print("Tests completed!")

if __name__ == "__main__":
    run_tests()