"""
Exercise 3: Flask Basics

This exercise will help you practice building web applications with Flask.
You'll create routes, handle requests, work with templates, and implement basic functionality.

Instructions:
1. Complete each function according to the specifications
2. Run the Flask application to test your implementations
3. Use the test functions to verify your solutions
"""

from flask import Flask, request, render_template_string, jsonify, redirect, url_for, session
import os
import tempfile
from typing import Dict, Any, List


def create_basic_flask_app() -> Flask:
    """
    Create a basic Flask application with essential configuration.
    
    Returns:
        Flask application instance with:
        - Secret key configured
        - Debug mode enabled
        - Basic error handling
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_basic_routes(app: Flask) -> None:
    """
    Add basic routes to the Flask application.
    
    Routes to implement:
    - GET / : Return "Welcome to Flask!"
    - GET /hello/<name> : Return "Hello, {name}!"
    - GET /about : Return information about the application
    - GET /contact : Return contact information
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_http_method_routes(app: Flask) -> None:
    """
    Add routes that handle different HTTP methods.
    
    Routes to implement:
    - GET /api/users : Return list of users as JSON
    - POST /api/users : Create a new user from JSON data
    - GET /form : Display a simple HTML form
    - POST /form : Handle form submission and return submitted data
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_template_routes(app: Flask) -> None:
    """
    Add routes that use templates for rendering HTML.
    
    Routes to implement:
    - GET /profile/<username> : Display user profile page
    - GET /products : Display list of products
    - GET /dashboard : Display dashboard (requires session)
    
    Args:
        app: Flask application instance
    
    Templates to use (as template strings):
    - profile.html: Display username and join date
    - products.html: Display list of products with prices
    - dashboard.html: Display welcome message with username from session
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_session_routes(app: Flask) -> None:
    """
    Add routes that demonstrate session handling.
    
    Routes to implement:
    - GET /login : Display login form
    - POST /login : Process login and set session
    - GET /logout : Clear session and redirect to home
    - GET /protected : Show content only if logged in
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_error_handlers(app: Flask) -> None:
    """
    Add custom error handlers to the Flask application.
    
    Error handlers to implement:
    - 404 Not Found: Return JSON with error message
    - 500 Internal Server Error: Return JSON with error message
    - 400 Bad Request: Return JSON with error message
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_request_processing(app: Flask) -> None:
    """
    Add request processing functions (before_request, after_request).
    
    Functions to implement:
    - before_request: Log request method and path
    - after_request: Add custom header to all responses
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


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
    
    Returns:
        Flask application with all routes and features
    """
    app = create_basic_flask_app()
    
    if app is None:
        return None
    
    add_basic_routes(app)
    add_http_method_routes(app)
    add_template_routes(app)
    add_session_routes(app)
    add_error_handlers(app)
    add_request_processing(app)
    
    return app


# Test functions
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
    if app is None:
        print("❌ Cannot test routes - basic app creation failed")
        return
    
    add_basic_routes(app)
    
    with app.test_client() as client:
        # Test home route
        response = client.get('/')
        assert response.status_code == 200, "Home route should return 200"
        assert b'Welcome to Flask!' in response.data, "Home route should return welcome message"
        
        # Test hello route
        response = client.get('/hello/Alice')
        assert response.status_code == 200, "Hello route should return 200"
        assert b'Hello, Alice!' in response.data, "Hello route should return personalized greeting"
        
        # Test about route
        response = client.get('/about')
        assert response.status_code == 200, "About route should return 200"
        
        # Test contact route
        response = client.get('/contact')
        assert response.status_code == 200, "Contact route should return 200"
    
    print("✓ Basic routes test passed")


def test_http_method_routes():
    """Test HTTP method routes"""
    print("Testing HTTP method routes...")
    
    app = create_basic_flask_app()
    if app is None:
        print("❌ Cannot test routes - basic app creation failed")
        return
    
    add_http_method_routes(app)
    
    with app.test_client() as client:
        # Test GET /api/users
        response = client.get('/api/users')
        assert response.status_code == 200, "GET /api/users should return 200"
        assert response.is_json, "Response should be JSON"
        
        # Test POST /api/users
        user_data = {'name': 'Test User', 'email': 'test@example.com'}
        response = client.post('/api/users', json=user_data)
        assert response.status_code in [200, 201], "POST /api/users should return 200 or 201"
        
        # Test GET /form
        response = client.get('/form')
        assert response.status_code == 200, "GET /form should return 200"
        
        # Test POST /form
        form_data = {'name': 'Test', 'email': 'test@example.com'}
        response = client.post('/form', data=form_data)
        assert response.status_code == 200, "POST /form should return 200"
    
    print("✓ HTTP method routes test passed")


def test_session_routes():
    """Test session routes"""
    print("Testing session routes...")
    
    app = create_basic_flask_app()
    if app is None:
        print("❌ Cannot test routes - basic app creation failed")
        return
    
    add_session_routes(app)
    
    with app.test_client() as client:
        # Test login form
        response = client.get('/login')
        assert response.status_code == 200, "GET /login should return 200"
        
        # Test login submission
        login_data = {'username': 'testuser', 'password': 'password'}
        response = client.post('/login', data=login_data)
        assert response.status_code in [200, 302], "POST /login should return 200 or 302"
        
        # Test protected route (should work after login)
        response = client.get('/protected')
        # Status could be 200 (if logged in) or 302 (if redirected)
        assert response.status_code in [200, 302], "Protected route should return 200 or 302"
        
        # Test logout
        response = client.get('/logout')
        assert response.status_code in [200, 302], "Logout should return 200 or 302"
    
    print("✓ Session routes test passed")


def test_error_handlers():
    """Test error handlers"""
    print("Testing error handlers...")
    
    app = create_basic_flask_app()
    if app is None:
        print("❌ Cannot test error handlers - basic app creation failed")
        return
    
    add_error_handlers(app)
    
    with app.test_client() as client:
        # Test 404 error
        response = client.get('/nonexistent-route')
        assert response.status_code == 404, "Nonexistent route should return 404"
    
    print("✓ Error handlers test passed")


def run_all_tests():
    """Run all test functions"""
    print("Running Flask Basics Exercise Tests")
    print("=" * 40)
    
    try:
        test_basic_app_creation()
        test_basic_routes()
        test_http_method_routes()
        test_session_routes()
        test_error_handlers()
        
        print("\n" + "=" * 40)
        print("All tests passed! 🎉")
        print("\nYou've successfully completed the Flask basics exercise.")
        print("You now understand how to:")
        print("- Create Flask applications")
        print("- Define routes with different HTTP methods")
        print("- Handle requests and generate responses")
        print("- Work with sessions")
        print("- Implement error handling")
        print("- Use templates for HTML rendering")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("Please review your implementation and try again.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your code for syntax errors.")


def run_flask_app():
    """Run the complete Flask application for manual testing"""
    app = create_complete_flask_app()
    
    if app is None:
        print("❌ Cannot run app - creation failed")
        return
    
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