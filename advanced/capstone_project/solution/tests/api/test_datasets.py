"""
Tests for dataset API endpoints.
"""
import pytest
import json
from app.models import Dataset


class TestDatasetAPI:
    """Test dataset API endpoints."""
    
    def test_list_datasets_empty(self, client, auth_headers):
        """Test listing datasets when none exist."""
        response = client.get('/api/datasets', headers=auth_headers)
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'datasets' in data
        assert len(data['datasets']) == 0
    
    def test_list_datasets_with_data(self, client, auth_headers, sample_dataset):
        """Test listing datasets with existing data."""
        response = client.get('/api/datasets', headers=auth_headers)
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert len(data['datasets']) == 1
        assert data['datasets'][0]['name'] == 'Sample Dataset'
    
    def test_upload_dataset_success(self, client, auth_headers, sample_csv_file):
        """Test successful dataset upload."""
        response = client.post('/api/datasets', 
                             data={
                                 'file': (sample_csv_file, 'test.csv'),
                                 'name': 'Test Dataset',
                                 'description': 'Test description'
                             },
                             headers=auth_headers,
                             content_type='multipart/form-data')
        
        assert response.status_code == 201
        
        data = json.loads(response.data)
        assert data['name'] == 'Test Dataset'
        assert data['file_type'] == 'csv'
    
    def test_upload_dataset_no_file(self, client, auth_headers):
        """Test dataset upload without file."""
        response = client.post('/api/datasets', 
                             data={'name': 'Test Dataset'},
                             headers=auth_headers)
        
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_get_dataset_details(self, client, auth_headers, sample_dataset):
        """Test getting dataset details."""
        response = client.get(f'/api/datasets/{sample_dataset.id}', headers=auth_headers)
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['id'] == sample_dataset.id
        assert data['name'] == sample_dataset.name
    
    def test_get_dataset_not_found(self, client, auth_headers):
        """Test getting non-existent dataset."""
        response = client.get('/api/datasets/999', headers=auth_headers)
        assert response.status_code == 404
    
    def test_update_dataset(self, client, auth_headers, sample_dataset):
        """Test updating dataset information."""
        response = client.put(f'/api/datasets/{sample_dataset.id}',
                            json={'name': 'Updated Dataset Name'},
                            headers=auth_headers)
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['name'] == 'Updated Dataset Name'
    
    def test_delete_dataset(self, client, auth_headers, sample_dataset):
        """Test deleting dataset."""
        response = client.delete(f'/api/datasets/{sample_dataset.id}', headers=auth_headers)
        assert response.status_code == 200
        
        # Verify dataset is deleted
        response = client.get(f'/api/datasets/{sample_dataset.id}', headers=auth_headers)
        assert response.status_code == 404
    
    def test_preview_dataset(self, client, auth_headers, sample_dataset):
        """Test dataset preview."""
        response = client.get(f'/api/datasets/{sample_dataset.id}/preview', headers=auth_headers)
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'columns' in data
        assert 'data' in data
        assert 'total_rows' in data
        assert len(data['data']) <= 10  # Default preview rows
    
    def test_column_statistics(self, client, auth_headers, sample_dataset):
        """Test getting column statistics."""
        response = client.get(f'/api/datasets/{sample_dataset.id}/columns/value/stats', 
                            headers=auth_headers)
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['name'] == 'value'
        assert 'count' in data
        assert 'mean' in data
    
    def test_column_statistics_not_found(self, client, auth_headers, sample_dataset):
        """Test getting statistics for non-existent column."""
        response = client.get(f'/api/datasets/{sample_dataset.id}/columns/nonexistent/stats', 
                            headers=auth_headers)
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data