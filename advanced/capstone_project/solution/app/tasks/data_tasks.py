"""
Background tasks for data processing operations.
"""
from celery.utils.log import get_task_logger
from app import db
from app.models.dataset import Dataset
from app.services.data_service import DataService
from celery_app import celery

logger = get_task_logger(__name__)


@celery.task(bind=True, name='app.tasks.data.process_dataset')
def process_dataset(self, dataset_id: int):
    """
    Process dataset metadata in the background.
    
    Args:
        dataset_id (int): ID of the dataset to process
    """
    logger.info(f"Processing dataset {dataset_id}")
    
    dataset = Dataset.query.get(dataset_id)
    if not dataset:
        logger.error(f"Dataset {dataset_id} not found")
        return {'error': 'Dataset not found'}
    
    try:
        self.update_state(state='PROGRESS', meta={'progress': 20, 'status': 'Loading dataset'})
        
        # Process dataset metadata
        DataService.process_dataset_metadata(dataset)
        
        self.update_state(state='PROGRESS', meta={'progress': 100, 'status': 'Processing complete'})
        
        logger.info(f"Dataset {dataset_id} processed successfully")
        
        return {
            'dataset_id': dataset_id,
            'status': 'completed',
            'row_count': dataset.row_count,
            'column_count': dataset.column_count
        }
        
    except Exception as e:
        logger.error(f"Dataset processing failed for {dataset_id}: {str(e)}")
        dataset.mark_processing_error(str(e))
        
        self.update_state(
            state='FAILURE',
            meta={'error': str(e), 'dataset_id': dataset_id}
        )
        
        raise


@celery.task(name='app.tasks.data.cleanup_orphaned_files')
def cleanup_orphaned_files():
    """Clean up orphaned upload files."""
    import os
    from flask import current_app
    
    logger.info("Starting cleanup of orphaned files")
    
    try:
        upload_dir = current_app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_dir):
            return {'message': 'Upload directory does not exist'}
        
        # Get all files in upload directory
        upload_files = set(os.listdir(upload_dir))
        
        # Get all dataset file paths
        datasets = Dataset.query.all()
        dataset_files = set()
        
        for dataset in datasets:
            if dataset.file_exists():
                filename = os.path.basename(dataset.file_path)
                dataset_files.add(filename)
        
        # Find orphaned files
        orphaned_files = upload_files - dataset_files
        
        deleted_count = 0
        for filename in orphaned_files:
            file_path = os.path.join(upload_dir, filename)
            try:
                os.remove(file_path)
                deleted_count += 1
                logger.info(f"Deleted orphaned file: {filename}")
            except OSError as e:
                logger.error(f"Failed to delete {filename}: {e}")
        
        logger.info(f"Cleanup completed. Deleted {deleted_count} orphaned files")
        
        return {
            'deleted_count': deleted_count,
            'orphaned_files': list(orphaned_files)
        }
        
    except Exception as e:
        logger.error(f"File cleanup failed: {str(e)}")
        raise