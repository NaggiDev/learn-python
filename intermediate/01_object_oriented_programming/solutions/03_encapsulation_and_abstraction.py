"""
Solution: Encapsulation and Abstraction in Python

This file contains solutions to the exercises in 03_encapsulation_and_abstraction.py
"""

from abc import ABC, abstractmethod

# Exercise 1: Basic Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False


# Exercise 2: Properties with Validation
class Person:
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self._email = email
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer")
        self._age = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError("Email must contain '@'")
        self._email = value
    
    @property
    def full_info(self):
        return f"Name: {self._name}, Age: {self._age}, Email: {self._email}"


# Exercise 3: Abstract Base Class
class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @property
    @abstractmethod
    def fuel_type(self):
        pass
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def start_engine(self):
        return "The car engine starts"
    
    def stop_engine(self):
        return "The car engine stops"
    
    @property
    def fuel_type(self):
        return "Gasoline"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
    
    def start_engine(self):
        return "The motorcycle engine starts"
    
    def stop_engine(self):
        return "The motorcycle engine stops"
    
    @property
    def fuel_type(self):
        return "Gasoline"


# Exercise 4: Encapsulation with Private Methods
class PasswordManager:
    def __init__(self):
        self._passwords = {}
    
    def __encrypt_password(self, password):
        # Simple "encryption" - just reverse the string
        return password[::-1]
    
    def __decrypt_password(self, encrypted):
        # Simple "decryption" - reverse the string again
        return encrypted[::-1]
    
    def add_password(self, service, password):
        encrypted = self.__encrypt_password(password)
        self._passwords[service] = encrypted
    
    def get_password(self, service):
        if service in self._passwords:
            encrypted = self._passwords[service]
            return self.__decrypt_password(encrypted)
        return None
    
    def remove_password(self, service):
        if service in self._passwords:
            del self._passwords[service]


# Exercise 5: Combining Encapsulation and Abstraction
class DataProcessor(ABC):
    def __init__(self, data):
        self._data = data
    
    @property
    def data(self):
        return self._data.copy()
    
    @abstractmethod
    def process(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass
    
    def reset(self, data):
        self._data = data

class SortProcessor(DataProcessor):
    def __init__(self, data):
        super().__init__(data)
        self._result = None
    
    def process(self):
        self._result = sorted(self._data)
    
    def get_result(self):
        return self._result

class FilterProcessor(DataProcessor):
    def __init__(self, data, filter_func):
        super().__init__(data)
        self._filter_func = filter_func
        self._result = None
    
    def process(self):
        self._result = list(filter(self._filter_func, self._data))
    
    def get_result(self):
        return self._result


# Main execution and testing
if __name__ == "__main__":
    # Exercise 1 demo
    account = BankAccount("12345", 1000)
    print(f"Account {account.account_number} has balance ${account.balance}")
    
    account.deposit(500)
    print(f"After deposit: ${account.balance}")
    
    success = account.withdraw(800)
    print(f"Withdrawal successful: {success}, new balance: ${account.balance}")
    
    success = account.withdraw(1000)
    print(f"Withdrawal successful: {success}, balance unchanged: ${account.balance}")
    
    # Exercise 2 demo
    person = Person("Alice", 30, "alice@example.com")
    print(person.full_info)
    
    try:
        person.age = -5
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Exercise 3 demo
    car = Car("Toyota", "Camry", 2022, 4)
    motorcycle = Motorcycle("Honda", "CBR", 2022, False)
    
    print(car.get_info())
    print(f"Starting car: {car.start_engine()}")
    print(f"Car fuel type: {car.fuel_type}")
    
    print(motorcycle.get_info())
    print(f"Starting motorcycle: {motorcycle.start_engine()}")
    
    # Exercise 4 demo
    pm = PasswordManager()
    pm.add_password("gmail", "password123")
    
    print(f"Gmail password: {pm.get_password('gmail')}")
    
    pm.remove_password("gmail")
    print(f"After removal: {pm.get_password('gmail')}")
    
    # Exercise 5 demo
    sort_processor = SortProcessor([3, 1, 4, 1, 5, 9, 2, 6])
    sort_processor.process()
    print(f"Sorted data: {sort_processor.get_result()}")
    
    filter_processor = FilterProcessor([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
    filter_processor.process()
    print(f"Even numbers: {filter_processor.get_result()}")
    
    # Run the tests
    from importlib import reload
    import sys
    
    # Add the exercises directory to the path so we can import the test function
    sys.path.append('../exercises')
    
    try:
        import exercises.03_encapsulation_and_abstraction as exercises
        reload(exercises)  # Reload to get the latest version
        exercises.run_tests()
    except ImportError:
        print("Could not import the exercises module. Make sure you're running this from the solutions directory.")