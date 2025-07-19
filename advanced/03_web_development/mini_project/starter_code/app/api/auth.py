"""
Task Management API - Authentication Routes

This module contains authentication-related API endpoints.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app import db
from app.models.user import User
from app.utils.validation import validate_required_fields, validate_email, validate_password
from app.utils.auth import admin_required

# Create blueprint
auth_bp = Blueprint('auth', __name__)

# JWT blacklist for logout functionality
blacklisted_tokens = set()


@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['username', 'email', 'password', 'first_name', 'last_name']
        validation_errors = validate_required_fields(data, required_fields)
        
        if validation_errors:
            return jsonify({'error': 'Validation failed', 'details': validation_errors}), 422
        
        # Validate email format
        if not validate_email(data['email']):
            return jsonify({'error': 'Invalid email format'}), 422
        
        # Validate password strength
        password_errors = validate_password(data['password'])
        if password_errors:
            return jsonify({'error': 'Password validation failed', 'details': password_errors}), 422
        
        # Check if username already exists
        if User.find_by_username(data['username']):
            return jsonify({'error': 'Username already exists'}), 409
        
        # Check if email already exists
        if User.find_by_email(data['email']):
            return jsonify({'error': 'Email already exists'}), 409
        
        # Create new user
        user = User(
            username=data['username'].strip().lower(),
            email=data['email'].strip().lower(),
            first_name=data['first_name'].strip(),
            last_name=data['last_name'].strip(),
            role=data.get('role', 'user')  # Default to 'user' role
        )
        user.set_password(data['password'])
        
        db.session.add(user)
        db.session.commit()
        
        # Generate tokens
        tokens = user.generate_tokens()
        
        return jsonify({
            'message': 'User registered successfully',
            'user': user.to_dict(),
            'tokens': tokens
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Registration failed', 'details': str(e)}), 500


@auth_bp.route('/login', methods=['POST'])
def login():
    """Authenticate user and return JWT tokens."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['username', 'password']
        validation_errors = validate_required_fields(data, required_fields)
        
        if validation_errors:
            return jsonify({'error': 'Validation failed', 'details': validation_errors}), 422
        
        # Find user by username or email
        user = User.find_by_username_or_email(data['username'].strip().lower())
        
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        
        if not user.is_active:
            return jsonify({'error': 'Account is deactivated'}), 401
        
        # Update last login
        user.update_last_login()
        
        # Generate tokens
        tokens = user.generate_tokens()
        
        return jsonify({
            'message': 'Login successful',
            'user': user.to_dict(),
            'tokens': tokens
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Login failed', 'details': str(e)}), 500


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """Logout user by blacklisting the JWT token."""
    try:
        jti = get_jwt()['jti']  # JWT ID
        blacklisted_tokens.add(jti)
        
        return jsonify({'message': 'Successfully logged out'}), 200
        
    except Exception as e:
        return jsonify({'error': 'Logout failed', 'details': str(e)}), 500


@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get current user's profile."""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'user': user.to_dict(include_sensitive=True)
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to get profile', 'details': str(e)}), 500


@auth_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    """Update current user's profile."""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Update allowed fields
        if 'first_name' in data:
            user.first_name = data['first_name'].strip()
        
        if 'last_name' in data:
            user.last_name = data['last_name'].strip()
        
        if 'email' in data:
            email = data['email'].strip().lower()
            if email != user.email:
                if not validate_email(email):
                    return jsonify({'error': 'Invalid email format'}), 422
                
                if User.find_by_email(email):
                    return jsonify({'error': 'Email already exists'}), 409
                
                user.email = email
        
        # Handle password change
        if 'current_password' in data and 'new_password' in data:
            if not user.check_password(data['current_password']):
                return jsonify({'error': 'Current password is incorrect'}), 400
            
            password_errors = validate_password(data['new_password'])
            if password_errors:
                return jsonify({'error': 'Password validation failed', 'details': password_errors}), 422
            
            user.set_password(data['new_password'])
        
        db.session.commit()
        
        return jsonify({
            'message': 'Profile updated successfully',
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update profile', 'details': str(e)}), 500


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Refresh access token using refresh token."""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user or not user.is_active:
            return jsonify({'error': 'User not found or inactive'}), 404
        
        # Generate new access token
        from flask_jwt_extended import create_access_token
        access_token = create_access_token(identity=user_id)
        
        return jsonify({
            'access_token': access_token
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Token refresh failed', 'details': str(e)}), 500


# JWT token blacklist checker
@auth_bp.before_app_request
def check_if_token_revoked():
    """Check if JWT token is blacklisted."""
    try:
        from flask_jwt_extended import verify_jwt_in_request, get_jwt
        
        # Only check for protected routes
        if request.endpoint and 'auth' in request.endpoint:
            return
        
        verify_jwt_in_request(optional=True)
        jti = get_jwt().get('jti')
        
        if jti in blacklisted_tokens:
            return jsonify({'error': 'Token has been revoked'}), 401
            
    except Exception:
        # If there's any error in token verification, let it pass
        # The actual JWT verification will handle it
        pass