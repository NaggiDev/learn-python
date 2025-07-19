"""
Task Management API - Test Configuration

This module contains pytest fixtures and configuration for testing.
"""

import pytest
from app import create_app, db
from app.models.user import User
from app.models.category import Category


@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create test CLI runner."""
    return app.test_cli_runner()


@pytest.fixture
def sample_user(app):
    """Create a sample user for testing."""
    with app.app_context():
        user = User(
            username='testuser',
            email='test@example.com',
            first_name='Test',
            last_name='User',
            role='user'
        )
        user.set_password('TestPassword123!')
        
        db.session.add(user)
        db.session.commit()
        
        return user


@pytest.fixture
def admin_user(app):
    """Create an admin user for testing."""
    with app.app_context():
        admin = User(
            username='admin',
            email='admin@example.com',
            first_name='Admin',
            last_name='User',
            role='admin'
        )
        admin.set_password('AdminPassword123!')
        
        db.session.add(admin)
        db.session.commit()
        
        return admin


@pytest.fixture
def sample_category(app):
    """Create a sample category for testing."""
    with app.app_context():
        category = Category(
            name='Test Category',
            description='A test category',
            color='#007bff'
        )
        
        db.session.add(category)
        db.session.commit()
        
        return category


@pytest.fixture
def auth_headers(client, sample_user):
    """Get authentication headers for a sample user."""
    response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'TestPassword123!'
    })
    
    data = response.get_json()
    access_token = data['tokens']['access_token']
    
    return {'Authorization': f'Bearer {access_token}'}


@pytest.fixture
def admin_headers(client, admin_user):
    """Get authentication headers for an admin user."""
    response = client.post('/api/auth/login', json={
        'username': 'admin',
        'password': 'AdminPassword123!'
    })
    
    data = response.get_json()
    access_token = data['tokens']['access_token']
    
    return {'Authorization': f'Bearer {access_token}'}