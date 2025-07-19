"""
Dataset model for managing uploaded data files.
"""
import os
from datetime import datetime
from typing import Optional, Dict, Any
from app import db


class Dataset(db.Model):
    """Dataset model for managing uploaded data files."""
    
    __tablename__ = 'datasets'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    file_type = db.Column(db.String(10), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.Text)
    
    # Metadata fields
    row_count = db.Column(db.Integer)
    column_count = db.Column(db.Integer)
    columns_info = db.Column(db.Text)  # JSON string of column information
    
    # Status fields
    is_processed = db.Column(db.Boolean, default=False)
    processing_error = db.Column(db.Text)
    
    # Relationships
    analysis_jobs = db.relationship('AnalysisJob', backref='dataset', lazy='dynamic', cascade='all, delete-orphan')
    
    def __init__(self, name: str, filename: str, file_path: str, file_size: int, 
                 file_type: str, user_id: int, description: str = None):
        """
        Initialize a new dataset.
        
        Args:
            name (str): Display name for the dataset
            filename (str): Original filename
            file_path (str): Path to the stored file
            file_size (int): File size in bytes
            file_type (str): File extension/type
            user_id (int): ID of the user who uploaded the dataset
            description (str, optional): Dataset description
        """
        self.name = name
        self.filename = filename
        self.file_path = file_path
        self.file_size = file_size
        self.file_type = file_type
        self.user_id = user_id
        self.description = description
    
    def get_file_size_formatted(self) -> str:
        """
        Get formatted file size string.
        
        Returns:
            str: Formatted file size (e.g., "1.5 MB")
        """
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
    
    def file_exists(self) -> bool:
        """
        Check if the dataset file still exists on disk.
        
        Returns:
            bool: True if file exists, False otherwise
        """
        return os.path.exists(self.file_path)
    
    def delete_file(self) -> bool:
        """
        Delete the dataset file from disk.
        
        Returns:
            bool: True if file was deleted successfully, False otherwise
        """
        try:
            if self.file_exists():
                os.remove(self.file_path)
            return True
        except OSError:
            return False
    
    def update_metadata(self, row_count: int, column_count: int, columns_info: str) -> None:
        """
        Update dataset metadata after processing.
        
        Args:
            row_count (int): Number of rows in the dataset
            column_count (int): Number of columns in the dataset
            columns_info (str): JSON string containing column information
        """
        self.row_count = row_count
        self.column_count = column_count
        self.columns_info = columns_info
        self.is_processed = True
        db.session.commit()
    
    def mark_processing_error(self, error_message: str) -> None:
        """
        Mark the dataset as having a processing error.
        
        Args:
            error_message (str): Error message to store
        """
        self.processing_error = error_message
        self.is_processed = False
        db.session.commit()
    
    def get_analysis_summary(self) -> Dict[str, Any]:
        """
        Get summary of analysis jobs for this dataset.
        
        Returns:
            dict: Analysis summary statistics
        """
        jobs = self.analysis_jobs.all()
        return {
            'total_jobs': len(jobs),
            'completed_jobs': len([j for j in jobs if j.status == 'completed']),
            'failed_jobs': len([j for j in jobs if j.status == 'failed']),
            'pending_jobs': len([j for j in jobs if j.status == 'pending']),
            'running_jobs': len([j for j in jobs if j.status == 'running'])
        }
    
    def to_dict(self, include_analysis_summary: bool = False) -> Dict[str, Any]:
        """
        Convert dataset instance to dictionary.
        
        Args:
            include_analysis_summary (bool): Whether to include analysis summary
            
        Returns:
            dict: Dataset data dictionary
        """
        data = {
            'id': self.id,
            'name': self.name,
            'filename': self.filename,
            'file_size': self.file_size,
            'file_size_formatted': self.get_file_size_formatted(),
            'file_type': self.file_type,
            'upload_date': self.upload_date.isoformat() if self.upload_date else None,
            'user_id': self.user_id,
            'description': self.description,
            'row_count': self.row_count,
            'column_count': self.column_count,
            'is_processed': self.is_processed,
            'processing_error': self.processing_error,
            'file_exists': self.file_exists()
        }
        
        if include_analysis_summary:
            data['analysis_summary'] = self.get_analysis_summary()
        
        return data
    
    def __repr__(self) -> str:
        """String representation of the dataset."""
        return f'<Dataset {self.name}>'