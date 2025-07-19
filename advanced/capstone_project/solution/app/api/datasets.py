"""
Dataset management API endpoints.
"""
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from flask_restx import Api, Resource, fields, Namespace
from werkzeug.datastructures import FileStorage
from marshmallow import Schema, fields as ma_fields, ValidationError
from app import db
from app.models.dataset import Dataset
from app.services.data_service import DataService

# Create blueprint
datasets_bp = Blueprint('datasets', __name__, url_prefix='/api/datasets')
datasets_ns = Namespace('datasets', description='Dataset management operations')

# Flask-RESTX models for documentation
dataset_response_model = datasets_ns.model('DatasetResponse', {
    'id': fields.Integer(description='Dataset ID'),
    'name': fields.String(description='Dataset name'),
    'filename': fields.String(description='Original filename'),
    'file_size': fields.Integer(description='File size in bytes'),
    'file_size_formatted': fields.String(description='Formatted file size'),
    'file_type': fields.String(description='File type/extension'),
    'upload_date': fields.String(description='Upload timestamp'),
    'description': fields.String(description='Dataset description'),
    'row_count': fields.Integer(description='Number of rows'),
    'column_count': fields.Integer(description='Number of columns'),
    'is_processed': fields.Boolean(description='Whether dataset has been processed'),
    'file_exists': fields.Boolean(description='Whether file exists on disk')
})

dataset_upload_parser = datasets_ns.parser()
dataset_upload_parser.add_argument('file', location='files', type=FileStorage, required=True, help='Dataset file to upload')
dataset_upload_parser.add_argument('name', type=str, help='Display name for the dataset')
dataset_upload_parser.add_argument('description', type=str, help='Dataset description')

dataset_preview_model = datasets_ns.model('DatasetPreview', {
    'columns': fields.List(fields.String, description='Column names'),
    'data': fields.List(fields.Raw, description='Preview data rows'),
    'total_rows': fields.Integer(description='Total number of rows'),
    'total_columns': fields.Integer(description='Total number of columns'),
    'dtypes': fields.Raw(description='Column data types')
})


@datasets_ns.route('')
class DatasetList(Resource):
    """Dataset list endpoint."""
    
    @datasets_ns.marshal_list_with(dataset_response_model)
    @datasets_ns.doc('list_datasets')
    @login_required
    def get(self):
        """Get list of user's datasets."""
        page = request.args.get('page', 1, type=int)
        per_page = min(request.args.get('per_page', 10, type=int), 100)
        
        # Get user's datasets
        query = Dataset.query.filter_by(user_id=current_user.id)
        
        # Apply filters
        if request.args.get('file_type'):
            query = query.filter_by(file_type=request.args.get('file_type'))
        
        if request.args.get('search'):
            search_term = f"%{request.args.get('search')}%"
            query = query.filter(Dataset.name.like(search_term))
        
        # Order by upload date (newest first)
        query = query.order_by(Dataset.upload_date.desc())
        
        # Paginate
        datasets = query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        
        return {
            'datasets': [dataset.to_dict() for dataset in datasets.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': datasets.total,
                'pages': datasets.pages,
                'has_next': datasets.has_next,
                'has_prev': datasets.has_prev
            }
        }
    
    @datasets_ns.expect(dataset_upload_parser)
    @datasets_ns.marshal_with(dataset_response_model, code=201)
    @datasets_ns.doc('upload_dataset')
    @login_required
    def post(self):
        """Upload a new dataset."""
        args = dataset_upload_parser.parse_args()
        
        if 'file' not in request.files:
            return {'error': 'No file provided'}, 400
        
        file = request.files['file']
        if file.filename == '':
            return {'error': 'No file selected'}, 400
        
        try:
            dataset = DataService.save_uploaded_file(
                file=file,
                user_id=current_user.id,
                name=args.get('name'),
                description=args.get('description')
            )
            
            current_app.logger.info(f'Dataset uploaded by user {current_user.username}: {dataset.name}')
            
            return dataset.to_dict(), 201
            
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            current_app.logger.error(f'Dataset upload failed: {str(e)}')
            return {'error': 'Upload failed'}, 500


@datasets_ns.route('/<int:dataset_id>')
class DatasetDetail(Resource):
    """Dataset detail endpoint."""
    
    @datasets_ns.marshal_with(dataset_response_model)
    @datasets_ns.doc('get_dataset')
    @login_required
    def get(self, dataset_id):
        """Get dataset details."""
        dataset = Dataset.query.get_or_404(dataset_id)
        
        # Check permissions
        if not current_user.can_view_dataset(dataset):
            return {'error': 'Access denied'}, 403
        
        return DataService.get_dataset_info(dataset)
    
    @datasets_ns.expect(datasets_ns.model('DatasetUpdate', {
        'name': fields.String(description='Dataset name'),
        'description': fields.String(description='Dataset description')
    }))
    @datasets_ns.marshal_with(dataset_response_model)
    @datasets_ns.doc('update_dataset')
    @login_required
    def put(self, dataset_id):
        """Update dataset information."""
        dataset = Dataset.query.get_or_404(dataset_id)
        
        # Check permissions
        if not current_user.can_edit_dataset(dataset):
            return {'error': 'Access denied'}, 403
        
        data = request.json or {}
        
        try:
            if 'name' in data:
                dataset.name = data['name'].strip()
                if not dataset.name:
                    return {'error': 'Name cannot be empty'}, 400
            
            if 'description' in data:
                dataset.description = data['description']
            
            db.session.commit()
            
            current_app.logger.info(f'Dataset updated: {dataset.name} (ID: {dataset.id})')
            
            return dataset.to_dict(), 200
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f'Dataset update failed: {str(e)}')
            return {'error': 'Update failed'}, 500
    
    @datasets_ns.doc('delete_dataset')
    @login_required
    def delete(self, dataset_id):
        """Delete a dataset."""
        dataset = Dataset.query.get_or_404(dataset_id)
        
        # Check permissions
        if not current_user.can_edit_dataset(dataset):
            return {'error': 'Access denied'}, 403
        
        try:
            if DataService.delete_dataset(dataset):
                return {'message': 'Dataset deleted successfully'}, 200
            else:
                return {'error': 'Failed to delete dataset'}, 500
                
        except Exception as e:
            current_app.logger.error(f'Dataset deletion failed: {str(e)}')
            return {'error': 'Deletion failed'}, 500


@datasets_ns.route('/<int:dataset_id>/preview')
class DatasetPreview(Resource):
    """Dataset preview endpoint."""
    
    @datasets_ns.marshal_with(dataset_preview_model)
    @datasets_ns.doc('preview_dataset')
    @login_required
    def get(self, dataset_id):
        """Get dataset preview."""
        dataset = Dataset.query.get_or_404(dataset_id)
        
        # Check permissions
        if not current_user.can_view_dataset(dataset):
            return {'error': 'Access denied'}, 403
        
        rows = request.args.get('rows', 10, type=int)
        rows = min(max(rows, 1), 100)  # Limit between 1 and 100
        
        try:
            preview = DataService.get_dataset_preview(dataset_id, rows)
            return preview, 200
            
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            current_app.logger.error(f'Dataset preview failed: {str(e)}')
            return {'error': 'Preview failed'}, 500


@datasets_ns.route('/<int:dataset_id>/columns/<string:column_name>/stats')
class ColumnStatistics(Resource):
    """Column statistics endpoint."""
    
    @datasets_ns.doc('get_column_stats')
    @login_required
    def get(self, dataset_id, column_name):
        """Get statistics for a specific column."""
        dataset = Dataset.query.get_or_404(dataset_id)
        
        # Check permissions
        if not current_user.can_view_dataset(dataset):
            return {'error': 'Access denied'}, 403
        
        try:
            stats = DataService.get_column_statistics(dataset, column_name)
            return stats, 200
            
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            current_app.logger.error(f'Column statistics failed: {str(e)}')
            return {'error': 'Statistics calculation failed'}, 500


@datasets_ns.route('/<int:dataset_id>/download')
class DatasetDownload(Resource):
    """Dataset download endpoint."""
    
    @datasets_ns.doc('download_dataset')
    @login_required
    def get(self, dataset_id):
        """Download dataset file."""
        dataset = Dataset.query.get_or_404(dataset_id)
        
        # Check permissions
        if not current_user.can_view_dataset(dataset):
            return {'error': 'Access denied'}, 403
        
        if not dataset.file_exists():
            return {'error': 'Dataset file not found'}, 404
        
        try:
            from flask import send_file
            return send_file(
                dataset.file_path,
                as_attachment=True,
                download_name=dataset.filename,
                mimetype='application/octet-stream'
            )
            
        except Exception as e:
            current_app.logger.error(f'Dataset download failed: {str(e)}')
            return {'error': 'Download failed'}, 500


# Register namespace with blueprint
datasets_bp.add_url_rule('', view_func=DatasetList.as_view('dataset_list'))
datasets_bp.add_url_rule('/<int:dataset_id>', view_func=DatasetDetail.as_view('dataset_detail'))
datasets_bp.add_url_rule('/<int:dataset_id>/preview', view_func=DatasetPreview.as_view('dataset_preview'))
datasets_bp.add_url_rule('/<int:dataset_id>/columns/<string:column_name>/stats', view_func=ColumnStatistics.as_view('column_stats'))
datasets_bp.add_url_rule('/<int:dataset_id>/download', view_func=DatasetDownload.as_view('dataset_download'))