"""
Exercise: Working with Functions and Scope

Instructions:
1. Complete the tasks in each section below
2. Run the script to check your work
3. Each task has a TODO comment indicating what you need to do
4. Some tasks have tests that will verify your solution

Learning objectives:
- Define and call functions
- Work with function parameters and arguments
- Return values from functions
- Understand variable scope (local, global, nonlocal)
- Use lambda functions
- Apply best practices for function design
"""

def main():
    print("=" * 50)
    print("FUNCTIONS AND SCOPE EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Basic Function Definition
    # ========================================
    print("\n--- Task 1: Basic Function Definition ---")
    
    # TODO: Define a function called 'greeting' that takes a name parameter
    # and prints a greeting message like "Hello, {name}!"
    # If no name is provided, it should use "Guest" as the default
    
    # Test the function
    greeting("Alice")  # Should print: Hello, Alice!
    greeting()         # Should print: Hello, Guest!
    
    print("Basic function definition completed!")
    
    # ========================================
    # Task 2: Return Values
    # ========================================
    print("\n--- Task 2: Return Values ---")
    
    # TODO: Define a function called 'calculate_rectangle_area' that takes
    # two parameters (length and width) and returns the area of the rectangle
    
    # Test the function
    test_cases = [
        (5, 10, 50),
        (3, 4, 12),
        (7, 7, 49),
        (2.5, 3, 7.5)
    ]
    
    for length, width, expected in test_cases:
        result = calculate_rectangle_area(length, width)
        print(f"Area of rectangle with length {length} and width {width}: {result}")
        assert result == expected, f"Expected {expected}, got {result}"
    
    print("Return values function is working correctly!")
    
    # ========================================
    # Task 3: Multiple Parameters and Default Values
    # ========================================
    print("\n--- Task 3: Multiple Parameters and Default Values ---")
    
    # TODO: Define a function called 'create_profile' that takes parameters:
    # - name (required)
    # - age (required)
    # - city (default: "Unknown")
    # - is_student (default: False)
    # The function should return a dictionary containing these values
    
    # Test the function
    test_cases = [
        (
            {"name": "Bob", "age": 25},
            {"name": "Bob", "age": 25, "city": "Unknown", "is_student": False}
        ),
        (
            {"name": "Charlie", "age": 30, "city": "New York"},
            {"name": "Charlie", "age": 30, "city": "New York", "is_student": False}
        ),
        (
            {"name": "Diana", "age": 22, "is_student": True},
            {"name": "Diana", "age": 22, "city": "Unknown", "is_student": True}
        ),
        (
            {"name": "Eve", "age": 28, "city": "London", "is_student": True},
            {"name": "Eve", "age": 28, "city": "London", "is_student": True}
        )
    ]
    
    for kwargs, expected in test_cases:
        result = create_profile(**kwargs)
        print(f"Profile created: {result}")
        assert result == expected, f"Expected {expected}, got {result}"
    
    print("Multiple parameters function is working correctly!")
    
    # ========================================
    # Task 4: Variable-Length Arguments
    # ========================================
    print("\n--- Task 4: Variable-Length Arguments ---")
    
    # TODO: Define a function called 'calculate_statistics' that takes any number
    # of numeric values and returns a dictionary with:
    # - 'count': the number of values
    # - 'sum': the sum of all values
    # - 'average': the average of all values
    # - 'min': the minimum value
    # - 'max': the maximum value
    # If no values are provided, return appropriate default values
    
    # Test the function
    test_cases = [
        (
            [1, 2, 3, 4, 5],
            {"count": 5, "sum": 15, "average": 3.0, "min": 1, "max": 5}
        ),
        (
            [10],
            {"count": 1, "sum": 10, "average": 10.0, "min": 10, "max": 10}
        ),
        (
            [7, 7, 7, 7],
            {"count": 4, "sum": 28, "average": 7.0, "min": 7, "max": 7}
        ),
        (
            [],
            {"count": 0, "sum": 0, "average": 0, "min": None, "max": None}
        )
    ]
    
    for values, expected in test_cases:
        result = calculate_statistics(*values)
        print(f"Statistics for {values}: {result}")
        assert result == expected, f"Expected {expected}, got {result}"
    
    print("Variable-length arguments function is working correctly!")
    
    # ========================================
    # Task 5: Scope and Side Effects
    # ========================================
    print("\n--- Task 5: Scope and Side Effects ---")
    
    # TODO: Fix the following function so it correctly modifies the global counter
    counter = 0
    
    def increment_counter():
        counter = counter + 1  # This will cause an error
    
    # TODO: Fix the following function so it correctly modifies the list
    def add_to_list(item, items=[]):
        items.append(item)
        return items
    
    # Test the counter function
    print(f"Counter before: {counter}")
    increment_counter()
    print(f"Counter after one increment: {counter}")
    increment_counter()
    print(f"Counter after two increments: {counter}")
    assert counter == 2, f"Expected counter to be 2, got {counter}"
    
    # Test the list function
    result1 = add_to_list(1)
    print(f"After adding 1: {result1}")
    result2 = add_to_list(2)
    print(f"After adding 2 (should be a new list): {result2}")
    assert result1 != result2, "Expected different lists"
    assert result1 == [1], f"Expected [1], got {result1}"
    assert result2 == [2], f"Expected [2], got {result2}"
    
    print("Scope and side effects functions are working correctly!")
    
    # ========================================
    # Task 6: Nested Functions and Closures
    # ========================================
    print("\n--- Task 6: Nested Functions and Closures ---")
    
    # TODO: Create a function called 'create_counter' that returns a nested function.
    # The nested function should increment and return a counter variable each time it's called.
    # Each counter should be independent.
    
    # Test the function
    counter1 = create_counter()
    counter2 = create_counter()
    
    print(f"Counter 1, first call: {counter1()}")  # Should print: 1
    print(f"Counter 1, second call: {counter1()}")  # Should print: 2
    print(f"Counter 2, first call: {counter2()}")  # Should print: 1
    print(f"Counter 1, third call: {counter1()}")  # Should print: 3
    
    assert counter1() == 4, f"Expected 4, got {counter1()}"
    assert counter2() == 2, f"Expected 2, got {counter2()}"
    
    print("Nested functions and closures are working correctly!")
    
    # ========================================
    # Task 7: Lambda Functions
    # ========================================
    print("\n--- Task 7: Lambda Functions ---")
    
    # TODO: Use lambda functions to transform the following list of numbers:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 1. Create a list of squares using map() and a lambda function
    squares = None  # Replace with your solution
    
    # 2. Create a list of even numbers using filter() and a lambda function
    evens = None  # Replace with your solution
    
    # 3. Sort the following list of tuples by the second element using a lambda function
    pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
    sorted_pairs = None  # Replace with your solution
    
    # Test the results
    print(f"Squares: {squares}")
    print(f"Even numbers: {evens}")
    print(f"Sorted pairs: {sorted_pairs}")
    
    assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], f"Expected [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], got {squares}"
    assert evens == [2, 4, 6, 8, 10], f"Expected [2, 4, 6, 8, 10], got {evens}"
    assert sorted_pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')], f"Expected [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')], got {sorted_pairs}"
    
    print("Lambda functions are working correctly!")
    
    # ========================================
    # Task 8: Challenge - Function Composition
    # ========================================
    print("\n--- Task 8: Challenge - Function Composition ---")
    
    # TODO: Create a function called 'compose' that takes two functions as arguments
    # and returns a new function that applies the first function to the result of
    # the second function when called with an argument.
    
    # Test the function
    def double(x):
        return x * 2
    
    def increment(x):
        return x + 1
    
    double_then_increment = compose(increment, double)
    increment_then_double = compose(double, increment)
    
    test_cases = [
        (5, double_then_increment, 11),  # (5 * 2) + 1 = 11
        (5, increment_then_double, 12),  # (5 + 1) * 2 = 12
        (0, double_then_increment, 1),   # (0 * 2) + 1 = 1
        (0, increment_then_double, 2)    # (0 + 1) * 2 = 2
    ]
    
    for input_val, func, expected in test_cases:
        result = func(input_val)
        print(f"Function composition with input {input_val}: {result}")
        assert result == expected, f"Expected {expected}, got {result}"
    
    print("Function composition is working correctly!")
    
    print("\nCongratulations! You've completed the functions and scope exercise.")

if __name__ == "__main__":
    main()