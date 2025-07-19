# Deployment Guide

## Production Deployment

### Prerequisites

- Python 3.8+
- Redis server
- PostgreSQL (recommended for production)
- Nginx (for reverse proxy)
- Supervisor or systemd (for process management)

### Environment Setup

1. **Create production environment file**:
   ```bash
   cp .env.example .env.production
   ```

2. **Update production configuration**:
   ```bash
   # .env.production
   FLASK_ENV=production
   SECRET_KEY=your-secure-secret-key
   DATABASE_URL=postgresql://user:password@localhost/dashboard_db
   REDIS_URL=redis://localhost:6379/0
   ```

### Database Setup

1. **Create PostgreSQL database**:
   ```sql
   CREATE DATABASE dashboard_db;
   CREATE USER dashboard_user WITH PASSWORD 'secure_password';
   GRANT ALL PRIVILEGES ON DATABASE dashboard_db TO dashboard_user;
   ```

2. **Run migrations**:
   ```bash
   python manage.py init-db
   python manage.py create-admin
   ```

### Application Deployment

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install gunicorn psycopg2-binary
   ```

2. **Configure Gunicorn**:
   ```bash
   # gunicorn.conf.py
   bind = "127.0.0.1:8000"
   workers = 4
   worker_class = "sync"
   worker_connections = 1000
   max_requests = 1000
   max_requests_jitter = 100
   timeout = 30
   keepalive = 2
   preload_app = True
   ```

3. **Start application**:
   ```bash
   gunicorn -c gunicorn.conf.py manage:app
   ```

### Celery Worker Setup

1. **Start Celery worker**:
   ```bash
   celery -A celery_app.celery worker --loglevel=info --concurrency=4
   ```

2. **Start Celery beat (for scheduled tasks)**:
   ```bash
   celery -A celery_app.celery beat --loglevel=info
   ```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/app/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    client_max_body_size 100M;
}
```

### Process Management with Supervisor

```ini
# /etc/supervisor/conf.d/dashboard.conf
[program:dashboard-web]
command=/path/to/venv/bin/gunicorn -c gunicorn.conf.py manage:app
directory=/path/to/app
user=dashboard
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/dashboard/web.log

[program:dashboard-worker]
command=/path/to/venv/bin/celery -A celery_app.celery worker --loglevel=info
directory=/path/to/app
user=dashboard
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/dashboard/worker.log

[program:dashboard-beat]
command=/path/to/venv/bin/celery -A celery_app.celery beat --loglevel=info
directory=/path/to/app
user=dashboard
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/dashboard/beat.log
```

### SSL/TLS Configuration

1. **Install Certbot**:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   ```

2. **Obtain SSL certificate**:
   ```bash
   sudo certbot --nginx -d your-domain.com
   ```

### Monitoring and Logging

1. **Application logs**:
   - Configure log rotation
   - Set up centralized logging (ELK stack, etc.)

2. **Performance monitoring**:
   - Use APM tools (New Relic, DataDog, etc.)
   - Monitor database performance
   - Set up alerts for critical metrics

### Backup Strategy

1. **Database backups**:
   ```bash
   # Daily backup script
   pg_dump dashboard_db > backup_$(date +%Y%m%d).sql
   ```

2. **File backups**:
   ```bash
   # Backup upload directory
   tar -czf uploads_backup_$(date +%Y%m%d).tar.gz uploads/
   ```

### Security Considerations

1. **Firewall configuration**:
   - Only expose necessary ports (80, 443)
   - Restrict database access

2. **Application security**:
   - Regular security updates
   - Input validation and sanitization
   - Rate limiting

3. **Data protection**:
   - Encrypt sensitive data
   - Secure file uploads
   - Regular security audits

### Performance Optimization

1. **Database optimization**:
   - Proper indexing
   - Query optimization
   - Connection pooling

2. **Caching**:
   - Redis for application cache
   - CDN for static assets
   - Browser caching headers

3. **Application optimization**:
   - Code profiling
   - Memory usage monitoring
   - Async processing for heavy tasks

### Scaling Considerations

1. **Horizontal scaling**:
   - Load balancer configuration
   - Multiple application instances
   - Database read replicas

2. **Vertical scaling**:
   - Resource monitoring
   - Performance bottleneck identification
   - Hardware upgrades

### Disaster Recovery

1. **Backup verification**:
   - Regular restore testing
   - Backup integrity checks

2. **Recovery procedures**:
   - Documented recovery steps
   - RTO/RPO targets
   - Failover procedures