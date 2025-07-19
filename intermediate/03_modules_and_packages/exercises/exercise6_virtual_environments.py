"""
Exercise 6: Virtual Environments Practice

This exercise will guide you through creating and managing virtual environments.
Since virtual environments are created and managed through command-line tools,
this Python file contains instructions and verification scripts.

Instructions:
1. Follow the step-by-step instructions below
2. Run this script to verify your virtual environment setup
3. Practice different virtual environment scenarios

Note: You'll need to run command-line commands outside of this script.
"""

import sys
import os
import subprocess
import platform

def check_python_version():
    """Check if Python version supports venv module."""
    print("Checking Python Version:")
    print("-" * 25)
    
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version >= (3, 3):
        print("✓ Python version supports venv module")
        return True
    else:
        print("✗ Python version too old for venv module")
        print("Please upgrade to Python 3.3 or later")
        return False

def check_venv_availability():
    """Check if venv module is available."""
    print("\nChecking venv Module:")
    print("-" * 20)
    
    try:
        import venv
        print("✓ venv module is available")
        return True
    except ImportError:
        print("✗ venv module not available")
        print("Try installing python3-venv package on your system")
        return False

def detect_virtual_environment():
    """Detect if currently running in a virtual environment."""
    print("\nVirtual Environment Detection:")
    print("-" * 30)
    
    # Check for virtual environment indicators
    in_venv = False
    venv_path = None
    
    # Method 1: Check VIRTUAL_ENV environment variable
    if 'VIRTUAL_ENV' in os.environ:
        in_venv = True
        venv_path = os.environ['VIRTUAL_ENV']
        print(f"✓ VIRTUAL_ENV detected: {venv_path}")
    
    # Method 2: Check sys.prefix vs sys.base_prefix
    elif hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
        in_venv = True
        venv_path = sys.prefix
        print(f"✓ Virtual environment detected: {venv_path}")
    
    # Method 3: Check for pyvenv.cfg file
    elif os.path.exists(os.path.join(sys.prefix, 'pyvenv.cfg')):
        in_venv = True
        venv_path = sys.prefix
        print(f"✓ pyvenv.cfg found: {venv_path}")
    
    if not in_venv:
        print("✗ Not currently in a virtual environment")
        print("Python executable:", sys.executable)
        print("Python prefix:", sys.prefix)
    
    return in_venv, venv_path

def show_python_path_info():
    """Show Python path information."""
    print("\nPython Path Information:")
    print("-" * 25)
    
    print(f"Python executable: {sys.executable}")
    print(f"Python prefix: {sys.prefix}")
    
    if hasattr(sys, 'base_prefix'):
        print(f"Base prefix: {sys.base_prefix}")
    
    print(f"Python path (first 3 entries):")
    for i, path in enumerate(sys.path[:3]):
        print(f"  {i+1}. {path}")

def check_pip_location():
    """Check pip location and version."""
    print("\nPip Information:")
    print("-" * 15)
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Pip version: {result.stdout.strip()}")
        else:
            print("✗ Pip not available or error occurred")
    except Exception as e:
        print(f"✗ Error checking pip: {e}")

def list_installed_packages():
    """List installed packages in current environment."""
    print("\nInstalled Packages:")
    print("-" * 18)
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'list'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            print(f"Total packages: {len(lines) - 2}")  # Subtract header lines
            print("First 10 packages:")
            for line in lines[2:12]:  # Skip header, show first 10
                print(f"  {line}")
            if len(lines) > 12:
                print(f"  ... and {len(lines) - 12} more")
        else:
            print("✗ Error listing packages")
    except Exception as e:
        print(f"✗ Error listing packages: {e}")

def provide_instructions():
    """Provide step-by-step instructions for virtual environment exercises."""
    print("\n" + "=" * 60)
    print("VIRTUAL ENVIRONMENT EXERCISES")
    print("=" * 60)
    
    system = platform.system().lower()
    
    print("\nEXERCISE 1: Create Your First Virtual Environment")
    print("-" * 50)
    print("1. Open a terminal/command prompt")
    print("2. Navigate to a directory where you want to create the environment")
    print("3. Create a virtual environment:")
    print("   python -m venv my_first_venv")
    print("   (or python3 -m venv my_first_venv on some systems)")
    print()
    
    if system == "windows":
        print("4. Activate the environment:")
        print("   my_first_venv\\Scripts\\activate")
        print("   (or my_first_venv\\Scripts\\Activate.ps1 in PowerShell)")
    else:
        print("4. Activate the environment:")
        print("   source my_first_venv/bin/activate")
    
    print("5. Verify activation by checking your prompt")
    print("6. Run this script again to see the difference!")
    print()
    
    print("EXERCISE 2: Package Installation Practice")
    print("-" * 40)
    print("1. With your virtual environment activated:")
    print("2. Install a package: pip install requests")
    print("3. Check installed packages: pip list")
    print("4. Install specific version: pip install flask==2.0.1")
    print("5. Save requirements: pip freeze > requirements.txt")
    print("6. View the requirements file: cat requirements.txt (Linux/Mac)")
    print("   or type requirements.txt (Windows)")
    print()
    
    print("EXERCISE 3: Environment Isolation Test")
    print("-" * 35)
    print("1. Create two different virtual environments:")
    print("   python -m venv env1")
    print("   python -m venv env2")
    print("2. Activate env1 and install requests")
    print("3. Activate env2 and install flask")
    print("4. Switch between environments and check 'pip list'")
    print("5. Notice how packages are isolated!")
    print()
    
    print("EXERCISE 4: Requirements File Practice")
    print("-" * 35)
    print("1. Create a new virtual environment: python -m venv project_env")
    if system == "windows":
        print("2. Activate it: project_env\\Scripts\\activate")
    else:
        print("2. Activate it: source project_env/bin/activate")
    print("3. Create a requirements.txt file with these contents:")
    print("   requests==2.28.1")
    print("   flask==2.2.2")
    print("   click>=8.0.0")
    print("4. Install from requirements: pip install -r requirements.txt")
    print("5. Verify installation: pip list")
    print()
    
    print("EXERCISE 5: Cleanup Practice")
    print("-" * 25)
    print("1. Deactivate any active environment: deactivate")
    print("2. Remove test environments:")
    if system == "windows":
        print("   rmdir /s my_first_venv")
        print("   rmdir /s env1")
        print("   rmdir /s env2")
    else:
        print("   rm -rf my_first_venv")
        print("   rm -rf env1")
        print("   rm -rf env2")
    print("3. Keep project_env for future exercises")
    print()
    
    print("TROUBLESHOOTING TIPS:")
    print("-" * 20)
    if system == "windows":
        print("• If PowerShell gives execution policy errors:")
        print("  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser")
    print("• If 'python' command not found, try 'python3'")
    print("• If venv module not found, install python3-venv package")
    print("• Always activate environment before installing packages")
    print("• Use 'which python' (Linux/Mac) or 'where python' (Windows)")
    print("  to verify you're using the right Python")

def main():
    """Run all virtual environment checks and provide instructions."""
    print("Virtual Environment Exercise and Verification")
    print("=" * 50)
    
    # Run checks
    if not check_python_version():
        return
    
    if not check_venv_availability():
        return
    
    in_venv, venv_path = detect_virtual_environment()
    show_python_path_info()
    check_pip_location()
    list_installed_packages()
    
    # Provide instructions
    provide_instructions()
    
    print("\n" + "=" * 60)
    if in_venv:
        print("✓ You are currently in a virtual environment!")
        print(f"Environment path: {venv_path}")
        print("Great! You can practice the exercises above.")
    else:
        print("ℹ You are not in a virtual environment.")
        print("Follow the exercises above to create and activate one,")
        print("then run this script again to see the difference!")
    
    print("\nRemember:")
    print("• Always use virtual environments for Python projects")
    print("• One environment per project")
    print("• Add venv/ to your .gitignore file")
    print("• Keep requirements.txt updated")

if __name__ == "__main__":
    main()

# Additional exercises to try:
# 1. Create a virtual environment with a specific Python version
# 2. Practice with different activation methods
# 3. Try creating environments in different locations
# 4. Experiment with --system-site-packages option
# 5. Practice environment recreation from requirements.txt