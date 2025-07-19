"""
Tests for database models.
"""
import pytest
from app import db
from app.models import User, Dataset, AnalysisJob, Dashboard


class TestUserModel:
    """Test User model functionality."""
    
    def test_user_creation(self, app):
        """Test creating a new user."""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            
            db.session.add(user)
            db.session.commit()
            
            assert user.id is not None
            assert user.username == 'testuser'
            assert user.email == 'test@example.com'
            assert user.role == 'analyst'  # default role
            assert user.is_active is True
    
    def test_password_hashing(self, app):
        """Test password hashing and verification."""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            
            # Password should be hashed
            assert user.password_hash != 'password123'
            
            # Should be able to verify correct password
            assert user.check_password('password123') is True
            
            # Should not verify incorrect password
            assert user.check_password('wrongpassword') is False
    
    def test_user_roles(self, app):
        """Test user role functionality."""
        with app.app_context():
            # Regular user
            user = User(username='user', email='user@example.com')
            assert user.is_admin() is False
            
            # Admin user
            admin = User(username='admin', email='admin@example.com', role='admin')
            assert admin.is_admin() is True
    
    def test_user_to_dict(self, app):
        """Test user dictionary representation."""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            db.session.add(user)
            db.session.commit()
            
            user_dict = user.to_dict()
            
            assert user_dict['username'] == 'testuser'
            assert user_dict['email'] == 'test@example.com'
            assert user_dict['role'] == 'analyst'
            assert 'password_hash' not in user_dict  # Should not expose password


class TestDatasetModel:
    """Test Dataset model functionality."""
    
    def test_dataset_creation(self, app, user):
        """Test creating a new dataset."""
        with app.app_context():
            dataset = Dataset(
                name='Test Dataset',
                filename='test.csv',
                file_path='/tmp/test.csv',
                file_size=1024,
                file_type='csv',
                user_id=user.id
            )
            
            db.session.add(dataset)
            db.session.commit()
            
            assert dataset.id is not None
            assert dataset.name == 'Test Dataset'
            assert dataset.filename == 'test.csv'
            assert dataset.file_size == 1024
            assert dataset.user_id == user.id
    
    def test_file_size_formatting(self, app, user):
        """Test file size formatting."""
        with app.app_context():
            dataset = Dataset(
                name='Test Dataset',
                filename='test.csv',
                file_path='/tmp/test.csv',
                file_size=1024,
                file_type='csv',
                user_id=user.id
            )
            
            assert dataset.get_file_size_formatted() == '1.0 KB'
    
    def test_dataset_to_dict(self, app, user):
        """Test dataset dictionary representation."""
        with app.app_context():
            dataset = Dataset(
                name='Test Dataset',
                filename='test.csv',
                file_path='/tmp/test.csv',
                file_size=1024,
                file_type='csv',
                user_id=user.id
            )
            db.session.add(dataset)
            db.session.commit()
            
            dataset_dict = dataset.to_dict()
            
            assert dataset_dict['name'] == 'Test Dataset'
            assert dataset_dict['filename'] == 'test.csv'
            assert dataset_dict['file_size'] == 1024
            assert dataset_dict['file_size_formatted'] == '1.0 KB'
            assert dataset_dict['user_id'] == user.id


class TestAnalysisJobModel:
    """Test AnalysisJob model functionality."""
    
    def test_analysis_job_creation(self, app, user, sample_dataset):
        """Test creating a new analysis job."""
        with app.app_context():
            job = AnalysisJob(
                job_type='descriptive_stats',
                dataset_id=sample_dataset.id,
                user_id=user.id,
                parameters={'columns': ['col1', 'col2']}
            )
            
            db.session.add(job)
            db.session.commit()
            
            assert job.id is not None
            assert job.job_type == 'descriptive_stats'
            assert job.status == 'pending'  # default status
            assert job.dataset_id == sample_dataset.id
            assert job.user_id == user.id
    
    def test_invalid_job_type(self, app, user, sample_dataset):
        """Test creating job with invalid type."""
        with app.app_context():
            with pytest.raises(ValueError):
                AnalysisJob(
                    job_type='invalid_type',
                    dataset_id=sample_dataset.id,
                    user_id=user.id
                )
    
    def test_job_parameters(self, app, user, sample_dataset):
        """Test job parameter handling."""
        with app.app_context():
            params = {'columns': ['col1', 'col2'], 'method': 'pearson'}
            job = AnalysisJob(
                job_type='correlation_analysis',
                dataset_id=sample_dataset.id,
                user_id=user.id,
                parameters=params
            )
            
            db.session.add(job)
            db.session.commit()
            
            retrieved_params = job.get_parameters()
            assert retrieved_params == params
    
    def test_job_lifecycle(self, app, user, sample_dataset):
        """Test job status transitions."""
        with app.app_context():
            job = AnalysisJob(
                job_type='descriptive_stats',
                dataset_id=sample_dataset.id,
                user_id=user.id
            )
            
            db.session.add(job)
            db.session.commit()
            
            # Start job
            job.start_job()
            assert job.status == 'running'
            assert job.started_at is not None
            
            # Complete job
            results = {'mean': 10.5, 'std': 2.3}
            job.complete_job(results)
            assert job.status == 'completed'
            assert job.completed_at is not None
            assert job.get_results() == results
            assert job.is_finished() is True


class TestDashboardModel:
    """Test Dashboard model functionality."""
    
    def test_dashboard_creation(self, app, user):
        """Test creating a new dashboard."""
        with app.app_context():
            config = {'charts': [{'type': 'bar', 'data': {}}]}
            dashboard = Dashboard(
                name='Test Dashboard',
                layout_config=config,
                user_id=user.id,
                description='A test dashboard'
            )
            
            db.session.add(dashboard)
            db.session.commit()
            
            assert dashboard.id is not None
            assert dashboard.name == 'Test Dashboard'
            assert dashboard.user_id == user.id
            assert dashboard.is_public is False  # default
    
    def test_dashboard_config_handling(self, app, user):
        """Test dashboard configuration handling."""
        with app.app_context():
            config = {'charts': [{'type': 'bar'}, {'type': 'line'}]}
            dashboard = Dashboard(
                name='Test Dashboard',
                layout_config=config,
                user_id=user.id
            )
            
            db.session.add(dashboard)
            db.session.commit()
            
            retrieved_config = dashboard.get_layout_config()
            assert retrieved_config == config
            assert dashboard.get_chart_count() == 2
    
    def test_dashboard_permissions(self, app, user, admin_user):
        """Test dashboard access permissions."""
        with app.app_context():
            # Private dashboard
            private_dashboard = Dashboard(
                name='Private Dashboard',
                layout_config={'charts': []},
                user_id=user.id,
                is_public=False
            )
            
            # Public dashboard
            public_dashboard = Dashboard(
                name='Public Dashboard',
                layout_config={'charts': []},
                user_id=user.id,
                is_public=True
            )
            
            db.session.add_all([private_dashboard, public_dashboard])
            db.session.commit()
            
            # Owner can access both
            assert private_dashboard.can_be_accessed_by(user) is True
            assert public_dashboard.can_be_accessed_by(user) is True
            
            # Admin can access both
            assert private_dashboard.can_be_accessed_by(admin_user) is True
            assert public_dashboard.can_be_accessed_by(admin_user) is True
            
            # Other user can only access public
            other_user = User(username='other', email='other@example.com')
            db.session.add(other_user)
            db.session.commit()
            
            assert private_dashboard.can_be_accessed_by(other_user) is False
            assert public_dashboard.can_be_accessed_by(other_user) is True
    
    def test_dashboard_cloning(self, app, user):
        """Test dashboard cloning functionality."""
        with app.app_context():
            original = Dashboard(
                name='Original Dashboard',
                layout_config={'charts': [{'type': 'bar'}]},
                user_id=user.id,
                description='Original description'
            )
            
            db.session.add(original)
            db.session.commit()
            
            # Create another user
            other_user = User(username='other', email='other@example.com')
            db.session.add(other_user)
            db.session.commit()
            
            # Clone dashboard
            cloned = original.clone('Cloned Dashboard', other_user.id)
            
            assert cloned.name == 'Cloned Dashboard'
            assert cloned.user_id == other_user.id
            assert cloned.get_layout_config() == original.get_layout_config()
            assert cloned.is_public is False  # Clones are private by default