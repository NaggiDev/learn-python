"""
Pytest configuration and fixtures for the Data Analytics Dashboard tests.
"""
import os
import tempfile
import pytest
from app import create_app, db
from app.models import User, Dataset, AnalysisJob, Dashboard


@pytest.fixture
def app():
    """Create and configure a test Flask application."""
    # Create a temporary file for the test database
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app('testing')
    app.config['DATABASE_URL'] = f'sqlite:///{db_path}'
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
    
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create a test runner for the Flask application."""
    return app.test_cli_runner()


@pytest.fixture
def auth(client):
    """Authentication helper for tests."""
    class AuthActions:
        def __init__(self, client):
            self._client = client
        
        def register(self, username='testuser', email='test@example.com', password='testpass123'):
            """Register a new user."""
            return self._client.post('/auth/register', json={
                'username': username,
                'email': email,
                'password': password
            })
        
        def login(self, username='testuser', password='testpass123'):
            """Log in a user."""
            return self._client.post('/auth/login', json={
                'username': username,
                'password': password
            })
        
        def logout(self):
            """Log out the current user."""
            return self._client.post('/auth/logout')
    
    return AuthActions(client)


@pytest.fixture
def user(app):
    """Create a test user."""
    with app.app_context():
        user = User(username='testuser', email='test@example.com')
        user.set_password('testpass123')
        db.session.add(user)
        db.session.commit()
        return user


@pytest.fixture
def admin_user(app):
    """Create a test admin user."""
    with app.app_context():
        admin = User(username='admin', email='admin@example.com', role='admin')
        admin.set_password('adminpass123')
        db.session.add(admin)
        db.session.commit()
        return admin


@pytest.fixture
def sample_dataset(app, user):
    """Create a sample dataset for testing."""
    with app.app_context():
        dataset = Dataset(
            name='Test Dataset',
            filename='test.csv',
            file_path='/tmp/test.csv',
            file_size=1024,
            file_type='csv',
            user_id=user.id,
            description='A test dataset'
        )
        db.session.add(dataset)
        db.session.commit()
        return dataset


@pytest.fixture
def sample_analysis_job(app, user, sample_dataset):
    """Create a sample analysis job for testing."""
    with app.app_context():
        job = AnalysisJob(
            job_type='descriptive_stats',
            dataset_id=sample_dataset.id,
            user_id=user.id,
            parameters={'columns': ['col1', 'col2']}
        )
        db.session.add(job)
        db.session.commit()
        return job


@pytest.fixture
def sample_dashboard(app, user):
    """Create a sample dashboard for testing."""
    with app.app_context():
        dashboard = Dashboard(
            name='Test Dashboard',
            layout_config={'charts': []},
            user_id=user.id,
            description='A test dashboard'
        )
        db.session.add(dashboard)
        db.session.commit()
        return dashboard


@pytest.fixture
def temp_upload_file():
    """Create a temporary file for upload testing."""
    import tempfile
    import csv
    
    # Create a temporary CSV file
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    
    # Write sample CSV data
    writer = csv.writer(temp_file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', '25', 'New York'])
    writer.writerow(['Jane', '30', 'Los Angeles'])
    writer.writerow(['Bob', '35', 'Chicago'])
    
    temp_file.close()
    
    yield temp_file.name
    
    # Clean up
    os.unlink(temp_file.name)