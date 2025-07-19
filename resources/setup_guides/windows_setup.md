# Python Setup Guide for Windows

This guide will help you install Python and set up your development environment on Windows.

## Prerequisites

- Windows 10 or later (Windows 7/8 may work but are not recommended)
- Administrator access to install software
- Stable internet connection

## Method 1: Official Python Installer (Recommended)

### Step 1: Download Python

1. Visit the official Python website: https://www.python.org/downloads/
2. Click "Download Python 3.x.x" (latest version)
3. The website should automatically detect Windows and offer the correct installer

### Step 2: Run the Installer

1. Locate the downloaded file (usually in Downloads folder)
2. Right-click and "Run as administrator"
3. **IMPORTANT**: Check "Add Python to PATH" before clicking Install
4. Choose "Install Now" for default installation
5. Wait for installation to complete
6. Click "Close" when finished

### Step 3: Verify Installation

1. Open Command Prompt (Win + R, type `cmd`, press Enter)
2. Type `python --version` and press Enter
3. You should see something like "Python 3.x.x"
4. Type `pip --version` to verify pip is installed

## Method 2: Microsoft Store (Alternative)

1. Open Microsoft Store
2. Search for "Python 3.x"
3. Click "Get" or "Install"
4. Launch from Start Menu after installation

## Setting Up Development Environment

### Install a Code Editor

**Option 1: Visual Studio Code (Recommended)**
1. Download from https://code.visualstudio.com/
2. Install with default settings
3. Install Python extension from Extensions marketplace

**Option 2: PyCharm Community**
1. Download from https://www.jetbrains.com/pycharm/
2. Choose Community Edition (free)
3. Install with default settings

### Create Your First Python File

1. Create a new folder for your Python projects
2. Open your code editor
3. Create a new file called `hello.py`
4. Add this code:
```python
print("Hello, Python!")
```
5. Save the file
6. Open Command Prompt in the folder
7. Run: `python hello.py`

## Package Management with pip

### Upgrading pip
```cmd
python -m pip install --upgrade pip
```

### Installing Packages
```cmd
pip install package_name
```

### Creating Virtual Environments
```cmd
python -m venv myproject
myproject\Scripts\activate
```

## Troubleshooting

### Python is not recognized as a command

**Problem**: Getting "'python' is not recognized as an internal or external command"

**Solutions**:
1. **Reinstall Python**: Uninstall Python, download installer again, and make sure to check "Add Python to PATH"
2. **Manual PATH setup**:
   - Open System Properties (Win + Pause)
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under System Variables, find "Path" and click "Edit"
   - Click "New" and add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x`
   - Click "New" and add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\Scripts`
   - Click OK and restart Command Prompt

### Permission Errors

**Problem**: Getting permission denied errors when installing packages

**Solutions**:
1. Run Command Prompt as Administrator
2. Use `--user` flag: `pip install --user package_name`
3. Use virtual environments (recommended)

### Multiple Python Versions

**Problem**: Having multiple Python versions causing conflicts

**Solutions**:
1. Use `py -3` instead of `python` to specifically use Python 3
2. Use `py -3.x` to use a specific version (e.g., `py -3.9`)
3. Uninstall older versions if not needed

### SSL Certificate Errors

**Problem**: SSL errors when using pip

**Solutions**:
1. Upgrade pip: `python -m pip install --upgrade pip`
2. Use trusted hosts: `pip install --trusted-host pypi.org --trusted-host pypi.python.org package_name`
3. Check your antivirus/firewall settings

### Virtual Environment Issues

**Problem**: Virtual environment not activating

**Solutions**:
1. Make sure you're in the correct directory
2. Use full path: `C:\path\to\venv\Scripts\activate`
3. Try using PowerShell instead of Command Prompt
4. Check execution policy in PowerShell: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Common Commands Reference

```cmd
# Check Python version
python --version

# Check pip version
pip --version

# Install a package
pip install package_name

# List installed packages
pip list

# Create virtual environment
python -m venv project_name

# Activate virtual environment
project_name\Scripts\activate

# Deactivate virtual environment
deactivate

# Run Python file
python filename.py

# Start Python interactive shell
python
```

## Next Steps

1. Complete the verification steps above
2. Try creating and running your first Python program
3. Set up a virtual environment for your projects
4. Install a code editor if you haven't already
5. Start with the Basic Level modules in the Python Learning Path

## Additional Resources

- [Official Python Documentation](https://docs.python.org/)
- [Python on Windows FAQ](https://docs.python.org/3/faq/windows.html)
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)