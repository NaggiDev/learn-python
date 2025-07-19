"""
Authentication API endpoints.
"""
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_user, logout_user, login_required, current_user
from flask_restx import Api, Resource, fields, Namespace
from marshmallow import Schema, fields as ma_fields, ValidationError
from app import db
from app.models.user import User

# Create blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
auth_ns = Namespace('auth', description='Authentication operations')

# Marshmallow schemas for validation
class UserRegistrationSchema(Schema):
    username = ma_fields.Str(required=True, validate=lambda x: len(x) >= 3)
    email = ma_fields.Email(required=True)
    password = ma_fields.Str(required=True, validate=lambda x: len(x) >= 6)
    role = ma_fields.Str(missing='analyst', validate=lambda x: x in ['admin', 'analyst', 'viewer'])

class UserLoginSchema(Schema):
    username = ma_fields.Str(required=True)
    password = ma_fields.Str(required=True)

# Flask-RESTX models for documentation
user_registration_model = auth_ns.model('UserRegistration', {
    'username': fields.String(required=True, description='Username (min 3 characters)'),
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='Password (min 6 characters)'),
    'role': fields.String(description='User role', enum=['admin', 'analyst', 'viewer'], default='analyst')
})

user_login_model = auth_ns.model('UserLogin', {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password')
})

user_response_model = auth_ns.model('UserResponse', {
    'id': fields.Integer(description='User ID'),
    'username': fields.String(description='Username'),
    'email': fields.String(description='Email address'),
    'role': fields.String(description='User role'),
    'created_at': fields.String(description='Account creation date'),
    'last_login': fields.String(description='Last login date')
})


@auth_ns.route('/register')
class UserRegistration(Resource):
    """User registration endpoint."""
    
    @auth_ns.expect(user_registration_model)
    @auth_ns.marshal_with(user_response_model, code=201)
    @auth_ns.doc('register_user')
    def post(self):
        """Register a new user account."""
        try:
            # Validate input data
            schema = UserRegistrationSchema()
            data = schema.load(request.json)
        except ValidationError as err:
            return {'error': 'Validation failed', 'details': err.messages}, 400
        
        # Check if username already exists
        if User.query.filter_by(username=data['username']).first():
            return {'error': 'Username already exists'}, 409
        
        # Check if email already exists
        if User.query.filter_by(email=data['email']).first():
            return {'error': 'Email already registered'}, 409
        
        try:
            # Create new user
            user = User(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                role=data['role']
            )
            
            db.session.add(user)
            db.session.commit()
            
            current_app.logger.info(f'New user registered: {user.username}')
            
            return user.to_dict(), 201
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f'User registration failed: {str(e)}')
            return {'error': 'Registration failed'}, 500


@auth_ns.route('/login')
class UserLogin(Resource):
    """User login endpoint."""
    
    @auth_ns.expect(user_login_model)
    @auth_ns.marshal_with(user_response_model)
    @auth_ns.doc('login_user')
    def post(self):
        """Authenticate user and create session."""
        try:
            # Validate input data
            schema = UserLoginSchema()
            data = schema.load(request.json)
        except ValidationError as err:
            return {'error': 'Validation failed', 'details': err.messages}, 400
        
        # Find user by username
        user = User.query.filter_by(username=data['username']).first()
        
        if not user or not user.check_password(data['password']):
            return {'error': 'Invalid username or password'}, 401
        
        if not user.is_active:
            return {'error': 'Account is disabled'}, 401
        
        # Log in the user
        login_user(user, remember=True)
        user.update_last_login()
        
        current_app.logger.info(f'User logged in: {user.username}')
        
        return user.to_dict(), 200


@auth_ns.route('/logout')
class UserLogout(Resource):
    """User logout endpoint."""
    
    @auth_ns.doc('logout_user')
    @login_required
    def post(self):
        """Log out the current user."""
        username = current_user.username
        logout_user()
        
        current_app.logger.info(f'User logged out: {username}')
        
        return {'message': 'Successfully logged out'}, 200


@auth_ns.route('/profile')
class UserProfile(Resource):
    """User profile endpoint."""
    
    @auth_ns.marshal_with(user_response_model)
    @auth_ns.doc('get_user_profile')
    @login_required
    def get(self):
        """Get current user's profile information."""
        return current_user.to_dict(), 200
    
    @auth_ns.expect(auth_ns.model('UserProfileUpdate', {
        'email': fields.String(description='Email address'),
        'password': fields.String(description='New password (min 6 characters)')
    }))
    @auth_ns.marshal_with(user_response_model)
    @auth_ns.doc('update_user_profile')
    @login_required
    def put(self):
        """Update current user's profile information."""
        data = request.json or {}
        
        try:
            # Update email if provided
            if 'email' in data:
                email = data['email'].strip()
                if not email:
                    return {'error': 'Email cannot be empty'}, 400
                
                # Check if email is already taken by another user
                existing_user = User.query.filter_by(email=email).first()
                if existing_user and existing_user.id != current_user.id:
                    return {'error': 'Email already registered'}, 409
                
                current_user.email = email
            
            # Update password if provided
            if 'password' in data:
                password = data['password']
                if len(password) < 6:
                    return {'error': 'Password must be at least 6 characters'}, 400
                
                current_user.set_password(password)
            
            db.session.commit()
            
            current_app.logger.info(f'User profile updated: {current_user.username}')
            
            return current_user.to_dict(), 200
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f'Profile update failed: {str(e)}')
            return {'error': 'Profile update failed'}, 500


@auth_ns.route('/users')
class UserList(Resource):
    """User management endpoint (admin only)."""
    
    @auth_ns.marshal_list_with(user_response_model)
    @auth_ns.doc('list_users')
    @login_required
    def get(self):
        """Get list of all users (admin only)."""
        if not current_user.is_admin():
            return {'error': 'Admin access required'}, 403
        
        users = User.query.all()
        return [user.to_dict() for user in users], 200


# Register namespace with blueprint
auth_bp.add_url_rule('/register', view_func=UserRegistration.as_view('register'))
auth_bp.add_url_rule('/login', view_func=UserLogin.as_view('login'))
auth_bp.add_url_rule('/logout', view_func=UserLogout.as_view('logout'))
auth_bp.add_url_rule('/profile', view_func=UserProfile.as_view('profile'))
auth_bp.add_url_rule('/users', view_func=UserList.as_view('users'))