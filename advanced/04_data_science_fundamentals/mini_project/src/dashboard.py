"""
Data Analysis Dashboard

This module creates a comprehensive data analysis dashboard that integrates
all the concepts learned in the Data Science Fundamentals module.

The dashboard includes:
- Data loading and preprocessing
- Statistical analysis
- Interactive visualizations
- Business insights and recommendations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set style for consistent visualizations
plt.style.use('default')
sns.set_palette("husl")


class RetailSalesDashboard:
    """
    Comprehensive retail sales analysis dashboard
    """
    
    def __init__(self, data_path):
        """
        Initialize the dashboard with data
        
        Parameters:
        -----------
        data_path : str
            Path to the sales data CSV file
        """
        self.data_path = data_path
        self.df = None
        self.df_clean = None
        self.load_and_preprocess_data()
    
    def load_and_preprocess_data(self):
        """
        Load and preprocess the sales data
        """
        print("Loading and preprocessing data...")
        
        # Load data
        self.df = pd.read_csv(self.data_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        
        # Create a clean version for analysis
        self.df_clean = self.df.copy()
        
        # Handle missing values
        self.df_clean['Customer_Age'].fillna(self.df_clean['Customer_Age'].median(), inplace=True)
        self.df_clean['Sales_Rep'].fillna('Unknown', inplace=True)
        self.df_clean['Discount_Percentage'].fillna(0, inplace=True)
        
        # Remove outliers (using IQR method)
        self._remove_outliers(['Sales_Amount', 'Quantity', 'Customer_Age'])
        
        # Add derived features
        self._add_derived_features()
        
        print(f"Data loaded: {len(self.df)} records")
        print(f"Clean data: {len(self.df_clean)} records")
    
    def _remove_outliers(self, columns):
        """
        Remove outliers using IQR method
        
        Parameters:
        -----------
        columns : list
            List of column names to check for outliers
        """
        for col in columns:
            if col in self.df_clean.columns:
                Q1 = self.df_clean[col].quantile(0.25)
                Q3 = self.df_clean[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                # Remove outliers
                self.df_clean = self.df_clean[
                    (self.df_clean[col] >= lower_bound) & 
                    (self.df_clean[col] <= upper_bound)
                ]
    
    def _add_derived_features(self):
        """
        Add derived features for analysis
        """
        # Time-based features
        self.df_clean['Month'] = self.df_clean['Date'].dt.month
        self.df_clean['Quarter'] = self.df_clean['Date'].dt.quarter
        self.df_clean['Year'] = self.df_clean['Date'].dt.year
        self.df_clean['Day_of_Week'] = self.df_clean['Date'].dt.day_name()
        self.df_clean['Is_Weekend'] = self.df_clean['Date'].dt.weekday >= 5
        
        # Business features
        self.df_clean['Unit_Price'] = self.df_clean['Sales_Amount'] / self.df_clean['Quantity']
        
        # Customer segments based on age
        self.df_clean['Age_Group'] = pd.cut(
            self.df_clean['Customer_Age'], 
            bins=[0, 25, 35, 50, 65, 100], 
            labels=['18-25', '26-35', '36-50', '51-65', '65+']
        )
        
        # Sales performance categories
        sales_quartiles = self.df_clean['Sales_Amount'].quantile([0.25, 0.5, 0.75])
        self.df_clean['Sales_Category'] = pd.cut(
            self.df_clean['Sales_Amount'],
            bins=[0, sales_quartiles[0.25], sales_quartiles[0.5], 
                  sales_quartiles[0.75], float('inf')],
            labels=['Low', 'Medium', 'High', 'Very High']
        )
    
    def generate_executive_summary(self):
        """
        Generate executive summary with key metrics
        
        Returns:
        --------
        dict
            Key business metrics
        """
        df = self.df_clean
        
        # Calculate key metrics
        total_sales = df['Sales_Amount'].sum()
        total_transactions = len(df)
        avg_transaction_value = df['Sales_Amount'].mean()
        total_quantity = df['Quantity'].sum()
        
        # Growth analysis (comparing years if data spans multiple years)
        if df['Year'].nunique() > 1:
            yearly_sales = df.groupby('Year')['Sales_Amount'].sum()
            if len(yearly_sales) >= 2:
                growth_rate = ((yearly_sales.iloc[-1] - yearly_sales.iloc[-2]) / 
                              yearly_sales.iloc[-2] * 100)
            else:
                growth_rate = 0
        else:
            growth_rate = 0
        
        # Top performers
        top_category = df.groupby('Product_Category')['Sales_Amount'].sum().idxmax()
        top_region = df.groupby('Region')['Sales_Amount'].sum().idxmax()
        
        # Customer insights
        avg_customer_age = df['Customer_Age'].mean()
        discount_impact = df[df['Discount_Applied'] == 'Yes']['Sales_Amount'].mean() - \
                         df[df['Discount_Applied'] == 'No']['Sales_Amount'].mean()
        
        summary = {
            'total_sales': total_sales,
            'total_transactions': total_transactions,
            'avg_transaction_value': avg_transaction_value,
            'total_quantity': total_quantity,
            'growth_rate': growth_rate,
            'top_category': top_category,
            'top_region': top_region,
            'avg_customer_age': avg_customer_age,
            'discount_impact': discount_impact,
            'online_vs_physical': df.groupby('Store_Type')['Sales_Amount'].sum().to_dict()
        }
        
        return summary
    
    def create_sales_trend_analysis(self):
        """
        Create sales trend analysis visualizations
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Monthly sales trend
        monthly_sales = self.df_clean.groupby(self.df_clean['Date'].dt.to_period('M'))['Sales_Amount'].sum()
        axes[0, 0].plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', linewidth=2)
        axes[0, 0].set_title('Monthly Sales Trend', fontsize=14, fontweight='bold')
        axes[0, 0].set_xlabel('Month')
        axes[0, 0].set_ylabel('Sales Amount ($)')
        axes[0, 0].tick_params(axis='x', rotation=45)
        axes[0, 0].grid(True, alpha=0.3)
        
        # Sales by day of week
        dow_sales = self.df_clean.groupby('Day_of_Week')['Sales_Amount'].mean()
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dow_sales = dow_sales.reindex(day_order)
        
        bars = axes[0, 1].bar(dow_sales.index, dow_sales.values, color='skyblue', alpha=0.8)
        axes[0, 1].set_title('Average Sales by Day of Week', fontsize=14, fontweight='bold')
        axes[0, 1].set_xlabel('Day of Week')
        axes[0, 1].set_ylabel('Average Sales Amount ($)')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                           f'${height:,.0f}', ha='center', va='bottom', fontweight='bold')
        
        # Quarterly comparison
        quarterly_sales = self.df_clean.groupby(['Year', 'Quarter'])['Sales_Amount'].sum().unstack(fill_value=0)
        quarterly_sales.plot(kind='bar', ax=axes[1, 0], width=0.8)
        axes[1, 0].set_title('Quarterly Sales Comparison', fontsize=14, fontweight='bold')
        axes[1, 0].set_xlabel('Year')
        axes[1, 0].set_ylabel('Sales Amount ($)')
        axes[1, 0].legend(title='Quarter', bbox_to_anchor=(1.05, 1), loc='upper left')
        axes[1, 0].tick_params(axis='x', rotation=0)
        
        # Sales distribution
        axes[1, 1].hist(self.df_clean['Sales_Amount'], bins=50, alpha=0.7, color='lightcoral', edgecolor='black')
        axes[1, 1].axvline(self.df_clean['Sales_Amount'].mean(), color='red', linestyle='--', 
                          linewidth=2, label=f'Mean: ${self.df_clean["Sales_Amount"].mean():.2f}')
        axes[1, 1].axvline(self.df_clean['Sales_Amount'].median(), color='blue', linestyle='--', 
                          linewidth=2, label=f'Median: ${self.df_clean["Sales_Amount"].median():.2f}')
        axes[1, 1].set_title('Sales Amount Distribution', fontsize=14, fontweight='bold')
        axes[1, 1].set_xlabel('Sales Amount ($)')
        axes[1, 1].set_ylabel('Frequency')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def create_product_analysis(self):
        """
        Create product performance analysis visualizations
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Sales by category
        category_sales = self.df_clean.groupby('Product_Category')['Sales_Amount'].sum().sort_values(ascending=True)
        bars = axes[0, 0].barh(category_sales.index, category_sales.values, color='lightgreen', alpha=0.8)
        axes[0, 0].set_title('Total Sales by Product Category', fontsize=14, fontweight='bold')
        axes[0, 0].set_xlabel('Sales Amount ($)')
        
        # Add value labels
        for bar in bars:
            width = bar.get_width()
            axes[0, 0].text(width + width*0.01, bar.get_y() + bar.get_height()/2,
                           f'${width:,.0f}', ha='left', va='center', fontweight='bold')
        
        # Average transaction value by category
        avg_transaction = self.df_clean.groupby('Product_Category')['Sales_Amount'].mean().sort_values(ascending=False)
        bars = axes[0, 1].bar(avg_transaction.index, avg_transaction.values, color='orange', alpha=0.8)
        axes[0, 1].set_title('Average Transaction Value by Category', fontsize=14, fontweight='bold')
        axes[0, 1].set_xlabel('Product Category')
        axes[0, 1].set_ylabel('Average Sales Amount ($)')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                           f'${height:.0f}', ha='center', va='bottom', fontweight='bold')
        
        # Quantity sold by category
        quantity_by_category = self.df_clean.groupby('Product_Category')['Quantity'].sum()
        wedges, texts, autotexts = axes[1, 0].pie(quantity_by_category.values, labels=quantity_by_category.index, 
                                                 autopct='%1.1f%%', startangle=90)
        axes[1, 0].set_title('Quantity Distribution by Category', fontsize=14, fontweight='bold')
        
        # Top products by sales
        top_products = self.df_clean.groupby('Product_Name')['Sales_Amount'].sum().nlargest(10)
        bars = axes[1, 1].barh(range(len(top_products)), top_products.values, color='purple', alpha=0.8)
        axes[1, 1].set_yticks(range(len(top_products)))
        axes[1, 1].set_yticklabels(top_products.index)
        axes[1, 1].set_title('Top 10 Products by Sales', fontsize=14, fontweight='bold')
        axes[1, 1].set_xlabel('Sales Amount ($)')
        
        # Add value labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            axes[1, 1].text(width + width*0.01, bar.get_y() + bar.get_height()/2,
                           f'${width:,.0f}', ha='left', va='center', fontweight='bold')
        
        plt.tight_layout()
        plt.show()
    
    def create_customer_analysis(self):
        """
        Create customer analysis visualizations
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Age distribution
        axes[0, 0].hist(self.df_clean['Customer_Age'], bins=20, alpha=0.7, color='lightblue', edgecolor='black')
        axes[0, 0].axvline(self.df_clean['Customer_Age'].mean(), color='red', linestyle='--', 
                          linewidth=2, label=f'Mean: {self.df_clean["Customer_Age"].mean():.1f}')
        axes[0, 0].set_title('Customer Age Distribution', fontsize=14, fontweight='bold')
        axes[0, 0].set_xlabel('Age')
        axes[0, 0].set_ylabel('Frequency')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # Sales by age group
        age_group_sales = self.df_clean.groupby('Age_Group')['Sales_Amount'].mean()
        bars = axes[0, 1].bar(age_group_sales.index, age_group_sales.values, color='coral', alpha=0.8)
        axes[0, 1].set_title('Average Sales by Age Group', fontsize=14, fontweight='bold')
        axes[0, 1].set_xlabel('Age Group')
        axes[0, 1].set_ylabel('Average Sales Amount ($)')
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                           f'${height:.0f}', ha='center', va='bottom', fontweight='bold')
        
        # Gender comparison
        gender_stats = self.df_clean.groupby('Customer_Gender').agg({
            'Sales_Amount': ['mean', 'count'],
            'Quantity': 'mean'
        }).round(2)
        
        # Flatten column names
        gender_stats.columns = ['Avg_Sales', 'Count', 'Avg_Quantity']
        
        x = np.arange(len(gender_stats.index))
        width = 0.35
        
        bars1 = axes[1, 0].bar(x - width/2, gender_stats['Avg_Sales'], width, 
                              label='Avg Sales', color='lightgreen', alpha=0.8)
        bars2 = axes[1, 0].bar(x + width/2, gender_stats['Avg_Quantity']*50, width, 
                              label='Avg Quantity (×50)', color='lightcoral', alpha=0.8)
        
        axes[1, 0].set_title('Sales Comparison by Gender', fontsize=14, fontweight='bold')
        axes[1, 0].set_xlabel('Gender')
        axes[1, 0].set_ylabel('Amount')
        axes[1, 0].set_xticks(x)
        axes[1, 0].set_xticklabels(gender_stats.index)
        axes[1, 0].legend()
        
        # Discount impact analysis
        discount_comparison = self.df_clean.groupby('Discount_Applied')['Sales_Amount'].agg(['mean', 'count'])
        
        bars = axes[1, 1].bar(discount_comparison.index, discount_comparison['mean'], 
                             color=['lightblue', 'orange'], alpha=0.8)
        axes[1, 1].set_title('Average Sales: Discount vs No Discount', fontsize=14, fontweight='bold')
        axes[1, 1].set_xlabel('Discount Applied')
        axes[1, 1].set_ylabel('Average Sales Amount ($)')
        
        # Add value labels and count
        for i, bar in enumerate(bars):
            height = bar.get_height()
            count = discount_comparison['count'].iloc[i]
            axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                           f'${height:.0f}\n(n={count})', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.show()
    
    def create_regional_analysis(self):
        """
        Create regional performance analysis
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Sales by region
        regional_sales = self.df_clean.groupby('Region')['Sales_Amount'].sum().sort_values(ascending=True)
        bars = axes[0, 0].barh(regional_sales.index, regional_sales.values, color='gold', alpha=0.8)
        axes[0, 0].set_title('Total Sales by Region', fontsize=14, fontweight='bold')
        axes[0, 0].set_xlabel('Sales Amount ($)')
        
        # Add value labels
        for bar in bars:
            width = bar.get_width()
            axes[0, 0].text(width + width*0.01, bar.get_y() + bar.get_height()/2,
                           f'${width:,.0f}', ha='left', va='center', fontweight='bold')
        
        # Regional performance heatmap
        regional_category = pd.crosstab(self.df_clean['Region'], self.df_clean['Product_Category'], 
                                       values=self.df_clean['Sales_Amount'], aggfunc='sum')
        
        sns.heatmap(regional_category, annot=True, fmt='.0f', cmap='YlOrRd', ax=axes[0, 1])
        axes[0, 1].set_title('Sales Heatmap: Region vs Category', fontsize=14, fontweight='bold')
        axes[0, 1].set_xlabel('Product Category')
        axes[0, 1].set_ylabel('Region')
        
        # Store type comparison by region
        store_region = pd.crosstab(self.df_clean['Region'], self.df_clean['Store_Type'], 
                                  values=self.df_clean['Sales_Amount'], aggfunc='sum')
        store_region_pct = store_region.div(store_region.sum(axis=1), axis=0) * 100
        
        store_region_pct.plot(kind='bar', stacked=True, ax=axes[1, 0], color=['lightblue', 'orange'])
        axes[1, 0].set_title('Store Type Distribution by Region (%)', fontsize=14, fontweight='bold')
        axes[1, 0].set_xlabel('Region')
        axes[1, 0].set_ylabel('Percentage')
        axes[1, 0].legend(title='Store Type')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Average transaction value by region
        avg_transaction_region = self.df_clean.groupby('Region')['Sales_Amount'].mean().sort_values(ascending=False)
        bars = axes[1, 1].bar(avg_transaction_region.index, avg_transaction_region.values, 
                             color='lightcoral', alpha=0.8)
        axes[1, 1].set_title('Average Transaction Value by Region', fontsize=14, fontweight='bold')
        axes[1, 1].set_xlabel('Region')
        axes[1, 1].set_ylabel('Average Sales Amount ($)')
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                           f'${height:.0f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.show()
    
    def perform_statistical_analysis(self):
        """
        Perform statistical analysis and hypothesis testing
        """
        print("Statistical Analysis Results")
        print("=" * 50)
        
        # 1. Test if there's a significant difference in sales between genders
        male_sales = self.df_clean[self.df_clean['Customer_Gender'] == 'M']['Sales_Amount']
        female_sales = self.df_clean[self.df_clean['Customer_Gender'] == 'F']['Sales_Amount']
        
        t_stat, p_value = stats.ttest_ind(male_sales, female_sales)
        print(f"\n1. Gender Sales Comparison (t-test):")
        print(f"   Male average: ${male_sales.mean():.2f}")
        print(f"   Female average: ${female_sales.mean():.2f}")
        print(f"   t-statistic: {t_stat:.3f}")
        print(f"   p-value: {p_value:.3f}")
        print(f"   Significant difference: {'Yes' if p_value < 0.05 else 'No'}")
        
        # 2. ANOVA test for sales across regions
        region_groups = [group['Sales_Amount'].values for name, group in self.df_clean.groupby('Region')]
        f_stat, p_value = stats.f_oneway(*region_groups)
        
        print(f"\n2. Regional Sales Comparison (ANOVA):")
        print(f"   F-statistic: {f_stat:.3f}")
        print(f"   p-value: {p_value:.3f}")
        print(f"   Significant difference between regions: {'Yes' if p_value < 0.05 else 'No'}")
        
        # 3. Correlation analysis
        numeric_cols = ['Sales_Amount', 'Quantity', 'Customer_Age', 'Discount_Percentage']
        correlation_matrix = self.df_clean[numeric_cols].corr()
        
        print(f"\n3. Correlation Analysis:")
        print("   Correlation Matrix:")
        print(correlation_matrix.round(3))
        
        # 4. Chi-square test for independence (Discount vs Store Type)
        contingency_table = pd.crosstab(self.df_clean['Discount_Applied'], self.df_clean['Store_Type'])
        chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        
        print(f"\n4. Discount vs Store Type Independence Test (Chi-square):")
        print(f"   Chi-square statistic: {chi2_stat:.3f}")
        print(f"   p-value: {p_value:.3f}")
        print(f"   Variables are independent: {'No' if p_value < 0.05 else 'Yes'}")
        
        # 5. Confidence interval for average sales
        mean_sales = self.df_clean['Sales_Amount'].mean()
        std_sales = self.df_clean['Sales_Amount'].std()
        n = len(self.df_clean)
        
        # 95% confidence interval
        confidence_level = 0.95
        alpha = 1 - confidence_level
        t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
        margin_of_error = t_critical * (std_sales / np.sqrt(n))
        
        ci_lower = mean_sales - margin_of_error
        ci_upper = mean_sales + margin_of_error
        
        print(f"\n5. 95% Confidence Interval for Average Sales:")
        print(f"   Mean: ${mean_sales:.2f}")
        print(f"   95% CI: [${ci_lower:.2f}, ${ci_upper:.2f}]")
        print(f"   Margin of error: ±${margin_of_error:.2f}")
    
    def generate_business_insights(self):
        """
        Generate actionable business insights
        """
        print("\nBusiness Insights and Recommendations")
        print("=" * 50)
        
        # Get summary statistics
        summary = self.generate_executive_summary()
        
        print(f"\n📊 EXECUTIVE SUMMARY:")
        print(f"   • Total Sales: ${summary['total_sales']:,.2f}")
        print(f"   • Total Transactions: {summary['total_transactions']:,}")
        print(f"   • Average Transaction: ${summary['avg_transaction_value']:.2f}")
        print(f"   • Growth Rate: {summary['growth_rate']:.1f}%")
        
        print(f"\n🏆 TOP PERFORMERS:")
        print(f"   • Best Category: {summary['top_category']}")
        print(f"   • Best Region: {summary['top_region']}")
        
        print(f"\n👥 CUSTOMER INSIGHTS:")
        print(f"   • Average Customer Age: {summary['avg_customer_age']:.1f} years")
        print(f"   • Discount Impact: ${summary['discount_impact']:.2f} per transaction")
        
        # Seasonal analysis
        monthly_sales = self.df_clean.groupby('Month')['Sales_Amount'].mean()
        peak_month = monthly_sales.idxmax()
        low_month = monthly_sales.idxmin()
        
        print(f"\n📅 SEASONAL PATTERNS:")
        print(f"   • Peak Month: {peak_month} (${monthly_sales[peak_month]:.2f} avg)")
        print(f"   • Lowest Month: {low_month} (${monthly_sales[low_month]:.2f} avg)")
        
        # Product insights
        category_performance = self.df_clean.groupby('Product_Category').agg({
            'Sales_Amount': ['sum', 'mean', 'count']
        }).round(2)
        
        print(f"\n🛍️ PRODUCT RECOMMENDATIONS:")
        
        # Find best performing category
        best_category = category_performance[('Sales_Amount', 'sum')].idxmax()
        print(f"   • Focus on {best_category} - highest total sales")
        
        # Find highest margin opportunity
        highest_avg = category_performance[('Sales_Amount', 'mean')].idxmax()
        print(f"   • Promote {highest_avg} - highest average transaction value")
        
        # Regional recommendations
        regional_performance = self.df_clean.groupby('Region')['Sales_Amount'].agg(['sum', 'mean', 'count'])
        underperforming_region = regional_performance['sum'].idxmin()
        
        print(f"\n🗺️ REGIONAL STRATEGY:")
        print(f"   • Investigate {underperforming_region} region - lowest total sales")
        print(f"   • Consider targeted marketing campaigns")
        
        # Discount analysis
        discount_effectiveness = self.df_clean.groupby('Discount_Applied').agg({
            'Sales_Amount': 'mean',
            'Quantity': 'mean'
        })
        
        print(f"\n💰 PRICING STRATEGY:")
        if summary['discount_impact'] > 0:
            print(f"   • Discounts are effective - increase average transaction by ${summary['discount_impact']:.2f}")
            print(f"   • Consider expanding discount programs")
        else:
            print(f"   • Discounts may be reducing profitability")
            print(f"   • Review discount strategy and targeting")
        
        print(f"\n🎯 ACTION ITEMS:")
        print(f"   1. Expand inventory in {summary['top_category']} category")
        print(f"   2. Increase marketing efforts in {underperforming_region} region")
        print(f"   3. Optimize discount strategy based on customer segments")
        print(f"   4. Plan inventory for seasonal peaks (Month {peak_month})")
        print(f"   5. Develop retention programs for high-value customers")
    
    def run_complete_analysis(self):
        """
        Run the complete dashboard analysis
        """
        print("🚀 RETAIL SALES ANALYSIS DASHBOARD")
        print("=" * 60)
        
        # Generate executive summary
        summary = self.generate_executive_summary()
        
        # Create all visualizations
        print("\n📈 Creating Sales Trend Analysis...")
        self.create_sales_trend_analysis()
        
        print("\n🛍️ Creating Product Analysis...")
        self.create_product_analysis()
        
        print("\n👥 Creating Customer Analysis...")
        self.create_customer_analysis()
        
        print("\n🗺️ Creating Regional Analysis...")
        self.create_regional_analysis()
        
        # Perform statistical analysis
        print("\n📊 Performing Statistical Analysis...")
        self.perform_statistical_analysis()
        
        # Generate business insights
        self.generate_business_insights()
        
        print(f"\n✅ Analysis Complete!")
        print(f"Dashboard generated successfully with {len(self.df_clean)} records analyzed.")


def main():
    """
    Main function to run the dashboard
    """
    # Initialize dashboard
    dashboard = RetailSalesDashboard('../data/retail_sales.csv')
    
    # Run complete analysis
    dashboard.run_complete_analysis()


if __name__ == "__main__":
    main()