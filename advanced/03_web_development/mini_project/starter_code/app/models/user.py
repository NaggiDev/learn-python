"""
Task Management API - User Model

This module contains the User model and related functionality.
"""

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from app import db


class User(db.Model):
    """User model for authentication and user management."""
    
    __tablename__ = 'users'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Authentication fields
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Profile fields
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    
    # Role and status
    role = db.Column(db.String(20), nullable=False, default='user')  # 'admin' or 'user'
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    
    # Timestamps
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Relationships
    owned_projects = db.relationship('Project', foreign_keys='Project.owner_id', 
                                   backref='owner', lazy='dynamic', cascade='all, delete-orphan')
    created_tasks = db.relationship('Task', foreign_keys='Task.created_by', 
                                  backref='creator', lazy='dynamic')
    assigned_tasks = db.relationship('Task', foreign_keys='Task.assigned_to', 
                                   backref='assignee', lazy='dynamic')
    project_memberships = db.relationship('ProjectMember', backref='user', 
                                        lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches the user's password."""
        return check_password_hash(self.password_hash, password)
    
    def generate_tokens(self):
        """Generate JWT access and refresh tokens for the user."""
        access_token = create_access_token(identity=self.id)
        refresh_token = create_refresh_token(identity=self.id)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    
    def update_last_login(self):
        """Update the user's last login timestamp."""
        self.last_login = datetime.utcnow()
        db.session.commit()
    
    def is_admin(self):
        """Check if the user has admin role."""
        return self.role == 'admin'
    
    def can_access_project(self, project):
        """Check if the user can access a specific project."""
        if self.is_admin():
            return True
        
        if project.owner_id == self.id:
            return True
        
        # Check if user is a member of the project
        membership = self.project_memberships.filter_by(project_id=project.id).first()
        return membership is not None
    
    def can_edit_project(self, project):
        """Check if the user can edit a specific project."""
        if self.is_admin():
            return True
        
        if project.owner_id == self.id:
            return True
        
        # Check if user is a member with edit permissions
        membership = self.project_memberships.filter_by(project_id=project.id).first()
        return membership and membership.role in ['owner', 'member']
    
    def can_edit_task(self, task):
        """Check if the user can edit a specific task."""
        if self.is_admin():
            return True
        
        if task.created_by == self.id or task.assigned_to == self.id:
            return True
        
        # Check if user can edit the project containing the task
        return self.can_edit_project(task.project)
    
    def to_dict(self, include_sensitive=False):
        """Convert user object to dictionary."""
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': f"{self.first_name} {self.last_name}",
            'role': self.role,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        
        if include_sensitive:
            data.update({
                'last_login': self.last_login.isoformat() if self.last_login else None,
                'owned_projects_count': self.owned_projects.count(),
                'created_tasks_count': self.created_tasks.count(),
                'assigned_tasks_count': self.assigned_tasks.count()
            })
        
        return data
    
    @staticmethod
    def find_by_username(username):
        """Find user by username."""
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def find_by_email(email):
        """Find user by email."""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def find_by_username_or_email(identifier):
        """Find user by username or email."""
        return User.query.filter(
            (User.username == identifier) | (User.email == identifier)
        ).first()