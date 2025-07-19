# Dependency Management with pip

## What is Dependency Management?

Dependency management is the process of handling external packages (libraries) that your Python project needs to function. It involves:

1. **Installing** packages your project depends on
2. **Specifying** exact versions for reproducibility
3. **Managing** conflicts between different package versions
4. **Documenting** dependencies for other developers
5. **Updating** packages safely

## Understanding pip

`pip` (Pip Installs Packages) is Python's standard package manager. It downloads packages from the Python Package Index (PyPI) and installs them in your Python environment.

### Basic pip Commands

```bash
# Install a package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Install minimum version
pip install package_name>=1.2.0

# Install version range
pip install "package_name>=1.2.0,<2.0.0"

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show package information
pip show package_name

# Search for packages (deprecated in newer versions)
pip search package_name
```

## Requirements Files

Requirements files are text files that list all the packages your project needs. They make it easy to recreate the same environment on different machines.

### Basic requirements.txt

```txt
requests
flask
numpy
pandas
```

### Versioned requirements.txt

```txt
requests==2.28.1
flask==2.2.2
numpy>=1.21.0
pandas>=1.4.0,<2.0.0
click~=8.0.0
```

### Version Specifiers

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `==` | Exact version | `django==4.1.0` |
| `>=` | Minimum version | `requests>=2.25.0` |
| `<=` | Maximum version | `numpy<=1.21.0` |
| `>` | Greater than | `flask>2.0.0` |
| `<` | Less than | `pandas<2.0.0` |
| `~=` | Compatible release | `click~=8.0.0` |
| `!=` | Not equal | `setuptools!=50.0.0` |

### Compatible Release (`~=`)

The `~=` operator is useful for allowing patch-level updates:

```txt
# ~=1.4.2 is equivalent to >=1.4.2, ==1.4.*
django~=4.1.0  # Allows 4.1.0, 4.1.1, 4.1.2, but not 4.2.0
```

## Working with Requirements Files

### Creating Requirements Files

```bash
# Generate requirements from current environment
pip freeze > requirements.txt

# Generate requirements with only top-level packages
pip-tools compile requirements.in

# Create requirements manually
echo "requests==2.28.1" > requirements.txt
echo "flask==2.2.2" >> requirements.txt
```

### Installing from Requirements Files

```bash
# Install all packages from requirements.txt
pip install -r requirements.txt

# Install with upgrade
pip install -r requirements.txt --upgrade

# Install only if not already installed
pip install -r requirements.txt --no-deps
```

### Multiple Requirements Files

Organize dependencies by purpose:

**requirements/base.txt** (core dependencies):
```txt
django>=4.1.0,<5.0.0
psycopg2-binary>=2.9.0
celery>=5.2.0
redis>=4.3.0
```

**requirements/development.txt** (development tools):
```txt
-r base.txt
pytest>=7.1.0
black>=22.6.0
flake8>=5.0.0
mypy>=0.971
django-debug-toolbar>=3.5.0
```

**requirements/production.txt** (production-specific):
```txt
-r base.txt
gunicorn>=20.1.0
whitenoise>=6.2.0
sentry-sdk>=1.9.0
```

**requirements/testing.txt** (testing dependencies):
```txt
-r base.txt
pytest>=7.1.0
pytest-django>=4.5.0
pytest-cov>=3.0.0
factory-boy>=3.2.0
```

## Advanced pip Features

### Installing from Different Sources

```bash
# Install from PyPI (default)
pip install requests

# Install from Git repository
pip install git+https://github.com/user/repo.git

# Install from specific branch/tag
pip install git+https://github.com/user/repo.git@branch_name
pip install git+https://github.com/user/repo.git@v1.2.3

# Install from local directory
pip install /path/to/local/package
pip install ./local_package

# Install in editable mode (development)
pip install -e ./local_package
```

### Installing with Extra Dependencies

Many packages offer optional dependencies:

```bash
# Install with extras
pip install requests[security]
pip install django[bcrypt,argon2]

# Multiple extras
pip install package[extra1,extra2]
```

### Constraints Files

Constraints files limit versions without requiring installation:

**constraints.txt**:
```txt
urllib3<2.0.0
certifi>=2021.10.8
```

```bash
# Install with constraints
pip install -r requirements.txt -c constraints.txt
```

## Dependency Resolution and Conflicts

### Understanding Dependency Trees

```bash
# Show dependency tree
pip show package_name

# Use pipdeptree for better visualization
pip install pipdeptree
pipdeptree
```

### Handling Conflicts

When packages have conflicting dependencies:

```bash
# Check for conflicts
pip check

# Force reinstall to resolve conflicts
pip install --force-reinstall package_name

# Install without dependencies (dangerous)
pip install --no-deps package_name
```

### Example Conflict Resolution

```txt
# Problem: Package A needs requests>=2.25.0
#          Package B needs requests<2.20.0

# Solution 1: Find compatible versions
package-a==1.0.0  # Uses requests>=2.18.0
package-b==2.1.0  # Uses requests<2.25.0
requests==2.24.0  # Satisfies both

# Solution 2: Use alternative packages
# Replace one package with a compatible alternative
```

## Package Security and Updates

### Checking for Security Issues

```bash
# Install safety tool
pip install safety

# Check for known vulnerabilities
safety check

# Check specific requirements file
safety check -r requirements.txt
```

### Updating Packages Safely

```bash
# Check outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package_name

# Update all packages (be careful!)
pip freeze | cut -d'=' -f1 | xargs pip install --upgrade
```

### Pinning Critical Dependencies

```txt
# Pin critical packages to specific versions
django==4.1.7  # Security-critical
psycopg2-binary==2.9.5  # Database driver

# Allow updates for less critical packages
requests>=2.28.0
beautifulsoup4~=4.11.0
```

## Best Practices for Dependency Management

### 1. Use Virtual Environments

Always use virtual environments to isolate project dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### 2. Pin Dependencies in Production

**requirements.txt** (production):
```txt
django==4.1.7
psycopg2-binary==2.9.5
gunicorn==20.1.0
redis==4.5.1
```

**requirements-dev.txt** (development):
```txt
-r requirements.txt
pytest>=7.1.0
black>=22.6.0
```

### 3. Regular Dependency Audits

```bash
# Monthly dependency review
pip list --outdated
safety check
pip check
```

### 4. Document Python Version Requirements

**requirements.txt**:
```txt
# Python 3.9+ required
django>=4.1.0
asyncio-mqtt>=0.11.0  # Requires Python 3.7+
```

### 5. Use Dependency Groups

Organize dependencies by purpose:

```txt
# Core application dependencies
django>=4.1.0,<5.0.0
celery>=5.2.0

# Development dependencies
pytest>=7.1.0
black>=22.6.0

# Production dependencies
gunicorn>=20.1.0
```

## Advanced Dependency Management Tools

### pip-tools

Better dependency management with compilation:

```bash
# Install pip-tools
pip install pip-tools

# Create requirements.in
echo "django" > requirements.in
echo "requests" >> requirements.in

# Compile to requirements.txt with exact versions
pip-compile requirements.in

# Update dependencies
pip-compile --upgrade requirements.in

# Sync environment with requirements
pip-sync requirements.txt
```

### Poetry

Modern dependency management:

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Initialize project
poetry init

# Add dependencies
poetry add django
poetry add pytest --group dev

# Install dependencies
poetry install

# Update dependencies
poetry update
```

### Pipenv

Combines pip and virtualenv:

```bash
# Install Pipenv
pip install pipenv

# Create environment and install packages
pipenv install django
pipenv install pytest --dev

# Activate shell
pipenv shell

# Install from Pipfile
pipenv install
```

## Dependency Management Workflows

### Development Workflow

```bash
# 1. Set up environment
python -m venv venv
source venv/bin/activate

# 2. Install base dependencies
pip install -r requirements.txt

# 3. Install development dependencies
pip install -r requirements-dev.txt

# 4. Add new dependency
pip install new-package

# 5. Update requirements
pip freeze > requirements.txt
```

### Production Deployment

```bash
# 1. Create clean environment
python -m venv prod_venv
source prod_venv/bin/activate

# 2. Install exact versions
pip install -r requirements.txt

# 3. Verify installation
pip check
safety check

# 4. Run application
python app.py
```

### Continuous Integration

**.github/workflows/test.yml**:
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    - name: Run tests
      run: pytest
    - name: Check security
      run: safety check
```

## Troubleshooting Common Issues

### 1. Package Not Found

```bash
# Update pip
pip install --upgrade pip

# Check package name
pip search package_name  # If available

# Try alternative index
pip install -i https://pypi.org/simple/ package_name
```

### 2. Permission Errors

```bash
# Use user installation
pip install --user package_name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package_name
```

### 3. Dependency Conflicts

```bash
# Check conflicts
pip check

# Create fresh environment
python -m venv fresh_env
source fresh_env/bin/activate
pip install -r requirements.txt
```

### 4. Slow Installation

```bash
# Use faster index
pip install -i https://pypi.douban.com/simple/ package_name

# Install without cache
pip install --no-cache-dir package_name

# Use wheel packages
pip install --only-binary=all package_name
```

## Example: Complete Project Setup

**Project Structure**:
```
my_project/
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── src/
│   └── my_project/
├── tests/
├── setup.py
└── README.md
```

**requirements/base.txt**:
```txt
django>=4.1.0,<5.0.0
psycopg2-binary>=2.9.0
celery>=5.2.0
redis>=4.3.0
python-decouple>=3.6
```

**requirements/development.txt**:
```txt
-r base.txt
pytest>=7.1.0
pytest-django>=4.5.0
black>=22.6.0
flake8>=5.0.0
mypy>=0.971
django-debug-toolbar>=3.5.0
ipython>=8.4.0
```

**requirements/production.txt**:
```txt
-r base.txt
gunicorn>=20.1.0
whitenoise>=6.2.0
sentry-sdk[django]>=1.9.0
```

**Setup Script** (setup.sh):
```bash
#!/bin/bash
set -e

echo "Setting up development environment..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements/development.txt

# Run initial setup
python manage.py migrate
python manage.py collectstatic --noinput

echo "Setup complete! Activate with: source venv/bin/activate"
```

## Summary

Effective dependency management involves:

1. **Use virtual environments** for isolation
2. **Pin versions** for reproducibility
3. **Organize dependencies** by purpose
4. **Regular security audits** with tools like safety
5. **Document requirements** clearly
6. **Test in clean environments** before deployment
7. **Keep dependencies updated** but test thoroughly
8. **Use appropriate tools** (pip, pip-tools, Poetry, etc.)

Good dependency management ensures your projects are:
- **Reproducible** across different environments
- **Secure** with up-to-date packages
- **Maintainable** with clear dependency documentation
- **Reliable** with tested dependency combinations

In the next lesson, we'll put all these concepts together in a comprehensive mini-project.