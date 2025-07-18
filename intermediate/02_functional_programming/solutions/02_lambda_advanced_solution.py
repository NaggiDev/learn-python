"""
Advanced Lambda Functions - Solutions

This file contains the solutions for the advanced lambda functions exercises.
"""

from functools import reduce

# Exercise 1: Lambda Factory Functions
def create_multiplier(n):
    """Create a function that returns a lambda for multiplying by a specific number"""
    return lambda x: x * n

# Exercise 2: Lambda with Nested Conditionals
# Lambda that assigns letter grades based on numeric scores
grade_calculator = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'

# Exercise 3: Lambda for String Processing
# Lambda that processes a string by removing whitespace, converting to lowercase, and replacing spaces with underscores
string_processor = lambda s: s.strip().lower().replace(' ', '_')

# Exercise 4: Lambda with Dictionary Operations
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 75000},
    {'name': 'Bob', 'department': 'Marketing', 'salary': 65000},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 80000},
    {'name': 'Diana', 'department': 'Marketing', 'salary': 70000},
]
# Sort by department first, then by salary descending
sorted_employees = sorted(employees, key=lambda emp: (emp['department'], -emp['salary']))

# Exercise 5: Lambda for Data Transformation
users = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'},
    {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25, 'city': 'Los Angeles'},
    {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 35, 'city': 'Chicago'},
]
# Transform to format: "Last, First (Age) - City"
formatted_users = map(lambda user: f"{user['last_name']}, {user['first_name']} ({user['age']}) - {user['city']}", users)

# Exercise 6: Lambda for Filtering Complex Data
products = [
    {'name': 'Laptop', 'price': 999, 'category': 'Electronics', 'in_stock': True},
    {'name': 'Book', 'price': 25, 'category': 'Education', 'in_stock': True},
    {'name': 'Phone', 'price': 699, 'category': 'Electronics', 'in_stock': False},
    {'name': 'Desk', 'price': 299, 'category': 'Furniture', 'in_stock': True},
]
# Filter: Electronics category, price < 800, and in stock
filtered_products = filter(lambda p: p['category'] == 'Electronics' and p['price'] < 800 and p['in_stock'], products)

# Exercise 7: Lambda with Reduce
numbers = [2, 3, 4, 5]
# Use lambda with reduce to find the product of all numbers
product = reduce(lambda x, y: x * y, numbers)

# Exercise 8: Lambda for Grouping Data
def group_by_key(items, key_func):
    """Group items using the key_func"""
    result = {}
    for item in items:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

test_items = [
    {'name': 'Apple', 'type': 'Fruit', 'color': 'Red'},
    {'name': 'Banana', 'type': 'Fruit', 'color': 'Yellow'},
    {'name': 'Carrot', 'type': 'Vegetable', 'color': 'Orange'},
    {'name': 'Broccoli', 'type': 'Vegetable', 'color': 'Green'},
]

# Group by type using lambda
grouped_by_type = group_by_key(test_items, lambda item: item['type'])

# Exercise 9: Lambda for Mathematical Operations
math_operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else float('inf'),
    'power': lambda x, y: x ** y,
}

# Exercise 10: Lambda for Data Validation
validators = {
    'email': lambda email: '@' in email and '.' in email.split('@')[1] if '@' in email else False,
    'phone': lambda phone: phone.isdigit() and len(phone) == 10,
    'password': lambda pwd: len(pwd) >= 8 and any(c.isdigit() for c in pwd) and any(c.isalpha() for c in pwd),
}

# Test data for validation
test_data = {
    'emails': ['user@example.com', 'invalid-email', 'test@domain.org', 'no-at-sign'],
    'phones': ['1234567890', '123-456-7890', '12345', 'abcdefghij'],
    'passwords': ['Password123', 'weak', 'NoDigits!', '12345678', 'Strong1Pass']
}

def demonstrate_solutions():
    """Demonstrate all the advanced lambda function solutions"""
    print("Advanced Lambda Functions Solutions Demonstration\n")
    
    # Exercise 1
    print("1. Lambda Factory Functions:")
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print(f"   double(5) = {double(5)}")
    print(f"   triple(4) = {triple(4)}")
    
    # Exercise 2
    print("\n2. Grade Calculator:")
    test_scores = [95, 85, 75, 65, 55]
    for score in test_scores:
        print(f"   Score {score}: {grade_calculator(score)}")
    
    # Exercise 3
    print("\n3. String Processor:")
    test_strings = ["  Hello World  ", "Python Programming", "  Test String  "]
    for s in test_strings:
        print(f"   '{s}' -> '{string_processor(s)}'")
    
    # Exercise 4
    print("\n4. Sorted Employees:")
    for emp in sorted_employees:
        print(f"   {emp['name']} - {emp['department']} - ${emp['salary']}")
    
    # Exercise 5
    print("\n5. Formatted Users:")
    for user in formatted_users:
        print(f"   {user}")
    
    # Exercise 6
    print("\n6. Filtered Products:")
    filtered_list = list(filtered_products)
    if filtered_list:
        for product in filtered_list:
            print(f"   {product['name']} - ${product['price']}")
    else:
        print("   No products match the criteria")
    
    # Exercise 7
    print(f"\n7. Product of {numbers}: {product}")
    
    # Exercise 8
    print("\n8. Grouped Items:")
    for group_type, items in grouped_by_type.items():
        print(f"   {group_type}: {[item['name'] for item in items]}")
    
    # Exercise 9
    print("\n9. Mathematical Operations:")
    print(f"   add(5, 3) = {math_operations['add'](5, 3)}")
    print(f"   subtract(10, 4) = {math_operations['subtract'](10, 4)}")
    print(f"   multiply(6, 7) = {math_operations['multiply'](6, 7)}")
    print(f"   divide(15, 3) = {math_operations['divide'](15, 3)}")
    print(f"   divide(10, 0) = {math_operations['divide'](10, 0)}")
    print(f"   power(2, 3) = {math_operations['power'](2, 3)}")
    
    # Exercise 10
    print("\n10. Data Validation:")
    print("   Email validation:")
    for email in test_data['emails']:
        result = validators['email'](email)
        print(f"     {email}: {'Valid' if result else 'Invalid'}")
    
    print("   Phone validation:")
    for phone in test_data['phones']:
        result = validators['phone'](phone)
        print(f"     {phone}: {'Valid' if result else 'Invalid'}")
    
    print("   Password validation:")
    for password in test_data['passwords']:
        result = validators['password'](password)
        print(f"     {password}: {'Valid' if result else 'Invalid'}")

def additional_advanced_examples():
    """Show additional advanced lambda examples"""
    print("\n" + "="*60)
    print("Additional Advanced Lambda Examples")
    print("="*60)
    
    # Example 1: Lambda with closures
    print("\n1. Lambda with Closures:")
    def create_counter(start=0):
        count = [start]  # Use list to make it mutable in closure
        return lambda: count.__setitem__(0, count[0] + 1) or count[0]
    
    counter1 = create_counter(10)
    counter2 = create_counter(100)
    print(f"   Counter1: {counter1()}, {counter1()}, {counter1()}")
    print(f"   Counter2: {counter2()}, {counter2()}")
    
    # Example 2: Lambda for functional composition
    print("\n2. Function Composition with Lambda:")
    compose = lambda f, g: lambda x: f(g(x))
    
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    
    # Compose functions: first multiply by 2, then add 1
    composed_func = compose(add_one, multiply_by_two)
    print(f"   compose(add_one, multiply_by_two)(5) = {composed_func(5)}")  # (5*2)+1 = 11
    
    # Example 3: Lambda for currying
    print("\n3. Currying with Lambda:")
    curry_add = lambda x: lambda y: x + y
    add_five = curry_add(5)
    print(f"   curry_add(5)(3) = {add_five(3)}")
    
    # Example 4: Lambda for memoization (simple case)
    print("\n4. Simple Memoization with Lambda:")
    def memoize(func):
        cache = {}
        return lambda x: cache.setdefault(x, func(x))
    
    # Expensive function (simulated)
    expensive_func = lambda x: x ** 2 + x * 10  # Simple example
    memoized_func = memoize(expensive_func)
    
    print(f"   First call memoized_func(5): {memoized_func(5)}")
    print(f"   Second call memoized_func(5): {memoized_func(5)}")  # Retrieved from cache
    
    # Example 5: Lambda for event handling simulation
    print("\n5. Event Handling with Lambda:")
    events = []
    
    # Create event handlers using lambda
    on_click = lambda element: events.append(f"Clicked {element}")
    on_hover = lambda element: events.append(f"Hovered {element}")
    
    # Simulate events
    on_click("Button1")
    on_hover("Link1")
    on_click("Button2")
    
    print("   Events:")
    for event in events:
        print(f"     {event}")

if __name__ == "__main__":
    demonstrate_solutions()
    additional_advanced_examples()