"""
NumPy Basics Exercises

This exercise file covers fundamental NumPy operations including:
- Array creation and manipulation
- Indexing and slicing
- Mathematical operations
- Array reshaping and broadcasting

Complete each exercise by implementing the required functionality.
Run the tests to verify your solutions.
"""

import numpy as np


def exercise_1_array_creation():
    """
    Exercise 1: Array Creation
    
    Create the following arrays:
    1. A 1D array with integers from 0 to 9
    2. A 2D array of zeros with shape (3, 4)
    3. A 3x3 identity matrix
    4. An array of 10 evenly spaced numbers between 0 and 1
    5. A 2x3 array filled with the value 7
    
    Returns:
        tuple: (array_1d, zeros_2d, identity_3x3, linspace_array, filled_array)
    """
    # TODO: Implement array creation
    array_1d = None
    zeros_2d = None
    identity_3x3 = None
    linspace_array = None
    filled_array = None
    
    return array_1d, zeros_2d, identity_3x3, linspace_array, filled_array


def exercise_2_array_properties():
    """
    Exercise 2: Array Properties
    
    Given an array, return its properties:
    - shape
    - size (total number of elements)
    - number of dimensions
    - data type
    
    Args:
        arr: Input NumPy array
        
    Returns:
        tuple: (shape, size, ndim, dtype)
    """
    # Create a test array for this exercise
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    
    # TODO: Extract array properties
    shape = None
    size = None
    ndim = None
    dtype = None
    
    return shape, size, ndim, dtype


def exercise_3_indexing_slicing():
    """
    Exercise 3: Indexing and Slicing
    
    Given a 2D array, perform the following operations:
    1. Extract the element at row 1, column 2
    2. Extract the entire second row
    3. Extract the entire third column
    4. Extract a 2x2 subarray from the top-left corner
    5. Extract all elements greater than 5
    
    Returns:
        tuple: (element, second_row, third_column, subarray, greater_than_5)
    """
    # Test array
    arr = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])
    
    # TODO: Implement indexing and slicing operations
    element = None
    second_row = None
    third_column = None
    subarray = None
    greater_than_5 = None
    
    return element, second_row, third_column, subarray, greater_than_5


def exercise_4_mathematical_operations():
    """
    Exercise 4: Mathematical Operations
    
    Perform element-wise operations on two arrays:
    1. Addition
    2. Multiplication
    3. Square root of the first array
    4. Exponential of the second array
    5. Element-wise maximum of both arrays
    
    Returns:
        tuple: (addition, multiplication, sqrt_a, exp_b, element_max)
    """
    a = np.array([1, 4, 9, 16])
    b = np.array([2, 3, 4, 5])
    
    # TODO: Implement mathematical operations
    addition = None
    multiplication = None
    sqrt_a = None
    exp_b = None
    element_max = None
    
    return addition, multiplication, sqrt_a, exp_b, element_max


def exercise_5_array_reshaping():
    """
    Exercise 5: Array Reshaping
    
    Given a 1D array of 12 elements:
    1. Reshape it to a 3x4 matrix
    2. Reshape it to a 2x2x3 array
    3. Transpose the 3x4 matrix
    4. Flatten the 3x4 matrix back to 1D
    
    Returns:
        tuple: (matrix_3x4, array_2x2x3, transposed, flattened)
    """
    arr = np.arange(12)
    
    # TODO: Implement reshaping operations
    matrix_3x4 = None
    array_2x2x3 = None
    transposed = None
    flattened = None
    
    return matrix_3x4, array_2x2x3, transposed, flattened


def exercise_6_broadcasting():
    """
    Exercise 6: Broadcasting
    
    Demonstrate broadcasting with:
    1. Add a scalar (10) to a 2D array
    2. Add a 1D array to each row of a 2D array
    3. Multiply a column vector by a row vector
    
    Returns:
        tuple: (scalar_broadcast, row_broadcast, outer_product)
    """
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_1d = np.array([10, 20, 30])
    col_vector = np.array([[1], [2]])
    row_vector = np.array([10, 20, 30])
    
    # TODO: Implement broadcasting operations
    scalar_broadcast = None
    row_broadcast = None
    outer_product = None
    
    return scalar_broadcast, row_broadcast, outer_product


def exercise_7_aggregation_functions():
    """
    Exercise 7: Aggregation Functions
    
    Calculate statistics for a 2D array:
    1. Sum of all elements
    2. Mean along rows (axis=0)
    3. Maximum along columns (axis=1)
    4. Standard deviation of the entire array
    5. Index of the minimum element (flattened array)
    
    Returns:
        tuple: (total_sum, row_means, col_maxes, std_dev, min_index)
    """
    arr = np.array([[1, 8, 3],
                    [4, 2, 9],
                    [7, 6, 5]])
    
    # TODO: Implement aggregation functions
    total_sum = None
    row_means = None
    col_maxes = None
    std_dev = None
    min_index = None
    
    return total_sum, row_means, col_maxes, std_dev, min_index


def exercise_8_linear_algebra():
    """
    Exercise 8: Linear Algebra Operations
    
    Perform linear algebra operations:
    1. Matrix multiplication of two 2x2 matrices
    2. Transpose of the first matrix
    3. Determinant of the first matrix
    4. Inverse of the first matrix (if possible)
    
    Returns:
        tuple: (matrix_mult, transpose, determinant, inverse)
    """
    A = np.array([[2, 1], [1, 3]])
    B = np.array([[1, 2], [3, 1]])
    
    # TODO: Implement linear algebra operations
    matrix_mult = None
    transpose = None
    determinant = None
    inverse = None
    
    return matrix_mult, transpose, determinant, inverse


def exercise_9_boolean_indexing():
    """
    Exercise 9: Boolean Indexing and Conditional Operations
    
    Given an array of random integers:
    1. Create a boolean mask for values greater than 5
    2. Replace all values less than 3 with 0
    3. Find indices where values equal 7
    4. Count how many values are between 3 and 7 (inclusive)
    
    Returns:
        tuple: (mask, modified_array, indices_of_7, count_between_3_and_7)
    """
    np.random.seed(42)  # For reproducible results
    arr = np.random.randint(0, 10, (4, 5))
    
    # TODO: Implement boolean indexing operations
    mask = None
    modified_array = None
    indices_of_7 = None
    count_between_3_and_7 = None
    
    return mask, modified_array, indices_of_7, count_between_3_and_7


def exercise_10_performance_comparison():
    """
    Exercise 10: Performance Comparison
    
    Compare the performance of Python loops vs NumPy vectorized operations
    for calculating the sum of squares of a large array.
    
    Implement both methods and return their execution times.
    
    Returns:
        tuple: (python_time, numpy_time, speedup_factor)
    """
    import time
    
    # Create a large array for testing
    large_array = np.random.random(100000)
    
    # TODO: Implement Python loop version
    def python_sum_of_squares(arr):
        # Convert to Python list and use loop
        python_list = arr.tolist()
        total = 0
        for x in python_list:
            total += x * x
        return total
    
    # TODO: Implement NumPy vectorized version
    def numpy_sum_of_squares(arr):
        return None  # Replace with NumPy implementation
    
    # Time the Python version
    start_time = time.time()
    python_result = python_sum_of_squares(large_array)
    python_time = time.time() - start_time
    
    # Time the NumPy version
    start_time = time.time()
    numpy_result = numpy_sum_of_squares(large_array)
    numpy_time = time.time() - start_time
    
    # Calculate speedup factor
    speedup_factor = python_time / numpy_time if numpy_time > 0 else 0
    
    return python_time, numpy_time, speedup_factor


# Test functions
def test_exercise_1():
    """Test array creation exercise"""
    array_1d, zeros_2d, identity_3x3, linspace_array, filled_array = exercise_1_array_creation()
    
    assert array_1d is not None and np.array_equal(array_1d, np.arange(10)), "1D array incorrect"
    assert zeros_2d is not None and zeros_2d.shape == (3, 4) and np.all(zeros_2d == 0), "Zeros array incorrect"
    assert identity_3x3 is not None and np.array_equal(identity_3x3, np.eye(3)), "Identity matrix incorrect"
    assert linspace_array is not None and len(linspace_array) == 10, "Linspace array incorrect"
    assert filled_array is not None and filled_array.shape == (2, 3) and np.all(filled_array == 7), "Filled array incorrect"
    
    print("✓ Exercise 1 passed: Array creation")


def test_exercise_2():
    """Test array properties exercise"""
    shape, size, ndim, dtype = exercise_2_array_properties()
    
    assert shape == (2, 2, 2), f"Shape incorrect: expected (2, 2, 2), got {shape}"
    assert size == 8, f"Size incorrect: expected 8, got {size}"
    assert ndim == 3, f"Dimensions incorrect: expected 3, got {ndim}"
    assert dtype == np.int64 or dtype == np.int32, f"Data type incorrect: got {dtype}"
    
    print("✓ Exercise 2 passed: Array properties")


def test_exercise_3():
    """Test indexing and slicing exercise"""
    element, second_row, third_column, subarray, greater_than_5 = exercise_3_indexing_slicing()
    
    assert element == 7, f"Element incorrect: expected 7, got {element}"
    assert np.array_equal(second_row, [5, 6, 7, 8]), "Second row incorrect"
    assert np.array_equal(third_column, [3, 7, 11]), "Third column incorrect"
    assert subarray.shape == (2, 2), "Subarray shape incorrect"
    assert len(greater_than_5) == 7, "Boolean indexing incorrect"
    
    print("✓ Exercise 3 passed: Indexing and slicing")


def test_exercise_4():
    """Test mathematical operations exercise"""
    addition, multiplication, sqrt_a, exp_b, element_max = exercise_4_mathematical_operations()
    
    assert addition is not None and np.array_equal(addition, [3, 7, 13, 21]), "Addition incorrect"
    assert multiplication is not None and np.array_equal(multiplication, [2, 12, 36, 80]), "Multiplication incorrect"
    assert sqrt_a is not None and np.allclose(sqrt_a, [1, 2, 3, 4]), "Square root incorrect"
    assert exp_b is not None and len(exp_b) == 4, "Exponential incorrect"
    assert element_max is not None and np.array_equal(element_max, [2, 4, 9, 16]), "Element-wise max incorrect"
    
    print("✓ Exercise 4 passed: Mathematical operations")


def test_exercise_5():
    """Test array reshaping exercise"""
    matrix_3x4, array_2x2x3, transposed, flattened = exercise_5_array_reshaping()
    
    assert matrix_3x4 is not None and matrix_3x4.shape == (3, 4), "3x4 reshape incorrect"
    assert array_2x2x3 is not None and array_2x2x3.shape == (2, 2, 3), "2x2x3 reshape incorrect"
    assert transposed is not None and transposed.shape == (4, 3), "Transpose incorrect"
    assert flattened is not None and flattened.shape == (12,), "Flatten incorrect"
    
    print("✓ Exercise 5 passed: Array reshaping")


def test_exercise_6():
    """Test broadcasting exercise"""
    scalar_broadcast, row_broadcast, outer_product = exercise_6_broadcasting()
    
    assert scalar_broadcast is not None and scalar_broadcast.shape == (2, 3), "Scalar broadcast incorrect"
    assert row_broadcast is not None and row_broadcast.shape == (2, 3), "Row broadcast incorrect"
    assert outer_product is not None and outer_product.shape == (2, 3), "Outer product incorrect"
    
    print("✓ Exercise 6 passed: Broadcasting")


def test_exercise_7():
    """Test aggregation functions exercise"""
    total_sum, row_means, col_maxes, std_dev, min_index = exercise_7_aggregation_functions()
    
    assert total_sum == 45, f"Total sum incorrect: expected 45, got {total_sum}"
    assert row_means is not None and len(row_means) == 3, "Row means incorrect"
    assert col_maxes is not None and len(col_maxes) == 3, "Column maxes incorrect"
    assert std_dev is not None and std_dev > 0, "Standard deviation incorrect"
    assert min_index is not None, "Min index incorrect"
    
    print("✓ Exercise 7 passed: Aggregation functions")


def test_exercise_8():
    """Test linear algebra exercise"""
    matrix_mult, transpose, determinant, inverse = exercise_8_linear_algebra()
    
    assert matrix_mult is not None and matrix_mult.shape == (2, 2), "Matrix multiplication incorrect"
    assert transpose is not None and transpose.shape == (2, 2), "Transpose incorrect"
    assert determinant is not None and isinstance(determinant, (int, float, np.number)), "Determinant incorrect"
    assert inverse is not None and inverse.shape == (2, 2), "Inverse incorrect"
    
    print("✓ Exercise 8 passed: Linear algebra")


def test_exercise_9():
    """Test boolean indexing exercise"""
    mask, modified_array, indices_of_7, count_between_3_and_7 = exercise_9_boolean_indexing()
    
    assert mask is not None and mask.dtype == bool, "Boolean mask incorrect"
    assert modified_array is not None and modified_array.shape == (4, 5), "Modified array incorrect"
    assert indices_of_7 is not None, "Indices of 7 incorrect"
    assert count_between_3_and_7 is not None and isinstance(count_between_3_and_7, (int, np.integer)), "Count incorrect"
    
    print("✓ Exercise 9 passed: Boolean indexing")


def test_exercise_10():
    """Test performance comparison exercise"""
    python_time, numpy_time, speedup_factor = exercise_10_performance_comparison()
    
    assert python_time > 0, "Python time should be positive"
    assert numpy_time > 0, "NumPy time should be positive"
    assert speedup_factor > 1, f"NumPy should be faster: speedup factor {speedup_factor}"
    
    print(f"✓ Exercise 10 passed: Performance comparison (NumPy is {speedup_factor:.1f}x faster)")


def run_all_tests():
    """Run all exercise tests"""
    print("Running NumPy Basics Exercises Tests...\n")
    
    try:
        test_exercise_1()
        test_exercise_2()
        test_exercise_3()
        test_exercise_4()
        test_exercise_5()
        test_exercise_6()
        test_exercise_7()
        test_exercise_8()
        test_exercise_9()
        test_exercise_10()
        
        print("\n🎉 All NumPy exercises completed successfully!")
        print("\nKey concepts mastered:")
        print("- Array creation and manipulation")
        print("- Indexing, slicing, and boolean operations")
        print("- Mathematical and statistical operations")
        print("- Broadcasting and vectorization")
        print("- Linear algebra operations")
        print("- Performance optimization with NumPy")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("Please review your implementation and try again.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your code for syntax errors.")


if __name__ == "__main__":
    run_all_tests()