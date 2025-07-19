"""
Analysis job model for tracking data analysis tasks.
"""
import json
from datetime import datetime
from app import db


class AnalysisJob(db.Model):
    """Analysis job model for tracking background analysis tasks."""
    
    __tablename__ = 'analysis_jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    job_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    parameters = db.Column(db.Text)  # JSON string of analysis parameters
    results = db.Column(db.Text)     # JSON string of analysis results
    error_message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    started_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    
    # Foreign keys
    dataset_id = db.Column(db.Integer, db.ForeignKey('datasets.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Valid job types
    VALID_JOB_TYPES = [
        'descriptive_stats',
        'correlation_analysis',
        'distribution_analysis',
        'outlier_detection',
        'data_profiling',
        'custom_analysis'
    ]
    
    # Valid status values
    VALID_STATUSES = [
        'pending',
        'running',
        'completed',
        'failed',
        'cancelled'
    ]
    
    def __init__(self, job_type, dataset_id, user_id, parameters=None):
        """Initialize analysis job instance."""
        if job_type not in self.VALID_JOB_TYPES:
            raise ValueError(f"Invalid job type: {job_type}")
        
        self.job_type = job_type
        self.dataset_id = dataset_id
        self.user_id = user_id
        self.parameters = json.dumps(parameters) if parameters else None
    
    def set_parameters(self, parameters):
        """Set analysis parameters as JSON string."""
        self.parameters = json.dumps(parameters)
    
    def get_parameters(self):
        """Get analysis parameters as dictionary."""
        return json.loads(self.parameters) if self.parameters else {}
    
    def set_results(self, results):
        """Set analysis results as JSON string."""
        self.results = json.dumps(results)
    
    def get_results(self):
        """Get analysis results as dictionary."""
        return json.loads(self.results) if self.results else {}
    
    def start_job(self):
        """Mark job as started."""
        self.status = 'running'
        self.started_at = datetime.utcnow()
        db.session.commit()
    
    def complete_job(self, results=None):
        """Mark job as completed with optional results."""
        self.status = 'completed'
        self.completed_at = datetime.utcnow()
        if results:
            self.set_results(results)
        db.session.commit()
    
    def fail_job(self, error_message):
        """Mark job as failed with error message."""
        self.status = 'failed'
        self.completed_at = datetime.utcnow()
        self.error_message = error_message
        db.session.commit()
    
    def cancel_job(self):
        """Mark job as cancelled."""
        self.status = 'cancelled'
        self.completed_at = datetime.utcnow()
        db.session.commit()
    
    def get_duration(self):
        """Get job duration in seconds."""
        if self.started_at and self.completed_at:
            return (self.completed_at - self.started_at).total_seconds()
        return None
    
    def is_finished(self):
        """Check if job is in a finished state."""
        return self.status in ['completed', 'failed', 'cancelled']
    
    def to_dict(self):
        """Convert analysis job to dictionary representation."""
        return {
            'id': self.id,
            'job_type': self.job_type,
            'status': self.status,
            'parameters': self.get_parameters(),
            'results': self.get_results() if self.status == 'completed' else None,
            'error_message': self.error_message,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'started_at': self.started_at.isoformat() if self.started_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'duration': self.get_duration(),
            'dataset_id': self.dataset_id,
            'user_id': self.user_id
        }
    
    def __repr__(self):
        """String representation of analysis job."""
        return f'<AnalysisJob {self.id}: {self.job_type} ({self.status})>'