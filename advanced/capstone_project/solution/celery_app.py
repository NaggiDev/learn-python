"""
Celery application configuration for background tasks.
"""
from celery import Celery
from app import create_app
from config import config
import os

# Create Flask app
flask_app = create_app(os.environ.get('FLASK_ENV', 'development'))

# Create Celery instance
celery = Celery(
    flask_app.import_name,
    broker=flask_app.config['CELERY_BROKER_URL'],
    backend=flask_app.config['CELERY_RESULT_BACKEND']
)

# Update Celery configuration
celery.conf.update(
    task_serializer=flask_app.config['CELERY_TASK_SERIALIZER'],
    result_serializer=flask_app.config['CELERY_RESULT_SERIALIZER'],
    accept_content=flask_app.config['CELERY_ACCEPT_CONTENT'],
    timezone=flask_app.config['CELERY_TIMEZONE'],
    enable_utc=flask_app.config['CELERY_ENABLE_UTC'],
    task_routes={
        'app.tasks.analysis.*': {'queue': 'analysis'},
        'app.tasks.data.*': {'queue': 'data_processing'},
        'app.tasks.reports.*': {'queue': 'reports'}
    },
    task_annotations={
        'app.tasks.analysis.run_analysis': {'rate_limit': '10/m'},
        'app.tasks.reports.generate_report': {'rate_limit': '5/m'}
    }
)


class ContextTask(celery.Task):
    """Make celery tasks work with Flask app context."""
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)


celery.Task = ContextTask

# Import tasks to register them
from app.tasks import analysis_tasks, data_tasks, report_tasks

if __name__ == '__main__':
    celery.start()