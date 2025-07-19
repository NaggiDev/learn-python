"""
Dataset management API endpoints.
"""
import os
from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.models import Dataset

ns = Namespace('datasets', description='Dataset management operations')

# API models for documentation
dataset_model = ns.model('Dataset', {
    'id': fields.Integer(description='Dataset ID'),
    'name': fields.String(required=True, description='Dataset name'),
    'filename': fields.String(description='Original filename'),
    'file_size': fields.Integer(description='File size in bytes'),
    'file_size_formatted': fields.String(description='Human-readable file size'),
    'file_type': fields.String(description='File type'),
    'upload_date': fields.String(description='Upload timestamp'),
    'description': fields.String(description='Dataset description'),
    'row_count': fields.Integer(description='Number of rows'),
    'column_count': fields.Integer(description='Number of columns'),
    'user_id': fields.Integer(description='Owner user ID')
})

dataset_upload_model = ns.model('DatasetUpload', {
    'name': fields.String(required=True, description='Dataset name'),
    'description': fields.String(description='Dataset description')
})


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@ns.route('')
class DatasetList(Resource):
    @ns.doc('list_datasets')
    @ns.marshal_list_with(dataset_model)
    @login_required
    def get(self):
        """Get list of user's datasets."""
        try:
            datasets = Dataset.query.filter_by(user_id=current_user.id).all()
            return [dataset.to_dict() for dataset in datasets]
        except Exception as e:
            current_app.logger.error(f'Error listing datasets: {str(e)}')
            ns.abort(500, 'Failed to retrieve datasets')

    @ns.doc('upload_dataset')
    @ns.expect(dataset_upload_model)
    @ns.marshal_with(dataset_model, code=201)
    @login_required
    def post(self):
        """Upload a new dataset."""
        try:
            # Check if file is present
            if 'file' not in request.files:
                ns.abort(400, 'No file provided')
            
            file = request.files['file']
            if file.filename == '':
                ns.abort(400, 'No file selected')
            
            if not allowed_file(file.filename):
                ns.abort(400, 'File type not allowed')
            
            # Get form data
            name = request.form.get('name', file.filename)
            description = request.form.get('description', '')
            
            # Secure filename and create path
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            
            # Ensure unique filename
            counter = 1
            base_name, ext = os.path.splitext(filename)
            while os.path.exists(file_path):
                filename = f"{base_name}_{counter}{ext}"
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                counter += 1
            
            # Save file
            file.save(file_path)
            file_size = os.path.getsize(file_path)
            file_type = filename.rsplit('.', 1)[1].lower()
            
            # Create dataset record
            dataset = Dataset(
                name=name,
                filename=filename,
                file_path=file_path,
                file_size=file_size,
                file_type=file_type,
                user_id=current_user.id,
                description=description
            )
            
            db.session.add(dataset)
            db.session.commit()
            
            current_app.logger.info(f'Dataset uploaded: {name} by {current_user.username}')
            
            return dataset.to_dict(), 201
            
        except Exception as e:
            current_app.logger.error(f'Error uploading dataset: {str(e)}')
            ns.abort(500, 'Failed to upload dataset')


@ns.route('/<int:dataset_id>')
class DatasetDetail(Resource):
    @ns.doc('get_dataset')
    @ns.marshal_with(dataset_model)
    @login_required
    def get(self, dataset_id):
        """Get dataset details."""
        try:
            dataset = Dataset.query.get_or_404(dataset_id)
            
            # Check permissions
            if not current_user.can_access_dataset(dataset):
                ns.abort(403, 'Access denied')
            
            return dataset.to_dict()
            
        except Exception as e:
            current_app.logger.error(f'Error getting dataset {dataset_id}: {str(e)}')
            ns.abort(500, 'Failed to retrieve dataset')

    @ns.doc('delete_dataset')
    @login_required
    def delete(self, dataset_id):
        """Delete a dataset."""
        try:
            dataset = Dataset.query.get_or_404(dataset_id)
            
            # Check permissions
            if not current_user.can_access_dataset(dataset):
                ns.abort(403, 'Access denied')
            
            # Delete physical file
            dataset.delete_file()
            
            # Delete database record
            db.session.delete(dataset)
            db.session.commit()
            
            current_app.logger.info(f'Dataset deleted: {dataset.name} by {current_user.username}')
            
            return {'message': 'Dataset deleted successfully'}, 200
            
        except Exception as e:
            current_app.logger.error(f'Error deleting dataset {dataset_id}: {str(e)}')
            ns.abort(500, 'Failed to delete dataset')


@ns.route('/<int:dataset_id>/preview')
class DatasetPreview(Resource):
    @ns.doc('preview_dataset')
    @login_required
    def get(self, dataset_id):
        """Preview dataset content."""
        try:
            dataset = Dataset.query.get_or_404(dataset_id)
            
            # Check permissions
            if not current_user.can_access_dataset(dataset):
                ns.abort(403, 'Access denied')
            
            # TODO: Implement data preview logic
            # This would involve reading the file and returning a sample
            return {
                'message': 'Preview functionality to be implemented',
                'dataset_id': dataset_id
            }
            
        except Exception as e:
            current_app.logger.error(f'Error previewing dataset {dataset_id}: {str(e)}')
            ns.abort(500, 'Failed to preview dataset')