# Logging in Python

## Introduction

Logging is the practice of recording events that occur during program execution. Unlike print statements, which are temporary debugging aids, logging provides a permanent, configurable way to track what your application is doing. Proper logging is essential for debugging, monitoring, and maintaining applications in production.

## Why Use Logging Instead of Print?

### Problems with Print Statements
- **No control over output**: All prints go to stdout
- **No filtering**: Can't easily turn off debug prints in production
- **No formatting**: Limited control over message format
- **No persistence**: Output is lost when program ends
- **Performance impact**: Always executed, even when not needed

### Benefits of Logging
- **Configurable levels**: Control what gets logged
- **Multiple outputs**: Log to files, console, remote servers
- **Structured format**: Consistent, parseable output
- **Performance**: Can be disabled without code changes
- **Production ready**: Designed for long-running applications

## Python's Logging Module

Python's built-in `logging` module provides a flexible logging system:

```python
import logging

# Basic logging
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
```

## Log Levels

Logging uses hierarchical levels to categorize messages:

| Level | Numeric Value | When to Use |
|-------|---------------|-------------|
| DEBUG | 10 | Detailed diagnostic information |
| INFO | 20 | General information about program flow |
| WARNING | 30 | Something unexpected happened, but program continues |
| ERROR | 40 | Serious problem occurred, some functionality failed |
| CRITICAL | 50 | Very serious error, program may not continue |

### Level Hierarchy
When you set a logging level, all messages at that level and above are shown:

```python
import logging

# Set logging level to WARNING
logging.basicConfig(level=logging.WARNING)

logging.debug("This won't be shown")     # Below WARNING
logging.info("This won't be shown")      # Below WARNING
logging.warning("This will be shown")    # WARNING level
logging.error("This will be shown")      # Above WARNING
logging.critical("This will be shown")   # Above WARNING
```

## Basic Configuration

### Simple Configuration
```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Application started")
logging.debug("Debug information")
```

### Configuration Options
```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w'  # 'w' to overwrite, 'a' to append
)
```

## Format Strings

Common format attributes:

| Attribute | Description |
|-----------|-------------|
| `%(asctime)s` | Human-readable time |
| `%(name)s` | Logger name |
| `%(levelname)s` | Log level name |
| `%(message)s` | The log message |
| `%(filename)s` | Filename where log was called |
| `%(lineno)d` | Line number where log was called |
| `%(funcName)s` | Function name where log was called |

### Example Format Strings
```python
# Simple format
format='%(levelname)s: %(message)s'
# Output: INFO: Application started

# Detailed format
format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
# Output: 2023-12-07 10:30:45 - myapp - INFO - main.py:15 - Application started

# Custom format
format='[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s'
# Output: [2023-12-07 10:30:45] INFO     myapp        Application started
```

## Loggers, Handlers, and Formatters

### Logger Hierarchy
```python
import logging

# Create loggers
logger = logging.getLogger('myapp')
db_logger = logging.getLogger('myapp.database')
api_logger = logging.getLogger('myapp.api')

# Logger hierarchy: myapp is parent of myapp.database and myapp.api
```

### Creating Custom Loggers
```python
import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

# Set levels for handlers
console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

# Create formatters
console_format = logging.Formatter('%(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatters to handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Use the logger
logger.debug("This goes to file only")
logger.warning("This goes to both console and file")
```

## Practical Logging Examples

### Application Startup and Shutdown
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Application starting")
    
    try:
        # Application logic here
        process_data()
        logging.info("Data processing completed successfully")
        
    except Exception as e:
        logging.error(f"Application failed: {e}")
        raise
    finally:
        logging.info("Application shutting down")

def process_data():
    logging.debug("Starting data processing")
    # Processing logic
    logging.debug("Data processing finished")
```

### Function Entry and Exit
```python
import logging
from functools import wraps

def log_function_call(func):
    """Decorator to log function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.debug(f"{func.__name__} returned {result}")
            return result
        except Exception as e:
            logging.error(f"{func.__name__} raised {type(e).__name__}: {e}")
            raise
    return wrapper

@log_function_call
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```

### Error Handling with Logging
```python
import logging

def safe_divide(a, b):
    """Divide two numbers with proper error logging."""
    try:
        logging.debug(f"Attempting to divide {a} by {b}")
        
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
        
    except (TypeError, ValueError) as e:
        logging.error(f"Division failed: {e}")
        raise
    except Exception as e:
        logging.critical(f"Unexpected error in division: {e}")
        raise
```

### Progress Tracking
```python
import logging
import time

def process_items(items):
    """Process a list of items with progress logging."""
    total = len(items)
    logging.info(f"Starting to process {total} items")
    
    for i, item in enumerate(items, 1):
        try:
            # Simulate processing
            time.sleep(0.1)
            process_single_item(item)
            
            # Log progress every 10 items or at the end
            if i % 10 == 0 or i == total:
                logging.info(f"Processed {i}/{total} items ({i/total*100:.1f}%)")
                
        except Exception as e:
            logging.error(f"Failed to process item {i}: {item} - {e}")
            continue
    
    logging.info("Processing completed")

def process_single_item(item):
    """Process a single item."""
    logging.debug(f"Processing item: {item}")
    # Processing logic here
```

## Configuration Files

### Using Configuration Files
Create a `logging.conf` file:

```ini
[loggers]
keys=root,myapp

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter,detailedFormatter

[logger_root]
level=WARNING
handlers=consoleHandler

[logger_myapp]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=myapp
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=WARNING
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=detailedFormatter
args=('app.log', 'w')

[formatter_simpleFormatter]
format=%(levelname)s - %(message)s

[formatter_detailedFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

Load the configuration:
```python
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('myapp')

logger.info("Application started")
```

### Dictionary Configuration
```python
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'simple': {
            'format': '%(levelname)s - %(message)s'
        },
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
            'filename': 'app.log',
            'mode': 'w',
        },
    },
    'loggers': {
        'myapp': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('myapp')
```

## Advanced Logging Techniques

### Rotating Log Files
```python
import logging
from logging.handlers import RotatingFileHandler

# Create logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# Create rotating file handler
# maxBytes: maximum size before rotation
# backupCount: number of backup files to keep
handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
```

### Time-based Rotation
```python
import logging
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',  # Rotate at midnight
    interval=1,       # Every 1 day
    backupCount=7     # Keep 7 days of logs
)
```

### Structured Logging with JSON
```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        return json.dumps(log_entry)

# Use JSON formatter
logger = logging.getLogger('myapp')
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info("This is a JSON log message")
```

### Context Managers for Logging
```python
import logging
from contextlib import contextmanager

@contextmanager
def log_context(operation_name):
    """Context manager for logging operation start and end."""
    logger = logging.getLogger(__name__)
    logger.info(f"Starting {operation_name}")
    start_time = time.time()
    
    try:
        yield
        duration = time.time() - start_time
        logger.info(f"Completed {operation_name} in {duration:.2f} seconds")
    except Exception as e:
        duration = time.time() - start_time
        logger.error(f"Failed {operation_name} after {duration:.2f} seconds: {e}")
        raise

# Usage
with log_context("data processing"):
    # Your code here
    process_data()
```

## Best Practices

### 1. Use Appropriate Log Levels
```python
# Good
logging.debug("User input validation details")
logging.info("User logged in successfully")
logging.warning("Deprecated API endpoint used")
logging.error("Database connection failed")
logging.critical("System out of memory")

# Avoid
logging.error("User clicked button")  # Too high level
logging.debug("System crashed")       # Too low level
```

### 2. Include Relevant Context
```python
# Good
logging.error(f"Failed to process user {user_id}: {error_message}")
logging.info(f"Processing batch {batch_id} with {len(items)} items")

# Less helpful
logging.error("Processing failed")
logging.info("Processing items")
```

### 3. Use Logger Names Effectively
```python
# Good - use module names
logger = logging.getLogger(__name__)

# Good - use hierarchical names
db_logger = logging.getLogger('myapp.database')
api_logger = logging.getLogger('myapp.api')
auth_logger = logging.getLogger('myapp.auth')
```

### 4. Don't Log Sensitive Information
```python
# Bad
logging.info(f"User login: username={username}, password={password}")

# Good
logging.info(f"User login attempt: username={username}")
logging.info(f"Login successful for user {username}")
```

### 5. Use Lazy Formatting
```python
# Good - formatting only happens if message is logged
logging.debug("Processing item %s with value %s", item_id, item_value)

# Less efficient - formatting always happens
logging.debug(f"Processing item {item_id} with value {item_value}")
```

## Testing with Logging

### Capturing Log Messages in Tests
```python
import logging
import unittest
from unittest.mock import patch

class TestLogging(unittest.TestCase):
    def test_function_logs_info(self):
        with self.assertLogs('myapp', level='INFO') as cm:
            my_function()
        
        self.assertIn('Expected log message', cm.output[0])
    
    @patch('logging.Logger.error')
    def test_error_logging(self, mock_error):
        function_that_should_log_error()
        mock_error.assert_called_once()
```

## Performance Considerations

### Conditional Logging
```python
# Expensive operation only if debug logging is enabled
if logger.isEnabledFor(logging.DEBUG):
    expensive_debug_info = calculate_expensive_debug_info()
    logger.debug(f"Debug info: {expensive_debug_info}")
```

### Lazy Evaluation
```python
# Use % formatting for lazy evaluation
logger.debug("Processing %s items", len(items))

# Or use lazy formatting with custom objects
class LazyFormat:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def __str__(self):
        return self.func(*self.args, **self.kwargs)

logger.debug("Expensive calculation: %s", LazyFormat(expensive_calculation))
```

## Common Pitfalls

### 1. Logging in Loops Without Throttling
```python
# Bad - can generate too many log messages
for item in large_list:
    logging.info(f"Processing {item}")

# Better - log progress periodically
for i, item in enumerate(large_list):
    if i % 100 == 0:
        logging.info(f"Processed {i}/{len(large_list)} items")
```

### 2. Not Configuring Logging Early
```python
# Good - configure logging at application startup
def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    logger.info("Application started")
    # Rest of application
```

### 3. Mixing Print and Logging
```python
# Inconsistent - avoid mixing
print("Debug info")
logging.info("Application info")

# Consistent - use logging for everything
logging.debug("Debug info")
logging.info("Application info")
```

## Summary

Effective logging is crucial for maintaining and debugging applications:

- **Use appropriate log levels** for different types of messages
- **Configure logging early** in your application lifecycle
- **Include relevant context** in log messages
- **Use structured logging** for complex applications
- **Rotate log files** to manage disk space
- **Don't log sensitive information**
- **Test your logging** to ensure it works as expected
- **Consider performance** when logging frequently

Logging is an investment in the maintainability and debuggability of your code. Start with simple logging and gradually adopt more advanced techniques as your applications grow in complexity.

---

**Next**: [Code Quality Tools](04_code_quality_tools.md)