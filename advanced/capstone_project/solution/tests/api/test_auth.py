"""
API tests for authentication endpoints.
"""
import pytest
from app import db
from app.models import User


class TestAuthAPI:
    """Test cases for authentication API."""
    
    def test_user_registration(self, client):
        """Test user registration endpoint."""
        response = client.post('/api/auth/register', json={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123',
            'role': 'analyst'
        })
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['username'] == 'newuser'
        assert data['email'] == 'new@example.com'
        assert data['role'] == 'analyst'
        assert 'password_hash' not in data
        
        # Verify user was created in database
        user = User.query.filter_by(username='newuser').first()
        assert user is not None
        assert user.check_password('newpass123')
    
    def test_registration_validation(self, client):
        """Test registration input validation."""
        # Missing required fields
        response = client.post('/api/auth/register', json={
            'username': 'test'
        })
        assert response.status_code == 400
        
        # Invalid email
        response = client.post('/api/auth/register', json={
            'username': 'testuser',
            'email': 'invalid-email',
            'password': 'testpass123'
        })
        assert response.status_code == 400
        
        # Short password
        response = client.post('/api/auth/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': '123'
        })
        assert response.status_code == 400
        
        # Short username
        response = client.post('/api/auth/register', json={
            'username': 'ab',
            'email': 'test@example.com',
            'password': 'testpass123'
        })
        assert response.status_code == 400
    
    def test_duplicate_registration(self, client):
        """Test registration with duplicate username/email."""
        # Create first user
        response = client.post('/api/auth/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        })
        assert response.status_code == 201
        
        # Try to register with same username
        response = client.post('/api/auth/register', json={
            'username': 'testuser',
            'email': 'different@example.com',
            'password': 'testpass123'
        })
        assert response.status_code == 409
        assert 'Username already exists' in response.get_json()['error']
        
        # Try to register with same email
        response = client.post('/api/auth/register', json={
            'username': 'differentuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        })
        assert response.status_code == 409
        assert 'Email already registered' in response.get_json()['error']
    
    def test_user_login(self, client, auth):
        """Test user login endpoint."""
        # Register user first
        auth.register()
        
        # Login
        response = auth.login()
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['username'] == 'newuser'
        assert 'last_login' in data
    
    def test_login_validation(self, client):
        """Test login input validation."""
        # Missing fields
        response = client.post('/api/auth/login', json={
            'username': 'test'
        })
        assert response.status_code == 400
        
        # Invalid credentials
        response = client.post('/api/auth/login', json={
            'username': 'nonexistent',
            'password': 'wrongpass'
        })
        assert response.status_code == 401
    
    def test_login_inactive_user(self, client):
        """Test login with inactive user."""
        # Create inactive user
        user = User(
            username='inactive',
            email='inactive@example.com',
            password='testpass123',
            role='analyst'
        )
        user.is_active = False
        db.session.add(user)
        db.session.commit()
        
        # Try to login
        response = client.post('/api/auth/login', json={
            'username': 'inactive',
            'password': 'testpass123'
        })
        assert response.status_code == 401
        assert 'Account is disabled' in response.get_json()['error']
    
    def test_user_logout(self, client, auth):
        """Test user logout endpoint."""
        # Register and login
        auth.register()
        auth.login()
        
        # Logout
        response = auth.logout()
        assert response.status_code == 200
        assert 'Successfully logged out' in response.get_json()['message']
    
    def test_logout_without_login(self, client):
        """Test logout without being logged in."""
        response = client.post('/api/auth/logout')
        assert response.status_code == 401  # Unauthorized
    
    def test_get_profile(self, client, auth):
        """Test get user profile endpoint."""
        # Register and login
        auth.register()
        auth.login()
        
        # Get profile
        response = client.get('/api/auth/profile')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['username'] == 'newuser'
        assert data['email'] == 'new@example.com'
        assert 'dataset_count' in data
    
    def test_get_profile_without_login(self, client):
        """Test get profile without being logged in."""
        response = client.get('/api/auth/profile')
        assert response.status_code == 401
    
    def test_update_profile(self, client, auth):
        """Test update user profile endpoint."""
        # Register and login
        auth.register()
        auth.login()
        
        # Update profile
        response = client.put('/api/auth/profile', json={
            'email': 'updated@example.com',
            'password': 'newpass123'
        })
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['email'] == 'updated@example.com'
        
        # Verify password was updated
        user = User.query.filter_by(username='newuser').first()
        assert user.check_password('newpass123')
        assert not user.check_password('newpass123')  # Old password should not work
    
    def test_update_profile_validation(self, client, auth):
        """Test profile update validation."""
        # Register and login
        auth.register()
        auth.login()
        
        # Empty email
        response = client.put('/api/auth/profile', json={
            'email': ''
        })
        assert response.status_code == 400
        
        # Short password
        response = client.put('/api/auth/profile', json={
            'password': '123'
        })
        assert response.status_code == 400
    
    def test_update_profile_duplicate_email(self, client, auth):
        """Test profile update with duplicate email."""
        # Create another user
        user2 = User(
            username='user2',
            email='user2@example.com',
            password='testpass123'
        )
        db.session.add(user2)
        db.session.commit()
        
        # Register and login first user
        auth.register()
        auth.login()
        
        # Try to update to existing email
        response = client.put('/api/auth/profile', json={
            'email': 'user2@example.com'
        })
        assert response.status_code == 409
        assert 'Email already registered' in response.get_json()['error']
    
    def test_list_users_admin(self, client, admin_headers):
        """Test list users endpoint (admin only)."""
        response = client.get('/api/auth/users')
        assert response.status_code == 200
        
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) >= 1  # At least the admin user
    
    def test_list_users_non_admin(self, client, auth_headers):
        """Test list users endpoint with non-admin user."""
        response = client.get('/api/auth/users')
        assert response.status_code == 403
        assert 'Admin access required' in response.get_json()['error']
    
    def test_list_users_without_login(self, client):
        """Test list users endpoint without login."""
        response = client.get('/api/auth/users')
        assert response.status_code == 401