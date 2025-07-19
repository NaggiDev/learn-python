"""
Task Management API - API Package

This package contains all API blueprints and route handlers.
"""

from app.api.auth import auth_bp
from app.api.users import users_bp
from app.api.projects import projects_bp
from app.api.tasks import tasks_bp
from app.api.categories import categories_bp

__all__ = ['auth_bp', 'users_bp', 'projects_bp', 'tasks_bp', 'categories_bp']