# Weather Analyzer - Starter Code

This is the starter code for the Intermediate Level Capstone Project: Weather Data Analysis Application. This project demonstrates intermediate Python concepts including object-oriented programming, functional programming, testing, and modular design.

## Project Structure

```
weather_analyzer/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── setup.py                 # Package setup configuration
├── .env.example             # Environment variables template
├── demo.py                  # Demonstration script
├── weather_analyzer/        # Main application package
│   ├── __init__.py
│   ├── main.py             # Command-line interface
│   ├── models/             # Data models
│   │   ├── __init__.py
│   │   ├── weather_data.py # Weather data model
│   │   └── location.py     # Location model
│   ├── services/           # External services
│   │   ├── __init__.py
│   │   ├── weather_api.py  # Weather API service
│   │   └── data_storage.py # Data storage service
│   ├── analysis/           # Data analysis
│   │   ├── __init__.py
│   │   ├── statistics.py   # Statistical analysis
│   │   └── trends.py       # Trend analysis
│   ├── visualization/      # Charts and reports
│   │   ├── __init__.py
│   │   └── charts.py       # Chart generation
│   └── utils/              # Utilities
│       ├── __init__.py
│       ├── config.py       # Configuration management
│       └── helpers.py      # Helper functions
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── test_models.py      # Model tests
│   ├── test_services.py    # Service tests
│   ├── test_analysis.py    # Analysis tests
│   └── test_integration.py # Integration tests
└── data/                   # Data storage
    ├── cache/              # API response cache
    └── reports/            # Generated reports
```

## Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API key (free registration at https://openweathermap.org/api)
- Internet connection for API access

### 2. Installation

1. Clone or download this starter code
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenWeatherMap API key
   ```

4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

### 3. Run the Demo

```bash
python demo.py
```

This will demonstrate the current capabilities and show you what needs to be implemented.

### 4. Run Tests

```bash
pytest
```

Note: Many tests will fail initially since the functionality is not yet implemented.

### 5. Use the Application

```bash
# Get current weather (not yet implemented)
python -m weather_analyzer current --city "London"

# Analyze weather trends (not yet implemented)
python -m weather_analyzer analyze --city "Paris" --days 5

# Compare multiple cities (not yet implemented)
python -m weather_analyzer compare --cities "London,Paris,Tokyo"

# Generate a report (not yet implemented)
python -m weather_analyzer report --city "Berlin" --output report.txt
```

## What's Implemented

The starter code provides:

### ✅ Complete Structure
- Full project organization with proper package structure
- Command-line interface framework
- Configuration management system
- Comprehensive test suite framework

### ✅ Data Models
- `WeatherData` class with all necessary fields
- `Location` and `Coordinates` classes
- Proper data validation and type hints
- String representations and utility methods

### ✅ Service Framework
- `WeatherAPIService` class structure with error handling
- `DataStorage` class for caching and persistence
- Rate limiting and request management
- File-based storage system

### ✅ Analysis Framework
- `WeatherStatistics` class for statistical analysis
- `TrendAnalyzer` class for trend detection
- Method signatures for all required functionality
- Proper error handling structure

### ✅ Visualization Framework
- `ChartGenerator` class for text-based charts
- Report generation capabilities
- Formatting utilities
- Chart scaling and display methods

### ✅ Testing Infrastructure
- Unit tests for all major components
- Integration tests for component interaction
- Test fixtures and mock objects
- Comprehensive test coverage framework

## What You Need to Implement

The starter code contains many `TODO` comments and `NotImplementedError` exceptions. Here's what you need to complete:

### 🔧 Core API Integration
- [ ] Implement `WeatherAPIService.get_current_weather()`
- [ ] Implement `WeatherAPIService.get_weather_forecast()`
- [ ] Implement `WeatherAPIService.get_historical_weather()`
- [ ] Implement API response parsing in `WeatherData.from_api_response()`

### 🔧 Data Processing
- [ ] Complete `WeatherData` validation and utility methods
- [ ] Implement caching logic in `DataStorage`
- [ ] Complete CSV import/export functionality
- [ ] Implement data cleaning and validation

### 🔧 Statistical Analysis
- [ ] Complete all statistical calculation methods
- [ ] Implement anomaly detection algorithms
- [ ] Add seasonal pattern analysis
- [ ] Complete extreme value detection

### 🔧 Trend Analysis
- [ ] Implement moving average calculations
- [ ] Complete trend direction detection
- [ ] Add pattern recognition algorithms
- [ ] Implement simple forecasting

### 🔧 Visualization
- [ ] Complete text-based chart generation
- [ ] Implement data formatting and scaling
- [ ] Add comprehensive report generation
- [ ] Complete table formatting

### 🔧 Command-Line Interface
- [ ] Implement all command handlers in `main.py`
- [ ] Add interactive features
- [ ] Complete error handling and user feedback
- [ ] Add progress indicators

## Implementation Guidelines

### 1. Start with the Models
Begin by completing the `TODO` items in the model classes:
- Finish `WeatherData` validation methods
- Complete coordinate distance calculations
- Implement data conversion methods

### 2. Implement API Integration
Work on the `WeatherAPIService`:
- Start with `get_current_weather()`
- Add proper error handling
- Implement response parsing
- Add caching integration

### 3. Add Statistical Analysis
Complete the analysis modules:
- Start with basic statistics (mean, median, etc.)
- Add more complex analysis methods
- Implement trend detection
- Add pattern recognition

### 4. Build Visualization
Work on the chart generation:
- Start with simple text-based charts
- Add data scaling and formatting
- Implement comprehensive reports
- Add export capabilities

### 5. Complete the CLI
Finish the command-line interface:
- Implement command handlers
- Add user interaction
- Complete error handling
- Add help and documentation

## Testing Strategy

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_models.py

# Run with coverage
pytest --cov=weather_analyzer

# Run with verbose output
pytest -v
```

### Test-Driven Development
1. Read the test cases to understand expected behavior
2. Implement the functionality to make tests pass
3. Add additional tests for edge cases
4. Refactor and improve the implementation

### Mock Testing
The test suite includes examples of mocking external services:
- API responses are mocked for testing
- File system operations are tested with temporary directories
- Network errors are simulated for error handling tests

## Configuration

### Environment Variables
Create a `.env` file with:
```
WEATHER_API_KEY=your_openweathermap_api_key_here
WEATHER_API_BASE_URL=https://api.openweathermap.org/data/2.5
LOG_LEVEL=INFO
CACHE_DURATION=3600
DATA_DIR=data
```

### API Key Setup
1. Go to https://openweathermap.org/api
2. Sign up for a free account
3. Generate an API key
4. Add it to your `.env` file

## Common Issues and Solutions

### Import Errors
If you get import errors:
```bash
# Install in development mode
pip install -e .

# Or add to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### API Key Issues
- Make sure your API key is valid and active
- Check that the `.env` file is in the correct location
- Verify the API key has the necessary permissions

### Test Failures
- Many tests will fail initially - this is expected
- Implement the functionality to make tests pass
- Some tests are placeholders and need to be completed

### Permission Errors
- Make sure the `data/` directory is writable
- Check file permissions if you get access errors
- Use absolute paths if relative paths cause issues

## Learning Objectives Checklist

As you work through this project, you should demonstrate:

### Object-Oriented Programming
- [ ] Class design and inheritance
- [ ] Encapsulation and data hiding
- [ ] Polymorphism and method overriding
- [ ] Composition and aggregation

### Functional Programming
- [ ] Higher-order functions
- [ ] Lambda functions and closures
- [ ] Map, filter, and reduce operations
- [ ] Immutable data structures

### Testing and Quality
- [ ] Unit testing with pytest
- [ ] Integration testing
- [ ] Mocking and test fixtures
- [ ] Code coverage analysis

### Modular Design
- [ ] Package and module organization
- [ ] Import management
- [ ] Dependency injection
- [ ] Configuration management

### Error Handling
- [ ] Exception handling strategies
- [ ] Custom exception classes
- [ ] Graceful error recovery
- [ ] User-friendly error messages

### External Integration
- [ ] REST API consumption
- [ ] Data serialization/deserialization
- [ ] Caching strategies
- [ ] Rate limiting

## Resources

### Python Documentation
- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Type Hints](https://docs.python.org/3/library/typing.html)

### Libraries Used
- [Requests Documentation](https://docs.python-requests.org/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

### Weather API
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [API Response Examples](https://openweathermap.org/current)

### Testing Resources
- [Python Testing 101](https://realpython.com/python-testing/)
- [Pytest Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)
- [Mocking in Python](https://realpython.com/python-mock-library/)

## Getting Help

If you get stuck:

1. **Read the TODO comments** - They provide specific guidance
2. **Check the test cases** - They show expected behavior
3. **Run the demo script** - It shows what should work
4. **Look at the documentation** - Links are provided above
5. **Start small** - Implement one method at a time
6. **Use the debugger** - Step through your code to understand issues

## Next Steps

Once you complete the basic implementation:

1. **Add advanced features** from the extension challenges
2. **Improve the user interface** with better formatting
3. **Add more sophisticated analysis** algorithms
4. **Implement web interface** using Flask
5. **Add machine learning** predictions
6. **Create a deployment** strategy

Good luck with your capstone project! Remember, this is your opportunity to demonstrate everything you've learned in the intermediate level.