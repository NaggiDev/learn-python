"""
Solution: Working with Functions and Scope

This file contains the solution to the functions and scope exercise.
"""

def main():
    print("=" * 50)
    print("FUNCTIONS AND SCOPE EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Basic Function Definition
    # ========================================
    print("\n--- Task 1: Basic Function Definition ---")
    
    def greeting(name="Guest"):
        """
        Prints a greeting message with the given name.
        If no name is provided, uses "Guest" as default.
        """
        print(f"Hello, {name}!")
    
    # Test the function
    greeting("Alice")  # Should print: Hello, Alice!
    greeting()         # Should print: Hello, Guest!
    
    print("Basic function definition completed!")
    
    # ========================================
    # Task 2: Return Values
    # ========================================
    print("\n--- Task 2: Return Values ---")
    
    def calculate_rectangle_area(length, width):
        """
        Calculates and returns the area of a rectangle.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
            
        Returns:
            float: The area of the rectangle
        """
        return length * width
    
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
    
    def create_profile(name, age, city="Unknown", is_student=False):
        """
        Creates and returns a user profile as a dictionary.
        
        Args:
            name (str): The user's name
            age (int): The user's age
            city (str, optional): The user's city. Defaults to "Unknown".
            is_student (bool, optional): Whether the user is a student. Defaults to False.
            
        Returns:
            dict: A dictionary containing the user's profile information
        """
        return {
            "name": name,
            "age": age,
            "city": city,
            "is_student": is_student
        }
    
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
    
    def calculate_statistics(*values):
        """
        Calculates statistics for a variable number of values.
        
        Args:
            *values: Any number of numeric values
            
        Returns:
            dict: A dictionary containing count, sum, average, min, and max
        """
        if not values:
            return {
                "count": 0,
                "sum": 0,
                "average": 0,
                "min": None,
                "max": None
            }
        
        return {
            "count": len(values),
            "sum": sum(values),
            "average": sum(values) / len(values),
            "min": min(values),
            "max": max(values)
        }
    
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
    
    # Fixed function to correctly modify the global counter
    counter = 0
    
    def increment_counter():
        """
        Increments the global counter variable.
        """
        global counter
        counter = counter + 1
    
    # Fixed function to avoid mutable default argument issue
    def add_to_list(item, items=None):
        """
        Adds an item to a list and returns the list.
        Creates a new list if none is provided.
        
        Args:
            item: The item to add to the list
            items (list, optional): The list to add the item to. Defaults to None.
            
        Returns:
            list: The list with the item added
        """
        if items is None:
            items = []
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
    
    def create_counter():
        """
        Creates and returns a counter function.
        Each counter function maintains its own count.
        
        Returns:
            function: A function that increments and returns its count
        """
        count = 0
        
        def counter():
            nonlocal count
            count += 1
            return count
        
        return counter
    
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
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 1. Create a list of squares using map() and a lambda function
    squares = list(map(lambda x: x**2, numbers))
    
    # 2. Create a list of even numbers using filter() and a lambda function
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    
    # 3. Sort the following list of tuples by the second element using a lambda function
    pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
    sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
    
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
    
    def compose(func1, func2):
        """
        Creates a new function that applies func1 to the result of func2.
        
        Args:
            func1: The outer function
            func2: The inner function
            
        Returns:
            function: A new function that composes func1 and func2
        """
        def composed_function(x):
            return func1(func2(x))
        
        return composed_function
    
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