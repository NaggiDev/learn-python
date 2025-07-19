"""
Statistical Analysis Exercises - Solutions

This file contains complete solutions for all statistical analysis exercises.
These solutions demonstrate comprehensive statistical analysis techniques using Python.
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
    Exercise 1: Descriptive Statistics - SOLUTION
    """
    # Generate sample data
    np.random.seed(42)
    data = np.random.gamma(2, 2, 1000)  # Gamma distribution for interesting shape
    
    # Calculate measures of central tendency
    mean_val = np.mean(data)
    median_val = np.median(data)
    mode_result = stats.mode(data, keepdims=True)
    mode_val = mode_result.mode[0]
    
    # Calculate measures of variability
    range_val = np.max(data) - np.min(data)
    variance_val = np.var(data, ddof=1)  # Sample variance
    std_dev_val = np.std(data, ddof=1)   # Sample std dev
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr_val = q3 - q1
    
    # Calculate distribution shape
    skewness_val = stats.skew(data)
    kurtosis_val = stats.kurtosis(data)
    
    # Calculate percentiles
    percentiles = [5, 10, 25, 50, 75, 90, 95]
    percentile_values = np.percentile(data, percentiles)
    
    # Create five-number summary
    five_number_summary = {
        'min': np.min(data),
        'q1': q1,
        'median': median_val,
        'q3': q3,
        'max': np.max(data)
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
        'percentiles': dict(zip(percentiles, percentile_values)),
        'five_number_summary': five_number_summary
    }


def exercise_2_probability_distributions():
    """
    Exercise 2: Probability Distributions - SOLUTION
    """
    np.random.seed(42)
    
    # Normal distribution analysis
    mu, sigma = 100, 15
    
    # Calculate probabilities
    prob_less_than_85 = stats.norm.cdf(85, mu, sigma)
    prob_between_90_110 = stats.norm.cdf(110, mu, sigma) - stats.norm.cdf(90, mu, sigma)
    prob_greater_than_130 = 1 - stats.norm.cdf(130, mu, sigma)
    
    # Calculate critical values
    value_at_95th_percentile = stats.norm.ppf(0.95, mu, sigma)
    value_at_5th_percentile = stats.norm.ppf(0.05, mu, sigma)
    
    # Binomial distribution
    n_trials, p_success = 20, 0.3
    
    # Calculate probabilities
    prob_exactly_5_successes = stats.binom.pmf(5, n_trials, p_success)
    prob_at_most_8_successes = stats.binom.cdf(8, n_trials, p_success)
    prob_at_least_10_successes = 1 - stats.binom.cdf(9, n_trials, p_success)
    
    # Calculate expected value and variance
    binomial_mean = n_trials * p_success
    binomial_variance = n_trials * p_success * (1 - p_success)
    
    # Poisson distribution
    lambda_param = 4
    
    # Calculate probabilities
    prob_exactly_3_events = stats.poisson.pmf(3, lambda_param)
    prob_less_than_2_events = stats.poisson.cdf(1, lambda_param)
    prob_more_than_6_events = 1 - stats.poisson.cdf(6, lambda_param)
    
    # Distribution fitting
    sample_data = np.random.normal(50, 10, 200)
    
    # Perform Shapiro-Wilk normality test
    shapiro_statistic, shapiro_p_value = stats.shapiro(sample_data)
    is_normal = shapiro_p_value > 0.05
    
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
    Exercise 3: Hypothesis Testing - SOLUTION
    """
    np.random.seed(42)
    
    # One-sample t-test
    sample = np.random.normal(52, 8, 25)
    hypothesized_mean = 50
    
    one_sample_t_stat, one_sample_p_value = stats.ttest_1samp(sample, hypothesized_mean)
    one_sample_reject_null = one_sample_p_value < 0.05
    
    # Two-sample t-test (independent samples)
    group1 = np.random.normal(100, 15, 30)
    group2 = np.random.normal(105, 15, 30)
    
    two_sample_t_stat, two_sample_p_value = stats.ttest_ind(group1, group2)
    two_sample_reject_null = two_sample_p_value < 0.05
    
    # Calculate effect size (Cohen's d)
    pooled_std = np.sqrt(((len(group1)-1)*np.var(group1, ddof=1) + 
                         (len(group2)-1)*np.var(group2, ddof=1)) / 
                         (len(group1) + len(group2) - 2))
    cohens_d = (np.mean(group2) - np.mean(group1)) / pooled_std
    
    # Paired t-test
    before = np.random.normal(80, 10, 20)
    after = before + np.random.normal(5, 3, 20)
    
    paired_t_stat, paired_p_value = stats.ttest_rel(before, after)
    paired_reject_null = paired_p_value < 0.05
    
    # Chi-square test of independence
    observed = np.array([[20, 30, 25],   # Male preferences
                        [25, 20, 30]])   # Female preferences
    
    chi2_stat, chi2_p_value, chi2_dof, chi2_expected = stats.chi2_contingency(observed)
    chi2_reject_null = chi2_p_value < 0.05
    
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
    Exercise 4: Correlation and Covariance Analysis - SOLUTION
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
    
    # Calculate Pearson correlations
    pearson_corr_1, _ = stats.pearsonr(x1, y1)
    pearson_corr_2, _ = stats.pearsonr(x2, y2)
    pearson_corr_3, _ = stats.pearsonr(x3, y3)
    pearson_corr_4, _ = stats.pearsonr(x4, y4)
    
    # Calculate Spearman correlations (rank-based)
    spearman_corr_1, _ = stats.spearmanr(x1, y1)
    spearman_corr_2, _ = stats.spearmanr(x2, y2)
    spearman_corr_3, _ = stats.spearmanr(x3, y3)
    spearman_corr_4, _ = stats.spearmanr(x4, y4)
    
    # Calculate covariances
    covariance_1 = np.cov(x1, y1)[0, 1]
    covariance_2 = np.cov(x2, y2)[0, 1]
    covariance_3 = np.cov(x3, y3)[0, 1]
    covariance_4 = np.cov(x4, y4)[0, 1]
    
    # Test correlation significance (for x1, y1)
    corr_test_statistic, corr_test_p_value = stats.pearsonr(x1, y1)
    corr_is_significant = corr_test_p_value < 0.05
    
    # Create correlation matrix
    data_matrix = np.column_stack([x1, y1, x2, y2])
    correlation_matrix = np.corrcoef(data_matrix.T)
    
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
    Exercise 5: Confidence Intervals - SOLUTION
    """
    np.random.seed(42)
    
    # Confidence interval for mean
    sample = np.random.normal(75, 12, 40)
    
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    n = len(sample)
    
    # 95% confidence interval for mean
    confidence_level = 0.95
    alpha = 1 - confidence_level
    t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
    
    margin_of_error = t_critical * (sample_std / np.sqrt(n))
    ci_mean_lower = sample_mean - margin_of_error
    ci_mean_upper = sample_mean + margin_of_error
    
    # Confidence interval for proportion
    successes = 65
    n_trials = 100
    sample_proportion = successes / n_trials
    
    # 95% confidence interval for proportion
    z_critical = stats.norm.ppf(0.975)  # 97.5th percentile for 95% CI
    
    # Standard error for proportion
    se_proportion = np.sqrt(sample_proportion * (1 - sample_proportion) / n_trials)
    ci_prop_lower = sample_proportion - z_critical * se_proportion
    ci_prop_upper = sample_proportion + z_critical * se_proportion
    
    # Bootstrap confidence intervals
    def bootstrap_mean(data, n_bootstrap=1000):
        bootstrap_means = []
        n = len(data)
        
        for _ in range(n_bootstrap):
            bootstrap_sample = np.random.choice(data, size=n, replace=True)
            bootstrap_means.append(np.mean(bootstrap_sample))
        
        return np.array(bootstrap_means)
    
    bootstrap_means = bootstrap_mean(sample)
    
    # Calculate percentile confidence interval
    ci_boot_lower = np.percentile(bootstrap_means, 2.5)
    ci_boot_upper = np.percentile(bootstrap_means, 97.5)
    
    # Prediction interval (simplified)
    x_reg = np.random.uniform(0, 10, 50)
    y_reg = 2 * x_reg + 1 + np.random.normal(0, 1, 50)
    
    # Fit simple linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_reg, y_reg)
    
    # Predict for new value
    x_new = 5.0
    y_pred = slope * x_new + intercept
    
    # Calculate prediction interval
    residuals = y_reg - (slope * x_reg + intercept)
    mse = np.mean(residuals**2)
    
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
    Exercise 6: Linear Regression Analysis - SOLUTION
    """
    np.random.seed(42)
    
    # Simple linear regression
    n = 100
    x = np.random.uniform(0, 10, n)
    y = 3 * x + 2 + np.random.normal(0, 2, n)
    
    # Perform simple linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Calculate R-squared
    r_squared = r_value**2
    
    # Calculate predictions and residuals
    y_pred = slope * x + intercept
    residuals = y - y_pred
    
    # Multiple linear regression
    x1 = np.random.randn(n)
    x2 = np.random.randn(n)
    x3 = np.random.randn(n)
    y_multi = 2*x1 + 3*x2 - 1*x3 + 5 + np.random.normal(0, 1, n)
    
    # Create design matrix (add intercept column)
    X = np.column_stack([np.ones(n), x1, x2, x3])  # n x 4 matrix
    
    # Calculate coefficients using normal equation
    coefficients = np.linalg.inv(X.T @ X) @ X.T @ y_multi
    
    # Calculate predictions
    y_multi_pred = X @ coefficients
    
    # Calculate R-squared for multiple regression
    ss_res = np.sum((y_multi - y_multi_pred) ** 2)
    ss_tot = np.sum((y_multi - np.mean(y_multi)) ** 2)
    r_squared_multi = 1 - (ss_res / ss_tot)
    
    # Regression diagnostics
    # Mean Squared Error
    mse_simple = np.mean(residuals**2)
    mse_multi = np.mean((y_multi - y_multi_pred)**2)
    
    # Mean Absolute Error
    mae_simple = np.mean(np.abs(residuals))
    mae_multi = np.mean(np.abs(y_multi - y_multi_pred))
    
    # Durbin-Watson test for autocorrelation
    def durbin_watson(residuals):
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
    Exercise 7: Analysis of Variance (ANOVA) - SOLUTION
    """
    np.random.seed(42)
    
    # One-way ANOVA
    group1 = np.random.normal(20, 5, 30)
    group2 = np.random.normal(25, 5, 30)
    group3 = np.random.normal(22, 5, 30)
    group4 = np.random.normal(28, 5, 30)
    
    # Perform one-way ANOVA
    f_statistic, p_value = stats.f_oneway(group1, group2, group3, group4)
    
    # Calculate group means
    group_means = [np.mean(group1), np.mean(group2), np.mean(group3), np.mean(group4)]
    
    # Calculate effect size (eta-squared)
    all_data = np.concatenate([group1, group2, group3, group4])
    group_labels = np.concatenate([
        np.repeat(0, len(group1)),
        np.repeat(1, len(group2)),
        np.repeat(2, len(group3)),
        np.repeat(3, len(group4))
    ])
    
    # Calculate sum of squares
    grand_mean = np.mean(all_data)
    
    # Between groups sum of squares
    ss_between = sum([len(group) * (np.mean(group) - grand_mean)**2 
                     for group in [group1, group2, group3, group4]])
    
    # Within groups sum of squares
    ss_within = sum([np.sum((group - np.mean(group))**2) 
                    for group in [group1, group2, group3, group4]])
    
    # Total sum of squares
    ss_total = np.sum((all_data - grand_mean)**2)
    
    # Calculate eta-squared
    eta_squared = ss_between / ss_total
    
    # Post-hoc pairwise comparisons
    pairwise_results = {}
    groups = [group1, group2, group3, group4]
    group_names = ['Group1', 'Group2', 'Group3', 'Group4']
    
    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            t_stat, p_val = stats.ttest_ind(groups[i], groups[j])
            pairwise_results[f"{group_names[i]}_vs_{group_names[j]}"] = {
                't_statistic': t_stat,
                'p_value': p_val
            }
    
    # Bonferroni correction
    n_comparisons = len(pairwise_results)
    bonferroni_alpha = 0.05 / n_comparisons
    
    # Count significant comparisons
    significant_before = sum(1 for result in pairwise_results.values() 
                           if result['p_value'] < 0.05)
    significant_after = sum(1 for result in pairwise_results.values() 
                          if result['p_value'] < bonferroni_alpha)
    
    # Two-way ANOVA simulation
    factor_a_levels = 3
    factor_b_levels = 2
    n_per_cell = 10
    
    two_way_data = []
    factor_a_labels = []
    factor_b_labels = []
    
    for a in range(factor_a_levels):
        for b in range(factor_b_levels):
            cell_mean = 20 + 5*a + 3*b + 2*a*b
            cell_data = np.random.normal(cell_mean, 3, n_per_cell)
            two_way_data.extend(cell_data)
            factor_a_labels.extend([a] * n_per_cell)
            factor_b_labels.extend([b] * n_per_cell)
    
    two_way_data = np.array(two_way_data)
    factor_a_labels = np.array(factor_a_labels)
    factor_b_labels = np.array(factor_b_labels)
    
    # Calculate means for each factor level
    factor_a_means = [np.mean(two_way_data[factor_a_labels == a]) 
                     for a in range(factor_a_levels)]
    factor_b_means = [np.mean(two_way_data[factor_b_labels == b]) 
                     for b in range(factor_b_levels)]
    
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


# Demonstration function
def demonstrate_statistical_solutions():
    """
    Demonstrate all statistical analysis solutions
    """
    print("Statistical Analysis Solutions - Demonstration")
    print("=" * 60)
    
    print("\n1. Descriptive Statistics:")
    results1 = exercise_1_descriptive_statistics()
    print(f"Mean: {results1['mean']:.3f}")
    print(f"Median: {results1['median']:.3f}")
    print(f"Standard Deviation: {results1['std_dev']:.3f}")
    print(f"Skewness: {results1['skewness']:.3f}")
    
    print("\n2. Probability Distributions:")
    results2 = exercise_2_probability_distributions()
    print(f"P(X < 85) for Normal(100,15): {results2['normal_analysis']['prob_less_than_85']:.3f}")
    print(f"Binomial mean (n=20, p=0.3): {results2['binomial_analysis']['mean']:.1f}")
    print(f"Normality test p-value: {results2['normality_test']['p_value']:.3f}")
    
    print("\n3. Hypothesis Testing:")
    results3 = exercise_3_hypothesis_testing()
    print(f"One-sample t-test p-value: {results3['one_sample_test']['p_value']:.3f}")
    print(f"Two-sample t-test Cohen's d: {results3['two_sample_test']['cohens_d']:.3f}")
    print(f"Chi-square test p-value: {results3['chi_square_test']['p_value']:.3f}")
    
    print("\n4. Correlation Analysis:")
    results4 = exercise_4_correlation_analysis()
    print(f"Strong positive Pearson r: {results4['pearson_correlations']['strong_positive']:.3f}")
    print(f"Non-linear Spearman r: {results4['spearman_correlations']['non_linear']:.3f}")
    
    print("\n5. Confidence Intervals:")
    results5 = exercise_5_confidence_intervals()
    mean_ci = results5['mean_ci']
    print(f"95% CI for mean: [{mean_ci['lower_bound']:.2f}, {mean_ci['upper_bound']:.2f}]")
    
    print("\n6. Regression Analysis:")
    results6 = exercise_6_regression_analysis()
    simple_reg = results6['simple_regression']
    print(f"Simple regression R²: {simple_reg['r_squared']:.3f}")
    print(f"Multiple regression R²: {results6['multiple_regression']['r_squared']:.3f}")
    
    print("\n7. ANOVA:")
    results7 = exercise_7_anova()
    anova_results = results7['one_way_anova']
    print(f"One-way ANOVA F-statistic: {anova_results['f_statistic']:.3f}")
    print(f"Effect size (η²): {anova_results['eta_squared']:.3f}")
    
    print("\n" + "=" * 60)
    print("All statistical analysis solutions demonstrated successfully!")


if __name__ == "__main__":
    demonstrate_statistical_solutions()