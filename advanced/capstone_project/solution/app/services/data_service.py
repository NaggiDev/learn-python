"""
Data service for handling dataset operations and file processing.
"""
import os
import json
import pandas as pd
import numpy as np
from typing import Dict, Any, List, Optional, Tuple
from werkzeug.utils import secure_filename
from flask import current_app
from app import db, cache
from app.models.dataset import Dataset


class DataService:
    """Service class for dataset operations and data processing."""
    
    @staticmethod
    def allowed_file(filename: str) -> bool:
        """
        Check if the file extension is allowed.
        
        Args:
            filename (str): Name of the file to check
            
        Returns:
            bool: True if file is allowed, False otherwise
        """
        return ('.' in filename and 
                filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS'])
    
    @staticmethod
    def save_uploaded_file(file, user_id: int, name: str = None, description: str = None) -> Dataset:
        """
        Save an uploaded file and create a dataset record.
        
        Args:
            file: Uploaded file object
            user_id (int): ID of the user uploading the file
            name (str, optional): Display name for the dataset
            description (str, optional): Dataset description
            
        Returns:
            Dataset: Created dataset instance
            
        Raises:
            ValueError: If file is invalid or processing fails
        """
        if not file or not file.filename:
            raise ValueError("No file provided")
        
        if not DataService.allowed_file(file.filename):
            raise ValueError("File type not allowed")
        
        # Secure the filename
        filename = secure_filename(file.filename)
        if not filename:
            raise ValueError("Invalid filename")
        
        # Generate unique filename to avoid conflicts
        timestamp = int(pd.Timestamp.now().timestamp())
        unique_filename = f"{timestamp}_{filename}"
        
        # Create upload directory if it doesn't exist
        upload_dir = current_app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        # Save file
        file_path = os.path.join(upload_dir, unique_filename)
        file.save(file_path)
        
        # Get file info
        file_size = os.path.getsize(file_path)
        file_type = filename.rsplit('.', 1)[1].lower()
        
        # Create dataset record
        dataset = Dataset(
            name=name or filename,
            filename=filename,
            file_path=file_path,
            file_size=file_size,
            file_type=file_type,
            user_id=user_id,
            description=description
        )
        
        try:
            # Process the file to extract metadata
            DataService.process_dataset_metadata(dataset)
            
            db.session.add(dataset)
            db.session.commit()
            
            current_app.logger.info(f"Dataset created: {dataset.name} (ID: {dataset.id})")
            
            return dataset
            
        except Exception as e:
            # Clean up file if database operation fails
            if os.path.exists(file_path):
                os.remove(file_path)
            
            if dataset.id:
                db.session.rollback()
            
            raise ValueError(f"Failed to process dataset: {str(e)}")
    
    @staticmethod
    def process_dataset_metadata(dataset: Dataset) -> None:
        """
        Process dataset file to extract metadata.
        
        Args:
            dataset (Dataset): Dataset instance to process
            
        Raises:
            ValueError: If file processing fails
        """
        try:
            df = DataService.load_dataset(dataset)
            
            # Extract basic metadata
            row_count = len(df)
            column_count = len(df.columns)
            
            # Extract column information
            columns_info = []
            for col in df.columns:
                col_info = {
                    'name': col,
                    'dtype': str(df[col].dtype),
                    'null_count': int(df[col].isnull().sum()),
                    'unique_count': int(df[col].nunique()),
                    'sample_values': df[col].dropna().head(5).tolist()
                }
                
                # Add statistics for numeric columns
                if pd.api.types.is_numeric_dtype(df[col]):
                    col_info.update({
                        'min': float(df[col].min()) if not pd.isna(df[col].min()) else None,
                        'max': float(df[col].max()) if not pd.isna(df[col].max()) else None,
                        'mean': float(df[col].mean()) if not pd.isna(df[col].mean()) else None,
                        'std': float(df[col].std()) if not pd.isna(df[col].std()) else None
                    })
                
                columns_info.append(col_info)
            
            # Update dataset metadata
            dataset.update_metadata(row_count, column_count, json.dumps(columns_info))
            
        except Exception as e:
            dataset.mark_processing_error(str(e))
            raise ValueError(f"Failed to process dataset metadata: {str(e)}")
    
    @staticmethod
    def load_dataset(dataset: Dataset) -> pd.DataFrame:
        """
        Load dataset file into a pandas DataFrame.
        
        Args:
            dataset (Dataset): Dataset instance to load
            
        Returns:
            pd.DataFrame: Loaded dataset
            
        Raises:
            ValueError: If file cannot be loaded
        """
        if not dataset.file_exists():
            raise ValueError("Dataset file not found")
        
        try:
            if dataset.file_type == 'csv':
                df = pd.read_csv(dataset.file_path)
            elif dataset.file_type == 'json':
                df = pd.read_json(dataset.file_path)
            elif dataset.file_type in ['xlsx', 'xls']:
                df = pd.read_excel(dataset.file_path)
            else:
                raise ValueError(f"Unsupported file type: {dataset.file_type}")
            
            return df
            
        except Exception as e:
            raise ValueError(f"Failed to load dataset: {str(e)}")
    
    @staticmethod
    @cache.memoize(timeout=3600)  # Cache for 1 hour
    def get_dataset_preview(dataset_id: int, rows: int = 10) -> Dict[str, Any]:
        """
        Get a preview of the dataset.
        
        Args:
            dataset_id (int): ID of the dataset
            rows (int): Number of rows to preview
            
        Returns:
            dict: Dataset preview data
            
        Raises:
            ValueError: If dataset cannot be loaded
        """
        dataset = Dataset.query.get(dataset_id)
        if not dataset:
            raise ValueError("Dataset not found")
        
        df = DataService.load_dataset(dataset)
        
        # Get preview data
        preview_df = df.head(rows)
        
        return {
            'columns': df.columns.tolist(),
            'data': preview_df.to_dict('records'),
            'total_rows': len(df),
            'total_columns': len(df.columns),
            'dtypes': {col: str(dtype) for col, dtype in df.dtypes.items()}
        }
    
    @staticmethod
    def get_dataset_info(dataset: Dataset) -> Dict[str, Any]:
        """
        Get comprehensive information about a dataset.
        
        Args:
            dataset (Dataset): Dataset instance
            
        Returns:
            dict: Dataset information
        """
        info = dataset.to_dict(include_analysis_summary=True)
        
        if dataset.columns_info:
            try:
                info['columns_info'] = json.loads(dataset.columns_info)
            except json.JSONDecodeError:
                info['columns_info'] = []
        
        return info
    
    @staticmethod
    def delete_dataset(dataset: Dataset) -> bool:
        """
        Delete a dataset and its associated file.
        
        Args:
            dataset (Dataset): Dataset instance to delete
            
        Returns:
            bool: True if deletion was successful
        """
        try:
            # Delete the file
            dataset.delete_file()
            
            # Delete from database
            db.session.delete(dataset)
            db.session.commit()
            
            # Clear cache
            cache.delete_memoized(DataService.get_dataset_preview, dataset.id)
            
            current_app.logger.info(f"Dataset deleted: {dataset.name} (ID: {dataset.id})")
            
            return True
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Failed to delete dataset {dataset.id}: {str(e)}")
            return False
    
    @staticmethod
    def filter_dataset(dataset: Dataset, filters: Dict[str, Any]) -> pd.DataFrame:
        """
        Apply filters to a dataset.
        
        Args:
            dataset (Dataset): Dataset to filter
            filters (dict): Filter conditions
            
        Returns:
            pd.DataFrame: Filtered dataset
        """
        df = DataService.load_dataset(dataset)
        
        for column, condition in filters.items():
            if column not in df.columns:
                continue
            
            if isinstance(condition, dict):
                # Handle complex conditions
                if 'min' in condition:
                    df = df[df[column] >= condition['min']]
                if 'max' in condition:
                    df = df[df[column] <= condition['max']]
                if 'equals' in condition:
                    df = df[df[column] == condition['equals']]
                if 'contains' in condition:
                    df = df[df[column].astype(str).str.contains(condition['contains'], na=False)]
            else:
                # Simple equality filter
                df = df[df[column] == condition]
        
        return df
    
    @staticmethod
    def get_column_statistics(dataset: Dataset, column: str) -> Dict[str, Any]:
        """
        Get statistics for a specific column.
        
        Args:
            dataset (Dataset): Dataset instance
            column (str): Column name
            
        Returns:
            dict: Column statistics
        """
        df = DataService.load_dataset(dataset)
        
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in dataset")
        
        series = df[column]
        stats = {
            'name': column,
            'dtype': str(series.dtype),
            'count': int(series.count()),
            'null_count': int(series.isnull().sum()),
            'unique_count': int(series.nunique()),
            'most_frequent': series.mode().iloc[0] if not series.mode().empty else None
        }
        
        if pd.api.types.is_numeric_dtype(series):
            stats.update({
                'min': float(series.min()) if not pd.isna(series.min()) else None,
                'max': float(series.max()) if not pd.isna(series.max()) else None,
                'mean': float(series.mean()) if not pd.isna(series.mean()) else None,
                'median': float(series.median()) if not pd.isna(series.median()) else None,
                'std': float(series.std()) if not pd.isna(series.std()) else None,
                'quartiles': {
                    'q1': float(series.quantile(0.25)) if not pd.isna(series.quantile(0.25)) else None,
                    'q3': float(series.quantile(0.75)) if not pd.isna(series.quantile(0.75)) else None
                }
            })
        
        return stats