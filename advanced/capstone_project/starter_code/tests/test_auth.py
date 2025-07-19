"""
Tests for authentication functionality.
"""
import pytest
from app.models import User


class TestAuth:
    """Test authentication endpoints."""
    
    def test_register_success(self, client):
        """Test successful user registration."""
        response = client.post('/auth/register', json={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123'
        })
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == 'User registered successfully'
        assert data['user']['username'] == 'newuser'
        assert data['user']['email'] == 'newuser@example.com'
    
    def test_register_missing_fields(self, client):
        """Test registration with missing fields."""
        response = client.post('/auth/register', json={
            'username': 'newuser'
            # Missing email and password
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
    
    def test_register_duplicate_username(self, client, user):
        """Test registration with duplicate username."""
        response = client.post('/auth/register', json={
            'username': 'testuser',  # Already exists
            'email': 'different@example.com',
            'password': 'password123'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'Username already exists' in data['error']
    
    def test_register_duplicate_email(self, client, user):
        """Test registration with duplicate email."""
        response = client.post('/auth/register', json={
            'username': 'differentuser',
            'email': 'test@example.com',  # Already exists
            'password': 'password123'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'Email already registered' in data['error']
    
    def test_login_success(self, client, auth):
        """Test successful login."""
        # First register a user
        auth.register()
        
        # Then login
        response = auth.login()
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'Login successful'
        assert data['user']['username'] == 'testuser'
    
    def test_login_invalid_credentials(self, client, auth):
        """Test login with invalid credentials."""
        # Register a user first
        auth.register()
        
        # Try to login with wrong password
        response = auth.login(password='wrongpassword')
        
        assert response.status_code == 401
        data = response.get_json()
        assert 'Invalid username or password' in data['error']
    
    def test_login_nonexistent_user(self, client, auth):
        """Test login with nonexistent user."""
        response = auth.login(username='nonexistent')
        
        assert response.status_code == 401
        data = response.get_json()
        assert 'Invalid username or password' in data['error']
    
    def test_logout_success(self, client, auth):
        """Test successful logout."""
        # Register and login first
        auth.register()
        auth.login()
        
        # Then logout
        response = auth.logout()
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'Logout successful'
    
    def test_logout_not_logged_in(self, client, auth):
        """Test logout when not logged in."""
        response = auth.logout()
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'No user logged in' in data['error']
    
    def test_profile_authenticated(self, client, auth):
        """Test getting profile when authenticated."""
        # Register and login first
        auth.register()
        auth.login()
        
        response = client.get('/auth/profile')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['user']['username'] == 'testuser'
        assert data['user']['email'] == 'test@example.com'
    
    def test_profile_unauthenticated(self, client):
        """Test getting profile when not authenticated."""
        response = client.get('/auth/profile')
        
        assert response.status_code == 401
        data = response.get_json()
        assert 'Authentication required' in data['error']
    
    def test_update_profile_success(self, client, auth):
        """Test successful profile update."""
        # Register and login first
        auth.register()
        auth.login()
        
        response = client.put('/auth/profile', json={
            'email': 'newemail@example.com'
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'Profile updated successfully'
        assert data['user']['email'] == 'newemail@example.com'
    
    def test_update_profile_duplicate_email(self, client, auth, user):
        """Test profile update with duplicate email."""
        # Register and login a new user
        auth.register(username='newuser', email='newuser@example.com')
        auth.login(username='newuser')
        
        # Try to update email to existing user's email
        response = client.put('/auth/profile', json={
            'email': 'test@example.com'  # user fixture's email
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'Email already in use' in data['error']
    
    def test_change_password_success(self, client, auth):
        """Test successful password change."""
        # Register and login first
        auth.register()
        auth.login()
        
        response = client.put('/auth/profile', json={
            'current_password': 'testpass123',
            'new_password': 'newpassword123'
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'Profile updated successfully'
    
    def test_change_password_wrong_current(self, client, auth):
        """Test password change with wrong current password."""
        # Register and login first
        auth.register()
        auth.login()
        
        response = client.put('/auth/profile', json={
            'current_password': 'wrongpassword',
            'new_password': 'newpassword123'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'Current password is incorrect' in data['error']