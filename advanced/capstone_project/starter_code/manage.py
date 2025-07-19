#!/usr/bin/env python
"""
Management script for the Data Analytics Dashboard application.
"""
import os
import click
from flask.cli import with_appcontext
from app import create_app, db
from app.models import User, Dataset, AnalysisJob, Dashboard


def create_application():
    """Create Flask application instance."""
    config_name = os.environ.get('FLASK_ENV', 'development')
    return create_app(config_name)


app = create_application()


@app.cli.command()
@with_appcontext
def init_db():
    """Initialize the database."""
    click.echo('Initializing database...')
    db.create_all()
    click.echo('Database initialized successfully!')


@app.cli.command()
@with_appcontext
def drop_db():
    """Drop all database tables."""
    if click.confirm('Are you sure you want to drop all database tables?'):
        db.drop_all()
        click.echo('Database tables dropped!')


@app.cli.command()
@with_appcontext
def reset_db():
    """Reset the database (drop and recreate)."""
    if click.confirm('Are you sure you want to reset the database?'):
        db.drop_all()
        db.create_all()
        click.echo('Database reset successfully!')


@app.cli.command()
@with_appcontext
def create_admin():
    """Create an admin user."""
    username = click.prompt('Admin username')
    email = click.prompt('Admin email')
    password = click.prompt('Admin password', hide_input=True, confirmation_prompt=True)
    
    # Check if user already exists
    if User.query.filter_by(username=username).first():
        click.echo(f'User {username} already exists!')
        return
    
    if User.query.filter_by(email=email).first():
        click.echo(f'User with email {email} already exists!')
        return
    
    # Create admin user
    admin = User(
        username=username,
        email=email,
        role='admin'
    )
    admin.set_password(password)
    
    db.session.add(admin)
    db.session.commit()
    
    click.echo(f'Admin user {username} created successfully!')


@app.cli.command()
@click.option('--host', default='127.0.0.1', help='Host to bind to')
@click.option('--port', default=5000, help='Port to bind to')
@click.option('--debug', is_flag=True, help='Enable debug mode')
def run(host, port, debug):
    """Run the development server."""
    app.run(host=host, port=port, debug=debug)


@app.cli.command()
def test():
    """Run the test suite."""
    import pytest
    pytest.main(['-v', 'tests/'])


@app.cli.command()
def test_coverage():
    """Run tests with coverage report."""
    import pytest
    pytest.main(['-v', '--cov=app', '--cov-report=html', 'tests/'])


if __name__ == '__main__':
    app.run(debug=True)