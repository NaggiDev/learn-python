# Data Processing Pipeline Mini-Project

## Project Overview

In this mini-project, you'll build a comprehensive data processing pipeline using functional programming concepts you've learned: lambda functions, map/filter/reduce, decorators, and generators. The project simulates processing sales data from multiple sources, applying various transformations, and generating reports.

## Learning Objectives

By completing this project, you will:

1. **Apply Lambda Functions**: Use lambda functions for simple data transformations
2. **Master Map/Filter/Reduce**: Chain functional operations for data processing
3. **Implement Decorators**: Add logging, timing, and validation to your functions
4. **Use Generators**: Create memory-efficient data processing pipelines
5. **Combine Concepts**: Integrate all functional programming concepts in a real-world scenario

## Project Requirements

### Core Features

1. **Data Generation**: Create generators that simulate sales data from different sources
2. **Data Cleaning**: Clean and validate incoming data using functional approaches
3. **Data Transformation**: Transform data using map, filter, and reduce operations
4. **Data Aggregation**: Calculate statistics and summaries using functional techniques
5. **Reporting**: Generate reports using decorators for logging and timing
6. **Pipeline Architecture**: Create a modular, composable data processing pipeline

### Technical Requirements

- Use lambda functions for simple transformations
- Implement at least 3 custom decorators
- Create generators for data sources and processing steps
- Use map, filter, and reduce for data operations
- Handle errors gracefully
- Include comprehensive logging
- Demonstrate memory efficiency with large datasets

## Project Structure

```
mini_project/
├── README.md                 # This file
├── requirements.txt          # Project dependencies
├── data_pipeline.py          # Main pipeline implementation
├── data_sources.py           # Data generation and sources
├── processors.py             # Data processing functions
├── decorators.py             # Custom decorators
├── utils.py                  # Utility functions
├── tests.py                  # Test cases
├── sample_data/              # Sample data files
│   ├── sales_data_1.csv
│   ├── sales_data_2.csv
│   └── products.csv
└── reports/                  # Generated reports directory
```

## Implementation Guide

### Phase 1: Data Sources (Generators)

Create generators that simulate different data sources:

```python
def sales_data_generator(source_id, num_records):
    """Generate sales records from a specific source"""
    # Implementation details in data_sources.py

def product_catalog_generator():
    """Generate product information"""
    # Implementation details in data_sources.py

def customer_data_generator():
    """Generate customer information"""
    # Implementation details in data_sources.py
```

### Phase 2: Data Processing (Map/Filter/Reduce)

Implement data processing functions using functional programming:

```python
def clean_sales_data(raw_data):
    """Clean and validate sales data using filter and map"""
    # Remove invalid records, standardize formats

def calculate_revenue_by_product(sales_data):
    """Calculate total revenue per product using reduce"""
    # Group by product and sum revenue

def top_customers(sales_data, n=10):
    """Find top N customers by total purchases"""
    # Use functional operations to aggregate and sort
```

### Phase 3: Decorators

Create decorators for cross-cutting concerns:

```python
@timer
@logger
@validate_data
def process_sales_batch(batch_data):
    """Process a batch of sales data"""
    # Main processing logic
```

### Phase 4: Pipeline Integration

Combine all components into a cohesive pipeline:

```python
def create_processing_pipeline():
    """Create the main data processing pipeline"""
    # Chain generators and processors together
```

## Sample Data Format

### Sales Data
```csv
transaction_id,customer_id,product_id,quantity,unit_price,timestamp,source
TXN001,CUST123,PROD456,2,29.99,2024-01-15 10:30:00,online
TXN002,CUST456,PROD789,1,149.99,2024-01-15 11:45:00,store
```

### Product Data
```csv
product_id,name,category,cost,margin
PROD456,Wireless Headphones,Electronics,20.00,0.50
PROD789,Running Shoes,Sports,75.00,1.00
```

## Expected Outputs

### Console Output
```
[2024-01-15 12:00:00] Starting data processing pipeline...
[2024-01-15 12:00:01] Processing batch 1 (1000 records)
[2024-01-15 12:00:01] Data cleaning completed - 950 valid records
[2024-01-15 12:00:02] Revenue calculation completed
[2024-01-15 12:00:02] Top customers analysis completed
[2024-01-15 12:00:02] Pipeline completed in 2.34 seconds
```

### Generated Reports
- Daily sales summary
- Top products by revenue
- Customer analysis
- Data quality report

## Getting Started

### Step 1: Set Up the Project
1. Create the project directory structure
2. Install any required dependencies
3. Review the sample data format

### Step 2: Implement Data Sources
1. Start with `data_sources.py`
2. Create generators for different data sources
3. Test data generation with small samples

### Step 3: Build Processors
1. Implement data cleaning functions
2. Create aggregation functions using reduce
3. Add filtering and transformation logic

### Step 4: Add Decorators
1. Create timing decorator
2. Implement logging decorator
3. Add data validation decorator

### Step 5: Build the Pipeline
1. Integrate all components
2. Create the main pipeline function
3. Add error handling and logging

### Step 6: Test and Optimize
1. Test with sample data
2. Verify memory efficiency
3. Optimize performance bottlenecks

## Testing Your Implementation

Run the provided tests to verify your implementation:

```bash
python tests.py
```

Expected test results:
- All data generators produce valid data
- Processing functions handle edge cases
- Decorators work correctly
- Pipeline processes data efficiently
- Memory usage remains reasonable for large datasets

## Extension Challenges

Once you complete the basic requirements, try these extensions:

1. **Real-time Processing**: Modify the pipeline to handle streaming data
2. **Multiple Output Formats**: Generate reports in JSON, XML, and CSV formats
3. **Data Validation**: Add comprehensive data validation with custom exceptions
4. **Performance Monitoring**: Add detailed performance metrics and profiling
5. **Configuration**: Make the pipeline configurable through external files
6. **Parallel Processing**: Use generators with threading for concurrent processing

## Evaluation Criteria

Your project will be evaluated on:

1. **Functional Programming Usage** (25%)
   - Proper use of lambda functions
   - Effective use of map, filter, reduce
   - Creative application of functional concepts

2. **Generator Implementation** (25%)
   - Memory-efficient data processing
   - Proper generator composition
   - Handling of large datasets

3. **Decorator Design** (20%)
   - Well-designed, reusable decorators
   - Proper use of functools.wraps
   - Clear separation of concerns

4. **Code Quality** (20%)
   - Clean, readable code
   - Proper error handling
   - Good documentation

5. **Pipeline Architecture** (10%)
   - Modular, composable design
   - Efficient data flow
   - Scalable architecture

## Tips for Success

1. **Start Simple**: Begin with basic functionality and gradually add complexity
2. **Test Frequently**: Test each component as you build it
3. **Use Type Hints**: Add type hints for better code documentation
4. **Profile Memory Usage**: Monitor memory consumption with large datasets
5. **Document Your Code**: Add docstrings and comments explaining your approach
6. **Think Functionally**: Try to solve problems using functional programming patterns

## Resources

- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Itertools Documentation](https://docs.python.org/3/library/itertools.html)
- [Functools Documentation](https://docs.python.org/3/library/functools.html)

Good luck with your data processing pipeline project!