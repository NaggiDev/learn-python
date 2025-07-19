"""
Tests for API endpoints.
"""
import pytest
import json
from app.models import Dataset, AnalysisJob, Dashboard


class TestDatasetAPI:
    """Test dataset API endpoints."""
    
    def test_list_datasets_authenticated(self, client, auth, sample_dataset):
        """Test listing datasets when authenticated."""
        auth.register()
        auth.login()
        
        response = client.get('/api/datasets')
        
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 1
        assert data[0]['name'] == 'Test Dataset'
    
    def test_list_datasets_unauthenticated(self, client):
        """Test listing datasets when not authenticated."""
        response = client.get('/api/datasets')
        
        # Should redirect to login or return 401
        assert response.status_code in [401, 302]
    
    def test_get_dataset_success(self, client, auth, sample_dataset):
        """Test getting a specific dataset."""
        auth.register()
        auth.login()
        
        response = client.get(f'/api/datasets/{sample_dataset.id}')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['name'] == 'Test Dataset'
        assert data['id'] == sample_dataset.id
    
    def test_get_dataset_not_found(self, client, auth):
        """Test getting a non-existent dataset."""
        auth.register()
        auth.login()
        
        response = client.get('/api/datasets/999')
        
        assert response.status_code == 404
    
    def test_delete_dataset_success(self, client, auth, sample_dataset):
        """Test deleting a dataset."""
        auth.register()
        auth.login()
        
        response = client.delete(f'/api/datasets/{sample_dataset.id}')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'deleted successfully' in data['message']


class TestAnalysisAPI:
    """Test analysis API endpoints."""
    
    def test_list_analysis_jobs(self, client, auth, sample_analysis_job):
        """Test listing analysis jobs."""
        auth.register()
        auth.login()
        
        response = client.get('/api/analysis/jobs')
        
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 1
        assert data[0]['job_type'] == 'descriptive_stats'
    
    def test_create_analysis_job(self, client, auth, sample_dataset):
        """Test creating a new analysis job."""
        auth.register()
        auth.login()
        
        job_data = {
            'dataset_id': sample_dataset.id,
            'job_type': 'correlation_analysis',
            'parameters': {'method': 'pearson'}
        }
        
        response = client.post('/api/analysis/jobs', 
                             data=json.dumps(job_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['job_type'] == 'correlation_analysis'
        assert data['status'] == 'pending'
    
    def test_create_analysis_job_invalid_type(self, client, auth, sample_dataset):
        """Test creating analysis job with invalid type."""
        auth.register()
        auth.login()
        
        job_data = {
            'dataset_id': sample_dataset.id,
            'job_type': 'invalid_type'
        }
        
        response = client.post('/api/analysis/jobs',
                             data=json.dumps(job_data),
                             content_type='application/json')
        
        assert response.status_code == 400
    
    def test_get_analysis_job(self, client, auth, sample_analysis_job):
        """Test getting a specific analysis job."""
        auth.register()
        auth.login()
        
        response = client.get(f'/api/analysis/jobs/{sample_analysis_job.id}')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['id'] == sample_analysis_job.id
        assert data['job_type'] == 'descriptive_stats'
    
    def test_cancel_analysis_job(self, client, auth, sample_analysis_job):
        """Test cancelling an analysis job."""
        auth.register()
        auth.login()
        
        response = client.delete(f'/api/analysis/jobs/{sample_analysis_job.id}')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'cancelled successfully' in data['message']


class TestVisualizationAPI:
    """Test visualization API endpoints."""
    
    def test_get_chart_types(self, client, auth):
        """Test getting available chart types."""
        auth.register()
        auth.login()
        
        response = client.get('/api/visualizations/types')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'chart_types' in data
        assert 'line' in data['chart_types']
        assert 'bar' in data['chart_types']
    
    def test_generate_chart(self, client, auth, sample_dataset):
        """Test generating a chart."""
        auth.register()
        auth.login()
        
        chart_data = {
            'dataset_id': sample_dataset.id,
            'chart_type': 'bar',
            'x_column': 'category',
            'y_column': 'value'
        }
        
        response = client.post('/api/visualizations/chart',
                             data=json.dumps(chart_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['chart_type'] == 'bar'
        assert 'chart_id' in data
    
    def test_generate_chart_invalid_type(self, client, auth, sample_dataset):
        """Test generating chart with invalid type."""
        auth.register()
        auth.login()
        
        chart_data = {
            'dataset_id': sample_dataset.id,
            'chart_type': 'invalid_type'
        }
        
        response = client.post('/api/visualizations/chart',
                             data=json.dumps(chart_data),
                             content_type='application/json')
        
        assert response.status_code == 400


class TestDashboardAPI:
    """Test dashboard API endpoints."""
    
    def test_list_dashboards(self, client, auth, sample_dashboard):
        """Test listing dashboards."""
        auth.register()
        auth.login()
        
        response = client.get('/api/dashboards')
        
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 1
        assert data[0]['name'] == 'Test Dashboard'
    
    def test_create_dashboard(self, client, auth):
        """Test creating a new dashboard."""
        auth.register()
        auth.login()
        
        dashboard_data = {
            'name': 'New Dashboard',
            'description': 'A new test dashboard',
            'layout_config': {'charts': []},
            'is_public': False
        }
        
        response = client.post('/api/dashboards',
                             data=json.dumps(dashboard_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['name'] == 'New Dashboard'
        assert data['is_public'] is False
    
    def test_get_dashboard(self, client, auth, sample_dashboard):
        """Test getting a specific dashboard."""
        auth.register()
        auth.login()
        
        response = client.get(f'/api/dashboards/{sample_dashboard.id}')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['name'] == 'Test Dashboard'
        assert data['id'] == sample_dashboard.id
    
    def test_update_dashboard(self, client, auth, sample_dashboard):
        """Test updating a dashboard."""
        auth.register()
        auth.login()
        
        update_data = {
            'name': 'Updated Dashboard',
            'description': 'Updated description'
        }
        
        response = client.put(f'/api/dashboards/{sample_dashboard.id}',
                            data=json.dumps(update_data),
                            content_type='application/json')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['name'] == 'Updated Dashboard'
    
    def test_delete_dashboard(self, client, auth, sample_dashboard):
        """Test deleting a dashboard."""
        auth.register()
        auth.login()
        
        response = client.delete(f'/api/dashboards/{sample_dashboard.id}')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'deleted successfully' in data['message']
    
    def test_clone_dashboard(self, client, auth, sample_dashboard):
        """Test cloning a dashboard."""
        auth.register()
        auth.login()
        
        clone_data = {
            'name': 'Cloned Dashboard'
        }
        
        response = client.post(f'/api/dashboards/{sample_dashboard.id}/clone',
                             data=json.dumps(clone_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['name'] == 'Cloned Dashboard'