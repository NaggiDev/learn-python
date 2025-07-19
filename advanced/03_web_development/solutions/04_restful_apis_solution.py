"""
Solution: RESTful APIs with Flask

This file contains the complete solutions for the RESTful APIs exercise.
"""

from flask import Flask, request, jsonify, Blueprint
from datetime import datetime
from typing import Dict, Any, List, Optional
import re
import math


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
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['DEBUG'] = True
    
    return app


def validate_isbn(isbn: str) -> bool:
    """Validate ISBN format"""
    # Simple ISBN-13 validation
    isbn_pattern = r'^978-\d-\d{6}-\d{2}-\d$'
    return bool(re.match(isbn_pattern, isbn))


def validate_year(year: int) -> bool:
    """Validate publication year"""
    current_year = datetime.now().year
    return 1000 <= year <= current_year


def validate_book_data(data: Dict[str, Any], required_fields: List[str] = None) -> List[str]:
    """Validate book data and return list of errors"""
    errors = []
    
    if required_fields:
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f'{field} is required')
    
    if 'title' in data and len(data['title'].strip()) < 1:
        errors.append('Title cannot be empty')
    
    if 'author' in data and len(data['author'].strip()) < 1:
        errors.append('Author cannot be empty')
    
    if 'isbn' in data and not validate_isbn(data['isbn']):
        errors.append('Invalid ISBN format (expected: 978-X-XXXXXX-XX-X)')
    
    if 'published_year' in data:
        try:
            year = int(data['published_year'])
            if not validate_year(year):
                errors.append('Invalid publication year')
        except (ValueError, TypeError):
            errors.append('Published year must be a number')
    
    if 'available' in data and not isinstance(data['available'], bool):
        errors.append('Available must be true or false')
    
    return errors


def validate_author_data(data: Dict[str, Any], required_fields: List[str] = None) -> List[str]:
    """Validate author data and return list of errors"""
    errors = []
    
    if required_fields:
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f'{field} is required')
    
    if 'name' in data and len(data['name'].strip()) < 1:
        errors.append('Name cannot be empty')
    
    if 'birth_year' in data:
        try:
            year = int(data['birth_year'])
            current_year = datetime.now().year
            if not (1800 <= year <= current_year):
                errors.append('Invalid birth year')
        except (ValueError, TypeError):
            errors.append('Birth year must be a number')
    
    if 'nationality' in data and len(data['nationality'].strip()) < 1:
        errors.append('Nationality cannot be empty')
    
    return errors


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


def add_book_routes(app: Flask) -> None:
    """
    Add RESTful routes for book management.
    """
    @app.route('/api/books', methods=['GET'])
    def get_books():
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        title_filter = request.args.get('title', '').lower()
        author_filter = request.args.get('author', '').lower()
        genre_filter = request.args.get('genre', '')
        available_filter = request.args.get('available', '')
        sort_by = request.args.get('sort', 'id')
        sort_order = request.args.get('order', 'asc')
        
        # Validate pagination parameters
        if page < 1:
            page = 1
        if per_page < 1 or per_page > 100:
            per_page = 10
        
        # Start with all books
        filtered_books = books.copy()
        
        # Apply filters
        if title_filter:
            filtered_books = [b for b in filtered_books 
                            if title_filter in b['title'].lower()]
        
        if author_filter:
            filtered_books = [b for b in filtered_books 
                            if author_filter in b['author'].lower()]
        
        if genre_filter:
            filtered_books = [b for b in filtered_books 
                            if b['genre'].lower() == genre_filter.lower()]
        
        if available_filter.lower() in ['true', 'false']:
            available_bool = available_filter.lower() == 'true'
            filtered_books = [b for b in filtered_books 
                            if b['available'] == available_bool]
        
        # Apply sorting
        reverse = sort_order.lower() == 'desc'
        if sort_by in ['id', 'title', 'author', 'published_year']:
            filtered_books.sort(key=lambda x: x[sort_by], reverse=reverse)
        
        # Apply pagination
        total = len(filtered_books)
        start = (page - 1) * per_page
        end = start + per_page
        paginated_books = filtered_books[start:end]
        
        return jsonify({
            'books': paginated_books,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'pages': math.ceil(total / per_page) if total > 0 else 0
            }
        })
    
    @app.route('/api/books/<int:book_id>', methods=['GET'])
    def get_book(book_id):
        book = find_book_by_id(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        return jsonify(book)
    
    @app.route('/api/books', methods=['POST'])
    def create_book():
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['title', 'author', 'isbn', 'published_year', 'genre']
        errors = validate_book_data(data, required_fields)
        
        if errors:
            return jsonify({'error': 'Validation failed', 'details': errors}), 422
        
        # Check for duplicate ISBN
        if any(book['isbn'] == data['isbn'] for book in books):
            return jsonify({'error': 'Book with this ISBN already exists'}), 409
        
        # Create new book
        new_book = {
            'id': get_next_book_id(),
            'title': data['title'].strip(),
            'author': data['author'].strip(),
            'isbn': data['isbn'],
            'published_year': int(data['published_year']),
            'genre': data['genre'].strip(),
            'available': data.get('available', True),
            'created_at': datetime.now().isoformat()
        }
        
        books.append(new_book)
        return jsonify(new_book), 201
    
    @app.route('/api/books/<int:book_id>', methods=['PUT'])
    def update_book(book_id):
        book = find_book_by_id(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields for PUT (complete replacement)
        required_fields = ['title', 'author', 'isbn', 'published_year', 'genre']
        errors = validate_book_data(data, required_fields)
        
        if errors:
            return jsonify({'error': 'Validation failed', 'details': errors}), 422
        
        # Check for duplicate ISBN (excluding current book)
        if any(b['isbn'] == data['isbn'] and b['id'] != book_id for b in books):
            return jsonify({'error': 'Book with this ISBN already exists'}), 409
        
        # Update book
        book.update({
            'title': data['title'].strip(),
            'author': data['author'].strip(),
            'isbn': data['isbn'],
            'published_year': int(data['published_year']),
            'genre': data['genre'].strip(),
            'available': data.get('available', book['available']),
            'updated_at': datetime.now().isoformat()
        })
        
        return jsonify(book)
    
    @app.route('/api/books/<int:book_id>', methods=['PATCH'])
    def patch_book(book_id):
        book = find_book_by_id(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate provided fields only
        errors = validate_book_data(data)
        if errors:
            return jsonify({'error': 'Validation failed', 'details': errors}), 422
        
        # Check for duplicate ISBN if ISBN is being updated
        if 'isbn' in data and any(b['isbn'] == data['isbn'] and b['id'] != book_id for b in books):
            return jsonify({'error': 'Book with this ISBN already exists'}), 409
        
        # Update only provided fields
        if 'title' in data:
            book['title'] = data['title'].strip()
        if 'author' in data:
            book['author'] = data['author'].strip()
        if 'isbn' in data:
            book['isbn'] = data['isbn']
        if 'published_year' in data:
            book['published_year'] = int(data['published_year'])
        if 'genre' in data:
            book['genre'] = data['genre'].strip()
        if 'available' in data:
            book['available'] = data['available']
        
        book['updated_at'] = datetime.now().isoformat()
        
        return jsonify(book)
    
    @app.route('/api/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        global books
        book = find_book_by_id(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        
        books = [b for b in books if b['id'] != book_id]
        return '', 204


def add_author_routes(app: Flask) -> None:
    """
    Add RESTful routes for author management.
    """
    @app.route('/api/authors', methods=['GET'])
    def get_authors():
        return jsonify({'authors': authors})
    
    @app.route('/api/authors/<int:author_id>', methods=['GET'])
    def get_author(author_id):
        author = find_author_by_id(author_id)
        if not author:
            return jsonify({'error': 'Author not found'}), 404
        return jsonify(author)
    
    @app.route('/api/authors', methods=['POST'])
    def create_author():
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['name', 'birth_year', 'nationality']
        errors = validate_author_data(data, required_fields)
        
        if errors:
            return jsonify({'error': 'Validation failed', 'details': errors}), 422
        
        # Check for duplicate name
        if any(author['name'].lower() == data['name'].lower() for author in authors):
            return jsonify({'error': 'Author with this name already exists'}), 409
        
        # Create new author
        new_author = {
            'id': get_next_author_id(),
            'name': data['name'].strip(),
            'birth_year': int(data['birth_year']),
            'nationality': data['nationality'].strip(),
            'created_at': datetime.now().isoformat()
        }
        
        authors.append(new_author)
        return jsonify(new_author), 201
    
    @app.route('/api/authors/<int:author_id>', methods=['PUT'])
    def update_author(author_id):
        author = find_author_by_id(author_id)
        if not author:
            return jsonify({'error': 'Author not found'}), 404
        
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['name', 'birth_year', 'nationality']
        errors = validate_author_data(data, required_fields)
        
        if errors:
            return jsonify({'error': 'Validation failed', 'details': errors}), 422
        
        # Check for duplicate name (excluding current author)
        if any(a['name'].lower() == data['name'].lower() and a['id'] != author_id for a in authors):
            return jsonify({'error': 'Author with this name already exists'}), 409
        
        # Update author
        author.update({
            'name': data['name'].strip(),
            'birth_year': int(data['birth_year']),
            'nationality': data['nationality'].strip(),
            'updated_at': datetime.now().isoformat()
        })
        
        return jsonify(author)
    
    @app.route('/api/authors/<int:author_id>', methods=['DELETE'])
    def delete_author(author_id):
        global authors
        author = find_author_by_id(author_id)
        if not author:
            return jsonify({'error': 'Author not found'}), 404
        
        authors = [a for a in authors if a['id'] != author_id]
        return '', 204
    
    @app.route('/api/authors/<int:author_id>/books', methods=['GET'])
    def get_author_books(author_id):
        author = find_author_by_id(author_id)
        if not author:
            return jsonify({'error': 'Author not found'}), 404
        
        author_books = [book for book in books if book['author'].lower() == author['name'].lower()]
        return jsonify({
            'author': author,
            'books': author_books,
            'total_books': len(author_books)
        })


def add_validation_helpers(app: Flask) -> None:
    """
    Add validation helper functions for the API.
    """
    # Validation functions are already defined above
    # This function could add them to the app context if needed
    app.validate_book_data = validate_book_data
    app.validate_author_data = validate_author_data
    app.validate_isbn = validate_isbn
    app.validate_year = validate_year


def add_error_handlers(app: Flask) -> None:
    """
    Add comprehensive error handlers for the API.
    """
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'error': 'Bad Request',
            'message': 'The request could not be understood by the server',
            'status_code': 400
        }), 400
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Not Found',
            'message': 'The requested resource was not found',
            'status_code': 404
        }), 404
    
    @app.errorhandler(409)
    def conflict(error):
        return jsonify({
            'error': 'Conflict',
            'message': 'The request conflicts with the current state of the resource',
            'status_code': 409
        }), 409
    
    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'error': 'Unprocessable Entity',
            'message': 'The request was well-formed but contains semantic errors',
            'status_code': 422
        }), 422
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An internal server error occurred',
            'status_code': 500
        }), 500


def add_filtering_and_pagination(app: Flask) -> None:
    """
    Add filtering and pagination support to the books endpoint.
    """
    # This functionality is already implemented in the add_book_routes function
    # The GET /api/books route includes filtering and pagination
    pass


def add_api_versioning(app: Flask) -> None:
    """
    Add API versioning support using URL prefixes.
    """
    # Version 1 API (basic functionality)
    v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
    
    @v1.route('/books', methods=['GET'])
    def get_books_v1():
        return jsonify({'books': books, 'version': '1.0'})
    
    @v1.route('/books/<int:book_id>', methods=['GET'])
    def get_book_v1(book_id):
        book = find_book_by_id(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        return jsonify(book)
    
    # Version 2 API (enhanced functionality)
    v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')
    
    @v2.route('/books', methods=['GET'])
    def get_books_v2():
        # Enhanced version with additional metadata
        enhanced_books = []
        for book in books:
            enhanced_book = book.copy()
            enhanced_book['metadata'] = {
                'version': '2.0',
                'enhanced': True,
                'word_count_estimate': len(book['title'].split()) * 50000  # Rough estimate
            }
            enhanced_books.append(enhanced_book)
        
        return jsonify({
            'books': enhanced_books,
            'version': '2.0',
            'total_count': len(enhanced_books)
        })
    
    @v2.route('/books/<int:book_id>', methods=['GET'])
    def get_book_v2(book_id):
        book = find_book_by_id(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        
        # Enhanced version with additional data
        enhanced_book = book.copy()
        enhanced_book['metadata'] = {
            'version': '2.0',
            'enhanced': True,
            'word_count_estimate': len(book['title'].split()) * 50000
        }
        
        return jsonify(enhanced_book)
    
    # Register blueprints
    app.register_blueprint(v1)
    app.register_blueprint(v2)


def create_complete_api() -> Flask:
    """
    Create a complete RESTful API with all features implemented.
    """
    app = create_book_api()
    
    add_book_routes(app)
    add_author_routes(app)
    add_validation_helpers(app)
    add_error_handlers(app)
    add_filtering_and_pagination(app)
    add_api_versioning(app)
    
    return app


# Test functions (same as in exercise file)
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
    add_book_routes(app)
    add_error_handlers(app)
    
    with app.test_client() as client:
        response = client.get('/api/books')
        assert response.status_code == 200, "GET /api/books should return 200"
        assert response.is_json, "Response should be JSON"
        
        response = client.get('/api/books/1')
        assert response.status_code == 200, "GET /api/books/1 should return 200"
        
        response = client.get('/api/books/999')
        assert response.status_code == 404, "GET /api/books/999 should return 404"
        
        new_book = {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '978-0-123456-78-0',
            'published_year': 2023,
            'genre': 'Test'
        }
        response = client.post('/api/books', json=new_book)
        assert response.status_code == 201, "POST /api/books should return 201"
        
        invalid_book = {'title': 'Incomplete Book'}
        response = client.post('/api/books', json=invalid_book)
        assert response.status_code in [400, 422], "POST with invalid data should return 400 or 422"
    
    print("✓ Book routes test passed")


def test_author_routes():
    """Test author CRUD operations"""
    print("Testing author routes...")
    
    app = create_book_api()
    add_author_routes(app)
    add_error_handlers(app)
    
    with app.test_client() as client:
        response = client.get('/api/authors')
        assert response.status_code == 200, "GET /api/authors should return 200"
        
        response = client.get('/api/authors/1')
        assert response.status_code == 200, "GET /api/authors/1 should return 200"
        
        new_author = {
            'name': 'Test Author',
            'birth_year': 1980,
            'nationality': 'American'
        }
        response = client.post('/api/authors', json=new_author)
        assert response.status_code == 201, "POST /api/authors should return 201"
        
        response = client.get('/api/authors/1/books')
        assert response.status_code == 200, "GET /api/authors/1/books should return 200"
    
    print("✓ Author routes test passed")


def test_error_handling():
    """Test error handling"""
    print("Testing error handling...")
    
    app = create_book_api()
    add_book_routes(app)
    add_error_handlers(app)
    
    with app.test_client() as client:
        response = client.get('/api/nonexistent')
        assert response.status_code == 404, "Non-existent endpoint should return 404"
        
        response = client.post('/api/books', data='invalid json', 
                             content_type='application/json')
        assert response.status_code == 400, "Invalid JSON should return 400"
    
    print("✓ Error handling test passed")


def test_filtering_and_pagination():
    """Test filtering and pagination"""
    print("Testing filtering and pagination...")
    
    app = create_book_api()
    add_book_routes(app)
    add_filtering_and_pagination(app)
    
    with app.test_client() as client:
        response = client.get('/api/books?page=1&per_page=1')
        assert response.status_code == 200, "Pagination should work"
        
        response = client.get('/api/books?genre=Programming')
        assert response.status_code == 200, "Filtering should work"
        
        response = client.get('/api/books?sort=title&order=asc')
        assert response.status_code == 200, "Sorting should work"
    
    print("✓ Filtering and pagination test passed")


def run_all_tests():
    """Run all test functions"""
    print("Running RESTful APIs Solution Tests")
    print("=" * 40)
    
    try:
        test_api_creation()
        test_book_routes()
        test_author_routes()
        test_error_handling()
        test_filtering_and_pagination()
        
        print("\n" + "=" * 40)
        print("All tests passed! 🎉")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


def run_api_server():
    """Run the complete API server for manual testing"""
    app = create_complete_api()
    
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
    print("\nVersioned APIs:")
    print("- GET /api/v1/books : Version 1 books API")
    print("- GET /api/v2/books : Version 2 books API (enhanced)")
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