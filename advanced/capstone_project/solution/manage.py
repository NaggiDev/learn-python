"""
Management script for the Data Analytics Dashboard application.
"""
import os
import click
from flask.cli import with_appcontext
from app import create_app, db
from app.models import User, Dataset, AnalysisJob, Dashboard


def create_cli_app():
    """Create Flask app for CLI commands."""
    return create_app(os.environ.get('FLASK_ENV', 'development'))


@click.group()
def cli():
    """Data Analytics Dashboard management commands."""
    pass


@cli.command()
@click.option('--drop', is_flag=True, help='Drop existing tables first')
@with_appcontext
def init_db(drop):
    """Initialize the database."""
    if drop:
        click.echo('Dropping existing tables...')
        db.drop_all()
    
    click.echo('Creating database tables...')
    db.create_all()
    click.echo('Database initialized successfully!')


@cli.command()
@click.option('--username', prompt=True, help='Admin username')
@click.option('--email', prompt=True, help='Admin email')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Admin password')
@with_appcontext
def create_admin(username, email, password):
    """Create an admin user."""
    # Check if user already exists
    if User.query.filter_by(username=username).first():
        click.echo(f'User {username} already exists!')
        return
    
    if User.query.filter_by(email=email).first():
        click.echo(f'Email {email} already registered!')
        return
    
    # Create admin user
    admin = User(
        username=username,
        email=email,
        password=password,
        role='admin'
    )
    
    db.session.add(admin)
    db.session.commit()
    
    click.echo(f'Admin user {username} created successfully!')


@cli.command()
@with_appcontext
def create_sample_data():
    """Create sample data for testing."""
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    
    click.echo('Creating sample data...')
    
    # Create sample user if not exists
    user = User.query.filter_by(username='demo').first()
    if not user:
        user = User(
            username='demo',
            email='demo@example.com',
            password='demo123',
            role='analyst'
        )
        db.session.add(user)
        db.session.commit()
    
    # Create sample CSV data
    np.random.seed(42)
    sample_data = {
        'id': range(1, 1001),
        'name': [f'Item_{i}' for i in range(1, 1001)],
        'category': np.random.choice(['A', 'B', 'C', 'D'], 1000),
        'value': np.random.normal(100, 20, 1000),
        'price': np.random.uniform(10, 500, 1000),
        'date': [datetime.now() - timedelta(days=np.random.randint(0, 365)) for _ in range(1000)],
        'is_active': np.random.choice([True, False], 1000, p=[0.8, 0.2])
    }
    
    df = pd.DataFrame(sample_data)
    
    # Save to CSV
    upload_dir = 'uploads'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    csv_path = os.path.join(upload_dir, 'sample_data.csv')
    df.to_csv(csv_path, index=False)
    
    # Create dataset record
    dataset = Dataset(
        name='Sample Dataset',
        filename='sample_data.csv',
        file_path=csv_path,
        file_size=os.path.getsize(csv_path),
        file_type='csv',
        user_id=user.id,
        description='Sample dataset for testing and demonstration'
    )
    
    # Process metadata
    from app.services.data_service import DataService
    DataService.process_dataset_metadata(dataset)
    
    db.session.add(dataset)
    db.session.commit()
    
    click.echo('Sample data created successfully!')
    click.echo(f'Dataset ID: {dataset.id}')
    click.echo(f'User: {user.username} (password: demo123)')


@cli.command()
@with_appcontext
def list_users():
    """List all users."""
    users = User.query.all()
    
    if not users:
        click.echo('No users found.')
        return
    
    click.echo('Users:')
    click.echo('-' * 60)
    for user in users:
        click.echo(f'ID: {user.id:3d} | Username: {user.username:15s} | Email: {user.email:25s} | Role: {user.role}')


@cli.command()
@with_appcontext
def list_datasets():
    """List all datasets."""
    datasets = Dataset.query.all()
    
    if not datasets:
        click.echo('No datasets found.')
        return
    
    click.echo('Datasets:')
    click.echo('-' * 80)
    for dataset in datasets:
        click.echo(f'ID: {dataset.id:3d} | Name: {dataset.name:20s} | Type: {dataset.file_type:5s} | Size: {dataset.get_file_size_formatted():8s} | Owner: {dataset.owner.username}')


@cli.command()
@click.option('--host', default='127.0.0.1', help='Host to bind to')
@click.option('--port', default=5000, help='Port to bind to')
@click.option('--debug', is_flag=True, help='Enable debug mode')
@with_appcontext
def run(host, port, debug):
    """Run the development server."""
    from flask import current_app
    current_app.run(host=host, port=port, debug=debug)


@cli.command()
@with_appcontext
def test():
    """Run the test suite."""
    import pytest
    import sys
    
    # Run pytest with coverage
    exit_code = pytest.main([
        'tests/',
        '--cov=app',
        '--cov-report=term-missing',
        '--cov-report=html:htmlcov',
        '-v'
    ])
    
    sys.exit(exit_code)


@cli.command()
@with_appcontext
def clean_uploads():
    """Clean up orphaned upload files."""
    upload_dir = 'uploads'
    if not os.path.exists(upload_dir):
        click.echo('Upload directory does not exist.')
        return
    
    # Get all files in upload directory
    upload_files = set(os.listdir(upload_dir))
    
    # Get all dataset file paths
    datasets = Dataset.query.all()
    dataset_files = set()
    
    for dataset in datasets:
        if dataset.file_exists():
            filename = os.path.basename(dataset.file_path)
            dataset_files.add(filename)
        else:
            # Dataset file is missing, mark as error
            dataset.mark_processing_error('File not found on disk')
            click.echo(f'Marked dataset {dataset.id} as having missing file')
    
    # Find orphaned files
    orphaned_files = upload_files - dataset_files
    
    if not orphaned_files:
        click.echo('No orphaned files found.')
        return
    
    click.echo(f'Found {len(orphaned_files)} orphaned files:')
    for filename in orphaned_files:
        click.echo(f'  - {filename}')
    
    if click.confirm('Delete orphaned files?'):
        deleted_count = 0
        for filename in orphaned_files:
            file_path = os.path.join(upload_dir, filename)
            try:
                os.remove(file_path)
                deleted_count += 1
                click.echo(f'Deleted: {filename}')
            except OSError as e:
                click.echo(f'Failed to delete {filename}: {e}')
        
        click.echo(f'Deleted {deleted_count} orphaned files.')
    
    db.session.commit()


@cli.command()
@with_appcontext
def db_stats():
    """Show database statistics."""
    stats = {
        'Users': User.query.count(),
        'Datasets': Dataset.query.count(),
        'Analysis Jobs': AnalysisJob.query.count(),
        'Dashboards': Dashboard.query.count()
    }
    
    click.echo('Database Statistics:')
    click.echo('-' * 30)
    for table, count in stats.items():
        click.echo(f'{table:15s}: {count:6d}')
    
    # Analysis job status breakdown
    job_stats = db.session.query(
        AnalysisJob.status,
        db.func.count(AnalysisJob.id)
    ).group_by(AnalysisJob.status).all()
    
    if job_stats:
        click.echo('\nAnalysis Job Status:')
        click.echo('-' * 30)
        for status, count in job_stats:
            click.echo(f'{status:15s}: {count:6d}')


if __name__ == '__main__':
    app = create_cli_app()
    with app.app_context():
        cli()