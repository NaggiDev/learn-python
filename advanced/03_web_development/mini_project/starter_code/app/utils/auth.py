"""
Task Management API - Authentication Utilities

This module contains authentication and authorization helper functions.
"""

from functools import wraps
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User


def admin_required(f):
    """
    Decorator to require admin role for accessing an endpoint.
    
    Args:
        f: Function to decorate
    
    Returns:
        Decorated function that checks for admin role
    """
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        if not user.is_admin():
            return jsonify({'error': 'Admin access required'}), 403
        
        return f(*args, **kwargs)
    
    return decorated_function


def get_current_user():
    """
    Get the current authenticated user.
    
    Returns:
        User object or None if not authenticated
    """
    try:
        user_id = get_jwt_identity()
        if user_id:
            return User.query.get(user_id)
    except Exception:
        pass
    
    return None


def require_user_or_admin(user_id):
    """
    Check if current user can access resources for the specified user_id.
    
    Args:
        user_id: ID of the user whose resources are being accessed
    
    Returns:
        Tuple of (is_authorized, current_user, error_response)
    """
    current_user = get_current_user()
    
    if not current_user:
        return False, None, (jsonify({'error': 'Authentication required'}), 401)
    
    if not current_user.is_active:
        return False, current_user, (jsonify({'error': 'Account is deactivated'}), 401)
    
    # Admin can access any user's resources
    if current_user.is_admin():
        return True, current_user, None
    
    # User can only access their own resources
    if current_user.id == user_id:
        return True, current_user, None
    
    return False, current_user, (jsonify({'error': 'Access denied'}), 403)


def check_project_access(project, access_type='read'):
    """
    Check if current user has access to a project.
    
    Args:
        project: Project object to check access for
        access_type: Type of access ('read', 'write', 'admin')
    
    Returns:
        Tuple of (has_access, current_user, error_response)
    """
    current_user = get_current_user()
    
    if not current_user:
        return False, None, (jsonify({'error': 'Authentication required'}), 401)
    
    if not current_user.is_active:
        return False, current_user, (jsonify({'error': 'Account is deactivated'}), 401)
    
    # Admin has full access to all projects
    if current_user.is_admin():
        return True, current_user, None
    
    # Project owner has full access
    if project.owner_id == current_user.id:
        return True, current_user, None
    
    # Check project membership
    membership = current_user.project_memberships.filter_by(project_id=project.id).first()
    
    if not membership:
        return False, current_user, (jsonify({'error': 'Project access denied'}), 403)
    
    # Check access level based on membership role
    if access_type == 'read':
        # All members can read
        return True, current_user, None
    elif access_type == 'write':
        # Only owners and members can write
        if membership.role in ['owner', 'member']:
            return True, current_user, None
    elif access_type == 'admin':
        # Only owners can perform admin actions
        if membership.role == 'owner':
            return True, current_user, None
    
    return False, current_user, (jsonify({'error': 'Insufficient permissions'}), 403)


def check_task_access(task, access_type='read'):
    """
    Check if current user has access to a task.
    
    Args:
        task: Task object to check access for
        access_type: Type of access ('read', 'write')
    
    Returns:
        Tuple of (has_access, current_user, error_response)
    """
    current_user = get_current_user()
    
    if not current_user:
        return False, None, (jsonify({'error': 'Authentication required'}), 401)
    
    if not current_user.is_active:
        return False, current_user, (jsonify({'error': 'Account is deactivated'}), 401)
    
    # Admin has full access to all tasks
    if current_user.is_admin():
        return True, current_user, None
    
    # Task creator and assignee have full access
    if task.created_by == current_user.id or task.assigned_to == current_user.id:
        return True, current_user, None
    
    # Check project access
    has_project_access, _, error_response = check_project_access(task.project, access_type)
    
    if not has_project_access:
        return False, current_user, error_response
    
    return True, current_user, None


def project_access_required(access_type='read'):
    """
    Decorator to require project access for accessing an endpoint.
    
    Args:
        access_type: Type of access required ('read', 'write', 'admin')
    
    Returns:
        Decorator function
    """
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def decorated_function(*args, **kwargs):
            # Get project_id from URL parameters
            project_id = kwargs.get('project_id') or kwargs.get('id')
            
            if not project_id:
                return jsonify({'error': 'Project ID required'}), 400
            
            from app.models.project import Project
            project = Project.query.get(project_id)
            
            if not project:
                return jsonify({'error': 'Project not found'}), 404
            
            has_access, current_user, error_response = check_project_access(project, access_type)
            
            if not has_access:
                return error_response
            
            # Add current_user and project to kwargs for use in the route
            kwargs['current_user'] = current_user
            kwargs['project'] = project
            
            return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator


def task_access_required(access_type='read'):
    """
    Decorator to require task access for accessing an endpoint.
    
    Args:
        access_type: Type of access required ('read', 'write')
    
    Returns:
        Decorator function
    """
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def decorated_function(*args, **kwargs):
            # Get task_id from URL parameters
            task_id = kwargs.get('task_id') or kwargs.get('id')
            
            if not task_id:
                return jsonify({'error': 'Task ID required'}), 400
            
            from app.models.task import Task
            task = Task.query.get(task_id)
            
            if not task:
                return jsonify({'error': 'Task not found'}), 404
            
            has_access, current_user, error_response = check_task_access(task, access_type)
            
            if not has_access:
                return error_response
            
            # Add current_user and task to kwargs for use in the route
            kwargs['current_user'] = current_user
            kwargs['task'] = task
            
            return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator