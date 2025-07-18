"""
Test Suite for Data Processing Pipeline Mini-Project

Run this file to test your implementation of the data processing pipeline.
"""

import sys
import time
from typing import Generator, Dict, Any

def test_data_sources():
    """Test data source generators."""
    print("Testing Data Sources...")
    
    try:
        # Try to import your implementations
        from data_sources import (
            sales_data_generator, 
            product_catalog_generator, 
            customer_data_generator,
            batch_data_generator
        )
        
        # Test sales data generator
        print("  ✓ Testing sales_data_generator...")
        sales_gen = sales_data_generator("test", 5)
        sales_data = list(sales_gen)
        assert len(sales_data) == 5, "Should generate 5 records"
        assert all('transaction_id' in record for record in sales_data), "All records should have transaction_id"
        
        # Test product catalog generator
        print("  ✓ Testing product_catalog_generator...")
        product_gen = product_catalog_generator()
        products = [next(product_gen) for _ in range(3)]
        assert len(products) == 3, "Should generate 3 products"
        assert all('product_id' in product for product in products), "All products should have product_id"
        
        # Test customer data generator
        print("  ✓ Testing customer_data_generator...")
        customer_gen = customer_data_generator(3)
        customers = list(customer_gen)
        assert len(customers) == 3, "Should generate 3 customers"
        
        # Test batch generator
        print("  ✓ Testing batch_data_generator...")
        sales_gen = sales_data_generator("batch_test", 7)
        batch_gen = batch_data_generator(sales_gen, 3)
        batches = list(batch_gen)
        assert len(batches) == 3, "Should create 3 batches (2 full, 1 partial)"
        assert len(batches[0]) == 3, "First batch should have 3 items"
        assert len(batches[-1]) == 1, "Last batch should have 1 item"
        
        print("✅ Data Sources: All tests passed!")
        return True
        
    except ImportError:
        print("❌ Data Sources: Import error - implement data_sources.py")
        return False
    except Exception as e:
        print(f"❌ Data Sources: {e}")
        return False

def test_decorators():
    """Test custom decorators."""
    print("\nTesting Decorators...")
    
    try:
        from decorators import timer, logger, validate_data, cache_results
        
        # Test timer decorator
        print("  ✓ Testing timer decorator...")
        @timer
        def slow_function():
            time.sleep(0.01)
            return "done"
        
        result = slow_function()
        assert result == "done", "Timer decorator should preserve return value"
        
        # Test validation decorator
        print("  ✓ Testing validation decorator...")
        @validate_data(required_fields=["id", "name"])
        def process_data(data):
            return data
        
        valid_data = {"id": 1, "name": "test"}
        result = process_data(valid_data)
        assert result == valid_data, "Should process valid data"
        
        try:
            invalid_data = {"id": 1}  # Missing name
            process_data(invalid_data)
            assert False, "Should raise exception for invalid data"
        except ValueError:
            pass  # Expected
        
        # Test cache decorator
        print("  ✓ Testing cache decorator...")
        call_count = 0
        
        @cache_results
        def cached_function(x):
            nonlocal call_count
            call_count += 1
            return x * 2
        
        result1 = cached_function(5)
        result2 = cached_function(5)  # Should use cache
        assert result1 == result2 == 10, "Should return correct result"
        assert call_count == 1, "Should only call function once due to caching"
        
        print("✅ Decorators: All tests passed!")
        return True
        
    except ImportError:
        print("❌ Decorators: Import error - implement decorators.py")
        return False
    except Exception as e:
        print(f"❌ Decorators: {e}")
        return False

def test_processors():
    """Test data processing functions."""
    print("\nTesting Processors...")
    
    try:
        from processors import clean_sales_data, is_valid_record, calculate_total_amount
        
        # Test validation function
        print("  ✓ Testing is_valid_record...")
        valid_record = {
            'transaction_id': 'TXN001',
            'customer_id': 'CUST123',
            'product_id': 'PROD456',
            'quantity': 2,
            'unit_price': 29.99
        }
        invalid_record = {
            'transaction_id': 'TXN002',
            'customer_id': 'CUST456',
            'quantity': -1,  # Invalid
            'unit_price': 0   # Invalid
        }
        
        assert is_valid_record(valid_record), "Should validate correct record"
        assert not is_valid_record(invalid_record), "Should reject invalid record"
        
        # Test total amount calculation
        print("  ✓ Testing calculate_total_amount...")
        total = calculate_total_amount(valid_record)
        expected = 2 * 29.99
        assert abs(total - expected) < 0.01, f"Expected {expected}, got {total}"
        
        print("✅ Processors: All tests passed!")
        return True
        
    except ImportError:
        print("❌ Processors: Import error - implement processors.py")
        return False
    except Exception as e:
        print(f"❌ Processors: {e}")
        return False

def test_pipeline_integration():
    """Test pipeline integration."""
    print("\nTesting Pipeline Integration...")
    
    try:
        from data_pipeline import DataPipeline, demonstrate_functional_concepts
        
        # Test pipeline creation
        print("  ✓ Testing DataPipeline class...")
        config = {
            'batch_size': 100,
            'sources': ['test_source'],
            'records_per_source': 50
        }
        pipeline = DataPipeline(config)
        assert pipeline.config['batch_size'] == 100, "Should use provided config"
        
        # Test functional concepts demonstration
        print("  ✓ Testing functional concepts...")
        demonstrate_functional_concepts()  # Should run without error
        
        print("✅ Pipeline Integration: All tests passed!")
        return True
        
    except ImportError:
        print("❌ Pipeline Integration: Import error - implement data_pipeline.py")
        return False
    except Exception as e:
        print(f"❌ Pipeline Integration: {e}")
        return False

def test_memory_efficiency():
    """Test memory efficiency of generators."""
    print("\nTesting Memory Efficiency...")
    
    try:
        # Test that generators are memory efficient
        def create_large_list(n):
            return [i for i in range(n)]
        
        def create_large_generator(n):
            for i in range(n):
                yield i
        
        n = 10000
        
        # Compare memory usage
        large_list = create_large_list(n)
        large_gen = create_large_generator(n)
        
        list_size = sys.getsizeof(large_list)
        gen_size = sys.getsizeof(large_gen)
        
        print(f"  List size: {list_size} bytes")
        print(f"  Generator size: {gen_size} bytes")
        print(f"  Memory savings: {list_size - gen_size} bytes")
        
        assert gen_size < list_size, "Generator should be more memory efficient"
        
        print("✅ Memory Efficiency: Test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Memory Efficiency: {e}")
        return False

def run_all_tests():
    """Run all tests and report results."""
    print("=" * 60)
    print("DATA PROCESSING PIPELINE - TEST SUITE")
    print("=" * 60)
    
    tests = [
        test_data_sources,
        test_decorators,
        test_processors,
        test_pipeline_integration,
        test_memory_efficiency
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
    
    print("\n" + "=" * 60)
    print(f"TEST RESULTS: {passed}/{total} test suites passed")
    print("=" * 60)
    
    if passed == total:
        print("🎉 Congratulations! All tests passed!")
        print("Your data processing pipeline implementation is working correctly.")
    else:
        print("📚 Some tests failed. Review the error messages above and:")
        print("   1. Implement the missing functions")
        print("   2. Fix any bugs in your implementation")
        print("   3. Run the tests again")
    
    print("\nNext steps:")
    print("   - Run individual module tests: python data_sources.py")
    print("   - Test the complete pipeline: python data_pipeline.py")
    print("   - Try the extension challenges in README.md")

if __name__ == "__main__":
    run_all_tests()