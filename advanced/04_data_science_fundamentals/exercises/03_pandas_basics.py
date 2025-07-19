"""
Pandas Basics Exercises

This exercise file covers fundamental Pandas operations including:
- DataFrame and Series creation and manipulation
- Data loading and exploration
- Data cleaning and preprocessing
- Grouping and aggregation
- Data merging and joining

Complete each exercise by implementing the required functionality.
Run the tests to verify your solutions.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def exercise_1_dataframe_creation():
    """
    Exercise 1: DataFrame Creation and Basic Operations
    
    Create a DataFrame with student information and perform basic operations:
    1. Create a DataFrame with columns: Name, Age, Grade, Subject, Score
    2. Add 8 student records
    3. Display basic information about the DataFrame
    4. Calculate summary statistics
    
    Returns:
        tuple: (df, info_dict, summary_stats)
    """
    # TODO: Create sample student data
    student_data = {
        # Add student information here
    }
    
    # TODO: Create DataFrame
    df = None
    
    # TODO: Create info dictionary with shape, columns, dtypes
    info_dict = {
        'shape': None,
        'columns': None,
        'dtypes': None
    }
    
    # TODO: Calculate summary statistics for numerical columns
    summary_stats = None
    
    return df, info_dict, summary_stats


def exercise_2_data_selection():
    """
    Exercise 2: Data Selection and Indexing
    
    Perform various data selection operations:
    1. Select specific columns
    2. Filter rows based on conditions
    3. Use boolean indexing
    4. Select data using iloc and loc
    
    Returns:
        tuple: (names_ages, high_scorers, math_students, specific_student)
    """
    # Sample data
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
        'Age': [20, 22, 21, 23, 20, 24],
        'Subject': ['Math', 'Physics', 'Math', 'Chemistry', 'Physics', 'Math'],
        'Score': [85, 78, 92, 88, 76, 95],
        'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney', 'Berlin']
    })
    
    # TODO: Select only Name and Age columns
    names_ages = None
    
    # TODO: Filter students with Score > 85
    high_scorers = None
    
    # TODO: Select students studying Math
    math_students = None
    
    # TODO: Select the student at index 2 using iloc
    specific_student = None
    
    return names_ages, high_scorers, math_students, specific_student


def exercise_3_data_manipulation():
    """
    Exercise 3: Data Manipulation and Transformation
    
    Perform data manipulation operations:
    1. Add new columns
    2. Modify existing columns
    3. Sort data
    4. Drop columns and rows
    
    Returns:
        tuple: (df_with_grade, df_sorted, df_cleaned)
    """
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Score': [85, 78, 92, 88, 76],
        'Age': [20, 22, 21, 23, 20],
        'Bonus': [5, 3, 8, 6, 4]
    })
    
    # TODO: Add a 'Grade' column based on Score
    # A: 90+, B: 80-89, C: 70-79, D: <70
    df_with_grade = df.copy()
    # Add your grade calculation here
    
    # TODO: Add 'Total_Score' column (Score + Bonus)
    # Add your total score calculation here
    
    # TODO: Sort by Total_Score in descending order
    df_sorted = None
    
    # TODO: Drop the 'Bonus' column and any rows where Age < 21
    df_cleaned = None
    
    return df_with_grade, df_sorted, df_cleaned


def exercise_4_missing_data():
    """
    Exercise 4: Handling Missing Data
    
    Work with missing data:
    1. Identify missing values
    2. Fill missing values using different strategies
    3. Drop rows/columns with missing values
    
    Returns:
        tuple: (missing_info, df_filled, df_dropped)
    """
    # Create DataFrame with missing values
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5, np.nan],
        'B': [np.nan, 2, 3, np.nan, 5, 6],
        'C': [1, np.nan, 3, 4, np.nan, 6],
        'D': [1, 2, 3, 4, 5, 6]
    })
    
    # TODO: Create missing info dictionary
    missing_info = {
        'total_missing': None,  # Total missing values in DataFrame
        'missing_per_column': None,  # Missing values per column
        'missing_percentage': None  # Percentage of missing values per column
    }
    
    # TODO: Fill missing values
    # Fill column A with mean, column B with forward fill, column C with 0
    df_filled = df.copy()
    # Add your filling logic here
    
    # TODO: Drop rows with any missing values
    df_dropped = None
    
    return missing_info, df_filled, df_dropped


def exercise_5_grouping_aggregation():
    """
    Exercise 5: Grouping and Aggregation
    
    Perform grouping and aggregation operations:
    1. Group by categorical column
    2. Calculate multiple aggregations
    3. Apply custom functions
    
    Returns:
        tuple: (dept_stats, custom_agg, pivot_table)
    """
    df = pd.DataFrame({
        'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
        'Salary': [70000, 50000, 75000, 60000, 52000, 80000, 65000, 48000],
        'Age': [28, 35, 30, 42, 29, 33, 38, 31],
        'Experience': [3, 8, 5, 15, 4, 7, 12, 6]
    })
    
    # TODO: Calculate department statistics
    # Group by Department and calculate mean, min, max for Salary and Age
    dept_stats = None
    
    # TODO: Custom aggregation
    # For each department, calculate: count of employees, total salary, avg experience
    custom_agg = None
    
    # TODO: Create pivot table
    # Rows: Department, Values: Salary (mean), Age (mean)
    pivot_table = None
    
    return dept_stats, custom_agg, pivot_table


def exercise_6_data_merging():
    """
    Exercise 6: Data Merging and Joining
    
    Merge different DataFrames:
    1. Inner join
    2. Left join
    3. Concatenation
    
    Returns:
        tuple: (inner_merged, left_merged, concatenated)
    """
    # Employee data
    employees = pd.DataFrame({
        'emp_id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'dept_id': [10, 20, 10, 30, 20]
    })
    
    # Department data
    departments = pd.DataFrame({
        'dept_id': [10, 20, 30, 40],
        'dept_name': ['IT', 'HR', 'Finance', 'Marketing'],
        'budget': [100000, 80000, 120000, 90000]
    })
    
    # Salary data
    salaries = pd.DataFrame({
        'emp_id': [1, 2, 3, 4, 5, 6],
        'salary': [70000, 50000, 75000, 60000, 52000, 55000]
    })
    
    # TODO: Inner join employees and departments on dept_id
    inner_merged = None
    
    # TODO: Left join the result with salaries on emp_id
    left_merged = None
    
    # TODO: Concatenate employees and a new DataFrame with additional employees
    new_employees = pd.DataFrame({
        'emp_id': [6, 7],
        'name': ['Frank', 'Grace'],
        'dept_id': [10, 30]
    })
    concatenated = None
    
    return inner_merged, left_merged, concatenated


def exercise_7_time_series():
    """
    Exercise 7: Time Series Operations
    
    Work with time series data:
    1. Create date ranges
    2. Set datetime index
    3. Resample data
    4. Calculate rolling statistics
    
    Returns:
        tuple: (ts_df, monthly_avg, rolling_stats)
    """
    # TODO: Create a time series DataFrame
    # Date range: 100 days starting from '2023-01-01'
    # Random values with trend
    dates = None
    values = None  # Create values with trend + noise
    
    ts_df = pd.DataFrame({
        'date': dates,
        'value': values
    })
    
    # TODO: Set date as index
    # Set the date column as index
    
    # TODO: Resample to monthly frequency and calculate mean
    monthly_avg = None
    
    # TODO: Calculate rolling statistics (7-day window)
    rolling_stats = ts_df.copy()
    # Add rolling mean and rolling std columns
    
    return ts_df, monthly_avg, rolling_stats


def exercise_8_data_cleaning():
    """
    Exercise 8: Data Cleaning Pipeline
    
    Implement a comprehensive data cleaning pipeline:
    1. Handle missing values
    2. Remove duplicates
    3. Fix data types
    4. Standardize text data
    5. Remove outliers
    
    Returns:
        tuple: (original_info, cleaned_df, cleaning_report)
    """
    # Create messy data
    messy_data = pd.DataFrame({
        'Name': ['Alice Johnson', 'bob smith', 'CHARLIE BROWN', 'alice johnson', 'Diana Prince', ''],
        'Age': [25, 30, np.nan, 25, 28, 35],
        'Salary': ['70000', '50000', '75000', '70000', '60000', '1000000'],  # String type, outlier
        'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'alice@email.com', np.nan, 'diana@email.com'],
        'Department': ['IT', 'hr', 'IT', 'IT', 'Finance', 'HR']
    })
    
    # TODO: Collect original data info
    original_info = {
        'shape': None,
        'missing_values': None,
        'duplicates': None,
        'data_types': None
    }
    
    # TODO: Clean the data
    cleaned_df = messy_data.copy()
    
    # 1. Handle missing values (fill or drop as appropriate)
    # 2. Remove duplicates
    # 3. Fix data types (convert Salary to numeric)
    # 4. Standardize text (proper case for names, uppercase for departments)
    # 5. Remove outliers (salary > 100000)
    
    # TODO: Create cleaning report
    cleaning_report = {
        'rows_removed': None,
        'missing_filled': None,
        'duplicates_removed': None,
        'outliers_removed': None
    }
    
    return original_info, cleaned_df, cleaning_report


def exercise_9_advanced_operations():
    """
    Exercise 9: Advanced Pandas Operations
    
    Perform advanced operations:
    1. Apply custom functions
    2. Use transform and apply with groupby
    3. Create categorical data
    4. Perform string operations
    
    Returns:
        tuple: (df_with_categories, transformed_df, string_operations)
    """
    df = pd.DataFrame({
        'Name': ['Alice Johnson', 'Bob Smith Jr.', 'Charlie Brown III', 'Diana Prince-Wayne'],
        'Age': [25, 30, 35, 28],
        'Salary': [70000, 50000, 75000, 60000],
        'Department': ['IT', 'HR', 'IT', 'Finance'],
        'Email': ['alice.johnson@company.com', 'bob.smith@company.com', 
                 'charlie.brown@company.com', 'diana.prince@company.com']
    })
    
    # TODO: Create categorical data and salary bands
    df_with_categories = df.copy()
    # Convert Department to category
    # Create salary bands: Low (<60k), Medium (60k-70k), High (>70k)
    
    # TODO: Transform data using groupby
    transformed_df = df.copy()
    # Add columns for:
    # - Salary rank within department
    # - Salary as percentage of department total
    # - Age difference from department average
    
    # TODO: String operations
    string_operations = df.copy()
    # Extract:
    # - First name from Name
    # - Last name from Name
    # - Username from Email (part before @)
    # - Domain from Email (part after @)
    
    return df_with_categories, transformed_df, string_operations


def exercise_10_performance_optimization():
    """
    Exercise 10: Performance Optimization
    
    Demonstrate performance optimization techniques:
    1. Compare different methods for the same operation
    2. Optimize data types
    3. Use vectorized operations
    
    Returns:
        tuple: (optimized_df, performance_comparison, memory_usage)
    """
    # Create large DataFrame for testing
    np.random.seed(42)
    n_rows = 10000
    
    df = pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
        'Value1': np.random.randn(n_rows),
        'Value2': np.random.randint(1, 100, n_rows),
        'Text': ['Text_' + str(i) for i in range(n_rows)],
        'Date': pd.date_range('2020-01-01', periods=n_rows, freq='H')
    })
    
    # TODO: Optimize data types
    optimized_df = df.copy()
    # Convert Category to category type
    # Convert Value2 to appropriate integer type
    # Any other optimizations you can think of
    
    # TODO: Performance comparison
    # Compare iterrows() vs vectorized operations for a calculation
    import time
    
    def slow_method(df):
        # Using iterrows (slow)
        result = []
        start_time = time.time()
        for idx, row in df.head(1000).iterrows():  # Only first 1000 for speed
            result.append(row['Value1'] * row['Value2'])
        slow_time = time.time() - start_time
        return slow_time
    
    def fast_method(df):
        # Using vectorized operations (fast)
        start_time = time.time()
        result = df.head(1000)['Value1'] * df.head(1000)['Value2']
        fast_time = time.time() - start_time
        return fast_time
    
    slow_time = slow_method(df)
    fast_time = fast_method(df)
    
    performance_comparison = {
        'slow_time': slow_time,
        'fast_time': fast_time,
        'speedup': slow_time / fast_time if fast_time > 0 else 0
    }
    
    # TODO: Memory usage comparison
    memory_usage = {
        'original_memory': None,  # Memory usage of original df
        'optimized_memory': None,  # Memory usage of optimized df
        'memory_saved': None  # Percentage saved
    }
    
    return optimized_df, performance_comparison, memory_usage


# Test functions
def test_exercise_1():
    """Test DataFrame creation exercise"""
    df, info_dict, summary_stats = exercise_1_dataframe_creation()
    
    assert df is not None, "DataFrame not created"
    assert len(df) >= 8, "Should have at least 8 student records"
    assert 'Name' in df.columns, "Should have Name column"
    assert info_dict['shape'] is not None, "Shape not calculated"
    assert summary_stats is not None, "Summary statistics not calculated"
    
    print("✓ Exercise 1 passed: DataFrame creation")


def test_exercise_2():
    """Test data selection exercise"""
    names_ages, high_scorers, math_students, specific_student = exercise_2_data_selection()
    
    assert names_ages is not None and len(names_ages.columns) == 2, "Names and ages selection incorrect"
    assert high_scorers is not None and all(high_scorers['Score'] > 85), "High scorers filter incorrect"
    assert math_students is not None and all(math_students['Subject'] == 'Math'), "Math students filter incorrect"
    assert specific_student is not None, "Specific student selection incorrect"
    
    print("✓ Exercise 2 passed: Data selection")


def test_exercise_3():
    """Test data manipulation exercise"""
    df_with_grade, df_sorted, df_cleaned = exercise_3_data_manipulation()
    
    assert 'Grade' in df_with_grade.columns, "Grade column not added"
    assert 'Total_Score' in df_with_grade.columns, "Total_Score column not added"
    assert df_sorted is not None, "Sorting not performed"
    assert df_cleaned is not None, "Data cleaning not performed"
    
    print("✓ Exercise 3 passed: Data manipulation")


def test_exercise_4():
    """Test missing data exercise"""
    missing_info, df_filled, df_dropped = exercise_4_missing_data()
    
    assert missing_info['total_missing'] is not None, "Missing values not counted"
    assert df_filled is not None, "Missing values not filled"
    assert df_dropped is not None, "Rows not dropped"
    
    print("✓ Exercise 4 passed: Missing data handling")


def test_exercise_5():
    """Test grouping and aggregation exercise"""
    dept_stats, custom_agg, pivot_table = exercise_5_grouping_aggregation()
    
    assert dept_stats is not None, "Department statistics not calculated"
    assert custom_agg is not None, "Custom aggregation not performed"
    assert pivot_table is not None, "Pivot table not created"
    
    print("✓ Exercise 5 passed: Grouping and aggregation")


def test_exercise_6():
    """Test data merging exercise"""
    inner_merged, left_merged, concatenated = exercise_6_data_merging()
    
    assert inner_merged is not None, "Inner merge not performed"
    assert left_merged is not None, "Left merge not performed"
    assert concatenated is not None, "Concatenation not performed"
    
    print("✓ Exercise 6 passed: Data merging")


def test_exercise_7():
    """Test time series exercise"""
    ts_df, monthly_avg, rolling_stats = exercise_7_time_series()
    
    assert ts_df is not None, "Time series DataFrame not created"
    assert monthly_avg is not None, "Monthly average not calculated"
    assert rolling_stats is not None, "Rolling statistics not calculated"
    
    print("✓ Exercise 7 passed: Time series operations")


def test_exercise_8():
    """Test data cleaning exercise"""
    original_info, cleaned_df, cleaning_report = exercise_8_data_cleaning()
    
    assert original_info is not None, "Original info not collected"
    assert cleaned_df is not None, "Data not cleaned"
    assert cleaning_report is not None, "Cleaning report not created"
    
    print("✓ Exercise 8 passed: Data cleaning pipeline")


def test_exercise_9():
    """Test advanced operations exercise"""
    df_with_categories, transformed_df, string_operations = exercise_9_advanced_operations()
    
    assert df_with_categories is not None, "Categories not created"
    assert transformed_df is not None, "Transformations not applied"
    assert string_operations is not None, "String operations not performed"
    
    print("✓ Exercise 9 passed: Advanced operations")


def test_exercise_10():
    """Test performance optimization exercise"""
    optimized_df, performance_comparison, memory_usage = exercise_10_performance_optimization()
    
    assert optimized_df is not None, "DataFrame not optimized"
    assert performance_comparison['speedup'] > 1, "Performance not improved"
    assert memory_usage is not None, "Memory usage not calculated"
    
    print("✓ Exercise 10 passed: Performance optimization")


def run_all_tests():
    """Run all exercise tests"""
    print("Running Pandas Basics Exercises Tests...\n")
    
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
        
        print("\n🎉 All Pandas exercises completed successfully!")
        print("\nKey concepts mastered:")
        print("- DataFrame and Series creation and manipulation")
        print("- Data selection, filtering, and indexing")
        print("- Data cleaning and preprocessing")
        print("- Grouping, aggregation, and pivot tables")
        print("- Data merging and joining")
        print("- Time series operations")
        print("- Advanced data transformations")
        print("- Performance optimization techniques")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("Please review your implementation and try again.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your code for syntax errors.")


if __name__ == "__main__":
    run_all_tests()