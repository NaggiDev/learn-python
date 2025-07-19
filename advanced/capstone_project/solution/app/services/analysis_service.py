"""
Analysis service for statistical analysis and data processing.
"""
import pandas as pd
import numpy as np
from typing import Dict, Any, List, Optional
from scipy import stats
from flask import current_app
from app import cache
from app.models.dataset import Dataset
from app.services.data_service import DataService


class AnalysisService:
    """Service class for statistical analysis operations."""
    
    @staticmethod
    @cache.memoize(timeout=3600)  # Cache for 1 hour
    def descriptive_statistics(dataset_id: int, columns: List[str] = None) -> Dict[str, Any]:
        """
        Calculate descriptive statistics for dataset columns.
        
        Args:
            dataset_id (int): ID of the dataset to analyze
            columns (list, optional): Specific columns to analyze
            
        Returns:
            dict: Descriptive statistics results
        """
        dataset = Dataset.query.get(dataset_id)
        if not dataset:
            raise ValueError("Dataset not found")
        
        df = DataService.load_dataset(dataset)
        
        # Select columns to analyze
        if columns:
            # Filter to only existing columns
            columns = [col for col in columns if col in df.columns]
            if not columns:
                raise ValueError("No valid columns specified")
            df = df[columns]
        
        results = {
            'dataset_id': dataset_id,
            'dataset_name': dataset.name,
            'total_rows': len(df),
            'total_columns': len(df.columns),
            'analysis_timestamp': pd.Timestamp.now().isoformat(),
            'columns': {}
        }
        
        for column in df.columns:
            col_stats = AnalysisService._analyze_column(df[column])
            results['columns'][column] = col_stats
        
        # Overall dataset statistics
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) > 0:
            results['numeric_summary'] = {
                'column_count': len(numeric_columns),
                'total_missing': int(df[numeric_columns].isnull().sum().sum()),
                'correlation_available': len(numeric_columns) > 1
            }
        
        return results
    
    @staticmethod
    def _analyze_column(series: pd.Series) -> Dict[str, Any]:
        """
        Analyze a single column and return statistics.
        
        Args:
            series (pd.Series): Column data to analyze
            
        Returns:
            dict: Column analysis results
        """
        stats_dict = {
            'name': series.name,
            'dtype': str(series.dtype),
            'count': int(series.count()),
            'null_count': int(series.isnull().sum()),
            'null_percentage': float(series.isnull().sum() / len(series) * 100),
            'unique_count': int(series.nunique()),
            'unique_percentage': float(series.nunique() / series.count() * 100) if series.count() > 0 else 0
        }
        
        # Most frequent value
        if series.count() > 0:
            mode_values = series.mode()
            stats_dict['most_frequent'] = mode_values.iloc[0] if not mode_values.empty else None
            stats_dict['most_frequent_count'] = int(series.value_counts().iloc[0]) if not series.value_counts().empty else 0
        
        # Numeric column analysis
        if pd.api.types.is_numeric_dtype(series):
            numeric_stats = AnalysisService._analyze_numeric_column(series)
            stats_dict.update(numeric_stats)
        
        # Categorical column analysis
        elif pd.api.types.is_object_dtype(series) or pd.api.types.is_categorical_dtype(series):
            categorical_stats = AnalysisService._analyze_categorical_column(series)
            stats_dict.update(categorical_stats)
        
        # DateTime column analysis
        elif pd.api.types.is_datetime64_any_dtype(series):
            datetime_stats = AnalysisService._analyze_datetime_column(series)
            stats_dict.update(datetime_stats)
        
        return stats_dict
    
    @staticmethod
    def _analyze_numeric_column(series: pd.Series) -> Dict[str, Any]:
        """Analyze numeric column."""
        clean_series = series.dropna()
        
        if len(clean_series) == 0:
            return {'analysis_type': 'numeric', 'error': 'No non-null values'}
        
        stats_dict = {
            'analysis_type': 'numeric',
            'min': float(clean_series.min()),
            'max': float(clean_series.max()),
            'mean': float(clean_series.mean()),
            'median': float(clean_series.median()),
            'std': float(clean_series.std()),
            'variance': float(clean_series.var()),
            'skewness': float(clean_series.skew()),
            'kurtosis': float(clean_series.kurtosis()),
            'quartiles': {
                'q1': float(clean_series.quantile(0.25)),
                'q2': float(clean_series.quantile(0.5)),
                'q3': float(clean_series.quantile(0.75))
            },
            'percentiles': {
                'p5': float(clean_series.quantile(0.05)),
                'p10': float(clean_series.quantile(0.10)),
                'p90': float(clean_series.quantile(0.90)),
                'p95': float(clean_series.quantile(0.95))
            }
        }
        
        # Outlier detection using IQR method
        q1, q3 = stats_dict['quartiles']['q1'], stats_dict['quartiles']['q3']
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = clean_series[(clean_series < lower_bound) | (clean_series > upper_bound)]
        
        stats_dict['outliers'] = {
            'count': len(outliers),
            'percentage': float(len(outliers) / len(clean_series) * 100),
            'lower_bound': lower_bound,
            'upper_bound': upper_bound
        }
        
        # Distribution analysis
        try:
            # Normality test (Shapiro-Wilk for small samples, Anderson-Darling for larger)
            if len(clean_series) <= 5000:
                shapiro_stat, shapiro_p = stats.shapiro(clean_series)
                stats_dict['normality_test'] = {
                    'test': 'shapiro',
                    'statistic': float(shapiro_stat),
                    'p_value': float(shapiro_p),
                    'is_normal': shapiro_p > 0.05
                }
            else:
                anderson_result = stats.anderson(clean_series, dist='norm')
                stats_dict['normality_test'] = {
                    'test': 'anderson',
                    'statistic': float(anderson_result.statistic),
                    'critical_values': anderson_result.critical_values.tolist(),
                    'significance_levels': anderson_result.significance_level.tolist()
                }
        except Exception:
            stats_dict['normality_test'] = {'error': 'Could not perform normality test'}
        
        return stats_dict
    
    @staticmethod
    def _analyze_categorical_column(series: pd.Series) -> Dict[str, Any]:
        """Analyze categorical column."""
        clean_series = series.dropna()
        
        if len(clean_series) == 0:
            return {'analysis_type': 'categorical', 'error': 'No non-null values'}
        
        value_counts = clean_series.value_counts()
        
        stats_dict = {
            'analysis_type': 'categorical',
            'top_values': value_counts.head(10).to_dict(),
            'entropy': float(stats.entropy(value_counts.values)),
            'mode': value_counts.index[0] if not value_counts.empty else None,
            'mode_frequency': int(value_counts.iloc[0]) if not value_counts.empty else 0,
            'mode_percentage': float(value_counts.iloc[0] / len(clean_series) * 100) if not value_counts.empty else 0
        }
        
        # String length analysis for text data
        if pd.api.types.is_string_dtype(series):
            str_lengths = clean_series.astype(str).str.len()
            stats_dict['string_length'] = {
                'min': int(str_lengths.min()),
                'max': int(str_lengths.max()),
                'mean': float(str_lengths.mean()),
                'median': float(str_lengths.median())
            }
        
        return stats_dict
    
    @staticmethod
    def _analyze_datetime_column(series: pd.Series) -> Dict[str, Any]:
        """Analyze datetime column."""
        clean_series = series.dropna()
        
        if len(clean_series) == 0:
            return {'analysis_type': 'datetime', 'error': 'No non-null values'}
        
        stats_dict = {
            'analysis_type': 'datetime',
            'min': clean_series.min().isoformat(),
            'max': clean_series.max().isoformat(),
            'range_days': (clean_series.max() - clean_series.min()).days,
            'most_frequent': clean_series.mode().iloc[0].isoformat() if not clean_series.mode().empty else None
        }
        
        # Extract time components for analysis
        stats_dict['time_components'] = {
            'years': sorted(clean_series.dt.year.unique().tolist()),
            'months': sorted(clean_series.dt.month.unique().tolist()),
            'days_of_week': sorted(clean_series.dt.dayofweek.unique().tolist()),
            'hours': sorted(clean_series.dt.hour.unique().tolist()) if clean_series.dt.hour.nunique() > 1 else None
        }
        
        return stats_dict
    
    @staticmethod
    @cache.memoize(timeout=3600)
    def correlation_analysis(dataset_id: int, columns: List[str] = None, method: str = 'pearson') -> Dict[str, Any]:
        """
        Calculate correlation matrix for numeric columns.
        
        Args:
            dataset_id (int): ID of the dataset to analyze
            columns (list, optional): Specific columns to include
            method (str): Correlation method ('pearson', 'spearman', 'kendall')
            
        Returns:
            dict: Correlation analysis results
        """
        dataset = Dataset.query.get(dataset_id)
        if not dataset:
            raise ValueError("Dataset not found")
        
        df = DataService.load_dataset(dataset)
        
        # Select numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
        
        if columns:
            # Filter to specified columns that are numeric
            columns = [col for col in columns if col in numeric_df.columns]
            if not columns:
                raise ValueError("No valid numeric columns specified")
            numeric_df = numeric_df[columns]
        
        if len(numeric_df.columns) < 2:
            raise ValueError("At least 2 numeric columns required for correlation analysis")
        
        if len(numeric_df.columns) > current_app.config.get('MAX_CORRELATION_COLUMNS', 50):
            raise ValueError(f"Too many columns for correlation analysis (max: {current_app.config.get('MAX_CORRELATION_COLUMNS', 50)})")
        
        # Calculate correlation matrix
        corr_matrix = numeric_df.corr(method=method)
        
        # Find strong correlations
        strong_correlations = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                corr_value = corr_matrix.iloc[i, j]
                if not pd.isna(corr_value) and abs(corr_value) >= 0.7:
                    strong_correlations.append({
                        'column1': corr_matrix.columns[i],
                        'column2': corr_matrix.columns[j],
                        'correlation': float(corr_value),
                        'strength': 'strong' if abs(corr_value) >= 0.8 else 'moderate'
                    })
        
        # Sort by absolute correlation value
        strong_correlations.sort(key=lambda x: abs(x['correlation']), reverse=True)
        
        return {
            'dataset_id': dataset_id,
            'dataset_name': dataset.name,
            'method': method,
            'correlation_matrix': corr_matrix.to_dict(),
            'strong_correlations': strong_correlations,
            'analysis_timestamp': pd.Timestamp.now().isoformat(),
            'columns_analyzed': corr_matrix.columns.tolist()
        }
    
    @staticmethod
    def distribution_analysis(dataset_id: int, column: str, bins: int = 30) -> Dict[str, Any]:
        """
        Analyze the distribution of a specific column.
        
        Args:
            dataset_id (int): ID of the dataset
            column (str): Column name to analyze
            bins (int): Number of bins for histogram
            
        Returns:
            dict: Distribution analysis results
        """
        dataset = Dataset.query.get(dataset_id)
        if not dataset:
            raise ValueError("Dataset not found")
        
        df = DataService.load_dataset(dataset)
        
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in dataset")
        
        series = df[column].dropna()
        
        if len(series) == 0:
            raise ValueError(f"Column '{column}' has no non-null values")
        
        results = {
            'dataset_id': dataset_id,
            'column': column,
            'analysis_timestamp': pd.Timestamp.now().isoformat()
        }
        
        if pd.api.types.is_numeric_dtype(series):
            # Histogram data
            hist, bin_edges = np.histogram(series, bins=bins)
            results['histogram'] = {
                'counts': hist.tolist(),
                'bin_edges': bin_edges.tolist(),
                'bins': bins
            }
            
            # Distribution fitting
            try:
                # Test for common distributions
                distributions = ['norm', 'expon', 'gamma', 'beta', 'lognorm']
                best_fit = None
                best_p_value = 0
                
                for dist_name in distributions:
                    try:
                        dist = getattr(stats, dist_name)
                        params = dist.fit(series)
                        ks_stat, p_value = stats.kstest(series, lambda x: dist.cdf(x, *params))
                        
                        if p_value > best_p_value:
                            best_p_value = p_value
                            best_fit = {
                                'distribution': dist_name,
                                'parameters': params,
                                'ks_statistic': float(ks_stat),
                                'p_value': float(p_value)
                            }
                    except Exception:
                        continue
                
                if best_fit:
                    results['best_fit_distribution'] = best_fit
                
            except Exception as e:
                results['distribution_fitting_error'] = str(e)
        
        else:
            # For categorical data, provide frequency distribution
            value_counts = series.value_counts()
            results['frequency_distribution'] = {
                'values': value_counts.index.tolist(),
                'counts': value_counts.values.tolist(),
                'percentages': (value_counts / len(series) * 100).tolist()
            }
        
        return results
    
    @staticmethod
    def outlier_detection(dataset_id: int, columns: List[str] = None, method: str = 'iqr') -> Dict[str, Any]:
        """
        Detect outliers in numeric columns.
        
        Args:
            dataset_id (int): ID of the dataset
            columns (list, optional): Specific columns to analyze
            method (str): Outlier detection method ('iqr', 'zscore', 'isolation_forest')
            
        Returns:
            dict: Outlier detection results
        """
        dataset = Dataset.query.get(dataset_id)
        if not dataset:
            raise ValueError("Dataset not found")
        
        df = DataService.load_dataset(dataset)
        numeric_df = df.select_dtypes(include=[np.number])
        
        if columns:
            columns = [col for col in columns if col in numeric_df.columns]
            if not columns:
                raise ValueError("No valid numeric columns specified")
            numeric_df = numeric_df[columns]
        
        if len(numeric_df.columns) == 0:
            raise ValueError("No numeric columns found for outlier detection")
        
        results = {
            'dataset_id': dataset_id,
            'method': method,
            'analysis_timestamp': pd.Timestamp.now().isoformat(),
            'columns': {}
        }
        
        for column in numeric_df.columns:
            series = numeric_df[column].dropna()
            
            if len(series) == 0:
                continue
            
            if method == 'iqr':
                outliers = AnalysisService._detect_outliers_iqr(series)
            elif method == 'zscore':
                outliers = AnalysisService._detect_outliers_zscore(series)
            else:
                raise ValueError(f"Unsupported outlier detection method: {method}")
            
            results['columns'][column] = outliers
        
        return results
    
    @staticmethod
    def _detect_outliers_iqr(series: pd.Series, factor: float = 1.5) -> Dict[str, Any]:
        """Detect outliers using IQR method."""
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        
        lower_bound = q1 - factor * iqr
        upper_bound = q3 + factor * iqr
        
        outliers = series[(series < lower_bound) | (series > upper_bound)]
        
        return {
            'method': 'iqr',
            'lower_bound': float(lower_bound),
            'upper_bound': float(upper_bound),
            'outlier_count': len(outliers),
            'outlier_percentage': float(len(outliers) / len(series) * 100),
            'outlier_values': outliers.tolist()[:100],  # Limit to first 100
            'q1': float(q1),
            'q3': float(q3),
            'iqr': float(iqr)
        }
    
    @staticmethod
    def _detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> Dict[str, Any]:
        """Detect outliers using Z-score method."""
        z_scores = np.abs(stats.zscore(series))
        outliers = series[z_scores > threshold]
        
        return {
            'method': 'zscore',
            'threshold': threshold,
            'outlier_count': len(outliers),
            'outlier_percentage': float(len(outliers) / len(series) * 100),
            'outlier_values': outliers.tolist()[:100],  # Limit to first 100
            'max_zscore': float(z_scores.max()),
            'mean_zscore': float(z_scores.mean())
        }