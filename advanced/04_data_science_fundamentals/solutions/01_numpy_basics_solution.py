"""
NumPy Basics Exercises - Solutions

This file contains the complete solutions for all NumPy exercises.
Study these solutions to understand the correct implementation patterns.
"""

import numpy as np
import time


def exercise_1_array_creation():
    """
    Exercise 1: Array Creation - SOLUTION
    """
    # 1. A 1D array with integers from 0 to 9
    array_1d = np.arange(10)
    
    # 2. A 2D array of zeros with shape (3, 4)
    zeros_2d = np.zeros((3, 4))
    
    # 3. A 3x3 identity matrix
    identity_3x3 = np.eye(3)
    
    # 4. An array of 10 evenly spaced numbers between 0 and 1
    linspace_array = np.linspace(0, 1, 10)
    
    # 5. A 2x3 array filled with the value 7
    filled_array = np.full((2, 3), 7)
    
    return array_1d, zeros_2d, identity_3x3, linspace_array, filled_array


def exercise_2_array_properties():
    """
    Exercise 2: Array Properties - SOLUTION
    """
    # Create the test array
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    
    # Extract array properties
    shape = arr.shape        # (2, 2, 2)
    size = arr.size          # 8
    ndim = arr.ndim          # 3
    dtype = arr.dtype        # int64 (or int32 depending on system)
    
    return shape, size, ndim, dtype


def exercise_3_indexing_slicing():
    """
    Exercise 3: Indexing and Slicing - SOLUTION
    """
    # Test array
    arr = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])
    
    # 1. Extract the element at row 1, column 2
    element = arr[1, 2]  # 7
    
    # 2. Extract the entire second row (index 1)
    second_row = arr[1]  # [5, 6, 7, 8]
    
    # 3. Extract the entire third column (index 2)
    third_column = arr[:, 2]  # [3, 7, 11]
    
    # 4. Extract a 2x2 subarray from the top-left corner
    subarray = arr[0:2, 0:2]  # [[1, 2], [5, 6]]
    
    # 5. Extract all elements greater than 5
    greater_than_5 = arr[arr > 5]  # [6, 7, 8, 9, 10, 11, 12]
    
    return element, second_row, third_column, subarray, greater_than_5


def exercise_4_mathematical_operations():
    """
    Exercise 4: Mathematical Operations - SOLUTION
    """
    a = np.array([1, 4, 9, 16])
    b = np.array([2, 3, 4, 5])
    
    # 1. Addition
    addition = a + b  # [3, 7, 13, 21]
    
    # 2. Multiplication
    multiplication = a * b  # [2, 12, 36, 80]
    
    # 3. Square root of the first array
    sqrt_a = np.sqrt(a)  # [1, 2, 3, 4]
    
    # 4. Exponential of the second array
    exp_b = np.exp(b)  # [e^2, e^3, e^4, e^5]
    
    # 5. Element-wise maximum of both arrays
    element_max = np.maximum(a, b)  # [2, 4, 9, 16]
    
    return addition, multiplication, sqrt_a, exp_b, element_max


def exercise_5_array_reshaping():
    """
    Exercise 5: Array Reshaping - SOLUTION
    """
    arr = np.arange(12)  # [0, 1, 2, ..., 11]
    
    # 1. Reshape it to a 3x4 matrix
    matrix_3x4 = arr.reshape(3, 4)
    
    # 2. Reshape it to a 2x2x3 array
    array_2x2x3 = arr.reshape(2, 2, 3)
    
    # 3. Transpose the 3x4 matrix
    transposed = matrix_3x4.T  # or matrix_3x4.transpose()
    
    # 4. Flatten the 3x4 matrix back to 1D
    flattened = matrix_3x4.flatten()  # or matrix_3x4.ravel()
    
    return matrix_3x4, array_2x2x3, transposed, flattened


def exercise_6_broadcasting():
    """
    Exercise 6: Broadcasting - SOLUTION
    """
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_1d = np.array([10, 20, 30])
    col_vector = np.array([[1], [2]])
    row_vector = np.array([10, 20, 30])
    
    # 1. Add a scalar (10) to a 2D array
    scalar_broadcast = arr_2d + 10  # [[11, 12, 13], [14, 15, 16]]
    
    # 2. Add a 1D array to each row of a 2D array
    row_broadcast = arr_2d + arr_1d  # [[11, 22, 33], [14, 25, 36]]
    
    # 3. Multiply a column vector by a row vector (outer product)
    outer_product = col_vector * row_vector  # [[10, 20, 30], [20, 40, 60]]
    
    return scalar_broadcast, row_broadcast, outer_product


def exercise_7_aggregation_functions():
    """
    Exercise 7: Aggregation Functions - SOLUTION
    """
    arr = np.array([[1, 8, 3],
                    [4, 2, 9],
                    [7, 6, 5]])
    
    # 1. Sum of all elements
    total_sum = np.sum(arr)  # 45
    
    # 2. Mean along rows (axis=0) - mean of each column
    row_means = np.mean(arr, axis=0)  # [4, 5.33, 5.67]
    
    # 3. Maximum along columns (axis=1) - max of each row
    col_maxes = np.max(arr, axis=1)  # [8, 9, 7]
    
    # 4. Standard deviation of the entire array
    std_dev = np.std(arr)  # ~2.58
    
    # 5. Index of the minimum element (flattened array)
    min_index = np.argmin(arr)  # 0 (element at position [0,0])
    
    return total_sum, row_means, col_maxes, std_dev, min_index


def exercise_8_linear_algebra():
    """
    Exercise 8: Linear Algebra Operations - SOLUTION
    """
    A = np.array([[2, 1], [1, 3]])
    B = np.array([[1, 2], [3, 1]])
    
    # 1. Matrix multiplication of two 2x2 matrices
    matrix_mult = np.dot(A, B)  # or A @ B
    # Result: [[5, 5], [10, 5]]
    
    # 2. Transpose of the first matrix
    transpose = A.T  # [[2, 1], [1, 3]]
    
    # 3. Determinant of the first matrix
    determinant = np.linalg.det(A)  # 5.0
    
    # 4. Inverse of the first matrix
    inverse = np.linalg.inv(A)  # [[0.6, -0.2], [-0.2, 0.4]]
    
    return matrix_mult, transpose, determinant, inverse


def exercise_9_boolean_indexing():
    """
    Exercise 9: Boolean Indexing and Conditional Operations - SOLUTION
    """
    np.random.seed(42)  # For reproducible results
    arr = np.random.randint(0, 10, (4, 5))
    
    # 1. Create a boolean mask for values greater than 5
    mask = arr > 5
    
    # 2. Replace all values less than 3 with 0
    modified_array = np.where(arr < 3, 0, arr)
    
    # 3. Find indices where values equal 7
    indices_of_7 = np.where(arr == 7)
    
    # 4. Count how many values are between 3 and 7 (inclusive)
    count_between_3_and_7 = np.sum((arr >= 3) & (arr <= 7))
    
    return mask, modified_array, indices_of_7, count_between_3_and_7


def exercise_10_performance_comparison():
    """
    Exercise 10: Performance Comparison - SOLUTION
    """
    # Create a large array for testing
    large_array = np.random.random(100000)
    
    # Python loop version
    def python_sum_of_squares(arr):
        python_list = arr.tolist()
        total = 0
        for x in python_list:
            total += x * x
        return total
    
    # NumPy vectorized version
    def numpy_sum_of_squares(arr):
        return np.sum(arr ** 2)
    
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


# Demonstration function to show all solutions
def demonstrate_solutions():
    """
    Demonstrate all exercise solutions with explanations
    """
    print("NumPy Basics Exercises - Solutions Demonstration")
    print("=" * 50)
    
    # Exercise 1
    print("\n1. Array Creation:")
    array_1d, zeros_2d, identity_3x3, linspace_array, filled_array = exercise_1_array_creation()
    print(f"1D array: {array_1d}")
    print(f"Zeros 2D shape: {zeros_2d.shape}")
    print(f"Identity matrix:\n{identity_3x3}")
    print(f"Linspace array: {linspace_array}")
    print(f"Filled array:\n{filled_array}")
    
    # Exercise 2
    print("\n2. Array Properties:")
    shape, size, ndim, dtype = exercise_2_array_properties()
    print(f"Shape: {shape}, Size: {size}, Dimensions: {ndim}, Type: {dtype}")
    
    # Exercise 3
    print("\n3. Indexing and Slicing:")
    element, second_row, third_column, subarray, greater_than_5 = exercise_3_indexing_slicing()
    print(f"Element at [1,2]: {element}")
    print(f"Second row: {second_row}")
    print(f"Third column: {third_column}")
    print(f"2x2 subarray:\n{subarray}")
    print(f"Elements > 5: {greater_than_5}")
    
    # Exercise 4
    print("\n4. Mathematical Operations:")
    addition, multiplication, sqrt_a, exp_b, element_max = exercise_4_mathematical_operations()
    print(f"Addition: {addition}")
    print(f"Multiplication: {multiplication}")
    print(f"Square root: {sqrt_a}")
    print(f"Element-wise max: {element_max}")
    
    # Exercise 5
    print("\n5. Array Reshaping:")
    matrix_3x4, array_2x2x3, transposed, flattened = exercise_5_array_reshaping()
    print(f"3x4 matrix:\n{matrix_3x4}")
    print(f"Transposed shape: {transposed.shape}")
    print(f"Flattened: {flattened}")
    
    # Exercise 6
    print("\n6. Broadcasting:")
    scalar_broadcast, row_broadcast, outer_product = exercise_6_broadcasting()
    print(f"Scalar broadcast:\n{scalar_broadcast}")
    print(f"Row broadcast:\n{row_broadcast}")
    print(f"Outer product:\n{outer_product}")
    
    # Exercise 7
    print("\n7. Aggregation Functions:")
    total_sum, row_means, col_maxes, std_dev, min_index = exercise_7_aggregation_functions()
    print(f"Total sum: {total_sum}")
    print(f"Row means: {row_means}")
    print(f"Column maxes: {col_maxes}")
    print(f"Standard deviation: {std_dev:.2f}")
    print(f"Min index: {min_index}")
    
    # Exercise 8
    print("\n8. Linear Algebra:")
    matrix_mult, transpose, determinant, inverse = exercise_8_linear_algebra()
    print(f"Matrix multiplication:\n{matrix_mult}")
    print(f"Determinant: {determinant}")
    print(f"Inverse:\n{inverse}")
    
    # Exercise 9
    print("\n9. Boolean Indexing:")
    mask, modified_array, indices_of_7, count_between_3_and_7 = exercise_9_boolean_indexing()
    print(f"Boolean mask shape: {mask.shape}")
    print(f"Modified array shape: {modified_array.shape}")
    print(f"Count between 3 and 7: {count_between_3_and_7}")
    
    # Exercise 10
    print("\n10. Performance Comparison:")
    python_time, numpy_time, speedup_factor = exercise_10_performance_comparison()
    print(f"Python time: {python_time:.4f}s")
    print(f"NumPy time: {numpy_time:.4f}s")
    print(f"Speedup factor: {speedup_factor:.1f}x")
    
    print("\n" + "=" * 50)
    print("All solutions demonstrated successfully!")


if __name__ == "__main__":
    demonstrate_solutions()