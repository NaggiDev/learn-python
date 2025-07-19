"""
Integration tests for complete workflow scenarios.
"""
import pytest
import json
import tempfile
import os
from app.models import User, Dataset, AnalysisJob


class TestFullWorkflow:
    """Test complete user workflows."""
    
    def test_complete_data_analysis_workflow(self, client, auth):
        """Test complete workflow from registration to analysis."""
        
        # 1. Register user
        response = auth.register('analyst', 'analyst@test.com', 'password123')
        assert response.status_code == 201
        
        # 2. Login user
        response = auth.login('analyst', 'password123')
        assert response.status_code == 200
        
        # 3. Upload dataset
        csv_content = """id,name,value,category
1,Item_1,10.5,A
2,Item_2,20.3,B
3,Item_3,15.7,A
4,Item_4,25.1,B
5,Item_5,30.2,C
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            temp_path = f.name
        
        try:
            with open(temp_path, 'rb') as f:
                response = client.post('/api/datasets',
                                     data={
                                         'file': (f, 'test_data.csv'),
                                         'name': 'Test Analysis Dataset',
                                         'description': 'Dataset for workflow testing'
                                     },
                                     content_type='multipart/form-data')
            
            assert response.status_code == 201
            dataset_data = json.loads(response.data)
            dataset_id = dataset_data['id']
            
            # 4. Preview dataset
            response = client.get(f'/api/datasets/{dataset_id}/preview')
            assert response.status_code == 200
            
            preview_data = json.loads(response.data)
            assert len(preview_data['columns']) == 4
            assert preview_data['total_rows'] == 5
            
            # 5. Run descriptive statistics
            response = client.post('/api/analysis/descriptive',
                                 json={'dataset_id': dataset_id})
            assert response.status_code == 200
            
            stats_data = json.loads(response.data)
            assert 'columns' in stats_data
            assert 'value' in stats_data['columns']
            assert stats_data['columns']['value']['analysis_type'] == 'numeric'
            
            # 6. Run correlation analysis
            response = client.post('/api/analysis/correlation',
                                 json={'dataset_id': dataset_id, 'method': 'pearson'})
            assert response.status_code == 200
            
            corr_data = json.loads(response.data)
            assert 'correlation_matrix' in corr_data
            assert corr_data['method'] == 'pearson'
            
            # 7. Create visualization
            response = client.post('/api/visualizations/chart',
                                 json={
                                     'dataset_id': dataset_id,
                                     'chart_type': 'histogram',
                                     'x_column': 'value',
                                     'format': 'png'
                                 })
            assert response.status_code == 200
            
            chart_data = json.loads(response.data)
            assert 'chart_data' in chart_data
            assert chart_data['chart_type'] == 'histogram'
            
            # 8. Get dataset statistics for specific column
            response = client.get(f'/api/datasets/{dataset_id}/columns/value/stats')
            assert response.status_code == 200
            
            col_stats = json.loads(response.data)
            assert col_stats['name'] == 'value'
            assert 'mean' in col_stats
            
            # 9. Delete dataset
            response = client.delete(f'/api/datasets/{dataset_id}')
            assert response.status_code == 200
            
            # 10. Verify dataset is deleted
            response = client.get(f'/api/datasets/{dataset_id}')
            assert response.status_code == 404
            
        finally:
            # Cleanup temp file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_user_management_workflow(self, client, auth):
        """Test user management workflow."""
        
        # 1. Register regular user
        response = auth.register('user1', 'user1@test.com', 'password123', 'analyst')
        assert response.status_code == 201
        
        # 2. Register admin user
        response = auth.register('admin1', 'admin@test.com', 'adminpass123', 'admin')
        assert response.status_code == 201
        
        # 3. Login as admin
        response = auth.login('admin1', 'adminpass123')
        assert response.status_code == 200
        
        # 4. List all users (admin only)
        response = client.get('/api/auth/users')
        assert response.status_code == 200
        
        users_data = json.loads(response.data)
        assert len(users_data) >= 2
        
        # 5. Logout admin
        response = auth.logout()
        assert response.status_code == 200
        
        # 6. Login as regular user
        response = auth.login('user1', 'password123')
        assert response.status_code == 200
        
        # 7. Try to access admin endpoint (should fail)
        response = client.get('/api/auth/users')
        assert response.status_code == 403
        
        # 8. Update profile
        response = client.put('/api/auth/profile',
                            json={'email': 'newemail@test.com'})
        assert response.status_code == 200
        
        profile_data = json.loads(response.data)
        assert profile_data['email'] == 'newemail@test.com'
    
    def test_error_handling_workflow(self, client, auth):
        """Test error handling in various scenarios."""
        
        # 1. Register and login user
        response = auth.register('errortest', 'error@test.com', 'password123')
        assert response.status_code == 201
        
        response = auth.login('errortest', 'password123')
        assert response.status_code == 200
        
        # 2. Try to access non-existent dataset
        response = client.get('/api/datasets/999')
        assert response.status_code == 404
        
        # 3. Try to run analysis on non-existent dataset
        response = client.post('/api/analysis/descriptive',
                             json={'dataset_id': 999})
        assert response.status_code == 400
        
        # 4. Try to create chart with invalid parameters
        response = client.post('/api/visualizations/chart',
                             json={
                                 'dataset_id': 999,
                                 'chart_type': 'invalid_type'
                             })
        assert response.status_code == 404  # Dataset not found first
        
        # 5. Try to upload invalid file type
        response = client.post('/api/datasets',
                             data={
                                 'file': (b'invalid content', 'test.txt'),
                                 'name': 'Invalid Dataset'
                             },
                             content_type='multipart/form-data')
        assert response.status_code == 400
        
        # 6. Try to register with existing username
        response = auth.register('errortest', 'another@test.com', 'password123')
        assert response.status_code == 409
        
        # 7. Try to login with wrong password
        response = client.post('/api/auth/login',
                             json={'username': 'errortest', 'password': 'wrongpass'})
        assert response.status_code == 401
    
    def test_concurrent_operations(self, client, auth, sample_dataset):
        """Test concurrent operations on the same dataset."""
        
        # Login user
        response = auth.login()
        assert response.status_code == 200
        
        # Run multiple analyses concurrently (simulated)
        analyses = [
            {'dataset_id': sample_dataset.id, 'analysis_type': 'descriptive_statistics'},
            {'dataset_id': sample_dataset.id, 'analysis_type': 'correlation_analysis'}
        ]
        
        results = []
        for analysis in analyses:
            response = client.post('/api/analysis/run',
                                 json={**analysis, 'async': False})
            results.append(response.status_code)
        
        # All analyses should succeed
        assert all(status == 200 for status in results)
        
        # Create multiple charts
        charts = [
            {
                'dataset_id': sample_dataset.id,
                'chart_type': 'histogram',
                'x_column': 'value',
                'format': 'png'
            },
            {
                'dataset_id': sample_dataset.id,
                'chart_type': 'bar',
                'x_column': 'category',
                'format': 'png'
            }
        ]
        
        chart_results = []
        for chart in charts:
            response = client.post('/api/visualizations/chart', json=chart)
            chart_results.append(response.status_code)
        
        # All charts should be created successfully
        assert all(status == 200 for status in chart_results)
    
    def test_data_validation_workflow(self, client, auth):
        """Test data validation throughout the workflow."""
        
        # Register and login
        response = auth.register('validator', 'validator@test.com', 'password123')
        assert response.status_code == 201
        
        response = auth.login('validator', 'password123')
        assert response.status_code == 200
        
        # Test various invalid inputs
        invalid_requests = [
            # Missing required fields
            ('/api/analysis/descriptive', {}),
            ('/api/visualizations/chart', {}),
            
            # Invalid data types
            ('/api/analysis/descriptive', {'dataset_id': 'invalid'}),
            ('/api/visualizations/chart', {'dataset_id': 'invalid', 'chart_type': 'histogram'}),
            
            # Invalid enum values
            ('/api/visualizations/chart', {
                'dataset_id': 1,
                'chart_type': 'invalid_chart_type'
            }),
        ]
        
        for endpoint, data in invalid_requests:
            response = client.post(endpoint, json=data)
            # Should return 400 (Bad Request) or 404 (Not Found) for invalid dataset
            assert response.status_code in [400, 404]
    
    def test_performance_workflow(self, client, auth):
        """Test performance-related scenarios."""
        
        # Register and login
        response = auth.register('perftest', 'perf@test.com', 'password123')
        assert response.status_code == 201
        
        response = auth.login('perftest', 'password123')
        assert response.status_code == 200
        
        # Create a larger dataset for performance testing
        large_csv_content = "id,name,value,category\n"
        for i in range(1000):  # 1000 rows
            large_csv_content += f"{i},Item_{i},{i * 1.5},Category_{i % 5}\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(large_csv_content)
            temp_path = f.name
        
        try:
            # Upload large dataset
            with open(temp_path, 'rb') as f:
                response = client.post('/api/datasets',
                                     data={
                                         'file': (f, 'large_test_data.csv'),
                                         'name': 'Large Test Dataset',
                                         'description': 'Large dataset for performance testing'
                                     },
                                     content_type='multipart/form-data')
            
            assert response.status_code == 201
            dataset_data = json.loads(response.data)
            dataset_id = dataset_data['id']
            
            # Test preview with different row counts
            for rows in [10, 50, 100]:
                response = client.get(f'/api/datasets/{dataset_id}/preview?rows={rows}')
                assert response.status_code == 200
                
                preview_data = json.loads(response.data)
                assert len(preview_data['data']) <= rows
            
            # Run analysis on large dataset
            response = client.post('/api/analysis/descriptive',
                                 json={'dataset_id': dataset_id})
            assert response.status_code == 200
            
            # Cleanup
            response = client.delete(f'/api/datasets/{dataset_id}')
            assert response.status_code == 200
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)