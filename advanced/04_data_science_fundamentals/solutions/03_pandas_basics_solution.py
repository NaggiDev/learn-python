"""
Pandas Basics Exercises - Solutions

This file contains complete solutions for all Pandas exercises.
These solutions demonstrate comprehensive Pandas functionality and best practices.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time


def exercise_1_dataframe_creation():
    """
    Exercise 1: DataFrame Creation and Basic Operations - SOLUTION
    """
    # Create sample student data
    student_data = {
        'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 
                'Eve Wilson', 'Frank Miller', 'Grace Lee', 'Henry Davis'],
        'Age': [20, 22, 21, 23, 20, 24, 19, 25],
        'Grade': ['A', 'B', 'A', 'B', 'C', 'A', 'B', 'A'],
        'Subject': ['Math', 'Physics', 'Chemistry', 'Math', 'Physics', 'Chemistry', 'Math', 'Physics'],
        'Score': [92, 78, 85, 88, 76, 91, 83, 89]
    }
    
    # Create DataFrame
    df = pd.DataFrame(student_data)
    
    # Create info dictionary
    info_dict = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict()
    }
    
    # Calculate summary statistics for numerical columns
    summary_stats = df.describe()
    
    return df, info_dict, summary_stats


def exercise_2_data_selection():
    """
    Exercise 2: Data Selection and Indexing - SOLUTION
    """
    # Sample data
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
        'Age': [20, 22, 21, 23, 20, 24],
        'Subject': ['Math', 'Physics', 'Math', 'Chemistry', 'Physics', 'Math'],
        'Score': [85, 78, 92, 88, 76, 95],
        'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney', 'Berlin']
    })
    
    # Select only Name and Age columns
    names_ages = df[['Name', 'Age']]
    
    # Filter students with Score > 85
    high_scorers = df[df['Score'] > 85]
    
    # Select students studying Math
    math_students = df[df['Subject'] == 'Math']
    
    # Select the student at index 2 using iloc
    specific_student = df.iloc[2]
    
    return names_ages, high_scorers, math_students, specific_student


def exercise_3_data_manipulation():
    """
    Exercise 3: Data Manipulation and Transformation - SOLUTION
    """
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Score': [85, 78, 92, 88, 76],
        'Age': [20, 22, 21, 23, 20],
        'Bonus': [5, 3, 8, 6, 4]
    })
    
    # Add a 'Grade' column based on Score
    df_with_grade = df.copy()
    df_with_grade['Grade'] = df_with_grade['Score'].apply(
        lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'D'
    )
    
    # Add 'Total_Score' column
    df_with_grade['Total_Score'] = df_with_grade['Score'] + df_with_grade['Bonus']
    
    # Sort by Total_Score in descending order
    df_sorted = df_with_grade.sort_values('Total_Score', ascending=False)
    
    # Drop the 'Bonus' column and rows where Age < 21
    df_cleaned = df_with_grade.drop('Bonus', axis=1)
    df_cleaned = df_cleaned[df_cleaned['Age'] >= 21]
    
    return df_with_grade, df_sorted, df_cleaned


def exercise_4_missing_data():
    """
    Exercise 4: Handling Missing Data - SOLUTION
    """
    # Create DataFrame with missing values
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5, np.nan],
        'B': [np.nan, 2, 3, np.nan, 5, 6],
        'C': [1, np.nan, 3, 4, np.nan, 6],
        'D': [1, 2, 3, 4, 5, 6]
    })
    
    # Create missing info dictionary
    missing_counts = df.isnull().sum()
    missing_info = {
        'total_missing': df.isnull().sum().sum(),
        'missing_per_column': missing_counts.to_dict(),
        'missing_percentage': (missing_counts / len(df) * 100).to_dict()
    }
    
    # Fill missing values
    df_filled = df.copy()
    df_filled['A'] = df_filled['A'].fillna(df_filled['A'].mean())  # Fill with mean
    df_filled['B'] = df_filled['B'].fillna(method='ffill')  # Forward fill
    df_filled['C'] = df_filled['C'].fillna(0)  # Fill with 0
    
    # Drop rows with any missing values
    df_dropped = df.dropna()
    
    return missing_info, df_filled, df_dropped


def exercise_5_grouping_aggregation():
    """
    Exercise 5: Grouping and Aggregation - SOLUTION
    """
    df = pd.DataFrame({
        'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
        'Salary': [70000, 50000, 75000, 60000, 52000, 80000, 65000, 48000],
        'Age': [28, 35, 30, 42, 29, 33, 38, 31],
        'Experience': [3, 8, 5, 15, 4, 7, 12, 6]
    })
    
    # Calculate department statistics
    dept_stats = df.groupby('Department')[['Salary', 'Age']].agg(['mean', 'min', 'max'])
    
    # Custom aggregation
    custom_agg = df.groupby('Department').agg({
        'Employee': 'count',
        'Salary': 'sum',
        'Experience': 'mean'
    }).rename(columns={'Employee': 'Count', 'Salary': 'Total_Salary', 'Experience': 'Avg_Experience'})
    
    # Create pivot table
    pivot_table = df.pivot_table(
        values=['Salary', 'Age'],
        index='Department',
        aggfunc='mean'
    )
    
    return dept_stats, custom_agg, pivot_table


def exercise_6_data_merging():
    """
    Exercise 6: Data Merging and Joining - SOLUTION
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
    
    # Inner join employees and departments
    inner_merged = pd.merge(employees, departments, on='dept_id', how='inner')
    
    # Left join with salaries
    left_merged = pd.merge(inner_merged, salaries, on='emp_id', how='left')
    
    # Concatenate with new employees
    new_employees = pd.DataFrame({
        'emp_id': [6, 7],
        'name': ['Frank', 'Grace'],
        'dept_id': [10, 30]
    })
    concatenated = pd.concat([employees, new_employees], ignore_index=True)
    
    return inner_merged, left_merged, concatenated


def exercise_7_time_series():
    """
    Exercise 7: Time Series Operations - SOLUTION
    """
    # Create a time series DataFrame
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    np.random.seed(42)
    trend = np.linspace(0, 10, 100)
    noise = np.random.normal(0, 1, 100)
    values = trend + noise
    
    ts_df = pd.DataFrame({
        'date': dates,
        'value': values
    })
    
    # Set date as index
    ts_df.set_index('date', inplace=True)
    
    # Resample to monthly frequency and calculate mean
    monthly_avg = ts_df.resample('M').mean()
    
    # Calculate rolling statistics (7-day window)
    rolling_stats = ts_df.copy()
    rolling_stats['rolling_mean'] = ts_df['value'].rolling(window=7).mean()
    rolling_stats['rolling_std'] = ts_df['value'].rolling(window=7).std()
    
    return ts_df, monthly_avg, rolling_stats


def exercise_8_data_cleaning():
    """
    Exercise 8: Data Cleaning Pipeline - SOLUTION
    """
    # Create messy data
    messy_data = pd.DataFrame({
        'Name': ['Alice Johnson', 'bob smith', 'CHARLIE BROWN', 'alice johnson', 'Diana Prince', ''],
        'Age': [25, 30, np.nan, 25, 28, 35],
        'Salary': ['70000', '50000', '75000', '70000', '60000', '1000000'],
        'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'alice@email.com', np.nan, 'diana@email.com'],
        'Department': ['IT', 'hr', 'IT', 'IT', 'Finance', 'HR']
    })
    
    # Collect original data info
    original_info = {
        'shape': messy_data.shape,
        'missing_values': messy_data.isnull().sum().sum(),
        'duplicates': messy_data.duplicated().sum(),
        'data_types': messy_data.dtypes.to_dict()
    }
    
    # Clean the data
    cleaned_df = messy_data.copy()
    
    # 1. Handle missing values
    cleaned_df['Age'] = cleaned_df['Age'].fillna(cleaned_df['Age'].median())
    cleaned_df['Email'] = cleaned_df['Email'].fillna('unknown@email.com')
    cleaned_df = cleaned_df[cleaned_df['Name'] != '']  # Remove empty names
    
    # 2. Remove duplicates
    duplicates_before = len(cleaned_df)
    cleaned_df = cleaned_df.drop_duplicates()
    duplicates_removed = duplicates_before - len(cleaned_df)
    
    # 3. Fix data types
    cleaned_df['Salary'] = pd.to_numeric(cleaned_df['Salary'])
    
    # 4. Standardize text
    cleaned_df['Name'] = cleaned_df['Name'].str.title()
    cleaned_df['Department'] = cleaned_df['Department'].str.upper()
    
    # 5. Remove outliers (salary > 100000)
    outliers_before = len(cleaned_df)
    cleaned_df = cleaned_df[cleaned_df['Salary'] <= 100000]
    outliers_removed = outliers_before - len(cleaned_df)
    
    # Create cleaning report
    cleaning_report = {
        'rows_removed': original_info['shape'][0] - len(cleaned_df),
        'missing_filled': original_info['missing_values'],
        'duplicates_removed': duplicates_removed,
        'outliers_removed': outliers_removed
    }
    
    return original_info, cleaned_df, cleaning_report


def exercise_9_advanced_operations():
    """
    Exercise 9: Advanced Pandas Operations - SOLUTION
    """
    df = pd.DataFrame({
        'Name': ['Alice Johnson', 'Bob Smith Jr.', 'Charlie Brown III', 'Diana Prince-Wayne'],
        'Age': [25, 30, 35, 28],
        'Salary': [70000, 50000, 75000, 60000],
        'Department': ['IT', 'HR', 'IT', 'Finance'],
        'Email': ['alice.johnson@company.com', 'bob.smith@company.com', 
                 'charlie.brown@company.com', 'diana.prince@company.com']
    })
    
    # Create categorical data and salary bands
    df_with_categories = df.copy()
    df_with_categories['Department'] = df_with_categories['Department'].astype('category')
    df_with_categories['Salary_Band'] = pd.cut(
        df_with_categories['Salary'],
        bins=[0, 60000, 70000, float('inf')],
        labels=['Low', 'Medium', 'High']
    )
    
    # Transform data using groupby
    transformed_df = df.copy()
    transformed_df['Salary_Rank'] = df.groupby('Department')['Salary'].rank(ascending=False)
    transformed_df['Salary_Pct_of_Dept'] = (
        df['Salary'] / df.groupby('Department')['Salary'].transform('sum') * 100
    )
    transformed_df['Age_Diff_from_Dept_Avg'] = (
        df['Age'] - df.groupby('Department')['Age'].transform('mean')
    )
    
    # String operations
    string_operations = df.copy()
    string_operations['First_Name'] = df['Name'].str.split().str[0]
    string_operations['Last_Name'] = df['Name'].str.split().str[-1]
    string_operations['Username'] = df['Email'].str.split('@').str[0]
    string_operations['Domain'] = df['Email'].str.split('@').str[1]
    
    return df_with_categories, transformed_df, string_operations


def exercise_10_performance_optimization():
    """
    Exercise 10: Performance Optimization - SOLUTION
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
    
    # Optimize data types
    optimized_df = df.copy()
    optimized_df['Category'] = optimized_df['Category'].astype('category')
    optimized_df['Value2'] = optimized_df['Value2'].astype('int8')  # Values are 1-100, fit in int8
    
    # Performance comparison functions
    def slow_method(df):
        result = []
        start_time = time.time()
        for idx, row in df.head(1000).iterrows():
            result.append(row['Value1'] * row['Value2'])
        slow_time = time.time() - start_time
        return slow_time
    
    def fast_method(df):
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
    
    # Memory usage comparison
    original_memory = df.memory_usage(deep=True).sum()
    optimized_memory = optimized_df.memory_usage(deep=True).sum()
    
    memory_usage = {
        'original_memory': original_memory,
        'optimized_memory': optimized_memory,
        'memory_saved': ((original_memory - optimized_memory) / original_memory * 100)
    }
    
    return optimized_df, performance_comparison, memory_usage


# Demonstration function
def demonstrate_pandas_solutions():
    """
    Demonstrate all Pandas exercise solutions with detailed explanations
    """
    print("Pandas Basics Exercises - Solutions Demonstration")
    print("=" * 60)
    
    # Exercise 1: DataFrame Creation
    print("\n1. DataFrame Creation:")
    df, info_dict, summary_stats = exercise_1_dataframe_creation()
    print(f"Created DataFrame with shape: {info_dict['shape']}")
    print(f"Columns: {info_dict['columns']}")
    print("Sample data:")
    print(df.head(3))
    
    # Exercise 2: Data Selection
    print("\n2. Data Selection:")
    names_ages, high_scorers, math_students, specific_student = exercise_2_data_selection()
    print(f"Names and ages shape: {names_ages.shape}")
    print(f"High scorers count: {len(high_scorers)}")
    print(f"Math students count: {len(math_students)}")
    print(f"Specific student: {specific_student['Name']}")
    
    # Exercise 3: Data Manipulation
    print("\n3. Data Manipulation:")
    df_with_grade, df_sorted, df_cleaned = exercise_3_data_manipulation()
    print(f"Added columns: {[col for col in df_with_grade.columns if col not in ['Name', 'Score', 'Age', 'Bonus']]}")
    print(f"Sorted DataFrame shape: {df_sorted.shape}")
    print(f"Cleaned DataFrame shape: {df_cleaned.shape}")
    
    # Exercise 4: Missing Data
    print("\n4. Missing Data Handling:")
    missing_info, df_filled, df_dropped = exercise_4_missing_data()
    print(f"Total missing values: {missing_info['total_missing']}")
    print(f"Filled DataFrame shape: {df_filled.shape}")
    print(f"Dropped DataFrame shape: {df_dropped.shape}")
    
    # Exercise 5: Grouping and Aggregation
    print("\n5. Grouping and Aggregation:")
    dept_stats, custom_agg, pivot_table = exercise_5_grouping_aggregation()
    print(f"Department statistics shape: {dept_stats.shape}")
    print(f"Custom aggregation shape: {custom_agg.shape}")
    print(f"Pivot table shape: {pivot_table.shape}")
    
    # Exercise 6: Data Merging
    print("\n6. Data Merging:")
    inner_merged, left_merged, concatenated = exercise_6_data_merging()
    print(f"Inner merged shape: {inner_merged.shape}")
    print(f"Left merged shape: {left_merged.shape}")
    print(f"Concatenated shape: {concatenated.shape}")
    
    # Exercise 7: Time Series
    print("\n7. Time Series Operations:")
    ts_df, monthly_avg, rolling_stats = exercise_7_time_series()
    print(f"Time series shape: {ts_df.shape}")
    print(f"Monthly averages: {len(monthly_avg)} months")
    print(f"Rolling stats columns: {rolling_stats.columns.tolist()}")
    
    # Exercise 8: Data Cleaning
    print("\n8. Data Cleaning Pipeline:")
    original_info, cleaned_df, cleaning_report = exercise_8_data_cleaning()
    print(f"Original shape: {original_info['shape']}")
    print(f"Cleaned shape: {cleaned_df.shape}")
    print(f"Rows removed: {cleaning_report['rows_removed']}")
    print(f"Outliers removed: {cleaning_report['outliers_removed']}")
    
    # Exercise 9: Advanced Operations
    print("\n9. Advanced Operations:")
    df_with_categories, transformed_df, string_operations = exercise_9_advanced_operations()
    print(f"Categories created: {df_with_categories.select_dtypes(include=['category']).columns.tolist()}")
    print(f"Transform columns added: {[col for col in transformed_df.columns if 'Rank' in col or 'Pct' in col or 'Diff' in col]}")
    print(f"String operations: {[col for col in string_operations.columns if col in ['First_Name', 'Last_Name', 'Username', 'Domain']]}")
    
    # Exercise 10: Performance Optimization
    print("\n10. Performance Optimization:")
    optimized_df, performance_comparison, memory_usage = exercise_10_performance_optimization()
    print(f"Speedup achieved: {performance_comparison['speedup']:.1f}x")
    print(f"Memory saved: {memory_usage['memory_saved']:.1f}%")
    print(f"Original memory: {memory_usage['original_memory'] / 1024**2:.2f} MB")
    print(f"Optimized memory: {memory_usage['optimized_memory'] / 1024**2:.2f} MB")
    
    print("\n" + "=" * 60)
    print("All Pandas solutions demonstrated successfully!")
    print("\nKey techniques showcased:")
    print("- Comprehensive DataFrame operations")
    print("- Advanced data selection and filtering")
    print("- Robust data cleaning pipelines")
    print("- Sophisticated grouping and aggregation")
    print("- Complex data merging and joining")
    print("- Time series analysis and resampling")
    print("- String operations and categorical data")
    print("- Performance optimization strategies")


if __name__ == "__main__":
    demonstrate_pandas_solutions()