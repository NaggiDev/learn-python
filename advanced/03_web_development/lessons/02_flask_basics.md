# Flask Framework Basics: Building Web Applications with Python

## Introduction

Flask is a lightweight and flexible Python web framework that provides the basic tools and libraries needed to build web applications. Unlike larger frameworks like Django, Flask follows a "micro-framework" philosophy, giving you the freedom to choose your components and structure your application as you see fit.

## Why Flask?

- **Simplicity**: Easy to learn and get started
- **Flexibility**: Minimal assumptions about your application structure
- **Extensibility**: Large ecosystem of extensions
- **Pythonic**: Follows Python conventions and idioms
- **Well-documented**: Excellent documentation and community support

## Installation and Setup

```bash
# Install Flask
pip install Flask

# For development, also install:
pip install Flask-DebugToolbar
```

## Your First Flask Application

### Hello World Example

```python
from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Save this as `app.py` and run:
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to see your application.

## Flask Application Structure

### Basic Structure
```
my_flask_app/
├── app.py              # Main application file
├── templates/          # HTML templates
│   ├── base.html
│   └── index.html
├── static/            # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── requirements.txt   # Dependencies
```

### Application Factory Pattern
For larger applications, use the application factory pattern:

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
```

## Routing

### Basic Routes

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact')
def contact():
    return 'Contact Page'
```

### Dynamic Routes

```python
@app.route('/user/<username>')
def user_profile(username):
    return f'User: {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'
```

### Route Converters
- `string` (default): accepts any text without a slash
- `int`: accepts positive integers
- `float`: accepts positive floating point values
- `path`: like string but accepts slashes
- `uuid`: accepts UUID strings

### HTTP Methods

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission
        username = request.form['username']
        password = request.form['password']
        return f'Login attempt for {username}'
    else:
        # Show login form
        return '''
        <form method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
        '''

@app.route('/api/users', methods=['GET'])
def get_users():
    return {'users': ['alice', 'bob', 'charlie']}

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return {'message': f'User {data["name"]} created'}, 201
```

## Request Handling

### Accessing Request Data

```python
from flask import request, Flask

app = Flask(__name__)

@app.route('/search')
def search():
    # Query parameters: /search?q=python&category=programming
    query = request.args.get('q', '')
    category = request.args.get('category', 'all')
    return f'Searching for "{query}" in category "{category}"'

@app.route('/submit', methods=['POST'])
def submit_form():
    # Form data
    name = request.form.get('name')
    email = request.form.get('email')
    
    # File uploads
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            file.save(f'uploads/{file.filename}')
    
    return f'Form submitted by {name} ({email})'

@app.route('/api/data', methods=['POST'])
def handle_json():
    # JSON data
    data = request.get_json()
    return {'received': data}
```

### Request Context

```python
from flask import request, g

@app.before_request
def before_request():
    # Runs before each request
    g.user = get_current_user()  # Example

@app.after_request
def after_request(response):
    # Runs after each request
    response.headers['X-Custom-Header'] = 'Flask App'
    return response
```

## Response Handling

### Different Response Types

```python
from flask import jsonify, redirect, url_for, abort, make_response

@app.route('/json')
def json_response():
    return jsonify({'message': 'Hello', 'status': 'success'})

@app.route('/redirect-example')
def redirect_example():
    return redirect(url_for('index'))

@app.route('/custom-response')
def custom_response():
    response = make_response('Custom Response')
    response.headers['Content-Type'] = 'text/plain'
    response.status_code = 201
    return response

@app.route('/error-example')
def error_example():
    abort(404)  # Raises a 404 error
```

### Status Codes

```python
@app.route('/created', methods=['POST'])
def create_resource():
    # Create resource logic here
    return {'message': 'Resource created'}, 201

@app.route('/no-content', methods=['DELETE'])
def delete_resource():
    # Delete resource logic here
    return '', 204
```

## Templates with Jinja2

### Basic Template Usage

```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

### Template Files

**templates/base.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Flask App{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">Home</a>
        <a href="{{ url_for('about') }}">About</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**templates/hello.html**:
```html
{% extends "base.html" %}

{% block title %}Hello {{ name }}{% endblock %}

{% block content %}
    <h1>Hello, {{ name }}!</h1>
    <p>Welcome to our Flask application.</p>
{% endblock %}
```

### Template Features

```html
<!-- Variables -->
<h1>{{ title }}</h1>
<p>User: {{ user.name }}</p>

<!-- Filters -->
<p>{{ message | upper }}</p>
<p>{{ price | round(2) }}</p>
<p>{{ date | strftime('%Y-%m-%d') }}</p>

<!-- Control structures -->
{% if user %}
    <p>Welcome, {{ user.name }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}

{% for item in items %}
    <li>{{ item.name }} - ${{ item.price }}</li>
{% endfor %}

<!-- URL generation -->
<a href="{{ url_for('user_profile', username='alice') }}">Alice's Profile</a>
```

## Static Files

### Serving Static Files

Flask automatically serves files from the `static/` directory:

```
static/
├── css/
│   └── style.css
├── js/
│   └── app.js
└── images/
    └── logo.png
```

### Using Static Files in Templates

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/app.js') }}"></script>
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

## Error Handling

### Custom Error Pages

```python
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error
    app.logger.error(f'Unhandled exception: {e}')
    return 'Something went wrong!', 500
```

### Try-Catch in Routes

```python
@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    try:
        result = a / b
        return {'result': result}
    except ZeroDivisionError:
        return {'error': 'Division by zero'}, 400
```

## Configuration

### Configuration Methods

```python
# Method 1: Direct assignment
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DEBUG'] = True

# Method 2: From object
class Config:
    SECRET_KEY = 'your-secret-key'
    DEBUG = True
    DATABASE_URL = 'sqlite:///app.db'

app.config.from_object(Config)

# Method 3: From file
app.config.from_pyfile('config.py')

# Method 4: From environment variables
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-key')
```

### Environment-based Configuration

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL = os.environ.get('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

## Sessions and Cookies

### Using Sessions

```python
from flask import session

app.secret_key = 'your-secret-key'  # Required for sessions

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    # Validate user credentials here
    session['username'] = username
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Welcome, {session["username"]}!'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
```

### Working with Cookies

```python
from flask import make_response, request

@app.route('/set-cookie')
def set_cookie():
    response = make_response('Cookie set!')
    response.set_cookie('user_preference', 'dark_mode')
    return response

@app.route('/get-cookie')
def get_cookie():
    preference = request.cookies.get('user_preference', 'light_mode')
    return f'Your preference: {preference}'
```

## Flask Extensions

### Popular Extensions

```python
# Flask-WTF for forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# Flask-SQLAlchemy for database
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

## Blueprints for Large Applications

### Creating Blueprints

```python
# app/main/routes.py
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Main page'

@bp.route('/about')
def about():
    return 'About page'
```

### Registering Blueprints

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app
```

## Testing Flask Applications

### Basic Testing

```python
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello' in response.data

def test_login(client):
    response = client.post('/login', data={
        'username': 'test',
        'password': 'password'
    })
    assert response.status_code == 302  # Redirect after login
```

## Best Practices

### 1. Application Structure
```
large_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   └── auth/
│       ├── __init__.py
│       └── routes.py
├── migrations/
├── tests/
├── config.py
└── run.py
```

### 2. Security Considerations

```python
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

# Enable HTTPS enforcement
Talisman(app)

# Secure session configuration
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Input validation
from wtforms.validators import DataRequired, Length

class UserForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(min=3, max=20)
    ])
```

### 3. Error Handling

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
```

### 4. Performance Tips

```python
# Use caching
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/expensive-operation')
@cache.cached(timeout=300)  # Cache for 5 minutes
def expensive_operation():
    # Expensive computation here
    return result

# Lazy loading
from flask import g

def get_db():
    if 'db' not in g:
        g.db = connect_to_database()
    return g.db
```

## Deployment Considerations

### Production Configuration

```python
# config.py
import os

class ProductionConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Security headers
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    
    # Logging
    LOG_LEVEL = 'INFO'
```

### WSGI Server

```python
# wsgi.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
```

Run with Gunicorn:
```bash
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

## Summary

Flask provides a solid foundation for building web applications with Python. Key concepts:

1. **Routing**: Map URLs to Python functions
2. **Request/Response**: Handle HTTP requests and generate responses
3. **Templates**: Separate presentation from logic using Jinja2
4. **Static Files**: Serve CSS, JavaScript, and images
5. **Error Handling**: Gracefully handle errors and exceptions
6. **Configuration**: Manage application settings
7. **Sessions**: Maintain user state across requests
8. **Extensions**: Extend functionality with Flask extensions
9. **Blueprints**: Organize large applications
10. **Testing**: Write tests for your applications

## Next Steps

In the next lesson, we'll explore RESTful API development with Flask, learning how to build APIs that follow REST principles and handle JSON data effectively.