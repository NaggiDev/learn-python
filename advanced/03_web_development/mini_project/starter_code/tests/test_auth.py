"""
Task Management API - Authentication Tests

This module contains tests for authentication endpoints.
"""

import pytest
from app.models.user import User


class TestAuthRegistration:
    """Test user registration functionality."""
    
    def test_register_success(self, client):
        """Test successful user registration."""
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'NewPassword123!',
            'first_name': 'New',
            'last_name': 'User'
        }
        
        response = client.post('/api/auth/register', json=user_data)
        
        assert response.status_code == 201
        data = response.get_json()
        assert 'user' in data
        assert 'tokens' in data
        assert data['user']['username'] == 'newuser'
        assert data['user']['email'] == 'newuser@example.com'
    
    def test_register_missing_fields(self, client):
        """Test registration with missing required fields."""
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com'
            # Missing password, first_name, last_name
        }
        
        response = client.post('/api/auth/register', json=user_data)
        
        assert response.status_code == 422
        data = response.get_json()
        assert 'error' in data
        assert 'details' in data
    
    def test_register_invalid_email(self, client):
        """Test registration with invalid email format."""
        user_data = {
            'username': 'newuser',
            'email': 'invalid-email',
            'password': 'NewPassword123!',
            'first_name': 'New',
            'last_name': 'User'
        }
        
        response = client.post('/api/auth/register', json=user_data)
        
        assert response.status_code == 422
        data = response.get_json()
        assert 'Invalid email format' in data['error']
    
    def test_register_weak_password(self, client):
        """Test registration with weak password."""
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'weak',
            'first_name': 'New',
            'last_name': 'User'
        }
        
        response = client.post('/api/auth/register', json=user_data)
        
        assert response.status_code == 422
        data = response.get_json()
        assert 'Password validation failed' in data['error']
    
    def test_register_duplicate_username(self, client, sample_user):
        """Test registration with existing username."""
        user_data = {
            'username': 'testuser',  # Same as sample_user
            'email': 'different@example.com',
            'password': 'NewPassword123!',
            'first_name': 'New',
            'last_name': 'User'
        }
        
        response = client.post('/api/auth/register', json=user_data)
        
        assert response.status_code == 409
        data = response.get_json()
        assert 'Username already exists' in data['error']
    
    def test_register_duplicate_email(self, client, sample_user):
        """Test registration with existing email."""
        user_data = {
            'username': 'newuser',
            'email': 'test@example.com',  # Same as sample_user
            'password': 'NewPassword123!',
            'first_name': 'New',
            'last_name': 'User'
        }
        
        response = client.post('/api/auth/register', json=user_data)
        
        assert response.status_code == 409
        data = response.get_json()
        assert 'Email already exists' in data['error']


class TestAuthLogin:
    """Test user login functionality."""
    
    def test_login_success(self, client, sample_user):
        """Test successful login."""
        login_data = {
            'username': 'testuser',
            'password': 'TestPassword123!'
        }
        
        response = client.post('/api/auth/login', json=login_data)
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'user' in data
        assert 'tokens' in data
        assert data['user']['username'] == 'testuser'
    
    def test_login_with_email(self, client, sample_user):
        """Test login using email instead of username."""
        login_data = {
            'username': 'test@example.com',  # Using email
            'password': 'TestPassword123!'
        }
        
        response = client.post('/api/auth/login', json=login_data)
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['user']['email'] == 'test@example.com'
    
    def test_login_invalid_credentials(self, client, sample_user):
        """Test login with invalid credentials."""
        login_data = {
            'username': 'testuser',
            'password': 'WrongPassword'
        }
        
        response = client.post('/api/auth/login', json=login_data)
        
        assert response.status_code == 401
        data = response.get_json()
        assert 'Invalid credentials' in data['error']
    
    def test_login_nonexistent_user(self, client):
        """Test login with non-existent user."""
        login_data = {
            'username': 'nonexistent',
            'password': 'SomePassword123!'
        }
        
        response = client.post('/api/auth/login', json=login_data)
        
        assert response.status_code == 401
        data = response.get_json()
        assert 'Invalid credentials' in data['error']
    
    def test_login_missing_fields(self, client):
        """Test login with missing required fields."""
        login_data = {
            'username': 'testuser'
            # Missing password
        }
        
        response = client.post('/api/auth/login', json=login_data)
        
        assert response.status_code == 422
        data = response.get_json()
        assert 'Validation failed' in data['error']


class TestAuthProfile:
    """Test user profile functionality."""
    
    def test_get_profile_success(self, client, auth_headers):
        """Test getting user profile."""
        response = client.get('/api/auth/profile', headers=auth_headers)
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'user' in data
        assert data['user']['username'] == 'testuser'
    
    def test_get_profile_unauthorized(self, client):
        """Test getting profile without authentication."""
        response = client.get('/api/auth/profile')
        
        assert response.status_code == 401
    
    def test_update_profile_success(self, client, auth_headers):
        """Test updating user profile."""
        update_data = {
            'first_name': 'Updated',
            'last_name': 'Name'
        }
        
        response = client.put('/api/auth/profile', 
                            json=update_data, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['user']['first_name'] == 'Updated'
        assert data['user']['last_name'] == 'Name'
    
    def test_update_profile_password(self, client, auth_headers):
        """Test updating user password."""
        update_data = {
            'current_password': 'TestPassword123!',
            'new_password': 'NewPassword123!'
        }
        
        response = client.put('/api/auth/profile', 
                            json=update_data, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'Profile updated successfully' in data['message']
    
    def test_update_profile_wrong_current_password(self, client, auth_headers):
        """Test updating password with wrong current password."""
        update_data = {
            'current_password': 'WrongPassword',
            'new_password': 'NewPassword123!'
        }
        
        response = client.put('/api/auth/profile', 
                            json=update_data, 
                            headers=auth_headers)
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'Current password is incorrect' in data['error']


class TestAuthLogout:
    """Test user logout functionality."""
    
    def test_logout_success(self, client, auth_headers):
        """Test successful logout."""
        response = client.post('/api/auth/logout', headers=auth_headers)
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'Successfully logged out' in data['message']
    
    def test_logout_unauthorized(self, client):
        """Test logout without authentication."""
        response = client.post('/api/auth/logout')
        
        assert response.status_code == 401