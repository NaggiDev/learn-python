"""
Authentication routes for user registration, login, and logout.
"""
from flask import request, jsonify, current_app
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.models import User


@bp.route('/register', methods=['POST'])
def register():
    """Register a new user account."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['username', 'email', 'password']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        username = data['username'].strip()
        email = data['email'].strip().lower()
        password = data['password']
        
        # Validate input
        if len(username) < 3:
            return jsonify({'error': 'Username must be at least 3 characters long'}), 400
        
        if len(password) < 6:
            return jsonify({'error': 'Password must be at least 6 characters long'}), 400
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400
        
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already registered'}), 400
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        current_app.logger.info(f'New user registered: {username}')
        
        return jsonify({
            'message': 'User registered successfully',
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        current_app.logger.error(f'Registration error: {str(e)}')
        return jsonify({'error': 'Registration failed'}), 500


@bp.route('/login', methods=['POST'])
def login():
    """Authenticate user and create session."""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('username') or not data.get('password'):
            return jsonify({'error': 'Username and password are required'}), 400
        
        username = data['username'].strip()
        password = data['password']
        
        # Find user by username or email
        user = User.query.filter(
            (User.username == username) | (User.email == username)
        ).first()
        
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401
        
        if not user.is_active:
            return jsonify({'error': 'Account is disabled'}), 401
        
        # Log in user
        login_user(user, remember=data.get('remember', False))
        user.update_last_login()
        
        current_app.logger.info(f'User logged in: {user.username}')
        
        return jsonify({
            'message': 'Login successful',
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        current_app.logger.error(f'Login error: {str(e)}')
        return jsonify({'error': 'Login failed'}), 500


@bp.route('/logout', methods=['POST'])
def logout():
    """Log out current user."""
    try:
        if current_user.is_authenticated:
            username = current_user.username
            logout_user()
            current_app.logger.info(f'User logged out: {username}')
            return jsonify({'message': 'Logout successful'}), 200
        else:
            return jsonify({'error': 'No user logged in'}), 400
            
    except Exception as e:
        current_app.logger.error(f'Logout error: {str(e)}')
        return jsonify({'error': 'Logout failed'}), 500


@bp.route('/profile', methods=['GET'])
def profile():
    """Get current user profile."""
    try:
        if not current_user.is_authenticated:
            return jsonify({'error': 'Authentication required'}), 401
        
        return jsonify({
            'user': current_user.to_dict()
        }), 200
        
    except Exception as e:
        current_app.logger.error(f'Profile error: {str(e)}')
        return jsonify({'error': 'Failed to get profile'}), 500


@bp.route('/profile', methods=['PUT'])
def update_profile():
    """Update current user profile."""
    try:
        if not current_user.is_authenticated:
            return jsonify({'error': 'Authentication required'}), 401
        
        data = request.get_json()
        
        # Update allowed fields
        if 'email' in data:
            email = data['email'].strip().lower()
            # Check if email is already taken by another user
            existing_user = User.query.filter_by(email=email).first()
            if existing_user and existing_user.id != current_user.id:
                return jsonify({'error': 'Email already in use'}), 400
            current_user.email = email
        
        # Update password if provided
        if 'current_password' in data and 'new_password' in data:
            if not current_user.check_password(data['current_password']):
                return jsonify({'error': 'Current password is incorrect'}), 400
            
            if len(data['new_password']) < 6:
                return jsonify({'error': 'New password must be at least 6 characters long'}), 400
            
            current_user.set_password(data['new_password'])
        
        db.session.commit()
        
        current_app.logger.info(f'Profile updated: {current_user.username}')
        
        return jsonify({
            'message': 'Profile updated successfully',
            'user': current_user.to_dict()
        }), 200
        
    except Exception as e:
        current_app.logger.error(f'Profile update error: {str(e)}')
        return jsonify({'error': 'Failed to update profile'}), 500