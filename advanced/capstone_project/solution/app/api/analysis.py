"""
Analysis API endpoints.
"""
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from flask_restx import Api, Resource, fields, Namespace
from app import db
from app.models.dataset import Dataset
from app.models.analysis_job import AnalysisJob
from app.services.analysis_service import AnalysisService
from app.tasks.analysis_tasks import run_analysis

# Create blueprint
analysis_bp = Blueprint('analysis', __name__, url_prefix='/api/analysis')
analysis_ns = Namespace('analysis', description='Data analysis operations')

# Flask-RESTX models
analysis_request_model = analysis_ns.model('AnalysisRequest', {
    'dataset_id': fields.Integer(required=True, description='Dataset ID'),
    'analysis_type': fields.String(required=True, description='Type of analysis', 
                                  enum=['descriptive_statistics', 'correlation_analysis', 'distribution_analysis', 'outlier_detection']),
    'parameters': fields.Raw(description='Analysis parameters'),
    'async': fields.Boolean(default=True, description='Run analysis asynchronously')
})

analysis_job_model = analysis_ns.model('AnalysisJob', {
    'id': fields.Integer(description='Job ID'),
    'dataset_id': fields.Integer(description='Dataset ID'),
    'job_type': fields.String(description='Analysis type'),
    'status': fields.String(description='Job status'),
    'created_at': fields.String(description='Creation timestamp'),
    'completed_at': fields.String(description='Completion timestamp'),
    'progress': fields.Integer(description='Progress percentage')
})


@analysis_ns.route('/run')
class RunAnalysis(Resource):
    """Run analysis endpoint."""
    
    @analysis_ns.expect(analysis_request_model)
    @analysis_ns.doc('run_analysis')
    @login_required
    def post(self):
        """Run data analysis."""
        data = request.json
        
        # Validate input
        if not data or 'dataset_id' not in data or 'analysis_type' not in data:
            return {'error': 'Missing required fields'}, 400
        
        dataset_id = data['dataset_id']
        analysis_type = data['analysis_type']
        parameters = data.get('parameters', {})
        run_async = data.get('async', True)
        
        # Check if dataset exists and user has access
        dataset = Dataset.query.get(dataset_id)
        if not dataset:
            return {'error': 'Dataset not found'}, 404
        
        if not current_user.can_view_dataset(dataset):
            return {'error': 'Access denied'}, 403
        
        try:
            if run_async:
                # Create analysis job
                job = AnalysisJob(
                    dataset_id=dataset_id,
                    job_type=analysis_type,
                    user_id=current_user.id,
                    parameters=parameters
                )
                
                db.session.add(job)
                db.session.commit()
                
                # Start background task
                task = run_analysis.delay(job.id)
                job.celery_task_id = task.id
                db.session.commit()
                
                return {
                    'job_id': job.id,
                    'task_id': task.id,
                    'status': 'started',
                    'message': 'Analysis started in background'
                }, 202
            
            else:
                # Run analysis synchronously
                if analysis_type == 'descriptive_statistics':
                    result = AnalysisService.descriptive_statistics(
                        dataset_id=dataset_id,
                        columns=parameters.get('columns')
                    )
                elif analysis_type == 'correlation_analysis':
                    result = AnalysisService.correlation_analysis(
                        dataset_id=dataset_id,
                        columns=parameters.get('columns'),
                        method=parameters.get('method', 'pearson')
                    )
                elif analysis_type == 'distribution_analysis':
                    result = AnalysisService.distribution_analysis(
                        dataset_id=dataset_id,
                        column=parameters.get('column'),
                        bins=parameters.get('bins', 30)
                    )
                elif analysis_type == 'outlier_detection':
                    result = AnalysisService.outlier_detection(
                        dataset_id=dataset_id,
                        columns=parameters.get('columns'),
                        method=parameters.get('method', 'iqr')
                    )
                else:
                    return {'error': f'Unknown analysis type: {analysis_type}'}, 400
                
                return {
                    'status': 'completed',
                    'result': result
                }, 200
                
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            current_app.logger.error(f'Analysis failed: {str(e)}')
            return {'error': 'Analysis failed'}, 500


@analysis_ns.route('/jobs')
class AnalysisJobList(Resource):
    """Analysis jobs list endpoint."""
    
    @analysis_ns.marshal_list_with(analysis_job_model)
    @analysis_ns.doc('list_analysis_jobs')
    @login_required
    def get(self):
        """Get list of user's analysis jobs."""
        page = request.args.get('page', 1, type=int)
        per_page = min(request.args.get('per_page', 20, type=int), 100)
        
        # Get user's analysis jobs
        query = AnalysisJob.query.filter_by(user_id=current_user.id)
        
        # Apply filters
        if request.args.get('status'):
            query = query.filter_by(status=request.args.get('status'))
        
        if request.args.get('job_type'):
            query = query.filter_by(job_type=request.args.get('job_type'))
        
        if request.args.get('dataset_id'):
            query = query.filter_by(dataset_id=request.args.get('dataset_id', type=int))
        
        # Order by creation date (newest first)
        query = query.order_by(AnalysisJob.created_at.desc())
        
        # Paginate
        jobs = query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        
        return {
            'jobs': [job.to_dict(include_results=False) for job in jobs.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': jobs.total,
                'pages': jobs.pages,
                'has_next': jobs.has_next,
                'has_prev': jobs.has_prev
            }
        }


@analysis_ns.route('/jobs/<int:job_id>')
class AnalysisJobDetail(Resource):
    """Analysis job detail endpoint."""
    
    @analysis_ns.doc('get_analysis_job')
    @login_required
    def get(self, job_id):
        """Get analysis job details."""
        job = AnalysisJob.query.get_or_404(job_id)
        
        # Check permissions
        if job.user_id != current_user.id and not current_user.is_admin():
            return {'error': 'Access denied'}, 403
        
        return job.to_dict(), 200
    
    @analysis_ns.doc('delete_analysis_job')
    @login_required
    def delete(self, job_id):
        """Delete analysis job."""
        job = AnalysisJob.query.get_or_404(job_id)
        
        # Check permissions
        if job.user_id != current_user.id and not current_user.is_admin():
            return {'error': 'Access denied'}, 403
        
        try:
            # Cancel Celery task if still running
            if job.celery_task_id and job.status == 'running':
                from celery_app import celery
                celery.control.revoke(job.celery_task_id, terminate=True)
            
            db.session.delete(job)
            db.session.commit()
            
            return {'message': 'Analysis job deleted successfully'}, 200
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f'Job deletion failed: {str(e)}')
            return {'error': 'Deletion failed'}, 500


@analysis_ns.route('/jobs/<int:job_id>/retry')
class RetryAnalysisJob(Resource):
    """Retry analysis job endpoint."""
    
    @analysis_ns.doc('retry_analysis_job')
    @login_required
    def post(self, job_id):
        """Retry failed analysis job."""
        job = AnalysisJob.query.get_or_404(job_id)
        
        # Check permissions
        if job.user_id != current_user.id and not current_user.is_admin():
            return {'error': 'Access denied'}, 403
        
        if not job.can_retry():
            return {'error': 'Job cannot be retried'}, 400
        
        try:
            # Retry the job
            if job.retry_job():
                # Start new background task
                task = run_analysis.delay(job.id)
                job.celery_task_id = task.id
                db.session.commit()
                
                return {
                    'job_id': job.id,
                    'task_id': task.id,
                    'status': 'retrying',
                    'retry_count': job.retry_count
                }, 200
            else:
                return {'error': 'Maximum retries exceeded'}, 400
                
        except Exception as e:
            current_app.logger.error(f'Job retry failed: {str(e)}')
            return {'error': 'Retry failed'}, 500


@analysis_ns.route('/descriptive')
class DescriptiveStatistics(Resource):
    """Descriptive statistics endpoint."""
    
    @analysis_ns.doc('descriptive_statistics')
    @login_required
    def post(self):
        """Calculate descriptive statistics."""
        data = request.json or {}
        dataset_id = data.get('dataset_id')
        columns = data.get('columns')
        
        if not dataset_id:
            return {'error': 'Dataset ID required'}, 400
        
        # Check dataset access
        dataset = Dataset.query.get(dataset_id)
        if not dataset or not current_user.can_view_dataset(dataset):
            return {'error': 'Dataset not found or access denied'}, 404
        
        try:
            result = AnalysisService.descriptive_statistics(dataset_id, columns)
            return result, 200
        except Exception as e:
            return {'error': str(e)}, 400


@analysis_ns.route('/correlation')
class CorrelationAnalysis(Resource):
    """Correlation analysis endpoint."""
    
    @analysis_ns.doc('correlation_analysis')
    @login_required
    def post(self):
        """Calculate correlation matrix."""
        data = request.json or {}
        dataset_id = data.get('dataset_id')
        columns = data.get('columns')
        method = data.get('method', 'pearson')
        
        if not dataset_id:
            return {'error': 'Dataset ID required'}, 400
        
        # Check dataset access
        dataset = Dataset.query.get(dataset_id)
        if not dataset or not current_user.can_view_dataset(dataset):
            return {'error': 'Dataset not found or access denied'}, 404
        
        try:
            result = AnalysisService.correlation_analysis(dataset_id, columns, method)
            return result, 200
        except Exception as e:
            return {'error': str(e)}, 400


# Register namespace with blueprint
analysis_bp.add_url_rule('/run', view_func=RunAnalysis.as_view('run_analysis'))
analysis_bp.add_url_rule('/jobs', view_func=AnalysisJobList.as_view('analysis_jobs'))
analysis_bp.add_url_rule('/jobs/<int:job_id>', view_func=AnalysisJobDetail.as_view('analysis_job_detail'))
analysis_bp.add_url_rule('/jobs/<int:job_id>/retry', view_func=RetryAnalysisJob.as_view('retry_job'))
analysis_bp.add_url_rule('/descriptive', view_func=DescriptiveStatistics.as_view('descriptive_stats'))
analysis_bp.add_url_rule('/correlation', view_func=CorrelationAnalysis.as_view('correlation_analysis'))