"""
Solution: Working with Basic Operators

This file contains the solution to the basic operators exercise.
"""

def main():
    print("=" * 50)
    print("BASIC OPERATORS EXERCISE")
    print("=" * 50)
    
    # ========================================
    # Task 1: Arithmetic Operators
    # ========================================
    print("\n--- Task 1: Arithmetic Operators ---")
    
    # Create two variables x and y
    x = 15
    y = 4
    
    # Calculate arithmetic operations
    addition_result = x + y
    subtraction_result = x - y
    multiplication_result = x * y
    division_result = x / y
    floor_division_result = x // y
    modulus_result = x % y
    exponentiation_result = x ** y
    
    # Print the results
    print(f"x = {x}, y = {y}")
    print(f"Addition: {x} + {y} = {addition_result}")
    print(f"Subtraction: {x} - {y} = {subtraction_result}")
    print(f"Multiplication: {x} * {y} = {multiplication_result}")
    print(f"Division: {x} / {y} = {division_result}")
    print(f"Floor Division: {x} // {y} = {floor_division_result}")
    print(f"Modulus: {x} % {y} = {modulus_result}")
    print(f"Exponentiation: {x} ** {y} = {exponentiation_result}")
    
    # Test the calculations
    assert addition_result == 19, f"Expected addition to be 19, got {addition_result}"
    assert subtraction_result == 11, f"Expected subtraction to be 11, got {subtraction_result}"
    assert multiplication_result == 60, f"Expected multiplication to be 60, got {multiplication_result}"
    assert division_result == 3.75, f"Expected division to be 3.75, got {division_result}"
    assert floor_division_result == 3, f"Expected floor division to be 3, got {floor_division_result}"
    assert modulus_result == 3, f"Expected modulus to be 3, got {modulus_result}"
    assert exponentiation_result == 50625, f"Expected exponentiation to be 50625, got {exponentiation_result}"
    print("All arithmetic operations are correct!")
    
    # ========================================
    # Task 2: Comparison Operators
    # ========================================
    print("\n--- Task 2: Comparison Operators ---")
    
    # Create two variables a and b
    a = 10
    b = 7
    
    # Calculate comparison operations
    equal_result = a == b
    not_equal_result = a != b
    greater_than_result = a > b
    less_than_result = a < b
    greater_equal_result = a >= b
    less_equal_result = a <= b
    
    # Print the results
    print(f"a = {a}, b = {b}")
    print(f"Equal: {a} == {b} is {equal_result}")
    print(f"Not Equal: {a} != {b} is {not_equal_result}")
    print(f"Greater Than: {a} > {b} is {greater_than_result}")
    print(f"Less Than: {a} < {b} is {less_than_result}")
    print(f"Greater Than or Equal: {a} >= {b} is {greater_equal_result}")
    print(f"Less Than or Equal: {a} <= {b} is {less_equal_result}")
    
    # Test the comparisons
    assert equal_result == False, f"Expected a == b to be False, got {equal_result}"
    assert not_equal_result == True, f"Expected a != b to be True, got {not_equal_result}"
    assert greater_than_result == True, f"Expected a > b to be True, got {greater_than_result}"
    assert less_than_result == False, f"Expected a < b to be False, got {less_than_result}"
    assert greater_equal_result == True, f"Expected a >= b to be True, got {greater_equal_result}"
    assert less_equal_result == False, f"Expected a <= b to be False, got {less_equal_result}"
    print("All comparison operations are correct!")
    
    # ========================================
    # Task 3: Logical Operators
    # ========================================
    print("\n--- Task 3: Logical Operators ---")
    
    # Create two boolean variables p and q
    p = True
    q = False
    
    # Calculate logical operations
    and_result = p and q
    or_result = p or q
    not_p_result = not p
    not_q_result = not q
    complex_result = (p or q) and (not p or not q)
    
    # Print the results
    print(f"p = {p}, q = {q}")
    print(f"AND: {p} and {q} is {and_result}")
    print(f"OR: {p} or {q} is {or_result}")
    print(f"NOT p: not {p} is {not_p_result}")
    print(f"NOT q: not {q} is {not_q_result}")
    print(f"Complex: (p OR q) AND (NOT p OR NOT q) is {complex_result}")
    
    # Test the logical operations
    assert and_result == False, f"Expected p and q to be False, got {and_result}"
    assert or_result == True, f"Expected p or q to be True, got {or_result}"
    assert not_p_result == False, f"Expected not p to be False, got {not_p_result}"
    assert not_q_result == True, f"Expected not q to be True, got {not_q_result}"
    assert complex_result == True, f"Expected complex expression to be True, got {complex_result}"
    print("All logical operations are correct!")
    
    # ========================================
    # Task 4: Assignment Operators
    # ========================================
    print("\n--- Task 4: Assignment Operators ---")
    
    # Create a variable 'value' with initial value 10
    value = 10
    
    print(f"Initial value: {value}")
    
    # 1. Add 5 to value using +=
    value += 5
    print(f"After adding 5: {value}")  # value = 15
    
    # 2. Subtract 3 from value using -=
    value -= 3
    print(f"After subtracting 3: {value}")  # value = 12
    
    # 3. Multiply value by 2 using *=
    value *= 2
    print(f"After multiplying by 2: {value}")  # value = 24
    
    # 4. Divide value by 4 using /=
    value /= 4
    print(f"After dividing by 4: {value}")  # value = 6.0
    
    # 5. Calculate value to the power of 2 using **=
    value **= 2
    print(f"After raising to power of 2: {value}")  # value = 36.0
    
    # Test the final value
    assert value == 36.0, f"Expected final value to be 36.0, got {value}"
    print("All assignment operations are correct!")
    
    # ========================================
    # Task 5: Identity and Membership Operators
    # ========================================
    print("\n--- Task 5: Identity and Membership Operators ---")
    
    # Create a list 'fruits' containing "apple", "banana", and "cherry"
    fruits = ["apple", "banana", "cherry"]
    
    # Create another list 'fruits_copy' with the same elements as 'fruits'
    fruits_copy = ["apple", "banana", "cherry"]
    
    # Create a variable 'same_list' that points to the 'fruits' list
    same_list = fruits
    
    # Check identity and membership
    is_same_identity = fruits is same_list
    is_same_value = fruits == fruits_copy
    is_same_object = fruits is fruits_copy
    has_apple = "apple" in fruits
    has_orange = "orange" in fruits
    
    # Print the results
    print(f"fruits: {fruits}")
    print(f"fruits_copy: {fruits_copy}")
    print(f"same_list: {same_list}")
    print(f"fruits and same_list are the same object: {is_same_identity}")
    print(f"fruits and fruits_copy have the same value: {is_same_value}")
    print(f"fruits and fruits_copy are the same object: {is_same_object}")
    print(f"'apple' is in fruits: {has_apple}")
    print(f"'orange' is in fruits: {has_orange}")
    
    # Test the identity and membership operations
    assert is_same_identity == True, f"Expected fruits and same_list to be the same object"
    assert is_same_value == True, f"Expected fruits and fruits_copy to have the same value"
    assert is_same_object == False, f"Expected fruits and fruits_copy to be different objects"
    assert has_apple == True, f"Expected 'apple' to be in fruits"
    assert has_orange == False, f"Expected 'orange' not to be in fruits"
    print("All identity and membership operations are correct!")
    
    # ========================================
    # Task 6: Operator Precedence
    # ========================================
    print("\n--- Task 6: Operator Precedence ---")
    
    # Calculate expressions with different precedence
    result1 = 2 + 3 * 4
    result2 = (2 + 3) * 4
    result3 = 10 / 2 + 3
    result4 = 10 / (2 + 3)
    result5 = 2 ** 3 ** 2  # Note: exponentiation is right-associative (2 ** (3 ** 2))
    result6 = (2 ** 3) ** 2
    
    # Print the results
    print(f"2 + 3 * 4 = {result1}")
    print(f"(2 + 3) * 4 = {result2}")
    print(f"10 / 2 + 3 = {result3}")
    print(f"10 / (2 + 3) = {result4}")
    print(f"2 ** 3 ** 2 = {result5}")
    print(f"(2 ** 3) ** 2 = {result6}")
    
    # Test the precedence calculations
    assert result1 == 14, f"Expected 2 + 3 * 4 to be 14, got {result1}"
    assert result2 == 20, f"Expected (2 + 3) * 4 to be 20, got {result2}"
    assert result3 == 8.0, f"Expected 10 / 2 + 3 to be 8.0, got {result3}"
    assert result4 == 2.0, f"Expected 10 / (2 + 3) to be 2.0, got {result4}"
    assert result5 == 512, f"Expected 2 ** 3 ** 2 to be 512, got {result5}"
    assert result6 == 64, f"Expected (2 ** 3) ** 2 to be 64, got {result6}"
    print("All precedence calculations are correct!")
    
    # ========================================
    # Task 7: Challenge - Complex Expressions
    # ========================================
    print("\n--- Task 7: Challenge - Complex Expressions ---")
    
    # Create variables m, n, and p
    m = 5
    n = 2
    p = 3
    
    # Calculate complex expressions
    expression1 = (m + n) * p - m / n
    expression2 = m ** n + p * (m - n)
    expression3 = (m + n) * p > m ** p or m + n == p * 2 + 1
    
    # Print the results
    print(f"m = {m}, n = {n}, p = {p}")
    print(f"(m + n) * p - m / n = {expression1}")
    print(f"m ** n + p * (m - n) = {expression2}")
    print(f"(m + n) * p > m ** p or m + n == p * 2 + 1: {expression3}")
    
    # Test the complex expressions
    assert expression1 == 19.5, f"Expected (m + n) * p - m / n to be 19.5, got {expression1}"
    assert expression2 == 34, f"Expected m ** n + p * (m - n) to be 34, got {expression2}"
    assert expression3 == True, f"Expected the complex boolean expression to be True, got {expression3}"
    print("All complex expressions are correct!")
    
    print("\nCongratulations! You've completed the basic operators exercise.")

if __name__ == "__main__":
    main()