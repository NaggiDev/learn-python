# Mini-Project: RESTful API Service

## Project Overview

Build a complete RESTful API service for a **Task Management System** that demonstrates all the concepts learned in the Web Development module. This project combines Flask, RESTful API design, database integration, and best practices for building production-ready web services.

## Learning Objectives

By completing this project, you will:

- Design and implement a complete RESTful API
- Use proper HTTP methods and status codes
- Implement database models with relationships
- Handle authentication and authorization
- Implement comprehensive error handling
- Write API documentation
- Create automated tests
- Follow web development best practices

## Project Requirements

### Core Features

1. **User Management**
   - User registration and authentication
   - User profiles and preferences
   - Role-based access control (Admin, User)

2. **Task Management**
   - Create, read, update, delete tasks
   - Task categories and priorities
   - Task assignment and collaboration
   - Task status tracking (Todo, In Progress, Done)

3. **Project Management**
   - Create and manage projects
   - Assign tasks to projects
   - Project collaboration and permissions

4. **API Features**
   - RESTful endpoints with proper HTTP methods
   - JSON request/response format
   - Pagination for list endpoints
   - Filtering and sorting capabilities
   - Comprehensive error handling

### Technical Requirements

1. **Framework**: Flask with Flask-SQLAlchemy
2. **Database**: SQLite for development (easily configurable for production)
3. **Authentication**: JWT-based authentication
4. **Validation**: Request data validation
5. **Testing**: Unit tests for all endpoints
6. **Documentation**: API documentation with examples

## API Specification

### Authentication Endpoints

```
POST /api/auth/register    # User registration
POST /api/auth/login       # User login
POST /api/auth/logout      # User logout
GET  /api/auth/profile     # Get current user profile
PUT  /api/auth/profile     # Update user profile
```

### User Management Endpoints

```
GET    /api/users          # List users (Admin only)
GET    /api/users/{id}     # Get specific user
PUT    /api/users/{id}     # Update user (Admin or self)
DELETE /api/users/{id}     # Delete user (Admin only)
```

### Project Endpoints

```
GET    /api/projects       # List user's projects
POST   /api/projects       # Create new project
GET    /api/projects/{id}  # Get specific project
PUT    /api/projects/{id}  # Update project
DELETE /api/projects/{id}  # Delete project
GET    /api/projects/{id}/tasks  # Get project tasks
POST   /api/projects/{id}/members  # Add project member
DELETE /api/projects/{id}/members/{user_id}  # Remove member
```

### Task Endpoints

```
GET    /api/tasks          # List user's tasks
POST   /api/tasks          # Create new task
GET    /api/tasks/{id}     # Get specific task
PUT    /api/tasks/{id}     # Update task
DELETE /api/tasks/{id}     # Delete task
POST   /api/tasks/{id}/assign  # Assign task to user
PUT    /api/tasks/{id}/status  # Update task status
GET    /api/tasks/search   # Search tasks
```

### Category Endpoints

```
GET    /api/categories     # List categories
POST   /api/categories     # Create category
GET    /api/categories/{id}  # Get specific category
PUT    /api/categories/{id}  # Update category
DELETE /api/categories/{id}  # Delete category
```

## Database Schema

### Users Table
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- first_name
- last_name
- role (admin, user)
- is_active
- created_at
- updated_at

### Projects Table
- id (Primary Key)
- name
- description
- owner_id (Foreign Key to Users)
- is_active
- created_at
- updated_at

### Tasks Table
- id (Primary Key)
- title
- description
- status (todo, in_progress, done)
- priority (low, medium, high)
- due_date
- project_id (Foreign Key to Projects)
- assigned_to (Foreign Key to Users)
- created_by (Foreign Key to Users)
- category_id (Foreign Key to Categories)
- created_at
- updated_at

### Categories Table
- id (Primary Key)
- name (Unique)
- description
- color
- created_at

### Project Members Table (Many-to-Many)
- project_id (Foreign Key to Projects)
- user_id (Foreign Key to Users)
- role (owner, member, viewer)
- joined_at

## Implementation Steps

### Phase 1: Project Setup and Basic Structure
1. Set up Flask application with proper structure
2. Configure database and SQLAlchemy
3. Create basic models
4. Set up testing framework

### Phase 2: Authentication System
1. Implement user registration and login
2. Add JWT token generation and validation
3. Create authentication middleware
4. Add user profile management

### Phase 3: Core API Endpoints
1. Implement user management endpoints
2. Create project CRUD operations
3. Implement task management
4. Add category management

### Phase 4: Advanced Features
1. Add filtering and pagination
2. Implement search functionality
3. Add task assignment and collaboration
4. Create project member management

### Phase 5: Testing and Documentation
1. Write comprehensive unit tests
2. Create API documentation
3. Add error handling and validation
4. Performance optimization

## Starter Code Structure

```
task_management_api/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── task.py
│   │   └── category.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── projects.py
│   │   ├── tasks.py
│   │   └── categories.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── validation.py
│   │   └── helpers.py
│   └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_projects.py
│   ├── test_tasks.py
│   └── conftest.py
├── migrations/
├── requirements.txt
├── run.py
└── README.md
```

## Getting Started

1. **Clone or create the project structure**
2. **Install dependencies**:
   ```bash
   pip install flask flask-sqlalchemy flask-jwt-extended flask-cors pytest
   ```
3. **Set up environment variables**:
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   export JWT_SECRET_KEY=your-secret-key
   ```
4. **Initialize the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
5. **Run the application**:
   ```bash
   python run.py
   ```

## Testing

Run the test suite:
```bash
pytest tests/ -v
```

Run specific test files:
```bash
pytest tests/test_auth.py -v
```

## API Usage Examples

### Register a new user
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword"
  }'
```

### Create a project (with JWT token)
```bash
curl -X POST http://localhost:5000/api/projects \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "name": "My Project",
    "description": "A sample project for task management"
  }'
```

### Create a task
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "title": "Complete API documentation",
    "description": "Write comprehensive API documentation",
    "priority": "high",
    "project_id": 1,
    "category_id": 1,
    "due_date": "2024-02-15"
  }'
```

## Evaluation Criteria

Your project will be evaluated on:

1. **Functionality** (40%)
   - All required endpoints implemented
   - Proper HTTP methods and status codes
   - Authentication and authorization working
   - Database operations functioning correctly

2. **Code Quality** (25%)
   - Clean, readable, and well-organized code
   - Proper error handling
   - Input validation
   - Following Python and Flask best practices

3. **API Design** (20%)
   - RESTful design principles
   - Consistent response formats
   - Proper use of HTTP status codes
   - Good URL structure

4. **Testing** (15%)
   - Comprehensive test coverage
   - Tests for all major functionality
   - Edge cases covered
   - Tests pass consistently

## Bonus Features

If you complete the core requirements, consider adding:

1. **File Attachments**: Allow file uploads for tasks
2. **Task Comments**: Add commenting system for tasks
3. **Email Notifications**: Send email notifications for task assignments
4. **Task Dependencies**: Implement task dependencies
5. **Time Tracking**: Add time tracking for tasks
6. **API Rate Limiting**: Implement rate limiting for API endpoints
7. **Caching**: Add caching for frequently accessed data
8. **WebSocket Support**: Real-time updates for task changes

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-JWT-Extended Documentation](https://flask-jwt-extended.readthedocs.io/)
- [RESTful API Design Best Practices](https://restfulapi.net/)
- [HTTP Status Codes](https://httpstatuses.com/)

## Submission

When you complete the project:

1. Ensure all tests pass
2. Create a comprehensive README with setup instructions
3. Include API documentation with examples
4. Add comments to complex code sections
5. Test the API with a tool like Postman or curl

Good luck building your RESTful API service! This project will give you hands-on experience with all the concepts covered in the Web Development module.