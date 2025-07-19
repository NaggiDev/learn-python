"""
Exercise 5: Database Integration with Flask

This exercise will help you practice integrating databases with Flask applications
using SQLAlchemy ORM. You'll create models, perform CRUD operations, and handle
relationships between data.

Instructions:
1. Complete each function according to the specifications
2. Run the Flask application to test your database operations
3. Use the test functions to verify your implementations
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from typing import Dict, Any, List, Optional
import os


# Initialize SQLAlchemy
db = SQLAlchemy()


def create_database_app() -> Flask:
    """
    Create a Flask application with database configuration.
    
    Returns:
        Flask application with SQLAlchemy configured
    
    TODO: Implement this function
    """
    # Your code here
    pass


def define_models() -> None:
    """
    Define database models for a blog application.
    
    Models to create:
    1. User model with fields: id, username, email, password_hash, created_at, is_active
    2. Category model with fields: id, name, description, created_at
    3. Post model with fields: id, title, content, user_id (FK), category_id (FK), 
       created_at, updated_at, published
    4. Comment model with fields: id, content, user_id (FK), post_id (FK), created_at
    
    Relationships:
    - User has many Posts (one-to-many)
    - User has many Comments (one-to-many)
    - Category has many Posts (one-to-many)
    - Post has many Comments (one-to-many)
    - Post belongs to User (many-to-one)
    - Post belongs to Category (many-to-one)
    - Comment belongs to User (many-to-one)
    - Comment belongs to Post (many-to-one)
    
    TODO: Implement this function by defining the models
    """
    # Your code here
    pass


def add_user_routes(app: Flask) -> None:
    """
    Add CRUD routes for user management.
    
    Routes to implement:
    - GET /api/users : List all users (with pagination)
    - GET /api/users/<id> : Get specific user
    - POST /api/users : Create new user
    - PUT /api/users/<id> : Update user
    - DELETE /api/users/<id> : Delete user
    - GET /api/users/<id>/posts : Get user's posts
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_post_routes(app: Flask) -> None:
    """
    Add CRUD routes for post management.
    
    Routes to implement:
    - GET /api/posts : List all posts (with filtering and pagination)
    - GET /api/posts/<id> : Get specific post with comments
    - POST /api/posts : Create new post
    - PUT /api/posts/<id> : Update post
    - DELETE /api/posts/<id> : Delete post
    - GET /api/posts/search : Search posts by title or content
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_category_routes(app: Flask) -> None:
    """
    Add CRUD routes for category management.
    
    Routes to implement:
    - GET /api/categories : List all categories
    - GET /api/categories/<id> : Get specific category
    - POST /api/categories : Create new category
    - PUT /api/categories/<id> : Update category
    - DELETE /api/categories/<id> : Delete category
    - GET /api/categories/<id>/posts : Get posts in category
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_comment_routes(app: Flask) -> None:
    """
    Add CRUD routes for comment management.
    
    Routes to implement:
    - GET /api/comments : List all comments
    - GET /api/comments/<id> : Get specific comment
    - POST /api/comments : Create new comment
    - PUT /api/comments/<id> : Update comment
    - DELETE /api/comments/<id> : Delete comment
    - GET /api/posts/<id>/comments : Get comments for a post
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_database_utilities(app: Flask) -> None:
    """
    Add utility functions for database operations.
    
    Utilities to implement:
    - Initialize database tables
    - Seed database with sample data
    - Database health check endpoint
    - Statistics endpoint (user count, post count, etc.)
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_advanced_queries(app: Flask) -> None:
    """
    Add routes that demonstrate advanced database queries.
    
    Routes to implement:
    - GET /api/stats : Get database statistics
    - GET /api/popular-posts : Get most commented posts
    - GET /api/active-users : Get users with most posts
    - GET /api/recent-activity : Get recent posts and comments
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_error_handling(app: Flask) -> None:
    """
    Add comprehensive error handling for database operations.
    
    Error handlers to implement:
    - Database connection errors
    - Integrity constraint violations
    - Foreign key constraint violations
    - General database errors
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def create_complete_blog_app() -> Flask:
    """
    Create a complete blog application with database integration.
    
    Returns:
        Flask application with all features implemented
    """
    app = create_database_app()
    
    if app is None:
        return None
    
    # Define models first
    define_models()
    
    # Add routes
    add_user_routes(app)
    add_post_routes(app)
    add_category_routes(app)
    add_comment_routes(app)
    add_database_utilities(app)
    add_advanced_queries(app)
    add_error_handling(app)
    
    return app


# Helper functions for testing
def init_database(app: Flask) -> None:
    """Initialize database tables"""
    with app.app_context():
        db.create_all()


def seed_database(app: Flask) -> None:
    """Seed database with sample data"""
    with app.app_context():
        # This will be implemented in the solution
        pass


# Test functions
def test_app_creation():
    """Test database app creation"""
    print("Testing database app creation...")
    
    app = create_database_app()
    assert app is not None, "Function should return a Flask app"
    assert isinstance(app, Flask), "Should return a Flask instance"
    
    # Check database configuration
    assert 'SQLALCHEMY_DATABASE_URI' in app.config, "Should have database URI configured"
    
    print("✓ Database app creation test passed")


def test_model_definition():
    """Test model definitions"""
    print("Testing model definitions...")
    
    app = create_database_app()
    if app is None:
        print("❌ Cannot test models - app creation failed")
        return
    
    with app.app_context():
        define_models()
        
        # Check if models are defined
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        
        # This test will be more comprehensive in the solution
        print("✓ Model definition test passed")


def test_user_operations():
    """Test user CRUD operations"""
    print("Testing user operations...")
    
    app = create_complete_blog_app()
    if app is None:
        print("❌ Cannot test user operations - app creation failed")
        return
    
    with app.app_context():
        db.create_all()
        
        with app.test_client() as client:
            # Test create user
            user_data = {
                'username': 'testuser',
                'email': 'test@example.com',
                'password': 'password123'
            }
            response = client.post('/api/users', json=user_data)
            assert response.status_code == 201, "User creation should return 201"
            
            # Test get users
            response = client.get('/api/users')
            assert response.status_code == 200, "Get users should return 200"
            
            # Test get specific user
            response = client.get('/api/users/1')
            assert response.status_code == 200, "Get specific user should return 200"
    
    print("✓ User operations test passed")


def test_post_operations():
    """Test post CRUD operations"""
    print("Testing post operations...")
    
    app = create_complete_blog_app()
    if app is None:
        print("❌ Cannot test post operations - app creation failed")
        return
    
    with app.app_context():
        db.create_all()
        seed_database(app)
        
        with app.test_client() as client:
            # Test create post
            post_data = {
                'title': 'Test Post',
                'content': 'This is a test post content.',
                'user_id': 1,
                'category_id': 1
            }
            response = client.post('/api/posts', json=post_data)
            assert response.status_code == 201, "Post creation should return 201"
            
            # Test get posts
            response = client.get('/api/posts')
            assert response.status_code == 200, "Get posts should return 200"
    
    print("✓ Post operations test passed")


def test_relationships():
    """Test model relationships"""
    print("Testing model relationships...")
    
    app = create_complete_blog_app()
    if app is None:
        print("❌ Cannot test relationships - app creation failed")
        return
    
    with app.app_context():
        db.create_all()
        seed_database(app)
        
        with app.test_client() as client:
            # Test user's posts
            response = client.get('/api/users/1/posts')
            assert response.status_code == 200, "Get user posts should return 200"
            
            # Test category's posts
            response = client.get('/api/categories/1/posts')
            assert response.status_code == 200, "Get category posts should return 200"
            
            # Test post's comments
            response = client.get('/api/posts/1/comments')
            assert response.status_code == 200, "Get post comments should return 200"
    
    print("✓ Relationships test passed")


def test_advanced_queries():
    """Test advanced database queries"""
    print("Testing advanced queries...")
    
    app = create_complete_blog_app()
    if app is None:
        print("❌ Cannot test advanced queries - app creation failed")
        return
    
    with app.app_context():
        db.create_all()
        seed_database(app)
        
        with app.test_client() as client:
            # Test statistics
            response = client.get('/api/stats')
            assert response.status_code == 200, "Get stats should return 200"
            
            # Test popular posts
            response = client.get('/api/popular-posts')
            assert response.status_code == 200, "Get popular posts should return 200"
    
    print("✓ Advanced queries test passed")


def run_all_tests():
    """Run all test functions"""
    print("Running Database Integration Exercise Tests")
    print("=" * 45)
    
    try:
        test_app_creation()
        test_model_definition()
        test_user_operations()
        test_post_operations()
        test_relationships()
        test_advanced_queries()
        
        print("\n" + "=" * 45)
        print("All tests passed! 🎉")
        print("\nYou've successfully completed the database integration exercise.")
        print("You now understand how to:")
        print("- Configure Flask with SQLAlchemy")
        print("- Define database models with relationships")
        print("- Perform CRUD operations with ORM")
        print("- Handle database errors and transactions")
        print("- Write advanced database queries")
        print("- Test database operations")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("Please review your implementation and try again.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your code for syntax errors.")


def run_blog_app():
    """Run the complete blog application for manual testing"""
    app = create_complete_blog_app()
    
    if app is None:
        print("❌ Cannot run app - creation failed")
        return
    
    # Initialize database
    with app.app_context():
        db.create_all()
        seed_database(app)
    
    print("Starting Blog API server...")
    print("Visit http://127.0.0.1:5000 to test your API")
    print("\nAvailable endpoints:")
    print("Users:")
    print("- GET /api/users : List users")
    print("- GET /api/users/<id> : Get specific user")
    print("- POST /api/users : Create user")
    print("- PUT /api/users/<id> : Update user")
    print("- DELETE /api/users/<id> : Delete user")
    print("- GET /api/users/<id>/posts : Get user's posts")
    print("\nPosts:")
    print("- GET /api/posts : List posts")
    print("- GET /api/posts/<id> : Get specific post")
    print("- POST /api/posts : Create post")
    print("- PUT /api/posts/<id> : Update post")
    print("- DELETE /api/posts/<id> : Delete post")
    print("- GET /api/posts/search : Search posts")
    print("\nCategories:")
    print("- GET /api/categories : List categories")
    print("- GET /api/categories/<id> : Get specific category")
    print("- POST /api/categories : Create category")
    print("- GET /api/categories/<id>/posts : Get category posts")
    print("\nComments:")
    print("- GET /api/comments : List comments")
    print("- POST /api/comments : Create comment")
    print("- GET /api/posts/<id>/comments : Get post comments")
    print("\nUtilities:")
    print("- GET /api/stats : Database statistics")
    print("- GET /api/popular-posts : Most commented posts")
    print("- GET /api/active-users : Most active users")
    
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run_blog_app()
    else:
        run_all_tests()