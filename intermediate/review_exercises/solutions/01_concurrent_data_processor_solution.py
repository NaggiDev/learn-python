"""
Concurrent Data Processor - Solution

This solution demonstrates the integration of intermediate concepts while introducing
advanced topics like threading and concurrent programming patterns.
"""

import time
import threading
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import wraps, reduce
from typing import Any, Callable, Dict, List, Optional, Tuple, Iterator
from dataclasses import dataclass, field
from enum import Enum
import logging
import os


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
    metadata: Optional[Dict] = field(default_factory=dict)


def timing_decorator(func: Callable) -> Callable:
    """Decorator to measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logging.debug(f"{func.__name__} executed in {execution_time:.4f} seconds")
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            logging.error(f"{func.__name__} failed after {execution_time:.4f} seconds: {e}")
            raise
    return wrapper


def validation_decorator(validator: Callable[[Any], bool]) -> Callable:
    """Decorator factory for input validation."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Validate first argument (assuming it's the data)
            if args and not validator(args[0]):
                raise ValueError(f"Invalid input for {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_decorator(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """Decorator for retrying failed operations."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        logging.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {e}")
                        time.sleep(delay)
                    else:
                        logging.error(f"All {max_attempts} attempts failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator


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
        self.data = data
        self.name = name
    
    def get_data(self) -> Iterator[Any]:
        """Get data from the list."""
        return iter(self.data)
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get metadata about the data source."""
        return {
            "name": self.name,
            "type": "list",
            "size": len(self.data),
            "data_types": list(set(type(item).__name__ for item in self.data))
        }


class FileDataSource(DataSource):
    """Data source that reads data from a file."""
    
    def __init__(self, filepath: str, parser: Callable[[str], Any] = None):
        self.filepath = filepath
        self.parser = parser or (lambda x: x.strip())
        
    def get_data(self) -> Iterator[Any]:
        """Get data from the file."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():  # Skip empty lines
                        yield self.parser(line)
        except FileNotFoundError:
            logging.error(f"File not found: {self.filepath}")
            return iter([])
        except Exception as e:
            logging.error(f"Error reading file {self.filepath}: {e}")
            return iter([])
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get metadata about the file."""
        metadata = {
            "name": os.path.basename(self.filepath),
            "type": "file",
            "filepath": self.filepath
        }
        
        try:
            stat = os.stat(self.filepath)
            metadata.update({
                "size_bytes": stat.st_size,
                "modified_time": stat.st_mtime
            })
        except Exception as e:
            metadata["error"] = str(e)
            
        return metadata


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
        self.func = func
        self.name = name or f"Function_{func.__name__}"
    
    @timing_decorator
    def transform(self, data: Any) -> Any:
        """Apply the function to transform data."""
        return self.func(data)
    
    def get_name(self) -> str:
        """Get the name of the transformer."""
        return self.name


class FilterTransformer(DataTransformer):
    """Transformer that filters data based on a predicate."""
    
    FILTER_MARKER = object()  # Sentinel object for filtered items
    
    def __init__(self, predicate: Callable[[Any], bool], name: str = None):
        self.predicate = predicate
        self.name = name or f"Filter_{predicate.__name__}"
    
    def transform(self, data: Any) -> Any:
        """Filter data based on predicate."""
        if self.predicate(data):
            return data
        return self.FILTER_MARKER
    
    def get_name(self) -> str:
        """Get the name of the transformer."""
        return self.name


class DataProcessor:
    """Main data processor that orchestrates data processing."""
    
    def __init__(self, mode: ProcessingMode = ProcessingMode.SEQUENTIAL, 
                 max_workers: int = 4):
        self.mode = mode
        self.max_workers = max_workers
        self.transformers = []
        self.logger = logging.getLogger(f"DataProcessor_{id(self)}")
        self.statistics = {
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "total_time": 0.0,
            "transformer_times": {}
        }
        
        if mode == ProcessingMode.CONCURRENT:
            self.executor = ThreadPoolExecutor(max_workers=max_workers)
        else:
            self.executor = None
    
    def add_transformer(self, transformer: DataTransformer) -> None:
        """Add a transformer to the processing pipeline."""
        self.transformers.append(transformer)
        self.statistics["transformer_times"][transformer.get_name()] = 0.0
    
    def process_data_source(self, source: DataSource) -> List[ProcessingResult]:
        """Process data from a source using the configured transformers."""
        start_time = time.time()
        
        # Get all data items
        data_items = list(source.get_data())
        self.logger.info(f"Processing {len(data_items)} items from {source.get_metadata()['name']}")
        
        # Process based on mode
        if self.mode == ProcessingMode.SEQUENTIAL:
            results = self._process_sequential(data_items)
        elif self.mode == ProcessingMode.CONCURRENT:
            results = self._process_concurrent(data_items)
        else:
            results = self._process_sequential(data_items)  # Default fallback
        
        # Update statistics
        total_time = time.time() - start_time
        self.statistics["total_time"] += total_time
        self.statistics["total_processed"] += len(data_items)
        self.statistics["successful"] += sum(1 for r in results if r.success)
        self.statistics["failed"] += sum(1 for r in results if not r.success)
        
        self.logger.info(f"Processed {len(data_items)} items in {total_time:.4f} seconds")
        return results
    
    def _process_sequential(self, data_items: List[Any]) -> List[ProcessingResult]:
        """Process data items sequentially."""
        results = []
        for item in data_items:
            result = self._process_single_item(item)
            results.append(result)
        return results
    
    def _process_concurrent(self, data_items: List[Any]) -> List[ProcessingResult]:
        """Process data items concurrently using thread pool."""
        if not self.executor:
            return self._process_sequential(data_items)
        
        # Submit all tasks
        future_to_item = {
            self.executor.submit(self._process_single_item, item): item 
            for item in data_items
        }
        
        results = []
        for future in as_completed(future_to_item):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                # Create error result
                error_result = ProcessingResult(
                    success=False,
                    data=None,
                    processing_time=0.0,
                    error_message=str(e)
                )
                results.append(error_result)
        
        return results
    
    def _process_single_item(self, item: Any) -> ProcessingResult:
        """Process a single data item through all transformers."""
        start_time = time.time()
        current_data = item
        
        try:
            # Apply all transformers in sequence
            for transformer in self.transformers:
                transformer_start = time.time()
                current_data = transformer.transform(current_data)
                transformer_time = time.time() - transformer_start
                self.statistics["transformer_times"][transformer.get_name()] += transformer_time
                
                # Check if item was filtered out
                if current_data is FilterTransformer.FILTER_MARKER:
                    break
            
            # Determine success
            success = current_data is not FilterTransformer.FILTER_MARKER
            final_data = current_data if success else None
            
            processing_time = time.time() - start_time
            
            return ProcessingResult(
                success=success,
                data=final_data,
                processing_time=processing_time,
                metadata={"original_item": item}
            )
            
        except Exception as e:
            processing_time = time.time() - start_time
            return ProcessingResult(
                success=False,
                data=None,
                processing_time=processing_time,
                error_message=str(e),
                metadata={"original_item": item}
            )
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get processing statistics."""
        stats = self.statistics.copy()
        if stats["total_processed"] > 0:
            stats["success_rate"] = stats["successful"] / stats["total_processed"]
            stats["average_time_per_item"] = stats["total_time"] / stats["total_processed"]
        else:
            stats["success_rate"] = 0.0
            stats["average_time_per_item"] = 0.0
        
        return stats
    
    def reset_statistics(self) -> None:
        """Reset processing statistics."""
        self.statistics = {
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "total_time": 0.0,
            "transformer_times": {t.get_name(): 0.0 for t in self.transformers}
        }


class ProcessingPipeline:
    """High-level pipeline that combines multiple processors and data sources."""
    
    def __init__(self, name: str = "DefaultPipeline"):
        self.name = name
        self.data_sources = []
        self.processors = []
        self.logger = logging.getLogger(f"Pipeline_{name}")
        self.results = {}
    
    def add_data_source(self, source: DataSource) -> None:
        """Add a data source to the pipeline."""
        self.data_sources.append(source)
    
    def add_processor(self, processor: DataProcessor) -> None:
        """Add a processor to the pipeline."""
        self.processors.append(processor)
    
    def run_pipeline(self) -> Dict[str, List[ProcessingResult]]:
        """Run the entire pipeline."""
        self.logger.info(f"Starting pipeline '{self.name}' with {len(self.data_sources)} sources and {len(self.processors)} processors")
        
        pipeline_results = {}
        
        for source in self.data_sources:
            source_name = source.get_metadata()["name"]
            source_results = []
            
            for processor in self.processors:
                try:
                    results = processor.process_data_source(source)
                    source_results.extend(results)
                except Exception as e:
                    self.logger.error(f"Error processing source {source_name}: {e}")
            
            pipeline_results[source_name] = source_results
        
        self.results = pipeline_results
        self.logger.info(f"Pipeline '{self.name}' completed")
        return pipeline_results
    
    def get_pipeline_summary(self) -> str:
        """Get a formatted summary of pipeline execution."""
        if not self.results:
            return f"Pipeline '{self.name}' has not been executed yet."
        
        summary_lines = [
            f"Pipeline Summary: {self.name}",
            "=" * 50
        ]
        
        total_items = 0
        total_successful = 0
        total_time = 0.0
        
        for source_name, results in self.results.items():
            successful = sum(1 for r in results if r.success)
            total_processing_time = sum(r.processing_time for r in results)
            
            summary_lines.extend([
                f"Source: {source_name}",
                f"  Items processed: {len(results)}",
                f"  Successful: {successful}",
                f"  Success rate: {successful/len(results)*100:.1f}%" if results else "  Success rate: 0%",
                f"  Total time: {total_processing_time:.4f}s",
                ""
            ])
            
            total_items += len(results)
            total_successful += successful
            total_time += total_processing_time
        
        summary_lines.extend([
            "Overall Statistics:",
            f"  Total items: {total_items}",
            f"  Total successful: {total_successful}",
            f"  Overall success rate: {total_successful/total_items*100:.1f}%" if total_items else "  Overall success rate: 0%",
            f"  Total processing time: {total_time:.4f}s"
        ])
        
        return "\n".join(summary_lines)


# Utility functions for functional programming demonstrations

def compose_functions(*functions: Callable) -> Callable:
    """Compose multiple functions into a single function."""
    def composed_function(x):
        return reduce(lambda acc, func: func(acc), functions, x)
    return composed_function


def create_data_pipeline(*transformers: DataTransformer) -> Callable[[Any], Any]:
    """Create a data processing pipeline from transformers."""
    def pipeline_function(data):
        current_data = data
        for transformer in transformers:
            current_data = transformer.transform(current_data)
            if current_data is FilterTransformer.FILTER_MARKER:
                break
        return current_data
    return pipeline_function


def parallel_map(func: Callable, data: List[Any], max_workers: int = 4) -> List[Any]:
    """Parallel version of map function using threading."""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(func, item) for item in data]
        results = []
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as e:
                results.append(f"Error: {e}")
        return results


def demonstrate_concurrent_processing():
    """Demonstrate the concurrent data processing capabilities."""
    print("Concurrent Data Processor Demonstration")
    print("=" * 50)
    
    # Create sample data - simulate some processing delay
    def slow_square(x):
        time.sleep(0.01)  # Simulate processing time
        return x ** 2
    
    def is_even(x):
        return x % 2 == 0
    
    numbers = list(range(1, 51))  # Numbers 1-50
    
    # Create data source
    source = ListDataSource(numbers, "NumberSource")
    
    # Create transformers
    square_transformer = FunctionTransformer(slow_square, "SlowSquare")
    even_filter = FilterTransformer(is_even, "EvenFilter")
    
    # Create processors with different modes
    sequential_processor = DataProcessor(ProcessingMode.SEQUENTIAL)
    concurrent_processor = DataProcessor(ProcessingMode.CONCURRENT, max_workers=4)
    
    # Add transformers
    for processor in [sequential_processor, concurrent_processor]:
        processor.add_transformer(square_transformer)
        processor.add_transformer(even_filter)
    
    # Process data and compare performance
    print(f"Processing {len(numbers)} numbers with square and even filter transformations...")
    
    # Sequential processing
    print("\nRunning sequential processing...")
    start_time = time.time()
    sequential_results = sequential_processor.process_data_source(source)
    sequential_time = time.time() - start_time
    
    # Concurrent processing
    print("Running concurrent processing...")
    start_time = time.time()
    concurrent_results = concurrent_processor.process_data_source(source)
    concurrent_time = time.time() - start_time
    
    print(f"\nResults:")
    print(f"Sequential processing time: {sequential_time:.4f} seconds")
    print(f"Concurrent processing time: {concurrent_time:.4f} seconds")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")
    
    # Show some results
    successful_sequential = [r for r in sequential_results if r.success]
    successful_concurrent = [r for r in concurrent_results if r.success]
    
    print(f"\nSuccessful results (sequential): {len(successful_sequential)}")
    print(f"Successful results (concurrent): {len(successful_concurrent)}")
    
    if successful_sequential:
        print(f"Sample results: {[r.data for r in successful_sequential[:5]]}")


def main():
    """Main function with demonstration."""
    demonstrate_concurrent_processing()


if __name__ == "__main__":
    main()