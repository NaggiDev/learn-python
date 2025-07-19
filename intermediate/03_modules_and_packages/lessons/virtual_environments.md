# Virtual Environments

## What are Virtual Environments?

A virtual environment is an isolated Python environment that allows you to install packages and dependencies for a specific project without affecting your system-wide Python installation or other projects. Think of it as a separate "sandbox" for each project.

## Why Use Virtual Environments?

### 1. Dependency Isolation
Different projects may require different versions of the same package. Virtual environments prevent conflicts between these requirements.

```
Project A needs Django 3.2
Project B needs Django 4.1
System Python has Django 2.1
```

Without virtual environments, you'd have conflicts. With virtual environments, each project gets its own Django version.

### 2. Clean System Python
Keep your system Python installation clean and minimal, reducing the risk of breaking system tools that depend on Python.

### 3. Reproducible Environments
Share exact dependency versions with team members or deploy to production with confidence.

### 4. Easy Cleanup
Delete a virtual environment to completely remove all its packages without affecting anything else.

## Creating Virtual Environments

Python 3.3+ includes the `venv` module for creating virtual environments.

### Basic Creation

```bash
# Create a virtual environment named 'myenv'
python -m venv myenv

# On some systems, you might need to use python3
python3 -m venv myenv
```

This creates a directory structure:
```
myenv/
├── bin/           # Scripts (Linux/Mac)
├── Scripts/       # Scripts (Windows)
├── include/       # C headers
├── lib/           # Python packages
└── pyvenv.cfg     # Configuration
```

### Creating with Specific Python Version

```bash
# Use a specific Python version
python3.9 -m venv myenv

# Or specify the full path
/usr/bin/python3.9 -m venv myenv
```

## Activating Virtual Environments

### Linux/Mac
```bash
# Activate the environment
source myenv/bin/activate

# Your prompt will change to show the active environment
(myenv) $ python --version
```

### Windows Command Prompt
```cmd
# Activate the environment
myenv\Scripts\activate.bat

# Your prompt will change
(myenv) C:\> python --version
```

### Windows PowerShell
```powershell
# You might need to change execution policy first
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Activate the environment
myenv\Scripts\Activate.ps1

# Your prompt will change
(myenv) PS C:\> python --version
```

## Working with Virtual Environments

### Check Active Environment
```bash
# Check if an environment is active
echo $VIRTUAL_ENV  # Linux/Mac
echo %VIRTUAL_ENV%  # Windows

# Check Python location
which python  # Linux/Mac
where python  # Windows
```

### Install Packages
```bash
# Install packages (only affects the virtual environment)
pip install requests
pip install django==4.1
pip install -r requirements.txt
```

### List Installed Packages
```bash
# List packages in the current environment
pip list

# Show package details
pip show requests
```

## Deactivating Virtual Environments

```bash
# Deactivate the current environment
deactivate

# Your prompt returns to normal
$ python --version  # Now uses system Python
```

## Virtual Environment Best Practices

### 1. One Environment Per Project
```
projects/
├── web_app/
│   ├── venv/
│   ├── app.py
│   └── requirements.txt
├── data_analysis/
│   ├── venv/
│   ├── analysis.py
│   └── requirements.txt
└── api_service/
    ├── venv/
    ├── server.py
    └── requirements.txt
```

### 2. Consistent Naming
Use consistent names for virtual environments:
- `venv` (most common)
- `env`
- `.venv` (hidden directory)

### 3. Add to .gitignore
Never commit virtual environments to version control:

```gitignore
# Virtual environments
venv/
env/
.venv/
ENV/
```

### 4. Document Dependencies
Always maintain a `requirements.txt` file:

```bash
# Generate requirements file
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

## Advanced Virtual Environment Usage

### Creating with System Site Packages
```bash
# Include system packages in the virtual environment
python -m venv --system-site-packages myenv
```

### Upgrading pip in Virtual Environment
```bash
# Activate environment first
source myenv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip
```

### Creating Lightweight Environments
```bash
# Create without pip (smaller, faster)
python -m venv --without-pip myenv

# Install pip later if needed
source myenv/bin/activate
python -m ensurepip --upgrade
```

## Alternative Virtual Environment Tools

### virtualenv (Third-party)
More features and faster than venv:

```bash
# Install virtualenv
pip install virtualenv

# Create environment
virtualenv myenv

# With specific Python version
virtualenv -p python3.9 myenv
```

### conda (Anaconda/Miniconda)
Popular in data science:

```bash
# Create environment
conda create -n myenv python=3.9

# Activate
conda activate myenv

# Install packages
conda install numpy pandas
```

### pipenv
Combines pip and virtualenv:

```bash
# Install pipenv
pip install pipenv

# Create environment and install packages
pipenv install requests

# Activate shell
pipenv shell
```

## Virtual Environment Workflows

### Development Workflow
```bash
# 1. Create project directory
mkdir my_project
cd my_project

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# 4. Install dependencies
pip install requests flask

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Work on your project
# ... coding ...

# 7. Deactivate when done
deactivate
```

### Team Collaboration Workflow
```bash
# Team member clones project
git clone https://github.com/team/project.git
cd project

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Start working
python app.py
```

### Production Deployment Workflow
```bash
# On production server
git clone https://github.com/company/app.git
cd app

# Create production environment
python -m venv venv
source venv/bin/activate

# Install only production dependencies
pip install -r requirements.txt

# Run application
python app.py
```

## Troubleshooting Virtual Environments

### Common Issues

#### 1. Permission Errors
```bash
# If you get permission errors on Windows
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 2. Wrong Python Version
```bash
# Check which Python is being used
which python
python --version

# Make sure you're in the right environment
echo $VIRTUAL_ENV
```

#### 3. Packages Not Found
```bash
# Make sure environment is activated
source venv/bin/activate

# Check if package is installed
pip list | grep package_name

# Reinstall if necessary
pip install package_name
```

#### 4. Environment Not Activating
```bash
# Check if activation script exists
ls venv/bin/activate      # Linux/Mac
dir venv\Scripts\activate.bat  # Windows

# Recreate if corrupted
rm -rf venv
python -m venv venv
```

### Debugging Commands
```bash
# Check Python executable location
which python

# Check pip location
which pip

# Check installed packages
pip list

# Check environment variables
env | grep VIRTUAL  # Linux/Mac
set | findstr VIRTUAL  # Windows
```

## Virtual Environment Scripts

### Activation Script (Linux/Mac)
Create `activate_env.sh`:
```bash
#!/bin/bash
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "Virtual environment activated"
else
    echo "Virtual environment not found"
    echo "Create one with: python -m venv venv"
fi
```

### Setup Script (Windows)
Create `setup_env.bat`:
```batch
@echo off
if exist venv (
    echo Activating existing virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo Creating new virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing requirements...
    pip install -r requirements.txt
)
```

## Environment Management Tips

### 1. Use Descriptive Names
```bash
# Good
python -m venv django_blog_env
python -m venv data_analysis_env

# Less clear
python -m venv env1
python -m venv temp
```

### 2. Document Python Version
Include Python version in your README:
```markdown
## Setup
This project requires Python 3.9+

1. Create virtual environment: `python3.9 -m venv venv`
2. Activate: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
```

### 3. Regular Cleanup
```bash
# Remove unused environments
rm -rf old_project_venv

# Clean pip cache
pip cache purge
```

### 4. Environment Testing
```bash
# Test clean environment
python -m venv test_env
source test_env/bin/activate
pip install -r requirements.txt
python -m pytest
deactivate
rm -rf test_env
```

## Integration with IDEs

### VS Code
1. Open project folder
2. Press `Ctrl+Shift+P`
3. Type "Python: Select Interpreter"
4. Choose the Python executable from your virtual environment

### PyCharm
1. File → Settings → Project → Python Interpreter
2. Click gear icon → Add
3. Select "Existing environment"
4. Browse to your virtual environment's Python executable

### Jupyter Notebooks
```bash
# Install ipykernel in your virtual environment
pip install ipykernel

# Add environment as Jupyter kernel
python -m ipykernel install --user --name=myenv --display-name="My Environment"

# Start Jupyter and select your kernel
jupyter notebook
```

## Summary

Virtual environments are essential for Python development:

1. **Create**: `python -m venv venv`
2. **Activate**: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. **Install**: `pip install package_name`
4. **Save**: `pip freeze > requirements.txt`
5. **Deactivate**: `deactivate`

Key benefits:
- Dependency isolation
- Clean system Python
- Reproducible environments
- Easy project sharing
- Safe experimentation

Always use virtual environments for Python projects to avoid dependency conflicts and maintain clean, reproducible development environments.

In the next lesson, we'll explore dependency management with pip and requirements files in more detail.