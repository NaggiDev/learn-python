"""
Background tasks for data analysis operations.
"""
from celery import current_task
from celery.utils.log import get_task_logger
from app import db
from app.models.analysis_job import AnalysisJob
from app.services.analysis_service import AnalysisService
from celery_app import celery

logger = get_task_logger(__name__)


@celery.task(bind=True, name='app.tasks.analysis.run_analysis')
def run_analysis(self, job_id: int):
    """
    Run analysis job in the background.
    
    Args:
        job_id (int): ID of the analysis job to run
    """
    logger.info(f"Starting analysis job {job_id}")
    
    # Get the job from database
    job = AnalysisJob.query.get(job_id)
    if not job:
        logger.error(f"Analysis job {job_id} not found")
        return {'error': 'Job not found'}
    
    try:
        # Mark job as started
        job.start_job(self.request.id)
        
        # Get job parameters
        params = job.get_parameters()
        dataset_id = job.dataset_id
        job_type = job.job_type
        
        # Update task progress
        self.update_state(state='PROGRESS', meta={'progress': 10, 'status': 'Initializing analysis'})
        
        # Run the appropriate analysis
        results = None
        
        if job_type == 'descriptive_statistics':
            self.update_state(state='PROGRESS', meta={'progress': 30, 'status': 'Calculating descriptive statistics'})
            results = AnalysisService.descriptive_statistics(
                dataset_id=dataset_id,
                columns=params.get('columns')
            )
            
        elif job_type == 'correlation_analysis':
            self.update_state(state='PROGRESS', meta={'progress': 30, 'status': 'Calculating correlations'})
            results = AnalysisService.correlation_analysis(
                dataset_id=dataset_id,
                columns=params.get('columns'),
                method=params.get('method', 'pearson')
            )
            
        elif job_type == 'distribution_analysis':
            self.update_state(state='PROGRESS', meta={'progress': 30, 'status': 'Analyzing distribution'})
            results = AnalysisService.distribution_analysis(
                dataset_id=dataset_id,
                column=params.get('column'),
                bins=params.get('bins', 30)
            )
            
        elif job_type == 'outlier_detection':
            self.update_state(state='PROGRESS', meta={'progress': 30, 'status': 'Detecting outliers'})
            results = AnalysisService.outlier_detection(
                dataset_id=dataset_id,
                columns=params.get('columns'),
                method=params.get('method', 'iqr')
            )
            
        else:
            raise ValueError(f"Unknown analysis type: {job_type}")
        
        # Update progress
        self.update_state(state='PROGRESS', meta={'progress': 90, 'status': 'Finalizing results'})
        
        # Mark job as completed
        job.complete_job(results)
        
        logger.info(f"Analysis job {job_id} completed successfully")
        
        return {
            'job_id': job_id,
            'status': 'completed',
            'results': results
        }
        
    except Exception as e:
        logger.error(f"Analysis job {job_id} failed: {str(e)}")
        
        # Mark job as failed
        job.fail_job(str(e))
        
        # Update task state
        self.update_state(
            state='FAILURE',
            meta={'error': str(e), 'job_id': job_id}
        )
        
        raise


@celery.task(bind=True, name='app.tasks.analysis.batch_analysis')
def batch_analysis(self, job_ids: list):
    """
    Run multiple analysis jobs in batch.
    
    Args:
        job_ids (list): List of analysis job IDs to run
    """
    logger.info(f"Starting batch analysis for jobs: {job_ids}")
    
    results = []
    total_jobs = len(job_ids)
    
    for i, job_id in enumerate(job_ids):
        try:
            # Update overall progress
            progress = int((i / total_jobs) * 100)
            self.update_state(
                state='PROGRESS',
                meta={
                    'progress': progress,
                    'status': f'Processing job {i+1} of {total_jobs}',
                    'current_job': job_id
                }
            )
            
            # Run individual analysis
            result = run_analysis.apply(args=[job_id])
            results.append({
                'job_id': job_id,
                'status': 'completed',
                'result': result.get()
            })
            
        except Exception as e:
            logger.error(f"Batch analysis failed for job {job_id}: {str(e)}")
            results.append({
                'job_id': job_id,
                'status': 'failed',
                'error': str(e)
            })
    
    logger.info(f"Batch analysis completed. {len([r for r in results if r['status'] == 'completed'])} succeeded, {len([r for r in results if r['status'] == 'failed'])} failed")
    
    return {
        'total_jobs': total_jobs,
        'completed': len([r for r in results if r['status'] == 'completed']),
        'failed': len([r for r in results if r['status'] == 'failed']),
        'results': results
    }


@celery.task(bind=True, name='app.tasks.analysis.scheduled_analysis')
def scheduled_analysis(self, dataset_id: int, analysis_config: dict):
    """
    Run scheduled analysis for a dataset.
    
    Args:
        dataset_id (int): ID of the dataset to analyze
        analysis_config (dict): Configuration for the analysis
    """
    logger.info(f"Running scheduled analysis for dataset {dataset_id}")
    
    try:
        # Create analysis jobs based on configuration
        job_ids = []
        
        for analysis_type, params in analysis_config.items():
            if params.get('enabled', False):
                # Create analysis job
                job = AnalysisJob(
                    dataset_id=dataset_id,
                    job_type=analysis_type,
                    user_id=params.get('user_id', 1),  # System user
                    parameters=params.get('parameters', {}),
                    priority=params.get('priority', 0)
                )
                
                db.session.add(job)
                db.session.commit()
                
                job_ids.append(job.id)
        
        # Run batch analysis
        if job_ids:
            result = batch_analysis.apply(args=[job_ids])
            return result.get()
        else:
            return {'message': 'No analysis jobs to run'}
            
    except Exception as e:
        logger.error(f"Scheduled analysis failed for dataset {dataset_id}: {str(e)}")
        raise


@celery.task(name='app.tasks.analysis.cleanup_old_jobs')
def cleanup_old_jobs(days_old: int = 30):
    """
    Clean up old completed analysis jobs.
    
    Args:
        days_old (int): Number of days after which to clean up jobs
    """
    from datetime import datetime, timedelta
    
    logger.info(f"Cleaning up analysis jobs older than {days_old} days")
    
    try:
        cutoff_date = datetime.utcnow() - timedelta(days=days_old)
        
        # Find old completed jobs
        old_jobs = AnalysisJob.query.filter(
            AnalysisJob.status.in_(['completed', 'failed']),
            AnalysisJob.completed_at < cutoff_date
        ).all()
        
        deleted_count = 0
        for job in old_jobs:
            db.session.delete(job)
            deleted_count += 1
        
        db.session.commit()
        
        logger.info(f"Cleaned up {deleted_count} old analysis jobs")
        
        return {
            'deleted_count': deleted_count,
            'cutoff_date': cutoff_date.isoformat()
        }
        
    except Exception as e:
        logger.error(f"Job cleanup failed: {str(e)}")
        db.session.rollback()
        raise