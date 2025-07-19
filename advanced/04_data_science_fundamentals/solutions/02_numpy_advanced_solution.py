"""
Advanced NumPy Exercises - Solutions

This file contains complete solutions for advanced NumPy exercises.
These solutions demonstrate sophisticated NumPy techniques and real-world applications.
"""

import numpy as np


def exercise_1_structured_arrays():
    """
    Exercise 1: Structured Arrays - SOLUTION
    """
    # Define the structured array dtype
    dtype = [('name', 'U20'), ('age', 'i4'), ('grade', 'f4'), ('passed', '?')]
    
    # Create sample student data
    students_data = [
        ('Alice Johnson', 20, 92.5, True),
        ('Bob Smith', 19, 78.0, True),
        ('Charlie Brown', 21, 88.5, True),
        ('Diana Prince', 20, 95.0, True),
        ('Eve Wilson', 22, 72.5, False)
    ]
    
    # Create structured array
    students_array = np.array(students_data, dtype=dtype)
    
    # Find students with grade > 85
    high_performers = students_array[students_array['grade'] > 85]
    
    # Calculate average age of passed students
    passed_students = students_array[students_array['passed']]
    avg_age_passed = np.mean(passed_students['age'])
    
    # Sort by grade in descending order
    sorted_indices = np.argsort(students_array['grade'])[::-1]
    sorted_by_grade = students_array[sorted_indices]
    
    return students_array, high_performers, avg_age_passed, sorted_by_grade


def exercise_2_image_processing():
    """
    Exercise 2: Image Processing with NumPy - SOLUTION
    """
    # Create a 100x100 gradient image
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    original_image = (X + Y) / 2  # Diagonal gradient
    
    # Add random noise
    np.random.seed(42)
    noise = np.random.normal(0, 0.1, original_image.shape)
    noisy_image = original_image + noise
    
    # Apply 3x3 averaging filter for blur effect
    blurred_image = np.zeros_like(noisy_image)
    for i in range(1, 99):
        for j in range(1, 99):
            blurred_image[i, j] = np.mean(noisy_image[i-1:i+2, j-1:j+2])
    
    # Detect edges using gradient magnitude
    grad_x = np.gradient(blurred_image, axis=1)
    grad_y = np.gradient(blurred_image, axis=0)
    edges = np.sqrt(grad_x**2 + grad_y**2)
    
    # Create binary mask for pixels above mean value
    threshold = np.mean(blurred_image)
    binary_mask = blurred_image > threshold
    
    return original_image, noisy_image, blurred_image, edges, binary_mask


def exercise_3_time_series_analysis():
    """
    Exercise 3: Time Series Analysis - SOLUTION
    """
    # Generate time points
    t = np.linspace(0, 4*np.pi, 200)
    
    # Create time series with trend + seasonality + noise
    np.random.seed(42)
    trend = 0.1 * t  # Linear trend
    seasonality = 2 * np.sin(t) + 0.5 * np.sin(3*t)  # Multiple seasonal components
    noise = np.random.normal(0, 0.3, len(t))
    time_series = trend + seasonality + noise
    
    # Calculate moving average with window size 10
    window_size = 10
    moving_avg = np.convolve(time_series, np.ones(window_size)/window_size, mode='valid')
    
    # Find local maxima (peaks)
    local_maxima = []
    for i in range(1, len(time_series)-1):
        if time_series[i] > time_series[i-1] and time_series[i] > time_series[i+1]:
            local_maxima.append(i)
    local_maxima = np.array(local_maxima)
    
    # Find local minima (valleys)
    local_minima = []
    for i in range(1, len(time_series)-1):
        if time_series[i] < time_series[i-1] and time_series[i] < time_series[i+1]:
            local_minima.append(i)
    local_minima = np.array(local_minima)
    
    # Detect outliers using z-score > 2
    z_scores = np.abs((time_series - np.mean(time_series)) / np.std(time_series))
    outliers = np.where(z_scores > 2)[0]
    
    return time_series, moving_avg, local_maxima, local_minima, outliers


def exercise_4_statistical_sampling():
    """
    Exercise 4: Statistical Sampling and Distributions - SOLUTION
    """
    np.random.seed(42)
    
    # Generate 1000 samples from normal distribution (mean=50, std=10)
    normal_samples = np.random.normal(50, 10, 1000)
    
    # Generate 1000 samples from uniform distribution (0, 100)
    uniform_samples = np.random.uniform(0, 100, 1000)
    
    # Perform bootstrap sampling on normal_samples
    n_bootstrap = 1000
    sample_size = 30
    bootstrap_means = []
    for _ in range(n_bootstrap):
        bootstrap_sample = np.random.choice(normal_samples, size=sample_size, replace=True)
        bootstrap_means.append(np.mean(bootstrap_sample))
    bootstrap_means = np.array(bootstrap_means)
    
    # Demonstrate Central Limit Theorem
    # Sample from exponential distribution, take means of samples of size 30
    n_experiments = 1000
    sample_size = 30
    clt_means = []
    for _ in range(n_experiments):
        exp_sample = np.random.exponential(scale=2, size=sample_size)
        clt_means.append(np.mean(exp_sample))
    clt_means = np.array(clt_means)
    
    return normal_samples, uniform_samples, bootstrap_means, clt_means


def exercise_5_matrix_operations():
    """
    Exercise 5: Advanced Matrix Operations - SOLUTION
    """
    # Generate sample data matrix
    np.random.seed(42)
    data = np.random.randn(100, 5)
    
    # Calculate covariance matrix
    cov_matrix = np.cov(data.T)
    
    # Perform eigendecomposition of covariance matrix
    eigenvals, eigenvecs = np.linalg.eig(cov_matrix)
    
    # Calculate matrix rank and condition number
    rank = np.linalg.matrix_rank(cov_matrix)
    condition_num = np.linalg.cond(cov_matrix)
    
    # Solve system Ax = b
    A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])
    b = np.array([4, 5, 6])
    solution = np.linalg.solve(A, b)
    
    # Perform SVD on the data matrix
    U, s, Vt = np.linalg.svd(data, full_matrices=False)
    
    return cov_matrix, eigenvals, eigenvecs, rank, condition_num, solution, U, s, Vt


def exercise_6_advanced_indexing():
    """
    Exercise 6: Advanced Indexing and Fancy Operations - SOLUTION
    """
    # Sample data
    np.random.seed(42)
    data = np.random.randn(20, 3)
    
    # Rearrange array using fancy indexing
    # Sort by the sum of each row
    row_sums = np.sum(data, axis=1)
    indices = np.argsort(row_sums)
    rearranged = data[indices]
    
    # Find k=3 nearest neighbors for the first point
    query_point = data[0]
    # Calculate Euclidean distances
    distances = np.sqrt(np.sum((data - query_point)**2, axis=1))
    # Get indices of 3 closest points (excluding the point itself)
    nearest_indices = np.argsort(distances)[1:4]  # Skip index 0 (the point itself)
    nearest_neighbors = data[nearest_indices]
    
    # Create a sparse-like operation
    # Set small values (abs < 0.5) to zero
    sparse_result = np.where(np.abs(data) < 0.5, 0, data)
    
    # Conditional replacement based on multiple conditions
    # Replace values where (x > 0 and y < 0) with 999
    conditional_array = data.copy()
    mask = (data[:, 0] > 0) & (data[:, 1] < 0)
    conditional_array[mask] = 999
    
    # Advanced broadcasting example
    # Subtract the mean of each column from all elements
    column_means = np.mean(data, axis=0)
    broadcast_result = data - column_means
    
    return rearranged, nearest_neighbors, sparse_result, conditional_array, broadcast_result


def exercise_7_numerical_methods():
    """
    Exercise 7: Numerical Methods - SOLUTION
    """
    # Numerical integration of sin(x) from 0 to pi using trapezoidal rule
    x = np.linspace(0, np.pi, 1000)
    y = np.sin(x)
    dx = x[1] - x[0]
    integral_result = np.trapz(y, dx=dx)  # Should be close to 2.0
    
    # Find root of x^2 - 2 = 0 using bisection method
    def f(x):
        return x**2 - 2
    
    # Bisection method implementation
    a, b = 0, 2
    tolerance = 1e-6
    max_iterations = 100
    
    for _ in range(max_iterations):
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    root = c  # Should be close to sqrt(2) ≈ 1.414
    
    # Numerical derivative of sin(x) at x = pi/4
    h = 1e-5
    x_point = np.pi/4
    derivative = (np.sin(x_point + h) - np.sin(x_point - h)) / (2 * h)
    # Should be close to cos(pi/4) ≈ 0.707
    
    # Polynomial interpolation
    x_data = np.array([0, 1, 2, 3, 4])
    y_data = np.array([1, 4, 9, 16, 25])  # y = x^2 + 1
    x_new = np.array([0.5, 1.5, 2.5])
    
    # Fit polynomial (degree 2 should be sufficient)
    coeffs = np.polyfit(x_data, y_data, 2)
    interpolated = np.polyval(coeffs, x_new)
    
    # Simple gradient descent for minimizing (x-3)^2
    def gradient(x):
        return 2 * (x - 3)
    
    x = 0  # Starting point
    learning_rate = 0.1
    n_iterations = 100
    
    for _ in range(n_iterations):
        x = x - learning_rate * gradient(x)
    
    optimized_params = x  # Should converge to 3
    
    return integral_result, root, derivative, interpolated, optimized_params


# Demonstration function
def demonstrate_advanced_solutions():
    """
    Demonstrate all advanced exercise solutions with detailed explanations
    """
    print("Advanced NumPy Exercises - Solutions Demonstration")
    print("=" * 60)
    
    # Exercise 1: Structured Arrays
    print("\n1. Structured Arrays:")
    students_array, high_performers, avg_age_passed, sorted_by_grade = exercise_1_structured_arrays()
    print(f"Total students: {len(students_array)}")
    print(f"High performers (grade > 85): {len(high_performers)}")
    print(f"Average age of passed students: {avg_age_passed:.1f}")
    print(f"Top student: {sorted_by_grade[0]['name']} with grade {sorted_by_grade[0]['grade']}")
    
    # Exercise 2: Image Processing
    print("\n2. Image Processing:")
    original_image, noisy_image, blurred_image, edges, binary_mask = exercise_2_image_processing()
    print(f"Original image range: [{original_image.min():.3f}, {original_image.max():.3f}]")
    print(f"Noise level (std): {np.std(noisy_image - original_image):.3f}")
    print(f"Edge strength (max): {edges.max():.3f}")
    print(f"Binary mask coverage: {np.mean(binary_mask)*100:.1f}%")
    
    # Exercise 3: Time Series Analysis
    print("\n3. Time Series Analysis:")
    time_series, moving_avg, local_maxima, local_minima, outliers = exercise_3_time_series_analysis()
    print(f"Time series length: {len(time_series)}")
    print(f"Local maxima found: {len(local_maxima)}")
    print(f"Local minima found: {len(local_minima)}")
    print(f"Outliers detected: {len(outliers)}")
    print(f"Moving average smoothing: {len(moving_avg)} points")
    
    # Exercise 4: Statistical Sampling
    print("\n4. Statistical Sampling:")
    normal_samples, uniform_samples, bootstrap_means, clt_means = exercise_4_statistical_sampling()
    print(f"Normal samples mean: {np.mean(normal_samples):.2f} (expected: 50)")
    print(f"Uniform samples range: [{uniform_samples.min():.1f}, {uniform_samples.max():.1f}]")
    print(f"Bootstrap means std: {np.std(bootstrap_means):.3f}")
    print(f"CLT means std: {np.std(clt_means):.3f} (should be ~0.365)")
    
    # Exercise 5: Matrix Operations
    print("\n5. Matrix Operations:")
    cov_matrix, eigenvals, eigenvecs, rank, condition_num, solution, U, s, Vt = exercise_5_matrix_operations()
    print(f"Covariance matrix shape: {cov_matrix.shape}")
    print(f"Largest eigenvalue: {eigenvals.max():.3f}")
    print(f"Matrix rank: {rank}")
    print(f"Condition number: {condition_num:.2f}")
    print(f"Linear system solution: {solution}")
    print(f"SVD singular values: {s[:3]}")  # Show first 3
    
    # Exercise 6: Advanced Indexing
    print("\n6. Advanced Indexing:")
    rearranged, nearest_neighbors, sparse_result, conditional_array, broadcast_result = exercise_6_advanced_indexing()
    print(f"Rearranged array shape: {rearranged.shape}")
    print(f"Nearest neighbors shape: {nearest_neighbors.shape}")
    print(f"Sparse result zeros: {np.sum(sparse_result == 0)}")
    print(f"Conditional replacements: {np.sum(conditional_array == 999)}")
    print(f"Broadcast result mean: {np.mean(broadcast_result):.6f} (should be ~0)")
    
    # Exercise 7: Numerical Methods
    print("\n7. Numerical Methods:")
    integral_result, root, derivative, interpolated, optimized_params = exercise_7_numerical_methods()
    print(f"Numerical integration result: {integral_result:.6f} (expected: 2.0)")
    print(f"Root finding result: {root:.6f} (expected: {np.sqrt(2):.6f})")
    print(f"Numerical derivative: {derivative:.6f} (expected: {np.cos(np.pi/4):.6f})")
    print(f"Interpolated values: {interpolated}")
    print(f"Optimization result: {optimized_params:.6f} (expected: 3.0)")
    
    print("\n" + "=" * 60)
    print("All advanced solutions demonstrated successfully!")
    print("\nThese exercises showcase:")
    print("- Complex data structures and custom dtypes")
    print("- Real-world image and signal processing")
    print("- Statistical analysis and sampling techniques")
    print("- Advanced linear algebra and matrix operations")
    print("- Sophisticated indexing and data manipulation")
    print("- Implementation of numerical algorithms")


if __name__ == "__main__":
    demonstrate_advanced_solutions()