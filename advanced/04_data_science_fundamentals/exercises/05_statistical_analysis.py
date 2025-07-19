"""
Statistical Analysis Exercises

This exercise file covers fundamental statistical analysis concepts including:
- Descriptive statistics
- Probability distributions
- Hypothesis testing
- Correlation analysis
- Confidence intervals
- Linear regression
- ANOVA

Complete each exercise by implementing the required functionality.
Run the tests to verify your solutions.
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, t, chi2
import warnings
warnings.filterwarnings('ignore')


def exercise_1_descriptive_statistics():
    """
    Exercise 1: Descriptive Statistics
    
    Calculate comprehensive descriptive statistics for a dataset:
    1. Measures of central tendency (mean, median, mode)
    2. Measures of variability (range, variance, std dev, IQR)
    3. Distribution shape (skewness, kurtosis)
    4. Percentiles and quartiles
    
    Returns:
        dict: Dictionary containing all calculated statistics
    """
    # Generate sample data
    np.random.seed(42)
    data = np.random.gamma(2, 2, 1000)  # Gamma distribution for interesting shape
    
    # TODO: Calculate measures of central tendency
    mean_val = None
    median_val = None
    mode_val = None  # Use scipy.stats.mode
    
    # TODO: Calculate measures of variability
    range_val = None
    variance_val = None  # Use ddof=1 for sample variance
    std_dev_val = None   # Use ddof=1 for sample std dev
    iqr_val = None       # Q3 - Q1
    
    # TODO: Calculate distribution shape
    skewness_val = None  # Use scipy.stats.skew
    kurtosis_val = None  # Use scipy.stats.kurtosis
    
    # TODO: Calculate percentiles
    percentiles = [5, 10, 25, 50, 75, 90, 95]
    percentile_values = None  # Use np.percentile
    
    # TODO: Create five-number summary
    five_number_summary = {
        'min': None,
        'q1': None,
        'median': None,
        'q3': None,
        'max': None
    }
    
    return {
        'data': data,
        'mean': mean_val,
        'median': median_val,
        'mode': mode_val,
        'range': range_val,
        'variance': variance_val,
        'std_dev': std_dev_val,
        'iqr': iqr_val,
        'skewness': skewness_val,
        'kurtosis': kurtosis_val,
        'percentiles': dict(zip(percentiles, percentile_values)) if percentile_values is not None else None,
        'five_number_summary': five_number_summary
    }


def exercise_2_probability_distributions():
    """
    Exercise 2: Probability Distributions
    
    Work with different probability distributions:
    1. Normal distribution calculations
    2. Binomial distribution
    3. Poisson distribution
    4. Distribution fitting and testing
    
    Returns:
        dict: Results from distribution analysis
    """
    np.random.seed(42)
    
    # TODO: Normal distribution analysis
    # Parameters: mean=100, std=15
    mu, sigma = 100, 15
    
    # Calculate probabilities
    prob_less_than_85 = None    # P(X < 85)
    prob_between_90_110 = None  # P(90 < X < 110)
    prob_greater_than_130 = None # P(X > 130)
    
    # Calculate critical values
    value_at_95th_percentile = None  # Value at 95th percentile
    value_at_5th_percentile = None   # Value at 5th percentile
    
    # TODO: Binomial distribution
    # Parameters: n=20 trials, p=0.3 success probability
    n_trials, p_success = 20, 0.3
    
    # Calculate probabilities
    prob_exactly_5_successes = None   # P(X = 5)
    prob_at_most_8_successes = None   # P(X ≤ 8)
    prob_at_least_10_successes = None # P(X ≥ 10)
    
    # Calculate expected value and variance
    binomial_mean = None
    binomial_variance = None
    
    # TODO: Poisson distribution
    # Parameter: λ=4 events per interval
    lambda_param = 4
    
    # Calculate probabilities
    prob_exactly_3_events = None  # P(X = 3)
    prob_less_than_2_events = None # P(X < 2)
    prob_more_than_6_events = None # P(X > 6)
    
    # TODO: Distribution fitting
    # Generate sample data and test if it follows normal distribution
    sample_data = np.random.normal(50, 10, 200)
    
    # Perform Shapiro-Wilk normality test
    shapiro_statistic = None
    shapiro_p_value = None
    is_normal = None  # True if p > 0.05
    
    return {
        'normal_analysis': {
            'prob_less_than_85': prob_less_than_85,
            'prob_between_90_110': prob_between_90_110,
            'prob_greater_than_130': prob_greater_than_130,
            'value_95th_percentile': value_at_95th_percentile,
            'value_5th_percentile': value_at_5th_percentile
        },
        'binomial_analysis': {
            'prob_exactly_5': prob_exactly_5_successes,
            'prob_at_most_8': prob_at_most_8_successes,
            'prob_at_least_10': prob_at_least_10_successes,
            'mean': binomial_mean,
            'variance': binomial_variance
        },
        'poisson_analysis': {
            'prob_exactly_3': prob_exactly_3_events,
            'prob_less_than_2': prob_less_than_2_events,
            'prob_more_than_6': prob_more_than_6_events
        },
        'normality_test': {
            'statistic': shapiro_statistic,
            'p_value': shapiro_p_value,
            'is_normal': is_normal
        }
    }


def exercise_3_hypothesis_testing():
    """
    Exercise 3: Hypothesis Testing
    
    Perform various hypothesis tests:
    1. One-sample t-test
    2. Two-sample t-test
    3. Paired t-test
    4. Chi-square test of independence
    
    Returns:
        dict: Results from all hypothesis tests
    """
    np.random.seed(42)
    
    # TODO: One-sample t-test
    # Test if sample mean differs from hypothesized value
    sample = np.random.normal(52, 8, 25)  # Sample data
    hypothesized_mean = 50
    
    # Perform one-sample t-test
    one_sample_t_stat = None
    one_sample_p_value = None
    one_sample_reject_null = None  # True if p < 0.05
    
    # TODO: Two-sample t-test (independent samples)
    # Compare means of two independent groups
    group1 = np.random.normal(100, 15, 30)
    group2 = np.random.normal(105, 15, 30)
    
    # Perform independent samples t-test
    two_sample_t_stat = None
    two_sample_p_value = None
    two_sample_reject_null = None  # True if p < 0.05
    
    # Calculate effect size (Cohen's d)
    cohens_d = None
    
    # TODO: Paired t-test
    # Compare before and after measurements
    before = np.random.normal(80, 10, 20)
    after = before + np.random.normal(5, 3, 20)  # After tends to be higher
    
    # Perform paired t-test
    paired_t_stat = None
    paired_p_value = None
    paired_reject_null = None  # True if p < 0.05
    
    # TODO: Chi-square test of independence
    # Test relationship between two categorical variables
    # Contingency table: rows=gender, columns=product preference
    observed = np.array([[20, 30, 25],   # Male preferences for products A, B, C
                        [25, 20, 30]])   # Female preferences for products A, B, C
    
    # Perform chi-square test
    chi2_stat = None
    chi2_p_value = None
    chi2_dof = None  # degrees of freedom
    chi2_expected = None  # expected frequencies
    chi2_reject_null = None  # True if p < 0.05
    
    return {
        'one_sample_test': {
            't_statistic': one_sample_t_stat,
            'p_value': one_sample_p_value,
            'reject_null': one_sample_reject_null,
            'sample_mean': np.mean(sample),
            'hypothesized_mean': hypothesized_mean
        },
        'two_sample_test': {
            't_statistic': two_sample_t_stat,
            'p_value': two_sample_p_value,
            'reject_null': two_sample_reject_null,
            'group1_mean': np.mean(group1),
            'group2_mean': np.mean(group2),
            'cohens_d': cohens_d
        },
        'paired_test': {
            't_statistic': paired_t_stat,
            'p_value': paired_p_value,
            'reject_null': paired_reject_null,
            'mean_difference': np.mean(after - before)
        },
        'chi_square_test': {
            'chi2_statistic': chi2_stat,
            'p_value': chi2_p_value,
            'degrees_of_freedom': chi2_dof,
            'expected_frequencies': chi2_expected,
            'reject_null': chi2_reject_null,
            'observed_frequencies': observed
        }
    }


def exercise_4_correlation_analysis():
    """
    Exercise 4: Correlation and Covariance Analysis
    
    Analyze relationships between variables:
    1. Pearson correlation
    2. Spearman correlation
    3. Covariance calculation
    4. Correlation significance testing
    
    Returns:
        dict: Correlation analysis results
    """
    np.random.seed(42)
    
    # Generate sample data with different correlation patterns
    n = 100
    
    # Strong positive linear relationship
    x1 = np.random.randn(n)
    y1 = 2 * x1 + np.random.randn(n) * 0.5
    
    # Moderate negative linear relationship
    x2 = np.random.randn(n)
    y2 = -1.5 * x2 + np.random.randn(n) * 1.5
    
    # Non-linear relationship (quadratic)
    x3 = np.random.uniform(-3, 3, n)
    y3 = x3**2 + np.random.randn(n) * 2
    
    # No relationship
    x4 = np.random.randn(n)
    y4 = np.random.randn(n)
    
    # TODO: Calculate Pearson correlations
    pearson_corr_1 = None  # x1, y1
    pearson_corr_2 = None  # x2, y2
    pearson_corr_3 = None  # x3, y3 (should be weak due to non-linearity)
    pearson_corr_4 = None  # x4, y4
    
    # TODO: Calculate Spearman correlations (rank-based)
    spearman_corr_1 = None  # x1, y1
    spearman_corr_2 = None  # x2, y2
    spearman_corr_3 = None  # x3, y3 (should be stronger than Pearson)
    spearman_corr_4 = None  # x4, y4
    
    # TODO: Calculate covariances
    covariance_1 = None  # x1, y1
    covariance_2 = None  # x2, y2
    covariance_3 = None  # x3, y3
    covariance_4 = None  # x4, y4
    
    # TODO: Test correlation significance
    # For x1, y1 relationship
    corr_test_statistic = None
    corr_test_p_value = None
    corr_is_significant = None  # True if p < 0.05
    
    # TODO: Create correlation matrix for multiple variables
    data_matrix = np.column_stack([x1, y1, x2, y2])
    correlation_matrix = None
    
    return {
        'pearson_correlations': {
            'strong_positive': pearson_corr_1,
            'moderate_negative': pearson_corr_2,
            'non_linear': pearson_corr_3,
            'no_relationship': pearson_corr_4
        },
        'spearman_correlations': {
            'strong_positive': spearman_corr_1,
            'moderate_negative': spearman_corr_2,
            'non_linear': spearman_corr_3,
            'no_relationship': spearman_corr_4
        },
        'covariances': {
            'strong_positive': covariance_1,
            'moderate_negative': covariance_2,
            'non_linear': covariance_3,
            'no_relationship': covariance_4
        },
        'significance_test': {
            'test_statistic': corr_test_statistic,
            'p_value': corr_test_p_value,
            'is_significant': corr_is_significant
        },
        'correlation_matrix': correlation_matrix,
        'sample_data': {
            'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
            'x3': x3, 'y3': y3, 'x4': x4, 'y4': y4
        }
    }


def exercise_5_confidence_intervals():
    """
    Exercise 5: Confidence Intervals
    
    Calculate confidence intervals for various parameters:
    1. Confidence interval for mean
    2. Confidence interval for proportion
    3. Bootstrap confidence intervals
    4. Prediction intervals
    
    Returns:
        dict: Confidence interval results
    """
    np.random.seed(42)
    
    # TODO: Confidence interval for mean
    sample = np.random.normal(75, 12, 40)
    
    # Calculate 95% confidence interval for mean
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    n = len(sample)
    
    # Use t-distribution for small sample
    confidence_level = 0.95
    alpha = 1 - confidence_level
    t_critical = None  # Use stats.t.ppf
    
    margin_of_error = None
    ci_mean_lower = None
    ci_mean_upper = None
    
    # TODO: Confidence interval for proportion
    # Sample: 65 successes out of 100 trials
    successes = 65
    n_trials = 100
    sample_proportion = successes / n_trials
    
    # Calculate 95% confidence interval for proportion
    z_critical = None  # Use stats.norm.ppf for 95% CI
    
    # Standard error for proportion
    se_proportion = None
    ci_prop_lower = None
    ci_prop_upper = None
    
    # TODO: Bootstrap confidence intervals
    def bootstrap_mean(data, n_bootstrap=1000):
        """Calculate bootstrap confidence interval for mean"""
        bootstrap_means = []
        n = len(data)
        
        for _ in range(n_bootstrap):
            # Resample with replacement
            bootstrap_sample = None  # Use np.random.choice
            bootstrap_means.append(np.mean(bootstrap_sample))
        
        return np.array(bootstrap_means)
    
    # Generate bootstrap samples
    bootstrap_means = bootstrap_mean(sample)
    
    # Calculate percentile confidence interval
    ci_boot_lower = None  # 2.5th percentile
    ci_boot_upper = None  # 97.5th percentile
    
    # TODO: Prediction interval (simplified)
    # For a simple linear regression context
    x_reg = np.random.uniform(0, 10, 50)
    y_reg = 2 * x_reg + 1 + np.random.normal(0, 1, 50)
    
    # Fit simple linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_reg, y_reg)
    
    # Predict for new value
    x_new = 5.0
    y_pred = slope * x_new + intercept
    
    # Calculate prediction interval (simplified)
    residuals = y_reg - (slope * x_reg + intercept)
    mse = np.mean(residuals**2)
    
    # Simplified prediction interval
    pred_std_error = np.sqrt(mse * (1 + 1/len(x_reg)))
    t_crit_pred = stats.t.ppf(0.975, df=len(x_reg)-2)
    
    pred_margin = t_crit_pred * pred_std_error
    pred_lower = y_pred - pred_margin
    pred_upper = y_pred + pred_margin
    
    return {
        'mean_ci': {
            'sample_mean': sample_mean,
            'lower_bound': ci_mean_lower,
            'upper_bound': ci_mean_upper,
            'margin_of_error': margin_of_error,
            'confidence_level': confidence_level
        },
        'proportion_ci': {
            'sample_proportion': sample_proportion,
            'lower_bound': ci_prop_lower,
            'upper_bound': ci_prop_upper,
            'sample_size': n_trials,
            'successes': successes
        },
        'bootstrap_ci': {
            'lower_bound': ci_boot_lower,
            'upper_bound': ci_boot_upper,
            'bootstrap_mean': np.mean(bootstrap_means),
            'original_mean': sample_mean
        },
        'prediction_interval': {
            'predicted_value': y_pred,
            'lower_bound': pred_lower,
            'upper_bound': pred_upper,
            'x_new': x_new
        }
    }


def exercise_6_regression_analysis():
    """
    Exercise 6: Linear Regression Analysis
    
    Perform comprehensive regression analysis:
    1. Simple linear regression
    2. Multiple linear regression
    3. Regression diagnostics
    4. Model evaluation
    
    Returns:
        dict: Regression analysis results
    """
    np.random.seed(42)
    
    # TODO: Simple linear regression
    n = 100
    x = np.random.uniform(0, 10, n)
    y = 3 * x + 2 + np.random.normal(0, 2, n)  # y = 3x + 2 + noise
    
    # Perform simple linear regression
    slope = None
    intercept = None
    r_value = None
    p_value = None
    std_err = None
    
    # Calculate R-squared
    r_squared = None
    
    # Calculate predictions and residuals
    y_pred = None
    residuals = None
    
    # TODO: Multiple linear regression (using matrix operations)
    # Generate data with multiple predictors
    x1 = np.random.randn(n)
    x2 = np.random.randn(n)
    x3 = np.random.randn(n)
    y_multi = 2*x1 + 3*x2 - 1*x3 + 5 + np.random.normal(0, 1, n)
    
    # Create design matrix (add intercept column)
    X = None  # Should be n x 4 matrix (intercept, x1, x2, x3)
    
    # Calculate coefficients using normal equation: β = (X'X)^(-1)X'y
    coefficients = None
    
    # Calculate predictions
    y_multi_pred = None
    
    # Calculate R-squared for multiple regression
    ss_res = np.sum((y_multi - y_multi_pred) ** 2)
    ss_tot = np.sum((y_multi - np.mean(y_multi)) ** 2)
    r_squared_multi = None
    
    # TODO: Regression diagnostics
    # Calculate various diagnostic measures
    
    # Mean Squared Error
    mse_simple = None
    mse_multi = None
    
    # Mean Absolute Error
    mae_simple = None
    mae_multi = None
    
    # Durbin-Watson test for autocorrelation (simplified)
    def durbin_watson(residuals):
        """Calculate Durbin-Watson statistic"""
        diff_residuals = np.diff(residuals)
        dw_stat = np.sum(diff_residuals**2) / np.sum(residuals**2)
        return dw_stat
    
    dw_statistic = durbin_watson(residuals)
    
    return {
        'simple_regression': {
            'slope': slope,
            'intercept': intercept,
            'r_value': r_value,
            'r_squared': r_squared,
            'p_value': p_value,
            'std_error': std_err,
            'mse': mse_simple,
            'mae': mae_simple,
            'predictions': y_pred,
            'residuals': residuals
        },
        'multiple_regression': {
            'coefficients': coefficients,
            'r_squared': r_squared_multi,
            'mse': mse_multi,
            'mae': mae_multi,
            'predictions': y_multi_pred
        },
        'diagnostics': {
            'durbin_watson': dw_statistic
        },
        'data': {
            'x': x, 'y': y,
            'x1': x1, 'x2': x2, 'x3': x3, 'y_multi': y_multi
        }
    }


def exercise_7_anova():
    """
    Exercise 7: Analysis of Variance (ANOVA)
    
    Perform ANOVA tests:
    1. One-way ANOVA
    2. Two-way ANOVA (simplified)
    3. Post-hoc analysis
    4. Effect size calculation
    
    Returns:
        dict: ANOVA analysis results
    """
    np.random.seed(42)
    
    # TODO: One-way ANOVA
    # Compare means across multiple groups
    group1 = np.random.normal(20, 5, 30)  # Group 1: mean=20
    group2 = np.random.normal(25, 5, 30)  # Group 2: mean=25
    group3 = np.random.normal(22, 5, 30)  # Group 3: mean=22
    group4 = np.random.normal(28, 5, 30)  # Group 4: mean=28
    
    # Perform one-way ANOVA
    f_statistic = None
    p_value = None
    
    # Calculate group means
    group_means = [np.mean(group1), np.mean(group2), np.mean(group3), np.mean(group4)]
    
    # TODO: Calculate effect size (eta-squared)
    # Combine all groups
    all_data = np.concatenate([group1, group2, group3, group4])
    group_labels = np.concatenate([
        np.repeat(0, len(group1)),
        np.repeat(1, len(group2)),
        np.repeat(2, len(group3)),
        np.repeat(3, len(group4))
    ])
    
    # Calculate sum of squares
    ss_between = None  # Sum of squares between groups
    ss_within = None   # Sum of squares within groups
    ss_total = None    # Total sum of squares
    
    # Calculate eta-squared (effect size)
    eta_squared = None
    
    # TODO: Post-hoc pairwise comparisons
    # Perform pairwise t-tests between all groups
    pairwise_results = {}
    groups = [group1, group2, group3, group4]
    group_names = ['Group1', 'Group2', 'Group3', 'Group4']
    
    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            t_stat, p_val = None, None  # Use stats.ttest_ind
            pairwise_results[f"{group_names[i]}_vs_{group_names[j]}"] = {
                't_statistic': t_stat,
                'p_value': p_val
            }
    
    # TODO: Bonferroni correction for multiple comparisons
    n_comparisons = len(pairwise_results)
    bonferroni_alpha = 0.05 / n_comparisons
    
    # Count significant comparisons before and after correction
    significant_before = None  # Count p < 0.05
    significant_after = None   # Count p < bonferroni_alpha
    
    # TODO: Two-way ANOVA simulation (simplified)
    # Create data with two factors
    factor_a_levels = 3  # Factor A has 3 levels
    factor_b_levels = 2  # Factor B has 2 levels
    n_per_cell = 10
    
    # Generate data for each combination
    two_way_data = []
    factor_a_labels = []
    factor_b_labels = []
    
    for a in range(factor_a_levels):
        for b in range(factor_b_levels):
            # Different means for different combinations
            cell_mean = 20 + 5*a + 3*b + 2*a*b  # Include interaction effect
            cell_data = np.random.normal(cell_mean, 3, n_per_cell)
            two_way_data.extend(cell_data)
            factor_a_labels.extend([a] * n_per_cell)
            factor_b_labels.extend([b] * n_per_cell)
    
    two_way_data = np.array(two_way_data)
    factor_a_labels = np.array(factor_a_labels)
    factor_b_labels = np.array(factor_b_labels)
    
    # Calculate means for each factor level
    factor_a_means = [np.mean(two_way_data[factor_a_labels == a]) for a in range(factor_a_levels)]
    factor_b_means = [np.mean(two_way_data[factor_b_labels == b]) for b in range(factor_b_levels)]
    
    return {
        'one_way_anova': {
            'f_statistic': f_statistic,
            'p_value': p_value,
            'group_means': group_means,
            'eta_squared': eta_squared,
            'ss_between': ss_between,
            'ss_within': ss_within,
            'ss_total': ss_total
        },
        'post_hoc_analysis': {
            'pairwise_results': pairwise_results,
            'bonferroni_alpha': bonferroni_alpha,
            'significant_before_correction': significant_before,
            'significant_after_correction': significant_after
        },
        'two_way_anova': {
            'factor_a_means': factor_a_means,
            'factor_b_means': factor_b_means,
            'data': two_way_data,
            'factor_a_labels': factor_a_labels,
            'factor_b_labels': factor_b_labels
        }
    }


# Test functions
def test_exercise_1():
    """Test descriptive statistics exercise"""
    try:
        results = exercise_1_descriptive_statistics()
        
        assert results['mean'] is not None, "Mean not calculated"
        assert results['median'] is not None, "Median not calculated"
        assert results['std_dev'] is not None, "Standard deviation not calculated"
        assert results['skewness'] is not None, "Skewness not calculated"
        assert results['percentiles'] is not None, "Percentiles not calculated"
        
        print("✓ Exercise 1 passed: Descriptive statistics")
        
    except Exception as e:
        print(f"❌ Exercise 1 failed: {e}")


def test_exercise_2():
    """Test probability distributions exercise"""
    try:
        results = exercise_2_probability_distributions()
        
        assert results['normal_analysis']['prob_less_than_85'] is not None, "Normal probability not calculated"
        assert results['binomial_analysis']['prob_exactly_5'] is not None, "Binomial probability not calculated"
        assert results['poisson_analysis']['prob_exactly_3'] is not None, "Poisson probability not calculated"
        assert results['normality_test']['p_value'] is not None, "Normality test not performed"
        
        print("✓ Exercise 2 passed: Probability distributions")
        
    except Exception as e:
        print(f"❌ Exercise 2 failed: {e}")


def test_exercise_3():
    """Test hypothesis testing exercise"""
    try:
        results = exercise_3_hypothesis_testing()
        
        assert results['one_sample_test']['t_statistic'] is not None, "One-sample t-test not performed"
        assert results['two_sample_test']['t_statistic'] is not None, "Two-sample t-test not performed"
        assert results['paired_test']['t_statistic'] is not None, "Paired t-test not performed"
        assert results['chi_square_test']['chi2_statistic'] is not None, "Chi-square test not performed"
        
        print("✓ Exercise 3 passed: Hypothesis testing")
        
    except Exception as e:
        print(f"❌ Exercise 3 failed: {e}")


def test_exercise_4():
    """Test correlation analysis exercise"""
    try:
        results = exercise_4_correlation_analysis()
        
        assert results['pearson_correlations']['strong_positive'] is not None, "Pearson correlation not calculated"
        assert results['spearman_correlations']['strong_positive'] is not None, "Spearman correlation not calculated"
        assert results['covariances']['strong_positive'] is not None, "Covariance not calculated"
        assert results['correlation_matrix'] is not None, "Correlation matrix not created"
        
        print("✓ Exercise 4 passed: Correlation analysis")
        
    except Exception as e:
        print(f"❌ Exercise 4 failed: {e}")


def test_exercise_5():
    """Test confidence intervals exercise"""
    try:
        results = exercise_5_confidence_intervals()
        
        assert results['mean_ci']['lower_bound'] is not None, "Mean CI not calculated"
        assert results['proportion_ci']['lower_bound'] is not None, "Proportion CI not calculated"
        assert results['bootstrap_ci']['lower_bound'] is not None, "Bootstrap CI not calculated"
        assert results['prediction_interval']['lower_bound'] is not None, "Prediction interval not calculated"
        
        print("✓ Exercise 5 passed: Confidence intervals")
        
    except Exception as e:
        print(f"❌ Exercise 5 failed: {e}")


def test_exercise_6():
    """Test regression analysis exercise"""
    try:
        results = exercise_6_regression_analysis()
        
        assert results['simple_regression']['slope'] is not None, "Simple regression not performed"
        assert results['multiple_regression']['coefficients'] is not None, "Multiple regression not performed"
        assert results['simple_regression']['r_squared'] is not None, "R-squared not calculated"
        assert results['diagnostics']['durbin_watson'] is not None, "Diagnostics not calculated"
        
        print("✓ Exercise 6 passed: Regression analysis")
        
    except Exception as e:
        print(f"❌ Exercise 6 failed: {e}")


def test_exercise_7():
    """Test ANOVA exercise"""
    try:
        results = exercise_7_anova()
        
        assert results['one_way_anova']['f_statistic'] is not None, "One-way ANOVA not performed"
        assert results['one_way_anova']['eta_squared'] is not None, "Effect size not calculated"
        assert results['post_hoc_analysis']['pairwise_results'], "Post-hoc analysis not performed"
        assert results['two_way_anova']['factor_a_means'] is not None, "Two-way ANOVA not performed"
        
        print("✓ Exercise 7 passed: ANOVA")
        
    except Exception as e:
        print(f"❌ Exercise 7 failed: {e}")


def run_all_tests():
    """Run all exercise tests"""
    print("Running Statistical Analysis Exercises Tests...\n")
    
    test_exercise_1()
    test_exercise_2()
    test_exercise_3()
    test_exercise_4()
    test_exercise_5()
    test_exercise_6()
    test_exercise_7()
    
    print("\n🎉 All statistical analysis exercises completed!")
    print("\nKey concepts mastered:")
    print("- Descriptive statistics and data summarization")
    print("- Probability distributions and calculations")
    print("- Hypothesis testing and significance")
    print("- Correlation and covariance analysis")
    print("- Confidence intervals and uncertainty")
    print("- Linear regression and model evaluation")
    print("- ANOVA and group comparisons")


if __name__ == "__main__":
    run_all_tests()