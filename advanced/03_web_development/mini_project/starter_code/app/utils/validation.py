"""
Task Management API - Validation Utilities

This module contains validation functions for request data.
"""

import re
from datetime import datetime
from typing import List, Dict, Any


def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> List[str]:
    """
    Validate that all required fields are present and not empty.
    
    Args:
        data: Dictionary containing the data to validate
        required_fields: List of required field names
    
    Returns:
        List of error messages for missing fields
    """
    errors = []
    
    for field in required_fields:
        if field not in data:
            errors.append(f'{field} is required')
        elif not data[field] or (isinstance(data[field], str) and not data[field].strip()):
            errors.append(f'{field} cannot be empty')
    
    return errors


def validate_email(email: str) -> bool:
    """
    Validate email format using regex.
    
    Args:
        email: Email address to validate
    
    Returns:
        True if email is valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email.strip()))


def validate_password(password: str) -> List[str]:
    """
    Validate password strength.
    
    Args:
        password: Password to validate
    
    Returns:
        List of error messages for password validation failures
    """
    errors = []
    
    if not password or not isinstance(password, str):
        errors.append('Password is required')
        return errors
    
    if len(password) < 8:
        errors.append('Password must be at least 8 characters long')
    
    if len(password) > 128:
        errors.append('Password must be less than 128 characters long')
    
    if not re.search(r'[A-Z]', password):
        errors.append('Password must contain at least one uppercase letter')
    
    if not re.search(r'[a-z]', password):
        errors.append('Password must contain at least one lowercase letter')
    
    if not re.search(r'\d', password):
        errors.append('Password must contain at least one digit')
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append('Password must contain at least one special character')
    
    return errors


def validate_username(username: str) -> List[str]:
    """
    Validate username format and requirements.
    
    Args:
        username: Username to validate
    
    Returns:
        List of error messages for username validation failures
    """
    errors = []
    
    if not username or not isinstance(username, str):
        errors.append('Username is required')
        return errors
    
    username = username.strip()
    
    if len(username) < 3:
        errors.append('Username must be at least 3 characters long')
    
    if len(username) > 80:
        errors.append('Username must be less than 80 characters long')
    
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        errors.append('Username can only contain letters, numbers, underscores, and hyphens')
    
    if username.startswith('_') or username.startswith('-'):
        errors.append('Username cannot start with underscore or hyphen')
    
    if username.endswith('_') or username.endswith('-'):
        errors.append('Username cannot end with underscore or hyphen')
    
    return errors


def validate_date_string(date_string: str) -> bool:
    """
    Validate date string format (YYYY-MM-DD).
    
    Args:
        date_string: Date string to validate
    
    Returns:
        True if date is valid, False otherwise
    """
    if not date_string or not isinstance(date_string, str):
        return False
    
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_priority(priority: str) -> bool:
    """
    Validate task priority value.
    
    Args:
        priority: Priority value to validate
    
    Returns:
        True if priority is valid, False otherwise
    """
    valid_priorities = ['low', 'medium', 'high']
    return priority and priority.lower() in valid_priorities


def validate_status(status: str) -> bool:
    """
    Validate task status value.
    
    Args:
        status: Status value to validate
    
    Returns:
        True if status is valid, False otherwise
    """
    valid_statuses = ['todo', 'in_progress', 'done']
    return status and status.lower() in valid_statuses


def validate_role(role: str) -> bool:
    """
    Validate user role value.
    
    Args:
        role: Role value to validate
    
    Returns:
        True if role is valid, False otherwise
    """
    valid_roles = ['admin', 'user']
    return role and role.lower() in valid_roles


def validate_project_member_role(role: str) -> bool:
    """
    Validate project member role value.
    
    Args:
        role: Role value to validate
    
    Returns:
        True if role is valid, False otherwise
    """
    valid_roles = ['owner', 'member', 'viewer']
    return role and role.lower() in valid_roles


def validate_hex_color(color: str) -> bool:
    """
    Validate hex color code format.
    
    Args:
        color: Color code to validate
    
    Returns:
        True if color is valid hex code, False otherwise
    """
    if not color or not isinstance(color, str):
        return False
    
    hex_pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(hex_pattern, color))


def validate_pagination_params(page: int, per_page: int, max_per_page: int = 100) -> Dict[str, Any]:
    """
    Validate and normalize pagination parameters.
    
    Args:
        page: Page number
        per_page: Items per page
        max_per_page: Maximum allowed items per page
    
    Returns:
        Dictionary with validated pagination parameters and any errors
    """
    errors = []
    
    # Validate page number
    if page < 1:
        page = 1
        errors.append('Page number must be at least 1')
    
    # Validate per_page
    if per_page < 1:
        per_page = 10
        errors.append('Items per page must be at least 1')
    elif per_page > max_per_page:
        per_page = max_per_page
        errors.append(f'Items per page cannot exceed {max_per_page}')
    
    return {
        'page': page,
        'per_page': per_page,
        'errors': errors
    }


def sanitize_string(value: str, max_length: int = None) -> str:
    """
    Sanitize string input by trimming whitespace and limiting length.
    
    Args:
        value: String to sanitize
        max_length: Maximum allowed length
    
    Returns:
        Sanitized string
    """
    if not value or not isinstance(value, str):
        return ''
    
    sanitized = value.strip()
    
    if max_length and len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    return sanitized