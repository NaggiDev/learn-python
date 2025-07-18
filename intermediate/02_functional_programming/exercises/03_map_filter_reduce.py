"""
Map, Filter, and Reduce Exercises

Complete the following exercises to practice using map(), filter(), and reduce().
Each exercise has test cases to verify your solution.
"""

from functools import reduce

# Exercise 1: Basic map() usage
# TODO: Use map() to convert a list of temperatures from Celsius to Fahrenheit
# Formula: F = C * 9/5 + 32
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = None  # Replace with your solution

# Exercise 2: map() with string operations
# TODO: Use map() to capitalize the first letter of each word
words = ['hello', 'world', 'python', 'programming']
capitalized_words = None  # Replace with your solution

# Exercise 3: map() with multiple iterables
# TODO: Use map() to calculate the area of rectangles given lengths and widths
lengths = [5, 3, 8, 2]
widths = [4, 6, 2, 9]
areas = None  # Replace with your solution

# Exercise 4: Basic filter() usage
# TODO: Use filter() to get only the positive numbers
numbers = [-5, 3, -2, 8, 0, -1, 7, 4]
positive_numbers = None  # Replace with your solution

# Exercise 5: filter() with string conditions
# TODO: Use filter() to get words that contain the letter 'a'
word_list = ['cat', 'dog', 'elephant', 'bird', 'snake', 'rabbit']
words_with_a = None  # Replace with your solution

# Exercise 6: filter() with complex conditions
# TODO: Filter products that are in stock and cost less than $100
products = [
    {'name': 'Laptop', 'price': 999, 'in_stock': True},
    {'name': 'Mouse', 'price': 25, 'in_stock': True},
    {'name': 'Keyboard', 'price': 75, 'in_stock': False},
    {'name': 'Monitor', 'price': 300, 'in_stock': True},
    {'name': 'Headphones', 'price': 50, 'in_stock': True}
]
affordable_available = None  # Replace with your solution

# Exercise 7: Basic reduce() usage
# TODO: Use reduce() to find the sum of all numbers
numbers_to_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = None  # Replace with your solution

# Exercise 8: reduce() to find maximum
# TODO: Use reduce() to find the maximum number in the list
numbers_for_max = [23, 45, 12, 67, 34, 89, 56]
maximum_number = None  # Replace with your solution

# Exercise 9: reduce() for string concatenation
# TODO: Use reduce() to concatenate all strings with a space separator
string_parts = ['Python', 'is', 'an', 'awesome', 'language']
concatenated_string = None  # Replace with your solution

# Exercise 10: Combining map(), filter(), and reduce()
# TODO: Square all even numbers and then sum them
numbers_for_combo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Step 1: Filter even numbers
# Step 2: Square them using map
# Step 3: Sum them using reduce
combo_result = None  # Replace with your solution

# Exercise 11: Data processing with map()
# TODO: Extract the 'name' field from each dictionary and convert to uppercase
employees = [
    {'name': 'alice', 'department': 'engineering', 'salary': 75000},
    {'name': 'bob', 'department': 'marketing', 'salary': 65000},
    {'name': 'charlie', 'department': 'engineering', 'salary': 80000}
]
employee_names_upper = None  # Replace with your solution

# Exercise 12: Advanced filter() usage
# TODO: Filter employees who work in 'engineering' and earn more than $70,000
high_paid_engineers = None  # Replace with your solution

# Exercise 13: reduce() for complex aggregation
# TODO: Use reduce() to find the employee with the highest salary
highest_paid_employee = None  # Replace with your solution

# Exercise 14: Nested data processing
# TODO: Process nested data - calculate total sales for each salesperson
sales_data = [
    {'name': 'John', 'sales': [100, 200, 150]},
    {'name': 'Jane', 'sales': [300, 250, 400]},
    {'name': 'Bob', 'sales': [180, 220, 160]}
]
# Calculate total sales for each person using map and reduce
total_sales_per_person = None  # Replace with your solution

# Exercise 15: Chain operations for data analysis
# TODO: From the sales data, find the name of the person with the highest total sales
top_salesperson = None  # Replace with your solution


# Test Functions
def test_exercise_1():
    """Test Celsius to Fahrenheit conversion"""
    if fahrenheit_temps is None:
        print("❌ Exercise 1: fahrenheit_temps not implemented")
        return False
    
    try:
        expected = [32.0, 50.0, 68.0, 86.0, 104.0]
        result = list(fahrenheit_temps)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 1: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 1: {e}")
        return False

def test_exercise_2():
    """Test word capitalization"""
    if capitalized_words is None:
        print("❌ Exercise 2: capitalized_words not implemented")
        return False
    
    try:
        expected = ['Hello', 'World', 'Python', 'Programming']
        result = list(capitalized_words)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 2: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 2: {e}")
        return False

def test_exercise_3():
    """Test rectangle area calculation"""
    if areas is None:
        print("❌ Exercise 3: areas not implemented")
        return False
    
    try:
        expected = [20, 18, 16, 18]  # 5*4, 3*6, 8*2, 2*9
        result = list(areas)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 3: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 3: {e}")
        return False

def test_exercise_4():
    """Test positive number filtering"""
    if positive_numbers is None:
        print("❌ Exercise 4: positive_numbers not implemented")
        return False
    
    try:
        expected = [3, 8, 7, 4]
        result = list(positive_numbers)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 4: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 4: {e}")
        return False

def test_exercise_5():
    """Test words containing 'a'"""
    if words_with_a is None:
        print("❌ Exercise 5: words_with_a not implemented")
        return False
    
    try:
        expected = ['cat', 'elephant', 'snake', 'rabbit']
        result = list(words_with_a)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 5: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 5: {e}")
        return False

def test_exercise_6():
    """Test product filtering"""
    if affordable_available is None:
        print("❌ Exercise 6: affordable_available not implemented")
        return False
    
    try:
        result = list(affordable_available)
        expected_names = ['Mouse', 'Headphones']
        actual_names = [p['name'] for p in result]
        assert actual_names == expected_names, f"Expected {expected_names}, got {actual_names}"
        print("✅ Exercise 6: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 6: {e}")
        return False

def test_exercise_7():
    """Test sum using reduce"""
    if total_sum is None:
        print("❌ Exercise 7: total_sum not implemented")
        return False
    
    try:
        expected = 55  # Sum of 1 to 10
        assert total_sum == expected, f"Expected {expected}, got {total_sum}"
        print("✅ Exercise 7: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 7: {e}")
        return False

def test_exercise_8():
    """Test maximum using reduce"""
    if maximum_number is None:
        print("❌ Exercise 8: maximum_number not implemented")
        return False
    
    try:
        expected = 89
        assert maximum_number == expected, f"Expected {expected}, got {maximum_number}"
        print("✅ Exercise 8: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 8: {e}")
        return False

def test_exercise_9():
    """Test string concatenation using reduce"""
    if concatenated_string is None:
        print("❌ Exercise 9: concatenated_string not implemented")
        return False
    
    try:
        expected = "Python is an awesome language"
        assert concatenated_string == expected, f"Expected '{expected}', got '{concatenated_string}'"
        print("✅ Exercise 9: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 9: {e}")
        return False

def test_exercise_10():
    """Test combination of map, filter, and reduce"""
    if combo_result is None:
        print("❌ Exercise 10: combo_result not implemented")
        return False
    
    try:
        expected = 220  # 2²+4²+6²+8²+10² = 4+16+36+64+100 = 220
        assert combo_result == expected, f"Expected {expected}, got {combo_result}"
        print("✅ Exercise 10: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 10: {e}")
        return False

def test_exercise_11():
    """Test employee name extraction and uppercasing"""
    if employee_names_upper is None:
        print("❌ Exercise 11: employee_names_upper not implemented")
        return False
    
    try:
        expected = ['ALICE', 'BOB', 'CHARLIE']
        result = list(employee_names_upper)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 11: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 11: {e}")
        return False

def test_exercise_12():
    """Test filtering high-paid engineers"""
    if high_paid_engineers is None:
        print("❌ Exercise 12: high_paid_engineers not implemented")
        return False
    
    try:
        result = list(high_paid_engineers)
        expected_names = ['alice', 'charlie']
        actual_names = [emp['name'] for emp in result]
        assert actual_names == expected_names, f"Expected {expected_names}, got {actual_names}"
        print("✅ Exercise 12: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 12: {e}")
        return False

def test_exercise_13():
    """Test finding highest paid employee"""
    if highest_paid_employee is None:
        print("❌ Exercise 13: highest_paid_employee not implemented")
        return False
    
    try:
        expected_name = 'charlie'
        assert highest_paid_employee['name'] == expected_name, f"Expected {expected_name}, got {highest_paid_employee['name']}"
        print("✅ Exercise 13: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 13: {e}")
        return False

def test_exercise_14():
    """Test total sales calculation"""
    if total_sales_per_person is None:
        print("❌ Exercise 14: total_sales_per_person not implemented")
        return False
    
    try:
        result = list(total_sales_per_person)
        expected = [450, 950, 560]  # John: 450, Jane: 950, Bob: 560
        assert result == expected, f"Expected {expected}, got {result}"
        print("✅ Exercise 14: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 14: {e}")
        return False

def test_exercise_15():
    """Test finding top salesperson"""
    if top_salesperson is None:
        print("❌ Exercise 15: top_salesperson not implemented")
        return False
    
    try:
        expected = 'Jane'
        assert top_salesperson == expected, f"Expected {expected}, got {top_salesperson}"
        print("✅ Exercise 15: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 15: {e}")
        return False

def run_all_tests():
    """Run all test functions"""
    print("Running Map, Filter, and Reduce Exercises Tests...\n")
    
    tests = [
        test_exercise_1, test_exercise_2, test_exercise_3, test_exercise_4,
        test_exercise_5, test_exercise_6, test_exercise_7, test_exercise_8,
        test_exercise_9, test_exercise_10, test_exercise_11, test_exercise_12,
        test_exercise_13, test_exercise_14, test_exercise_15
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 Congratulations! All map, filter, and reduce exercises completed successfully!")
    else:
        print("📚 Keep working on the remaining exercises. You're mastering functional programming!")

if __name__ == "__main__":
    run_all_tests()