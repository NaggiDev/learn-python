"""
Solution: Database Integration with Flask

This file contains the complete solutions for the database integration exercise.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import func, desc, or_
from datetime import datetime
from typing import Dict, Any, List, Optional
import hashlib


# Initialize SQLAlchemy
db = SQLAlchemy()


def create_database_app() -> Flask:
    """Create a Flask application with database configuration."""
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    
    # Initialize SQLAlchemy with app
    db.init_app(app)
    
    return app


# Models
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    posts = db.relationship('Post', backref='author', lazy=True, cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='author', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self, include_posts=False):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }
        if include_posts:
            data['posts'] = [post.to_dict() for post in self.posts]
        return data
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()


class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    posts = db.relationship('Post', backref='category', lazy=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'
    
    def to_dict(self, include_posts=False):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'post_count': len(self.posts)
        }
        if include_posts:
            data['posts'] = [post.to_dict() for post in self.posts]
        return data


class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published = db.Column(db.Boolean, default=True, index=True)
    
    # Relationships
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Post {self.title}>'
    
    def to_dict(self, include_comments=False, include_author=True, include_category=True):
        data = {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'published': self.published,
            'comment_count': len(self.comments)
        }
        
        if include_author:
            data['author'] = {
                'id': self.author.id,
                'username': self.author.username
            }
        
        if include_category:
            data['category'] = {
                'id': self.category.id,
                'name': self.category.name
            }
        
        if include_comments:
            data['comments'] = [comment.to_dict() for comment in self.comments]
        
        return data


class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    def __repr__(self):
        return f'<Comment {self.id}>'
    
    def to_dict(self, include_author=True, include_post=False):
        data = {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }
        
        if include_author:
            data['author'] = {
                'id': self.author.id,
                'username': self.author.username
            }
        
        if include_post:
            data['post'] = {
                'id': self.post.id,
                'title': self.post.title
            }
        
        return data


def define_models() -> None:
    """Define database models for a blog application."""
    # Models are already defined above as classes
    pass

def 
validate_user_data(data: Dict[str, Any], required_fields: List[str] = None) -> List[str]:
    """Validate user data"""
    errors = []
    
    if required_fields:
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f'{field} is required')
    
    if 'username' in data:
        if len(data['username']) < 3:
            errors.append('Username must be at least 3 characters long')
        if len(data['username']) > 80:
            errors.append('Username must be less than 80 characters')
    
    if 'email' in data:
        if '@' not in data['email'] or '.' not in data['email']:
            errors.append('Invalid email format')
    
    if 'password' in data:
        if len(data['password']) < 6:
            errors.append('Password must be at least 6 characters long')
    
    return errors


def add_user_routes(app: Flask) -> None:
    """Add CRUD routes for user management."""
    @app.route('/api/users', methods=['GET'])
    def get_users():
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        if per_page > 100:
            per_page = 100
        
        users = User.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'users': [user.to_dict() for user in users.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': users.total,
                'pages': users.pages
            }
        })
    
    @app.route('/api/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())
    
    @app.route('/api/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate data
        required_fields = ['username', 'email', 'password']
        errors = validate_user_data(data, required_fields)
        if errors:
            return jsonify({'error': 'Validation failed', 'details': errors}), 422
        
        try:
            # Check for existing user
            if User.query.filter_by(username=data['username']).first():
                return jsonify({'error': 'Username already exists'}), 409
            
            if User.query.filter_by(email=data['email']).first():
                return jsonify({'error': 'Email already exists'}), 409
            
            # Create user
            user = User(
                username=data['username'],
                email=data['email']
            )
            user.set_password(data['password'])
            
            db.session.add(user)
            db.session.commit()
            
            return jsonify(user.to_dict()), 201
            
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'User already exists'}), 409
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        try:
            if 'username' in data and data['username'] != user.username:
                if User.query.filter_by(username=data['username']).first():
                    return jsonify({'error': 'Username already exists'}), 409
                user.username = data['username']
            
            if 'email' in data and data['email'] != user.email:
                if User.query.filter_by(email=data['email']).first():
                    return jsonify({'error': 'Email already exists'}), 409
                user.email = data['email']
            
            if 'password' in data:
                user.set_password(data['password'])
            
            if 'is_active' in data:
                user.is_active = data['is_active']
            
            db.session.commit()
            return jsonify(user.to_dict())
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        
        try:
            db.session.delete(user)
            db.session.commit()
            return '', 204
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/users/<int:user_id>/posts', methods=['GET'])
    def get_user_posts(user_id):
        user = User.query.get_or_404(user_id)
        posts = Post.query.filter_by(user_id=user_id).order_by(Post.created_at.desc()).all()
        
        return jsonify({
            'user': user.to_dict(),
            'posts': [post.to_dict() for post in posts],
            'total_posts': len(posts)
        })


def add_post_routes(app: Flask) -> None:
    """Add CRUD routes for post management."""
    @app.route('/api/posts', methods=['GET'])
    def get_posts():
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        category_id = request.args.get('category_id', type=int)
        published = request.args.get('published', type=bool)
        
        if per_page > 100:
            per_page = 100
        
        query = Post.query
        
        if category_id:
            query = query.filter_by(category_id=category_id)
        
        if published is not None:
            query = query.filter_by(published=published)
        
        query = query.order_by(Post.created_at.desc())
        
        posts = query.paginate(page=page, per_page=per_page, error_out=False)
        
        return jsonify({
            'posts': [post.to_dict() for post in posts.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': posts.total,
                'pages': posts.pages
            }
        })
    
    @app.route('/api/posts/<int:post_id>', methods=['GET'])
    def get_post(post_id):
        post = Post.query.get_or_404(post_id)
        return jsonify(post.to_dict(include_comments=True))
    
    @app.route('/api/posts', methods=['POST'])
    def create_post():
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        required_fields = ['title', 'content', 'user_id', 'category_id']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 422
        
        # Verify user and category exist
        user = User.query.get(data['user_id'])
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({'error': 'Category not found'}), 404
        
        try:
            post = Post(
                title=data['title'],
                content=data['content'],
                user_id=data['user_id'],
                category_id=data['category_id'],
                published=data.get('published', True)
            )
            
            db.session.add(post)
            db.session.commit()
            
            return jsonify(post.to_dict()), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/posts/<int:post_id>', methods=['PUT'])
    def update_post(post_id):
        post = Post.query.get_or_404(post_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        try:
            if 'title' in data:
                post.title = data['title']
            
            if 'content' in data:
                post.content = data['content']
            
            if 'category_id' in data:
                category = Category.query.get(data['category_id'])
                if not category:
                    return jsonify({'error': 'Category not found'}), 404
                post.category_id = data['category_id']
            
            if 'published' in data:
                post.published = data['published']
            
            post.updated_at = datetime.utcnow()
            
            db.session.commit()
            return jsonify(post.to_dict())
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/posts/<int:post_id>', methods=['DELETE'])
    def delete_post(post_id):
        post = Post.query.get_or_404(post_id)
        
        try:
            db.session.delete(post)
            db.session.commit()
            return '', 204
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/posts/search', methods=['GET'])
    def search_posts():
        query_text = request.args.get('q', '').strip()
        if not query_text:
            return jsonify({'error': 'Query parameter "q" is required'}), 400
        
        posts = Post.query.filter(
            or_(
                Post.title.contains(query_text),
                Post.content.contains(query_text)
            )
        ).order_by(Post.created_at.desc()).all()
        
        return jsonify({
            'query': query_text,
            'posts': [post.to_dict() for post in posts],
            'total_results': len(posts)
        })


def add_category_routes(app: Flask) -> None:
    """Add CRUD routes for category management."""
    @app.route('/api/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.order_by(Category.name).all()
        return jsonify({
            'categories': [category.to_dict() for category in categories]
        })
    
    @app.route('/api/categories/<int:category_id>', methods=['GET'])
    def get_category(category_id):
        category = Category.query.get_or_404(category_id)
        return jsonify(category.to_dict())
    
    @app.route('/api/categories', methods=['POST'])
    def create_category():
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        if 'name' not in data or not data['name']:
            return jsonify({'error': 'Name is required'}), 422
        
        try:
            if Category.query.filter_by(name=data['name']).first():
                return jsonify({'error': 'Category already exists'}), 409
            
            category = Category(
                name=data['name'],
                description=data.get('description', '')
            )
            
            db.session.add(category)
            db.session.commit()
            
            return jsonify(category.to_dict()), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/categories/<int:category_id>', methods=['PUT'])
    def update_category(category_id):
        category = Category.query.get_or_404(category_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        try:
            if 'name' in data:
                existing = Category.query.filter_by(name=data['name']).first()
                if existing and existing.id != category_id:
                    return jsonify({'error': 'Category name already exists'}), 409
                category.name = data['name']
            
            if 'description' in data:
                category.description = data['description']
            
            db.session.commit()
            return jsonify(category.to_dict())
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/categories/<int:category_id>', methods=['DELETE'])
    def delete_category(category_id):
        category = Category.query.get_or_404(category_id)
        
        if category.posts:
            return jsonify({
                'error': 'Cannot delete category with existing posts',
                'post_count': len(category.posts)
            }), 409
        
        try:
            db.session.delete(category)
            db.session.commit()
            return '', 204
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/categories/<int:category_id>/posts', methods=['GET'])
    def get_category_posts(category_id):
        category = Category.query.get_or_404(category_id)
        posts = Post.query.filter_by(category_id=category_id).order_by(Post.created_at.desc()).all()
        
        return jsonify({
            'category': category.to_dict(),
            'posts': [post.to_dict() for post in posts],
            'total_posts': len(posts)
        })


def add_comment_routes(app: Flask) -> None:
    """Add CRUD routes for comment management."""
    @app.route('/api/comments', methods=['GET'])
    def get_comments():
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        if per_page > 100:
            per_page = 100
        
        comments = Comment.query.order_by(Comment.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'comments': [comment.to_dict(include_post=True) for comment in comments.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': comments.total,
                'pages': comments.pages
            }
        })
    
    @app.route('/api/comments/<int:comment_id>', methods=['GET'])
    def get_comment(comment_id):
        comment = Comment.query.get_or_404(comment_id)
        return jsonify(comment.to_dict(include_post=True))
    
    @app.route('/api/comments', methods=['POST'])
    def create_comment():
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        required_fields = ['content', 'user_id', 'post_id']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 422
        
        # Verify user and post exist
        user = User.query.get(data['user_id'])
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        post = Post.query.get(data['post_id'])
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        try:
            comment = Comment(
                content=data['content'],
                user_id=data['user_id'],
                post_id=data['post_id']
            )
            
            db.session.add(comment)
            db.session.commit()
            
            return jsonify(comment.to_dict()), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/comments/<int:comment_id>', methods=['PUT'])
    def update_comment(comment_id):
        comment = Comment.query.get_or_404(comment_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        if 'content' in data:
            if len(data['content']) < 1:
                return jsonify({'error': 'Content cannot be empty'}), 422
            comment.content = data['content']
        
        try:
            db.session.commit()
            return jsonify(comment.to_dict())
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/comments/<int:comment_id>', methods=['DELETE'])
    def delete_comment(comment_id):
        comment = Comment.query.get_or_404(comment_id)
        
        try:
            db.session.delete(comment)
            db.session.commit()
            return '', 204
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'An error occurred'}), 500
    
    @app.route('/api/posts/<int:post_id>/comments', methods=['GET'])
    def get_post_comments(post_id):
        post = Post.query.get_or_404(post_id)
        comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.asc()).all()
        
        return jsonify({
            'post': post.to_dict(include_comments=False),
            'comments': [comment.to_dict() for comment in comments],
            'total_comments': len(comments)
        })


def add_database_utilities(app: Flask) -> None:
    """Add utility functions for database operations."""
    @app.route('/api/init-db', methods=['POST'])
    def init_database():
        try:
            db.create_all()
            return jsonify({'message': 'Database initialized successfully'}), 200
        except Exception as e:
            return jsonify({'error': 'Failed to initialize database'}), 500
    
    @app.route('/api/seed-db', methods=['POST'])
    def seed_database():
        try:
            # Create sample categories
            categories = [
                Category(name='Technology', description='Posts about technology and programming'),
                Category(name='Science', description='Scientific articles and discoveries'),
                Category(name='Lifestyle', description='Lifestyle and personal development')
            ]
            
            for category in categories:
                if not Category.query.filter_by(name=category.name).first():
                    db.session.add(category)
            
            # Create sample users
            users_data = [
                {'username': 'alice', 'email': 'alice@example.com', 'password': 'password123'},
                {'username': 'bob', 'email': 'bob@example.com', 'password': 'password123'},
                {'username': 'charlie', 'email': 'charlie@example.com', 'password': 'password123'}
            ]
            
            for user_data in users_data:
                if not User.query.filter_by(username=user_data['username']).first():
                    user = User(username=user_data['username'], email=user_data['email'])
                    user.set_password(user_data['password'])
                    db.session.add(user)
            
            db.session.commit()
            
            # Create sample posts
            posts_data = [
                {
                    'title': 'Introduction to Flask',
                    'content': 'Flask is a lightweight web framework for Python...',
                    'username': 'alice',
                    'category': 'Technology'
                },
                {
                    'title': 'The Future of AI',
                    'content': 'Artificial Intelligence is rapidly evolving...',
                    'username': 'bob',
                    'category': 'Technology'
                }
            ]
            
            for post_data in posts_data:
                user = User.query.filter_by(username=post_data['username']).first()
                category = Category.query.filter_by(name=post_data['category']).first()
                
                if user and category and not Post.query.filter_by(title=post_data['title']).first():
                    post = Post(
                        title=post_data['title'],
                        content=post_data['content'],
                        user_id=user.id,
                        category_id=category.id
                    )
                    db.session.add(post)
            
            db.session.commit()
            
            return jsonify({'message': 'Database seeded successfully'}), 200
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Failed to seed database'}), 500
    
    @app.route('/api/health', methods=['GET'])
    def health_check():
        try:
            user_count = User.query.count()
            return jsonify({
                'status': 'healthy',
                'database': 'connected',
                'user_count': user_count
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'unhealthy',
                'database': 'disconnected',
                'error': str(e)
            }), 500


def add_advanced_queries(app: Flask) -> None:
    """Add routes that demonstrate advanced database queries."""
    @app.route('/api/stats', methods=['GET'])
    def get_stats():
        try:
            stats = {
                'users': {
                    'total': User.query.count(),
                    'active': User.query.filter_by(is_active=True).count()
                },
                'posts': {
                    'total': Post.query.count(),
                    'published': Post.query.filter_by(published=True).count()
                },
                'comments': {
                    'total': Comment.query.count()
                },
                'categories': {
                    'total': Category.query.count()
                }
            }
            
            return jsonify(stats)
            
        except Exception as e:
            return jsonify({'error': 'Failed to get statistics'}), 500
    
    @app.route('/api/popular-posts', methods=['GET'])
    def get_popular_posts():
        try:
            popular_posts = db.session.query(
                Post,
                func.count(Comment.id).label('comment_count')
            ).outerjoin(Comment).group_by(Post.id).order_by(
                desc('comment_count')
            ).limit(10).all()
            
            result = []
            for post, comment_count in popular_posts:
                post_dict = post.to_dict()
                post_dict['comment_count'] = comment_count
                result.append(post_dict)
            
            return jsonify({
                'popular_posts': result
            })
            
        except Exception as e:
            return jsonify({'error': 'Failed to get popular posts'}), 500
    
    @app.route('/api/active-users', methods=['GET'])
    def get_active_users():
        try:
            active_users = db.session.query(
                User,
                func.count(Post.id).label('post_count')
            ).outerjoin(Post).group_by(User.id).order_by(
                desc('post_count')
            ).limit(10).all()
            
            result = []
            for user, post_count in active_users:
                user_dict = user.to_dict()
                user_dict['post_count'] = post_count
                result.append(user_dict)
            
            return jsonify({
                'active_users': result
            })
            
        except Exception as e:
            return jsonify({'error': 'Failed to get active users'}), 500
    
    @app.route('/api/recent-activity', methods=['GET'])
    def get_recent_activity():
        try:
            recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
            recent_comments = Comment.query.order_by(Comment.created_at.desc()).limit(5).all()
            
            return jsonify({
                'recent_posts': [post.to_dict() for post in recent_posts],
                'recent_comments': [comment.to_dict(include_post=True) for comment in recent_comments]
            })
            
        except Exception as e:
            return jsonify({'error': 'Failed to get recent activity'}), 500


def add_error_handling(app: Flask) -> None:
    """Add comprehensive error handling for database operations."""
    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        db.session.rollback()
        return jsonify({
            'error': 'Database integrity error',
            'message': 'The operation violates database constraints'
        }), 409
    
    @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(e):
        db.session.rollback()
        return jsonify({
            'error': 'Database error',
            'message': 'A database error occurred'
        }), 500
    
    @app.errorhandler(404)
    def handle_not_found(e):
        return jsonify({
            'error': 'Not Found',
            'message': 'The requested resource was not found'
        }), 404


def create_complete_blog_app() -> Flask:
    """Create a complete blog application with database integration."""
    app = create_database_app()
    
    define_models()
    
    add_user_routes(app)
    add_post_routes(app)
    add_category_routes(app)
    add_comment_routes(app)
    add_database_utilities(app)
    add_advanced_queries(app)
    add_error_handling(app)
    
    return app


def init_database(app: Flask) -> None:
    """Initialize database tables"""
    with app.app_context():
        db.create_all()


def seed_database(app: Flask) -> None:
    """Seed database with sample data"""
    with app.app_context():
        if User.query.count() == 0:
            # Create categories
            tech_category = Category(name='Technology', description='Tech posts')
            lifestyle_category = Category(name='Lifestyle', description='Lifestyle posts')
            db.session.add_all([tech_category, lifestyle_category])
            
            # Create users
            alice = User(username='alice', email='alice@example.com')
            alice.set_password('password123')
            bob = User(username='bob', email='bob@example.com')
            bob.set_password('password123')
            db.session.add_all([alice, bob])
            
            db.session.commit()
            
            # Create posts
            post1 = Post(
                title='Flask Tutorial',
                content='Learn Flask web development...',
                user_id=alice.id,
                category_id=tech_category.id
            )
            post2 = Post(
                title='Healthy Living',
                content='Tips for a healthy lifestyle...',
                user_id=bob.id,
                category_id=lifestyle_category.id
            )
            db.session.add_all([post1, post2])
            
            db.session.commit()
            
            # Create comments
            comment1 = Comment(
                content='Great tutorial!',
                user_id=bob.id,
                post_id=post1.id
            )
            comment2 = Comment(
                content='Very helpful tips.',
                user_id=alice.id,
                post_id=post2.id
            )
            db.session.add_all([comment1, comment2])
            
            db.session.commit()


# Test functions
def test_app_creation():
    print("Testing database app creation...")
    app = create_database_app()
    assert app is not None, "Function should return a Flask app"
    assert isinstance(app, Flask), "Should return a Flask instance"
    assert 'SQLALCHEMY_DATABASE_URI' in app.config, "Should have database URI configured"
    print("✓ Database app creation test passed")


def test_model_definition():
    print("Testing model definitions...")
    app = create_database_app()
    with app.app_context():
        db.create_all()
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        expected_tables = ['users', 'categories', 'posts', 'comments']
        for table in expected_tables:
            assert table in tables, f"Table {table} should exist"
    print("✓ Model definition test passed")


def test_user_operations():
    print("Testing user operations...")
    app = create_complete_blog_app()
    with app.app_context():
        db.create_all()
        with app.test_client() as client:
            user_data = {
                'username': 'testuser',
                'email': 'test@example.com',
                'password': 'password123'
            }
            response = client.post('/api/users', json=user_data)
            assert response.status_code == 201, "User creation should return 201"
            
            response = client.get('/api/users')
            assert response.status_code == 200, "Get users should return 200"
            
            response = client.get('/api/users/1')
            assert response.status_code == 200, "Get specific user should return 200"
    print("✓ User operations test passed")


def test_post_operations():
    print("Testing post operations...")
    app = create_complete_blog_app()
    with app.app_context():
        db.create_all()
        seed_database(app)
        with app.test_client() as client:
            post_data = {
                'title': 'Test Post',
                'content': 'This is a test post content.',
                'user_id': 1,
                'category_id': 1
            }
            response = client.post('/api/posts', json=post_data)
            assert response.status_code == 201, "Post creation should return 201"
            
            response = client.get('/api/posts')
            assert response.status_code == 200, "Get posts should return 200"
    print("✓ Post operations test passed")


def test_relationships():
    print("Testing model relationships...")
    app = create_complete_blog_app()
    with app.app_context():
        db.create_all()
        seed_database(app)
        with app.test_client() as client:
            response = client.get('/api/users/1/posts')
            assert response.status_code == 200, "Get user posts should return 200"
            
            response = client.get('/api/categories/1/posts')
            assert response.status_code == 200, "Get category posts should return 200"
            
            response = client.get('/api/posts/1/comments')
            assert response.status_code == 200, "Get post comments should return 200"
    print("✓ Relationships test passed")


def test_advanced_queries():
    print("Testing advanced queries...")
    app = create_complete_blog_app()
    with app.app_context():
        db.create_all()
        seed_database(app)
        with app.test_client() as client:
            response = client.get('/api/stats')
            assert response.status_code == 200, "Get stats should return 200"
            
            response = client.get('/api/popular-posts')
            assert response.status_code == 200, "Get popular posts should return 200"
    print("✓ Advanced queries test passed")


def run_all_tests():
    print("Running Database Integration Solution Tests")
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
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


def run_blog_app():
    """Run the complete blog application for manual testing"""
    app = create_complete_blog_app()
    
    with app.app_context():
        db.create_all()
        seed_database(app)
    
    print("Starting Blog API server...")
    print("Visit http://127.0.0.1:5000 to test your API")
    print("\nKey endpoints:")
    print("- GET /api/users : List users")
    print("- POST /api/users : Create user")
    print("- GET /api/posts : List posts")
    print("- POST /api/posts : Create post")
    print("- GET /api/categories : List categories")
    print("- GET /api/stats : Database statistics")
    print("- POST /api/seed-db : Seed with sample data")
    
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run_blog_app()
    else:
        run_all_tests()