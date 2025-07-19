"""
Dataset model for storing uploaded data files information.
"""
import os
from datetime import datetime
from app import db


class Dataset(db.Model):
    """Dataset model for storing information about uploaded data files."""
    
    __tablename__ = 'datasets'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    file_type = db.Column(db.String(10), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text)
    
    # Metadata fields
    row_count = db.Column(db.Integer)
    column_count = db.Column(db.Integer)
    columns_info = db.Column(db.Text)  # JSON string of column information
    
    # Foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    analysis_jobs = db.relationship('AnalysisJob', backref='dataset', lazy='dynamic', cascade='all, delete-orphan')
    
    def __init__(self, name, filename, file_path, file_size, file_type, user_id, description=None):
        """Initialize dataset instance."""
        self.name = name
        self.filename = filename
        self.file_path = file_path
        self.file_size = file_size
        self.file_type = file_type
        self.user_id = user_id
        self.description = description
    
    def get_file_size_formatted(self):
        """Get human-readable file size."""
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
    
    def file_exists(self):
        """Check if the physical file still exists."""
        return os.path.exists(self.file_path)
    
    def delete_file(self):
        """Delete the physical file from disk."""
        if self.file_exists():
            try:
                os.remove(self.file_path)
                return True
            except OSError:
                return False
        return True  # File doesn't exist, consider it deleted
    
    def update_metadata(self, row_count=None, column_count=None, columns_info=None):
        """Update dataset metadata."""
        if row_count is not None:
            self.row_count = row_count
        if column_count is not None:
            self.column_count = column_count
        if columns_info is not None:
            self.columns_info = columns_info
        db.session.commit()
    
    def to_dict(self):
        """Convert dataset to dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'filename': self.filename,
            'file_size': self.file_size,
            'file_size_formatted': self.get_file_size_formatted(),
            'file_type': self.file_type,
            'upload_date': self.upload_date.isoformat() if self.upload_date else None,
            'description': self.description,
            'row_count': self.row_count,
            'column_count': self.column_count,
            'user_id': self.user_id,
            'file_exists': self.file_exists()
        }
    
    def __repr__(self):
        """String representation of dataset."""
        return f'<Dataset {self.name}>'