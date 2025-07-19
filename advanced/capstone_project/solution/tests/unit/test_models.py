"""
Unit tests for database models.
"""
import pytest
from app import db
from app.models import User, Dataset, AnalysisJob, Dashboard


class TestUserModel:
    """Test cases for User model."""
    
    def test_user_creation(self):
        """Test user creation."""
        user = User(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            role='analyst'
        )
        
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'
        assert user.role == 'analyst'
        assert user.check_password('testpass123')
        assert not user.check_password('wrongpass')
    
    def test_password_hashing(self):
        """Test password hashing."""
        user = User(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Password should be hashed
        assert user.password_hash != 'testpass123'
        assert user.check_password('testpass123')
        
        # Change password
        user.set_password('newpass123')
        assert user.check_password('newpass123')
        assert not user.check_password('testpass123')
    
    def test_user_roles(self):
        """Test user role methods."""
        admin = User(username='admin', email='admin@test.com', password='pass', role='admin')
        analyst = User(username='analyst', email='analyst@test.com', password='pass', role='analyst')
        
        assert admin.is_admin()
        assert admin.has_role('admin')
        assert not analyst.is_admin()
        assert analyst.has_role('analyst')
    
    def test_user_permissions(self):
        """Test user permission methods."""
        user1 = User(username='user1', email='user1@test.com', password='pass')
        user2 = User(username='user2', email='user2@test.com', password='pass')
        admin = User(username='admin', email='admin@test.com', password='pass', role='admin')
        
        db.session.add_all([user1, user2, admin])
        db.session.commit()
        
        # Create dataset owned by user1
        dataset = Dataset(
            name='Test Dataset',
            filename='test.csv',
            file_path='/tmp/test.csv',
            file_size=1000,
            file_type='csv',
            user_id=user1.id
        )
        db.session.add(dataset)
        db.session.commit()
        
        # Test permissions
        assert user1.can_edit_dataset(dataset)
        assert user1.can_view_dataset(dataset)
        assert not user2.can_edit_dataset(dataset)
        assert not user2.can_view_dataset(dataset)
        assert admin.can_edit_dataset(dataset)
        assert admin.can_view_dataset(dataset)
    
    def test_user_to_dict(self):
        """Test user serialization."""
        user = User(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            role='analyst'
        )
        db.session.add(user)
        db.session.commit()
        
        user_dict = user.to_dict()
        
        assert user_dict['username'] == 'testuser'
        assert user_dict['email'] == 'test@example.com'
        assert user_dict['role'] == 'analyst'
        assert 'password_hash' not in user_dict
        assert 'dataset_count' in user_dict
        assert 'analysis_job_count' in user_dict


class TestDatasetModel:
    """Test cases for Dataset model."""
    
    def test_dataset_creation(self, sample_user):
        """Test dataset creation."""
        dataset = Dataset(
            name='Test Dataset',
            filename='test.csv',
            file_path='/tmp/test.csv',
            file_size=1000,
            file_type='csv',
            user_id=sample_user.id,
            description='Test dataset'
        )
        
        assert dataset.name == 'Test Dataset'
        assert dataset.filename == 'test.csv'
        assert dataset.file_type == 'csv'
        assert dataset.user_id == sample_user.id
    
    def test_file_size_formatting(self, sample_user):
        """Test file size formatting."""
        dataset = Dataset(
            name='Test Dataset',
            filename='test.csv',
            file_path='/tmp/test.csv',
            file_size=1024,
            file_type='csv',
            user_id=sample_user.id
        )
        
        assert dataset.get_file_size_formatted() == '1.0 KB'
        
        dataset.file_size = 1024 * 1024
        assert dataset.get_file_size_formatted() == '1.0 MB'
    
    def test_dataset_metadata(self, sample_user):
        """Test dataset metadata methods."""
        dataset = Dataset(
            name='Test Dataset',
            filename='test.csv',
            file_path='/tmp/test.csv',
            file_size=1000,
            file_type='csv',
            user_id=sample_user.id
        )
        db.session.add(dataset)
        db.session.commit()
        
        # Update metadata
        dataset.update_metadata(100, 5, '{"columns": []}')
        
        assert dataset.row_count == 100
        assert dataset.column_count == 5
        assert dataset.is_processed
        
        # Mark processing error
        dataset.mark_processing_error('Test error')
        
        assert dataset.processing_error == 'Test error'
        assert not dataset.is_processed
    
    def test_dataset_to_dict(self, sample_user):
        """Test dataset serialization."""
        dataset = Dataset(
            name='Test Dataset',
            filename='test.csv',
            file_path='/tmp/test.csv',
            file_size=1000,
            file_type='csv',
            user_id=sample_user.id,
            description='Test dataset'
        )
        db.session.add(dataset)
        db.session.commit()
        
        dataset_dict = dataset.to_dict()
        
        assert dataset_dict['name'] == 'Test Dataset'
        assert dataset_dict['filename'] == 'test.csv'
        assert dataset_dict['file_type'] == 'csv'
        assert dataset_dict['description'] == 'Test dataset'
        assert 'file_size_formatted' in dataset_dict


class TestAnalysisJobModel:
    """Test cases for AnalysisJob model."""
    
    def test_analysis_job_creation(self, sample_user, sample_dataset):
        """Test analysis job creation."""
        job = AnalysisJob(
            dataset_id=sample_dataset.id,
            job_type='descriptive_statistics',
            user_id=sample_user.id,
            parameters={'columns': ['value']},
            priority=1
        )
        
        assert job.dataset_id == sample_dataset.id
        assert job.job_type == 'descriptive_statistics'
        assert job.user_id == sample_user.id
        assert job.status == 'pending'
        assert job.priority == 1
    
    def test_job_parameters(self, sample_user, sample_dataset):
        """Test job parameter handling."""
        job = AnalysisJob(
            dataset_id=sample_dataset.id,
            job_type='correlation_analysis',
            user_id=sample_user.id,
            parameters={'method': 'pearson', 'columns': ['value']}
        )
        
        params = job.get_parameters()
        assert params['method'] == 'pearson'
        assert params['columns'] == ['value']
        
        # Update parameters
        job.set_parameters({'method': 'spearman'})
        params = job.get_parameters()
        assert params['method'] == 'spearman'
    
    def test_job_lifecycle(self, sample_user, sample_dataset):
        """Test job lifecycle methods."""
        job = AnalysisJob(
            dataset_id=sample_dataset.id,
            job_type='descriptive_statistics',
            user_id=sample_user.id
        )
        db.session.add(job)
        db.session.commit()
        
        # Start job
        job.start_job('task_123')
        assert job.status == 'running'
        assert job.celery_task_id == 'task_123'
        assert job.started_at is not None
        
        # Complete job
        results = {'mean': 50.5, 'std': 28.87}
        job.complete_job(results)
        assert job.status == 'completed'
        assert job.completed_at is not None
        assert job.get_results() == results
        
        # Test duration
        duration = job.get_duration()
        assert duration is not None
        assert duration >= 0
    
    def test_job_failure_and_retry(self, sample_user, sample_dataset):
        """Test job failure and retry logic."""
        job = AnalysisJob(
            dataset_id=sample_dataset.id,
            job_type='descriptive_statistics',
            user_id=sample_user.id,
            max_retries=2
        )
        db.session.add(job)
        db.session.commit()
        
        # Fail job
        job.fail_job('Test error')
        assert job.status == 'failed'
        assert job.error_message == 'Test error'
        assert job.can_retry()
        
        # Retry job
        assert job.retry_job()
        assert job.status == 'pending'
        assert job.retry_count == 1
        assert job.error_message is None
        
        # Fail again
        job.fail_job('Another error')
        assert job.retry_job()
        assert job.retry_count == 2
        
        # Fail third time - no more retries
        job.fail_job('Final error')
        assert not job.can_retry()
        assert not job.retry_job()


class TestDashboardModel:
    """Test cases for Dashboard model."""
    
    def test_dashboard_creation(self, sample_user):
        """Test dashboard creation."""
        dashboard = Dashboard(
            name='Test Dashboard',
            user_id=sample_user.id,
            description='Test dashboard'
        )
        
        assert dashboard.name == 'Test Dashboard'
        assert dashboard.user_id == sample_user.id
        assert dashboard.description == 'Test dashboard'
        assert not dashboard.is_public
        assert not dashboard.auto_refresh
    
    def test_dashboard_layout_config(self, sample_user):
        """Test dashboard layout configuration."""
        layout_config = {
            'charts': [
                {'id': 'chart1', 'type': 'bar', 'dataset_id': 1},
                {'id': 'chart2', 'type': 'line', 'dataset_id': 2}
            ]
        }
        
        dashboard = Dashboard(
            name='Test Dashboard',
            user_id=sample_user.id,
            layout_config=layout_config
        )
        
        assert dashboard.get_layout_config() == layout_config
        assert dashboard.chart_count == 2
    
    def test_dashboard_chart_management(self, sample_user):
        """Test dashboard chart management."""
        dashboard = Dashboard(
            name='Test Dashboard',
            user_id=sample_user.id
        )
        db.session.add(dashboard)
        db.session.commit()
        
        # Add chart
        chart_config = {'type': 'bar', 'dataset_id': 1, 'column': 'value'}
        dashboard.add_chart(chart_config)
        
        charts = dashboard.get_charts()
        assert len(charts) == 1
        assert charts[0]['type'] == 'bar'
        assert 'id' in charts[0]
        
        # Update chart
        chart_id = charts[0]['id']
        new_config = {'type': 'line', 'dataset_id': 1, 'column': 'value'}
        assert dashboard.update_chart(chart_id, new_config)
        
        updated_charts = dashboard.get_charts()
        assert updated_charts[0]['type'] == 'line'
        
        # Remove chart
        assert dashboard.remove_chart(chart_id)
        assert len(dashboard.get_charts()) == 0
    
    def test_dashboard_permissions(self, sample_user):
        """Test dashboard access permissions."""
        user2 = User(username='user2', email='user2@test.com', password='pass')
        admin = User(username='admin', email='admin@test.com', password='pass', role='admin')
        db.session.add_all([user2, admin])
        db.session.commit()
        
        # Private dashboard
        private_dashboard = Dashboard(
            name='Private Dashboard',
            user_id=sample_user.id,
            is_public=False
        )
        
        assert private_dashboard.is_accessible_by(sample_user)
        assert not private_dashboard.is_accessible_by(user2)
        assert private_dashboard.is_accessible_by(admin)
        
        # Public dashboard
        public_dashboard = Dashboard(
            name='Public Dashboard',
            user_id=sample_user.id,
            is_public=True
        )
        
        assert public_dashboard.is_accessible_by(sample_user)
        assert public_dashboard.is_accessible_by(user2)
        assert public_dashboard.is_accessible_by(admin)