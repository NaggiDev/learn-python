# RESTful APIs: Building Web Services with Flask

## Introduction

REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful APIs provide a standardized way for different systems to communicate over HTTP. In this lesson, you'll learn how to design and implement RESTful APIs using Flask.

## What is REST?

REST is based on several key principles:

1. **Stateless**: Each request contains all information needed to process it
2. **Client-Server**: Clear separation between client and server
3. **Cacheable**: Responses should be cacheable when appropriate
4. **Uniform Interface**: Consistent way to interact with resources
5. **Layered System**: Architecture can be composed of hierarchical layers
6. **Code on Demand** (optional): Server can send executable code to client

## REST Principles in Practice

### Resources and URIs

In REST, everything is a resource identified by a URI:

```
/users          # Collection of users
/users/123      # Specific user with ID 123
/users/123/posts # Posts belonging to user 123
/posts          # Collection of posts
/posts/456      # Specific post with ID 456
```

### HTTP Methods (Verbs)

RESTful APIs use HTTP methods to indicate the desired action:

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Retrieve resource(s) | `GET /users` |
| POST | Create new resource | `POST /users` |
| PUT | Update/replace entire resource | `PUT /users/123` |
| PATCH | Partially update resource | `PATCH /users/123` |
| DELETE | Remove resource | `DELETE /users/123` |

### HTTP Status Codes

Use appropriate status codes to indicate the result:

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Resource conflict |
| 422 | Unprocessable Entity | Validation errors |
| 500 | Internal Server Error | Server error |

## Building RESTful APIs with Flask

### Basic API Structure

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample data (in production, use a database)
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'created_at': '2024-01-01'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'created_at': '2024-01-02'}
]

# GET /users - List all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

# GET /users/<id> - Get specific user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# POST /users - Create new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Validation
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400
    
    # Create new user
    new_user = {
        'id': max(u['id'] for u in users) + 1 if users else 1,
        'name': data['name'],
        'email': data['email'],
        'created_at': datetime.now().isoformat()
    }
    users.append(new_user)
    
    return jsonify(new_user), 201

# PUT /users/<id> - Update entire user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400
    
    user['name'] = data['name']
    user['email'] = data['email']
    user['updated_at'] = datetime.now().isoformat()
    
    return jsonify(user)

# PATCH /users/<id> - Partially update user
@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Update only provided fields
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']
    
    user['updated_at'] = datetime.now().isoformat()
    
    return jsonify(user)

# DELETE /users/<id> - Delete user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    users = [u for u in users if u['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```

## Advanced API Features

### Request Validation

```python
from flask import Flask, request, jsonify
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_user_data(data, required_fields=None):
    errors = []
    
    if required_fields:
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f'{field} is required')
    
    if 'email' in data and not validate_email(data['email']):
        errors.append('Invalid email format')
    
    if 'name' in data and len(data['name']) < 2:
        errors.append('Name must be at least 2 characters long')
    
    return errors

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Validate required fields
    errors = validate_user_data(data, required_fields=['name', 'email'])
    if errors:
        return jsonify({'errors': errors}), 422
    
    # Create user logic here...
```

### Pagination

```python
@app.route('/api/users', methods=['GET'])
def get_users():
    # Get pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Validate pagination parameters
    if page < 1:
        page = 1
    if per_page < 1 or per_page > 100:
        per_page = 10
    
    # Calculate pagination
    start = (page - 1) * per_page
    end = start + per_page
    paginated_users = users[start:end]
    
    # Build response
    response = {
        'users': paginated_users,
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': len(users),
            'pages': (len(users) + per_page - 1) // per_page
        }
    }
    
    return jsonify(response)
```

### Filtering and Sorting

```python
@app.route('/api/users', methods=['GET'])
def get_users():
    # Get query parameters
    name_filter = request.args.get('name')
    email_filter = request.args.get('email')
    sort_by = request.args.get('sort', 'id')
    sort_order = request.args.get('order', 'asc')
    
    # Start with all users
    filtered_users = users.copy()
    
    # Apply filters
    if name_filter:
        filtered_users = [u for u in filtered_users 
                         if name_filter.lower() in u['name'].lower()]
    
    if email_filter:
        filtered_users = [u for u in filtered_users 
                         if email_filter.lower() in u['email'].lower()]
    
    # Apply sorting
    reverse = sort_order.lower() == 'desc'
    if sort_by in ['id', 'name', 'email']:
        filtered_users.sort(key=lambda x: x[sort_by], reverse=reverse)
    
    return jsonify({'users': filtered_users})
```

### Error Handling

```python
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({
        'error': e.name,
        'message': e.description,
        'status_code': e.code
    }), e.code

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f'Unhandled exception: {e}')
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred'
    }), 500

# Custom error responses
def not_found_error(message="Resource not found"):
    return jsonify({'error': message}), 404

def validation_error(errors):
    return jsonify({'error': 'Validation failed', 'details': errors}), 422

def conflict_error(message="Resource conflict"):
    return jsonify({'error': message}), 409
```

### Content Negotiation

```python
from flask import request, jsonify

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return not_found_error()
    
    # Check Accept header
    if request.headers.get('Accept') == 'application/xml':
        # Return XML format (simplified example)
        xml_response = f'''<?xml version="1.0"?>
        <user>
            <id>{user['id']}</id>
            <name>{user['name']}</name>
            <email>{user['email']}</email>
        </user>'''
        return xml_response, 200, {'Content-Type': 'application/xml'}
    
    # Default to JSON
    return jsonify(user)
```

## API Versioning

### URL Path Versioning

```python
from flask import Blueprint

# Version 1 API
v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

@v1.route('/users', methods=['GET'])
def get_users_v1():
    # Version 1 implementation
    return jsonify({'users': users})

# Version 2 API
v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

@v2.route('/users', methods=['GET'])
def get_users_v2():
    # Version 2 implementation with additional fields
    enhanced_users = []
    for user in users:
        enhanced_user = user.copy()
        enhanced_user['full_profile'] = True
        enhanced_users.append(enhanced_user)
    
    return jsonify({'users': enhanced_users, 'version': '2.0'})

# Register blueprints
app.register_blueprint(v1)
app.register_blueprint(v2)
```

### Header Versioning

```python
@app.route('/api/users', methods=['GET'])
def get_users():
    version = request.headers.get('API-Version', '1.0')
    
    if version == '2.0':
        # Version 2 logic
        return jsonify({'users': users, 'version': '2.0'})
    else:
        # Version 1 logic (default)
        return jsonify({'users': users})
```

## Authentication and Authorization

### API Key Authentication

```python
from functools import wraps

# Simple API key storage (use database in production)
API_KEYS = {
    'key123': {'user': 'alice', 'permissions': ['read', 'write']},
    'key456': {'user': 'bob', 'permissions': ['read']}
}

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        
        if not api_key or api_key not in API_KEYS:
            return jsonify({'error': 'Invalid API key'}), 401
        
        # Store API key info in request context
        request.api_key_info = API_KEYS[api_key]
        return f(*args, **kwargs)
    
    return decorated_function

def require_permission(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if permission not in request.api_key_info['permissions']:
                return jsonify({'error': 'Insufficient permissions'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/api/users', methods=['GET'])
@require_api_key
def get_users():
    return jsonify({'users': users})

@app.route('/api/users', methods=['POST'])
@require_api_key
@require_permission('write')
def create_user():
    # Create user logic here...
    pass
```

### JWT Authentication

```python
import jwt
from datetime import datetime, timedelta

app.config['JWT_SECRET_KEY'] = 'your-secret-key'

def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, app.config['JWT_SECRET_KEY'], algorithm='HS256')

def verify_token(token):
    try:
        payload = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def require_jwt(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'error': 'Token missing'}), 401
        
        if token.startswith('Bearer '):
            token = token[7:]
        
        user_id = verify_token(token)
        if not user_id:
            return jsonify({'error': 'Invalid token'}), 401
        
        request.current_user_id = user_id
        return f(*args, **kwargs)
    
    return decorated_function
```

## API Documentation

### Using Docstrings

```python
@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Get list of users
    
    Query Parameters:
        page (int): Page number (default: 1)
        per_page (int): Items per page (default: 10)
        name (str): Filter by name
        email (str): Filter by email
        sort (str): Sort field (id, name, email)
        order (str): Sort order (asc, desc)
    
    Returns:
        200: List of users
        400: Invalid parameters
    
    Example:
        GET /api/users?page=1&per_page=5&sort=name&order=asc
    """
    # Implementation here...
```

### OpenAPI/Swagger Integration

```python
from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, doc='/docs/')

# Define models
user_model = api.model('User', {
    'id': fields.Integer(required=True, description='User ID'),
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email'),
    'created_at': fields.String(description='Creation timestamp')
})

user_input_model = api.model('UserInput', {
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email')
})

@api.route('/users')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """Get list of users"""
        return users
    
    @api.expect(user_input_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        # Implementation here...
        pass

@api.route('/users/<int:user_id>')
class User(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Get a specific user"""
        # Implementation here...
        pass
```

## Testing RESTful APIs

### Unit Testing

```python
import unittest
import json
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_get_users(self):
        response = self.app.get('/api/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('users', data)
    
    def test_create_user(self):
        user_data = {
            'name': 'Test User',
            'email': 'test@example.com'
        }
        response = self.app.post('/api/users',
                               data=json.dumps(user_data),
                               content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Test User')
    
    def test_get_nonexistent_user(self):
        response = self.app.get('/api/users/999')
        self.assertEqual(response.status_code, 404)
    
    def test_invalid_user_data(self):
        invalid_data = {'name': ''}  # Missing email
        response = self.app.post('/api/users',
                               data=json.dumps(invalid_data),
                               content_type='application/json')
        self.assertEqual(response.status_code, 422)

if __name__ == '__main__':
    unittest.main()
```

## Best Practices

### 1. Use Consistent Naming

```python
# Good - consistent plural nouns
/api/users
/api/posts
/api/comments

# Bad - inconsistent naming
/api/user
/api/getAllPosts
/api/comment-list
```

### 2. Use HTTP Status Codes Correctly

```python
# GET - 200 OK
# POST - 201 Created
# PUT/PATCH - 200 OK
# DELETE - 204 No Content
# Validation errors - 422 Unprocessable Entity
# Not found - 404 Not Found
# Unauthorized - 401 Unauthorized
# Forbidden - 403 Forbidden
```

### 3. Implement Proper Error Handling

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested resource was not found',
        'status_code': 404
    }), 404
```

### 4. Use Request Validation

```python
def validate_json_request(required_fields):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not request.is_json:
                return jsonify({'error': 'Content-Type must be application/json'}), 400
            
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No JSON data provided'}), 400
            
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return jsonify({
                    'error': 'Missing required fields',
                    'missing_fields': missing_fields
                }), 400
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator
```

### 5. Implement Rate Limiting

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/users', methods=['POST'])
@limiter.limit("5 per minute")
def create_user():
    # Implementation here...
    pass
```

## Summary

RESTful APIs provide a standardized way to build web services. Key principles:

1. **Resources**: Everything is a resource with a unique URI
2. **HTTP Methods**: Use appropriate verbs for different actions
3. **Status Codes**: Return meaningful HTTP status codes
4. **Stateless**: Each request should be independent
5. **JSON**: Use JSON for data exchange
6. **Validation**: Validate all input data
7. **Error Handling**: Provide clear error messages
8. **Authentication**: Secure your APIs appropriately
9. **Documentation**: Document your API endpoints
10. **Testing**: Write comprehensive tests

## Next Steps

In the next lesson, we'll explore database integration with Flask, learning how to persist data and build more robust APIs with database backends.