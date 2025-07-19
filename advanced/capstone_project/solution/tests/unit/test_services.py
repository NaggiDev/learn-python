"""
Tests for service classes.
"""
import pytest
import pandas as pd
import tempfile
import os
from app.services.data_service import DataService
from app.services.analysis_service import AnalysisService
from app.models import Dataset


class TestDataService:
    """Test DataService class."""
    
    def test_allowed_file_valid(self):
        """Test allowed file validation with valid files."""
        assert DataService.allowed_file('test.csv') == True
        assert DataService.allowed_file('test.json') == True
        assert DataService.allowed_file('test.xlsx') == True
        assert DataService.allowed_file('test.xls') == True
    
    def test_allowed_file_invalid(self):
        """Test allowed file validation with invalid files."""
        assert DataService.allowed_file('test.txt') == False
        assert DataService.allowed_file('test.pdf') == False
        assert DataService.allowed_file('test') == False
        assert DataService.allowed_file('') == False
    
    def test_load_dataset_csv(self, sample_dataset):
        """Test loading CSV dataset."""
        df = DataService.load_dataset(sample_dataset)
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert 'id' in df.columns
        assert 'name' in df.columns
        assert 'value' in df.columns
    
    def test_load_dataset_not_found(self, sample_user):
        """Test loading non-existent dataset file."""
        dataset = Dataset(
            name='Missing Dataset',
            filename='missing.csv',
            file_path='/nonexistent/path.csv',
            file_size=100,
            file_type='csv',
            user_id=sample_user.id
        )
        
        with pytest.raises(ValueError, match="Dataset file not found"):
            DataService.load_dataset(dataset)
    
    def test_get_dataset_preview(self, sample_dataset):
        """Test getting dataset preview."""
        preview = DataService.get_dataset_preview(sample_dataset.id, rows=5)
        
        assert 'columns' in preview
        assert 'data' in preview
        assert 'total_rows' in preview
        assert len(preview['data']) <= 5
    
    def test_get_column_statistics_numeric(self, sample_dataset):
        """Test getting statistics for numeric column."""
        stats = DataService.get_column_statistics(sample_dataset, 'value')
        
        assert stats['name'] == 'value'
        assert 'count' in stats
        assert 'mean' in stats
        assert 'min' in stats
        assert 'max' in stats
    
    def test_get_column_statistics_categorical(self, sample_dataset):
        """Test getting statistics for categorical column."""
        stats = DataService.get_column_statistics(sample_dataset, 'category')
        
        assert stats['name'] == 'category'
        assert 'count' in stats
        assert 'unique_count' in stats
        assert 'most_frequent' in stats
    
    def test_get_column_statistics_not_found(self, sample_dataset):
        """Test getting statistics for non-existent column."""
        with pytest.raises(ValueError, match="Column 'nonexistent' not found"):
            DataService.get_column_statistics(sample_dataset, 'nonexistent')


class TestAnalysisService:
    """Test AnalysisService class."""
    
    def test_descriptive_statistics(self, sample_dataset):
        """Test descriptive statistics calculation."""
        result = AnalysisService.descriptive_statistics(sample_dataset.id)
        
        assert result['dataset_id'] == sample_dataset.id
        assert 'columns' in result
        assert 'total_rows' in result
        assert 'total_columns' in result
        
        # Check that numeric columns have proper statistics
        value_stats = result['columns']['value']
        assert value_stats['analysis_type'] == 'numeric'
        assert 'mean' in value_stats
        assert 'std' in value_stats
        assert 'quartiles' in value_stats
    
    def test_descriptive_statistics_specific_columns(self, sample_dataset):
        """Test descriptive statistics for specific columns."""
        result = AnalysisService.descriptive_statistics(
            sample_dataset.id, 
            columns=['value', 'category']
        )
        
        assert len(result['columns']) == 2
        assert 'value' in result['columns']
        assert 'category' in result['columns']
    
    def test_correlation_analysis(self, sample_dataset):
        """Test correlation analysis."""
        result = AnalysisService.correlation_analysis(sample_dataset.id)
        
        assert result['dataset_id'] == sample_dataset.id
        assert 'correlation_matrix' in result
        assert 'method' in result
        assert result['method'] == 'pearson'
    
    def test_correlation_analysis_spearman(self, sample_dataset):
        """Test Spearman correlation analysis."""
        result = AnalysisService.correlation_analysis(
            sample_dataset.id, 
            method='spearman'
        )
        
        assert result['method'] == 'spearman'
        assert 'correlation_matrix' in result
    
    def test_distribution_analysis_numeric(self, sample_dataset):
        """Test distribution analysis for numeric column."""
        result = AnalysisService.distribution_analysis(
            sample_dataset.id, 
            column='value'
        )
        
        assert result['dataset_id'] == sample_dataset.id
        assert result['column'] == 'value'
        assert 'histogram' in result
        assert 'counts' in result['histogram']
        assert 'bin_edges' in result['histogram']
    
    def test_distribution_analysis_categorical(self, sample_dataset):
        """Test distribution analysis for categorical column."""
        result = AnalysisService.distribution_analysis(
            sample_dataset.id, 
            column='category'
        )
        
        assert result['column'] == 'category'
        assert 'frequency_distribution' in result
        assert 'values' in result['frequency_distribution']
        assert 'counts' in result['frequency_distribution']
    
    def test_outlier_detection_iqr(self, sample_dataset):
        """Test outlier detection using IQR method."""
        result = AnalysisService.outlier_detection(
            sample_dataset.id,
            columns=['value'],
            method='iqr'
        )
        
        assert result['dataset_id'] == sample_dataset.id
        assert result['method'] == 'iqr'
        assert 'columns' in result
        assert 'value' in result['columns']
        
        value_outliers = result['columns']['value']
        assert 'outlier_count' in value_outliers
        assert 'lower_bound' in value_outliers
        assert 'upper_bound' in value_outliers
    
    def test_outlier_detection_zscore(self, sample_dataset):
        """Test outlier detection using Z-score method."""
        result = AnalysisService.outlier_detection(
            sample_dataset.id,
            columns=['value'],
            method='zscore'
        )
        
        assert result['method'] == 'zscore'
        value_outliers = result['columns']['value']
        assert 'threshold' in value_outliers
        assert 'max_zscore' in value_outliers
    
    def test_analysis_invalid_dataset(self):
        """Test analysis with invalid dataset ID."""
        with pytest.raises(ValueError, match="Dataset not found"):
            AnalysisService.descriptive_statistics(999)
    
    def test_analysis_invalid_column(self, sample_dataset):
        """Test analysis with invalid column name."""
        with pytest.raises(ValueError, match="Column 'nonexistent' not found"):
            AnalysisService.distribution_analysis(
                sample_dataset.id, 
                column='nonexistent'
            )