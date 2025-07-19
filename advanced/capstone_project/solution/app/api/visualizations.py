"""
Visualization API endpoints.
"""
import io
import base64
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from flask_restx import Api, Resource, fields, Namespace
from app import db
from app.models.dataset import Dataset
from app.services.data_service import DataService

# Create blueprint
visualizations_bp = Blueprint('visualizations', __name__, url_prefix='/api/visualizations')
visualizations_ns = Namespace('visualizations', description='Data visualization operations')

# Flask-RESTX models
chart_request_model = visualizations_ns.model('ChartRequest', {
    'dataset_id': fields.Integer(required=True, description='Dataset ID'),
    'chart_type': fields.String(required=True, description='Type of chart', 
                               enum=['histogram', 'scatter', 'line', 'bar', 'box', 'heatmap']),
    'x_column': fields.String(description='X-axis column'),
    'y_column': fields.String(description='Y-axis column'),
    'color_column': fields.String(description='Color grouping column'),
    'title': fields.String(description='Chart title'),
    'width': fields.Integer(default=800, description='Chart width'),
    'height': fields.Integer(default=600, description='Chart height'),
    'format': fields.String(default='png', enum=['png', 'svg', 'html'], description='Output format')
})


@visualizations_ns.route('/chart')
class CreateChart(Resource):
    """Create visualization chart endpoint."""
    
    @visualizations_ns.expect(chart_request_model)
    @visualizations_ns.doc('create_chart')
    @login_required
    def post(self):
        """Create a data visualization chart."""
        data = request.json
        
        # Validate input
        if not data or 'dataset_id' not in data or 'chart_type' not in data:
            return {'error': 'Missing required fields'}, 400
        
        dataset_id = data['dataset_id']
        chart_type = data['chart_type']
        
        # Check if dataset exists and user has access
        dataset = Dataset.query.get(dataset_id)
        if not dataset:
            return {'error': 'Dataset not found'}, 404
        
        if not current_user.can_view_dataset(dataset):
            return {'error': 'Access denied'}, 403
        
        try:
            # Load dataset
            df = DataService.load_dataset(dataset)
            
            # Validate columns
            x_column = data.get('x_column')
            y_column = data.get('y_column')
            color_column = data.get('color_column')
            
            if x_column and x_column not in df.columns:
                return {'error': f'Column {x_column} not found'}, 400
            if y_column and y_column not in df.columns:
                return {'error': f'Column {y_column} not found'}, 400
            if color_column and color_column not in df.columns:
                return {'error': f'Column {color_column} not found'}, 400
            
            # Create visualization
            chart_format = data.get('format', 'png')
            width = data.get('width', 800)
            height = data.get('height', 600)
            title = data.get('title', f'{chart_type.title()} Chart')
            
            if chart_format == 'html':
                # Use Plotly for interactive charts
                chart_data = create_plotly_chart(df, chart_type, x_column, y_column, 
                                               color_column, title, width, height)
            else:
                # Use Matplotlib/Seaborn for static charts
                chart_data = create_matplotlib_chart(df, chart_type, x_column, y_column, 
                                                   color_column, title, width, height, chart_format)
            
            return {
                'chart_data': chart_data,
                'format': chart_format,
                'dataset_id': dataset_id,
                'chart_type': chart_type,
                'title': title
            }, 200
            
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            current_app.logger.error(f'Chart creation failed: {str(e)}')
            return {'error': 'Chart creation failed'}, 500


def create_matplotlib_chart(df, chart_type, x_column, y_column, color_column, title, width, height, format_type):
    """Create chart using Matplotlib/Seaborn."""
    plt.figure(figsize=(width/100, height/100))
    
    try:
        if chart_type == 'histogram':
            if not x_column:
                raise ValueError("X column required for histogram")
            
            if color_column:
                for category in df[color_column].unique():
                    subset = df[df[color_column] == category]
                    plt.hist(subset[x_column].dropna(), alpha=0.7, label=str(category))
                plt.legend()
            else:
                plt.hist(df[x_column].dropna())
            
            plt.xlabel(x_column)
            plt.ylabel('Frequency')
            
        elif chart_type == 'scatter':
            if not x_column or not y_column:
                raise ValueError("Both X and Y columns required for scatter plot")
            
            if color_column:
                scatter = plt.scatter(df[x_column], df[y_column], c=df[color_column].astype('category').cat.codes, alpha=0.6)
                plt.colorbar(scatter)
            else:
                plt.scatter(df[x_column], df[y_column], alpha=0.6)
            
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            
        elif chart_type == 'line':
            if not x_column or not y_column:
                raise ValueError("Both X and Y columns required for line plot")
            
            if color_column:
                for category in df[color_column].unique():
                    subset = df[df[color_column] == category].sort_values(x_column)
                    plt.plot(subset[x_column], subset[y_column], label=str(category))
                plt.legend()
            else:
                df_sorted = df.sort_values(x_column)
                plt.plot(df_sorted[x_column], df_sorted[y_column])
            
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            
        elif chart_type == 'bar':
            if not x_column:
                raise ValueError("X column required for bar chart")
            
            if y_column:
                # Grouped bar chart
                df_grouped = df.groupby(x_column)[y_column].mean()
                df_grouped.plot(kind='bar')
                plt.ylabel(y_column)
            else:
                # Count bar chart
                df[x_column].value_counts().plot(kind='bar')
                plt.ylabel('Count')
            
            plt.xlabel(x_column)
            plt.xticks(rotation=45)
            
        elif chart_type == 'box':
            if not y_column:
                raise ValueError("Y column required for box plot")
            
            if x_column:
                sns.boxplot(data=df, x=x_column, y=y_column)
                plt.xticks(rotation=45)
            else:
                sns.boxplot(data=df, y=y_column)
            
        elif chart_type == 'heatmap':
            # Correlation heatmap for numeric columns
            numeric_df = df.select_dtypes(include=['number'])
            if len(numeric_df.columns) < 2:
                raise ValueError("At least 2 numeric columns required for heatmap")
            
            corr_matrix = numeric_df.corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
            
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}")
        
        plt.title(title)
        plt.tight_layout()
        
        # Convert to base64 string
        buffer = io.BytesIO()
        plt.savefig(buffer, format=format_type, dpi=100, bbox_inches='tight')
        buffer.seek(0)
        
        chart_data = base64.b64encode(buffer.getvalue()).decode()
        plt.close()
        
        return chart_data
        
    except Exception as e:
        plt.close()
        raise e


def create_plotly_chart(df, chart_type, x_column, y_column, color_column, title, width, height):
    """Create interactive chart using Plotly."""
    try:
        if chart_type == 'histogram':
            if not x_column:
                raise ValueError("X column required for histogram")
            
            fig = px.histogram(df, x=x_column, color=color_column, title=title)
            
        elif chart_type == 'scatter':
            if not x_column or not y_column:
                raise ValueError("Both X and Y columns required for scatter plot")
            
            fig = px.scatter(df, x=x_column, y=y_column, color=color_column, title=title)
            
        elif chart_type == 'line':
            if not x_column or not y_column:
                raise ValueError("Both X and Y columns required for line plot")
            
            fig = px.line(df, x=x_column, y=y_column, color=color_column, title=title)
            
        elif chart_type == 'bar':
            if not x_column:
                raise ValueError("X column required for bar chart")
            
            if y_column:
                fig = px.bar(df, x=x_column, y=y_column, color=color_column, title=title)
            else:
                value_counts = df[x_column].value_counts()
                fig = px.bar(x=value_counts.index, y=value_counts.values, title=title)
                fig.update_xaxes(title=x_column)
                fig.update_yaxes(title='Count')
            
        elif chart_type == 'box':
            if not y_column:
                raise ValueError("Y column required for box plot")
            
            fig = px.box(df, x=x_column, y=y_column, color=color_column, title=title)
            
        elif chart_type == 'heatmap':
            # Correlation heatmap
            numeric_df = df.select_dtypes(include=['number'])
            if len(numeric_df.columns) < 2:
                raise ValueError("At least 2 numeric columns required for heatmap")
            
            corr_matrix = numeric_df.corr()
            fig = px.imshow(corr_matrix, text_auto=True, aspect="auto", title=title)
            
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}")
        
        fig.update_layout(width=width, height=height)
        
        return fig.to_html(include_plotlyjs='cdn')
        
    except Exception as e:
        raise e


@visualizations_ns.route('/chart-types')
class ChartTypes(Resource):
    """Get available chart types endpoint."""
    
    @visualizations_ns.doc('get_chart_types')
    @login_required
    def get(self):
        """Get list of available chart types."""
        chart_types = [
            {
                'type': 'histogram',
                'name': 'Histogram',
                'description': 'Distribution of a single numeric variable',
                'required_columns': ['x'],
                'optional_columns': ['color']
            },
            {
                'type': 'scatter',
                'name': 'Scatter Plot',
                'description': 'Relationship between two numeric variables',
                'required_columns': ['x', 'y'],
                'optional_columns': ['color']
            },
            {
                'type': 'line',
                'name': 'Line Chart',
                'description': 'Trend over time or ordered values',
                'required_columns': ['x', 'y'],
                'optional_columns': ['color']
            },
            {
                'type': 'bar',
                'name': 'Bar Chart',
                'description': 'Comparison of categories',
                'required_columns': ['x'],
                'optional_columns': ['y', 'color']
            },
            {
                'type': 'box',
                'name': 'Box Plot',
                'description': 'Distribution summary with quartiles',
                'required_columns': ['y'],
                'optional_columns': ['x', 'color']
            },
            {
                'type': 'heatmap',
                'name': 'Heatmap',
                'description': 'Correlation matrix of numeric variables',
                'required_columns': [],
                'optional_columns': []
            }
        ]
        
        return {'chart_types': chart_types}, 200


# Register namespace with blueprint
visualizations_bp.add_url_rule('/chart', view_func=CreateChart.as_view('create_chart'))
visualizations_bp.add_url_rule('/chart-types', view_func=ChartTypes.as_view('chart_types'))