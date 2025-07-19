# Database Integration with Flask: Building Persistent Web Applications

## Introduction

Most web applications need to store and retrieve data persistently. While we've been using in-memory data structures in previous lessons, real applications require databases. In this lesson, you'll learn how to integrate databases with Flask applications using SQLAlchemy, Python's most popular Object-Relational Mapping (ORM) library.

## Why Use a Database?

- **Persistence**: Data survives application restarts
- **Concurrency**: Multiple users can access data simultaneously
- **Integrity**: Enforce data consistency and relationships
- **Scalability**: Handle large amounts of data efficiently
- **Querying**: Complex data retrieval and filtering
- **Transactions**: Ensure data consistency across operations

## Database Options

### SQLite
- **Pros**: Lightweight, no setup required, perfect for development
- **Cons**: Limited concurrency, not suitable for high-traffic production
- **Use case**: Development, small applications, prototyping

### PostgreSQL
- **Pros**: Full-featured, excellent performance, strong consistency
- **Cons**: More complex setup
- **Use case**: Production applications, complex queries

### MySQL
- **Pros**: Widely used, good performance, mature ecosystem
- **Cons**: Some limitations compared to PostgreSQL
- **Use case**: Web applications, content management systems

## SQLAlchemy Overview

SQLAlchemy is a Python SQL toolkit and ORM that provides:

- **Core**: Expression language for SQL operations
- **ORM**: Object-Relational Mapping for working with Python objects
- **Connection pooling**: Efficient database connections
- **Migration support**: Database schema versioning

## Flask-SQLAlchemy Setup

### Installation

```bash
pip install Flask-SQLAlchemy
```

### Basic Configuration

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)
```

### Database URI Formats

```python
# SQLite (file-based)
'sqlite:///app.db'  # Relative path
'sqlite:////absolute/path/to/app.db'  # Absolute path
'sqlite:///:memory:'  # In-memory database

# PostgreSQL
'postgresql://username:password@localhost/database_name'
'postgresql://user:pass@localhost:5432/mydb'

# MySQL
'mysql://username:password@localhost/database_name'
'mysql+pymysql://user:pass@localhost:3306/mydb'
```

## Defining Models

### Basic Model

```python
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<User {self.username}>'
```

### Column Types

```python
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2))  # 10 digits, 2 decimal places
    in_stock = db.Column(db.Boolean, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # JSON column (PostgreSQL, MySQL 5.7+)
    metadata = db.Column(db.JSON)
```

### Common Column Options

```python
class Example(db.Model):
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Unique constraint
    email = db.Column(db.String(120), unique=True)
    
    # Not null constraint
    name = db.Column(db.String(80), nullable=False)
    
    # Default value
    status = db.Column(db.String(20), default='active')
    
    # Index for faster queries
    username = db.Column(db.String(80), index=True)
    
    # Foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
```

## Relationships

### One-to-Many Relationship

```python
class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    # One-to-many relationship
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    # The backref creates a 'category' attribute on Product
```

### Many-to-Many Relationship

```python
# Association table
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # Many-to-many relationship
    roles = db.relationship('Role', secondary=user_roles, lazy='subquery',
                           backref=db.backref('users', lazy=True))

class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
```

### One-to-One Relationship

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # One-to-one relationship
    profile = db.relationship('UserProfile', backref='user', uselist=False)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    bio = db.Column(db.Text)
```

## Database Operations

### Creating Tables

```python
# Create all tables
with app.app_context():
    db.create_all()

# Drop all tables (be careful!)
with app.app_context():
    db.drop_all()
```

### CRUD Operations

#### Create (Insert)

```python
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Create new user instance
    user = User(
        username=data['username'],
        email=data['email']
    )
    
    # Add to session and commit
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 201

# Bulk insert
def create_multiple_users(users_data):
    users = [User(username=data['username'], email=data['email']) 
             for data in users_data]
    
    db.session.add_all(users)
    db.session.commit()
    
    return users
```

#### Read (Query)

```python
# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email
    } for user in users])

# Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })

# Query with filters
@app.route('/users/search', methods=['GET'])
def search_users():
    username = request.args.get('username')
    email = request.args.get('email')
    
    query = User.query
    
    if username:
        query = query.filter(User.username.like(f'%{username}%'))
    
    if email:
        query = query.filter(User.email == email)
    
    users = query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email
    } for user in users])
```

#### Update

```python
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    # Update fields
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.updated_at = datetime.utcnow()
    
    # Commit changes
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })

# Bulk update
def update_users_status(user_ids, status):
    User.query.filter(User.id.in_(user_ids)).update(
        {User.is_active: status}, 
        synchronize_session=False
    )
    db.session.commit()
```

#### Delete

```python
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    
    db.session.delete(user)
    db.session.commit()
    
    return '', 204

# Bulk delete
def delete_inactive_users():
    User.query.filter(User.is_active == False).delete()
    db.session.commit()
```

## Advanced Querying

### Filtering and Ordering

```python
# Basic filters
users = User.query.filter(User.is_active == True).all()
users = User.query.filter(User.username.like('%john%')).all()
users = User.query.filter(User.created_at > datetime(2024, 1, 1)).all()

# Multiple conditions
users = User.query.filter(
    User.is_active == True,
    User.created_at > datetime(2024, 1, 1)
).all()

# OR conditions
from sqlalchemy import or_
users = User.query.filter(
    or_(User.username == 'john', User.email.like('%@gmail.com'))
).all()

# Ordering
users = User.query.order_by(User.username).all()
users = User.query.order_by(User.created_at.desc()).all()

# Limiting and pagination
users = User.query.limit(10).all()
users = User.query.offset(20).limit(10).all()

# Pagination helper
page = request.args.get('page', 1, type=int)
per_page = 10
users = User.query.paginate(
    page=page, 
    per_page=per_page, 
    error_out=False
)
```

### Joins and Relationships

```python
# Eager loading with join
users_with_profiles = User.query.join(UserProfile).all()

# Left outer join
users_with_profiles = User.query.outerjoin(UserProfile).all()

# Query with relationship data
products_with_categories = Product.query.join(Category).add_columns(
    Product.name, Category.name.label('category_name')
).all()

# Using relationship attributes
user = User.query.first()
user_products = user.products  # Lazy loading

# Eager loading to avoid N+1 queries
from sqlalchemy.orm import joinedload
users = User.query.options(joinedload(User.products)).all()
```

### Aggregation

```python
from sqlalchemy import func

# Count
user_count = User.query.count()
active_users = User.query.filter(User.is_active == True).count()

# Group by and aggregate
category_counts = db.session.query(
    Category.name,
    func.count(Product.id).label('product_count')
).join(Product).group_by(Category.name).all()

# Having clause
popular_categories = db.session.query(
    Category.name,
    func.count(Product.id).label('product_count')
).join(Product).group_by(Category.name).having(
    func.count(Product.id) > 5
).all()
```

## Error Handling and Transactions

### Transaction Management

```python
from sqlalchemy.exc import IntegrityError

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    try:
        user = User(
            username=data['username'],
            email=data['email']
        )
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({'id': user.id, 'username': user.username}), 201
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username or email already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred'}), 500

# Manual transaction control
def transfer_funds(from_account_id, to_account_id, amount):
    try:
        from_account = Account.query.get(from_account_id)
        to_account = Account.query.get(to_account_id)
        
        if from_account.balance < amount:
            raise ValueError("Insufficient funds")
        
        from_account.balance -= amount
        to_account.balance += amount
        
        db.session.commit()
        return True
        
    except Exception as e:
        db.session.rollback()
        raise e
```

### Context Managers

```python
from contextlib import contextmanager

@contextmanager
def db_transaction():
    try:
        db.session.begin()
        yield db.session
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

# Usage
def create_user_with_profile(user_data, profile_data):
    with db_transaction():
        user = User(**user_data)
        db.session.add(user)
        db.session.flush()  # Get the user ID
        
        profile = UserProfile(user_id=user.id, **profile_data)
        db.session.add(profile)
```

## Database Migrations

### Flask-Migrate Setup

```bash
pip install Flask-Migrate
```

```python
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

### Migration Commands

```bash
# Initialize migration repository
flask db init

# Create a new migration
flask db migrate -m "Add user table"

# Apply migrations
flask db upgrade

# Downgrade to previous version
flask db downgrade

# Show current migration version
flask db current

# Show migration history
flask db history
```

### Custom Migration

```python
# In a migration file
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Add a new column
    op.add_column('users', sa.Column('last_login', sa.DateTime()))
    
    # Create an index
    op.create_index('idx_users_email', 'users', ['email'])

def downgrade():
    # Remove the column
    op.drop_column('users', 'last_login')
    
    # Drop the index
    op.drop_index('idx_users_email', 'users')
```

## Performance Optimization

### Query Optimization

```python
# Use select_related to avoid N+1 queries
from sqlalchemy.orm import selectinload

# Bad: N+1 query problem
users = User.query.all()
for user in users:
    print(user.profile.first_name)  # Each access hits the database

# Good: Eager loading
users = User.query.options(selectinload(User.profile)).all()
for user in users:
    print(user.profile.first_name)  # No additional queries

# Load only needed columns
users = User.query.with_entities(User.id, User.username).all()
```

### Indexing

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    # Composite index
    __table_args__ = (
        db.Index('idx_username_email', 'username', 'email'),
    )
```

### Connection Pooling

```python
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'pool_recycle': 120,
    'pool_pre_ping': True,
    'max_overflow': 20
}
```

## Testing with Databases

### Test Configuration

```python
import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(client):
    response = client.post('/users', json={
        'username': 'testuser',
        'email': 'test@example.com'
    })
    
    assert response.status_code == 201
    data = response.get_json()
    assert data['username'] == 'testuser'
```

### Database Fixtures

```python
@pytest.fixture
def sample_users(app):
    with app.app_context():
        users = [
            User(username='user1', email='user1@example.com'),
            User(username='user2', email='user2@example.com')
        ]
        
        db.session.add_all(users)
        db.session.commit()
        
        return users

def test_get_users(client, sample_users):
    response = client.get('/users')
    assert response.status_code == 200
    
    data = response.get_json()
    assert len(data) == 2
```

## Best Practices

### 1. Model Design

```python
class BaseModel(db.Model):
    """Base model with common fields"""
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class User(BaseModel):
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
```

### 2. Repository Pattern

```python
class UserRepository:
    @staticmethod
    def create(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def update(user, **kwargs):
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return user
    
    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()

# Usage in routes
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserRepository.create(data['username'], data['email'])
    return jsonify(user.to_dict()), 201
```

### 3. Environment-based Configuration

```python
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
```

### 4. Connection Management

```python
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

# For long-running operations
def process_large_dataset():
    try:
        # Process data in chunks
        chunk_size = 1000
        offset = 0
        
        while True:
            users = User.query.offset(offset).limit(chunk_size).all()
            if not users:
                break
                
            # Process users
            for user in users:
                # Do something with user
                pass
            
            # Clear session to free memory
            db.session.expunge_all()
            offset += chunk_size
            
    except Exception as e:
        db.session.rollback()
        raise e
```

## Summary

Database integration is essential for building robust web applications. Key concepts:

1. **ORM Benefits**: Object-relational mapping simplifies database operations
2. **Model Definition**: Define database schema using Python classes
3. **Relationships**: Model data relationships (one-to-many, many-to-many)
4. **CRUD Operations**: Create, read, update, delete data
5. **Query Optimization**: Use eager loading and indexing for performance
6. **Transactions**: Ensure data consistency with proper transaction handling
7. **Migrations**: Version control for database schema changes
8. **Testing**: Use in-memory databases for testing
9. **Best Practices**: Follow patterns for maintainable code
10. **Error Handling**: Gracefully handle database errors

## Next Steps

In the next lesson, we'll build a complete RESTful API service mini-project that combines all the concepts we've learned: Flask, RESTful APIs, and database integration.