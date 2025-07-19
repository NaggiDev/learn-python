"""
Dashboard management API endpoints.
"""
from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user
from app import db
from app.models import Dashboard

ns = Namespace('dashboards', description='Dashboard management operations')

# API models for documentation
dashboard_model = ns.model('Dashboard', {
    'id': fields.Integer(description='Dashboard ID'),
    'name': fields.String(required=True, description='Dashboard name'),
    'description': fields.String(description='Dashboard description'),
    'is_public': fields.Boolean(description='Whether dashboard is public'),
    'created_at': fields.String(description='Creation timestamp'),
    'updated_at': fields.String(description='Last update timestamp'),
    'user_id': fields.Integer(description='Creator user ID'),
    'chart_count': fields.Integer(description='Number of charts'),
    'layout_config': fields.Raw(description='Dashboard layout configuration')
})

dashboard_create_model = ns.model('DashboardCreate', {
    'name': fields.String(required=True, description='Dashboard name'),
    'description': fields.String(description='Dashboard description'),
    'is_public': fields.Boolean(description='Whether dashboard is public'),
    'layout_config': fields.Raw(required=True, description='Dashboard layout configuration')
})

dashboard_update_model = ns.model('DashboardUpdate', {
    'name': fields.String(description='Dashboard name'),
    'description': fields.String(description='Dashboard description'),
    'is_public': fields.Boolean(description='Whether dashboard is public'),
    'layout_config': fields.Raw(description='Dashboard layout configuration')
})


@ns.route('')
class DashboardList(Resource):
    @ns.doc('list_dashboards')
    @ns.marshal_list_with(dashboard_model)
    @login_required
    def get(self):
        """Get list of user's dashboards."""
        try:
            # Get user's own dashboards and public dashboards
            user_dashboards = Dashboard.query.filter_by(user_id=current_user.id).all()
            public_dashboards = Dashboard.query.filter(
                Dashboard.is_public == True,
                Dashboard.user_id != current_user.id
            ).all()
            
            all_dashboards = user_dashboards + public_dashboards
            return [dashboard.to_dict(include_config=False) for dashboard in all_dashboards]
            
        except Exception as e:
            current_app.logger.error(f'Error listing dashboards: {str(e)}')
            ns.abort(500, 'Failed to retrieve dashboards')

    @ns.doc('create_dashboard')
    @ns.expect(dashboard_create_model)
    @ns.marshal_with(dashboard_model, code=201)
    @login_required
    def post(self):
        """Create a new dashboard."""
        try:
            data = request.get_json()
            
            # Validate required fields
            if not data.get('name') or not data.get('layout_config'):
                ns.abort(400, 'name and layout_config are required')
            
            # Create dashboard
            dashboard = Dashboard(
                name=data['name'],
                layout_config=data['layout_config'],
                user_id=current_user.id,
                description=data.get('description', ''),
                is_public=data.get('is_public', False)
            )
            
            db.session.add(dashboard)
            db.session.commit()
            
            current_app.logger.info(f'Dashboard created: {dashboard.name} by {current_user.username}')
            
            return dashboard.to_dict(), 201
            
        except Exception as e:
            current_app.logger.error(f'Error creating dashboard: {str(e)}')
            ns.abort(500, 'Failed to create dashboard')


@ns.route('/<int:dashboard_id>')
class DashboardDetail(Resource):
    @ns.doc('get_dashboard')
    @ns.marshal_with(dashboard_model)
    @login_required
    def get(self, dashboard_id):
        """Get dashboard details."""
        try:
            dashboard = Dashboard.query.get_or_404(dashboard_id)
            
            # Check permissions
            if not dashboard.can_be_accessed_by(current_user):
                ns.abort(403, 'Access denied')
            
            return dashboard.to_dict()
            
        except Exception as e:
            current_app.logger.error(f'Error getting dashboard {dashboard_id}: {str(e)}')
            ns.abort(500, 'Failed to retrieve dashboard')

    @ns.doc('update_dashboard')
    @ns.expect(dashboard_update_model)
    @ns.marshal_with(dashboard_model)
    @login_required
    def put(self, dashboard_id):
        """Update a dashboard."""
        try:
            dashboard = Dashboard.query.get_or_404(dashboard_id)
            
            # Check permissions
            if not dashboard.can_be_edited_by(current_user):
                ns.abort(403, 'Access denied')
            
            data = request.get_json()
            
            # Update fields
            if 'name' in data:
                dashboard.name = data['name']
            if 'description' in data:
                dashboard.description = data['description']
            if 'is_public' in data:
                dashboard.is_public = data['is_public']
            if 'layout_config' in data:
                dashboard.set_layout_config(data['layout_config'])
            
            db.session.commit()
            
            current_app.logger.info(f'Dashboard updated: {dashboard.name} by {current_user.username}')
            
            return dashboard.to_dict()
            
        except Exception as e:
            current_app.logger.error(f'Error updating dashboard {dashboard_id}: {str(e)}')
            ns.abort(500, 'Failed to update dashboard')

    @ns.doc('delete_dashboard')
    @login_required
    def delete(self, dashboard_id):
        """Delete a dashboard."""
        try:
            dashboard = Dashboard.query.get_or_404(dashboard_id)
            
            # Check permissions
            if not dashboard.can_be_edited_by(current_user):
                ns.abort(403, 'Access denied')
            
            dashboard_name = dashboard.name
            db.session.delete(dashboard)
            db.session.commit()
            
            current_app.logger.info(f'Dashboard deleted: {dashboard_name} by {current_user.username}')
            
            return {'message': 'Dashboard deleted successfully'}, 200
            
        except Exception as e:
            current_app.logger.error(f'Error deleting dashboard {dashboard_id}: {str(e)}')
            ns.abort(500, 'Failed to delete dashboard')


@ns.route('/<int:dashboard_id>/clone')
class DashboardClone(Resource):
    @ns.doc('clone_dashboard')
    @ns.marshal_with(dashboard_model, code=201)
    @login_required
    def post(self, dashboard_id):
        """Clone a dashboard."""
        try:
            original_dashboard = Dashboard.query.get_or_404(dashboard_id)
            
            # Check permissions
            if not original_dashboard.can_be_accessed_by(current_user):
                ns.abort(403, 'Access denied')
            
            data = request.get_json() or {}
            new_name = data.get('name', f"Copy of {original_dashboard.name}")
            
            # Create cloned dashboard
            cloned_dashboard = original_dashboard.clone(new_name, current_user.id)
            
            db.session.add(cloned_dashboard)
            db.session.commit()
            
            current_app.logger.info(f'Dashboard cloned: {new_name} by {current_user.username}')
            
            return cloned_dashboard.to_dict(), 201
            
        except Exception as e:
            current_app.logger.error(f'Error cloning dashboard {dashboard_id}: {str(e)}')
            ns.abort(500, 'Failed to clone dashboard')