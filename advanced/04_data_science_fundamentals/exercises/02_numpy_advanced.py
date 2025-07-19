"""
Advanced NumPy Exercises

This exercise file covers advanced NumPy operations including:
- Working with structured arrays
- Advanced indexing techniques
- Image processing with arrays
- Time series analysis
- Statistical operations and random sampling

Complete each exercise by implementing the required functionality.
"""

import numpy as np
import matplotlib.pyplot as plt


def exercise_1_structured_arrays():
    """
    Exercise 1: Structured Arrays
    
    Create a structured array to represent student data with fields:
    - name (string, max 20 characters)
    - age (integer)
    - grade (float)
    - passed (boolean)
    
    Create 5 student records and perform operations:
    1. Find students with grade > 85
    2. Calculate average age of passed students
    3. Sort by grade in descending order
    
    Returns:
        tuple: (students_array, high_performers, avg_age_passed, sorted_by_grade)
    """
    # TODO: Define the structured array dtype
    dtype = None
    
    # TODO: Create sample student data
    students_data = [
        # Add 5 student records here
    ]
    
    # TODO: Create structured array
    students_array = None
    
    # TODO: Find students with grade > 85
    high_performers = None
    
    # TODO: Calculate average age of passed students
    avg_age_passed = None
    
    # TODO: Sort by grade in descending order
    sorted_by_grade = None
    
    return students_array, high_performers, avg_age_passed, sorted_by_grade


def exercise_2_image_processing():
    """
    Exercise 2: Image Processing with NumPy
    
    Create a synthetic image (2D array) and perform basic image operations:
    1. Create a 100x100 grayscale image with a gradient
    2. Add random noise to the image
    3. Apply a simple blur filter (3x3 averaging)
    4. Detect edges using a simple difference filter
    5. Create a binary mask for pixels above threshold
    
    Returns:
        tuple: (original_image, noisy_image, blurred_image, edges, binary_mask)
    """
    # TODO: Create a 100x100 gradient image
    # Hint: Use np.linspace and np.meshgrid or broadcasting
    original_image = None
    
    # TODO: Add random noise (normal distribution, std=0.1)
    noisy_image = None
    
    # TODO: Apply 3x3 averaging filter for blur effect
    # Hint: You can use nested loops or convolution-like operation
    blurred_image = None
    
    # TODO: Detect edges using gradient magnitude
    # Hint: Calculate differences in x and y directions
    edges = None
    
    # TODO: Create binary mask for pixels above mean value
    binary_mask = None
    
    return original_image, noisy_image, blurred_image, edges, binary_mask


def exercise_3_time_series_analysis():
    """
    Exercise 3: Time Series Analysis
    
    Generate and analyze a synthetic time series:
    1. Create a time series with trend, seasonality, and noise
    2. Calculate moving averages (window size 10)
    3. Find local maxima and minima
    4. Calculate autocorrelation at different lags
    5. Detect outliers using z-score method
    
    Returns:
        tuple: (time_series, moving_avg, local_maxima, local_minima, outliers)
    """
    # Generate time points
    t = np.linspace(0, 4*np.pi, 200)
    
    # TODO: Create time series with trend + seasonality + noise
    # Trend: linear increase
    # Seasonality: sine wave
    # Noise: random normal
    time_series = None
    
    # TODO: Calculate moving average with window size 10
    moving_avg = None
    
    # TODO: Find local maxima (peaks)
    # Hint: Compare each point with its neighbors
    local_maxima = None
    
    # TODO: Find local minima (valleys)
    local_minima = None
    
    # TODO: Detect outliers using z-score > 2
    outliers = None
    
    return time_series, moving_avg, local_maxima, local_minima, outliers


def exercise_4_statistical_sampling():
    """
    Exercise 4: Statistical Sampling and Distributions
    
    Perform various statistical sampling operations:
    1. Generate samples from different distributions
    2. Calculate empirical vs theoretical statistics
    3. Perform bootstrap sampling
    4. Create a histogram comparison
    5. Test central limit theorem
    
    Returns:
        tuple: (normal_samples, uniform_samples, bootstrap_means, clt_means)
    """
    np.random.seed(42)  # For reproducible results
    
    # TODO: Generate 1000 samples from normal distribution (mean=50, std=10)
    normal_samples = None
    
    # TODO: Generate 1000 samples from uniform distribution (0, 100)
    uniform_samples = None
    
    # TODO: Perform bootstrap sampling on normal_samples
    # Take 1000 bootstrap samples of size 30 and calculate their means
    bootstrap_means = None
    
    # TODO: Demonstrate Central Limit Theorem
    # Sample from exponential distribution, take means of samples of size 30
    # Repeat 1000 times
    clt_means = None
    
    return normal_samples, uniform_samples, bootstrap_means, clt_means


def exercise_5_matrix_operations():
    """
    Exercise 5: Advanced Matrix Operations
    
    Perform advanced linear algebra operations:
    1. Create a covariance matrix from data
    2. Perform eigendecomposition
    3. Calculate matrix rank and condition number
    4. Solve a system of linear equations
    5. Perform Singular Value Decomposition (SVD)
    
    Returns:
        tuple: (cov_matrix, eigenvals, eigenvecs, rank, condition_num, solution, U, s, Vt)
    """
    # Generate sample data matrix (100 samples, 5 features)
    np.random.seed(42)
    data = np.random.randn(100, 5)
    
    # TODO: Calculate covariance matrix
    cov_matrix = None
    
    # TODO: Perform eigendecomposition of covariance matrix
    eigenvals = None
    eigenvecs = None
    
    # TODO: Calculate matrix rank and condition number
    rank = None
    condition_num = None
    
    # TODO: Solve system Ax = b where A is 3x3 and b is 3x1
    A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])
    b = np.array([4, 5, 6])
    solution = None
    
    # TODO: Perform SVD on the data matrix
    U = None
    s = None
    Vt = None
    
    return cov_matrix, eigenvals, eigenvecs, rank, condition_num, solution, U, s, Vt


def exercise_6_advanced_indexing():
    """
    Exercise 6: Advanced Indexing and Fancy Operations
    
    Demonstrate advanced indexing techniques:
    1. Use fancy indexing to rearrange array elements
    2. Implement k-nearest neighbors search
    3. Create sparse matrix operations
    4. Perform conditional replacements
    5. Use advanced broadcasting
    
    Returns:
        tuple: (rearranged, nearest_neighbors, sparse_result, conditional_array, broadcast_result)
    """
    # Sample data
    np.random.seed(42)
    data = np.random.randn(20, 3)
    
    # TODO: Rearrange array using fancy indexing
    # Create indices to sort by the sum of each row
    indices = None
    rearranged = None
    
    # TODO: Find k=3 nearest neighbors for the first point
    # Calculate distances and find indices of 3 closest points
    query_point = data[0]
    distances = None
    nearest_neighbors = None
    
    # TODO: Create a sparse-like operation
    # Set small values (abs < 0.5) to zero
    sparse_result = None
    
    # TODO: Conditional replacement based on multiple conditions
    # Replace values where (x > 0 and y < 0) with 999
    conditional_array = None
    
    # TODO: Advanced broadcasting example
    # Subtract the mean of each column from all elements
    broadcast_result = None
    
    return rearranged, nearest_neighbors, sparse_result, conditional_array, broadcast_result


def exercise_7_numerical_methods():
    """
    Exercise 7: Numerical Methods
    
    Implement basic numerical methods using NumPy:
    1. Numerical integration using trapezoidal rule
    2. Root finding using bisection method
    3. Numerical differentiation
    4. Interpolation using polynomial fitting
    5. Optimization using gradient descent
    
    Returns:
        tuple: (integral_result, root, derivative, interpolated, optimized_params)
    """
    # TODO: Numerical integration of sin(x) from 0 to pi
    x = np.linspace(0, np.pi, 1000)
    y = np.sin(x)
    integral_result = None  # Should be close to 2.0
    
    # TODO: Find root of x^2 - 2 = 0 using bisection method
    # Implement simple bisection between 0 and 2
    def f(x):
        return x**2 - 2
    
    root = None  # Should be close to sqrt(2)
    
    # TODO: Numerical derivative of sin(x) at x = pi/4
    h = 1e-5
    x_point = np.pi/4
    derivative = None  # Should be close to cos(pi/4)
    
    # TODO: Polynomial interpolation
    # Fit a polynomial to some data points and evaluate at new points
    x_data = np.array([0, 1, 2, 3, 4])
    y_data = np.array([1, 4, 9, 16, 25])  # y = x^2 + 1
    x_new = np.array([0.5, 1.5, 2.5])
    interpolated = None
    
    # TODO: Simple gradient descent for minimizing (x-3)^2
    # Start at x=0, learning rate=0.1, 100 iterations
    def gradient(x):
        return 2 * (x - 3)
    
    optimized_params = None  # Should converge to 3
    
    return integral_result, root, derivative, interpolated, optimized_params


# Test functions
def test_exercise_1():
    """Test structured arrays exercise"""
    students_array, high_performers, avg_age_passed, sorted_by_grade = exercise_1_structured_arrays()
    
    assert students_array is not None, "Students array not created"
    assert len(students_array) == 5, "Should have 5 students"
    assert high_performers is not None, "High performers not found"
    assert avg_age_passed is not None, "Average age not calculated"
    assert sorted_by_grade is not None, "Sorting not performed"
    
    print("✓ Exercise 1 passed: Structured arrays")


def test_exercise_2():
    """Test image processing exercise"""
    original_image, noisy_image, blurred_image, edges, binary_mask = exercise_2_image_processing()
    
    assert original_image is not None and original_image.shape == (100, 100), "Original image incorrect"
    assert noisy_image is not None and noisy_image.shape == (100, 100), "Noisy image incorrect"
    assert blurred_image is not None, "Blurred image not created"
    assert edges is not None, "Edge detection not performed"
    assert binary_mask is not None and binary_mask.dtype == bool, "Binary mask incorrect"
    
    print("✓ Exercise 2 passed: Image processing")


def test_exercise_3():
    """Test time series analysis exercise"""
    time_series, moving_avg, local_maxima, local_minima, outliers = exercise_3_time_series_analysis()
    
    assert time_series is not None and len(time_series) == 200, "Time series incorrect"
    assert moving_avg is not None, "Moving average not calculated"
    assert local_maxima is not None, "Local maxima not found"
    assert local_minima is not None, "Local minima not found"
    assert outliers is not None, "Outliers not detected"
    
    print("✓ Exercise 3 passed: Time series analysis")


def test_exercise_4():
    """Test statistical sampling exercise"""
    normal_samples, uniform_samples, bootstrap_means, clt_means = exercise_4_statistical_sampling()
    
    assert normal_samples is not None and len(normal_samples) == 1000, "Normal samples incorrect"
    assert uniform_samples is not None and len(uniform_samples) == 1000, "Uniform samples incorrect"
    assert bootstrap_means is not None, "Bootstrap means not calculated"
    assert clt_means is not None, "CLT demonstration not performed"
    
    print("✓ Exercise 4 passed: Statistical sampling")


def test_exercise_5():
    """Test matrix operations exercise"""
    cov_matrix, eigenvals, eigenvecs, rank, condition_num, solution, U, s, Vt = exercise_5_matrix_operations()
    
    assert cov_matrix is not None and cov_matrix.shape == (5, 5), "Covariance matrix incorrect"
    assert eigenvals is not None and len(eigenvals) == 5, "Eigenvalues incorrect"
    assert eigenvecs is not None, "Eigenvectors incorrect"
    assert rank is not None, "Matrix rank not calculated"
    assert condition_num is not None, "Condition number not calculated"
    assert solution is not None and len(solution) == 3, "Linear system solution incorrect"
    assert U is not None and s is not None and Vt is not None, "SVD not performed"
    
    print("✓ Exercise 5 passed: Matrix operations")


def test_exercise_6():
    """Test advanced indexing exercise"""
    rearranged, nearest_neighbors, sparse_result, conditional_array, broadcast_result = exercise_6_advanced_indexing()
    
    assert rearranged is not None, "Array rearrangement not performed"
    assert nearest_neighbors is not None, "Nearest neighbors not found"
    assert sparse_result is not None, "Sparse operation not performed"
    assert conditional_array is not None, "Conditional replacement not performed"
    assert broadcast_result is not None, "Broadcasting not performed"
    
    print("✓ Exercise 6 passed: Advanced indexing")


def test_exercise_7():
    """Test numerical methods exercise"""
    integral_result, root, derivative, interpolated, optimized_params = exercise_7_numerical_methods()
    
    assert integral_result is not None, "Numerical integration not performed"
    assert root is not None, "Root finding not performed"
    assert derivative is not None, "Numerical differentiation not performed"
    assert interpolated is not None, "Interpolation not performed"
    assert optimized_params is not None, "Optimization not performed"
    
    print("✓ Exercise 7 passed: Numerical methods")


def run_all_tests():
    """Run all advanced exercise tests"""
    print("Running Advanced NumPy Exercises Tests...\n")
    
    try:
        test_exercise_1()
        test_exercise_2()
        test_exercise_3()
        test_exercise_4()
        test_exercise_5()
        test_exercise_6()
        test_exercise_7()
        
        print("\n🎉 All advanced NumPy exercises completed successfully!")
        print("\nAdvanced concepts mastered:")
        print("- Structured arrays and custom data types")
        print("- Image processing with arrays")
        print("- Time series analysis techniques")
        print("- Statistical sampling and distributions")
        print("- Advanced linear algebra operations")
        print("- Sophisticated indexing and broadcasting")
        print("- Numerical methods implementation")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("Please review your implementation and try again.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your code for syntax errors.")


if __name__ == "__main__":
    run_all_tests()