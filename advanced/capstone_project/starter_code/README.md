# Data Analytics Dashboard - Starter Code

## Project Setup

This starter code provides the foundation for building the Data Analytics Dashboard capstone project. Follow the setup instructions below to get started.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for version control)

## Installation

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file with your configuration.

5. **Initialize the database:**
   ```bash
   python manage.py init-db
   ```

6. **Run the application:**
   ```bash
   python manage.py run
   ```

## Project Structure

```
starter_code/
├── app/                    # Main application package
│   ├── __init__.py        # Flask app factory
│   ├── models/            # Database models
│   ├── api/               # API blueprints
│   ├── auth/              # Authentication module
│   ├── core/              # Core business logic
│   ├── utils/             # Utility functions
│   └── static/            # Static files (CSS, JS)
├── tests/                 # Test suite
├── migrations/            # Database migrations
├── uploads/               # File upload directory
├── config.py              # Configuration settings
├── manage.py              # Management commands
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## Development Workflow

1. **Start with the models** - Define your database schema
2. **Implement authentication** - Set up user registration and login
3. **Build the API endpoints** - Create RESTful API for data operations
4. **Add data processing** - Implement analysis and visualization features
5. **Create the frontend** - Build the user interface
6. **Add background tasks** - Implement async processing
7. **Write tests** - Ensure code quality and reliability

## Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```

Run tests with coverage:
```bash
python -m pytest tests/ --cov=app --cov-report=html
```

## API Documentation

Once the application is running, visit:
- Swagger UI: http://localhost:5000/api/docs
- API endpoints: http://localhost:5000/api/

## Key Implementation Notes

- Follow PEP 8 style guidelines
- Use type hints for better code documentation
- Implement proper error handling
- Add logging for debugging and monitoring
- Write comprehensive tests for all functionality
- Document your API endpoints
- Use environment variables for configuration

## Next Steps

1. Review the project requirements in the main README.md
2. Study the provided starter code structure
3. Implement features incrementally, testing as you go
4. Refer to the advanced level modules for specific implementation guidance
5. Ask for help when needed - this is a challenging project!

Good luck with your capstone project!