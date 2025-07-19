"""
Database models for the Data Analytics Dashboard

This module contains SQLAlchemy models for the application.
Students should implement the database schema based on the project requirements.

TODO: Implement the following models:
1. User model with authentication
2. Dataset model for uploaded files
3. AnalysisJob model for background tasks
4. Dashboard model for saved dashboards
5. Relationships between models
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

# Import db from app.py to avoid circular imports
from app import db


class User(UserMixin, db.Model):
    """
    User model for authentication and authorization
    
    TODO: Implement the User model with the following fields:
    - id (primary key)
    - username (unique)
    - email (unique)
    - password_hash
    - role (analyst, admin)
    - created_at
    - last_login
    """
    
    __tablename__ = 'users'
    
    # TODO: Define table columns
    # Hint: Use appropriate SQLAlchemy column types and constraints
    
    def __init__(self, username, email, password, role='analyst'):
        """Initialize a new user"""
        # TODO: Implement user initialization
        # Hint: Set username, email, hash password, set role and timestamps
        pass
    
    def set_password(self, password):
        """Hash and set user password"""
        # TODO: Implement password hashing
        # Hint: Use werkzeug.security.generate_password_hash
        pass
    
    def check_password(self, password):
        """Check if provided password matches user's password"""
        # TODO: Implement password verification
        # Hint: Use werkzeug.security.check_password_hash
        pass
    
    def to_dict(self):
        """Convert user object to dictionary for JSON serialization"""
        # TODO: Implement user serialization
        # Hint: Return dictionary with safe user information (no password)
        pass
    
    def __repr__(self):
        return f'<User {self.username}>'


class Dataset(db.Model):
    """
    Dataset model for uploaded data files
    
    TODO: Implement the Dataset model with the following fields:
    - id (primary key)
    - name
    - filename
    - file_path
    - file_size
    - file_type (csv, json, xlsx)
    - upload_date
    - user_id (foreign key)
    - description
    """
    
    __tablename__ = 'datasets'
    
    # TODO: Define table columns
    # Hint: Include foreign key relationship to User model
    
    def __init__(self, name, filename, file_path, file_size, file_type, user_id, description=None):
        """Initialize a new dataset"""
        # TODO: Implement dataset initialization
        pass
    
    def to_dict(self):
        """Convert dataset object to dictionary for JSON serialization"""
        # TODO: Implement dataset serialization
        pass
    
    def get_file_size_mb(self):
        """Get file size in megabytes"""
        # TODO: Convert file size from bytes to MB
        pass
    
    def __repr__(self):
        return f'<Dataset {self.name}>'


class AnalysisJob(db.Model):
    """
    Analysis job model for tracking background analysis tasks
    
    TODO: Implement the AnalysisJob model with the following fields:
    - id (primary key)
    - dataset_id (foreign key)
    - job_type (descriptive, correlation, distribution)
    - status (pending, running, completed, failed)
    - parameters (JSON)
    - results (JSON)
    - created_at
    - completed_at
    - user_id (foreign key)
    """
    
    __tablename__ = 'analysis_jobs'
    
    # TODO: Define table columns
    # Hint: Include foreign key relationships to Dataset and User models
    
    def __init__(self, dataset_id, job_type, user_id, parameters=None):
        """Initialize a new analysis job"""
        # TODO: Implement analysis job initialization
        pass
    
    def set_parameters(self, parameters):
        """Set job parameters as JSON"""
        # TODO: Serialize parameters to JSON string
        pass
    
    def get_parameters(self):
        """Get job parameters from JSON"""
        # TODO: Deserialize parameters from JSON string
        pass
    
    def set_results(self, results):
        """Set job results as JSON"""
        # TODO: Serialize results to JSON string
        pass
    
    def get_results(self):
        """Get job results from JSON"""
        # TODO: Deserialize results from JSON string
        pass
    
    def to_dict(self):
        """Convert analysis job object to dictionary for JSON serialization"""
        # TODO: Implement analysis job serialization
        pass
    
    def __repr__(self):
        return f'<AnalysisJob {self.id}: {self.job_type}>'


class Dashboard(db.Model):
    """
    Dashboard model for saved dashboard configurations
    
    TODO: Implement the Dashboard model with the following fields:
    - id (primary key)
    - name
    - description
    - layout_config (JSON)
    - user_id (foreign key)
    - created_at
    - updated_at
    """
    
    __tablename__ = 'dashboards'
    
    # TODO: Define table columns
    # Hint: Include foreign key relationship to User model
    
    def __init__(self, name, layout_config, user_id, description=None):
        """Initialize a new dashboard"""
        # TODO: Implement dashboard initialization
        pass
    
    def set_layout_config(self, config):
        """Set dashboard layout configuration as JSON"""
        # TODO: Serialize layout config to JSON string
        pass
    
    def get_layout_config(self):
        """Get dashboard layout configuration from JSON"""
        # TODO: Deserialize layout config from JSON string
        pass
    
    def to_dict(self):
        """Convert dashboard object to dictionary for JSON serialization"""
        # TODO: Implement dashboard serialization
        pass
    
    def __repr__(self):
        return f'<Dashboard {self.name}>'


# TODO: Define any additional helper functions or model relationships
# Hint: Consider adding methods for common queries or data validation