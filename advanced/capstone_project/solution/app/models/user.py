"""
User model for authentication and authorization.
"""
from datetime import datetime
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash
from app import db


class User(UserMixin, db.Model):
    """User model for authentication and role-based access control."""
    
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
    dashboards = db.relationship('Dashboard', backref='owner', lazy='dynamic', cascade='all, delete-orphan')
    
    def __init__(self, username: str, email: str, password: str, role: str = 'analyst'):
        """
        Initialize a new user.
        
        Args:
            username (str): Unique username
            email (str): User's email address
            password (str): Plain text password (will be hashed)
            role (str): User role ('admin', 'analyst', 'viewer')
        """
        self.username = username
        self.email = email
        self.set_password(password)
        self.role = role
    
    def set_password(self, password: str) -> None:
        """
        Hash and set the user's password.
        
        Args:
            password (str): Plain text password
        """
        self.password_hash = generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password: str) -> bool:
        """
        Check if the provided password matches the user's password.
        
        Args:
            password (str): Plain text password to check
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return check_password_hash(self.password_hash, password)
    
    def update_last_login(self) -> None:
        """Update the user's last login timestamp."""
        self.last_login = datetime.utcnow()
        db.session.commit()
    
    def has_role(self, role: str) -> bool:
        """
        Check if the user has a specific role.
        
        Args:
            role (str): Role to check
            
        Returns:
            bool: True if user has the role, False otherwise
        """
        return self.role == role
    
    def is_admin(self) -> bool:
        """Check if the user is an administrator."""
        return self.role == 'admin'
    
    def can_edit_dataset(self, dataset) -> bool:
        """
        Check if the user can edit a specific dataset.
        
        Args:
            dataset: Dataset instance to check
            
        Returns:
            bool: True if user can edit, False otherwise
        """
        return self.is_admin() or dataset.user_id == self.id
    
    def can_view_dataset(self, dataset) -> bool:
        """
        Check if the user can view a specific dataset.
        
        Args:
            dataset: Dataset instance to check
            
        Returns:
            bool: True if user can view, False otherwise
        """
        # For now, users can only view their own datasets
        # This can be extended for shared datasets
        return self.is_admin() or dataset.user_id == self.id
    
    def can_view_dashboard(self, dashboard) -> bool:
        """
        Check if the user can view a specific dashboard.
        
        Args:
            dashboard: Dashboard instance to check
            
        Returns:
            bool: True if user can view, False otherwise
        """
        return dashboard.is_accessible_by(self)
    
    def can_edit_dashboard(self, dashboard) -> bool:
        """
        Check if the user can edit a specific dashboard.
        
        Args:
            dashboard: Dashboard instance to check
            
        Returns:
            bool: True if user can edit, False otherwise
        """
        return self.is_admin() or dashboard.user_id == self.id
    
    def to_dict(self) -> dict:
        """
        Convert user instance to dictionary.
        
        Returns:
            dict: User data dictionary
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'is_active': self.is_active,
            'dataset_count': self.datasets.count(),
            'analysis_job_count': self.analysis_jobs.count(),
            'dashboard_count': self.dashboards.count()
        }
    
    def __repr__(self) -> str:
        """String representation of the user."""
        return f'<User {self.username}>'