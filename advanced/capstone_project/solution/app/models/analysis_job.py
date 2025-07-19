"""
Analysis job model for tracking data analysis tasks.
"""
import json
from datetime import datetime
from typing import Dict, Any, Optional
from app import db


class AnalysisJob(db.Model):
    """Analysis job model for tracking background analysis tasks."""
    
    __tablename__ = 'analysis_jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    dataset_id = db.Column(db.Integer, db.ForeignKey('datasets.id'), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    parameters = db.Column(db.Text)  # JSON string of job parameters
    results = db.Column(db.Text)     # JSON string of job results
    error_message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    started_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Celery task ID for tracking
    celery_task_id = db.Column(db.String(255))
    
    # Job priority and retry information
    priority = db.Column(db.Integer, default=0)
    retry_count = db.Column(db.Integer, default=0)
    max_retries = db.Column(db.Integer, default=3)
    
    def __init__(self, dataset_id: int, job_type: str, user_id: int, 
                 parameters: Dict[str, Any] = None, priority: int = 0):
        """
        Initialize a new analysis job.
        
        Args:
            dataset_id (int): ID of the dataset to analyze
            job_type (str): Type of analysis job
            user_id (int): ID of the user who requested the job
            parameters (dict, optional): Job parameters
            priority (int): Job priority (higher = more priority)
        """
        self.dataset_id = dataset_id
        self.job_type = job_type
        self.user_id = user_id
        self.parameters = json.dumps(parameters or {})
        self.priority = priority
    
    def get_parameters(self) -> Dict[str, Any]:
        """
        Get job parameters as dictionary.
        
        Returns:
            dict: Job parameters
        """
        try:
            return json.loads(self.parameters) if self.parameters else {}
        except json.JSONDecodeError:
            return {}
    
    def set_parameters(self, parameters: Dict[str, Any]) -> None:
        """
        Set job parameters from dictionary.
        
        Args:
            parameters (dict): Job parameters to set
        """
        self.parameters = json.dumps(parameters)
    
    def get_results(self) -> Dict[str, Any]:
        """
        Get job results as dictionary.
        
        Returns:
            dict: Job results
        """
        try:
            return json.loads(self.results) if self.results else {}
        except json.JSONDecodeError:
            return {}
    
    def set_results(self, results: Dict[str, Any]) -> None:
        """
        Set job results from dictionary.
        
        Args:
            results (dict): Job results to set
        """
        self.results = json.dumps(results)
    
    def start_job(self, celery_task_id: str = None) -> None:
        """
        Mark the job as started.
        
        Args:
            celery_task_id (str, optional): Celery task ID
        """
        self.status = 'running'
        self.started_at = datetime.utcnow()
        if celery_task_id:
            self.celery_task_id = celery_task_id
        db.session.commit()
    
    def complete_job(self, results: Dict[str, Any]) -> None:
        """
        Mark the job as completed with results.
        
        Args:
            results (dict): Job results
        """
        self.status = 'completed'
        self.completed_at = datetime.utcnow()
        self.set_results(results)
        db.session.commit()
    
    def fail_job(self, error_message: str) -> None:
        """
        Mark the job as failed with error message.
        
        Args:
            error_message (str): Error message
        """
        self.status = 'failed'
        self.completed_at = datetime.utcnow()
        self.error_message = error_message
        db.session.commit()
    
    def retry_job(self) -> bool:
        """
        Attempt to retry the job if retries are available.
        
        Returns:
            bool: True if job can be retried, False otherwise
        """
        if self.retry_count < self.max_retries:
            self.retry_count += 1
            self.status = 'pending'
            self.error_message = None
            self.started_at = None
            self.completed_at = None
            db.session.commit()
            return True
        return False
    
    def get_duration(self) -> Optional[float]:
        """
        Get job duration in seconds.
        
        Returns:
            float or None: Duration in seconds, None if not completed
        """
        if self.started_at and self.completed_at:
            return (self.completed_at - self.started_at).total_seconds()
        return None
    
    def is_finished(self) -> bool:
        """
        Check if the job is finished (completed or failed).
        
        Returns:
            bool: True if job is finished, False otherwise
        """
        return self.status in ['completed', 'failed']
    
    def can_retry(self) -> bool:
        """
        Check if the job can be retried.
        
        Returns:
            bool: True if job can be retried, False otherwise
        """
        return self.status == 'failed' and self.retry_count < self.max_retries
    
    def to_dict(self, include_results: bool = True) -> Dict[str, Any]:
        """
        Convert analysis job instance to dictionary.
        
        Args:
            include_results (bool): Whether to include job results
            
        Returns:
            dict: Analysis job data dictionary
        """
        data = {
            'id': self.id,
            'dataset_id': self.dataset_id,
            'job_type': self.job_type,
            'status': self.status,
            'parameters': self.get_parameters(),
            'error_message': self.error_message,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'started_at': self.started_at.isoformat() if self.started_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'user_id': self.user_id,
            'celery_task_id': self.celery_task_id,
            'priority': self.priority,
            'retry_count': self.retry_count,
            'max_retries': self.max_retries,
            'duration': self.get_duration(),
            'can_retry': self.can_retry()
        }
        
        if include_results:
            data['results'] = self.get_results()
        
        return data
    
    def __repr__(self) -> str:
        """String representation of the analysis job."""
        return f'<AnalysisJob {self.id}: {self.job_type} ({self.status})>'