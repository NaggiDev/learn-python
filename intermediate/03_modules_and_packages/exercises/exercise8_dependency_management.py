"""
Exercise 8: Dependency Management with pip

This exercise focuses on practical dependency management techniques
including requirements files, version pinning, and conflict resolution.

Instructions:
1. Follow the step-by-step exercises below
2. Use this script to verify your dependency management setup
3. Practice different dependency scenarios
"""

import sys
import os
import subprocess
import json
import tempfile
from pathlib import Path
import re

def check_pip_version():
    """Check pip version and capabilities."""
    print("Checking pip Version:")
    print("-" * 20)
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {result.stdout.strip()}")
            
            # Extract version number
            version_match = re.search(r'pip (\d+\.\d+)', result.stdout)
            if version_match:
                version = float(version_match.group(1))
                if version >= 21.0:
                    print("✓ pip version supports modern features")
                else:
                    print("⚠ Consider upgrading pip: pip install --upgrade pip")
            return True
        else:
            print("✗ Error checking pip version")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def analyze_current_environment():
    """Analyze the current Python environment."""
    print("\nCurrent Environment Analysis:")
    print("-" * 30)
    
    # Check if in virtual environment
    in_venv = 'VIRTUAL_ENV' in os.environ or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print("✓ Running in virtual environment")
        if 'VIRTUAL_ENV' in os.environ:
            print(f"  Path: {os.environ['VIRTUAL_ENV']}")
    else:
        print("⚠ Not in virtual environment (recommended for exercises)")
    
    # Get package count
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            packages = json.loads(result.stdout)
            print(f"✓ {len(packages)} packages installed")
            
            # Show some key packages
            key_packages = ['pip', 'setuptools', 'wheel']
            for pkg_info in packages:
                if pkg_info['name'].lower() in key_packages:
                    print(f"  {pkg_info['name']}: {pkg_info['version']}")
        else:
            print("✗ Error getting package list")
    except Exception as e:
        print(f"✗ Error analyzing environment: {e}")

def create_sample_requirements():
    """Create sample requirements files for exercises."""
    print("\nCreating Sample Requirements Files:")
    print("-" * 35)
    
    # Create requirements directory
    req_dir = Path("requirements_exercise")
    req_dir.mkdir(exist_ok=True)
    
    # Basic requirements.txt
    basic_req = req_dir / "basic_requirements.txt"
    basic_content = """# Basic requirements - no version pinning
requests
click
python-dateutil
"""
    basic_req.write_text(basic_content)
    print(f"✓ Created {basic_req}")
    
    # Pinned requirements.txt
    pinned_req = req_dir / "pinned_requirements.txt"
    pinned_content = """# Pinned requirements - exact versions
requests==2.28.1
click==8.1.3
python-dateutil==2.8.2
"""
    pinned_req.write_text(pinned_content)
    print(f"✓ Created {pinned_req}")
    
    # Flexible requirements.txt
    flexible_req = req_dir / "flexible_requirements.txt"
    flexible_content = """# Flexible requirements - version ranges
requests>=2.25.0,<3.0.0
click~=8.1.0
python-dateutil>=2.8.0
urllib3>=1.26.0,!=1.26.5
"""
    flexible_req.write_text(flexible_content)
    print(f"✓ Created {flexible_req}")
    
    # Development requirements.txt
    dev_req = req_dir / "dev_requirements.txt"
    dev_content = """# Development requirements
-r pinned_requirements.txt
pytest>=7.1.0
black>=22.6.0
flake8>=5.0.0
mypy>=0.971
"""
    dev_req.write_text(dev_content)
    print(f"✓ Created {dev_req}")
    
    # Production requirements.txt
    prod_req = req_dir / "prod_requirements.txt"
    prod_content = """# Production requirements
-r pinned_requirements.txt
gunicorn>=20.1.0
whitenoise>=6.2.0
"""
    prod_req.write_text(prod_content)
    print(f"✓ Created {prod_req}")
    
    return req_dir

def demonstrate_pip_commands():
    """Demonstrate various pip commands."""
    print("\nDemonstrating pip Commands:")
    print("-" * 28)
    
    commands = [
        ("pip list", "List installed packages"),
        ("pip list --outdated", "Show outdated packages"),
        ("pip show requests", "Show package details"),
        ("pip check", "Check for dependency conflicts"),
    ]
    
    for cmd, description in commands:
        print(f"\n{description}:")
        print(f"Command: {cmd}")
        
        try:
            # Split command for subprocess
            cmd_parts = cmd.split()
            cmd_parts[0] = sys.executable
            cmd_parts.insert(1, '-m')
            
            result = subprocess.run(cmd_parts, capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                output = result.stdout.strip()
                if len(output) > 300:  # Truncate long output
                    lines = output.split('\n')
                    print(f"✓ Success (showing first 5 lines):")
                    for line in lines[:5]:
                        print(f"  {line}")
                    if len(lines) > 5:
                        print(f"  ... and {len(lines) - 5} more lines")
                else:
                    print(f"✓ Success:")
                    for line in output.split('\n')[:10]:  # Max 10 lines
                        print(f"  {line}")
            else:
                print(f"✗ Error: {result.stderr.strip()}")
                
        except subprocess.TimeoutExpired:
            print("✗ Command timed out")
        except Exception as e:
            print(f"✗ Error running command: {e}")

def analyze_requirements_file(filepath):
    """Analyze a requirements file."""
    print(f"\nAnalyzing {filepath.name}:")
    print("-" * (12 + len(filepath.name)))
    
    if not filepath.exists():
        print(f"✗ File not found: {filepath}")
        return
    
    content = filepath.read_text()
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    packages = []
    includes = []
    comments = []
    
    for line in lines:
        if line.startswith('#'):
            comments.append(line)
        elif line.startswith('-r '):
            includes.append(line[3:])
        elif line and not line.startswith('-'):
            packages.append(line)
    
    print(f"✓ {len(packages)} package requirements")
    print(f"✓ {len(includes)} included files")
    print(f"✓ {len(comments)} comment lines")
    
    if packages:
        print("Package requirements:")
        for pkg in packages:
            # Parse package specification
            if '==' in pkg:
                name, version = pkg.split('==', 1)
                print(f"  📌 {name}: exactly {version}")
            elif '>=' in pkg and '<' in pkg:
                print(f"  📊 {pkg}: version range")
            elif '~=' in pkg:
                print(f"  🔄 {pkg}: compatible release")
            elif '>=' in pkg:
                name, version = pkg.split('>=', 1)
                print(f"  ⬆️ {name}: minimum {version}")
            else:
                print(f"  📦 {pkg}: any version")
    
    if includes:
        print("Included files:")
        for inc in includes:
            print(f"  📄 {inc}")

def simulate_dependency_scenarios():
    """Simulate common dependency management scenarios."""
    print("\nDependency Management Scenarios:")
    print("-" * 32)
    
    scenarios = [
        {
            "name": "Scenario 1: Fresh Project Setup",
            "description": "Setting up dependencies for a new project",
            "steps": [
                "1. Create virtual environment: python -m venv project_env",
                "2. Activate environment",
                "3. Install from requirements: pip install -r requirements.txt",
                "4. Verify installation: pip list"
            ]
        },
        {
            "name": "Scenario 2: Adding New Dependency",
            "description": "Adding a new package to existing project",
            "steps": [
                "1. Install new package: pip install new-package",
                "2. Test that it works in your code",
                "3. Update requirements: pip freeze > requirements.txt",
                "4. Or manually add to requirements with version"
            ]
        },
        {
            "name": "Scenario 3: Updating Dependencies",
            "description": "Safely updating project dependencies",
            "steps": [
                "1. Check outdated: pip list --outdated",
                "2. Update specific package: pip install --upgrade package-name",
                "3. Test your application thoroughly",
                "4. Update requirements file if tests pass"
            ]
        },
        {
            "name": "Scenario 4: Resolving Conflicts",
            "description": "Handling dependency conflicts",
            "steps": [
                "1. Check for conflicts: pip check",
                "2. Identify conflicting packages",
                "3. Find compatible versions",
                "4. Update requirements with compatible versions"
            ]
        }
    ]
    
    for scenario in scenarios:
        print(f"\n{scenario['name']}:")
        print(f"Description: {scenario['description']}")
        print("Steps:")
        for step in scenario['steps']:
            print(f"  {step}")

def provide_exercises():
    """Provide hands-on dependency management exercises."""
    print("\n" + "=" * 60)
    print("DEPENDENCY MANAGEMENT EXERCISES")
    print("=" * 60)
    
    print("\nEXERCISE 1: Basic Requirements Management")
    print("-" * 40)
    print("1. Create a new virtual environment:")
    print("   python -m venv deps_exercise")
    print("2. Activate the environment")
    print("3. Install packages individually:")
    print("   pip install requests")
    print("   pip install click")
    print("   pip install python-dateutil")
    print("4. Generate requirements file:")
    print("   pip freeze > my_requirements.txt")
    print("5. Examine the generated file")
    print("6. Create a new environment and install from requirements:")
    print("   python -m venv test_env")
    print("   # Activate test_env")
    print("   pip install -r my_requirements.txt")
    
    print("\nEXERCISE 2: Version Pinning Practice")
    print("-" * 35)
    print("1. Use the pinned_requirements.txt file created earlier")
    print("2. Create environment: python -m venv pinned_env")
    print("3. Activate and install: pip install -r requirements_exercise/pinned_requirements.txt")
    print("4. Verify exact versions: pip list")
    print("5. Try to upgrade a package: pip install --upgrade requests")
    print("6. Notice how it upgrades despite pinning")
    print("7. Reinstall from requirements to restore pinned versions")
    
    print("\nEXERCISE 3: Flexible Version Ranges")
    print("-" * 32)
    print("1. Use flexible_requirements.txt")
    print("2. Create environment: python -m venv flexible_env")
    print("3. Install: pip install -r requirements_exercise/flexible_requirements.txt")
    print("4. Check what versions were installed: pip list")
    print("5. Try upgrading within constraints: pip install --upgrade requests")
    print("6. Observe how versions stay within specified ranges")
    
    print("\nEXERCISE 4: Development vs Production Dependencies")
    print("-" * 50)
    print("1. Create production environment:")
    print("   python -m venv prod_env")
    print("   # Activate and install")
    print("   pip install -r requirements_exercise/prod_requirements.txt")
    print("2. Create development environment:")
    print("   python -m venv dev_env")
    print("   # Activate and install")
    print("   pip install -r requirements_exercise/dev_requirements.txt")
    print("3. Compare package lists between environments")
    print("4. Notice how dev environment includes testing tools")
    
    print("\nEXERCISE 5: Dependency Conflict Resolution")
    print("-" * 40)
    print("1. Create environment: python -m venv conflict_test")
    print("2. Install conflicting packages:")
    print("   pip install 'requests==2.25.0'")
    print("   pip install 'urllib3==1.26.8'  # May conflict")
    print("3. Check for conflicts: pip check")
    print("4. If conflicts exist, find compatible versions")
    print("5. Create requirements.txt with compatible versions")
    
    print("\nEXERCISE 6: Security and Updates")
    print("-" * 30)
    print("1. Install safety tool: pip install safety")
    print("2. Check for vulnerabilities: safety check")
    print("3. Check outdated packages: pip list --outdated")
    print("4. Create update strategy for your requirements")
    print("5. Test updates in isolated environment first")
    
    print("\nEXERCISE 7: Advanced pip Features")
    print("-" * 30)
    print("1. Install from Git repository:")
    print("   pip install git+https://github.com/psf/requests.git")
    print("2. Install with extras:")
    print("   pip install 'requests[security]'")
    print("3. Install in editable mode (if you have local package):")
    print("   pip install -e ./my_local_package")
    print("4. Use constraints file:")
    print("   echo 'urllib3<2.0.0' > constraints.txt")
    print("   pip install -r requirements.txt -c constraints.txt")

def main():
    """Run dependency management exercises and demonstrations."""
    print("Dependency Management with pip")
    print("=" * 35)
    
    # Check pip and environment
    if not check_pip_version():
        return
    
    analyze_current_environment()
    
    # Create sample files
    req_dir = create_sample_requirements()
    
    # Demonstrate pip commands
    demonstrate_pip_commands()
    
    # Analyze sample requirements files
    for req_file in req_dir.glob("*.txt"):
        analyze_requirements_file(req_file)
    
    # Show scenarios and exercises
    simulate_dependency_scenarios()
    provide_exercises()
    
    print("\n" + "=" * 60)
    print("DEPENDENCY MANAGEMENT BEST PRACTICES:")
    print("=" * 60)
    print("✓ Always use virtual environments")
    print("✓ Pin versions in production requirements")
    print("✓ Use version ranges for development flexibility")
    print("✓ Separate requirements by environment (dev/prod/test)")
    print("✓ Regularly check for security vulnerabilities")
    print("✓ Test dependency updates in isolated environments")
    print("✓ Document Python version requirements")
    print("✓ Use pip check to verify dependency compatibility")
    print("✓ Keep requirements files in version control")
    print("✓ Consider using tools like pip-tools or Poetry for complex projects")
    
    print(f"\nSample requirements files created in: {req_dir.absolute()}")
    print("Use these files to practice the exercises above!")

if __name__ == "__main__":
    main()

# Additional advanced topics to explore:
# 1. Using pip-tools for better dependency management
# 2. Creating and publishing your own packages to PyPI
# 3. Using private package repositories
# 4. Dependency management in Docker containers
# 5. Automated dependency updates with tools like Dependabot