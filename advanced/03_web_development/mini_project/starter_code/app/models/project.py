"""
Task Management API - Project Models

This module contains the Project and ProjectMember models.
TODO: Implement project models
"""

from datetime import datetime
from app import db


class Project(db.Model):
    """Project model for organizing tasks."""
    
    __tablename__ = 'projects'
    
    # TODO: Implement Project model
    # Fields: id, name, description, owner_id, is_active, created_at, updated_at
    # Relationships: owner, tasks, members
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Project {self.name}>'


class ProjectMember(db.Model):
    """Project membership model for managing project access."""
    
    __tablename__ = 'project_members'
    
    # TODO: Implement ProjectMember model
    # Fields: project_id, user_id, role, joined_at
    
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    
    def __repr__(self):
        return f'<ProjectMember {self.user_id}@{self.project_id}>'