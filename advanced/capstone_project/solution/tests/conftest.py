"""
Test configuration and fixtures.
"""
import os
import tempfile
import pytest
import pandas as pd
from app import create_app, db
from app.models import User, Dataset


@pytest.fixture
def app():
    """Create application for testing."""
    # Create temporary database file
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
    """Create test client."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create test CLI runner."""
    return app.test_cli_runner()


@pytest.fixture
def auth_headers(client):
    """Create authentication headers for API requests."""
    # Create test user
    user = User(
        username='testuser',
        email='test@example.com',
        password='testpass123',
        role='analyst'
    )
    db.session.add(user)
    db.session.commit()
    
    # Login user
    response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    
    assert response.status_code == 200
    
    # Return headers (Flask-Login uses session cookies)
    return {}


@pytest.fixture
def admin_headers(client):
    """Create admin authentication headers."""
    # Create admin user
    admin = User(
        username='admin',
        email='admin@example.com',
        password='adminpass123',
        role='admin'
    )
    db.session.add(admin)
    db.session.commit()
    
    # Login admin
    response = client.post('/api/auth/login', json={
        'username': 'admin',
        'password': 'adminpass123'
    })
    
    assert response.status_code == 200
    
    return {}


@pytest.fixture
def sample_user():
    """Create a sample user."""
    user = User(
        username='sampleuser',
        email='sample@example.com',
        password='samplepass123',
        role='analyst'
    )
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def sample_dataset(sample_user):
    """Create a sample dataset."""
    # Create temporary CSV file
    import tempfile
    import os
    
    # Create sample data
    data = {
        'id': range(1, 101),
        'name': [f'Item_{i}' for i in range(1, 101)],
        'value': [i * 10 for i in range(1, 101)],
        'category': ['A', 'B', 'C'] * 33 + ['A']
    }
    df = pd.DataFrame(data)
    
    # Save to temporary file
    fd, path = tempfile.mkstemp(suffix='.csv')
    df.to_csv(path, index=False)
    os.close(fd)
    
    # Create dataset record
    dataset = Dataset(
        name='Sample Dataset',
        filename='sample.csv',
        file_path=path,
        file_size=os.path.getsize(path),
        file_type='csv',
        user_id=sample_user.id,
        description='Sample dataset for testing'
    )
    
    # Process metadata
    from app.services.data_service import DataService
    DataService.process_dataset_metadata(dataset)
    
    db.session.add(dataset)
    db.session.commit()
    
    yield dataset
    
    # Cleanup
    if os.path.exists(path):
        os.unlink(path)


@pytest.fixture
def sample_csv_file():
    """Create a sample CSV file for upload testing."""
    import tempfile
    import io
    
    # Create sample data
    csv_content = """id,name,value,category
1,Item_1,10,A
2,Item_2,20,B
3,Item_3,30,C
4,Item_4,40,A
5,Item_5,50,B
"""
    
    # Create file-like object
    file_obj = io.BytesIO(csv_content.encode('utf-8'))
    file_obj.name = 'test_data.csv'
    
    return file_obj


class AuthActions:
    """Helper class for authentication actions in tests."""
    
    def __init__(self, client):
        self._client = client
    
    def login(self, username='testuser', password='testpass123'):
        """Login a user."""
        return self._client.post('/api/auth/login', json={
            'username': username,
            'password': password
        })
    
    def logout(self):
        """Logout current user."""
        return self._client.post('/api/auth/logout')
    
    def register(self, username='newuser', email='new@example.com', password='newpass123', role='analyst'):
        """Register a new user."""
        return self._client.post('/api/auth/register', json={
            'username': username,
            'email': email,
            'password': password,
            'role': role
        })


@pytest.fixture
def auth(client):
    """Authentication helper fixture."""
    return AuthActions(client)