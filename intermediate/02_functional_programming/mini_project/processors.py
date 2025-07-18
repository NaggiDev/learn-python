"""
Data Processors Module

This module contains data processing functions using functional programming concepts.
Implement the functions below using map, filter, reduce, and other functional techniques.
"""

from functools import reduce
from typing import Dict, Any, List, Generator, Tuple
from collections import defaultdict
import statistics

# TODO: Implement the data processing functions below

def clean_sales_data(raw_data: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
    """
    Clean and validate sales data using functional programming techniques.
    
    Args:
        raw_data: Generator of raw sales records
        
    Yields:
        Cleaned and validated sales records
        
    Cleaning rules:
    - Remove records with missing required fields
    - Convert data types appropriately
    - Remove records with invalid values (negative quantities, zero prices, etc.)
    - Standardize field formats
    """
    # TODO: Implement this function using filter and map
    # Hint: Use filter to remove invalid records, map to transform valid ones
    pass

def calculate_revenue_by_product(sales_data: Generator[Dict[str, Any], None, None]) -> Dict[str, float]:
    """
    Calculate total revenue by product using reduce.
    
    Args:
        sales_data: Generator of sales records
        
    Returns:
        Dictionary mapping product_id to total revenue
    """
    # TODO: Implement this function using reduce
    # Hint: Reduce the sales data into a dictionary of product revenues
    pass

def find_top_customers(sales_data: Generator[Dict[str, Any], None, None], n: int = 10) -> List[Tuple[str, float]]:
    """
    Find top N customers by total purchase amount.
    
    Args:
        sales_data: Generator of sales records
        n: Number of top customers to return
        
    Returns:
        List of tuples (customer_id, total_amount) sorted by amount descending
    """
    # TODO: Implement this function using functional programming
    # Hint: Use reduce to aggregate by customer, then sort
    pass

def filter_by_date_range(sales_data: Generator[Dict[str, Any], None, None], 
                        start_date: str, end_date: str) -> Generator[Dict[str, Any], None, None]:
    """
    Filter sales data by date range.
    
    Args:
        sales_data: Generator of sales records
        start_date: Start date in 'YYYY-MM-DD' format
        end_date: End date in 'YYYY-MM-DD' format
        
    Yields:
        Sales records within the date range
    """
    # TODO: Implement this function using filter
    # Hint: Parse dates and compare timestamps
    pass

def calculate_daily_statistics(sales_data: Generator[Dict[str, Any], None, None]) -> Dict[str, Dict[str, float]]:
    """
    Calculate daily sales statistics.
    
    Args:
        sales_data: Generator of sales records
        
    Returns:
        Dictionary mapping date to statistics (total_revenue, avg_order_value, num_transactions)
    """
    # TODO: Implement this function using functional programming
    # Hint: Group by date, then calculate statistics for each group
    pass

def transform_for_analysis(sales_data: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
    """
    Transform sales data for analysis by adding calculated fields.
    
    Args:
        sales_data: Generator of sales records
        
    Yields:
        Enhanced sales records with additional calculated fields:
        - total_amount: quantity * unit_price
        - profit_margin: calculated based on product cost
        - day_of_week: extracted from timestamp
        - hour_of_day: extracted from timestamp
    """
    # TODO: Implement this function using map
    # Hint: Use map to add calculated fields to each record
    pass

def detect_anomalies(sales_data: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
    """
    Detect anomalous sales records using statistical methods.
    
    Args:
        sales_data: Generator of sales records
        
    Yields:
        Records that appear to be anomalous (unusual quantities, prices, etc.)
    """
    # TODO: Implement this function using functional programming
    # Hint: Calculate statistics first, then filter based on thresholds
    pass

def aggregate_by_category(sales_data: Generator[Dict[str, Any], None, None], 
                         product_catalog: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, float]]:
    """
    Aggregate sales data by product category.
    
    Args:
        sales_data: Generator of sales records
        product_catalog: Dictionary mapping product_id to product info
        
    Returns:
        Dictionary mapping category to aggregated metrics
    """
    # TODO: Implement this function using functional programming
    # Hint: Join sales data with product catalog, then aggregate by category
    pass

def create_sales_summary(sales_data: Generator[Dict[str, Any], None, None]) -> Dict[str, Any]:
    """
    Create a comprehensive sales summary using multiple functional operations.
    
    Args:
        sales_data: Generator of sales records
        
    Returns:
        Dictionary containing various summary statistics
    """
    # TODO: Implement this function combining multiple functional operations
    # Include: total revenue, number of transactions, average order value,
    # top products, top customers, sales by source, etc.
    pass

def pipeline_processor(data_generators: List[Generator], 
                      processing_functions: List[callable]) -> Generator[Any, None, None]:
    """
    Create a processing pipeline that chains multiple generators and processors.
    
    Args:
        data_generators: List of data generator functions
        processing_functions: List of processing functions to apply
        
    Yields:
        Processed data from the pipeline
    """
    # TODO: Implement this function to chain generators and processors
    # Hint: Use functional composition to create a pipeline
    pass

# Utility functions for data processing
def is_valid_record(record: Dict[str, Any]) -> bool:
    """
    Check if a sales record is valid.
    
    Args:
        record: Sales record to validate
        
    Returns:
        True if record is valid, False otherwise
    """
    required_fields = ['transaction_id', 'customer_id', 'product_id', 'quantity', 'unit_price']
    
    # Check required fields
    if not all(field in record for field in required_fields):
        return False
    
    # Check data types and values
    try:
        quantity = float(record['quantity'])
        unit_price = float(record['unit_price'])
        
        if quantity <= 0 or unit_price <= 0:
            return False
            
        return True
    except (ValueError, TypeError):
        return False

def parse_timestamp(timestamp_str: str) -> Dict[str, Any]:
    """
    Parse timestamp string and extract date components.
    
    Args:
        timestamp_str: Timestamp string
        
    Returns:
        Dictionary with parsed date components
    """
    from datetime import datetime
    
    try:
        dt = datetime.fromisoformat(timestamp_str.replace(' ', 'T'))
        return {
            'date': dt.date().isoformat(),
            'day_of_week': dt.strftime('%A'),
            'hour_of_day': dt.hour,
            'month': dt.month,
            'year': dt.year
        }
    except:
        return {}

def calculate_total_amount(record: Dict[str, Any]) -> float:
    """
    Calculate total amount for a sales record.
    
    Args:
        record: Sales record
        
    Returns:
        Total amount (quantity * unit_price)
    """
    try:
        return float(record['quantity']) * float(record['unit_price'])
    except (ValueError, TypeError, KeyError):
        return 0.0

# Test function to verify implementations
def test_processors():
    """Test all processor functions to ensure they work correctly."""
    print("Testing data processors...")
    
    # Sample test data
    sample_sales = [
        {
            'transaction_id': 'TXN001',
            'customer_id': 'CUST123',
            'product_id': 'PROD456',
            'quantity': 2,
            'unit_price': 29.99,
            'timestamp': '2024-01-15 10:30:00',
            'source': 'online'
        },
        {
            'transaction_id': 'TXN002',
            'customer_id': 'CUST456',
            'product_id': 'PROD789',
            'quantity': 1,
            'unit_price': 149.99,
            'timestamp': '2024-01-15 11:45:00',
            'source': 'store'
        },
        {
            'transaction_id': 'TXN003',
            'customer_id': 'CUST123',
            'product_id': 'PROD456',
            'quantity': -1,  # Invalid quantity
            'unit_price': 29.99,
            'timestamp': '2024-01-15 12:00:00',
            'source': 'online'
        }
    ]
    
    def sample_data_generator():
        for record in sample_sales:
            yield record
    
    # Test data cleaning
    print("\n1. Testing clean_sales_data:")
    try:
        cleaned_data = list(clean_sales_data(sample_data_generator()))
        print(f"   Original records: {len(sample_sales)}")
        print(f"   Cleaned records: {len(cleaned_data)}")
        print("   ✅ Data cleaning works!")
    except Exception as e:
        print(f"   ❌ Data cleaning error: {e}")
    
    # Test revenue calculation
    print("\n2. Testing calculate_revenue_by_product:")
    try:
        revenue_by_product = calculate_revenue_by_product(sample_data_generator())
        print(f"   Revenue by product: {revenue_by_product}")
        print("   ✅ Revenue calculation works!")
    except Exception as e:
        print(f"   ❌ Revenue calculation error: {e}")
    
    # Test utility functions
    print("\n3. Testing utility functions:")
    try:
        valid_record = sample_sales[0]
        invalid_record = sample_sales[2]
        
        print(f"   Valid record check: {is_valid_record(valid_record)}")
        print(f"   Invalid record check: {is_valid_record(invalid_record)}")
        
        timestamp_info = parse_timestamp(valid_record['timestamp'])
        print(f"   Parsed timestamp: {timestamp_info}")
        
        total = calculate_total_amount(valid_record)
        print(f"   Total amount: {total}")
        
        print("   ✅ Utility functions work!")
    except Exception as e:
        print(f"   ❌ Utility functions error: {e}")

if __name__ == "__main__":
    test_processors()