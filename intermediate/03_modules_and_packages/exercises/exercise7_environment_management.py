"""
Exercise 7: Advanced Environment Management

This exercise focuses on advanced virtual environment management techniques
including environment recreation, dependency management, and automation.

Instructions:
1. Complete the basic virtual environment exercise first
2. Follow the advanced scenarios below
3. Use this script to verify your setups
"""

import sys
import os
import subprocess
import json
import tempfile
from pathlib import Path

def create_sample_project():
    """Create a sample project structure for testing."""
    print("Creating Sample Project Structure:")
    print("-" * 35)
    
    # Create temporary project directory
    project_dir = Path("sample_project")
    
    if project_dir.exists():
        print(f"✓ Project directory already exists: {project_dir}")
    else:
        project_dir.mkdir()
        print(f"✓ Created project directory: {project_dir}")
    
    # Create sample files
    files_to_create = {
        "app.py": '''#!/usr/bin/env python3
"""
Sample application for virtual environment testing.
"""

import requests
import json
from datetime import datetime

def get_current_time():
    """Get current time as string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def fetch_data(url):
    """Fetch data from URL."""
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def main():
    """Main application function."""
    print(f"Sample App started at {get_current_time()}")
    
    # Test requests library
    print("Testing requests library...")
    data = fetch_data("https://httpbin.org/json")
    print(f"Fetched data: {data}")

if __name__ == "__main__":
    main()
''',
        "requirements.txt": '''requests==2.28.1
python-dateutil==2.8.2
click>=8.0.0
''',
        "requirements-dev.txt": '''# Development dependencies
-r requirements.txt
pytest==7.1.2
black==22.6.0
flake8==5.0.4
''',
        "README.md": '''# Sample Project

This is a sample project for virtual environment testing.

## Setup

1. Create virtual environment: `python -m venv venv`
2. Activate environment: `source venv/bin/activate` (Linux/Mac) or `venv\\Scripts\\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run application: `python app.py`

## Development Setup

For development, install dev dependencies:
```bash
pip install -r requirements-dev.txt
```
''',
        ".gitignore": '''# Virtual environments
venv/
env/
.venv/
ENV/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
'''
    }
    
    for filename, content in files_to_create.items():
        file_path = project_dir / filename
        if not file_path.exists():
            file_path.write_text(content)
            print(f"✓ Created {filename}")
        else:
            print(f"✓ {filename} already exists")
    
    return project_dir

def check_environment_isolation():
    """Check if current environment is properly isolated."""
    print("\nEnvironment Isolation Check:")
    print("-" * 28)
    
    # Check if in virtual environment
    in_venv = 'VIRTUAL_ENV' in os.environ or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print("✓ Running in virtual environment")
        if 'VIRTUAL_ENV' in os.environ:
            print(f"  Environment path: {os.environ['VIRTUAL_ENV']}")
    else:
        print("✗ Not in virtual environment")
        print("  Activate a virtual environment first!")
        return False
    
    # Check Python executable location
    python_exe = sys.executable
    print(f"Python executable: {python_exe}")
    
    # Check if Python is in the virtual environment
    if 'VIRTUAL_ENV' in os.environ:
        venv_path = os.environ['VIRTUAL_ENV']
        if venv_path in python_exe:
            print("✓ Using virtual environment Python")
        else:
            print("✗ Not using virtual environment Python")
            return False
    
    return True

def analyze_requirements_file(requirements_file):
    """Analyze a requirements file."""
    print(f"\nAnalyzing {requirements_file}:")
    print("-" * (12 + len(requirements_file)))
    
    if not os.path.exists(requirements_file):
        print(f"✗ {requirements_file} not found")
        return
    
    with open(requirements_file, 'r') as f:
        lines = f.readlines()
    
    packages = []
    includes = []
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        elif line.startswith('-r '):
            includes.append(line[3:])
        else:
            packages.append(line)
    
    print(f"✓ Found {len(packages)} package requirements")
    print(f"✓ Found {len(includes)} included files")
    
    if packages:
        print("Packages:")
        for pkg in packages[:5]:  # Show first 5
            print(f"  - {pkg}")
        if len(packages) > 5:
            print(f"  ... and {len(packages) - 5} more")
    
    if includes:
        print("Included files:")
        for inc in includes:
            print(f"  - {inc}")

def check_package_versions():
    """Check versions of installed packages."""
    print("\nPackage Version Check:")
    print("-" * 22)
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            packages = json.loads(result.stdout)
            print(f"✓ Found {len(packages)} installed packages")
            
            # Check for common packages
            common_packages = ['pip', 'setuptools', 'requests', 'flask', 'django']
            found_packages = {pkg['name'].lower(): pkg['version'] for pkg in packages}
            
            print("Common packages:")
            for pkg in common_packages:
                if pkg in found_packages:
                    print(f"  ✓ {pkg}: {found_packages[pkg]}")
                else:
                    print(f"  ✗ {pkg}: not installed")
        else:
            print("✗ Error getting package list")
    except Exception as e:
        print(f"✗ Error checking packages: {e}")

def simulate_environment_recreation():
    """Simulate recreating an environment from requirements."""
    print("\nEnvironment Recreation Simulation:")
    print("-" * 35)
    
    # This would normally be done in a fresh environment
    print("Steps to recreate environment:")
    print("1. Create new virtual environment")
    print("2. Activate the environment")
    print("3. Install from requirements.txt")
    print("4. Verify installation")
    
    # Check if we can simulate this
    requirements_file = "sample_project/requirements.txt"
    if os.path.exists(requirements_file):
        print(f"\n✓ Found requirements file: {requirements_file}")
        analyze_requirements_file(requirements_file)
        
        print("\nTo recreate this environment:")
        print("1. python -m venv new_env")
        print("2. source new_env/bin/activate  # Linux/Mac")
        print("   or new_env\\Scripts\\activate  # Windows")
        print(f"3. pip install -r {requirements_file}")
    else:
        print("✗ No requirements file found")

def provide_advanced_exercises():
    """Provide advanced virtual environment exercises."""
    print("\n" + "=" * 60)
    print("ADVANCED VIRTUAL ENVIRONMENT EXERCISES")
    print("=" * 60)
    
    print("\nEXERCISE 1: Project Environment Setup")
    print("-" * 35)
    print("1. Navigate to the sample_project directory")
    print("2. Create a virtual environment: python -m venv venv")
    print("3. Activate the environment")
    print("4. Install requirements: pip install -r requirements.txt")
    print("5. Test the application: python app.py")
    print("6. Check what was installed: pip list")
    
    print("\nEXERCISE 2: Development vs Production Environments")
    print("-" * 50)
    print("1. Create two environments:")
    print("   python -m venv prod_env")
    print("   python -m venv dev_env")
    print("2. In prod_env:")
    print("   - Activate and install: pip install -r requirements.txt")
    print("3. In dev_env:")
    print("   - Activate and install: pip install -r requirements-dev.txt")
    print("4. Compare package lists between environments")
    
    print("\nEXERCISE 3: Environment Cloning")
    print("-" * 30)
    print("1. From an existing environment, create requirements:")
    print("   pip freeze > current_requirements.txt")
    print("2. Create new environment: python -m venv cloned_env")
    print("3. Activate and install: pip install -r current_requirements.txt")
    print("4. Verify environments are identical: pip list")
    
    print("\nEXERCISE 4: Dependency Conflict Resolution")
    print("-" * 40)
    print("1. Create environment: python -m venv conflict_test")
    print("2. Try installing conflicting versions:")
    print("   pip install django==3.2")
    print("   pip install django==4.1")
    print("3. Observe how pip handles the conflict")
    print("4. Check final version: pip show django")
    
    print("\nEXERCISE 5: Environment Automation")
    print("-" * 30)
    print("Create setup scripts for your environments:")
    
    print("\nLinux/Mac setup script (setup.sh):")
    print("#!/bin/bash")
    print("python3 -m venv venv")
    print("source venv/bin/activate")
    print("pip install --upgrade pip")
    print("pip install -r requirements.txt")
    print("echo 'Environment ready!'")
    
    print("\nWindows setup script (setup.bat):")
    print("@echo off")
    print("python -m venv venv")
    print("call venv\\Scripts\\activate.bat")
    print("pip install --upgrade pip")
    print("pip install -r requirements.txt")
    print("echo Environment ready!")
    
    print("\nEXERCISE 6: Environment Health Check")
    print("-" * 35)
    print("Create a health check script that verifies:")
    print("1. Virtual environment is active")
    print("2. All required packages are installed")
    print("3. Package versions match requirements")
    print("4. No conflicting packages exist")
    
    print("\nEXERCISE 7: Multi-Python Version Testing")
    print("-" * 40)
    print("If you have multiple Python versions:")
    print("1. Create environments with different Python versions:")
    print("   python3.8 -m venv env38")
    print("   python3.9 -m venv env39")
    print("   python3.10 -m venv env310")
    print("2. Test your application in each environment")
    print("3. Note any compatibility issues")

def main():
    """Run advanced environment management exercises."""
    print("Advanced Virtual Environment Management")
    print("=" * 40)
    
    # Create sample project
    project_dir = create_sample_project()
    
    # Run checks
    if check_environment_isolation():
        analyze_requirements_file("sample_project/requirements.txt")
        analyze_requirements_file("sample_project/requirements-dev.txt")
        check_package_versions()
    
    simulate_environment_recreation()
    provide_advanced_exercises()
    
    print("\n" + "=" * 60)
    print("BEST PRACTICES SUMMARY:")
    print("=" * 60)
    print("✓ One virtual environment per project")
    print("✓ Always activate before installing packages")
    print("✓ Keep requirements.txt updated")
    print("✓ Use different requirements files for different environments")
    print("✓ Add virtual environment directories to .gitignore")
    print("✓ Document Python version requirements")
    print("✓ Test in clean environments before deployment")
    print("✓ Use automation scripts for consistent setup")
    
    print(f"\nSample project created in: {project_dir.absolute()}")
    print("Use this project to practice the exercises above!")

if __name__ == "__main__":
    main()

# Additional advanced topics to explore:
# 1. Using tox for testing across multiple Python versions
# 2. Docker containers as alternative to virtual environments
# 3. Poetry for advanced dependency management
# 4. Conda environments for data science projects
# 5. Virtual environment management with pyenv