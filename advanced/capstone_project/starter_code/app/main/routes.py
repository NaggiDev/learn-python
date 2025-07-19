"""
Main routes for serving the frontend application.
"""
from flask import render_template, send_from_directory, current_app
from app.main import bp


@bp.route('/')
def index():
    """Serve the main application page."""
    return render_template('index.html')


@bp.route('/dashboard')
def dashboard():
    """Serve the dashboard page."""
    return render_template('dashboard.html')


@bp.route('/datasets')
def datasets():
    """Serve the datasets management page."""
    return render_template('datasets.html')


@bp.route('/analysis')
def analysis():
    """Serve the analysis page."""
    return render_template('analysis.html')


@bp.route('/visualizations')
def visualizations():
    """Serve the visualizations page."""
    return render_template('visualizations.html')


@bp.route('/health')
def health_check():
    """Health check endpoint."""
    return {'status': 'healthy', 'message': 'Data Analytics Dashboard is running'}