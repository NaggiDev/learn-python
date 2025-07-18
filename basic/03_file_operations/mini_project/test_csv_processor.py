#!/usr/bin/env python3
"""
Tests for the CSV Data Processor.
"""

import os
import csv
import unittest
from csv_processor import CSVProcessor


class TestCSVProcessor(unittest.TestCase):
    """Test cases for the CSV Processor."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = CSVProcessor()
        self.sample_dir = "sample_data"
        self.expected_dir = "expected_outputs"
        self.output_dir = "test_outputs"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def tearDown(self):
        """Tear down test fixtures."""
        # Clean up test output files
        for file in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, file))
    
    def test_detect_dialect(self):
        """Test dialect detection."""
        employees_path = os.path.join(self.sample_dir, "employees.csv")
        dialect = self.processor.detect_dialect(employees_path)
        
        self.assertEqual(dialect['delimiter'], ',')
        self.assertEqual(dialect['quotechar'], '"')
        self.assertTrue(dialect['has_header'])
    
    def test_read_csv(self):
        """Test reading CSV files."""
        employees_path = os.path.join(self.sample_dir, "employees.csv")
        data, columns = self.processor.read_csv(employees_path)
        
        self.assertEqual(len(data), 10)
        self.assertEqual(len(columns), 8)
        self.assertEqual(columns[0], "employee_id")
        self.assertEqual(data[0]["first_name"], "John")
    
    def test_filter_data(self):
        """Test filtering data."""
        employees_path = os.path.join(self.sample_dir, "employees.csv")
        output_path = os.path.join(self.output_dir, "filtered_employees.csv")
        expected_path = os.path.join(self.expected_dir, "filtered_employees.csv")
        
        # Filter employees with salary > 70000
        self.processor.filter_data(employees_path, "salary", ">", "70000", output_path)
        
        # Compare output with expected output
        with open(output_path, 'r', newline='') as output_file, open(expected_path, 'r', newline='') as expected_file:
            output_reader = csv.DictReader(output_file)
            expected_reader = csv.DictReader(expected_file)
            
            output_data = list(output_reader)
            expected_data = list(expected_reader)
            
            self.assertEqual(len(output_data), len(expected_data))
            
            for i in range(len(output_data)):
                self.assertEqual(output_data[i]["employee_id"], expected_data[i]["employee_id"])
                self.assertEqual(output_data[i]["salary"], expected_data[i]["salary"])
    
    def test_sort_data(self):
        """Test sorting data."""
        sales_path = os.path.join(self.sample_dir, "sales.csv")
        output_path = os.path.join(self.output_dir, "sorted_sales.csv")
        expected_path = os.path.join(self.expected_dir, "sorted_sales.csv")
        
        # Sort sales by date
        self.processor.sort_data(sales_path, ["sale_date"], output_path)
        
        # Compare output with expected output
        with open(output_path, 'r', newline='') as output_file, open(expected_path, 'r', newline='') as expected_file:
            output_reader = csv.DictReader(output_file)
            expected_reader = csv.DictReader(expected_file)
            
            output_data = list(output_reader)
            expected_data = list(expected_reader)
            
            self.assertEqual(len(output_data), len(expected_data))
            
            for i in range(len(output_data)):
                self.assertEqual(output_data[i]["sale_date"], expected_data[i]["sale_date"])
    
    def test_calculate_stats(self):
        """Test calculating statistics."""
        employees_path = os.path.join(self.sample_dir, "employees.csv")
        
        # Calculate statistics on salary column
        # This is a visual test, so we just make sure it doesn't raise an exception
        self.processor.calculate_stats(employees_path, "salary")
    
    def test_transform_data(self):
        """Test transforming data."""
        employees_path = os.path.join(self.sample_dir, "employees.csv")
        output_path = os.path.join(self.output_dir, "transformed_employees.csv")
        
        # Give everyone a 10% raise
        self.processor.transform_data(employees_path, "salary", "multiply", "1.1", output_path)
        
        # Verify the transformation
        data, columns = self.processor.read_csv(output_path)
        original_data, _ = self.processor.read_csv(employees_path)
        
        for i in range(len(data)):
            original_salary = float(original_data[i]["salary"])
            transformed_salary = float(data[i]["salary"])
            self.assertAlmostEqual(transformed_salary, original_salary * 1.1, delta=0.01)
    
    def test_merge_files(self):
        """Test merging files."""
        employees_path = os.path.join(self.sample_dir, "employees.csv")
        sales_path = os.path.join(self.sample_dir, "sales.csv")
        output_path = os.path.join(self.output_dir, "merged_data.csv")
        expected_path = os.path.join(self.expected_dir, "merged_data.csv")
        
        # Merge employees and sales on employee_id
        self.processor.merge_files([employees_path, sales_path], "employee_id", output_path)
        
        # Compare output with expected output
        with open(output_path, 'r', newline='') as output_file, open(expected_path, 'r', newline='') as expected_file:
            output_reader = csv.DictReader(output_file)
            expected_reader = csv.DictReader(expected_file)
            
            output_data = list(output_reader)
            expected_data = list(expected_reader)
            
            self.assertEqual(len(output_data), len(expected_data))
            
            # Check that all expected columns are present
            for column in expected_reader.fieldnames:
                self.assertIn(column, output_reader.fieldnames)


if __name__ == '__main__':
    unittest.main()