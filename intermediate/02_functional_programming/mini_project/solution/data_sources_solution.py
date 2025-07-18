"""
Data Sources Module - Solution

Complete implementation of data generators for the pipeline.
"""

import random
import datetime
from typing import Generator, Dict, Any

def sales_data_generator(source_id: str, num_records: int) -> Generator[Dict[str, Any], None, None]:
    """Generate sales records from a specific source."""
    for i in range(num_records):
        yield {
            'transaction_id': generate_transaction_id(),
            'customer_id': generate_customer_id(),
            'product_id': generate_product_id(),
            'quantity': random.randint(1, 5),
            'unit_price': random_price(),
            'timestamp': random_timestamp().isoformat(),
            'source': source_id
        }

def product_catalog_generator() -> Generator[Dict[str, Any], None, None]:
    """Generate product catalog information."""
    products = [
        ("Wireless Headphones", "Electronics", 20.00, 0.50),
        ("Running Shoes", "Sports", 40.00, 0.75),
        ("Coffee Maker", "Home & Kitchen", 30.00, 0.67),
        ("Laptop Stand", "Electronics", 15.00, 1.00),
        ("Bluetooth Speaker", "Electronics", 25.00, 0.60),
        ("Yoga Mat", "Sports", 12.00, 1.25),
        ("Water Bottle", "Sports", 8.00, 1.50),
        ("Desk Lamp", "Home & Kitchen", 18.00, 0.89),
        ("Phone Case", "Accessories", 5.00, 2.00),
        ("Backpack", "Accessories", 35.00, 0.71),
        ("Tablet", "Electronics", 150.00, 0.33),
        ("Gaming Mouse", "Electronics", 22.00, 0.82)
    ]
    
    for i, (name, category, cost, margin) in enumerate(products):
        yield {
            'product_id': f"PROD{100 + i}",
            'name': name,
            'category': category,
            'cost': cost,
            'margin': margin
        }

def customer_data_generator(num_customers: int = 1000) -> Generator[Dict[str, Any], None, None]:
    """Generate customer information."""
    tiers = ['bronze', 'silver', 'gold', 'platinum']
    
    for i in range(num_customers):
        customer_id = f"CUST{1000 + i}"
        name = random.choice(SAMPLE_CUSTOMER_NAMES)
        email = f"{name.lower().replace(' ', '.')}@email.com"
        reg_date = random_timestamp(days_back=365).date().isoformat()
        tier = random.choice(tiers)
        
        yield {
            'customer_id': customer_id,
            'name': name,
            'email': email,
            'registration_date': reg_date,
            'tier': tier
        }

def corrupted_data_generator(source_id: str, num_records: int, corruption_rate: float = 0.1) -> Generator[Dict[str, Any], None, None]:
    """Generate sales data with some corrupted/invalid records."""
    for i in range(num_records):
        if random.random() < corruption_rate:
            # Generate corrupted record
            corrupted_record = {
                'transaction_id': generate_transaction_id() if random.random() > 0.3 else None,
                'customer_id': generate_customer_id() if random.random() > 0.2 else '',
                'product_id': generate_product_id() if random.random() > 0.2 else None,
                'quantity': random.randint(-2, 5) if random.random() > 0.3 else 'invalid',
                'unit_price': random_price() if random.random() > 0.3 else -10.0,
                'timestamp': random_timestamp().isoformat() if random.random() > 0.2 else 'invalid_date',
                'source': source_id
            }
            yield corrupted_record
        else:
            # Generate valid record
            yield {
                'transaction_id': generate_transaction_id(),
                'customer_id': generate_customer_id(),
                'product_id': generate_product_id(),
                'quantity': random.randint(1, 5),
                'unit_price': random_price(),
                'timestamp': random_timestamp().isoformat(),
                'source': source_id
            }

def batch_data_generator(data_generator: Generator, batch_size: int) -> Generator[list, None, None]:
    """Convert a single-record generator into a batch generator."""
    batch = []
    for record in data_generator:
        batch.append(record)
        if len(batch) == batch_size:
            yield batch
            batch = []
    
    # Yield remaining records if any
    if batch:
        yield batch

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
    "Edward Norton", "Fiona Apple", "George Lucas", "Helen Troy",
    "Ivan Petrov", "Julia Roberts", "Kevin Hart", "Lisa Simpson"
]

SAMPLE_SOURCES = ["online", "store_1", "store_2", "mobile", "phone"]

# Helper functions
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

def test_generators():
    """Test all generators to ensure they work correctly."""
    print("Testing data generators...")
    
    # Test sales data generator
    print("\n1. Testing sales_data_generator:")
    sales_gen = sales_data_generator("test_source", 3)
    for i, record in enumerate(sales_gen):
        print(f"   Record {i+1}: {record}")
    print("   ✅ Sales data generator works!")
    
    # Test product catalog generator
    print("\n2. Testing product_catalog_generator:")
    product_gen = product_catalog_generator()
    for i, product in enumerate(product_gen):
        if i >= 3:  # Only show first 3
            break
        print(f"   Product {i+1}: {product}")
    print("   ✅ Product catalog generator works!")
    
    # Test customer data generator
    print("\n3. Testing customer_data_generator:")
    customer_gen = customer_data_generator(3)
    for i, customer in enumerate(customer_gen):
        print(f"   Customer {i+1}: {customer}")
    print("   ✅ Customer data generator works!")
    
    # Test corrupted data generator
    print("\n4. Testing corrupted_data_generator:")
    corrupted_gen = corrupted_data_generator("test", 5, 0.4)
    valid_count = 0
    for i, record in enumerate(corrupted_gen):
        is_valid = all(record.get(field) for field in ['transaction_id', 'customer_id', 'product_id'])
        if is_valid:
            valid_count += 1
        print(f"   Record {i+1} valid: {is_valid}")
    print(f"   Valid records: {valid_count}/5")
    print("   ✅ Corrupted data generator works!")
    
    # Test batch generator
    print("\n5. Testing batch_data_generator:")
    sales_gen = sales_data_generator("batch_test", 7)
    batch_gen = batch_data_generator(sales_gen, 3)
    for i, batch in enumerate(batch_gen):
        print(f"   Batch {i+1} size: {len(batch)}")
    print("   ✅ Batch data generator works!")

if __name__ == "__main__":
    test_generators()