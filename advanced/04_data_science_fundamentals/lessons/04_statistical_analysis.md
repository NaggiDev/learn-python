# Basic Statistical Analysis: Descriptive and Inferential Statistics

## Introduction

Statistics is the science of collecting, analyzing, interpreting, and presenting data. In data science, statistical analysis helps us:

- **Understand data patterns** and distributions
- **Make inferences** about populations from samples
- **Test hypotheses** and validate assumptions
- **Quantify uncertainty** and confidence in results
- **Make data-driven decisions** with measurable confidence

Python provides powerful libraries for statistical analysis, including NumPy, SciPy, and specialized packages like statsmodels.

## Types of Statistics

### Descriptive Statistics
Descriptive statistics summarize and describe the main features of a dataset:
- **Central tendency**: Mean, median, mode
- **Variability**: Range, variance, standard deviation
- **Distribution shape**: Skewness, kurtosis
- **Relationships**: Correlation, covariance

### Inferential Statistics
Inferential statistics make predictions or inferences about a population based on sample data:
- **Hypothesis testing**: Testing claims about populations
- **Confidence intervals**: Estimating population parameters
- **Regression analysis**: Modeling relationships between variables
- **ANOVA**: Comparing means across groups

## Descriptive Statistics

### Measures of Central Tendency

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
np.random.seed(42)
data = np.random.normal(100, 15, 1000)  # Normal distribution, mean=100, std=15

# Mean (arithmetic average)
mean_value = np.mean(data)
print(f"Mean: {mean_value:.2f}")

# Median (middle value)
median_value = np.median(data)
print(f"Median: {median_value:.2f}")

# Mode (most frequent value)
mode_result = stats.mode(data, keepdims=True)
mode_value = mode_result.mode[0]
print(f"Mode: {mode_value:.2f}")
```

### Measures of Variability

```python
# Range
data_range = np.max(data) - np.min(data)
print(f"Range: {data_range:.2f}")

# Variance and Standard deviation
variance = np.var(data, ddof=1)  # ddof=1 for sample variance
std_dev = np.std(data, ddof=1)
print(f"Variance: {variance:.2f}")
print(f"Standard deviation: {std_dev:.2f}")

# Interquartile range (IQR)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
print(f"IQR: {iqr:.2f}")
```

### Distribution Shape

```python
# Skewness (asymmetry of distribution)
skewness = stats.skew(data)
print(f"Skewness: {skewness:.3f}")

# Kurtosis (tail heaviness)
kurt = stats.kurtosis(data)
print(f"Kurtosis: {kurt:.3f}")
```

## Probability Distributions

### Normal Distribution

```python
# Normal distribution parameters
mu, sigma = 100, 15

# Generate data and plot
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
y = stats.norm.pdf(x, mu, sigma)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label=f'Normal(μ={mu}, σ={sigma})')
plt.fill_between(x, y, alpha=0.3)
plt.axvline(mu, color='red', linestyle='--', label='Mean')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## Correlation and Covariance

### Correlation Analysis

```python
# Generate correlated data
np.random.seed(42)
n = 100
x1 = np.random.randn(n)
y1 = 2 * x1 + np.random.randn(n) * 0.5  # Strong positive correlation

# Calculate correlation
corr1 = np.corrcoef(x1, y1)[0, 1]
print(f"Correlation coefficient: {corr1:.3f}")

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(x1, y1, alpha=0.7)
plt.title(f'Correlation Example (r = {corr1:.3f})')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)
plt.show()
```

## Hypothesis Testing

### One-Sample t-test

```python
# Test if sample mean differs significantly from a hypothesized value
np.random.seed(42)
sample = np.random.normal(105, 15, 30)  # Sample with true mean = 105

# Null hypothesis: μ = 100
hypothesized_mean = 100
t_statistic, p_value = stats.ttest_1samp(sample, hypothesized_mean)

print(f"One-Sample t-test:")
print(f"Sample mean: {np.mean(sample):.2f}")
print(f"Hypothesized mean: {hypothesized_mean}")
print(f"t-statistic: {t_statistic:.3f}")
print(f"p-value: {p_value:.3f}")

alpha = 0.05
if p_value < alpha:
    print(f"Reject null hypothesis (p < {alpha})")
else:
    print(f"Fail to reject null hypothesis (p ≥ {alpha})")
```

### Two-Sample t-test

```python
# Compare means of two independent groups
np.random.seed(42)
group1 = np.random.normal(100, 15, 30)
group2 = np.random.normal(110, 15, 30)

t_stat, p_val = stats.ttest_ind(group1, group2)

print(f"Two-Sample t-test:")
print(f"Group 1 mean: {np.mean(group1):.2f}")
print(f"Group 2 mean: {np.mean(group2):.2f}")
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_val:.3f}")

if p_val < alpha:
    print("Significant difference between group means")
else:
    print("No significant difference between group means")
```

## Confidence Intervals

### Confidence Interval for Mean

```python
# Calculate confidence interval for population mean
np.random.seed(42)
sample = np.random.normal(100, 15, 50)

sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
n = len(sample)

# 95% confidence interval
confidence_level = 0.95
alpha = 1 - confidence_level
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)

margin_of_error = t_critical * (sample_std / np.sqrt(n))
ci_lower = sample_mean - margin_of_error
ci_upper = sample_mean + margin_of_error

print(f"95% Confidence Interval: [{ci_lower:.2f}, {ci_upper:.2f}]")
print(f"We are 95% confident that the true population mean")
print(f"lies between {ci_lower:.2f} and {ci_upper:.2f}")
```

## Linear Regression

### Simple Linear Regression

```python
# Simple linear regression
np.random.seed(42)
n = 100
x = np.random.uniform(0, 10, n)
y = 2 * x + 1 + np.random.normal(0, 2, n)  # y = 2x + 1 + noise

# Calculate regression coefficients
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f"Simple Linear Regression:")
print(f"Slope: {slope:.3f}")
print(f"Intercept: {intercept:.3f}")
print(f"R-squared: {r_value**2:.3f}")
print(f"p-value: {p_value:.3e}")

# Plot
y_pred = slope * x + intercept
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, label='Data points')
plt.plot(x, y_pred, 'r-', linewidth=2, 
         label=f'Regression line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## Analysis of Variance (ANOVA)

### One-Way ANOVA

```python
# Compare means across multiple groups
np.random.seed(42)
group_a = np.random.normal(100, 15, 30)
group_b = np.random.normal(110, 15, 30)
group_c = np.random.normal(105, 15, 30)

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(group_a, group_b, group_c)

print(f"One-Way ANOVA:")
print(f"F-statistic: {f_statistic:.3f}")
print(f"p-value: {p_value:.3f}")

if p_value < 0.05:
    print("At least one group mean is significantly different")
else:
    print("No significant difference between group means")
```

## Practical Statistical Analysis

### Complete Analysis Function

```python
def statistical_summary(data):
    """Perform comprehensive statistical analysis"""
    print("Statistical Summary")
    print("=" * 40)
    
    # Basic statistics
    print(f"Count: {len(data)}")
    print(f"Mean: {np.mean(data):.3f}")
    print(f"Median: {np.median(data):.3f}")
    print(f"Std Dev: {np.std(data, ddof=1):.3f}")
    print(f"Min: {np.min(data):.3f}")
    print(f"Max: {np.max(data):.3f}")
    
    # Distribution properties
    print(f"Skewness: {stats.skew(data):.3f}")
    print(f"Kurtosis: {stats.kurtosis(data):.3f}")
    
    # Normality test
    if len(data) >= 8:
        stat, p_val = stats.shapiro(data[:5000])  # Limit sample size
        print(f"Normality test p-value: {p_val:.3f}")
        if p_val > 0.05:
            print("Data appears normally distributed")
        else:
            print("Data does not appear normally distributed")

# Example usage
np.random.seed(42)
sample_data = np.random.normal(100, 15, 200)
statistical_summary(sample_data)
```

## Best Practices

### Key Guidelines

1. **Always visualize your data** before applying statistical tests
2. **Check assumptions** (normality, independence, equal variances)
3. **Consider effect sizes** along with p-values
4. **Account for multiple comparisons** when appropriate
5. **Report confidence intervals** to show uncertainty
6. **Use appropriate sample sizes** for reliable results

### Common Pitfalls to Avoid

- Confusing statistical significance with practical significance
- Ignoring assumptions of statistical tests
- Multiple testing without correction
- Cherry-picking results
- Correlation vs. causation confusion

## Summary

Statistical analysis provides the foundation for making data-driven decisions:

### Key Concepts Covered
- **Descriptive statistics**: Summarizing data characteristics
- **Probability distributions**: Understanding data patterns
- **Hypothesis testing**: Making inferences with confidence
- **Correlation analysis**: Measuring relationships
- **Regression**: Modeling relationships between variables
- **ANOVA**: Comparing multiple groups

### Applications
- A/B testing and experimental design
- Quality control and process improvement
- Market research and analysis
- Scientific research validation
- Risk assessment and decision making

Understanding these statistical concepts enables you to analyze data rigorously and communicate findings with appropriate confidence levels.

## Next Steps

In the next section, we'll apply all the concepts learned in this module through a comprehensive mini-project that demonstrates the complete data science workflow.