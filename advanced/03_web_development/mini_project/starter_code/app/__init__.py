"""
Task Management API - Application Factory

This module contains the application factory function that creates and configures
the Flask application with all necessary extensions and blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()


def create_app(config_name='development'):
    """
    Application factory function that creates and configures the Flask app.
    
    Args:
        config_name (str): Configuration name ('development', 'testing', 'production')
    
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    from app.config import config
    app.config.from_object(config[config_name])
    
    # Initialize extensions with app
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    # Enable CORS for all routes
    CORS(app)
    
    # Register blueprints
    from app.api import auth_bp, users_bp, projects_bp, tasks_bp, categories_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(projects_bp, url_prefix='/api/projects')
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')
    app.register_blueprint(categories_bp, url_prefix='/api/categories')
    
    # Register error handlers
    register_error_handlers(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
        
        # Create default categories if they don't exist
        from app.models.category import Category
        if Category.query.count() == 0:
            default_categories = [
                Category(name='General', description='General tasks', color='#6c757d'),
                Category(name='Development', description='Development tasks', color='#007bff'),
                Category(name='Design', description='Design tasks', color='#28a745'),
                Category(name='Testing', description='Testing tasks', color='#ffc107'),
                Category(name='Documentation', description='Documentation tasks', color='#17a2b8')
            ]
            
            for category in default_categories:
                db.session.add(category)
            
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
    
    return app


def register_error_handlers(app):
    """Register error handlers for the application."""
    
    @app.errorhandler(400)
    def bad_request(error):
        return {
            'error': 'Bad Request',
            'message': 'The request could not be understood by the server',
            'status_code': 400
        }, 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return {
            'error': 'Unauthorized',
            'message': 'Authentication is required to access this resource',
            'status_code': 401
        }, 401
    
    @app.errorhandler(403)
    def forbidden(error):
        return {
            'error': 'Forbidden',
            'message': 'You do not have permission to access this resource',
            'status_code': 403
        }, 403
    
    @app.errorhandler(404)
    def not_found(error):
        return {
            'error': 'Not Found',
            'message': 'The requested resource was not found',
            'status_code': 404
        }, 404
    
    @app.errorhandler(409)
    def conflict(error):
        return {
            'error': 'Conflict',
            'message': 'The request conflicts with the current state of the resource',
            'status_code': 409
        }, 409
    
    @app.errorhandler(422)
    def unprocessable_entity(error):
        return {
            'error': 'Unprocessable Entity',
            'message': 'The request was well-formed but contains semantic errors',
            'status_code': 422
        }, 422
    
    @app.errorhandler(500)
    def internal_server_error(error):
        return {
            'error': 'Internal Server Error',
            'message': 'An internal server error occurred',
            'status_code': 500
        }, 500