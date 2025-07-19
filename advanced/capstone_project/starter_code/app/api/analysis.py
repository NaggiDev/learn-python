"""
Data analysis API endpoints.
"""
from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user
from app import db
from app.models import Dataset, AnalysisJob

ns = Namespace('analysis', description='Data analysis operations')

# API models for documentation
analysis_job_model = ns.model('AnalysisJob', {
    'id': fields.Integer(description='Job ID'),
    'job_type': fields.String(description='Type of analysis'),
    'status': fields.String(description='Job status'),
    'parameters': fields.Raw(description='Analysis parameters'),
    'results': fields.Raw(description='Analysis results'),
    'error_message': fields.String(description='Error message if failed'),
    'created_at': fields.String(description='Creation timestamp'),
    'started_at': fields.String(description='Start timestamp'),
    'completed_at': fields.String(description='Completion timestamp'),
    'duration': fields.Float(description='Duration in seconds'),
    'dataset_id': fields.Integer(description='Dataset ID'),
    'user_id': fields.Integer(description='User ID')
})

analysis_request_model = ns.model('AnalysisRequest', {
    'dataset_id': fields.Integer(required=True, description='Dataset ID'),
    'job_type': fields.String(required=True, description='Type of analysis'),
    'parameters': fields.Raw(description='Analysis parameters')
})


@ns.route('/jobs')
class AnalysisJobList(Resource):
    @ns.doc('list_analysis_jobs')
    @ns.marshal_list_with(analysis_job_model)
    @login_required
    def get(self):
        """Get list of user's analysis jobs."""
        try:
            jobs = AnalysisJob.query.filter_by(user_id=current_user.id).order_by(
                AnalysisJob.created_at.desc()
            ).all()
            return [job.to_dict() for job in jobs]
        except Exception as e:
            current_app.logger.error(f'Error listing analysis jobs: {str(e)}')
            ns.abort(500, 'Failed to retrieve analysis jobs')

    @ns.doc('create_analysis_job')
    @ns.expect(analysis_request_model)
    @ns.marshal_with(analysis_job_model, code=201)
    @login_required
    def post(self):
        """Create a new analysis job."""
        try:
            data = request.get_json()
            
            # Validate required fields
            if not data.get('dataset_id') or not data.get('job_type'):
                ns.abort(400, 'dataset_id and job_type are required')
            
            dataset_id = data['dataset_id']
            job_type = data['job_type']
            parameters = data.get('parameters', {})
            
            # Check if dataset exists and user has access
            dataset = Dataset.query.get_or_404(dataset_id)
            if not current_user.can_access_dataset(dataset):
                ns.abort(403, 'Access denied to dataset')
            
            # Validate job type
            if job_type not in AnalysisJob.VALID_JOB_TYPES:
                ns.abort(400, f'Invalid job type. Valid types: {AnalysisJob.VALID_JOB_TYPES}')
            
            # Create analysis job
            job = AnalysisJob(
                job_type=job_type,
                dataset_id=dataset_id,
                user_id=current_user.id,
                parameters=parameters
            )
            
            db.session.add(job)
            db.session.commit()
            
            # TODO: Queue job for background processing
            current_app.logger.info(f'Analysis job created: {job.id} by {current_user.username}')
            
            return job.to_dict(), 201
            
        except Exception as e:
            current_app.logger.error(f'Error creating analysis job: {str(e)}')
            ns.abort(500, 'Failed to create analysis job')


@ns.route('/jobs/<int:job_id>')
class AnalysisJobDetail(Resource):
    @ns.doc('get_analysis_job')
    @ns.marshal_with(analysis_job_model)
    @login_required
    def get(self, job_id):
        """Get analysis job details."""
        try:
            job = AnalysisJob.query.get_or_404(job_id)
            
            # Check permissions
            if job.user_id != current_user.id and not current_user.is_admin():
                ns.abort(403, 'Access denied')
            
            return job.to_dict()
            
        except Exception as e:
            current_app.logger.error(f'Error getting analysis job {job_id}: {str(e)}')
            ns.abort(500, 'Failed to retrieve analysis job')

    @ns.doc('cancel_analysis_job')
    @login_required
    def delete(self, job_id):
        """Cancel an analysis job."""
        try:
            job = AnalysisJob.query.get_or_404(job_id)
            
            # Check permissions
            if job.user_id != current_user.id and not current_user.is_admin():
                ns.abort(403, 'Access denied')
            
            # Can only cancel pending or running jobs
            if job.status not in ['pending', 'running']:
                ns.abort(400, 'Job cannot be cancelled')
            
            job.cancel_job()
            
            current_app.logger.info(f'Analysis job cancelled: {job_id} by {current_user.username}')
            
            return {'message': 'Job cancelled successfully'}, 200
            
        except Exception as e:
            current_app.logger.error(f'Error cancelling analysis job {job_id}: {str(e)}')
            ns.abort(500, 'Failed to cancel analysis job')


@ns.route('/descriptive')
class DescriptiveAnalysis(Resource):
    @ns.doc('descriptive_analysis')
    @ns.expect(analysis_request_model)
    @ns.marshal_with(analysis_job_model, code=201)
    @login_required
    def post(self):
        """Generate descriptive statistics for a dataset."""
        try:
            data = request.get_json()
            data['job_type'] = 'descriptive_stats'
            
            # Reuse the job creation logic
            return AnalysisJobList().post()
            
        except Exception as e:
            current_app.logger.error(f'Error creating descriptive analysis: {str(e)}')
            ns.abort(500, 'Failed to create descriptive analysis')


@ns.route('/correlation')
class CorrelationAnalysis(Resource):
    @ns.doc('correlation_analysis')
    @ns.expect(analysis_request_model)
    @ns.marshal_with(analysis_job_model, code=201)
    @login_required
    def post(self):
        """Calculate correlation matrix for a dataset."""
        try:
            data = request.get_json()
            data['job_type'] = 'correlation_analysis'
            
            # Reuse the job creation logic
            return AnalysisJobList().post()
            
        except Exception as e:
            current_app.logger.error(f'Error creating correlation analysis: {str(e)}')
            ns.abort(500, 'Failed to create correlation analysis')


@ns.route('/distribution')
class DistributionAnalysis(Resource):
    @ns.doc('distribution_analysis')
    @ns.expect(analysis_request_model)
    @ns.marshal_with(analysis_job_model, code=201)
    @login_required
    def post(self):
        """Analyze data distributions for a dataset."""
        try:
            data = request.get_json()
            data['job_type'] = 'distribution_analysis'
            
            # Reuse the job creation logic
            return AnalysisJobList().post()
            
        except Exception as e:
            current_app.logger.error(f'Error creating distribution analysis: {str(e)}')
            ns.abort(500, 'Failed to create distribution analysis')