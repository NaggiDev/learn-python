"""
Map, Filter, and Reduce - Solutions

This file contains the solutions for the map, filter, and reduce exercises.
"""

from functools import reduce

# Exercise 1: Basic map() usage
# Convert temperatures from Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = map(lambda c: c * 9/5 + 32, celsius_temps)

# Exercise 2: map() with string operations
# Capitalize the first letter of each word
words = ['hello', 'world', 'python', 'programming']
capitalized_words = map(str.capitalize, words)

# Exercise 3: map() with multiple iterables
# Calculate area of rectangles
lengths = [5, 3, 8, 2]
widths = [4, 6, 2, 9]
areas = map(lambda l, w: l * w, lengths, widths)

# Exercise 4: Basic filter() usage
# Get only positive numbers
numbers = [-5, 3, -2, 8, 0, -1, 7, 4]
positive_numbers = filter(lambda x: x > 0, numbers)

# Exercise 5: filter() with string conditions
# Get words that contain the letter 'a'
word_list = ['cat', 'dog', 'elephant', 'bird', 'snake', 'rabbit']
words_with_a = filter(lambda word: 'a' in word, word_list)

# Exercise 6: filter() with complex conditions
# Filter products that are in stock and cost less than $100
products = [
    {'name': 'Laptop', 'price': 999, 'in_stock': True},
    {'name': 'Mouse', 'price': 25, 'in_stock': True},
    {'name': 'Keyboard', 'price': 75, 'in_stock': False},
    {'name': 'Monitor', 'price': 300, 'in_stock': True},
    {'name': 'Headphones', 'price': 50, 'in_stock': True}
]
affordable_available = filter(lambda p: p['in_stock'] and p['price'] < 100, products)

# Exercise 7: Basic reduce() usage
# Find the sum of all numbers
numbers_to_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = reduce(lambda x, y: x + y, numbers_to_sum)

# Exercise 8: reduce() to find maximum
# Find the maximum number
numbers_for_max = [23, 45, 12, 67, 34, 89, 56]
maximum_number = reduce(lambda x, y: x if x > y else y, numbers_for_max)

# Exercise 9: reduce() for string concatenation
# Concatenate strings with space separator
string_parts = ['Python', 'is', 'an', 'awesome', 'language']
concatenated_string = reduce(lambda x, y: x + ' ' + y, string_parts)

# Exercise 10: Combining map(), filter(), and reduce()
# Square all even numbers and sum them
numbers_for_combo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
combo_result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers_for_combo))
)

# Exercise 11: Data processing with map()
# Extract names and convert to uppercase
employees = [
    {'name': 'alice', 'department': 'engineering', 'salary': 75000},
    {'name': 'bob', 'department': 'marketing', 'salary': 65000},
    {'name': 'charlie', 'department': 'engineering', 'salary': 80000}
]
employee_names_upper = map(lambda emp: emp['name'].upper(), employees)

# Exercise 12: Advanced filter() usage
# Filter high-paid engineers
high_paid_engineers = filter(
    lambda emp: emp['department'] == 'engineering' and emp['salary'] > 70000,
    employees
)

# Exercise 13: reduce() for complex aggregation
# Find employee with highest salary
highest_paid_employee = reduce(
    lambda x, y: x if x['salary'] > y['salary'] else y,
    employees
)

# Exercise 14: Nested data processing
# Calculate total sales for each person
sales_data = [
    {'name': 'John', 'sales': [100, 200, 150]},
    {'name': 'Jane', 'sales': [300, 250, 400]},
    {'name': 'Bob', 'sales': [180, 220, 160]}
]
total_sales_per_person = map(
    lambda person: reduce(lambda x, y: x + y, person['sales']),
    sales_data
)

# Exercise 15: Chain operations for data analysis
# Find the name of person with highest total sales
top_salesperson = reduce(
    lambda x, y: x if x[1] > y[1] else y,
    map(lambda person: (person['name'], reduce(lambda x, y: x + y, person['sales'])), sales_data)
)[0]

def demonstrate_solutions():
    """Demonstrate all the solutions"""
    print("Map, Filter, and Reduce Solutions Demonstration\n")
    
    # Exercise 1
    print("1. Celsius to Fahrenheit conversion:")
    print(f"   Celsius: {celsius_temps}")
    print(f"   Fahrenheit: {list(fahrenheit_temps)}")
    
    # Exercise 2
    print("\n2. Capitalized words:")
    print(f"   Original: {words}")
    print(f"   Capitalized: {list(capitalized_words)}")
    
    # Exercise 3
    print("\n3. Rectangle areas:")
    print(f"   Lengths: {lengths}")
    print(f"   Widths: {widths}")
    print(f"   Areas: {list(areas)}")
    
    # Exercise 4
    print("\n4. Positive numbers:")
    print(f"   Original: {numbers}")
    print(f"   Positive: {list(positive_numbers)}")
    
    # Exercise 5
    print("\n5. Words containing 'a':")
    print(f"   Original: {word_list}")
    print(f"   With 'a': {list(words_with_a)}")
    
    # Exercise 6
    print("\n6. Affordable available products:")
    affordable_list = list(affordable_available)
    for product in affordable_list:
        print(f"   {product['name']}: ${product['price']}")
    
    # Exercise 7
    print(f"\n7. Sum of numbers 1-10: {total_sum}")
    
    # Exercise 8
    print(f"8. Maximum number: {maximum_number}")
    
    # Exercise 9
    print(f"9. Concatenated string: '{concatenated_string}'")
    
    # Exercise 10
    print(f"10. Sum of squared even numbers: {combo_result}")
    
    # Exercise 11
    print("\n11. Employee names (uppercase):")
    print(f"    {list(employee_names_upper)}")
    
    # Exercise 12
    print("\n12. High-paid engineers:")
    for emp in high_paid_engineers:
        print(f"    {emp['name']}: ${emp['salary']}")
    
    # Exercise 13
    print(f"\n13. Highest paid employee: {highest_paid_employee['name']} (${highest_paid_employee['salary']})")
    
    # Exercise 14
    print("\n14. Total sales per person:")
    sales_totals = list(total_sales_per_person)
    for i, person in enumerate(sales_data):
        print(f"    {person['name']}: ${sales_totals[i]}")
    
    # Exercise 15
    print(f"\n15. Top salesperson: {top_salesperson}")

def additional_examples():
    """Show additional examples and patterns"""
    print("\n" + "="*60)
    print("Additional Map, Filter, Reduce Examples")
    print("="*60)
    
    # Example 1: Data pipeline
    print("\n1. Data Processing Pipeline:")
    raw_data = [
        "  John Doe, 25, Engineer  ",
        "  Jane Smith, 30, Designer  ",
        "  Bob Johnson, 35, Manager  "
    ]
    
    # Clean, parse, and process data
    processed_data = list(map(
        lambda line: {
            'name': line.strip().split(', ')[0],
            'age': int(line.strip().split(', ')[1]),
            'role': line.strip().split(', ')[2]
        },
        filter(lambda line: line.strip(), raw_data)
    ))
    
    print("   Processed data:")
    for person in processed_data:
        print(f"     {person}")
    
    # Example 2: Statistical operations
    print("\n2. Statistical Operations:")
    scores = [85, 92, 78, 96, 88, 73, 91, 87, 94, 82]
    
    # Calculate mean
    mean = reduce(lambda x, y: x + y, scores) / len(scores)
    print(f"   Mean: {mean:.2f}")
    
    # Find scores above average
    above_average = list(filter(lambda score: score > mean, scores))
    print(f"   Above average scores: {above_average}")
    
    # Calculate variance
    squared_diffs = list(map(lambda x: (x - mean) ** 2, scores))
    variance = reduce(lambda x, y: x + y, squared_diffs) / len(scores)
    print(f"   Variance: {variance:.2f}")
    
    # Example 3: Text processing
    print("\n3. Text Processing:")
    text = "The quick brown fox jumps over the lazy dog"
    words = text.split()
    
    # Count words by length
    word_lengths = list(map(len, words))
    length_counts = reduce(
        lambda acc, length: {**acc, length: acc.get(length, 0) + 1},
        word_lengths,
        {}
    )
    print(f"   Word length distribution: {length_counts}")
    
    # Find longest words
    max_length = reduce(lambda x, y: max(x, y), word_lengths)
    longest_words = list(filter(lambda word: len(word) == max_length, words))
    print(f"   Longest words: {longest_words}")
    
    # Example 4: Functional composition
    print("\n4. Functional Composition:")
    
    # Create a pipeline of transformations
    def compose(*functions):
        return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)
    
    # Define individual transformations
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    # Compose functions
    pipeline = compose(square, multiply_by_two, add_one)
    
    test_numbers = [1, 2, 3, 4, 5]
    results = list(map(pipeline, test_numbers))
    print(f"   Input: {test_numbers}")
    print(f"   Pipeline (add_one -> multiply_by_two -> square): {results}")
    
    # Example 5: Error handling in functional operations
    print("\n5. Error Handling:")
    mixed_data = ['1', '2', 'invalid', '4', '5', 'also_invalid', '7']
    
    def safe_int_convert(s):
        try:
            return int(s)
        except ValueError:
            return None
    
    # Convert and filter out None values
    converted = list(filter(
        lambda x: x is not None,
        map(safe_int_convert, mixed_data)
    ))
    print(f"   Original: {mixed_data}")
    print(f"   Converted integers: {converted}")
    
    # Sum the valid numbers
    total = reduce(lambda x, y: x + y, converted, 0)
    print(f"   Sum: {total}")

if __name__ == "__main__":
    demonstrate_solutions()
    additional_examples()