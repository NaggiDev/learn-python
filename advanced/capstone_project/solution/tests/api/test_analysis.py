"""
Tests for analysis API endpoints.
"""
import pytest
import json
from app.models import AnalysisJob


class TestAnalysisAPI:
    """Test analysis API endpoints."""
    
    def test_run_descriptive_analysis_sync(self, client, auth_headers, sample_dataset):
        """Test running descriptive analysis synchronously."""
        response = client.post('/api/analysis/run',
                             json={
                                 'dataset_id': sample_dataset.id,
                                 'analysis_type': 'descriptive_statistics',
                                 'async': False
                             },
                             headers=auth_headers)
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'completed'
        assert 'result' in data
        assert data['result']['dataset_id'] == sample_dataset.id
    
    def test_run_analysis_async(self, client, auth_headers, sample_dataset):
        """Test running analysis asynchronously."""
        response = client.post('/api/analysis/run',
                             json={
                                 'dataset_id': sample_dataset.id,
                                 'analysis_type': 'descriptive_statistics',
                                 'async': True
                             },
                             headers=auth_headers)
        
        assert response.status_code == 202
        
        data = json.loads(response.data)
        assert 'job_id' in data
        assert 'task_id' in data
        assert data['status'] == 'started'
    
    def test_run_correlation_analysis(self, client, auth_headers, sample_dataset):
        """Test running correlation analysis."""
        response = client.post('/api/analysis/run',
                             json={
                                 'dataset_id': sample_dataset.id,
                                 'analysis_type': 'correlation_analysis',
                                 'async': False,
                                 'parameters': {
                                     'method': 'pearson'
                                 }
                             },
                             headers=auth_headers)
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'completed'
        assert 'correlation_matrix' in data['result']
    
    def test_run_analysis_invalid_dataset(self, client, auth_headers):
        """Test running analysis on non-existent dataset."""
        response = client.post('/api/analysis/run',
                             json={
                                 'dataset_id': 999,
                                 'analysis_type': 'descriptive_statistics',
                                 'async': False
                             },
                             headers=auth_headers)
        
        assert response.status_code == 404
    
    def test_run_analysis_invalid_type(self, client, auth_headers, sample_dataset):
        """Test running invalid analysis type."""
        response = client.post('/api/analysis/run',
                             json={
                                 'dataset_id': sample_dataset.id,
                                 'analysis_type': 'invalid_analysis',
                                 'async': False
                             },
                             headers=auth_headers)
        
        assert response.status_code == 400
    
    def test_list_analysis_jobs_empty(self, client, auth_headers):
        """Test listing analysis jobs when none exist."""
        response = client.get('/api/analysis/jobs', headers=auth_headers)
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'jobs' in data
        assert len(data['jobs']) == 0
    
    def test_descriptive_statistics_endpoint(self, client, auth_headers, sample_dataset):
        """Test direct descriptive statistics endpoint."""
        response = client.post('/api/analysis/descriptive',
                             json={'dataset_id': sample_dataset.id},
                             headers=auth_headers)
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['dataset_id'] == sample_dataset.id
        assert 'columns' in data
        assert 'total_rows' in data
    
    def test_correlation_analysis_endpoint(self, client, auth_headers, sample_dataset):
        """Test direct correlation analysis endpoint."""
        response = client.post('/api/analysis/correlation',
                             json={
                                 'dataset_id': sample_dataset.id,
                                 'method': 'pearson'
                             },
                             headers=auth_headers)
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['dataset_id'] == sample_dataset.id
        assert 'correlation_matrix' in data
        assert data['method'] == 'pearson'
    
    def test_analysis_missing_dataset_id(self, client, auth_headers):
        """Test analysis endpoints without dataset ID."""
        response = client.post('/api/analysis/descriptive',
                             json={},
                             headers=auth_headers)
        
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data