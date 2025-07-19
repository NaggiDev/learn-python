"""
Task Management API - Main Application Entry Point

This file serves as the entry point for the Flask application.
Run this file to start the development server.
"""

from app import create_app
import os

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment variables
    debug = os.environ.get('FLASK_ENV') == 'development'
    port = int(os.environ.get('PORT', 5000))
    
    print("Starting Task Management API...")
    print(f"Debug mode: {debug}")
    print(f"Port: {port}")
    print("Available endpoints:")
    print("- POST /api/auth/register : Register new user")
    print("- POST /api/auth/login : User login")
    print("- GET /api/auth/profile : Get user profile")
    print("- GET /api/projects : List projects")
    print("- POST /api/projects : Create project")
    print("- GET /api/tasks : List tasks")
    print("- POST /api/tasks : Create task")
    print("- GET /api/categories : List categories")
    
    app.run(debug=debug, port=port, host='0.0.0.0')