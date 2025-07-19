"""
Concurrent Data Processor - Review Exercise

This exercise combines multiple intermediate concepts while introducing advanced topics:
- Object-oriented programming (classes, inheritance, composition)
- Functional programming (map, filter, reduce, decorators)
- Module organization and package structure
- Testing and debugging practices
- Introduction to threading and concurrency (advanced topic)

Requirements:
1. Create a DataProcessor system that can:
   - Process data using various transformation functions
   - Handle multiple data sources concurrently
   - Apply functional programming patterns for data transformation
   - Provide a plugin-like architecture for processors
   - Include comprehensive logging and error handling
   - Support both synchronous and asynchronous processing modes

2. Implement proper OOP design with inheritance and composition
3. Use decorators for timing, logging, and validation
4. Include comprehensive test coverage
5. Demonstrate functional programming concepts

This bridges to advanced concepts by introducing:
- Threading and concurrent execution
- Producer-consumer patterns
- Performance monitoring and optimization
- Scalable architecture design
"""

import time
import threading
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import wraps, reduce
from typing import Any, Callable, Dict, List, Optional, Tuple, Iterator
from dataclasses import dataclass
from enum import Enum
import logging
import queue


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class ProcessingMode(Enum):
    """Enumeration for processing modes."""
    SEQUENTIAL = "sequential"
    CONCURRENT = "concurrent"
    BATCH = "batch"


@dataclass
class ProcessingResult:
    """Data class to hold processing results."""
    success: bool
    data: Any
    processing_time: float
    error_message: Optional[str] = None
    metadata: Optional[Dict] = None


def timing_decorator(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.
    
    This demonstrates decorator usage from intermediate concepts
    while preparing for performance monitoring in advanced topics.
    """
    # TODO: Implement timing decorator
    # - Measure execution time
    # - Log timing information
    # - Return original function result
    # - Handle exceptions gracefully
    pass


def validation_decorator(validator: Callable[[Any], bool]) -> Callable:
    """
    Decorator factory for input validation.
    
    Args:
        validator: Function that validates input and returns bool
        
    Returns:
        Decorator function
    """
    # TODO: Implement validation decorator factory
    # - Create decorator that validates input using provided validator
    # - Raise ValueError for invalid input
    # - Log validation attempts
    pass


def retry_decorator(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """
    Decorator for retrying failed operations.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between attempts in seconds
        
    Returns:
        Decorator function
    """
    # TODO: Implement retry decorator
    # - Retry failed operations up to max_attempts
    # - Add delay between attempts
    # - Log retry attempts
    # - Re-raise exception after max attempts
    pass


class DataSource(ABC):
    """Abstract base class for data sources."""
    
    @abstractmethod
    def get_data(self) -> Iterator[Any]:
        """Get data from the source."""
        pass
    
    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        """Get metadata about the data source."""
        pass


class ListDataSource(DataSource):
    """Data source that provides data from a list."""
    
    def __init__(self, data: List[Any], name: str = "ListSource"):
        """
        Initialize list data source.
        
        Args:
            data: List of data items
            name: Name of the data source
        """
        # TODO: Implement list data source initialization
        pass
    
    def get_data(self) -> Iterator[Any]:
        """Get data from the list."""
        # TODO: Implement data retrieval
        pass
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get metadata about the data source."""
        # TODO: Implement metadata retrieval
        pass


class FileDataSource(DataSource):
    """Data source that reads data from a file."""
    
    def __init__(self, filepath: str, parser: Callable[[str], Any] = None):
        """
        Initialize file data source.
        
        Args:
            filepath: Path to the data file
            parser: Optional function to parse each line
        """
        # TODO: Implement file data source initialization
        pass
    
    def get_data(self) -> Iterator[Any]:
        """Get data from the file."""
        # TODO: Implement file data reading
        # - Read file line by line
        # - Apply parser if provided
        # - Handle file reading errors
        pass
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get metadata about the file."""
        # TODO: Implement file metadata retrieval
        pass


class DataTransformer(ABC):
    """Abstract base class for data transformers."""
    
    @abstractmethod
    def transform(self, data: Any) -> Any:
        """Transform a single data item."""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Get the name of the transformer."""
        pass


class FunctionTransformer(DataTransformer):
    """Transformer that applies a function to data."""
    
    def __init__(self, func: Callable[[Any], Any], name: str = None):
        """
        Initialize function transformer.
        
        Args:
            func: Function to apply to data
            name: Optional name for the transformer
        """
        # TODO: Implement function transformer initialization
        pass
    
    def transform(self, data: Any) -> Any:
        """Apply the function to transform data."""
        # TODO: Implement data transformation
        pass
    
    def get_name(self) -> str:
        """Get the name of the transformer."""
        # TODO: Return transformer name
        pass


class FilterTransformer(DataTransformer):
    """Transformer that filters data based on a predicate."""
    
    def __init__(self, predicate: Callable[[Any], bool], name: str = None):
        """
        Initialize filter transformer.
        
        Args:
            predicate: Function that returns True for items to keep
            name: Optional name for the transformer
        """
        # TODO: Implement filter transformer initialization
        pass
    
    def transform(self, data: Any) -> Any:
        """Filter data based on predicate."""
        # TODO: Implement data filtering
        # - Return data if predicate is True
        # - Return None or special marker if predicate is False
        pass
    
    def get_name(self) -> str:
        """Get the name of the transformer."""
        # TODO: Return transformer name
        pass


class DataProcessor:
    """Main data processor that orchestrates data processing."""
    
    def __init__(self, mode: ProcessingMode = ProcessingMode.SEQUENTIAL, 
                 max_workers: int = 4):
        """
        Initialize data processor.
        
        Args:
            mode: Processing mode (sequential, concurrent, batch)
            max_workers: Maximum number of worker threads for concurrent processing
        """
        # TODO: Implement data processor initialization
        # - Set processing mode and worker count
        # - Initialize logger
        # - Set up thread pool if needed
        # - Initialize statistics tracking
        pass
    
    def add_transformer(self, transformer: DataTransformer) -> None:
        """Add a transformer to the processing pipeline."""
        # TODO: Implement transformer addition
        pass
    
    def process_data_source(self, source: DataSource) -> List[ProcessingResult]:
        """
        Process data from a source using the configured transformers.
        
        Args:
            source: Data source to process
            
        Returns:
            List of processing results
        """
        # TODO: Implement data source processing
        # - Get data from source
        # - Apply transformers based on processing mode
        # - Return results with timing and metadata
        pass
    
    def _process_sequential(self, data_items: List[Any]) -> List[ProcessingResult]:
        """Process data items sequentially."""
        # TODO: Implement sequential processing
        # - Process each item through all transformers
        # - Measure timing for each item
        # - Handle errors gracefully
        pass
    
    def _process_concurrent(self, data_items: List[Any]) -> List[ProcessingResult]:
        """Process data items concurrently using thread pool."""
        # TODO: Implement concurrent processing
        # - Use ThreadPoolExecutor to process items in parallel
        # - Collect results as they complete
        # - Handle thread synchronization
        # - Measure overall and per-item timing
        pass
    
    def _process_single_item(self, item: Any) -> ProcessingResult:
        """Process a single data item through all transformers."""
        # TODO: Implement single item processing
        # - Apply all transformers in sequence
        # - Use functional programming patterns (reduce, map, filter)
        # - Handle transformation errors
        # - Return ProcessingResult with timing and metadata
        pass
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get processing statistics."""
        # TODO: Implement statistics collection
        # - Total items processed
        # - Success/failure rates
        # - Average processing time
        # - Transformer performance metrics
        pass
    
    def reset_statistics(self) -> None:
        """Reset processing statistics."""
        # TODO: Implement statistics reset
        pass


class ProcessingPipeline:
    """High-level pipeline that combines multiple processors and data sources."""
    
    def __init__(self, name: str = "DefaultPipeline"):
        """
        Initialize processing pipeline.
        
        Args:
            name: Name of the pipeline
        """
        # TODO: Implement pipeline initialization
        # - Set pipeline name
        # - Initialize processors and data sources lists
        # - Set up logging
        pass
    
    def add_data_source(self, source: DataSource) -> None:
        """Add a data source to the pipeline."""
        # TODO: Implement data source addition
        pass
    
    def add_processor(self, processor: DataProcessor) -> None:
        """Add a processor to the pipeline."""
        # TODO: Implement processor addition
        pass
    
    def run_pipeline(self) -> Dict[str, List[ProcessingResult]]:
        """
        Run the entire pipeline.
        
        Returns:
            Dictionary mapping source names to processing results
        """
        # TODO: Implement pipeline execution
        # - Process each data source with each processor
        # - Collect and organize results
        # - Handle pipeline-level errors
        # - Log pipeline execution summary
        pass
    
    def get_pipeline_summary(self) -> str:
        """Get a formatted summary of pipeline execution."""
        # TODO: Implement pipeline summary generation
        # - Include processing statistics
        # - Show performance metrics
        # - Format nicely for display
        pass


# Utility functions for functional programming demonstrations

def compose_functions(*functions: Callable) -> Callable:
    """
    Compose multiple functions into a single function.
    
    This demonstrates functional programming concepts.
    """
    # TODO: Implement function composition
    # - Use reduce to compose functions
    # - Return a single function that applies all functions in sequence
    pass


def create_data_pipeline(*transformers: DataTransformer) -> Callable[[Any], Any]:
    """
    Create a data processing pipeline from transformers.
    
    Args:
        transformers: Variable number of data transformers
        
    Returns:
        Function that applies all transformers in sequence
    """
    # TODO: Implement data pipeline creation
    # - Combine transformers into a single processing function
    # - Use functional programming patterns
    pass


def parallel_map(func: Callable, data: List[Any], max_workers: int = 4) -> List[Any]:
    """
    Parallel version of map function using threading.
    
    This introduces concurrent programming concepts.
    """
    # TODO: Implement parallel map
    # - Use ThreadPoolExecutor to apply function in parallel
    # - Maintain order of results
    # - Handle exceptions in worker threads
    pass


def demonstrate_concurrent_processing():
    """Demonstrate the concurrent data processing capabilities."""
    print("Concurrent Data Processor Demonstration")
    print("=" * 50)
    
    # Create sample data
    numbers = list(range(1, 101))  # Numbers 1-100
    
    # Create data source
    source = ListDataSource(numbers, "NumberSource")
    
    # Create transformers
    square_transformer = FunctionTransformer(lambda x: x ** 2, "Square")
    even_filter = FilterTransformer(lambda x: x % 2 == 0, "EvenFilter")
    
    # Create processors with different modes
    sequential_processor = DataProcessor(ProcessingMode.SEQUENTIAL)
    concurrent_processor = DataProcessor(ProcessingMode.CONCURRENT, max_workers=4)
    
    # Add transformers
    for processor in [sequential_processor, concurrent_processor]:
        processor.add_transformer(square_transformer)
        processor.add_transformer(even_filter)
    
    # Process data and compare performance
    print("Processing 100 numbers with square and even filter transformations...")
    
    # Sequential processing
    start_time = time.time()
    sequential_results = sequential_processor.process_data_source(source)
    sequential_time = time.time() - start_time
    
    # Concurrent processing
    start_time = time.time()
    concurrent_results = concurrent_processor.process_data_source(source)
    concurrent_time = time.time() - start_time
    
    print(f"Sequential processing time: {sequential_time:.4f} seconds")
    print(f"Concurrent processing time: {concurrent_time:.4f} seconds")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")
    
    # Show statistics
    print("\nSequential Processor Statistics:")
    print(sequential_processor.get_statistics())
    
    print("\nConcurrent Processor Statistics:")
    print(concurrent_processor.get_statistics())


def main():
    """Main function with menu-driven interface."""
    print("=== Concurrent Data Processor ===")
    print("1. Run demonstration")
    print("2. Create custom pipeline")
    print("3. Test individual components")
    print("4. Performance comparison")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            demonstrate_concurrent_processing()
            
        elif choice == "2":
            # TODO: Implement custom pipeline creation
            print("Custom pipeline creation not yet implemented")
            
        elif choice == "3":
            # TODO: Implement component testing
            print("Component testing not yet implemented")
            
        elif choice == "4":
            # TODO: Implement performance comparison
            print("Performance comparison not yet implemented")
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()