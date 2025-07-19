"""
Background tasks for report generation.
"""
from celery.utils.log import get_task_logger
from app import db
from app.models.dataset import Dataset
from app.services.analysis_service import AnalysisService
from celery_app import celery

logger = get_task_logger(__name__)


@celery.task(bind=True, name='app.tasks.reports.generate_report')
def generate_report(self, dataset_id: int, report_config: dict):
    """
    Generate analysis report for a dataset.
    
    Args:
        dataset_id (int): ID of the dataset
        report_config (dict): Report configuration
    """
    logger.info(f"Generating report for dataset {dataset_id}")
    
    dataset = Dataset.query.get(dataset_id)
    if not dataset:
        logger.error(f"Dataset {dataset_id} not found")
        return {'error': 'Dataset not found'}
    
    try:
        self.update_state(state='PROGRESS', meta={'progress': 10, 'status': 'Initializing report'})
        
        report_data = {
            'dataset_info': dataset.to_dict(),
            'analyses': {}
        }
        
        # Run requested analyses
        total_analyses = len(report_config.get('analyses', []))
        
        for i, analysis_type in enumerate(report_config.get('analyses', [])):
            progress = 20 + (i / total_analyses) * 60
            self.update_state(state='PROGRESS', meta={
                'progress': int(progress),
                'status': f'Running {analysis_type} analysis'
            })
            
            try:
                if analysis_type == 'descriptive_statistics':
                    result = AnalysisService.descriptive_statistics(dataset_id)
                elif analysis_type == 'correlation_analysis':
                    result = AnalysisService.correlation_analysis(dataset_id)
                else:
                    logger.warning(f"Unknown analysis type: {analysis_type}")
                    continue
                
                report_data['analyses'][analysis_type] = result
                
            except Exception as e:
                logger.error(f"Analysis {analysis_type} failed: {str(e)}")
                report_data['analyses'][analysis_type] = {'error': str(e)}
        
        self.update_state(state='PROGRESS', meta={'progress': 90, 'status': 'Finalizing report'})
        
        # Generate report summary
        report_data['summary'] = {
            'total_analyses': len(report_data['analyses']),
            'successful_analyses': len([a for a in report_data['analyses'].values() if 'error' not in a]),
            'failed_analyses': len([a for a in report_data['analyses'].values() if 'error' in a])
        }
        
        logger.info(f"Report generated successfully for dataset {dataset_id}")
        
        return {
            'dataset_id': dataset_id,
            'status': 'completed',
            'report_data': report_data
        }
        
    except Exception as e:
        logger.error(f"Report generation failed for dataset {dataset_id}: {str(e)}")
        
        self.update_state(
            state='FAILURE',
            meta={'error': str(e), 'dataset_id': dataset_id}
        )
        
        raise