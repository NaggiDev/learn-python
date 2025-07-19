# Task Management API - Starter Code

This is the starter code for the Task Management API mini-project. It provides a basic structure and some implemented functionality to help you get started.

## What's Included

### ✅ Implemented Features

1. **Application Structure**
   - Flask application factory pattern
   - Blueprint-based route organization
   - Configuration management for different environments
   - Database setup with SQLAlchemy

2. **Authentication System**
   - User registration and login
   - JWT token generation and validation
   - Password hashing and validation
   - User profile management
   - Role-based access control (admin/user)

3. **Category Management**
   - CRUD operations for task categories
   - Admin-only category management
   - Color coding for categories

4. **User Model**
   - Complete User model with relationships
   - Password management
   - Role and permission checking

5. **Utilities**
   - Input validation functions
   - Authentication decorators
   - Error handling

6. **Testing Framework**
   - Pytest configuration
   - Test fixtures
   - Authentication tests

### 🚧 TODO: Features to Implement

1. **Project Management**
   - Complete Project and ProjectMember models
   - Project CRUD operations
   - Project member management
   - Project access control

2. **Task Management**
   - Complete Task model
   - Task CRUD operations
   - Task assignment and status updates
   - Task search and filtering

3. **User Management**
   - User listing and management endpoints
   - User profile updates by admin

4. **Advanced Features**
   - Pagination for all list endpoints
   - Advanced filtering and sorting
   - Task due date notifications
   - File attachments (bonus)

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your configuration
```

### 3. Initialize Database

```bash
# The database will be created automatically when you run the app
python run.py
```

### 4. Test the API

```bash
# Register a new user
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPassword123!",
    "first_name": "Test",
    "last_name": "User"
  }'

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "TestPassword123!"
  }'

# Get categories (requires authentication)
curl -X GET http://localhost:5000/api/categories \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 5. Run Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_auth.py -v

# Run with coverage
pytest --cov=app tests/
```

## Project Structure

```
task_management_api/
├── app/
│   ├── __init__.py              # ✅ Application factory
│   ├── config.py                # ✅ Configuration classes
│   ├── models/
│   │   ├── __init__.py          # ✅ Models package
│   │   ├── user.py              # ✅ User model (complete)
│   │   ├── category.py          # ✅ Category model (complete)
│   │   ├── project.py           # 🚧 Project models (TODO)
│   │   └── task.py              # 🚧 Task model (TODO)
│   ├── api/
│   │   ├── __init__.py          # ✅ API package
│   │   ├── auth.py              # ✅ Authentication routes (complete)
│   │   ├── categories.py        # ✅ Category routes (complete)
│   │   ├── users.py             # 🚧 User routes (TODO)
│   │   ├── projects.py          # 🚧 Project routes (TODO)
│   │   └── tasks.py             # 🚧 Task routes (TODO)
│   └── utils/
│       ├── __init__.py          # ✅ Utils package
│       ├── validation.py        # ✅ Validation functions
│       └── auth.py              # ✅ Auth utilities
├── tests/
│   ├── __init__.py              # ✅ Tests package
│   ├── conftest.py              # ✅ Test configuration
│   ├── test_auth.py             # ✅ Auth tests (complete)
│   ├── test_users.py            # 🚧 User tests (TODO)
│   ├── test_projects.py         # 🚧 Project tests (TODO)
│   └── test_tasks.py            # 🚧 Task tests (TODO)
├── requirements.txt             # ✅ Dependencies
├── run.py                       # ✅ Application entry point
├── .env.example                 # ✅ Environment template
└── README.md                    # ✅ This file
```

## Implementation Guide

### Step 1: Complete the Models

1. **Project Model** (`app/models/project.py`)
   - Add all required fields
   - Set up relationships with User and Task
   - Add helper methods

2. **Task Model** (`app/models/task.py`)
   - Add all required fields
   - Set up relationships with Project, User, and Category
   - Add status and priority enums

3. **ProjectMember Model** (`app/models/project.py`)
   - Complete the many-to-many relationship
   - Add role management

### Step 2: Implement API Endpoints

1. **User Management** (`app/api/users.py`)
   - List users (admin only)
   - Get user details
   - Update user (admin or self)
   - Delete user (admin only)

2. **Project Management** (`app/api/projects.py`)
   - CRUD operations for projects
   - Project member management
   - Access control

3. **Task Management** (`app/api/tasks.py`)
   - CRUD operations for tasks
   - Task assignment
   - Status updates
   - Search and filtering

### Step 3: Add Tests

Write comprehensive tests for all new endpoints and functionality.

### Step 4: Add Advanced Features

- Pagination
- Advanced filtering
- File uploads
- Email notifications

## Available Endpoints

### Authentication (✅ Complete)
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `GET /api/auth/profile` - Get user profile
- `PUT /api/auth/profile` - Update user profile
- `POST /api/auth/refresh` - Refresh access token

### Categories (✅ Complete)
- `GET /api/categories` - List categories
- `POST /api/categories` - Create category (admin)
- `GET /api/categories/<id>` - Get category
- `PUT /api/categories/<id>` - Update category (admin)
- `DELETE /api/categories/<id>` - Delete category (admin)

### Users (🚧 TODO)
- `GET /api/users` - List users (admin)
- `GET /api/users/<id>` - Get user
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user (admin)

### Projects (🚧 TODO)
- `GET /api/projects` - List user's projects
- `POST /api/projects` - Create project
- `GET /api/projects/<id>` - Get project
- `PUT /api/projects/<id>` - Update project
- `DELETE /api/projects/<id>` - Delete project
- `GET /api/projects/<id>/tasks` - Get project tasks
- `POST /api/projects/<id>/members` - Add member
- `DELETE /api/projects/<id>/members/<user_id>` - Remove member

### Tasks (🚧 TODO)
- `GET /api/tasks` - List user's tasks
- `POST /api/tasks` - Create task
- `GET /api/tasks/<id>` - Get task
- `PUT /api/tasks/<id>` - Update task
- `DELETE /api/tasks/<id>` - Delete task
- `POST /api/tasks/<id>/assign` - Assign task
- `PUT /api/tasks/<id>/status` - Update status
- `GET /api/tasks/search` - Search tasks

## Tips for Implementation

1. **Follow the Existing Patterns**
   - Look at the auth and categories implementations
   - Use the same error handling patterns
   - Follow the same response format

2. **Use the Utility Functions**
   - Validation functions in `app/utils/validation.py`
   - Authentication decorators in `app/utils/auth.py`

3. **Write Tests First**
   - Follow TDD approach
   - Use the existing test fixtures
   - Test both success and error cases

4. **Handle Permissions Carefully**
   - Use the provided authentication decorators
   - Check user permissions for each operation
   - Ensure users can only access their own data

## Need Help?

- Check the existing implementations for patterns
- Review the requirements in the main README
- Look at the test files for expected behavior
- Use the validation utilities for input checking

Good luck with your implementation! 🚀