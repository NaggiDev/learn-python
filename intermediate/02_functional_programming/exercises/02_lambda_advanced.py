"""
Advanced Lambda Functions Exercises

These exercises focus on more complex lambda function usage patterns
and real-world applications.
"""

# Exercise 1: Lambda Factory Functions
# TODO: Create a function that returns a lambda for multiplying by a specific number
def create_multiplier(n):
    # Return a lambda function that multiplies its input by n
    return None  # Replace with your lambda

# Exercise 2: Lambda with Nested Conditionals
# TODO: Create a lambda that assigns letter grades based on numeric scores
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F
grade_calculator = None  # Replace with your lambda

# Exercise 3: Lambda for String Processing
# TODO: Create a lambda that processes a string by:
# - Removing leading/trailing whitespace
# - Converting to lowercase
# - Replacing spaces with underscores
string_processor = None  # Replace with your lambda

# Exercise 4: Lambda with Dictionary Operations
# TODO: Use lambda to sort a list of dictionaries by multiple criteria
# First by 'department', then by 'salary' (descending)
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 75000},
    {'name': 'Bob', 'department': 'Marketing', 'salary': 65000},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 80000},
    {'name': 'Diana', 'department': 'Marketing', 'salary': 70000},
]
sorted_employees = None  # Replace with your solution

# Exercise 5: Lambda for Data Transformation
# TODO: Transform a list of user data into a specific format
users = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'},
    {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25, 'city': 'Los Angeles'},
    {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 35, 'city': 'Chicago'},
]
# Transform to format: "Last, First (Age) - City"
formatted_users = None  # Replace with your solution using map and lambda

# Exercise 6: Lambda for Filtering Complex Data
# TODO: Filter products based on multiple conditions using lambda
products = [
    {'name': 'Laptop', 'price': 999, 'category': 'Electronics', 'in_stock': True},
    {'name': 'Book', 'price': 25, 'category': 'Education', 'in_stock': True},
    {'name': 'Phone', 'price': 699, 'category': 'Electronics', 'in_stock': False},
    {'name': 'Desk', 'price': 299, 'category': 'Furniture', 'in_stock': True},
]
# Filter: Electronics category, price < 800, and in stock
filtered_products = None  # Replace with your solution

# Exercise 7: Lambda with Reduce (you'll need to import functools)
from functools import reduce
# TODO: Use lambda with reduce to find the product of all numbers in a list
numbers = [2, 3, 4, 5]
product = None  # Replace with your solution using reduce and lambda

# Exercise 8: Lambda for Grouping Data
# TODO: Use lambda to create a function that groups items by a key
def group_by_key(items, key_func):
    # This function should group items using the key_func
    # Return a dictionary where keys are the result of key_func and values are lists of items
    result = {}
    # TODO: Implement this function
    return result

# Test data for grouping
test_items = [
    {'name': 'Apple', 'type': 'Fruit', 'color': 'Red'},
    {'name': 'Banana', 'type': 'Fruit', 'color': 'Yellow'},
    {'name': 'Carrot', 'type': 'Vegetable', 'color': 'Orange'},
    {'name': 'Broccoli', 'type': 'Vegetable', 'color': 'Green'},
]

# Group by type
grouped_by_type = None  # Replace with your solution using group_by_key and lambda

# Exercise 9: Lambda for Mathematical Operations
# TODO: Create a list of lambda functions for different mathematical operations
math_operations = {
    'add': None,      # lambda for addition
    'subtract': None, # lambda for subtraction
    'multiply': None, # lambda for multiplication
    'divide': None,   # lambda for division (handle division by zero)
    'power': None,    # lambda for exponentiation
}

# Exercise 10: Lambda for Data Validation
# TODO: Create validation functions using lambda
validators = {
    'email': None,     # lambda to validate email format
    'phone': None,     # lambda to validate phone number (simple: 10 digits)
    'password': None,  # lambda to validate password (min 8 chars, has digit and letter)
}

# Test data for validation
test_data = {
    'emails': ['user@example.com', 'invalid-email', 'test@domain.org', 'no-at-sign'],
    'phones': ['1234567890', '123-456-7890', '12345', 'abcdefghij'],
    'passwords': ['Password123', 'weak', 'NoDigits!', '12345678', 'Strong1Pass']
}


# Test Functions
def test_exercise_1():
    """Test lambda factory functions"""
    try:
        double = create_multiplier(2)
        triple = create_multiplier(3)
        
        if double is None or triple is None:
            print("❌ Exercise 1: create_multiplier not implemented")
            return False
        
        assert double(5) == 10, f"Expected 10, got {double(5)}"
        assert triple(4) == 12, f"Expected 12, got {triple(4)}"
        print("✅ Exercise 1: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 1: {e}")
        return False

def test_exercise_2():
    """Test grade calculator lambda"""
    if grade_calculator is None:
        print("❌ Exercise 2: grade_calculator not implemented")
        return False
    
    try:
        test_cases = [(95, 'A'), (85, 'B'), (75, 'C'), (65, 'D'), (55, 'F')]
        for score, expected in test_cases:
            result = grade_calculator(score)
            assert result == expected, f"Score {score}: expected {expected}, got {result}"
        print("✅ Exercise 2: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 2: {e}")
        return False

def test_exercise_3():
    """Test string processor lambda"""
    if string_processor is None:
        print("❌ Exercise 3: string_processor not implemented")
        return False
    
    try:
        test_cases = [
            ("  Hello World  ", "hello_world"),
            ("Python Programming", "python_programming"),
            ("  Test String  ", "test_string")
        ]
        for input_str, expected in test_cases:
            result = string_processor(input_str)
            assert result == expected, f"Input '{input_str}': expected '{expected}', got '{result}'"
        print("✅ Exercise 3: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 3: {e}")
        return False

def test_exercise_4():
    """Test employee sorting"""
    if sorted_employees is None:
        print("❌ Exercise 4: sorted_employees not implemented")
        return False
    
    try:
        # Should be sorted by department first, then by salary descending
        expected_order = ['Charlie', 'Alice', 'Diana', 'Bob']  # Engineering (Charlie 80k, Alice 75k), Marketing (Diana 70k, Bob 65k)
        actual_order = [emp['name'] for emp in sorted_employees]
        assert actual_order == expected_order, f"Expected {expected_order}, got {actual_order}"
        print("✅ Exercise 4: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 4: {e}")
        return False

def test_exercise_5():
    """Test user data transformation"""
    if formatted_users is None:
        print("❌ Exercise 5: formatted_users not implemented")
        return False
    
    try:
        expected = ['Doe, John (30) - New York', 'Smith, Jane (25) - Los Angeles', 'Johnson, Bob (35) - Chicago']
        result = list(formatted_users)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 5: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 5: {e}")
        return False

def test_exercise_6():
    """Test product filtering"""
    if filtered_products is None:
        print("❌ Exercise 6: filtered_products not implemented")
        return False
    
    try:
        result = list(filtered_products)
        # Should only include Phone if it were in stock, but it's not, so empty list
        # Actually, no products match all criteria (Electronics, < 800, in stock)
        # Laptop is Electronics and in stock but price is 999 (not < 800)
        # Phone is Electronics and < 800 but not in stock
        expected_names = []  # No products match all criteria
        actual_names = [p['name'] for p in result]
        assert actual_names == expected_names, f"Expected {expected_names}, got {actual_names}"
        print("✅ Exercise 6: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 6: {e}")
        return False

def test_exercise_7():
    """Test reduce with lambda"""
    if product is None:
        print("❌ Exercise 7: product not implemented")
        return False
    
    try:
        expected = 2 * 3 * 4 * 5  # 120
        assert product == expected, f"Expected {expected}, got {product}"
        print("✅ Exercise 7: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 7: {e}")
        return False

def test_exercise_8():
    """Test grouping function"""
    if grouped_by_type is None:
        print("❌ Exercise 8: grouped_by_type not implemented")
        return False
    
    try:
        expected_keys = {'Fruit', 'Vegetable'}
        actual_keys = set(grouped_by_type.keys())
        assert actual_keys == expected_keys, f"Expected keys {expected_keys}, got {actual_keys}"
        
        fruit_names = {item['name'] for item in grouped_by_type['Fruit']}
        vegetable_names = {item['name'] for item in grouped_by_type['Vegetable']}
        
        assert fruit_names == {'Apple', 'Banana'}, f"Expected fruit names {{'Apple', 'Banana'}}, got {fruit_names}"
        assert vegetable_names == {'Carrot', 'Broccoli'}, f"Expected vegetable names {{'Carrot', 'Broccoli'}}, got {vegetable_names}"
        
        print("✅ Exercise 8: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 8: {e}")
        return False

def test_exercise_9():
    """Test mathematical operations"""
    if any(op is None for op in math_operations.values()):
        print("❌ Exercise 9: math_operations not fully implemented")
        return False
    
    try:
        assert math_operations['add'](5, 3) == 8
        assert math_operations['subtract'](10, 4) == 6
        assert math_operations['multiply'](6, 7) == 42
        assert math_operations['divide'](15, 3) == 5
        assert math_operations['divide'](10, 0) == float('inf')  # Handle division by zero
        assert math_operations['power'](2, 3) == 8
        print("✅ Exercise 9: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 9: {e}")
        return False

def test_exercise_10():
    """Test validation functions"""
    if any(validator is None for validator in validators.values()):
        print("❌ Exercise 10: validators not fully implemented")
        return False
    
    try:
        # Test email validation
        email_results = [validators['email'](email) for email in test_data['emails']]
        expected_email = [True, False, True, False]
        assert email_results == expected_email, f"Email validation failed: {email_results}"
        
        # Test phone validation
        phone_results = [validators['phone'](phone) for phone in test_data['phones']]
        expected_phone = [True, False, False, False]  # Only '1234567890' should be valid
        assert phone_results == expected_phone, f"Phone validation failed: {phone_results}"
        
        # Test password validation
        password_results = [validators['password'](pwd) for pwd in test_data['passwords']]
        expected_password = [True, False, False, False, True]  # 'Password123' and 'Strong1Pass' should be valid
        assert password_results == expected_password, f"Password validation failed: {password_results}"
        
        print("✅ Exercise 10: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 10: {e}")
        return False

def run_all_tests():
    """Run all test functions"""
    print("Running Advanced Lambda Functions Exercises Tests...\n")
    
    tests = [
        test_exercise_1, test_exercise_2, test_exercise_3, test_exercise_4,
        test_exercise_5, test_exercise_6, test_exercise_7, test_exercise_8,
        test_exercise_9, test_exercise_10
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 Congratulations! All advanced lambda exercises completed successfully!")
    else:
        print("📚 Keep working on the remaining exercises. These are challenging!")

if __name__ == "__main__":
    run_all_tests()