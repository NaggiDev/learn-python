# Pandas Fundamentals: DataFrame Operations and Data Manipulation

## Introduction

Pandas is the cornerstone library for data manipulation and analysis in Python. Built on top of NumPy, it provides high-level data structures and tools for working with structured data. The name "pandas" is derived from "panel data," reflecting its origins in econometrics, but it has become the standard tool for data analysis across all domains.

## Why Pandas?

### Powerful Data Structures
- **DataFrame**: 2D labeled data structure (like a spreadsheet or SQL table)
- **Series**: 1D labeled array (like a column in a spreadsheet)
- **Index**: Provides meaningful labels for data access

### Data Integration
- Read from and write to various formats (CSV, Excel, JSON, SQL, etc.)
- Handle missing data gracefully
- Merge and join datasets from different sources

### Data Manipulation
- Filter, group, and aggregate data efficiently
- Reshape and pivot data
- Apply complex transformations

### Performance
- Optimized operations built on NumPy
- Vectorized operations for speed
- Memory-efficient data handling

## Core Data Structures

### 1. Series

A Series is a one-dimensional labeled array that can hold any data type:

```python
import pandas as pd
import numpy as np

# Creating Series
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s3 = pd.Series({'a': 1, 'b': 2, 'c': 3})

print("Basic Series:")
print(s1)
print("\nSeries with custom index:")
print(s2)
print("\nSeries from dictionary:")
print(s3)

# Series attributes
print(f"\nValues: {s2.values}")
print(f"Index: {s2.index}")
print(f"Data type: {s2.dtype}")
print(f"Shape: {s2.shape}")
```

### 2. DataFrame

A DataFrame is a 2D labeled data structure with columns of potentially different types:

```python
# Creating DataFrames
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Tokyo', 'Paris'],
    'Salary': [70000, 80000, 90000, 75000]
}

df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)

# DataFrame from lists
df2 = pd.DataFrame([
    ['Alice', 25, 'New York', 70000],
    ['Bob', 30, 'London', 80000],
    ['Charlie', 35, 'Tokyo', 90000],
    ['Diana', 28, 'Paris', 75000]
], columns=['Name', 'Age', 'City', 'Salary'])

print("\nDataFrame from lists:")
print(df2)

# DataFrame attributes
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Index: {df.index.tolist()}")
print(f"Data types:\n{df.dtypes}")
```

## Data Input/Output

Pandas can read from and write to numerous file formats:

```python
# Reading data
df_csv = pd.read_csv('data.csv')
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df_json = pd.read_json('data.json')

# Writing data
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', sheet_name='Data', index=False)
df.to_json('output.json', orient='records')

# Reading with options
df_custom = pd.read_csv('data.csv', 
                       sep=';',           # Custom separator
                       header=0,          # Header row
                       names=['A', 'B'],  # Custom column names
                       skiprows=1,        # Skip rows
                       nrows=100,         # Limit rows
                       dtype={'A': str},  # Specify data types
                       parse_dates=['date_col'])  # Parse dates
```

## Data Exploration

### Basic Information

```python
# Dataset overview
print("Dataset Info:")
print(df.info())

print("\nDataset Description:")
print(df.describe())

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nRandom sample:")
print(df.sample(3))

# Shape and size
print(f"\nShape: {df.shape}")
print(f"Size: {df.size}")
print(f"Memory usage:\n{df.memory_usage()}")
```

### Data Types and Missing Values

```python
# Check data types
print("Data types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

print("\nMissing values percentage:")
print((df.isnull().sum() / len(df)) * 100)

# Check for duplicates
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Unique values
print("\nUnique values per column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()}")
```

## Data Selection and Indexing

### Column Selection

```python
# Single column (returns Series)
ages = df['Age']
print("Ages Series:")
print(ages)

# Multiple columns (returns DataFrame)
subset = df[['Name', 'Age']]
print("\nName and Age:")
print(subset)

# Column access using dot notation
names = df.Name  # Only works if column name is valid Python identifier
```

### Row Selection

```python
# Select by index position
first_row = df.iloc[0]  # First row
first_three = df.iloc[0:3]  # First three rows
last_row = df.iloc[-1]  # Last row

print("First row:")
print(first_row)

# Select by index label
df_indexed = df.set_index('Name')
alice_data = df_indexed.loc['Alice']
print("\nAlice's data:")
print(alice_data)

# Select multiple rows by label
subset_people = df_indexed.loc[['Alice', 'Charlie']]
print("\nAlice and Charlie:")
print(subset_people)
```

### Boolean Indexing

```python
# Filter rows based on conditions
high_earners = df[df['Salary'] > 75000]
print("High earners:")
print(high_earners)

# Multiple conditions
young_high_earners = df[(df['Age'] < 30) & (df['Salary'] > 70000)]
print("\nYoung high earners:")
print(young_high_earners)

# Using isin() for multiple values
european_cities = df[df['City'].isin(['London', 'Paris'])]
print("\nEuropean employees:")
print(european_cities)

# String operations
ny_employees = df[df['City'].str.contains('New')]
print("\nEmployees in cities containing 'New':")
print(ny_employees)
```

## Data Manipulation

### Adding and Modifying Columns

```python
# Add new column
df['Bonus'] = df['Salary'] * 0.1
df['Total_Compensation'] = df['Salary'] + df['Bonus']

# Conditional column creation
df['Seniority'] = df['Age'].apply(lambda x: 'Senior' if x >= 30 else 'Junior')

# Using np.where for conditional logic
df['Location_Type'] = np.where(df['City'].isin(['New York', 'London']), 
                              'Major City', 'Other')

print("DataFrame with new columns:")
print(df)

# Modify existing column
df['Age'] = df['Age'] + 1  # Everyone gets a year older
df['City'] = df['City'].str.upper()  # Convert to uppercase
```

### Dropping Data

```python
# Drop columns
df_no_bonus = df.drop(['Bonus'], axis=1)
df_minimal = df.drop(['Bonus', 'Total_Compensation'], axis=1)

# Drop rows
df_no_first = df.drop(0, axis=0)  # Drop first row
df_filtered = df.drop(df[df['Age'] < 25].index)  # Drop rows where Age < 25

# Drop duplicates
df_unique = df.drop_duplicates()
df_unique_names = df.drop_duplicates(subset=['Name'])
```

### Sorting

```python
# Sort by single column
df_sorted_age = df.sort_values('Age')
df_sorted_age_desc = df.sort_values('Age', ascending=False)

# Sort by multiple columns
df_sorted_multi = df.sort_values(['City', 'Age'])

# Sort by index
df_sorted_index = df.sort_index()

print("Sorted by age (ascending):")
print(df_sorted_age)
```

## Data Cleaning

### Handling Missing Values

```python
# Create DataFrame with missing values for demonstration
data_with_na = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
}
df_na = pd.DataFrame(data_with_na)

print("DataFrame with missing values:")
print(df_na)

# Check for missing values
print("\nMissing values:")
print(df_na.isnull())

# Drop rows with any missing values
df_dropna_any = df_na.dropna()
print("\nAfter dropping rows with any NA:")
print(df_dropna_any)

# Drop rows with all missing values
df_dropna_all = df_na.dropna(how='all')

# Drop columns with missing values
df_dropna_cols = df_na.dropna(axis=1)

# Fill missing values
df_filled = df_na.fillna(0)  # Fill with 0
df_filled_method = df_na.fillna(method='forward')  # Forward fill
df_filled_mean = df_na.fillna(df_na.mean())  # Fill with column mean

print("\nFilled with column means:")
print(df_filled_mean)
```

### Data Type Conversion

```python
# Convert data types
df['Age'] = df['Age'].astype(str)  # Convert to string
df['Salary'] = df['Salary'].astype(float)  # Convert to float

# Convert to datetime
date_data = pd.DataFrame({
    'date_string': ['2023-01-01', '2023-02-01', '2023-03-01']
})
date_data['date'] = pd.to_datetime(date_data['date_string'])

print("Date conversion:")
print(date_data.dtypes)

# Convert to categorical (saves memory for repeated values)
df['City'] = df['City'].astype('category')
print(f"\nCity column type: {df['City'].dtype}")
```

## Grouping and Aggregation

### Basic Grouping

```python
# Group by single column
city_groups = df.groupby('City')

# Basic aggregations
print("Average salary by city:")
print(city_groups['Salary'].mean())

print("\nCount by city:")
print(city_groups.size())

# Multiple aggregations
print("\nMultiple statistics by city:")
print(city_groups['Salary'].agg(['mean', 'min', 'max', 'std']))
```

### Advanced Grouping

```python
# Group by multiple columns
df['Department'] = ['IT', 'HR', 'IT', 'Finance']
dept_city_groups = df.groupby(['Department', 'City'])

print("Salary by department and city:")
print(dept_city_groups['Salary'].mean())

# Custom aggregation functions
def salary_range(series):
    return series.max() - series.min()

print("\nSalary range by department:")
print(df.groupby('Department')['Salary'].agg(salary_range))

# Apply different functions to different columns
agg_dict = {
    'Age': ['mean', 'min', 'max'],
    'Salary': ['mean', 'sum'],
    'Name': 'count'
}
print("\nCustom aggregations:")
print(df.groupby('Department').agg(agg_dict))
```

### Transform and Apply

```python
# Transform: return same shape as input
df['Salary_Normalized'] = df.groupby('Department')['Salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Apply: can return different shapes
def dept_summary(group):
    return pd.Series({
        'count': len(group),
        'avg_age': group['Age'].mean(),
        'total_salary': group['Salary'].sum()
    })

dept_summaries = df.groupby('Department').apply(dept_summary)
print("Department summaries:")
print(dept_summaries)
```

## Data Reshaping

### Pivot Tables

```python
# Create sample data for pivoting
sales_data = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=12, freq='M'),
    'Product': ['A', 'B'] * 6,
    'Region': ['North', 'South', 'North', 'South'] * 3,
    'Sales': np.random.randint(100, 1000, 12)
})

print("Sales data:")
print(sales_data)

# Create pivot table
pivot = sales_data.pivot_table(
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc='mean'
)

print("\nPivot table:")
print(pivot)

# Pivot with multiple aggregations
pivot_multi = sales_data.pivot_table(
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc=['mean', 'sum', 'count']
)

print("\nMulti-function pivot:")
print(pivot_multi)
```

### Melting (Unpivoting)

```python
# Melt wide format to long format
melted = pd.melt(pivot.reset_index(), 
                id_vars=['Product'],
                value_vars=['North', 'South'],
                var_name='Region',
                value_name='Sales')

print("Melted data:")
print(melted)
```

### Stack and Unstack

```python
# Stack: pivot columns to rows
stacked = pivot.stack()
print("Stacked data:")
print(stacked)

# Unstack: pivot rows to columns
unstacked = stacked.unstack()
print("\nUnstacked data:")
print(unstacked)
```

## Merging and Joining

### Concatenation

```python
# Create sample DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Vertical concatenation (stack rows)
concat_vertical = pd.concat([df1, df2], ignore_index=True)
print("Vertical concatenation:")
print(concat_vertical)

# Horizontal concatenation (side by side)
df3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})
concat_horizontal = pd.concat([df1, df3], axis=1)
print("\nHorizontal concatenation:")
print(concat_horizontal)
```

### Merging

```python
# Create sample DataFrames for merging
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'dept_id': [10, 20, 10, 30]
})

departments = pd.DataFrame({
    'dept_id': [10, 20, 30],
    'dept_name': ['IT', 'HR', 'Finance']
})

# Inner join (default)
inner_merge = pd.merge(employees, departments, on='dept_id')
print("Inner merge:")
print(inner_merge)

# Left join
left_merge = pd.merge(employees, departments, on='dept_id', how='left')
print("\nLeft merge:")
print(left_merge)

# Outer join
outer_merge = pd.merge(employees, departments, on='dept_id', how='outer')
print("\nOuter merge:")
print(outer_merge)

# Merge on different column names
departments_alt = departments.rename(columns={'dept_id': 'id'})
merge_diff_cols = pd.merge(employees, departments_alt, 
                          left_on='dept_id', right_on='id')
```

## Time Series Operations

### DateTime Handling

```python
# Create time series data
dates = pd.date_range('2023-01-01', periods=100, freq='D')
ts_data = pd.DataFrame({
    'date': dates,
    'value': np.random.randn(100).cumsum()
})

# Set date as index
ts_data.set_index('date', inplace=True)

print("Time series data:")
print(ts_data.head())

# Date-based selection
jan_data = ts_data['2023-01']
week1 = ts_data['2023-01-01':'2023-01-07']

print("\nJanuary data shape:", jan_data.shape)
print("First week shape:", week1.shape)
```

### Resampling

```python
# Resample to weekly frequency
weekly = ts_data.resample('W').mean()
print("Weekly resampled data:")
print(weekly.head())

# Resample to monthly with different aggregations
monthly_stats = ts_data.resample('M').agg({
    'value': ['mean', 'min', 'max', 'std']
})
print("\nMonthly statistics:")
print(monthly_stats.head())

# Rolling window operations
ts_data['rolling_mean'] = ts_data['value'].rolling(window=7).mean()
ts_data['rolling_std'] = ts_data['value'].rolling(window=7).std()

print("\nWith rolling statistics:")
print(ts_data.head(10))
```

## Performance Optimization

### Efficient Operations

```python
# Use vectorized operations instead of loops
# Bad: Using loops
def slow_calculation(df):
    result = []
    for idx, row in df.iterrows():
        result.append(row['A'] * row['B'])
    return result

# Good: Using vectorized operations
def fast_calculation(df):
    return df['A'] * df['B']

# Use categorical data for repeated strings
df['City'] = df['City'].astype('category')

# Use appropriate data types
df['Age'] = df['Age'].astype('int8')  # If age is always < 128

# Avoid chained indexing
# Bad: df['A'][df['B'] > 0] = 1
# Good: df.loc[df['B'] > 0, 'A'] = 1
```

### Memory Management

```python
# Check memory usage
print("Memory usage:")
print(df.memory_usage(deep=True))

# Optimize data types
def optimize_dtypes(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            # Try to convert to category if few unique values
            if df[col].nunique() / len(df) < 0.5:
                df[col] = df[col].astype('category')
        elif df[col].dtype == 'int64':
            # Downcast integers
            df[col] = pd.to_numeric(df[col], downcast='integer')
        elif df[col].dtype == 'float64':
            # Downcast floats
            df[col] = pd.to_numeric(df[col], downcast='float')
    return df

# Use chunking for large files
def process_large_file(filename, chunksize=10000):
    results = []
    for chunk in pd.read_csv(filename, chunksize=chunksize):
        # Process each chunk
        processed_chunk = chunk.groupby('category').sum()
        results.append(processed_chunk)
    
    # Combine results
    final_result = pd.concat(results).groupby(level=0).sum()
    return final_result
```

## Best Practices

### Code Organization

```python
# Chain operations for readability
result = (df
          .query('Age > 25')
          .groupby('Department')
          .agg({'Salary': 'mean', 'Age': 'count'})
          .round(2)
          .sort_values('Salary', ascending=False))

# Use method chaining with assign for new columns
df_processed = (df
                .assign(
                    Bonus=lambda x: x['Salary'] * 0.1,
                    Total=lambda x: x['Salary'] + x['Bonus']
                )
                .query('Total > 70000')
                .sort_values('Total', ascending=False))
```

### Error Handling

```python
# Handle missing files gracefully
try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("File not found, creating empty DataFrame")
    df = pd.DataFrame()

# Validate data
def validate_dataframe(df, required_columns):
    missing_cols = set(required_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    return True

# Use copy() when modifying DataFrames to avoid SettingWithCopyWarning
df_copy = df.copy()
df_copy.loc[df_copy['Age'] > 30, 'Category'] = 'Senior'
```

## Common Patterns and Idioms

### Data Cleaning Pipeline

```python
def clean_data(df):
    """Comprehensive data cleaning pipeline"""
    # Make a copy to avoid modifying original
    df_clean = df.copy()
    
    # Handle missing values
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].median())
    
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    df_clean[categorical_cols] = df_clean[categorical_cols].fillna('Unknown')
    
    # Remove duplicates
    df_clean = df_clean.drop_duplicates()
    
    # Standardize text columns
    for col in categorical_cols:
        df_clean[col] = df_clean[col].str.strip().str.title()
    
    # Remove outliers using IQR method
    for col in numeric_cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]
    
    return df_clean
```

### Analysis Template

```python
def analyze_dataset(df, target_column=None):
    """Standard exploratory data analysis"""
    print("Dataset Overview:")
    print(f"Shape: {df.shape}")
    print(f"Memory usage: {df.memory_usage().sum() / 1024**2:.2f} MB")
    
    print("\nData Types:")
    print(df.dtypes.value_counts())
    
    print("\nMissing Values:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("No missing values")
    
    print("\nNumerical Summary:")
    print(df.describe())
    
    if target_column and target_column in df.columns:
        print(f"\nTarget Variable ({target_column}) Analysis:")
        print(df[target_column].value_counts())
        
        # Correlation with target
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        correlations = df[numeric_cols].corr()[target_column].sort_values(ascending=False)
        print(f"\nCorrelations with {target_column}:")
        print(correlations)
```

## Summary

Pandas provides a comprehensive toolkit for data manipulation and analysis:

### Key Strengths
- **Intuitive data structures** (Series and DataFrame)
- **Flexible data I/O** capabilities
- **Powerful data manipulation** operations
- **Efficient grouping and aggregation**
- **Time series functionality**
- **Integration with the Python ecosystem**

### Common Use Cases
- Data cleaning and preprocessing
- Exploratory data analysis
- Data transformation and reshaping
- Time series analysis
- Data aggregation and reporting
- Preparing data for machine learning

### Performance Tips
- Use vectorized operations
- Choose appropriate data types
- Leverage categorical data for strings
- Use method chaining for readability
- Consider chunking for large datasets

Pandas is an essential tool for any data scientist or analyst working with Python. Its combination of power, flexibility, and ease of use makes it the go-to library for data manipulation tasks.

## Next Steps

In the next lesson, we'll explore data visualization with Matplotlib and Seaborn, learning how to create compelling visual representations of the data we've learned to manipulate with Pandas.