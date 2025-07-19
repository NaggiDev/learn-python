"""
Exercise 4: Logging Practice

This exercise will help you practice using Python's logging module.
Complete the TODO sections to implement proper logging.

Instructions:
1. Complete each function by adding appropriate logging statements
2. Configure logging as specified in each section
3. Run the script to see the logging output
4. Experiment with different log levels and formats

Run this file: python 04_logging_practice.py
"""

import logging
import time
import json
from datetime import datetime


# TODO 1: Basic Logging Configuration
# Configure basic logging with:
# - Level: DEBUG
# - Format: '%(asctime)s - %(levelname)s - %(message)s'
# - Date format: '%Y-%m-%d %H:%M:%S'

def configure_basic_logging():
    """Configure basic logging for the application."""
    # TODO: Implement basic logging configuration
    pass


# TODO 2: File and Console Logging
def configure_advanced_logging():
    """
    Configure logging to output to both console and file.
    
    Requirements:
    - Console: WARNING level and above, simple format
    - File: DEBUG level and above, detailed format
    - File name: 'app.log'
    """
    # TODO: Create a logger named 'myapp'
    logger = None
    
    # TODO: Create console handler (WARNING level)
    console_handler = None
    
    # TODO: Create file handler (DEBUG level)
    file_handler = None
    
    # TODO: Create formatters
    console_format = None  # Simple: '%(levelname)s - %(message)s'
    file_format = None     # Detailed: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # TODO: Set formatters and add handlers to logger
    
    return logger


# TODO 3: Function with Logging
def calculate_factorial(n):
    """
    Calculate factorial with proper logging.
    
    Add logging for:
    - Function entry with parameter
    - Each iteration (debug level)
    - Final result (info level)
    - Error cases (error level)
    """
    logger = logging.getLogger('myapp.math')
    
    # TODO: Log function entry
    
    # TODO: Validate input and log errors
    if n < 0:
        # TODO: Log error for negative input
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        # TODO: Log base case
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
        # TODO: Log each iteration (debug level)
    
    # TODO: Log final result
    return result


# TODO 4: Error Handling with Logging
def safe_file_reader(filename):
    """
    Read a file with proper error logging.
    
    Add logging for:
    - Attempt to read file (info level)
    - Success (info level)
    - File not found (error level)
    - Permission errors (error level)
    - Other exceptions (critical level)
    """
    logger = logging.getLogger('myapp.file')
    
    # TODO: Log attempt to read file
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # TODO: Log successful read
            return content
    except FileNotFoundError:
        # TODO: Log file not found error
        raise
    except PermissionError:
        # TODO: Log permission error
        raise
    except Exception as e:
        # TODO: Log unexpected error
        raise


# TODO 5: Progress Logging
def process_items(items):
    """
    Process a list of items with progress logging.
    
    Add logging for:
    - Start of processing (info level)
    - Progress every 10 items (info level)
    - Individual item processing (debug level)
    - Completion (info level)
    """
    logger = logging.getLogger('myapp.processor')
    
    # TODO: Log start of processing
    
    for i, item in enumerate(items, 1):
        # TODO: Log individual item processing (debug)
        
        # Simulate processing time
        time.sleep(0.01)
        
        # TODO: Log progress every 10 items or at the end
        
    # TODO: Log completion


# TODO 6: Context Manager with Logging
class LoggedOperation:
    """
    Context manager that logs operation start and end.
    
    Should log:
    - Operation start (info level)
    - Operation success with duration (info level)
    - Operation failure with duration (error level)
    """
    
    def __init__(self, operation_name):
        self.operation_name = operation_name
        self.logger = logging.getLogger('myapp.operations')
        self.start_time = None
    
    def __enter__(self):
        # TODO: Log operation start and record start time
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Calculate duration and log completion or failure
        pass


# TODO 7: Custom Formatter
class CustomFormatter(logging.Formatter):
    """
    Custom formatter that adds color to console output.
    
    Colors:
    - DEBUG: Blue
    - INFO: Green
    - WARNING: Yellow
    - ERROR: Red
    - CRITICAL: Red background
    """
    
    # ANSI color codes
    COLORS = {
        'DEBUG': '\033[94m',    # Blue
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[41m', # Red background
        'ENDC': '\033[0m'       # End color
    }
    
    def format(self, record):
        # TODO: Implement custom formatting with colors
        # Hint: Use self.COLORS to add color codes
        pass


# TODO 8: JSON Logging
class JSONFormatter(logging.Formatter):
    """
    Formatter that outputs log records as JSON.
    
    Should include:
    - timestamp (ISO format)
    - level
    - logger name
    - message
    - module
    - function
    - line number
    """
    
    def format(self, record):
        # TODO: Create a dictionary with log information
        log_entry = {}
        
        # TODO: Convert to JSON string
        return ""


# TODO 9: Logging Decorator
def log_function_calls(logger_name=None):
    """
    Decorator that logs function calls and returns.
    
    Should log:
    - Function entry with arguments (debug level)
    - Function exit with return value (debug level)
    - Exceptions (error level)
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # TODO: Get logger (use logger_name or func.__module__)
            logger = None
            
            # TODO: Log function entry
            
            try:
                # TODO: Call function and log return
                result = func(*args, **kwargs)
                # TODO: Log successful return
                return result
            except Exception as e:
                # TODO: Log exception
                raise
        
        return wrapper
    return decorator


# TODO 10: Configuration from Dictionary
def setup_logging_from_config():
    """
    Set up logging using dictionary configuration.
    
    Create a configuration that:
    - Has loggers for 'myapp', 'myapp.math', 'myapp.file'
    - Uses both console and file handlers
    - Has different log levels for different loggers
    """
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            # TODO: Define formatters
        },
        'handlers': {
            # TODO: Define handlers
        },
        'loggers': {
            # TODO: Define loggers
        }
    }
    
    # TODO: Apply configuration
    pass


# Test functions - DO NOT MODIFY
def test_basic_logging():
    """Test basic logging configuration."""
    print("\n=== Testing Basic Logging ===")
    configure_basic_logging()
    
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")


def test_advanced_logging():
    """Test advanced logging with file and console output."""
    print("\n=== Testing Advanced Logging ===")
    logger = configure_advanced_logging()
    
    if logger:
        logger.debug("Debug message - should only appear in file")
        logger.info("Info message - should only appear in file")
        logger.warning("Warning message - should appear in both")
        logger.error("Error message - should appear in both")


def test_factorial_logging():
    """Test factorial function with logging."""
    print("\n=== Testing Factorial with Logging ===")
    try:
        result = calculate_factorial(5)
        print(f"Factorial result: {result}")
        
        # Test error case
        calculate_factorial(-1)
    except ValueError as e:
        print(f"Caught expected error: {e}")


def test_file_reader_logging():
    """Test file reader with logging."""
    print("\n=== Testing File Reader with Logging ===")
    
    # Test with existing file
    try:
        content = safe_file_reader(__file__)
        print(f"Read {len(content)} characters from file")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    # Test with non-existent file
    try:
        safe_file_reader("nonexistent_file.txt")
    except FileNotFoundError:
        print("Caught expected FileNotFoundError")


def test_progress_logging():
    """Test progress logging."""
    print("\n=== Testing Progress Logging ===")
    items = list(range(25))  # 25 items to process
    process_items(items)


def test_context_manager():
    """Test logging context manager."""
    print("\n=== Testing Context Manager ===")
    
    # Successful operation
    with LoggedOperation("successful task"):
        time.sleep(0.1)
        print("Task completed successfully")
    
    # Failed operation
    try:
        with LoggedOperation("failing task"):
            time.sleep(0.1)
            raise ValueError("Something went wrong")
    except ValueError:
        print("Caught expected error")


@log_function_calls('myapp.test')
def sample_function(x, y):
    """Sample function to test the logging decorator."""
    return x + y


def test_decorator():
    """Test the logging decorator."""
    print("\n=== Testing Logging Decorator ===")
    result = sample_function(3, 4)
    print(f"Function result: {result}")


def main():
    """Main function to run all tests."""
    print("LOGGING PRACTICE EXERCISES")
    print("=" * 50)
    
    # Run tests
    test_basic_logging()
    test_advanced_logging()
    test_factorial_logging()
    test_file_reader_logging()
    test_progress_logging()
    test_context_manager()
    test_decorator()
    
    print("\n" + "=" * 50)
    print("Complete the TODO sections to see proper logging output!")
    print("Check 'app.log' file for file-based logging output.")


if __name__ == "__main__":
    main()