# Data Visualization: Creating Effective Visualizations with Matplotlib and Seaborn

## Introduction

Data visualization is the graphical representation of information and data. It's a crucial skill in data science because it allows us to:

- **Explore data** and discover patterns
- **Communicate insights** effectively
- **Tell stories** with data
- **Make data accessible** to non-technical audiences
- **Support decision-making** with visual evidence

Python offers powerful libraries for data visualization, with Matplotlib as the foundational library and Seaborn providing high-level statistical visualizations.

## Why Visualization Matters

### The Power of Visual Communication

Human brains process visual information much faster than text or numbers. A well-designed visualization can:

- Reveal patterns that aren't obvious in raw data
- Highlight outliers and anomalies
- Show relationships between variables
- Communicate complex information quickly
- Make data memorable and engaging

### Anscombe's Quartet

A famous example demonstrating the importance of visualization is Anscombe's Quartet - four datasets with nearly identical statistical properties but very different distributions when plotted.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Anscombe's Quartet data
anscombe = sns.load_dataset("anscombe")

# Create subplots for each dataset
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
datasets = ['I', 'II', 'III', 'IV']

for i, dataset in enumerate(datasets):
    row, col = i // 2, i % 2
    data = anscombe[anscombe.dataset == dataset]
    
    axes[row, col].scatter(data.x, data.y)
    axes[row, col].plot(np.unique(data.x), 
                       np.poly1d(np.polyfit(data.x, data.y, 1))(np.unique(data.x)), 'r--')
    axes[row, col].set_title(f'Dataset {dataset}')
    axes[row, col].set_xlabel('X')
    axes[row, col].set_ylabel('Y')

plt.tight_layout()
plt.show()
```

## Matplotlib Fundamentals

Matplotlib is the foundation of Python data visualization. It provides fine-grained control over every aspect of a plot.

### Basic Plotting

```python
import matplotlib.pyplot as plt
import numpy as np

# Basic line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()
```

### Figure and Axes Architecture

Understanding Matplotlib's architecture is crucial for creating complex visualizations:

```python
# Create figure and axes explicitly
fig, ax = plt.subplots(figsize=(10, 6))

# Plot on the axes
ax.plot(x, y, label='sin(x)', linewidth=2)
ax.plot(x, np.cos(x), label='cos(x)', linewidth=2, linestyle='--')

# Customize the axes
ax.set_title('Trigonometric Functions', fontsize=16)
ax.set_xlabel('X values', fontsize=12)
ax.set_ylabel('Y values', fontsize=12)
ax.legend()
ax.grid(True, alpha=0.3)

plt.show()
```

### Multiple Subplots

```python
# Create multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Different plot types
x = np.linspace(0, 10, 50)

# Line plot
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Line Plot')

# Scatter plot
axes[0, 1].scatter(x, np.cos(x), alpha=0.6)
axes[0, 1].set_title('Scatter Plot')

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
axes[1, 0].bar(categories, values)
axes[1, 0].set_title('Bar Plot')

# Histogram
data = np.random.normal(0, 1, 1000)
axes[1, 1].hist(data, bins=30, alpha=0.7)
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()
```

### Customization Options

```python
# Comprehensive customization example
fig, ax = plt.subplots(figsize=(12, 8))

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Plot with different styles
ax.plot(x, y1, color='blue', linewidth=2, linestyle='-', marker='o', 
        markersize=4, markevery=10, label='sin(x)')
ax.plot(x, y2, color='red', linewidth=2, linestyle='--', marker='s', 
        markersize=4, markevery=10, label='cos(x)')
ax.plot(x, y3, color='green', linewidth=2, linestyle=':', marker='^', 
        markersize=4, markevery=10, label='sin(x)cos(x)')

# Customize appearance
ax.set_title('Trigonometric Functions Comparison', fontsize=18, fontweight='bold')
ax.set_xlabel('X values', fontsize=14)
ax.set_ylabel('Y values', fontsize=14)
ax.legend(fontsize=12, loc='upper right')
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)

# Set axis limits and ticks
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(-1.5, 2, 0.5))

# Add annotations
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(2, 1.3),
            arrowprops=dict(arrowstyle='->', color='black'),
            fontsize=12, ha='center')

plt.tight_layout()
plt.show()
```

## Common Plot Types

### 1. Line Plots

Best for showing trends over time or continuous data:

```python
# Time series example
dates = pd.date_range('2023-01-01', periods=365, freq='D')
stock_price = 100 + np.cumsum(np.random.randn(365) * 0.5)

plt.figure(figsize=(12, 6))
plt.plot(dates, stock_price, linewidth=1.5)
plt.title('Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 2. Scatter Plots

Best for showing relationships between two continuous variables:

```python
# Correlation example
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure(figsize=(10, 8))
plt.scatter(x, y, alpha=0.6, s=50)
plt.title('Scatter Plot with Correlation')
plt.xlabel('X Variable')
plt.ylabel('Y Variable')

# Add trend line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2)

plt.grid(True, alpha=0.3)
plt.show()
```

### 3. Bar Charts

Best for comparing categories:

```python
# Categorical data comparison
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales_q1 = [23, 45, 56, 78, 32]
sales_q2 = [34, 52, 48, 82, 28]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 8))
bars1 = ax.bar(x - width/2, sales_q1, width, label='Q1', alpha=0.8)
bars2 = ax.bar(x + width/2, sales_q2, width, label='Q2', alpha=0.8)

ax.set_xlabel('Products')
ax.set_ylabel('Sales (thousands)')
ax.set_title('Quarterly Sales Comparison')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Add value labels on bars
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height}', ha='center', va='bottom')

add_value_labels(bars1)
add_value_labels(bars2)

plt.tight_layout()
plt.show()
```

### 4. Histograms

Best for showing distribution of a single variable:

```python
# Distribution analysis
np.random.seed(42)
data1 = np.random.normal(100, 15, 1000)
data2 = np.random.normal(120, 20, 1000)

plt.figure(figsize=(12, 8))
plt.hist(data1, bins=30, alpha=0.7, label='Group A', density=True)
plt.hist(data2, bins=30, alpha=0.7, label='Group B', density=True)

plt.title('Distribution Comparison')
plt.xlabel('Values')
plt.ylabel('Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 5. Box Plots

Best for showing distribution summary and outliers:

```python
# Box plot for multiple groups
data = [np.random.normal(100, 15, 100),
        np.random.normal(110, 20, 100),
        np.random.normal(95, 10, 100),
        np.random.normal(105, 25, 100)]

plt.figure(figsize=(10, 8))
box_plot = plt.boxplot(data, labels=['Group A', 'Group B', 'Group C', 'Group D'],
                      patch_artist=True)

# Customize box colors
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Distribution Comparison with Box Plots')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)
plt.show()
```

## Seaborn: Statistical Data Visualization

Seaborn builds on Matplotlib to provide high-level statistical visualizations with attractive default styles.

### Setting Up Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

# Load sample dataset
tips = sns.load_dataset("tips")
print(tips.head())
```

### Distribution Plots

```python
# Distribution visualization
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Histogram with KDE
sns.histplot(data=tips, x="total_bill", kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Total Bill')

# Box plot by category
sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[0, 1])
axes[0, 1].set_title('Total Bill by Day')

# Violin plot (combines box plot and KDE)
sns.violinplot(data=tips, x="day", y="total_bill", ax=axes[1, 0])
axes[1, 0].set_title('Total Bill Distribution by Day')

# Strip plot with jitter
sns.stripplot(data=tips, x="day", y="total_bill", size=4, alpha=0.7, ax=axes[1, 1])
axes[1, 1].set_title('Total Bill Points by Day')

plt.tight_layout()
plt.show()
```

### Relationship Plots

```python
# Relationship visualization
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Scatter plot with regression line
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", ax=axes[0, 0])
sns.regplot(data=tips, x="total_bill", y="tip", scatter=False, ax=axes[0, 0])
axes[0, 0].set_title('Tip vs Total Bill')

# Correlation heatmap
correlation_matrix = tips.select_dtypes(include=[np.number]).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=axes[0, 1])
axes[0, 1].set_title('Correlation Matrix')

# Pair plot (relationships between all numeric variables)
# Note: This creates a separate figure
sns.pairplot(tips, hue="time", diag_kind="kde")
plt.show()

# Categorical relationships
sns.catplot(data=tips, x="day", y="total_bill", hue="sex", kind="bar", height=6, aspect=1.2)
plt.title('Average Total Bill by Day and Gender')
plt.show()
```

### Advanced Seaborn Plots

```python
# Advanced statistical plots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Joint plot showing both scatter and distributions
# Note: This creates a separate figure
g = sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg", height=8)
g.fig.suptitle('Joint Distribution: Total Bill vs Tip', y=1.02)
plt.show()

# Facet grid for multiple subplots
g = sns.FacetGrid(tips, col="time", row="sex", height=4, aspect=1.2)
g.map(sns.scatterplot, "total_bill", "tip", alpha=0.7)
g.add_legend()
plt.show()

# Cluster map
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot("month", "year", "passengers")
sns.clustermap(flights_pivot, cmap="viridis", figsize=(12, 8))
plt.show()
```

## Advanced Visualization Techniques

### 1. Subplots with Different Scales

```python
# Multiple y-axes
fig, ax1 = plt.subplots(figsize=(12, 8))

# First y-axis
x = np.arange(1, 13)
sales = [100, 120, 140, 110, 160, 180, 200, 190, 220, 240, 210, 250]
ax1.plot(x, sales, 'b-', marker='o', linewidth=2, markersize=6)
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales (thousands)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Second y-axis
ax2 = ax1.twinx()
profit_margin = [15, 18, 20, 16, 22, 25, 28, 26, 30, 32, 29, 35]
ax2.plot(x, profit_margin, 'r-', marker='s', linewidth=2, markersize=6)
ax2.set_ylabel('Profit Margin (%)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Sales and Profit Margin Over Time')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 2. 3D Plotting

```python
from mpl_toolkits.mplot3d import Axes3D

# 3D surface plot
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Create data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create surface plot
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot')

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
```

### 3. Animation

```python
from matplotlib.animation import FuncAnimation

# Animated line plot
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Animated Sine Wave')
ax.grid(True)

def animate(frame):
    line.set_ydata(np.sin(x + frame/10))
    return line,

# Create animation
anim = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# To save as GIF (requires pillow or imageio)
# anim.save('sine_wave.gif', writer='pillow', fps=20)

plt.show()
```

## Best Practices for Data Visualization

### 1. Choose the Right Chart Type

```python
# Chart type selection guide
chart_guide = {
    'Comparison': ['Bar Chart', 'Column Chart', 'Radar Chart'],
    'Composition': ['Pie Chart', 'Stacked Bar', 'Area Chart'],
    'Distribution': ['Histogram', 'Box Plot', 'Violin Plot'],
    'Relationship': ['Scatter Plot', 'Line Chart', 'Heatmap'],
    'Trend': ['Line Chart', 'Area Chart', 'Slope Graph']
}

for purpose, charts in chart_guide.items():
    print(f"{purpose}: {', '.join(charts)}")
```

### 2. Color Usage

```python
# Effective color usage
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Sequential colors for ordered data
data_sequential = np.random.rand(10, 10)
im1 = axes[0, 0].imshow(data_sequential, cmap='Blues')
axes[0, 0].set_title('Sequential Colors (Blues)')
plt.colorbar(im1, ax=axes[0, 0])

# Diverging colors for data with meaningful center
data_diverging = np.random.randn(10, 10)
im2 = axes[0, 1].imshow(data_diverging, cmap='RdBu_r')
axes[0, 1].set_title('Diverging Colors (Red-Blue)')
plt.colorbar(im2, ax=axes[0, 1])

# Qualitative colors for categorical data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
colors = plt.cm.Set3(np.linspace(0, 1, len(categories)))
axes[1, 0].bar(categories, values, color=colors)
axes[1, 0].set_title('Qualitative Colors (Set3)')

# Colorblind-friendly palette
sns.barplot(x=categories, y=values, palette='colorblind', ax=axes[1, 1])
axes[1, 1].set_title('Colorblind-Friendly Palette')

plt.tight_layout()
plt.show()
```

### 3. Clear Labeling and Titles

```python
# Example of clear, informative visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue_2022 = [120, 135, 148, 162, 178, 195]
revenue_2023 = [145, 158, 172, 189, 205, 223]

x = np.arange(len(months))
width = 0.35

bars1 = ax.bar(x - width/2, revenue_2022, width, label='2022', alpha=0.8, color='skyblue')
bars2 = ax.bar(x + width/2, revenue_2023, width, label='2023', alpha=0.8, color='lightcoral')

# Clear, descriptive title
ax.set_title('Monthly Revenue Comparison: 2022 vs 2023\n(Showing 15% average growth)', 
             fontsize=16, fontweight='bold', pad=20)

# Descriptive axis labels
ax.set_xlabel('Month', fontsize=12, fontweight='bold')
ax.set_ylabel('Revenue ($ thousands)', fontsize=12, fontweight='bold')

# Clear tick labels
ax.set_xticks(x)
ax.set_xticklabels(months)

# Legend with clear positioning
ax.legend(title='Year', title_fontsize=12, fontsize=11, loc='upper left')

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'${height}k', ha='center', va='bottom', fontweight='bold')

# Professional grid
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()
```

### 4. Avoiding Common Mistakes

```python
# Common mistakes and how to avoid them

# Mistake 1: Misleading scales
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

data = [98, 99, 100, 101, 102]
labels = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']

# Misleading: Y-axis doesn't start at 0
ax1.bar(labels, data)
ax1.set_ylim(97, 103)
ax1.set_title('Misleading: Exaggerated Differences')
ax1.set_ylabel('Sales')

# Better: Y-axis starts at 0 or shows full context
ax2.bar(labels, data)
ax2.set_ylim(0, 110)
ax2.set_title('Better: Full Context')
ax2.set_ylabel('Sales')

plt.tight_layout()
plt.show()

# Mistake 2: Too much information
# Instead of cramming everything into one plot, use multiple focused plots
```

## Interactive Visualizations

### Using Plotly for Interactivity

```python
# Note: This requires plotly installation
# pip install plotly

try:
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    
    # Interactive scatter plot
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", 
                    color="species", size="petal_length",
                    hover_data=['petal_width'],
                    title="Interactive Iris Dataset Visualization")
    
    # Show plot (will open in browser)
    # fig.show()
    
    print("Plotly example ready - uncomment fig.show() to display")
    
except ImportError:
    print("Plotly not installed. Install with: pip install plotly")
```

## Visualization for Different Audiences

### 1. Executive Dashboard Style

```python
# Executive-friendly visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

# KPI Cards style
metrics = ['Revenue', 'Profit', 'Customers', 'Growth']
values = [1250000, 187500, 15420, 12.5]
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']

for i, (metric, value, color) in enumerate(zip(metrics, values, colors)):
    ax = [ax1, ax2, ax3, ax4][i]
    ax.text(0.5, 0.7, metric, ha='center', va='center', fontsize=16, fontweight='bold')
    
    if metric == 'Growth':
        ax.text(0.5, 0.3, f'{value}%', ha='center', va='center', 
                fontsize=24, fontweight='bold', color=color)
    elif metric in ['Revenue', 'Profit']:
        ax.text(0.5, 0.3, f'${value:,.0f}', ha='center', va='center', 
                fontsize=20, fontweight='bold', color=color)
    else:
        ax.text(0.5, 0.3, f'{value:,.0f}', ha='center', va='center', 
                fontsize=20, fontweight='bold', color=color)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Add border
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(2)
        spine.set_edgecolor(color)

plt.suptitle('Q3 2023 Performance Dashboard', fontsize=20, fontweight='bold', y=0.95)
plt.tight_layout()
plt.show()
```

### 2. Technical/Scientific Style

```python
# Scientific publication style
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Generate sample experimental data
x = np.linspace(0, 10, 50)
y_true = 2 * np.exp(-x/3) * np.cos(x)
y_measured = y_true + np.random.normal(0, 0.1, len(x))
y_error = np.abs(np.random.normal(0, 0.1, len(x)))

# Plot with error bars
ax.errorbar(x, y_measured, yerr=y_error, fmt='o', capsize=3, capthick=1, 
           alpha=0.7, label='Measured data')
ax.plot(x, y_true, 'r-', linewidth=2, label='Theoretical model')

ax.set_xlabel('Time (s)', fontsize=12)
ax.set_ylabel('Amplitude (V)', fontsize=12)
ax.set_title('Damped Oscillation: Experimental vs Theoretical', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

# Add equation as text
ax.text(0.05, 0.95, r'$y = 2e^{-t/3}\cos(t)$', transform=ax.transAxes, 
        fontsize=14, verticalalignment='top', 
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.show()
```

## Performance Considerations

### Optimizing Large Datasets

```python
# Strategies for large datasets
def plot_large_dataset_efficiently():
    # Generate large dataset
    n_points = 100000
    x = np.random.randn(n_points)
    y = np.random.randn(n_points)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Strategy 1: Sampling
    sample_size = 5000
    indices = np.random.choice(n_points, sample_size, replace=False)
    ax1.scatter(x[indices], y[indices], alpha=0.6, s=1)
    ax1.set_title(f'Sampling: {sample_size} of {n_points} points')
    
    # Strategy 2: Hexbin for density
    ax2.hexbin(x, y, gridsize=50, cmap='Blues')
    ax2.set_title('Hexbin: Density representation')
    
    plt.tight_layout()
    plt.show()

# Uncomment to run
# plot_large_dataset_efficiently()
```

## Summary

Data visualization is a powerful tool for:

### Key Principles
- **Clarity**: Make your message clear and unambiguous
- **Accuracy**: Represent data truthfully without distortion
- **Efficiency**: Convey maximum information with minimum ink
- **Aesthetics**: Create visually appealing and professional plots

### Library Strengths
- **Matplotlib**: Fine-grained control, publication-quality plots
- **Seaborn**: Statistical visualizations, attractive defaults
- **Plotly**: Interactive visualizations, web-ready plots

### Best Practices
- Choose appropriate chart types for your data
- Use color effectively and consider accessibility
- Provide clear labels, titles, and legends
- Avoid misleading scales and unnecessary complexity
- Consider your audience when designing visualizations

### Common Applications
- Exploratory data analysis
- Statistical reporting
- Business dashboards
- Scientific publications
- Presentations and storytelling

Mastering data visualization is essential for effective data communication. The combination of Matplotlib's flexibility and Seaborn's statistical focus provides a comprehensive toolkit for creating compelling visualizations that reveal insights and tell stories with data.

## Next Steps

In the next lesson, we'll explore basic statistical analysis, learning how to apply statistical methods to understand and interpret data patterns, which will complement the visualization skills you've developed here.