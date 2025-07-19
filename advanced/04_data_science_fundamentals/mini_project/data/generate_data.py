"""
Synthetic Retail Sales Data Generator

This script generates a realistic retail sales dataset for the Data Analysis Dashboard project.
The dataset includes various features that allow for comprehensive analysis including:
- Time series analysis
- Customer segmentation
- Product performance analysis
- Regional comparisons
- Statistical hypothesis testing
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_retail_sales_data(n_records=10000, start_date='2022-01-01', end_date='2023-12-31'):
    """
    Generate synthetic retail sales data
    
    Parameters:
    -----------
    n_records : int
        Number of sales records to generate
    start_date : str
        Start date for the data range
    end_date : str
        End date for the data range
        
    Returns:
    --------
    pandas.DataFrame
        Generated sales data
    """
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Define data parameters
    product_categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    regions = ['North', 'South', 'East', 'West', 'Central']
    store_types = ['Online', 'Physical']
    genders = ['M', 'F']
    
    # Product names by category
    products = {
        'Electronics': ['Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smart Watch', 
                       'Camera', 'Gaming Console', 'TV', 'Speaker', 'Charger'],
        'Clothing': ['T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes', 
                    'Sweater', 'Shorts', 'Skirt', 'Blouse', 'Pants'],
        'Home': ['Coffee Maker', 'Vacuum', 'Lamp', 'Pillow', 'Blanket',
                'Kitchen Set', 'Mirror', 'Plant', 'Candle', 'Storage Box'],
        'Books': ['Fiction Novel', 'Cookbook', 'Biography', 'Self-Help', 'Textbook',
                 'Children Book', 'Travel Guide', 'History Book', 'Science Book', 'Art Book'],
        'Sports': ['Running Shoes', 'Yoga Mat', 'Dumbbells', 'Tennis Racket', 'Basketball',
                  'Bicycle', 'Swimming Goggles', 'Fitness Tracker', 'Water Bottle', 'Gym Bag']
    }
    
    # Generate date range
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    date_range = pd.date_range(start=start, end=end, freq='D')
    
    # Initialize lists to store data
    data = []
    
    # Generate sales representatives
    sales_reps = [f'REP_{i:03d}' for i in range(1, 51)]  # 50 sales reps
    
    print(f"Generating {n_records} sales records...")
    
    for i in range(n_records):
        if i % 1000 == 0:
            print(f"Generated {i} records...")
        
        # Generate date with seasonal bias
        date = np.random.choice(date_range)
        month = date.month
        
        # Seasonal effects
        seasonal_multiplier = 1.0
        if month in [11, 12]:  # Holiday season
            seasonal_multiplier = 1.5
        elif month in [6, 7, 8]:  # Summer
            seasonal_multiplier = 1.2
        elif month in [1, 2]:  # Post-holiday slump
            seasonal_multiplier = 0.8
        
        # Select product category with some bias
        category_weights = [0.25, 0.20, 0.20, 0.15, 0.20]  # Electronics slightly favored
        category = np.random.choice(product_categories, p=category_weights)
        
        # Select specific product
        product = np.random.choice(products[category])
        
        # Select region
        region = np.random.choice(regions)
        
        # Regional bias for certain products
        if category == 'Sports' and region in ['West', 'South']:
            seasonal_multiplier *= 1.1
        elif category == 'Electronics' and region in ['North', 'East']:
            seasonal_multiplier *= 1.1
        
        # Store type affects product selection
        store_type = np.random.choice(store_types, p=[0.6, 0.4])  # Online slightly favored
        
        # Base price by category
        base_prices = {
            'Electronics': (50, 1500),
            'Clothing': (20, 200),
            'Home': (15, 300),
            'Books': (10, 50),
            'Sports': (25, 400)
        }
        
        min_price, max_price = base_prices[category]
        base_price = np.random.uniform(min_price, max_price)
        
        # Quantity (most sales are 1-3 items)
        quantity = np.random.choice([1, 2, 3, 4, 5], p=[0.5, 0.25, 0.15, 0.07, 0.03])
        
        # Customer demographics
        customer_age = int(np.random.normal(40, 15))
        customer_age = max(18, min(80, customer_age))  # Clamp to reasonable range
        
        customer_gender = np.random.choice(genders)
        
        # Age affects product preferences
        if category == 'Electronics' and customer_age < 35:
            base_price *= 1.1  # Younger customers buy more expensive electronics
        elif category == 'Books' and customer_age > 50:
            quantity = max(1, int(quantity * 1.2))  # Older customers buy more books
        
        # Discount logic
        discount_probability = 0.3  # 30% of sales have discounts
        discount_applied = np.random.random() < discount_probability
        
        if discount_applied:
            # Discount percentage (5% to 30%)
            discount_percentage = np.random.uniform(5, 30)
            
            # Higher discounts for higher-priced items
            if base_price > 500:
                discount_percentage = np.random.uniform(10, 25)
            elif base_price < 50:
                discount_percentage = np.random.uniform(5, 15)
        else:
            discount_percentage = 0
        
        # Calculate final price
        discounted_price = base_price * (1 - discount_percentage / 100)
        sales_amount = discounted_price * quantity * seasonal_multiplier
        
        # Add some random variation
        sales_amount *= np.random.uniform(0.9, 1.1)
        sales_amount = round(sales_amount, 2)
        
        # Select sales rep
        sales_rep = np.random.choice(sales_reps)
        
        # Create record
        record = {
            'Date': date.strftime('%Y-%m-%d'),
            'Product_Category': category,
            'Product_Name': product,
            'Region': region,
            'Sales_Amount': sales_amount,
            'Quantity': quantity,
            'Customer_Age': customer_age,
            'Customer_Gender': customer_gender,
            'Discount_Applied': 'Yes' if discount_applied else 'No',
            'Discount_Percentage': round(discount_percentage, 1),
            'Sales_Rep': sales_rep,
            'Store_Type': store_type
        }
        
        data.append(record)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Sort by date
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    
    # Add derived features
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    df['Year'] = df['Date'].dt.year
    df['Day_of_Week'] = df['Date'].dt.day_name()
    df['Is_Weekend'] = df['Date'].dt.weekday >= 5
    
    # Calculate unit price
    df['Unit_Price'] = df['Sales_Amount'] / df['Quantity']
    
    # Add profit margin (simplified)
    profit_margins = {
        'Electronics': 0.15,
        'Clothing': 0.40,
        'Home': 0.25,
        'Books': 0.20,
        'Sports': 0.30
    }
    df['Profit_Margin'] = df['Product_Category'].map(profit_margins)
    df['Profit_Amount'] = df['Sales_Amount'] * df['Profit_Margin']
    
    print(f"Generated {len(df)} sales records successfully!")
    
    return df


def add_data_quality_issues(df, missing_rate=0.02, outlier_rate=0.01):
    """
    Add realistic data quality issues to the dataset
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Clean dataset
    missing_rate : float
        Proportion of values to make missing
    outlier_rate : float
        Proportion of values to make outliers
        
    Returns:
    --------
    pandas.DataFrame
        Dataset with quality issues
    """
    
    df_dirty = df.copy()
    n_records = len(df_dirty)
    
    # Add missing values
    missing_columns = ['Customer_Age', 'Sales_Rep', 'Discount_Percentage']
    
    for col in missing_columns:
        if col in df_dirty.columns:
            n_missing = int(n_records * missing_rate)
            missing_indices = np.random.choice(df_dirty.index, n_missing, replace=False)
            df_dirty.loc[missing_indices, col] = np.nan
    
    # Add outliers
    outlier_columns = ['Sales_Amount', 'Quantity', 'Customer_Age']
    
    for col in outlier_columns:
        if col in df_dirty.columns:
            n_outliers = int(n_records * outlier_rate)
            outlier_indices = np.random.choice(df_dirty.index, n_outliers, replace=False)
            
            if col == 'Sales_Amount':
                # Make some sales amounts extremely high
                df_dirty.loc[outlier_indices, col] *= np.random.uniform(5, 10, len(outlier_indices))
            elif col == 'Quantity':
                # Make some quantities extremely high
                df_dirty.loc[outlier_indices, col] = np.random.randint(20, 100, len(outlier_indices))
            elif col == 'Customer_Age':
                # Make some ages unrealistic
                df_dirty.loc[outlier_indices, col] = np.random.choice([5, 150], len(outlier_indices))
    
    return df_dirty


def generate_summary_statistics(df):
    """
    Generate summary statistics for the dataset
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Sales dataset
        
    Returns:
    --------
    dict
        Summary statistics
    """
    
    stats = {
        'total_records': len(df),
        'date_range': f"{df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}",
        'total_sales': df['Sales_Amount'].sum(),
        'average_sale': df['Sales_Amount'].mean(),
        'total_quantity': df['Quantity'].sum(),
        'unique_products': df['Product_Name'].nunique(),
        'unique_customers': len(df),  # Assuming each record is a unique customer transaction
        'regions': df['Region'].nunique(),
        'sales_reps': df['Sales_Rep'].nunique(),
        'categories': df['Product_Category'].nunique(),
        'discount_rate': (df['Discount_Applied'] == 'Yes').mean(),
        'online_sales_rate': (df['Store_Type'] == 'Online').mean()
    }
    
    return stats


def main():
    """
    Main function to generate the retail sales dataset
    """
    
    print("Retail Sales Data Generator")
    print("=" * 40)
    
    # Generate clean dataset
    df_clean = generate_retail_sales_data(n_records=10000)
    
    # Add some data quality issues for realistic analysis
    df_with_issues = add_data_quality_issues(df_clean, missing_rate=0.02, outlier_rate=0.01)
    
    # Generate summary statistics
    stats = generate_summary_statistics(df_clean)
    
    # Save datasets
    df_clean.to_csv('retail_sales_clean.csv', index=False)
    df_with_issues.to_csv('retail_sales.csv', index=False)
    
    print("\nDataset Summary:")
    print("-" * 20)
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key.replace('_', ' ').title()}: {value:,.2f}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value:,}")
    
    print(f"\nDatasets saved:")
    print(f"- retail_sales_clean.csv ({len(df_clean)} records)")
    print(f"- retail_sales.csv ({len(df_with_issues)} records with quality issues)")
    
    print("\nSample data:")
    print(df_clean.head())
    
    print("\nData types:")
    print(df_clean.dtypes)
    
    print("\nMissing values in dataset with issues:")
    print(df_with_issues.isnull().sum())


if __name__ == "__main__":
    main()