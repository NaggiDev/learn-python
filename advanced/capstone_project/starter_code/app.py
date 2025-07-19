"""
Data Analytics Dashboard - Main Application Entry Point

This is the main Flask application file for the Data Analytics Dashboard.
Students should implement the core application logic here.

TODO: Implement the following:
1. Flask app configuration
2. Database initialization
3. Blueprint registration
4. Error handlers
5. Application factory pattern
"""

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from datetime import datetime

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app(config_name='development'):
    """
    Application factory pattern for creating Flask app instances.
    
    TODO: Complete the application factory implementation
    - Configure the app based on environment
    - Initialize all extensions
    - Register blueprints
    - Set up error handlers
    """
    app = Flask(__name__)
    
    # TODO: Configure the application
    # Hint: Set up database URI, secret key, and other configurations
    
    # TODO: Initialize extensions with the app
    # Hint: Use init_app() method for each extension
    
    # TODO: Register blueprints
    # Hint: Import and register auth, api, and main blueprints
    
    # TODO: Set up error handlers
    # Hint: Handle 404, 500, and other common errors
    
    @app.route('/')
    def index():
        """Main dashboard page"""
        # TODO: Implement the main dashboard view
        return render_template('index.html')
    
    @app.route('/health')
    def health_check():
        """Health check endpoint for monitoring"""
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.utcnow().isoformat(),
            'version': '1.0.0'
        })
    
    return app


if __name__ == '__main__':
    # TODO: Create and run the application
    # Hint: Use the application factory and run in debug mode for development
    pass