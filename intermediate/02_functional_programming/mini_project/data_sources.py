"""
Data Sources Module

This module contains generators that simulate different data sources for the pipeline.
Implement the functions below to create realistic data generators.
"""

import random
import datetime
from typing import Generator, Dict, Any

# TODO: Implement the data generators below

def sales_data_generator(source_id: str, num_records: int) -> Generator[Dict[str, Any], None, None]:
    """
    Generate sales records from a specific source.
    
    Args:
        source_id: Identifier for the data source (e.g., 'online', 'store_1', 'mobile')
        num_records: Number of records to generate
        
    Yields:
        Dict containing sales record with keys:
        - transaction_id: Unique transaction identifier
        - customer_id: Customer identifier
        - product_id: Product identifier
        - quantity: Number of items purchased
        - unit_price: Price per unit
        - timestamp: Transaction timestamp
        - source: Source identifier
    """
    # TODO: Implement this generator
    # Hint: Use random data generation and yield one record at a time
    pass

def product_catalog_generator() -> Generator[Dict[str, Any], None, None]:
    """
    Generate product catalog information.
    
    Yields:
        Dict containing product information with keys:
        - product_id: Unique product identifier
        - name: Product name
        - category: Product category
        - cost: Product cost
        - margin: Profit margin percentage
    """
    # TODO: Implement this generator
    # Create a realistic product catalog
    pass

def customer_data_generator(num_customers: int = 1000) -> Generator[Dict[str, Any], None, None]:
    """
    Generate customer information.
    
    Args:
        num_customers: Number of customers to generate
        
    Yields:
        Dict containing customer information with keys:
        - customer_id: Unique customer identifier
        - name: Customer name
        - email: Customer email
        - registration_date: Date customer registered
        - tier: Customer tier (bronze, silver, gold, platinum)
    """
    # TODO: Implement this generator
    pass

def corrupted_data_generator(source_id: str, num_records: int, corruption_rate: float = 0.1) -> Generator[Dict[str, Any], None, None]:
    """
    Generate sales data with some corrupted/invalid records for testing data cleaning.
    
    Args:
        source_id: Identifier for the data source
        num_records: Number of records to generate
        corruption_rate: Percentage of records that should be corrupted (0.0 to 1.0)
        
    Yields:
        Dict containing sales record (some may have invalid/missing data)
    """
    # TODO: Implement this generator
    # Include some records with missing fields, invalid data types, etc.
    pass

def batch_data_generator(data_generator: Generator, batch_size: int) -> Generator[list, None, None]:
    """
    Convert a single-record generator into a batch generator.
    
    Args:
        data_generator: Generator that yields individual records
        batch_size: Number of records per batch
        
    Yields:
        List of records (batch)
    """
    # TODO: Implement this generator
    # Collect records into batches and yield each batch
    pass

# Sample data for realistic generation
SAMPLE_PRODUCTS = [
    "Wireless Headphones", "Running Shoes", "Coffee Maker", "Laptop Stand",
    "Bluetooth Speaker", "Yoga Mat", "Water Bottle", "Desk Lamp",
    "Phone Case", "Backpack", "Tablet", "Gaming Mouse"
]

SAMPLE_CATEGORIES = [
    "Electronics", "Sports", "Home & Kitchen", "Accessories", "Health & Fitness"
]

SAMPLE_CUSTOMER_NAMES = [
    "Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince",
    "Edward Norton", "Fiona Apple", "George Lucas", "Helen Troy"
]

SAMPLE_SOURCES = ["online", "store_1", "store_2", "mobile", "phone"]

# Helper functions (you can use these in your implementations)
def generate_transaction_id() -> str:
    """Generate a unique transaction ID."""
    return f"TXN{random.randint(100000, 999999)}"

def generate_customer_id() -> str:
    """Generate a customer ID."""
    return f"CUST{random.randint(1000, 9999)}"

def generate_product_id() -> str:
    """Generate a product ID."""
    return f"PROD{random.randint(100, 999)}"

def random_timestamp(days_back: int = 30) -> datetime.datetime:
    """Generate a random timestamp within the last N days."""
    now = datetime.datetime.now()
    random_days = random.randint(0, days_back)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    return now - datetime.timedelta(days=random_days, hours=random_hours, minutes=random_minutes)

def random_price(min_price: float = 5.0, max_price: float = 500.0) -> float:
    """Generate a random price."""
    return round(random.uniform(min_price, max_price), 2)

# Test function to verify your implementations
def test_generators():
    """Test all generators to ensure they work correctly."""
    print("Testing data generators...")
    
    # Test sales data generator
    print("\n1. Testing sales_data_generator:")
    try:
        sales_gen = sales_data_generator("test_source", 3)
        for i, record in enumerate(sales_gen):
            print(f"   Record {i+1}: {record}")
        print("   ✅ Sales data generator works!")
    except Exception as e:
        print(f"   ❌ Sales data generator error: {e}")
    
    # Test product catalog generator
    print("\n2. Testing product_catalog_generator:")
    try:
        product_gen = product_catalog_generator()
        for i, product in enumerate(product_gen):
            if i >= 3:  # Only show first 3
                break
            print(f"   Product {i+1}: {product}")
        print("   ✅ Product catalog generator works!")
    except Exception as e:
        print(f"   ❌ Product catalog generator error: {e}")
    
    # Test customer data generator
    print("\n3. Testing customer_data_generator:")
    try:
        customer_gen = customer_data_generator(3)
        for i, customer in enumerate(customer_gen):
            print(f"   Customer {i+1}: {customer}")
        print("   ✅ Customer data generator works!")
    except Exception as e:
        print(f"   ❌ Customer data generator error: {e}")
    
    # Test batch generator
    print("\n4. Testing batch_data_generator:")
    try:
        sales_gen = sales_data_generator("batch_test", 7)
        batch_gen = batch_data_generator(sales_gen, 3)
        for i, batch in enumerate(batch_gen):
            print(f"   Batch {i+1} size: {len(batch)}")
        print("   ✅ Batch data generator works!")
    except Exception as e:
        print(f"   ❌ Batch data generator error: {e}")

if __name__ == "__main__":
    test_generators()