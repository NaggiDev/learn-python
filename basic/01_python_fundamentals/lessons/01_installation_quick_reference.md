# Python Installation Quick Reference

This quick reference guide provides the essential commands and steps for installing Python on different operating systems.

## Windows

### Official Installer Method
1. Download from [python.org/downloads](https://www.python.org/downloads/)
2. Run installer
3. ✅ **CHECK** "Add Python to PATH"
4. Click "Install Now"
5. Verify: Open Command Prompt and run `python --version`

### Microsoft Store Method
1. Open Microsoft Store
2. Search for "Python"
3. Select version (e.g., Python 3.10)
4. Click "Get" or "Install"
5. Verify: Open Command Prompt and run `python --version`

### Windows Package Manager (winget)
```
winget install Python.Python.3
```

## macOS

### Homebrew Method (Recommended)
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Verify installation
python3 --version
```

### Official Installer Method
1. Download from [python.org/downloads](https://www.python.org/downloads/)
2. Open the .pkg file
3. Follow installation instructions
4. Verify: Open Terminal and run `python3 --version`

## Linux

### Ubuntu/Debian
```bash
# Update package lists
sudo apt update

# Install Python
sudo apt install python3 python3-pip

# Verify installation
python3 --version
```

### Fedora
```bash
# Install Python
sudo dnf install python3 python3-pip

# Verify installation
python3 --version
```

### Arch Linux
```bash
# Install Python
sudo pacman -S python python-pip

# Verify installation
python --version
```

### CentOS/RHEL
```bash
# Install Python
sudo yum install python3 python3-pip

# Verify installation
python3 --version
```

## Virtual Environment Setup

### Creating a Virtual Environment
```bash
# Windows
python -m venv myenv

# macOS/Linux
python3 -m venv myenv
```

### Activating a Virtual Environment

#### Windows
```
# Command Prompt
myenv\Scripts\activate

# PowerShell
myenv\Scripts\Activate.ps1
```

#### macOS/Linux
```bash
source myenv/bin/activate
```

### Installing Packages in Virtual Environment
```bash
# After activating the environment
pip install package_name
```

### Deactivating a Virtual Environment
```
deactivate
```

## Checking Python Configuration

### Python Version
```bash
python --version  # Windows
python3 --version  # macOS/Linux
```

### Pip Version
```bash
pip --version  # Windows
pip3 --version  # macOS/Linux
```

### Installed Packages
```bash
pip list
```

### Python Path
```bash
# Windows
where python

# macOS/Linux
which python3
```

### Python Installation Details
```bash
# Windows
python -m site

# macOS/Linux
python3 -m site
```

## Common Flags and Options

### Python Command Options
```bash
python -c "print('Hello, World!')"  # Run a command
python -m module_name               # Run a module
python -i script.py                 # Run script and enter interactive mode
python -V                           # Print version
```

### Pip Command Options
```bash
pip install -r requirements.txt     # Install from requirements file
pip install --user package_name     # Install to user directory
pip install --upgrade package_name  # Upgrade a package
pip uninstall package_name          # Uninstall a package
pip freeze > requirements.txt       # Save installed packages list
```

## Next Steps After Installation

1. Verify Python is working:
   ```bash
   # Windows
   python -c "print('Hello, Python!')"
   
   # macOS/Linux
   python3 -c "print('Hello, Python!')"
   ```

2. Set up a code editor (VS Code, PyCharm, etc.)

3. Learn basic Python commands in the interactive shell:
   ```bash
   # Windows
   python
   
   # macOS/Linux
   python3
   ```

4. Create and run your first Python script:
   ```python
   # hello.py
   print("Hello, World!")
   ```

5. Install essential packages:
   ```bash
   pip install pytest requests
   ```