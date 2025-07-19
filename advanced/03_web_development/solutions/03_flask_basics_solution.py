"""
Solution: Flask Basics

This file contains the complete solutions for the Flask basics exercise.
"""

from flask import Flask, request, render_template_string, jsonify, redirect, url_for, session
import os
import tempfile
from typing import Dict, Any, List
import logging


def create_basic_flask_app() -> Flask:
    """
    Create a basic Flask application with essential configuration.
    """
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
    app.config['DEBUG'] = True
    
    # Basic logging setup
    logging.basicConfig(level=logging.INFO)
    
    return app


def add_basic_routes(app: Flask) -> None:
    """
    Add basic routes to the Flask application.
    """
    @app.route('/')
    def home():
        return 'Welcome to Flask!'
    
    @app.route('/hello/<name>')
    def hello(name):
        return f'Hello, {name}!'
    
    @app.route('/about')
    def about():
        return '''
        <h1>About Our Flask Application</h1>
        <p>This is a sample Flask application for learning web development.</p>
        <p>Built with Python and Flask framework.</p>
        '''
    
    @app.route('/contact')
    def contact():
        return '''
        <h1>Contact Us</h1>
        <p>Email: contact@example.com</p>
        <p>Phone: (555) 123-4567</p>
        <p>Address: 123 Flask Street, Python City</p>
        '''


def add_http_method_routes(app: Flask) -> None:
    """
    Add routes that handle different HTTP methods.
    """
    # Sample data storage (in production, use a database)
    users = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
    ]
    
    @app.route('/api/users', methods=['GET'])
    def get_users():
        return jsonify({'users': users})
    
    @app.route('/api/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email are required'}), 400
        
        new_user = {
            'id': len(users) + 1,
            'name': data['name'],
            'email': data['email']
        }
        users.append(new_user)
        
        return jsonify({'message': 'User created successfully', 'user': new_user}), 201
    
    @app.route('/form', methods=['GET'])
    def show_form():
        return '''
        <h2>Contact Form</h2>
        <form method="POST">
            <p>
                <label>Name:</label><br>
                <input type="text" name="name" required>
            </p>
            <p>
                <label>Email:</label><br>
                <input type="email" name="email" required>
            </p>
            <p>
                <label>Message:</label><br>
                <textarea name="message" rows="4" cols="50"></textarea>
            </p>
            <p>
                <input type="submit" value="Submit">
            </p>
        </form>
        '''
    
    @app.route('/form', methods=['POST'])
    def handle_form():
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message', '')
        
        return f'''
        <h2>Form Submitted Successfully!</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Message:</strong> {message}</p>
        <p><a href="/form">Submit another form</a></p>
        '''


def add_template_routes(app: Flask) -> None:
    """
    Add routes that use templates for rendering HTML.
    """
    # Sample data
    products = [
        {'id': 1, 'name': 'Laptop', 'price': 999.99},
        {'id': 2, 'name': 'Mouse', 'price': 29.99},
        {'id': 3, 'name': 'Keyboard', 'price': 79.99}
    ]
    
    @app.route('/profile/<username>')
    def profile(username):
        template = '''
        <h1>User Profile</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Member since:</strong> {{ join_date }}</p>
        <p><strong>Status:</strong> Active</p>
        <p><a href="/">Back to Home</a></p>
        '''
        return render_template_string(template, 
                                    username=username, 
                                    join_date='January 2024')
    
    @app.route('/products')
    def show_products():
        template = '''
        <h1>Our Products</h1>
        <table border="1" style="border-collapse: collapse;">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Price</th>
            </tr>
            {% for product in products %}
            <tr>
                <td>{{ product.id }}</td>
                <td>{{ product.name }}</td>
                <td>${{ "%.2f"|format(product.price) }}</td>
            </tr>
            {% endfor %}
        </table>
        <p><a href="/">Back to Home</a></p>
        '''
        return render_template_string(template, products=products)
    
    @app.route('/dashboard')
    def dashboard():
        if 'username' not in session:
            return redirect(url_for('login'))
        
        template = '''
        <h1>Dashboard</h1>
        <p>Welcome back, {{ username }}!</p>
        <p>You are successfully logged in.</p>
        <ul>
            <li><a href="/profile/{{ username }}">View Profile</a></li>
            <li><a href="/products">Browse Products</a></li>
            <li><a href="/logout">Logout</a></li>
        </ul>
        '''
        return render_template_string(template, username=session['username'])


def add_session_routes(app: Flask) -> None:
    """
    Add routes that demonstrate session handling.
    """
    @app.route('/login', methods=['GET'])
    def login_form():
        return '''
        <h2>Login</h2>
        <form method="POST">
            <p>
                <label>Username:</label><br>
                <input type="text" name="username" required>
            </p>
            <p>
                <label>Password:</label><br>
                <input type="password" name="password" required>
            </p>
            <p>
                <input type="submit" value="Login">
            </p>
        </form>
        <p><small>Use any username and password to login</small></p>
        '''
    
    @app.route('/login', methods=['POST'])
    def login():
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple validation (in production, use proper authentication)
        if username and password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return '''
            <h2>Login Failed</h2>
            <p>Please provide both username and password.</p>
            <p><a href="/login">Try again</a></p>
            '''
    
    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return '''
        <h2>Logged Out</h2>
        <p>You have been successfully logged out.</p>
        <p><a href="/">Home</a> | <a href="/login">Login again</a></p>
        '''
    
    @app.route('/protected')
    def protected():
        if 'username' not in session:
            return redirect(url_for('login'))
        
        return f'''
        <h2>Protected Content</h2>
        <p>Hello, {session['username']}! This is protected content.</p>
        <p>Only logged-in users can see this page.</p>
        <p><a href="/dashboard">Dashboard</a> | <a href="/logout">Logout</a></p>
        '''


def add_error_handlers(app: Flask) -> None:
    """
    Add custom error handlers to the Flask application.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Not Found',
            'message': 'The requested resource was not found on this server.',
            'status_code': 404
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An internal server error occurred.',
            'status_code': 500
        }), 500
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'error': 'Bad Request',
            'message': 'The request could not be understood by the server.',
            'status_code': 400
        }), 400


def add_request_processing(app: Flask) -> None:
    """
    Add request processing functions (before_request, after_request).
    """
    @app.before_request
    def before_request():
        # Log request information
        app.logger.info(f'{request.method} {request.path} - {request.remote_addr}')
    
    @app.after_request
    def after_request(response):
        # Add custom header to all responses
        response.headers['X-Custom-Header'] = 'Flask-Learning-App'
        response.headers['X-Powered-By'] = 'Python-Flask'
        return response


# Sample data for testing
SAMPLE_USERS = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
]

SAMPLE_PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99},
    {'id': 2, 'name': 'Mouse', 'price': 29.99},
    {'id': 3, 'name': 'Keyboard', 'price': 79.99}
]


def create_complete_flask_app() -> Flask:
    """
    Create a complete Flask application with all features implemented.
    """
    app = create_basic_flask_app()
    
    add_basic_routes(app)
    add_http_method_routes(app)
    add_template_routes(app)
    add_session_routes(app)
    add_error_handlers(app)
    add_request_processing(app)
    
    return app


# Test functions (same as in exercise file)
def test_basic_app_creation():
    """Test basic Flask app creation"""
    print("Testing basic Flask app creation...")
    
    app = create_basic_flask_app()
    assert app is not None, "Function should return a Flask app"
    assert isinstance(app, Flask), "Should return a Flask instance"
    assert app.secret_key is not None, "App should have a secret key"
    
    print("✓ Basic app creation test passed")


def test_basic_routes():
    """Test basic routes"""
    print("Testing basic routes...")
    
    app = create_basic_flask_app()
    add_basic_routes(app)
    
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200, "Home route should return 200"
        assert b'Welcome to Flask!' in response.data, "Home route should return welcome message"
        
        response = client.get('/hello/Alice')
        assert response.status_code == 200, "Hello route should return 200"
        assert b'Hello, Alice!' in response.data, "Hello route should return personalized greeting"
        
        response = client.get('/about')
        assert response.status_code == 200, "About route should return 200"
        
        response = client.get('/contact')
        assert response.status_code == 200, "Contact route should return 200"
    
    print("✓ Basic routes test passed")


def test_http_method_routes():
    """Test HTTP method routes"""
    print("Testing HTTP method routes...")
    
    app = create_basic_flask_app()
    add_http_method_routes(app)
    
    with app.test_client() as client:
        response = client.get('/api/users')
        assert response.status_code == 200, "GET /api/users should return 200"
        assert response.is_json, "Response should be JSON"
        
        user_data = {'name': 'Test User', 'email': 'test@example.com'}
        response = client.post('/api/users', json=user_data)
        assert response.status_code in [200, 201], "POST /api/users should return 200 or 201"
        
        response = client.get('/form')
        assert response.status_code == 200, "GET /form should return 200"
        
        form_data = {'name': 'Test', 'email': 'test@example.com'}
        response = client.post('/form', data=form_data)
        assert response.status_code == 200, "POST /form should return 200"
    
    print("✓ HTTP method routes test passed")


def test_session_routes():
    """Test session routes"""
    print("Testing session routes...")
    
    app = create_basic_flask_app()
    add_session_routes(app)
    
    with app.test_client() as client:
        response = client.get('/login')
        assert response.status_code == 200, "GET /login should return 200"
        
        login_data = {'username': 'testuser', 'password': 'password'}
        response = client.post('/login', data=login_data)
        assert response.status_code in [200, 302], "POST /login should return 200 or 302"
        
        response = client.get('/protected')
        assert response.status_code in [200, 302], "Protected route should return 200 or 302"
        
        response = client.get('/logout')
        assert response.status_code in [200, 302], "Logout should return 200 or 302"
    
    print("✓ Session routes test passed")


def test_error_handlers():
    """Test error handlers"""
    print("Testing error handlers...")
    
    app = create_basic_flask_app()
    add_error_handlers(app)
    
    with app.test_client() as client:
        response = client.get('/nonexistent-route')
        assert response.status_code == 404, "Nonexistent route should return 404"
    
    print("✓ Error handlers test passed")


def run_all_tests():
    """Run all test functions"""
    print("Running Flask Basics Solution Tests")
    print("=" * 40)
    
    try:
        test_basic_app_creation()
        test_basic_routes()
        test_http_method_routes()
        test_session_routes()
        test_error_handlers()
        
        print("\n" + "=" * 40)
        print("All tests passed! 🎉")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


def run_flask_app():
    """Run the complete Flask application for manual testing"""
    app = create_complete_flask_app()
    
    print("Starting Flask application...")
    print("Visit http://127.0.0.1:5000 to test your application")
    print("Available routes:")
    print("- GET / : Home page")
    print("- GET /hello/<name> : Personalized greeting")
    print("- GET /about : About page")
    print("- GET /contact : Contact page")
    print("- GET /api/users : List users (JSON)")
    print("- POST /api/users : Create user (JSON)")
    print("- GET /form : Display form")
    print("- POST /form : Handle form submission")
    print("- GET /profile/<username> : User profile")
    print("- GET /products : Product list")
    print("- GET /login : Login form")
    print("- POST /login : Process login")
    print("- GET /logout : Logout")
    print("- GET /protected : Protected content")
    print("- GET /dashboard : Dashboard (requires login)")
    
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run_flask_app()
    else:
        run_all_tests()