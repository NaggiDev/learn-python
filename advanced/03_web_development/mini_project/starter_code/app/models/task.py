"""
Task Management API - Task Model

This module contains the Task model.
TODO: Implement task model
"""

from datetime import datetime
from app import db


class Task(db.Model):
    """Task model for managing individual tasks."""
    
    __tablename__ = 'tasks'
    
    # TODO: Implement Task model
    # Fields: id, title, description, status, priority, due_date, 
    #         project_id, assigned_to, created_by, category_id, created_at, updated_at
    # Relationships: project, assignee, creator, category
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f'<Task {self.title}>'