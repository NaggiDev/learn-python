"""
Solution: Verify Python Installation and Setup

This is the solution to the Python installation verification exercise.
It demonstrates how to check Python version, system information, and more.
"""

import sys
import platform
import datetime
import os
import pkg_resources

def check_python_installation():
    """Check Python installation and print system information."""
    print("=" * 50)
    print("Python Installation Verification")
    print("=" * 50)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    print(f"Python version info: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Check platform information
    print(f"\nOperating System: {platform.system()} {platform.version()}")
    print(f"Machine: {platform.machine()}")
    
    # Check date and time
    current_time = datetime.datetime.now()
    print(f"\nCurrent date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Day of the week: {current_time.strftime('%A')}")
    
    # Simple calculation to verify Python is working
    calculation = 10 * 5 + 3
    print(f"\nTest calculation (10 * 5 + 3): {calculation}")
    
    # Print current working directory
    print(f"\nCurrent working directory: {os.getcwd()}")
    
    # Check for installed packages
    print("\nChecking for commonly used packages:")
    packages_to_check = ['numpy', 'pandas', 'matplotlib', 'requests', 'flask']
    
    for package in packages_to_check:
        try:
            dist = pkg_resources.get_distribution(package)
            print(f"✓ {package} ({dist.version}) is installed")
        except pkg_resources.DistributionNotFound:
            print(f"✗ {package} is not installed")
    
    # Print user information
    print(f"\nUsername: {os.getlogin() if hasattr(os, 'getlogin') else 'Unknown'}")
    
    print("\nCongratulations! If you can see this message, Python is installed correctly.")
    print("=" * 50)
    
if __name__ == "__main__":
    check_python_installation()
    
    # Bonus: List the first 10 available modules
    print("\nSample of available Python modules:")
    modules = sorted(sys.modules.keys())
    for module in modules[:10]:
        print(f"- {module}")
    print("... and many more!")