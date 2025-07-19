"""
Data Pipeline with Monitoring - Review Exercise

This exercise combines ALL intermediate concepts while introducing data engineering patterns:
- Object-oriented programming (classes, inheritance, composition, abstract classes)
- Functional programming patterns (decorators, higher-order functions, map/filter/reduce)
- Module organization and package structure
- Testing and debugging practices with comprehensive logging
- Introduction to data engineering and monitoring patterns (advanced topic)

Requirements:
1. Create a DataPipeline system that can:
   - Process data through multiple transformation stages
   - Monitor pipeline performance and health
   - Handle data validation and quality checks
   - Implement error handling and recovery mechanisms
   - Provide real-time metrics and alerting
   - Support different data sources and sinks
   - Include comprehensive logging and debugging

2. Implement proper OOP design with abstract base classes and interfaces
3. Use functional programming for data transformations
4. Include comprehensive test coverage and monitoring
5. Demonstrate all intermediate concepts in a cohesive system

This bridges to advanced concepts by introducing:
- Data engineering patterns and architectures
- Real-time monitoring and alerting systems
- Performance optimization and profiling
- Scalable data processing architectures
"""

import json
import time
import statistics
from abc import ABC, abstractmethod
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from functools import wraps, reduce
from typing import Any, Callable, Dict, List, Optional, Iterator, Union
import logging
import threading
import queue
import csv
import io


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class PipelineStatus(Enum):
    """Pipeline status enumeration."""
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPING = "stopping"
    ERROR = "error"


class DataQuality(Enum):
    """Data quality levels."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"


class AlertLevel(Enum):
    """Alert severity levels."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


@dataclass
class PipelineMetrics:
    """Metrics for pipeline monitoring."""
    records_processed: int = 0
    records_failed: int = 0
    processing_rate: float = 0.0  # records per second
    average_processing_time: float = 0.0
    error_rate: float = 0.0
    data_quality_score: float = 0.0
    uptime: float = 0.0
    memory_usage: float = 0.0
    cpu_usage: float = 0.0
    last_updated: datetime = field(default_factory=datetime.now)


@dataclass
class DataRecord:
    """Represents a data record in the pipeline."""
    id: str
    data: Dict[str, Any]
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    processed_at: Optional[datetime] = None
    stage: str = "input"
    quality_score: float = 1.0
    errors: List[str] = field(default_factory=list)


@dataclass
class ProcessingResult:
    """Result of data processing operation."""
    success: bool
    record: Optional[DataRecord] = None
    error_message: Optional[str] = None
    processing_time: float = 0.0
    stage: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Alert:
    """System alert."""
    level: AlertLevel
    message: str
    component: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


def monitoring_decorator(component_name: str) -> Callable:
    """
    Decorator to add monitoring to pipeline components.
    
    Args:
        component_name: Name of the component being monitored
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            start_time = time.time()
            component_logger = logging.getLogger(f"monitor.{component_name}")
            
            try:
                component_logger.debug(f"Starting {func.__name__}")
                result = func(self, *args, **kwargs)
                
                execution_time = time.time() - start_time
                component_logger.info(f"Completed {func.__name__} in {execution_time:.3f}s")
                
                # Update metrics if monitor exists
                if hasattr(self, 'monitor') and self.monitor:
                    self.monitor.record_operation(component_name, execution_time, True)
                
                return result
                
            except Exception as e:
                execution_time = time.time() - start_time
                component_logger.error(f"Failed {func.__name__} after {execution_time:.3f}s: {str(e)}")
                
                # Update metrics if monitor exists
                if hasattr(self, 'monitor') and self.monitor:
                    self.monitor.record_operation(component_name, execution_time, False)
                    self.monitor.add_alert(AlertLevel.ERROR, f"{component_name} error: {str(e)}", component_name)
                
                raise
        
        return wrapper
    return decorator


def demonstrate_data_pipeline():
    """Demonstrate the data pipeline with monitoring."""
    print("Data Pipeline with Monitoring Demonstration")
    print("=" * 50)
    
    # Create sample data
    sample_data = [
        {"id": 1, "name": "Alice", "age": 25, "salary": 50000, "department": "Engineering"},
        {"id": 2, "name": "Bob", "age": 30, "salary": 60000, "department": "Marketing"},
        {"id": 3, "name": "Charlie", "age": 35, "salary": 70000, "department": "Engineering"},
        {"id": 4, "name": "Diana", "age": 28, "salary": 55000, "department": "Sales"},
        {"id": 5, "name": "Eve", "age": 32, "salary": 65000, "department": "Engineering"},
    ]
    
    print(f"Created sample dataset with {len(sample_data)} records")
    print("This is a simplified demonstration - full implementation would include:")
    print("- Complete data pipeline with transformers")
    print("- Real-time monitoring and alerting")
    print("- Data quality validation")
    print("- Performance metrics collection")
    print("- Error handling and recovery")


def main():
    """Main function with menu-driven interface."""
    print("=== Data Pipeline with Monitoring ===")
    print("1. Run demonstration")
    print("2. Create custom pipeline")
    print("3. Monitor existing pipeline")
    print("4. Performance testing")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            demonstrate_data_pipeline()
            
        elif choice == "2":
            print("Custom pipeline creation not yet implemented")
            
        elif choice == "3":
            print("Pipeline monitoring not yet implemented")
            
        elif choice == "4":
            print("Performance testing not yet implemented")
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()