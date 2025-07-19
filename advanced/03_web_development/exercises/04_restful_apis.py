"""
Exercise 4: RESTful APIs with Flask

This exercise will help you practice building RESTful APIs with proper HTTP methods,
status codes, validation, and error handling.

Instructions:
1. Complete each function according to the specifications
2. Run the Flask application to test your API endpoints
3. Use the test functions to verify your implementations
"""

from flask import Flask, request, jsonify
from datetime import datetime
from typing import Dict, Any, List, Optional
import re


# Sample data storage (in production, use a database)
books = [
    {
        'id': 1,
        'title': 'The Python Tutorial',
        'author': 'Guido van Rossum',
        'isbn': '978-0-123456-78-9',
        'published_year': 2020,
        'genre': 'Programming',
        'available': True,
        'created_at': '2024-01-01T00:00:00'
    },
    {
        'id': 2,
        'title': 'Flask Web Development',
        'author': 'Miguel Grinberg',
        'isbn': '978-1-449-37262-0',
        'published_year': 2018,
        'genre': 'Programming',
        'available': True,
        'created_at': '2024-01-02T00:00:00'
    }
]

authors = [
    {
        'id': 1,
        'name': 'Guido van Rossum',
        'birth_year': 1956,
        'nationality': 'Dutch',
        'created_at': '2024-01-01T00:00:00'
    },
    {
        'id': 2,
        'name': 'Miguel Grinberg',
        'birth_year': 1970,
        'nationality': 'Argentinian',
        'created_at': '2024-01-02T00:00:00'
    }
]


def create_book_api() -> Flask:
    """
    Create a Flask application with RESTful API endpoints for managing books.
    
    Returns:
        Flask application with book management API
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_book_routes(app: Flask) -> None:
    """
    Add RESTful routes for book management.
    
    Routes to implement:
    - GET /api/books : List all books (with optional filtering and pagination)
    - GET /api/books/<id> : Get specific book
    - POST /api/books : Create new book
    - PUT /api/books/<id> : Update entire book
    - PATCH /api/books/<id> : Partially update book
    - DELETE /api/books/<id> : Delete book
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_author_routes(app: Flask) -> None:
    """
    Add RESTful routes for author management.
    
    Routes to implement:
    - GET /api/authors : List all authors
    - GET /api/authors/<id> : Get specific author
    - POST /api/authors : Create new author
    - PUT /api/authors/<id> : Update author
    - DELETE /api/authors/<id> : Delete author
    - GET /api/authors/<id>/books : Get books by specific author
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_validation_helpers(app: Flask) -> None:
    """
    Add validation helper functions for the API.
    
    Validation functions to implement:
    - validate_book_data(data, required_fields=None) -> List[str]
    - validate_author_data(data, required_fields=None) -> List[str]
    - validate_isbn(isbn) -> bool
    - validate_year(year) -> bool
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_error_handlers(app: Flask) -> None:
    """
    Add comprehensive error handlers for the API.
    
    Error handlers to implement:
    - 400 Bad Request
    - 404 Not Found
    - 409 Conflict
    - 422 Unprocessable Entity
    - 500 Internal Server Error
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def add_filtering_and_pagination(app: Flask) -> None:
    """
    Add filtering and pagination support to the books endpoint.
    
    Query parameters to support:
    - page: Page number (default: 1)
    - per_page: Items per page (default: 10, max: 100)
    - title: Filter by title (partial match)
    - author: Filter by author name (partial match)
    - genre: Filter by genre (exact match)
    - available: Filter by availability (true/false)
    - sort: Sort field (title, author, published_year)
    - order: Sort order (asc, desc)
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function (modify the GET /api/books route)
    """
    # Your code here
    pass


def add_api_versioning(app: Flask) -> None:
    """
    Add API versioning support using URL prefixes.
    
    Versions to implement:
    - v1: Basic CRUD operations
    - v2: Enhanced with additional fields and features
    
    Args:
        app: Flask application instance
    
    TODO: Implement this function
    """
    # Your code here
    pass


def create_complete_api() -> Flask:
    """
    Create a complete RESTful API with all features implemented.
    
    Returns:
        Flask application with complete API
    """
    app = create_book_api()
    
    if app is None:
        return None
    
    add_book_routes(app)
    add_author_routes(app)
    add_validation_helpers(app)
    add_error_handlers(app)
    add_filtering_and_pagination(app)
    add_api_versioning(app)
    
    return app


# Helper functions for testing
def find_book_by_id(book_id: int) -> Optional[Dict[str, Any]]:
    """Find a book by ID"""
    return next((book for book in books if book['id'] == book_id), None)


def find_author_by_id(author_id: int) -> Optional[Dict[str, Any]]:
    """Find an author by ID"""
    return next((author for author in authors if author['id'] == author_id), None)


def get_next_book_id() -> int:
    """Get the next available book ID"""
    return max(book['id'] for book in books) + 1 if books else 1


def get_next_author_id() -> int:
    """Get the next available author ID"""
    return max(author['id'] for author in authors) + 1 if authors else 1


# Test functions
def test_api_creation():
    """Test API creation"""
    print("Testing API creation...")
    
    app = create_book_api()
    assert app is not None, "Function should return a Flask app"
    assert isinstance(app, Flask), "Should return a Flask instance"
    
    print("✓ API creation test passed")


def test_book_routes():
    """Test book CRUD operations"""
    print("Testing book routes...")
    
    app = create_book_api()
    if app is None:
        print("❌ Cannot test routes - API creation failed")
        return
    
    add_book_routes(app)
    add_error_handlers(app)
    
    with app.test_client() as client:
        # Test GET /api/books
        response = client.get('/api/books')
        assert response.status_code == 200, "GET /api/books should return 200"
        assert response.is_json, "Response should be JSON"
        
        # Test GET /api/books/<id>
        response = client.get('/api/books/1')
        assert response.status_code == 200, "GET /api/books/1 should return 200"
        
        # Test GET non-existent book
        response = client.get('/api/books/999')
        assert response.status_code == 404, "GET /api/books/999 should return 404"
        
        # Test POST /api/books
        new_book = {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '978-0-123456-78-0',
            'published_year': 2023,
            'genre': 'Test'
        }
        response = client.post('/api/books', json=new_book)
        assert response.status_code == 201, "POST /api/books should return 201"
        
        # Test POST with invalid data
        invalid_book = {'title': 'Incomplete Book'}
        response = client.post('/api/books', json=invalid_book)
        assert response.status_code in [400, 422], "POST with invalid data should return 400 or 422"
    
    print("✓ Book routes test passed")


def test_author_routes():
    """Test author CRUD operations"""
    print("Testing author routes...")
    
    app = create_book_api()
    if app is None:
        print("❌ Cannot test routes - API creation failed")
        return
    
    add_author_routes(app)
    add_error_handlers(app)
    
    with app.test_client() as client:
        # Test GET /api/authors
        response = client.get('/api/authors')
        assert response.status_code == 200, "GET /api/authors should return 200"
        
        # Test GET /api/authors/<id>
        response = client.get('/api/authors/1')
        assert response.status_code == 200, "GET /api/authors/1 should return 200"
        
        # Test POST /api/authors
        new_author = {
            'name': 'Test Author',
            'birth_year': 1980,
            'nationality': 'American'
        }
        response = client.post('/api/authors', json=new_author)
        assert response.status_code == 201, "POST /api/authors should return 201"
        
        # Test GET /api/authors/<id>/books
        response = client.get('/api/authors/1/books')
        assert response.status_code == 200, "GET /api/authors/1/books should return 200"
    
    print("✓ Author routes test passed")


def test_error_handling():
    """Test error handling"""
    print("Testing error handling...")
    
    app = create_book_api()
    if app is None:
        print("❌ Cannot test error handling - API creation failed")
        return
    
    add_book_routes(app)
    add_error_handlers(app)
    
    with app.test_client() as client:
        # Test 404 error
        response = client.get('/api/nonexistent')
        assert response.status_code == 404, "Non-existent endpoint should return 404"
        
        # Test 400 error (invalid JSON)
        response = client.post('/api/books', data='invalid json', 
                             content_type='application/json')
        assert response.status_code == 400, "Invalid JSON should return 400"
    
    print("✓ Error handling test passed")


def test_filtering_and_pagination():
    """Test filtering and pagination"""
    print("Testing filtering and pagination...")
    
    app = create_book_api()
    if app is None:
        print("❌ Cannot test filtering - API creation failed")
        return
    
    add_book_routes(app)
    add_filtering_and_pagination(app)
    
    with app.test_client() as client:
        # Test pagination
        response = client.get('/api/books?page=1&per_page=1')
        assert response.status_code == 200, "Pagination should work"
        
        # Test filtering
        response = client.get('/api/books?genre=Programming')
        assert response.status_code == 200, "Filtering should work"
        
        # Test sorting
        response = client.get('/api/books?sort=title&order=asc')
        assert response.status_code == 200, "Sorting should work"
    
    print("✓ Filtering and pagination test passed")


def run_all_tests():
    """Run all test functions"""
    print("Running RESTful APIs Exercise Tests")
    print("=" * 40)
    
    try:
        test_api_creation()
        test_book_routes()
        test_author_routes()
        test_error_handling()
        test_filtering_and_pagination()
        
        print("\n" + "=" * 40)
        print("All tests passed! 🎉")
        print("\nYou've successfully completed the RESTful APIs exercise.")
        print("You now understand how to:")
        print("- Design RESTful API endpoints")
        print("- Use appropriate HTTP methods and status codes")
        print("- Implement CRUD operations")
        print("- Add validation and error handling")
        print("- Implement filtering and pagination")
        print("- Version your APIs")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("Please review your implementation and try again.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your code for syntax errors.")


def run_api_server():
    """Run the complete API server for manual testing"""
    app = create_complete_api()
    
    if app is None:
        print("❌ Cannot run server - API creation failed")
        return
    
    print("Starting RESTful API server...")
    print("Visit http://127.0.0.1:5000 to test your API")
    print("\nAvailable endpoints:")
    print("Books:")
    print("- GET /api/books : List books")
    print("- GET /api/books/<id> : Get specific book")
    print("- POST /api/books : Create book")
    print("- PUT /api/books/<id> : Update book")
    print("- PATCH /api/books/<id> : Partially update book")
    print("- DELETE /api/books/<id> : Delete book")
    print("\nAuthors:")
    print("- GET /api/authors : List authors")
    print("- GET /api/authors/<id> : Get specific author")
    print("- POST /api/authors : Create author")
    print("- PUT /api/authors/<id> : Update author")
    print("- DELETE /api/authors/<id> : Delete author")
    print("- GET /api/authors/<id>/books : Get books by author")
    print("\nQuery parameters for books:")
    print("- page, per_page : Pagination")
    print("- title, author, genre : Filtering")
    print("- sort, order : Sorting")
    
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run_api_server()
    else:
        run_all_tests()