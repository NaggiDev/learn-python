"""
Task Management API - Category Model

This module contains the Category model for task categorization.
"""

from datetime import datetime
from app import db


class Category(db.Model):
    """Category model for organizing tasks."""
    
    __tablename__ = 'categories'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Category information
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    description = db.Column(db.Text)
    color = db.Column(db.String(7), nullable=False, default='#6c757d')  # Hex color code
    
    # Timestamps
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relationships
    tasks = db.relationship('Task', backref='category', lazy='dynamic')
    
    def __repr__(self):
        return f'<Category {self.name}>'
    
    def to_dict(self, include_tasks=False):
        """Convert category object to dictionary."""
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'color': self.color,
            'created_at': self.created_at.isoformat(),
            'task_count': self.tasks.count()
        }
        
        if include_tasks:
            data['tasks'] = [task.to_dict() for task in self.tasks]
        
        return data
    
    @staticmethod
    def find_by_name(name):
        """Find category by name."""
        return Category.query.filter_by(name=name).first()
    
    @staticmethod
    def get_all_active():
        """Get all categories ordered by name."""
        return Category.query.order_by(Category.name).all()