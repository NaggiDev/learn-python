"""
API blueprint for RESTful endpoints.
"""
from flask import Blueprint
from flask_restx import Api

bp = Blueprint('api', __name__)

# Initialize Flask-RESTX API
api = Api(
    bp,
    title='Data Analytics Dashboard API',
    version='1.0',
    description='RESTful API for the Data Analytics Dashboard',
    doc='/docs/',
    prefix='/api'
)

# Import and register namespaces
from app.api.datasets import ns as datasets_ns
from app.api.analysis import ns as analysis_ns
from app.api.visualizations import ns as visualizations_ns
from app.api.dashboards import ns as dashboards_ns

api.add_namespace(datasets_ns, path='/datasets')
api.add_namespace(analysis_ns, path='/analysis')
api.add_namespace(visualizations_ns, path='/visualizations')
api.add_namespace(dashboards_ns, path='/dashboards')