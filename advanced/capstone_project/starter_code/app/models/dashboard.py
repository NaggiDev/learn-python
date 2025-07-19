"""
Dashboard model for storing dashboard configurations.
"""
import json
from datetime import datetime
from app import db


class Dashboard(db.Model):
    """Dashboard model for storing dashboard layouts and configurations."""
    
    __tablename__ = 'dashboards'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    layout_config = db.Column(db.Text, nullable=False)  # JSON string of dashboard layout
    is_public = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self, name, layout_config, user_id, description=None, is_public=False):
        """Initialize dashboard instance."""
        self.name = name
        self.layout_config = json.dumps(layout_config) if isinstance(layout_config, dict) else layout_config
        self.user_id = user_id
        self.description = description
        self.is_public = is_public
    
    def set_layout_config(self, config):
        """Set dashboard layout configuration as JSON string."""
        self.layout_config = json.dumps(config)
        self.updated_at = datetime.utcnow()
    
    def get_layout_config(self):
        """Get dashboard layout configuration as dictionary."""
        return json.loads(self.layout_config) if self.layout_config else {}
    
    def update_config(self, config):
        """Update dashboard configuration."""
        self.set_layout_config(config)
        db.session.commit()
    
    def clone(self, new_name, user_id):
        """Create a copy of this dashboard for another user."""
        cloned_dashboard = Dashboard(
            name=new_name,
            layout_config=self.layout_config,
            user_id=user_id,
            description=f"Cloned from: {self.name}",
            is_public=False
        )
        return cloned_dashboard
    
    def can_be_accessed_by(self, user):
        """Check if a user can access this dashboard."""
        return (
            self.user_id == user.id or  # Owner
            self.is_public or           # Public dashboard
            user.is_admin()            # Admin user
        )
    
    def can_be_edited_by(self, user):
        """Check if a user can edit this dashboard."""
        return (
            self.user_id == user.id or  # Owner
            user.is_admin()            # Admin user
        )
    
    def get_chart_count(self):
        """Get the number of charts in this dashboard."""
        config = self.get_layout_config()
        return len(config.get('charts', []))
    
    def to_dict(self, include_config=True):
        """Convert dashboard to dictionary representation."""
        result = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_public': self.is_public,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'user_id': self.user_id,
            'chart_count': self.get_chart_count()
        }
        
        if include_config:
            result['layout_config'] = self.get_layout_config()
        
        return result
    
    def __repr__(self):
        """String representation of dashboard."""
        return f'<Dashboard {self.name}>'