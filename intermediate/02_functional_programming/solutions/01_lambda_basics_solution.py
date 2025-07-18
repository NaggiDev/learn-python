"""
Lambda Functions - Solutions

This file contains the solutions for the lambda functions exercises.
Study these solutions to understand the correct implementation.
"""

# Exercise 1: Basic Lambda Creation
# Create a lambda function that doubles a number
double = lambda x: x * 2

# Exercise 2: Lambda with Multiple Arguments
# Create a lambda function that calculates the area of a rectangle
rectangle_area = lambda length, width: length * width

# Exercise 3: Lambda with Conditional Logic
# Create a lambda function that returns the absolute value of a number
absolute_value = lambda x: x if x >= 0 else -x

# Exercise 4: Lambda for String Operations
# Create a lambda function that capitalizes the first letter of a string
capitalize_first = lambda s: s.capitalize()

# Exercise 5: Lambda with Default Arguments
# Create a lambda function that raises a number to a power (default power is 2)
power = lambda base, exp=2: base ** exp

# Exercise 6: Using Lambda with Built-in Functions
# Use lambda with map() to convert temperatures from Celsius to Fahrenheit
celsius_temps = [0, 20, 30, 40, 100]
fahrenheit_temps = map(lambda c: c * 9/5 + 32, celsius_temps)

# Exercise 7: Using Lambda with Filter
# Use lambda with filter() to get only positive numbers from a list
numbers = [-5, -2, 0, 3, 8, -1, 7]
positive_numbers = filter(lambda x: x > 0, numbers)

# Exercise 8: Using Lambda with Sorted
# Use lambda with sorted() to sort a list of tuples by the second element
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 96)]
sorted_students = sorted(students, key=lambda student: student[1])

# Exercise 9: Complex Lambda with Conditional
# Create a lambda function that categorizes numbers as 'positive', 'negative', or 'zero'
categorize_number = lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'zero'

# Exercise 10: Lambda for Data Processing
# Extract and uppercase the 'name' field from each dictionary
people = [
    {'name': 'john', 'age': 25},
    {'name': 'jane', 'age': 30},
    {'name': 'bob', 'age': 35}
]
uppercase_names = map(lambda person: person['name'].upper(), people)

# Demonstration of solutions
def demonstrate_solutions():
    """Demonstrate all the lambda function solutions"""
    print("Lambda Functions Solutions Demonstration\n")
    
    # Exercise 1
    print("1. Double function:")
    print(f"   double(5) = {double(5)}")
    print(f"   double(-3) = {double(-3)}")
    
    # Exercise 2
    print("\n2. Rectangle area:")
    print(f"   rectangle_area(5, 3) = {rectangle_area(5, 3)}")
    print(f"   rectangle_area(10, 2) = {rectangle_area(10, 2)}")
    
    # Exercise 3
    print("\n3. Absolute value:")
    print(f"   absolute_value(-5) = {absolute_value(-5)}")
    print(f"   absolute_value(3) = {absolute_value(3)}")
    
    # Exercise 4
    print("\n4. Capitalize first:")
    print(f"   capitalize_first('hello') = '{capitalize_first('hello')}'")
    print(f"   capitalize_first('python') = '{capitalize_first('python')}'")
    
    # Exercise 5
    print("\n5. Power function:")
    print(f"   power(5) = {power(5)}")  # Default power of 2
    print(f"   power(3, 3) = {power(3, 3)}")
    print(f"   power(2, 4) = {power(2, 4)}")
    
    # Exercise 6
    print("\n6. Celsius to Fahrenheit:")
    print(f"   Celsius: {celsius_temps}")
    print(f"   Fahrenheit: {list(fahrenheit_temps)}")
    
    # Exercise 7
    print("\n7. Positive numbers:")
    print(f"   Original: {numbers}")
    print(f"   Positive: {list(positive_numbers)}")
    
    # Exercise 8
    print("\n8. Sorted students:")
    print(f"   Original: {students}")
    print(f"   Sorted by grade: {sorted_students}")
    
    # Exercise 9
    print("\n9. Number categorization:")
    test_numbers = [5, -3, 0, 10, -7]
    for num in test_numbers:
        print(f"   categorize_number({num}) = '{categorize_number(num)}'")
    
    # Exercise 10
    print("\n10. Uppercase names:")
    print(f"    Original: {people}")
    print(f"    Names: {list(uppercase_names)}")

# Additional examples showing lambda best practices
def additional_examples():
    """Show additional lambda function examples and best practices"""
    print("\n" + "="*50)
    print("Additional Lambda Examples and Best Practices")
    print("="*50)
    
    # Example 1: Lambda with multiple operations
    print("\n1. Lambda for complex calculations:")
    # Calculate compound interest: A = P(1 + r/n)^(nt)
    compound_interest = lambda p, r, n, t: p * (1 + r/n) ** (n*t)
    principal = 1000
    rate = 0.05
    compounds_per_year = 12
    years = 5
    result = compound_interest(principal, rate, compounds_per_year, years)
    print(f"   Compound Interest: ${result:.2f}")
    
    # Example 2: Lambda for data validation
    print("\n2. Lambda for validation:")
    is_valid_email = lambda email: '@' in email and '.' in email.split('@')[1]
    emails = ['user@example.com', 'invalid-email', 'test@domain.org']
    for email in emails:
        print(f"   {email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
    
    # Example 3: Lambda with list comprehensions
    print("\n3. Lambda with list comprehensions:")
    apply_discount = lambda price, discount: price * (1 - discount)
    prices = [100, 200, 150, 300]
    discount_rate = 0.1
    discounted_prices = [apply_discount(price, discount_rate) for price in prices]
    print(f"   Original prices: {prices}")
    print(f"   Discounted prices: {discounted_prices}")
    
    # Example 4: Lambda for sorting complex data
    print("\n4. Lambda for complex sorting:")
    products = [
        {'name': 'Laptop', 'price': 999, 'rating': 4.5},
        {'name': 'Phone', 'price': 699, 'rating': 4.8},
        {'name': 'Tablet', 'price': 399, 'rating': 4.2}
    ]
    
    # Sort by price (ascending)
    by_price = sorted(products, key=lambda p: p['price'])
    print("   Sorted by price:")
    for product in by_price:
        print(f"     {product['name']}: ${product['price']}")
    
    # Sort by rating (descending)
    by_rating = sorted(products, key=lambda p: p['rating'], reverse=True)
    print("   Sorted by rating (desc):")
    for product in by_rating:
        print(f"     {product['name']}: {product['rating']} stars")
    
    # Example 5: Lambda with error handling
    print("\n5. Lambda with error handling:")
    safe_divide = lambda x, y: x / y if y != 0 else float('inf')
    test_cases = [(10, 2), (15, 3), (8, 0), (20, 4)]
    for x, y in test_cases:
        result = safe_divide(x, y)
        print(f"   {x} / {y} = {result}")

if __name__ == "__main__":
    demonstrate_solutions()
    additional_examples()