"""
User model for authentication and authorization.
"""
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(UserMixin, db.Model):
    """User model for storing user account information."""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='analyst')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    datasets = db.relationship('Dataset', backref='owner', lazy='dynamic', cascade='all, delete-orphan')
    analysis_jobs = db.relationship('AnalysisJob', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    dashboards = db.relationship('Dashboard', backref='creator', lazy='dynamic', cascade='all, delete-orphan')
    
    def __init__(self, username, email, role='analyst'):
        """Initialize user instance."""
        self.username = username
        self.email = email
        self.role = role
    
    def set_password(self, password):
        """Set password hash."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if provided password matches hash."""
        return check_password_hash(self.password_hash, password)
    
    def update_last_login(self):
        """Update last login timestamp."""
        self.last_login = datetime.utcnow()
        db.session.commit()
    
    def is_admin(self):
        """Check if user has admin role."""
        return self.role == 'admin'
    
    def can_access_dataset(self, dataset):
        """Check if user can access a specific dataset."""
        return self.is_admin() or dataset.user_id == self.id
    
    def to_dict(self):
        """Convert user to dictionary representation."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'is_active': self.is_active
        }
    
    def __repr__(self):
        """String representation of user."""
        return f'<User {self.username}>'