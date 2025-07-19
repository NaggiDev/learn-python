"""
Dashboard model for managing visualization dashboards.
"""
import json
from datetime import datetime
from typing import Dict, Any, List
from app import db


class Dashboard(db.Model):
    """Dashboard model for managing visualization dashboards."""
    
    __tablename__ = 'dashboards'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    layout_config = db.Column(db.Text, nullable=False)  # JSON string of dashboard layout
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Dashboard settings
    is_public = db.Column(db.Boolean, default=False)
    auto_refresh = db.Column(db.Boolean, default=False)
    refresh_interval = db.Column(db.Integer, default=300)  # seconds
    
    # Dashboard metadata
    chart_count = db.Column(db.Integer, default=0)
    last_viewed = db.Column(db.DateTime)
    view_count = db.Column(db.Integer, default=0)
    
    def __init__(self, name: str, user_id: int, layout_config: Dict[str, Any] = None, 
                 description: str = None):
        """
        Initialize a new dashboard.
        
        Args:
            name (str): Dashboard name
            user_id (int): ID of the user who owns the dashboard
            layout_config (dict, optional): Dashboard layout configuration
            description (str, optional): Dashboard description
        """
        self.name = name
        self.user_id = user_id
        self.description = description
        self.set_layout_config(layout_config or {})
        self.update_chart_count()
    
    def get_layout_config(self) -> Dict[str, Any]:
        """
        Get dashboard layout configuration as dictionary.
        
        Returns:
            dict: Layout configuration
        """
        try:
            return json.loads(self.layout_config) if self.layout_config else {}
        except json.JSONDecodeError:
            return {}
    
    def set_layout_config(self, config: Dict[str, Any]) -> None:
        """
        Set dashboard layout configuration from dictionary.
        
        Args:
            config (dict): Layout configuration to set
        """
        self.layout_config = json.dumps(config)
        self.updated_at = datetime.utcnow()
        self.update_chart_count()
    
    def update_chart_count(self) -> None:
        """Update the chart count based on layout configuration."""
        config = self.get_layout_config()
        charts = config.get('charts', [])
        self.chart_count = len(charts)
    
    def add_chart(self, chart_config: Dict[str, Any]) -> None:
        """
        Add a chart to the dashboard.
        
        Args:
            chart_config (dict): Chart configuration
        """
        config = self.get_layout_config()
        if 'charts' not in config:
            config['charts'] = []
        
        # Generate unique chart ID
        chart_id = f"chart_{len(config['charts']) + 1}_{int(datetime.utcnow().timestamp())}"
        chart_config['id'] = chart_id
        
        config['charts'].append(chart_config)
        self.set_layout_config(config)
    
    def remove_chart(self, chart_id: str) -> bool:
        """
        Remove a chart from the dashboard.
        
        Args:
            chart_id (str): ID of the chart to remove
            
        Returns:
            bool: True if chart was removed, False if not found
        """
        config = self.get_layout_config()
        charts = config.get('charts', [])
        
        for i, chart in enumerate(charts):
            if chart.get('id') == chart_id:
                charts.pop(i)
                config['charts'] = charts
                self.set_layout_config(config)
                return True
        
        return False
    
    def update_chart(self, chart_id: str, chart_config: Dict[str, Any]) -> bool:
        """
        Update a chart in the dashboard.
        
        Args:
            chart_id (str): ID of the chart to update
            chart_config (dict): New chart configuration
            
        Returns:
            bool: True if chart was updated, False if not found
        """
        config = self.get_layout_config()
        charts = config.get('charts', [])
        
        for i, chart in enumerate(charts):
            if chart.get('id') == chart_id:
                chart_config['id'] = chart_id  # Preserve the ID
                charts[i] = chart_config
                config['charts'] = charts
                self.set_layout_config(config)
                return True
        
        return False
    
    def get_charts(self) -> List[Dict[str, Any]]:
        """
        Get all charts in the dashboard.
        
        Returns:
            list: List of chart configurations
        """
        config = self.get_layout_config()
        return config.get('charts', [])
    
    def record_view(self) -> None:
        """Record a view of the dashboard."""
        self.last_viewed = datetime.utcnow()
        self.view_count += 1
        db.session.commit()
    
    def update_timestamp(self) -> None:
        """Update the dashboard's last modified timestamp."""
        self.updated_at = datetime.utcnow()
    
    def clone(self, new_name: str, user_id: int) -> 'Dashboard':
        """
        Create a clone of this dashboard for another user.
        
        Args:
            new_name (str): Name for the cloned dashboard
            user_id (int): ID of the user who will own the clone
            
        Returns:
            Dashboard: New dashboard instance
        """
        clone = Dashboard(
            name=new_name,
            user_id=user_id,
            layout_config=self.get_layout_config(),
            description=f"Cloned from: {self.name}"
        )
        return clone
    
    def get_dataset_dependencies(self) -> List[int]:
        """
        Get list of dataset IDs that this dashboard depends on.
        
        Returns:
            list: List of dataset IDs
        """
        dataset_ids = set()
        charts = self.get_charts()
        
        for chart in charts:
            dataset_id = chart.get('dataset_id')
            if dataset_id:
                dataset_ids.add(dataset_id)
        
        return list(dataset_ids)
    
    def is_accessible_by(self, user) -> bool:
        """
        Check if a user can access this dashboard.
        
        Args:
            user: User instance to check
            
        Returns:
            bool: True if user can access, False otherwise
        """
        # Owner can always access
        if self.user_id == user.id:
            return True
        
        # Admin can access all dashboards
        if user.is_admin():
            return True
        
        # Public dashboards can be accessed by anyone
        if self.is_public:
            return True
        
        return False
    
    def to_dict(self, include_layout: bool = True) -> Dict[str, Any]:
        """
        Convert dashboard instance to dictionary.
        
        Args:
            include_layout (bool): Whether to include layout configuration
            
        Returns:
            dict: Dashboard data dictionary
        """
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'is_public': self.is_public,
            'auto_refresh': self.auto_refresh,
            'refresh_interval': self.refresh_interval,
            'chart_count': self.chart_count,
            'last_viewed': self.last_viewed.isoformat() if self.last_viewed else None,
            'view_count': self.view_count,
            'dataset_dependencies': self.get_dataset_dependencies()
        }
        
        if include_layout:
            data['layout_config'] = self.get_layout_config()
        
        return data
    
    def __repr__(self) -> str:
        """String representation of the dashboard."""
        return f'<Dashboard {self.name}>'