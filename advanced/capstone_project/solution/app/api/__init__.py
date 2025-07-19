"""
API package initialization and configuration.
"""
from flask import Blueprint
from flask_restx import Api


def create_api(app):
    """
    Create and configure the Flask-RESTX API.
    
    Args:
        app: Flask application instance
        
    Returns:
        Api: Configured Flask-RESTX API instance
    """
    # Create main API blueprint
    api_bp = Blueprint('api', __name__, url_prefix='/api')
    
    # Configure API
    api = Api(
        api_bp,
        version=app.config.get('API_VERSION', 'v1'),
        title=app.config.get('API_TITLE', 'Data Analytics Dashboard API'),
        description=app.config.get('API_DESCRIPTION', 'RESTful API for the Data Analytics Dashboard'),
        doc='/doc/',  # Swagger documentation endpoint
        validate=True,
        ordered=True
    )
    
    # Register the API blueprint with the app
    app.register_blueprint(api_bp)
    
    return api