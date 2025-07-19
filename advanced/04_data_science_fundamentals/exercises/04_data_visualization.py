"""
Data Visualization Exercises

This exercise file covers fundamental data visualization concepts including:
- Basic plotting with Matplotlib
- Statistical visualizations with Seaborn
- Customization and styling
- Different chart types for different data
- Best practices in visualization design

Complete each exercise by implementing the required functionality.
Run the tests to verify your solutions.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


def exercise_1_basic_plotting():
    """
    Exercise 1: Basic Matplotlib Plotting
    
    Create basic plots using Matplotlib:
    1. Line plot of a mathematical function
    2. Scatter plot with customization
    3. Bar chart with multiple series
    4. Histogram with customization
    
    Returns:
        tuple: (fig_line, fig_scatter, fig_bar, fig_hist)
    """
    # TODO: Create line plot
    # Plot sin(x) and cos(x) from 0 to 2π
    x = np.linspace(0, 2*np.pi, 100)
    
    fig_line, ax_line = plt.subplots(figsize=(10, 6))
    # Add your line plotting code here
    # Include: title, labels, legend, grid
    
    # TODO: Create scatter plot
    # Generate random data with correlation
    np.random.seed(42)
    n_points = 100
    x_scatter = np.random.randn(n_points)
    y_scatter = 2 * x_scatter + np.random.randn(n_points) * 0.5
    
    fig_scatter, ax_scatter = plt.subplots(figsize=(8, 6))
    # Add your scatter plotting code here
    # Include: colors, alpha, title, labels
    
    # TODO: Create bar chart
    # Compare sales data for different products
    products = ['Product A', 'Product B', 'Product C', 'Product D']
    q1_sales = [23, 45, 56, 78]
    q2_sales = [34, 52, 48, 82]
    
    fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
    # Add your bar chart code here
    # Include: grouped bars, labels, legend, value labels on bars
    
    # TODO: Create histogram
    # Show distribution of random data
    np.random.seed(42)
    data1 = np.random.normal(100, 15, 1000)
    data2 = np.random.normal(120, 20, 1000)
    
    fig_hist, ax_hist = plt.subplots(figsize=(10, 6))
    # Add your histogram code here
    # Include: overlapping histograms, transparency, labels, legend
    
    return fig_line, fig_scatter, fig_bar, fig_hist


def exercise_2_subplots_customization():
    """
    Exercise 2: Subplots and Advanced Customization
    
    Create a figure with multiple subplots showing different aspects of data:
    1. 2x2 subplot layout
    2. Different plot types in each subplot
    3. Consistent styling across subplots
    4. Proper spacing and layout
    
    Returns:
        matplotlib.figure.Figure: The complete figure with subplots
    """
    # Sample data
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=365, freq='D')
    stock_prices = 100 + np.cumsum(np.random.randn(365) * 0.5)
    volumes = np.random.randint(1000, 5000, 365)
    
    # TODO: Create 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # TODO: Subplot 1 (top-left): Line plot of stock prices over time
    # Include: date formatting, trend line, title
    
    # TODO: Subplot 2 (top-right): Histogram of daily returns
    # Calculate daily returns and plot distribution
    
    # TODO: Subplot 3 (bottom-left): Scatter plot of price vs volume
    # Include: correlation analysis, trend line
    
    # TODO: Subplot 4 (bottom-right): Box plot of monthly returns
    # Group returns by month and create box plot
    
    # TODO: Add overall title and adjust layout
    
    return fig


def exercise_3_seaborn_statistical_plots():
    """
    Exercise 3: Statistical Visualizations with Seaborn
    
    Create statistical plots using Seaborn:
    1. Distribution plots (histogram, KDE, box plot)
    2. Relationship plots (scatter, regression)
    3. Categorical plots
    4. Correlation heatmap
    
    Returns:
        tuple: (fig_dist, fig_rel, fig_cat, fig_corr)
    """
    # Load sample dataset
    tips = sns.load_dataset("tips")
    
    # TODO: Create distribution plots
    fig_dist, axes_dist = plt.subplots(2, 2, figsize=(15, 12))
    
    # Subplot 1: Histogram with KDE for total_bill
    # Subplot 2: Box plot of total_bill by day
    # Subplot 3: Violin plot of total_bill by time
    # Subplot 4: Strip plot of tip by day
    
    # TODO: Create relationship plots
    fig_rel, axes_rel = plt.subplots(2, 2, figsize=(15, 12))
    
    # Subplot 1: Scatter plot of total_bill vs tip with regression line
    # Subplot 2: Scatter plot colored by time
    # Subplot 3: Joint plot (you can use a simple scatter for this exercise)
    # Subplot 4: Residual plot
    
    # TODO: Create categorical plots
    fig_cat, axes_cat = plt.subplots(2, 2, figsize=(15, 12))
    
    # Subplot 1: Bar plot of average total_bill by day
    # Subplot 2: Count plot of day
    # Subplot 3: Point plot showing tip by day and time
    # Subplot 4: Swarm plot of total_bill by day
    
    # TODO: Create correlation heatmap
    fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
    
    # Calculate correlation matrix for numerical columns
    # Create heatmap with annotations
    
    return fig_dist, fig_rel, fig_cat, fig_corr


def exercise_4_time_series_visualization():
    """
    Exercise 4: Time Series Visualization
    
    Create comprehensive time series visualizations:
    1. Line plot with multiple series
    2. Seasonal decomposition visualization
    3. Rolling statistics
    4. Candlestick-style plot (using OHLC data)
    
    Returns:
        tuple: (fig_ts, fig_seasonal, fig_rolling, fig_ohlc)
    """
    # Generate sample time series data
    np.random.seed(42)
    dates = pd.date_range('2020-01-01', periods=1000, freq='D')
    
    # Create multiple time series
    trend = np.linspace(100, 200, 1000)
    seasonal = 10 * np.sin(2 * np.pi * np.arange(1000) / 365.25)
    noise = np.random.normal(0, 5, 1000)
    ts1 = trend + seasonal + noise
    
    ts2 = 150 + 20 * np.sin(2 * np.pi * np.arange(1000) / 30) + np.random.normal(0, 3, 1000)
    
    # TODO: Create basic time series plot
    fig_ts, ax_ts = plt.subplots(figsize=(15, 8))
    # Plot both time series with proper date formatting
    # Include: legend, grid, title, axis labels
    
    # TODO: Create seasonal decomposition visualization
    fig_seasonal, axes_seasonal = plt.subplots(4, 1, figsize=(15, 12))
    # Plot: original, trend, seasonal, residual components
    # You can create simplified versions of these components
    
    # TODO: Create rolling statistics plot
    fig_rolling, ax_rolling = plt.subplots(figsize=(15, 8))
    # Plot original data with rolling mean and rolling std
    # Use different window sizes (e.g., 30 days, 90 days)
    
    # TODO: Create OHLC-style plot
    # Generate OHLC data from the time series
    fig_ohlc, ax_ohlc = plt.subplots(figsize=(15, 8))
    # Create a simplified candlestick plot using rectangles and lines
    # Or use a simple line plot with high/low ranges
    
    return fig_ts, fig_seasonal, fig_rolling, fig_ohlc


def exercise_5_advanced_customization():
    """
    Exercise 5: Advanced Plot Customization
    
    Create highly customized visualizations:
    1. Custom color schemes and palettes
    2. Annotations and text
    3. Multiple y-axes
    4. Custom styling and themes
    
    Returns:
        tuple: (fig_custom, fig_multi_axis, fig_annotated, fig_styled)
    """
    # Sample data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    revenue = [120, 135, 148, 162, 178, 195, 210, 205, 220, 240, 225, 250]
    profit_margin = [15, 18, 20, 16, 22, 25, 28, 26, 30, 32, 29, 35]
    employees = [50, 52, 55, 58, 62, 65, 68, 70, 72, 75, 78, 80]
    
    # TODO: Create custom color scheme plot
    fig_custom, ax_custom = plt.subplots(figsize=(12, 8))
    # Create a bar chart with custom colors
    # Use a custom color palette, gradients, or patterns
    # Include custom styling for all elements
    
    # TODO: Create multiple y-axes plot
    fig_multi_axis, ax1 = plt.subplots(figsize=(12, 8))
    # Plot revenue on left y-axis
    # Plot profit margin on right y-axis
    # Include proper labeling and colors for each axis
    
    # TODO: Create annotated plot
    fig_annotated, ax_annotated = plt.subplots(figsize=(12, 8))
    # Create a line plot with annotations
    # Add arrows pointing to specific data points
    # Include text boxes with insights
    # Highlight maximum and minimum values
    
    # TODO: Create styled plot with custom theme
    fig_styled, ax_styled = plt.subplots(figsize=(12, 8))
    # Apply custom styling (colors, fonts, grid, etc.)
    # Create a professional-looking visualization
    # Use consistent styling throughout
    
    return fig_custom, fig_multi_axis, fig_annotated, fig_styled


def exercise_6_dashboard_creation():
    """
    Exercise 6: Dashboard-Style Visualization
    
    Create a comprehensive dashboard with multiple KPIs and charts:
    1. KPI cards showing key metrics
    2. Trend charts
    3. Comparison charts
    4. Distribution analysis
    
    Returns:
        matplotlib.figure.Figure: Complete dashboard figure
    """
    # Generate sample business data
    np.random.seed(42)
    
    # KPI data
    kpis = {
        'Revenue': 1250000,
        'Profit': 187500,
        'Customers': 15420,
        'Growth': 12.5
    }
    
    # Time series data
    dates = pd.date_range('2023-01-01', periods=12, freq='M')
    monthly_revenue = [100000, 110000, 125000, 118000, 135000, 142000,
                      155000, 148000, 162000, 175000, 168000, 180000]
    monthly_customers = [1200, 1250, 1300, 1280, 1350, 1400,
                        1450, 1420, 1480, 1520, 1500, 1550]
    
    # Product data
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    product_sales = [250000, 320000, 180000, 420000, 280000]
    
    # Regional data
    regions = ['North', 'South', 'East', 'West']
    regional_performance = [85, 92, 78, 88]
    
    # TODO: Create dashboard layout
    fig = plt.figure(figsize=(20, 16))
    
    # TODO: Create KPI cards (top row)
    # Create 4 subplots for KPI cards
    # Style them to look like dashboard cards
    
    # TODO: Create trend chart (middle left)
    # Show monthly revenue and customer trends
    
    # TODO: Create product comparison (middle right)
    # Bar chart or pie chart of product sales
    
    # TODO: Create regional performance (bottom left)
    # Horizontal bar chart or radar chart
    
    # TODO: Create distribution analysis (bottom right)
    # Histogram or box plot of some metric
    
    # TODO: Add overall dashboard title and styling
    
    return fig


def exercise_7_interactive_elements():
    """
    Exercise 7: Interactive and Dynamic Elements
    
    Create visualizations with interactive-like features:
    1. Hover-style information display
    2. Clickable legend simulation
    3. Zoom and pan simulation
    4. Dynamic color coding
    
    Returns:
        tuple: (fig_hover, fig_legend, fig_zoom, fig_dynamic)
    """
    # Sample data
    np.random.seed(42)
    n_points = 50
    categories = np.random.choice(['A', 'B', 'C', 'D'], n_points)
    x = np.random.randn(n_points)
    y = np.random.randn(n_points)
    sizes = np.random.randint(20, 200, n_points)
    
    # TODO: Create hover-style information plot
    fig_hover, ax_hover = plt.subplots(figsize=(10, 8))
    # Create scatter plot with detailed annotations
    # Show information for selected points
    
    # TODO: Create legend interaction simulation
    fig_legend, ax_legend = plt.subplots(figsize=(10, 8))
    # Create plot where different categories can be "highlighted"
    # Use different alpha values to simulate selection
    
    # TODO: Create zoom simulation
    fig_zoom, (ax_zoom1, ax_zoom2) = plt.subplots(1, 2, figsize=(15, 6))
    # Show full data in left plot, zoomed region in right plot
    # Connect them with lines or annotations
    
    # TODO: Create dynamic color coding
    fig_dynamic, ax_dynamic = plt.subplots(figsize=(10, 8))
    # Create plot where colors change based on data values
    # Use color mapping to show additional dimensions
    
    return fig_hover, fig_legend, fig_zoom, fig_dynamic


def exercise_8_publication_quality():
    """
    Exercise 8: Publication-Quality Visualizations
    
    Create publication-ready visualizations:
    1. Scientific paper style
    2. Business report style
    3. Infographic style
    4. Technical documentation style
    
    Returns:
        tuple: (fig_scientific, fig_business, fig_infographic, fig_technical)
    """
    # Scientific data
    x_sci = np.linspace(0, 10, 100)
    y_sci = 2 * np.exp(-x_sci/3) * np.cos(x_sci)
    y_noise = y_sci + np.random.normal(0, 0.1, len(x_sci))
    
    # Business data
    quarters = ['Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 
               'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
    revenue = [2.1, 2.3, 2.5, 2.8, 3.1, 3.4, 3.6, 3.9]
    
    # TODO: Create scientific publication style
    fig_scientific, ax_scientific = plt.subplots(figsize=(10, 8))
    # Include: error bars, equation, proper citations style
    # Use academic formatting conventions
    
    # TODO: Create business report style
    fig_business, ax_business = plt.subplots(figsize=(12, 8))
    # Include: corporate colors, clean design, key insights
    # Professional business formatting
    
    # TODO: Create infographic style
    fig_infographic, ax_infographic = plt.subplots(figsize=(10, 12))
    # Include: bold colors, large text, visual elements
    # Eye-catching design for general audience
    
    # TODO: Create technical documentation style
    fig_technical, ax_technical = plt.subplots(figsize=(10, 8))
    # Include: detailed annotations, specifications
    # Clear technical communication
    
    return fig_scientific, fig_business, fig_infographic, fig_technical


# Test functions
def test_exercise_1():
    """Test basic plotting exercise"""
    try:
        fig_line, fig_scatter, fig_bar, fig_hist = exercise_1_basic_plotting()
        
        assert fig_line is not None, "Line plot not created"
        assert fig_scatter is not None, "Scatter plot not created"
        assert fig_bar is not None, "Bar chart not created"
        assert fig_hist is not None, "Histogram not created"
        
        plt.close('all')  # Clean up figures
        print("✓ Exercise 1 passed: Basic plotting")
        
    except Exception as e:
        print(f"❌ Exercise 1 failed: {e}")


def test_exercise_2():
    """Test subplots and customization exercise"""
    try:
        fig = exercise_2_subplots_customization()
        
        assert fig is not None, "Figure not created"
        assert len(fig.axes) == 4, "Should have 4 subplots"
        
        plt.close('all')
        print("✓ Exercise 2 passed: Subplots and customization")
        
    except Exception as e:
        print(f"❌ Exercise 2 failed: {e}")


def test_exercise_3():
    """Test Seaborn statistical plots exercise"""
    try:
        fig_dist, fig_rel, fig_cat, fig_corr = exercise_3_seaborn_statistical_plots()
        
        assert fig_dist is not None, "Distribution plots not created"
        assert fig_rel is not None, "Relationship plots not created"
        assert fig_cat is not None, "Categorical plots not created"
        assert fig_corr is not None, "Correlation heatmap not created"
        
        plt.close('all')
        print("✓ Exercise 3 passed: Seaborn statistical plots")
        
    except Exception as e:
        print(f"❌ Exercise 3 failed: {e}")


def test_exercise_4():
    """Test time series visualization exercise"""
    try:
        fig_ts, fig_seasonal, fig_rolling, fig_ohlc = exercise_4_time_series_visualization()
        
        assert fig_ts is not None, "Time series plot not created"
        assert fig_seasonal is not None, "Seasonal plot not created"
        assert fig_rolling is not None, "Rolling statistics plot not created"
        assert fig_ohlc is not None, "OHLC plot not created"
        
        plt.close('all')
        print("✓ Exercise 4 passed: Time series visualization")
        
    except Exception as e:
        print(f"❌ Exercise 4 failed: {e}")


def test_exercise_5():
    """Test advanced customization exercise"""
    try:
        fig_custom, fig_multi_axis, fig_annotated, fig_styled = exercise_5_advanced_customization()
        
        assert fig_custom is not None, "Custom plot not created"
        assert fig_multi_axis is not None, "Multi-axis plot not created"
        assert fig_annotated is not None, "Annotated plot not created"
        assert fig_styled is not None, "Styled plot not created"
        
        plt.close('all')
        print("✓ Exercise 5 passed: Advanced customization")
        
    except Exception as e:
        print(f"❌ Exercise 5 failed: {e}")


def test_exercise_6():
    """Test dashboard creation exercise"""
    try:
        fig = exercise_6_dashboard_creation()
        
        assert fig is not None, "Dashboard not created"
        
        plt.close('all')
        print("✓ Exercise 6 passed: Dashboard creation")
        
    except Exception as e:
        print(f"❌ Exercise 6 failed: {e}")


def test_exercise_7():
    """Test interactive elements exercise"""
    try:
        fig_hover, fig_legend, fig_zoom, fig_dynamic = exercise_7_interactive_elements()
        
        assert fig_hover is not None, "Hover plot not created"
        assert fig_legend is not None, "Legend plot not created"
        assert fig_zoom is not None, "Zoom plot not created"
        assert fig_dynamic is not None, "Dynamic plot not created"
        
        plt.close('all')
        print("✓ Exercise 7 passed: Interactive elements")
        
    except Exception as e:
        print(f"❌ Exercise 7 failed: {e}")


def test_exercise_8():
    """Test publication quality exercise"""
    try:
        fig_scientific, fig_business, fig_infographic, fig_technical = exercise_8_publication_quality()
        
        assert fig_scientific is not None, "Scientific plot not created"
        assert fig_business is not None, "Business plot not created"
        assert fig_infographic is not None, "Infographic plot not created"
        assert fig_technical is not None, "Technical plot not created"
        
        plt.close('all')
        print("✓ Exercise 8 passed: Publication quality")
        
    except Exception as e:
        print(f"❌ Exercise 8 failed: {e}")


def run_all_tests():
    """Run all exercise tests"""
    print("Running Data Visualization Exercises Tests...\n")
    
    test_exercise_1()
    test_exercise_2()
    test_exercise_3()
    test_exercise_4()
    test_exercise_5()
    test_exercise_6()
    test_exercise_7()
    test_exercise_8()
    
    print("\n🎉 All data visualization exercises completed!")
    print("\nKey concepts mastered:")
    print("- Basic plotting with Matplotlib")
    print("- Statistical visualizations with Seaborn")
    print("- Advanced customization and styling")
    print("- Time series visualization")
    print("- Dashboard creation")
    print("- Publication-quality plots")
    print("- Interactive visualization concepts")


if __name__ == "__main__":
    run_all_tests()