"""
Exercise: Verify Python Installation and Setup

Instructions:
1. Run this script to verify that your Python installation is working correctly
2. The script will check your Python version and print some basic information
3. If the script runs without errors, your Python installation is working!
4. Try modifying the script to print additional information

Learning objectives:
- Verify Python installation
- Run a Python script
- Understand basic Python syntax
"""

import sys
import platform
import datetime

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
    
    # Simple calculation to verify Python is working
    calculation = 10 * 5 + 3
    print(f"\nTest calculation (10 * 5 + 3): {calculation}")
    
    print("\nCongratulations! If you can see this message, Python is installed correctly.")
    print("=" * 50)
    
    # TODO: Add your own code below to print additional information
    # For example, try printing your name and the current day of the week
    
    
if __name__ == "__main__":
    check_python_installation()
    
    # Challenge: Try to modify this script to:
    # 1. Print the current working directory
    # 2. List all modules available in your Python installation
    # 3. Check if certain packages are installed