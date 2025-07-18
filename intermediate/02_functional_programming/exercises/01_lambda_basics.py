"""
Lambda Functions - Basic Exercises

Complete the following exercises to practice using lambda functions.
Each exercise has test cases to verify your solution.
"""

# Exercise 1: Basic Lambda Creation
# TODO: Create a lambda function that doubles a number
double = None  # Replace None with your lambda function

# Exercise 2: Lambda with Multiple Arguments
# TODO: Create a lambda function that calculates the area of a rectangle
rectangle_area = None  # Replace None with your lambda function

# Exercise 3: Lambda with Conditional Logic
# TODO: Create a lambda function that returns the absolute value of a number
absolute_value = None  # Replace None with your lambda function

# Exercise 4: Lambda for String Operations
# TODO: Create a lambda function that capitalizes the first letter of a string
capitalize_first = None  # Replace None with your lambda function

# Exercise 5: Lambda with Default Arguments
# TODO: Create a lambda function that raises a number to a power (default power is 2)
power = None  # Replace None with your lambda function

# Exercise 6: Using Lambda with Built-in Functions
# TODO: Use lambda with map() to convert a list of temperatures from Celsius to Fahrenheit
# Formula: F = C * 9/5 + 32
celsius_temps = [0, 20, 30, 40, 100]
fahrenheit_temps = None  # Replace None with your solution using map() and lambda

# Exercise 7: Using Lambda with Filter
# TODO: Use lambda with filter() to get only positive numbers from a list
numbers = [-5, -2, 0, 3, 8, -1, 7]
positive_numbers = None  # Replace None with your solution using filter() and lambda

# Exercise 8: Using Lambda with Sorted
# TODO: Use lambda with sorted() to sort a list of tuples by the second element
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 96)]
sorted_students = None  # Replace None with your solution using sorted() and lambda

# Exercise 9: Complex Lambda with Conditional
# TODO: Create a lambda function that categorizes numbers as 'positive', 'negative', or 'zero'
categorize_number = None  # Replace None with your lambda function

# Exercise 10: Lambda for Data Processing
# TODO: Use lambda to process a list of dictionaries
# Extract and uppercase the 'name' field from each dictionary
people = [
    {'name': 'john', 'age': 25},
    {'name': 'jane', 'age': 30},
    {'name': 'bob', 'age': 35}
]
uppercase_names = None  # Replace None with your solution using map() and lambda


# Test Functions
def test_exercise_1():
    """Test double lambda function"""
    if double is None:
        print("❌ Exercise 1: double function not implemented")
        return False
    
    try:
        assert double(5) == 10, f"Expected 10, got {double(5)}"
        assert double(-3) == -6, f"Expected -6, got {double(-3)}"
        assert double(0) == 0, f"Expected 0, got {double(0)}"
        print("✅ Exercise 1: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 1: {e}")
        return False

def test_exercise_2():
    """Test rectangle_area lambda function"""
    if rectangle_area is None:
        print("❌ Exercise 2: rectangle_area function not implemented")
        return False
    
    try:
        assert rectangle_area(5, 3) == 15, f"Expected 15, got {rectangle_area(5, 3)}"
        assert rectangle_area(10, 2) == 20, f"Expected 20, got {rectangle_area(10, 2)}"
        print("✅ Exercise 2: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 2: {e}")
        return False

def test_exercise_3():
    """Test absolute_value lambda function"""
    if absolute_value is None:
        print("❌ Exercise 3: absolute_value function not implemented")
        return False
    
    try:
        assert absolute_value(-5) == 5, f"Expected 5, got {absolute_value(-5)}"
        assert absolute_value(3) == 3, f"Expected 3, got {absolute_value(3)}"
        assert absolute_value(0) == 0, f"Expected 0, got {absolute_value(0)}"
        print("✅ Exercise 3: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 3: {e}")
        return False

def test_exercise_4():
    """Test capitalize_first lambda function"""
    if capitalize_first is None:
        print("❌ Exercise 4: capitalize_first function not implemented")
        return False
    
    try:
        assert capitalize_first("hello") == "Hello", f"Expected 'Hello', got {capitalize_first('hello')}"
        assert capitalize_first("python") == "Python", f"Expected 'Python', got {capitalize_first('python')}"
        print("✅ Exercise 4: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 4: {e}")
        return False

def test_exercise_5():
    """Test power lambda function"""
    if power is None:
        print("❌ Exercise 5: power function not implemented")
        return False
    
    try:
        assert power(5) == 25, f"Expected 25, got {power(5)}"
        assert power(3, 3) == 27, f"Expected 27, got {power(3, 3)}"
        assert power(2, 4) == 16, f"Expected 16, got {power(2, 4)}"
        print("✅ Exercise 5: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 5: {e}")
        return False

def test_exercise_6():
    """Test Celsius to Fahrenheit conversion"""
    if fahrenheit_temps is None:
        print("❌ Exercise 6: fahrenheit_temps not implemented")
        return False
    
    try:
        expected = [32.0, 68.0, 86.0, 104.0, 212.0]
        result = list(fahrenheit_temps)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 6: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 6: {e}")
        return False

def test_exercise_7():
    """Test positive numbers filter"""
    if positive_numbers is None:
        print("❌ Exercise 7: positive_numbers not implemented")
        return False
    
    try:
        expected = [3, 8, 7]
        result = list(positive_numbers)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 7: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 7: {e}")
        return False

def test_exercise_8():
    """Test sorting students by grade"""
    if sorted_students is None:
        print("❌ Exercise 8: sorted_students not implemented")
        return False
    
    try:
        expected = [('Charlie', 78), ('Alice', 85), ('Bob', 92), ('Diana', 96)]
        assert sorted_students == expected, f"Expected {expected}, got {sorted_students}"
        print("✅ Exercise 8: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 8: {e}")
        return False

def test_exercise_9():
    """Test categorize_number lambda function"""
    if categorize_number is None:
        print("❌ Exercise 9: categorize_number function not implemented")
        return False
    
    try:
        assert categorize_number(5) == 'positive', f"Expected 'positive', got {categorize_number(5)}"
        assert categorize_number(-3) == 'negative', f"Expected 'negative', got {categorize_number(-3)}"
        assert categorize_number(0) == 'zero', f"Expected 'zero', got {categorize_number(0)}"
        print("✅ Exercise 9: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 9: {e}")
        return False

def test_exercise_10():
    """Test uppercase names extraction"""
    if uppercase_names is None:
        print("❌ Exercise 10: uppercase_names not implemented")
        return False
    
    try:
        expected = ['JOHN', 'JANE', 'BOB']
        result = list(uppercase_names)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 10: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 10: {e}")
        return False

def run_all_tests():
    """Run all test functions"""
    print("Running Lambda Functions Exercises Tests...\n")
    
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
        print("🎉 Congratulations! All exercises completed successfully!")
    else:
        print("📚 Keep working on the remaining exercises. You're doing great!")

if __name__ == "__main__":
    run_all_tests()