# Python Setup Guide for macOS

This guide will help you install Python and set up your development environment on macOS.

## Prerequisites

- macOS 10.9 or later
- Administrator access to install software
- Stable internet connection
- Xcode Command Line Tools (will be installed automatically if needed)

## Method 1: Official Python Installer (Recommended)

### Step 1: Download Python

1. Visit the official Python website: https://www.python.org/downloads/
2. Click "Download Python 3.x.x" (latest version)
3. The website should automatically detect macOS and offer the correct installer

### Step 2: Install Python

1. Locate the downloaded `.pkg` file (usually in Downloads folder)
2. Double-click to open the installer
3. Follow the installation wizard:
   - Click "Continue" through the introduction screens
   - Accept the license agreement
   - Choose installation location (default is recommended)
   - Click "Install" and enter your password when prompted
4. Click "Close" when installation is complete

### Step 3: Verify Installation

1. Open Terminal (Cmd + Space, type "Terminal", press Enter)
2. Type `python3 --version` and press Enter
3. You should see something like "Python 3.x.x"
4. Type `pip3 --version` to verify pip is installed

## Method 2: Homebrew (Popular Alternative)

### Install Homebrew First
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install Python via Homebrew
```bash
brew install python
```

### Verify Installation
```bash
python3 --version
pip3 --version
```

## Method 3: pyenv (For Multiple Python Versions)

### Install pyenv
```bash
brew install pyenv
```

### Add to Shell Profile
Add these lines to your `~/.zshrc` or `~/.bash_profile`:
```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
```

### Install Python
```bash
pyenv install 3.11.0
pyenv global 3.11.0
```

## Setting Up Development Environment

### Install a Code Editor

**Option 1: Visual Studio Code (Recommended)**
1. Download from https://code.visualstudio.com/
2. Drag to Applications folder
3. Install Python extension from Extensions marketplace

**Option 2: PyCharm Community**
1. Download from https://www.jetbrains.com/pycharm/
2. Choose Community Edition (free)
3. Drag to Applications folder

### Create Your First Python File

1. Create a new folder for your Python projects:
```bash
mkdir ~/python_projects
cd ~/python_projects
```
2. Create a new file:
```bash
touch hello.py
```
3. Edit with your preferred editor and add:
```python
print("Hello, Python!")
```
4. Run the file:
```bash
python3 hello.py
```

## Package Management with pip

### Upgrading pip
```bash
python3 -m pip install --upgrade pip
```

### Installing Packages
```bash
pip3 install package_name
```

### Creating Virtual Environments
```bash
python3 -m venv myproject
source myproject/bin/activate
```

## Shell Configuration

### Setting up Aliases (Optional but Recommended)

Add these to your `~/.zshrc` or `~/.bash_profile`:
```bash
alias python=python3
alias pip=pip3
```

Then reload your shell:
```bash
source ~/.zshrc  # or source ~/.bash_profile
```

## Troubleshooting

### Command Not Found: python3

**Problem**: Getting "command not found: python3"

**Solutions**:
1. **Check if Python is installed**: Look in `/usr/bin/python3` or `/usr/local/bin/python3`
2. **Reinstall Python**: Download from python.org and reinstall
3. **Check PATH**: Add Python to PATH in your shell profile:
```bash
export PATH="/usr/local/bin:$PATH"
```

### Permission Errors

**Problem**: Getting permission denied errors when installing packages

**Solutions**:
1. Use `--user` flag: `pip3 install --user package_name`
2. Use virtual environments (recommended)
3. Fix pip permissions:
```bash
python3 -m pip install --user --upgrade pip
```

### SSL Certificate Errors

**Problem**: SSL errors when using pip

**Solutions**:
1. Update certificates:
```bash
/Applications/Python\ 3.x/Install\ Certificates.command
```
2. Upgrade pip:
```bash
python3 -m pip install --upgrade pip
```
3. Use trusted hosts:
```bash
pip3 install --trusted-host pypi.org --trusted-host pypi.python.org package_name
```

### Xcode Command Line Tools Issues

**Problem**: Errors related to missing development tools

**Solutions**:
1. Install Xcode Command Line Tools:
```bash
xcode-select --install
```
2. Accept Xcode license:
```bash
sudo xcodebuild -license accept
```

### Multiple Python Versions Conflicts

**Problem**: Having multiple Python versions causing conflicts

**Solutions**:
1. Use specific version commands: `python3.9`, `python3.10`, etc.
2. Use pyenv to manage versions
3. Check which Python you're using:
```bash
which python3
python3 --version
```

### Virtual Environment Not Activating

**Problem**: Virtual environment activation issues

**Solutions**:
1. Make sure you're in the correct directory
2. Use full path to activate script:
```bash
source /full/path/to/venv/bin/activate
```
3. Check if virtual environment was created properly:
```bash
ls -la venv/bin/
```

### Homebrew Python vs System Python

**Problem**: Conflicts between different Python installations

**Solutions**:
1. Use Homebrew Python consistently:
```bash
brew link python
```
2. Check your PATH order in shell profile
3. Use `which python3` to see which Python is being used

## Common Commands Reference

```bash
# Check Python version
python3 --version

# Check pip version
pip3 --version

# Install a package
pip3 install package_name

# List installed packages
pip3 list

# Create virtual environment
python3 -m venv project_name

# Activate virtual environment
source project_name/bin/activate

# Deactivate virtual environment
deactivate

# Run Python file
python3 filename.py

# Start Python interactive shell
python3

# Check which Python is being used
which python3

# View Python path
python3 -c "import sys; print(sys.path)"
```

## macOS-Specific Tips

### Using Terminal Effectively
- Use Tab completion for file/directory names
- Use `Cmd + T` to open new terminal tabs
- Use `Cmd + K` to clear terminal screen

### File System Navigation
```bash
# Home directory
cd ~

# List files (including hidden)
ls -la

# Create directory
mkdir directory_name

# Remove file
rm filename

# Remove directory
rm -rf directory_name
```

## Next Steps

1. Complete the verification steps above
2. Set up your preferred code editor
3. Create your first Python program
4. Set up a virtual environment for your projects
5. Start with the Basic Level modules in the Python Learning Path

## Additional Resources

- [Official Python Documentation](https://docs.python.org/)
- [Python on macOS Guide](https://docs.python.org/3/using/mac.html)
- [Homebrew Documentation](https://docs.brew.sh/)
- [pyenv Documentation](https://github.com/pyenv/pyenv)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)