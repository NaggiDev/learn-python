"""
Dashboard API endpoints.
"""
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from flask_restx import Api, Resource, fields, Namespace
from app import db
from app.models.dashboard import Dashboard

# Create blueprint
dashboards_bp = Blueprint('dashboards', __name__, url_prefix='/api/dashboards')
dashboards_ns = Namespace('dashboards', description='Dashboard management operations')

# Flask-RESTX models
dashboard_model = dashboards_ns.model('Dashboard', {
    'id': fields.Integer(description='Dashboard ID'),
    'name': fields.String(required=True, description='Dashboard name'),
    'description': fields.String(description='Dashboard description'),
    'layout_config': fields.Raw(description='Dashboard layout configuration'),
    'created_at': fields.String(description='Creation timestamp'),
    'updated_at': fields.String(description='Last update timestamp')
})

dashboard_create_model = dashboards_ns.model('DashboardCreate', {
    'name': fields.String(required=True, description='Dashboard name'),
    'description': fields.String(description='Dashboard description'),
    'layout_config': fields.Raw(description='Dashboard layout configuration')
})


@dashboards_ns.route('')
class DashboardList(Resource):
    """Dashboard list endpoint."""
    
    @dashboards_ns.marshal_list_with(dashboard_model)
    @dashboards_ns.doc('list_dashboards')
    @login_required
    def get(self):
        """Get list of user's dashboards."""
        page = request.args.get('page', 1, type=int)
        per_page = min(request.args.get('per_page', 10, type=int), 100)
        
        # Get user's dashboards
        query = Dashboard.query.filter_by(user_id=current_user.id)
        
        # Apply search filter
        if request.args.get('search'):
            search_term = f"%{request.args.get('search')}%"
            query = query.filter(Dashboard.name.like(search_term))
        
        # Order by update date (newest first)
        query = query.order_by(Dashboard.updated_at.desc())
        
        # Paginate
        dashboards = query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        
        return {
            'dashboards': [dashboard.to_dict() for dashboard in dashboards.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': dashboards.total,
                'pages': dashboards.pages,
                'has_next': dashboards.has_next,
                'has_prev': dashboards.has_prev
            }
        }
    
    @dashboards_ns.expect(dashboard_create_model)
    @dashboards_ns.marshal_with(dashboard_model, code=201)
    @dashboards_ns.doc('create_dashboard')
    @login_required
    def post(self):
        """Create a new dashboard."""
        data = request.json
        
        if not data or not data.get('name'):
            return {'error': 'Dashboard name is required'}, 400
        
        try:
            dashboard = Dashboard(
                name=data['name'].strip(),
                description=data.get('description', ''),
                layout_config=data.get('layout_config', {}),
                user_id=current_user.id
            )
            
            db.session.add(dashboard)
            db.session.commit()
            
            current_app.logger.info(f'Dashboard created: {dashboard.name} (ID: {dashboard.id})')
            
            return dashboard.to_dict(), 201
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f'Dashboard creation failed: {str(e)}')
            return {'error': 'Dashboard creation failed'}, 500


@dashboards_ns.route('/<int:dashboard_id>')
class DashboardDetail(Resource):
    """Dashboard detail endpoint."""
    
    @dashboards_ns.marshal_with(dashboard_model)
    @dashboards_ns.doc('get_dashboard')
    @login_required
    def get(self, dashboard_id):
        """Get dashboard details."""
        dashboard = Dashboard.query.get_or_404(dashboard_id)
        
        # Check permissions
        if not current_user.can_view_dashboard(dashboard):
            return {'error': 'Access denied'}, 403
        
        return dashboard.to_dict(), 200
    
    @dashboards_ns.expect(dashboard_create_model)
    @dashboards_ns.marshal_with(dashboard_model)
    @dashboards_ns.doc('update_dashboard')
    @login_required
    def put(self, dashboard_id):
        """Update dashboard."""
        dashboard = Dashboard.query.get_or_404(dashboard_id)
        
        # Check permissions
        if not current_user.can_edit_dashboard(dashboard):
            return {'error': 'Access denied'}, 403
        
        data = request.json or {}
        
        try:
            if 'name' in data:
                dashboard.name = data['name'].strip()
                if not dashboard.name:
                    return {'error': 'Name cannot be empty'}, 400
            
            if 'description' in data:
                dashboard.description = data['description']
            
            if 'layout_config' in data:
                dashboard.layout_config = data['layout_config']
            
            dashboard.update_timestamp()
            db.session.commit()
            
            current_app.logger.info(f'Dashboard updated: {dashboard.name} (ID: {dashboard.id})')
            
            return dashboard.to_dict(), 200
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f'Dashboard update failed: {str(e)}')
            return {'error': 'Update failed'}, 500
    
    @dashboards_ns.doc('delete_dashboard')
    @login_required
    def delete(self, dashboard_id):
        """Delete dashboard."""
        dashboard = Dashboard.query.get_or_404(dashboard_id)
        
        # Check permissions
        if not current_user.can_edit_dashboard(dashboard):
            return {'error': 'Access denied'}, 403
        
        try:
            db.session.delete(dashboard)
            db.session.commit()
            
            current_app.logger.info(f'Dashboard deleted: {dashboard.name} (ID: {dashboard.id})')
            
            return {'message': 'Dashboard deleted successfully'}, 200
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f'Dashboard deletion failed: {str(e)}')
            return {'error': 'Deletion failed'}, 500


@dashboards_ns.route('/<int:dashboard_id>/clone')
class CloneDashboard(Resource):
    """Clone dashboard endpoint."""
    
    @dashboards_ns.marshal_with(dashboard_model, code=201)
    @dashboards_ns.doc('clone_dashboard')
    @login_required
    def post(self, dashboard_id):
        """Clone an existing dashboard."""
        original_dashboard = Dashboard.query.get_or_404(dashboard_id)
        
        # Check permissions
        if not current_user.can_view_dashboard(original_dashboard):
            return {'error': 'Access denied'}, 403
        
        try:
            # Create cloned dashboard
            cloned_dashboard = Dashboard(
                name=f"{original_dashboard.name} (Copy)",
                description=original_dashboard.description,
                layout_config=original_dashboard.layout_config,
                user_id=current_user.id
            )
            
            db.session.add(cloned_dashboard)
            db.session.commit()
            
            current_app.logger.info(f'Dashboard cloned: {cloned_dashboard.name} (ID: {cloned_dashboard.id})')
            
            return cloned_dashboard.to_dict(), 201
            
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f'Dashboard cloning failed: {str(e)}')
            return {'error': 'Cloning failed'}, 500


# Register namespace with blueprint
dashboards_bp.add_url_rule('', view_func=DashboardList.as_view('dashboard_list'))
dashboards_bp.add_url_rule('/<int:dashboard_id>', view_func=DashboardDetail.as_view('dashboard_detail'))
dashboards_bp.add_url_rule('/<int:dashboard_id>/clone', view_func=CloneDashboard.as_view('clone_dashboard'))