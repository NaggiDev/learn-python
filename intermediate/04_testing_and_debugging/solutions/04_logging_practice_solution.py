"""
Solution: Logging Practice

This file contains the completed solutions for the logging exercise.
"""

import logging
import logging.config
import time
import json
from datetime import datetime
from functools import wraps


# Solution 1: Basic Logging Configuration
def configure_basic_logging():
    """Configure basic logging for the application."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


# Solution 2: File and Console Logging
def configure_advanced_logging():
    """
    Configure logging to output to both console and file.
    
    Requirements:
    - Console: WARNING level and above, simple format
    - File: DEBUG level and above, detailed format
    - File name: 'app.log'
    """
    # Create a logger named 'myapp'
    logger = logging.getLogger('myapp')
    logger.setLevel(logging.DEBUG)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Create console handler (WARNING level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    
    # Create file handler (DEBUG level)
    file_handler = logging.FileHandler('app.log', mode='w')
    file_handler.setLevel(logging.DEBUG)
    
    # Create formatters
    console_format = logging.Formatter('%(levelname)s - %(message)s')
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Set formatters and add handlers to logger
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger


# Solution 3: Function with Logging
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
    
    # Log function entry
    logger.debug(f"calculate_factorial called with n={n}")
    
    # Validate input and log errors
    if n < 0:
        logger.error(f"Invalid input: factorial not defined for negative numbers (n={n})")
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        logger.debug(f"Base case: factorial({n}) = 1")
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
        logger.debug(f"Step {i}: result = {result}")
    
    # Log final result
    logger.info(f"Calculated factorial({n}) = {result}")
    return result


# Solution 4: Error Handling with Logging
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
    
    # Log attempt to read file
    logger.info(f"Attempting to read file: {filename}")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Log successful read
            logger.info(f"Successfully read {len(content)} characters from {filename}")
            return content
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        raise
    except PermissionError:
        logger.error(f"Permission denied when reading file: {filename}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected error reading file {filename}: {type(e).__name__}: {e}")
        raise


# Solution 5: Progress Logging
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
    
    total = len(items)
    logger.info(f"Starting to process {total} items")
    
    for i, item in enumerate(items, 1):
        # Log individual item processing (debug)
        logger.debug(f"Processing item {i}/{total}: {item}")
        
        # Simulate processing time
        time.sleep(0.01)
        
        # Log progress every 10 items or at the end
        if i % 10 == 0 or i == total:
            percentage = (i / total) * 100
            logger.info(f"Progress: {i}/{total} items processed ({percentage:.1f}%)")
    
    # Log completion
    logger.info(f"Completed processing all {total} items")


# Solution 6: Context Manager with Logging
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
        # Log operation start and record start time
        self.start_time = time.time()
        self.logger.info(f"Starting operation: {self.operation_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Calculate duration and log completion or failure
        duration = time.time() - self.start_time
        
        if exc_type is None:
            # Operation succeeded
            self.logger.info(f"Operation '{self.operation_name}' completed successfully in {duration:.3f} seconds")
        else:
            # Operation failed
            self.logger.error(f"Operation '{self.operation_name}' failed after {duration:.3f} seconds: {exc_type.__name__}: {exc_val}")
        
        # Don't suppress the exception
        return False


# Solution 7: Custom Formatter
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
        # Get the original formatted message
        original_format = super().format(record)
        
        # Add color codes
        color = self.COLORS.get(record.levelname, '')
        end_color = self.COLORS['ENDC']
        
        return f"{color}{original_format}{end_color}"


# Solution 8: JSON Logging
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
        # Create a dictionary with log information
        log_entry = {
            'timestamp': datetime.utcfromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Convert to JSON string
        return json.dumps(log_entry)


# Solution 9: Logging Decorator
def log_function_calls(logger_name=None):
    """
    Decorator that logs function calls and returns.
    
    Should log:
    - Function entry with arguments (debug level)
    - Function exit with return value (debug level)
    - Exceptions (error level)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get logger (use logger_name or func.__module__)
            logger = logging.getLogger(logger_name or func.__module__)
            
            # Log function entry
            logger.debug(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            
            try:
                # Call function and log return
                result = func(*args, **kwargs)
                logger.debug(f"{func.__name__} returned {result}")
                return result
            except Exception as e:
                # Log exception
                logger.error(f"{func.__name__} raised {type(e).__name__}: {e}")
                raise
        
        return wrapper
    return decorator


# Solution 10: Configuration from Dictionary
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
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'simple': {
                'format': '%(levelname)s - %(message)s'
            },
            'json': {
                '()': JSONFormatter,
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'WARNING',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'standard',
                'filename': 'app_config.log',
                'mode': 'w'
            },
            'json_file': {
                'class': 'logging.FileHandler',
                'level': 'INFO',
                'formatter': 'json',
                'filename': 'app_json.log',
                'mode': 'w'
            }
        },
        'loggers': {
            'myapp': {
                'level': 'DEBUG',
                'handlers': ['console', 'file'],
                'propagate': False
            },
            'myapp.math': {
                'level': 'DEBUG',
                'handlers': ['console', 'file', 'json_file'],
                'propagate': False
            },
            'myapp.file': {
                'level': 'INFO',
                'handlers': ['console', 'file'],
                'propagate': False
            }
        }
    }
    
    # Apply configuration
    logging.config.dictConfig(config)


# Test functions - Same as original but with solutions working
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


def test_custom_formatter():
    """Test custom color formatter."""
    print("\n=== Testing Custom Formatter ===")
    
    # Create logger with custom formatter
    logger = logging.getLogger('color_test')
    logger.setLevel(logging.DEBUG)
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Create handler with custom formatter
    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter('%(levelname)s - %(message)s'))
    logger.addHandler(handler)
    
    logger.debug("This should be blue")
    logger.info("This should be green")
    logger.warning("This should be yellow")
    logger.error("This should be red")
    logger.critical("This should have red background")


def test_json_logging():
    """Test JSON formatter."""
    print("\n=== Testing JSON Logging ===")
    
    # Create logger with JSON formatter
    logger = logging.getLogger('json_test')
    logger.setLevel(logging.DEBUG)
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Create handler with JSON formatter
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    
    logger.info("This is a JSON formatted log message")
    logger.error("This is a JSON formatted error message")


def test_config_logging():
    """Test dictionary configuration."""
    print("\n=== Testing Dictionary Configuration ===")
    setup_logging_from_config()
    
    # Test different loggers
    main_logger = logging.getLogger('myapp')
    math_logger = logging.getLogger('myapp.math')
    file_logger = logging.getLogger('myapp.file')
    
    main_logger.info("Main logger message")
    math_logger.debug("Math logger debug message")
    file_logger.warning("File logger warning message")


def main():
    """Main function to run all tests."""
    print("LOGGING PRACTICE EXERCISES - SOLUTIONS")
    print("=" * 50)
    
    # Run tests
    test_basic_logging()
    test_advanced_logging()
    test_factorial_logging()
    test_file_reader_logging()
    test_progress_logging()
    test_context_manager()
    test_decorator()
    test_custom_formatter()
    test_json_logging()
    test_config_logging()
    
    print("\n" + "=" * 50)
    print("All logging exercises completed!")
    print("Check the following files for logging output:")
    print("- app.log (advanced logging)")
    print("- app_config.log (dictionary config)")
    print("- app_json.log (JSON formatted logs)")
    print("=" * 50)


if __name__ == "__main__":
    main()