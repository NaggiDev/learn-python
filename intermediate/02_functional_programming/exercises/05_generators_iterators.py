"""
Generators and Iterators Exercises

Complete the following exercises to practice creating and using generators and iterators.
Each exercise has test cases to verify your solution.
"""

import sys
import time

# Exercise 1: Basic Iterator Class
# TODO: Create a custom iterator class that counts down from a given number
class CountDown:
    def __init__(self, start):
        # Your implementation here
        pass
    
    def __iter__(self):
        # Your implementation here
        pass
    
    def __next__(self):
        # Your implementation here
        pass

# Exercise 2: Basic Generator Function
# TODO: Create a generator function that yields numbers from 1 to n
def number_generator(n):
    # Your implementation here
    pass

# Exercise 3: Fibonacci Generator
# TODO: Create a generator that yields Fibonacci numbers
def fibonacci_generator():
    # Your implementation here
    pass

# Exercise 4: Even Numbers Generator
# TODO: Create a generator that yields only even numbers from a given range
def even_numbers(start, end):
    # Your implementation here
    pass

# Exercise 5: Generator Expression
# TODO: Create a generator expression that yields squares of numbers from 1 to n
def squares_generator(n):
    # Return a generator expression
    pass

# Exercise 6: File Line Generator
# TODO: Create a generator that reads lines from a file (simulate with a list)
def file_lines(lines_list):
    # Your implementation here - treat lines_list as file content
    pass

# Exercise 7: Infinite Generator
# TODO: Create an infinite generator that cycles through a given list
def cycle_generator(items):
    # Your implementation here
    pass

# Exercise 8: Generator Pipeline
# TODO: Create generators that can be chained together
def data_source():
    """Generate numbers 1-10"""
    # Your implementation here
    pass

def filter_evens(data):
    """Filter even numbers from data generator"""
    # Your implementation here
    pass

def square_numbers(data):
    """Square numbers from data generator"""
    # Your implementation here
    pass

# Exercise 9: Generator with Send
# TODO: Create a generator that can receive values using send()
def accumulator_generator():
    # Your implementation here
    pass

# Exercise 10: Tree Traversal Generator
# TODO: Create a generator for tree traversal
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    # Your implementation here
    pass

# Exercise 11: Batch Generator
# TODO: Create a generator that yields items in batches
def batch_generator(items, batch_size):
    # Your implementation here
    pass

# Exercise 12: Prime Numbers Generator
# TODO: Create a generator that yields prime numbers
def prime_generator():
    # Your implementation here
    pass

# Exercise 13: Generator Decorator
# TODO: Create a decorator that converts a function's return value into a generator
def make_generator(func):
    # Your implementation here
    pass

# Exercise 14: Memory-Efficient Data Processing
# TODO: Create a generator that processes large amounts of data efficiently
def process_large_data(data_size):
    """
    Simulate processing large dataset without loading everything into memory
    Generate data_size number of processed items
    """
    # Your implementation here
    pass

# Exercise 15: Custom Range Generator
# TODO: Create a custom range generator with step functionality
def custom_range(start, stop=None, step=1):
    # Your implementation here - should work like built-in range()
    pass


# Test Functions
def test_exercise_1():
    """Test CountDown iterator"""
    print("Testing Exercise 1: CountDown Iterator")
    try:
        countdown = CountDown(3)
        result = list(countdown)
        expected = [3, 2, 1]
        assert result == expected, f"Expected {expected}, got {result}"
        
        # Test iterator protocol
        countdown2 = CountDown(2)
        assert hasattr(countdown2, '__iter__'), "CountDown should have __iter__ method"
        assert hasattr(countdown2, '__next__'), "CountDown should have __next__ method"
        
        print("✅ Exercise 1: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 1: {e}")
        return False

def test_exercise_2():
    """Test number generator"""
    print("\nTesting Exercise 2: Number Generator")
    try:
        gen = number_generator(5)
        result = list(gen)
        expected = [1, 2, 3, 4, 5]
        assert result == expected, f"Expected {expected}, got {result}"
        
        # Test it's actually a generator
        gen2 = number_generator(3)
        assert hasattr(gen2, '__next__'), "Should return a generator"
        
        print("✅ Exercise 2: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 2: {e}")
        return False

def test_exercise_3():
    """Test Fibonacci generator"""
    print("\nTesting Exercise 3: Fibonacci Generator")
    try:
        fib_gen = fibonacci_generator()
        result = [next(fib_gen) for _ in range(8)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13]
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 3: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 3: {e}")
        return False

def test_exercise_4():
    """Test even numbers generator"""
    print("\nTesting Exercise 4: Even Numbers Generator")
    try:
        gen = even_numbers(1, 10)
        result = list(gen)
        expected = [2, 4, 6, 8, 10]
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 4: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 4: {e}")
        return False

def test_exercise_5():
    """Test squares generator expression"""
    print("\nTesting Exercise 5: Squares Generator")
    try:
        gen = squares_generator(5)
        result = list(gen)
        expected = [1, 4, 9, 16, 25]
        assert result == expected, f"Expected {expected}, got {result}"
        
        # Test it's a generator
        gen2 = squares_generator(3)
        assert hasattr(gen2, '__next__'), "Should return a generator"
        
        print("✅ Exercise 5: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 5: {e}")
        return False

def test_exercise_6():
    """Test file lines generator"""
    print("\nTesting Exercise 6: File Lines Generator")
    try:
        lines = ["line 1", "line 2", "line 3"]
        gen = file_lines(lines)
        result = list(gen)
        expected = ["line 1", "line 2", "line 3"]
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 6: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 6: {e}")
        return False

def test_exercise_7():
    """Test cycle generator"""
    print("\nTesting Exercise 7: Cycle Generator")
    try:
        gen = cycle_generator(['A', 'B', 'C'])
        result = [next(gen) for _ in range(7)]
        expected = ['A', 'B', 'C', 'A', 'B', 'C', 'A']
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 7: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 7: {e}")
        return False

def test_exercise_8():
    """Test generator pipeline"""
    print("\nTesting Exercise 8: Generator Pipeline")
    try:
        # Test individual generators
        data = list(data_source())
        assert data == list(range(1, 11)), f"data_source should yield 1-10, got {data}"
        
        # Test pipeline
        pipeline = square_numbers(filter_evens(data_source()))
        result = list(pipeline)
        expected = [4, 16, 36, 64, 100]  # squares of even numbers 2,4,6,8,10
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 8: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 8: {e}")
        return False

def test_exercise_9():
    """Test generator with send"""
    print("\nTesting Exercise 9: Accumulator Generator")
    try:
        gen = accumulator_generator()
        next(gen)  # Prime the generator
        
        result1 = gen.send(5)
        result2 = gen.send(3)
        result3 = gen.send(2)
        
        # Should accumulate: 5, 5+3=8, 8+2=10
        expected = [5, 8, 10]
        actual = [result1, result2, result3]
        assert actual == expected, f"Expected {expected}, got {actual}"
        
        print("✅ Exercise 9: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 9: {e}")
        return False

def test_exercise_10():
    """Test tree traversal generator"""
    print("\nTesting Exercise 10: Tree Traversal Generator")
    try:
        # Create a simple binary tree
        #       4
        #      / \
        #     2   6
        #    / \ / \
        #   1  3 5  7
        root = TreeNode(4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7))
        )
        
        result = list(inorder_traversal(root))
        expected = [1, 2, 3, 4, 5, 6, 7]
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 10: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 10: {e}")
        return False

def test_exercise_11():
    """Test batch generator"""
    print("\nTesting Exercise 11: Batch Generator")
    try:
        items = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        gen = batch_generator(items, 3)
        result = list(gen)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 11: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 11: {e}")
        return False

def test_exercise_12():
    """Test prime generator"""
    print("\nTesting Exercise 12: Prime Generator")
    try:
        gen = prime_generator()
        result = [next(gen) for _ in range(10)]
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 12: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 12: {e}")
        return False

def test_exercise_13():
    """Test generator decorator"""
    print("\nTesting Exercise 13: Generator Decorator")
    try:
        @make_generator
        def get_numbers():
            return [1, 2, 3, 4, 5]
        
        gen = get_numbers()
        assert hasattr(gen, '__next__'), "Decorated function should return a generator"
        
        result = list(gen)
        expected = [1, 2, 3, 4, 5]
        assert result == expected, f"Expected {expected}, got {result}"
        
        print("✅ Exercise 13: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 13: {e}")
        return False

def test_exercise_14():
    """Test memory-efficient data processing"""
    print("\nTesting Exercise 14: Memory-Efficient Data Processing")
    try:
        gen = process_large_data(5)
        assert hasattr(gen, '__next__'), "Should return a generator"
        
        result = list(gen)
        # Should process 5 items, exact processing depends on implementation
        assert len(result) == 5, f"Expected 5 processed items, got {len(result)}"
        
        # Test memory efficiency by checking it's actually a generator
        gen2 = process_large_data(1000)
        gen_size = sys.getsizeof(gen2)
        list_size = sys.getsizeof(list(range(1000)))
        assert gen_size < list_size, "Generator should be more memory efficient than list"
        
        print("✅ Exercise 14: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 14: {e}")
        return False

def test_exercise_15():
    """Test custom range generator"""
    print("\nTesting Exercise 15: Custom Range Generator")
    try:
        # Test basic range
        result1 = list(custom_range(5))
        expected1 = [0, 1, 2, 3, 4]
        assert result1 == expected1, f"Expected {expected1}, got {result1}"
        
        # Test range with start and stop
        result2 = list(custom_range(2, 7))
        expected2 = [2, 3, 4, 5, 6]
        assert result2 == expected2, f"Expected {expected2}, got {result2}"
        
        # Test range with step
        result3 = list(custom_range(0, 10, 2))
        expected3 = [0, 2, 4, 6, 8]
        assert result3 == expected3, f"Expected {expected3}, got {result3}"
        
        # Test it's a generator
        gen = custom_range(3)
        assert hasattr(gen, '__next__'), "Should return a generator"
        
        print("✅ Exercise 15: Passed")
        return True
    except Exception as e:
        print(f"❌ Exercise 15: {e}")
        return False

def run_all_tests():
    """Run all test functions"""
    print("Running Generators and Iterators Exercises Tests...\n")
    
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
        print("🎉 Congratulations! All generators and iterators exercises completed successfully!")
    else:
        print("📚 Keep working on the remaining exercises. Generators are powerful tools!")

if __name__ == "__main__":
    run_all_tests()