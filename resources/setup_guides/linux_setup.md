# Python Setup Guide for Linux

This guide will help you install Python and set up your development environment on Linux distributions.

## Prerequisites

- Any modern Linux distribution
- Terminal access
- Internet connection
- Basic familiarity with command line

## Distribution-Specific Installation

### Ubuntu/Debian

#### Update Package Lists
```bash
sudo apt update
```

#### Install Python 3 and pip
```bash
sudo apt install python3 python3-pip python3-venv
```

#### Install Development Tools (Optional but Recommended)
```bash
sudo apt install python3-dev build-essential
```

### CentOS/RHEL/Fedora

#### For CentOS/RHEL 8+
```bash
sudo dnf install python3 python3-pip python3-venv
```

#### For older CentOS/RHEL versions
```bash
sudo yum install python3 python3-pip
```

#### For Fedora
```bash
sudo dnf install python3 python3-pip python3-venv
```

### Arch Linux

```bash
sudo pacman -S python python-pip
```

### openSUSE

```bash
sudo zypper install python3 python3-pip python3-venv
```

## Alternative Installation Methods

### Method 1: From Source (Any Distribution)

#### Install Dependencies
```bash
# Ubuntu/Debian
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

# CentOS/RHEL/Fedora
sudo dnf groupinstall "Development Tools"
sudo dnf install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
```

#### Download and Compile Python
```bash
cd /tmp
wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
tar -xf Python-3.11.0.tgz
cd Python-3.11.0
./configure --enable-optimizations
make -j $(nproc)
sudo make altinstall
```

### Method 2: Using pyenv (Recommended for Multiple Versions)

#### Install pyenv
```bash
curl https://pyenv.run | bash
```

#### Add to Shell Profile
Add these lines to your `~/.bashrc` or `~/.zshrc`:
```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

#### Reload Shell and Install Python
```bash
source ~/.bashrc  # or ~/.zshrc
pyenv install 3.11.0
pyenv global 3.11.0
```

## Verify Installation

```bash
python3 --version
pip3 --version
```

You should see output similar to:
```
Python 3.x.x
pip 22.x.x from /usr/lib/python3/dist-packages/pip (python 3.x)
```

## Setting Up Development Environment

### Install a Code Editor

**Option 1: Visual Studio Code**
```bash
# Ubuntu/Debian
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code

# Fedora
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf install code

# Arch Linux
yay -S visual-studio-code-bin
```

**Option 2: PyCharm Community**
```bash
# Snap (works on most distributions)
sudo snap install pycharm-community --classic

# Or download from JetBrains website
```

**Option 3: Vim/Neovim (Lightweight)**
```bash
# Ubuntu/Debian
sudo apt install vim neovim

# Fedora
sudo dnf install vim neovim

# Arch
sudo pacman -S vim neovim
```

### Create Your First Python File

```bash
mkdir ~/python_projects
cd ~/python_projects
echo 'print("Hello, Python!")' > hello.py
python3 hello.py
```

## Package Management with pip

### Upgrade pip
```bash
python3 -m pip install --upgrade pip
```

### Install Packages
```bash
pip3 install package_name
```

### Install Packages User-wide (No sudo required)
```bash
pip3 install --user package_name
```

### Create Virtual Environments
```bash
python3 -m venv myproject
source myproject/bin/activate
```

## Shell Configuration

### Setting up Aliases
Add these to your `~/.bashrc` or `~/.zshrc`:
```bash
alias python=python3
alias pip=pip3
```

### Reload Shell Configuration
```bash
source ~/.bashrc  # or ~/.zshrc
```

## Troubleshooting

### Python3 Command Not Found

**Problem**: Getting "command not found: python3"

**Solutions**:
1. **Install Python**: Use your distribution's package manager
2. **Check if installed but not in PATH**:
```bash
find /usr -name python3 2>/dev/null
```
3. **Create symlink if needed**:
```bash
sudo ln -s /usr/bin/python3.x /usr/bin/python3
```

### Permission Errors with pip

**Problem**: Getting permission denied errors when installing packages

**Solutions**:
1. **Use --user flag** (recommended):
```bash
pip3 install --user package_name
```
2. **Use virtual environments** (best practice):
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install package_name
```
3. **Fix pip directory permissions**:
```bash
mkdir -p ~/.local/lib/python3.x/site-packages
```

### Missing Development Headers

**Problem**: Errors when installing packages that need compilation

**Solutions**:
```bash
# Ubuntu/Debian
sudo apt install python3-dev python3-setuptools

# CentOS/RHEL/Fedora
sudo dnf install python3-devel python3-setuptools

# Arch Linux
sudo pacman -S python python-setuptools
```

### SSL Certificate Issues

**Problem**: SSL errors when using pip

**Solutions**:
1. **Update certificates**:
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ca-certificates

# CentOS/RHEL/Fedora
sudo dnf update ca-certificates
```
2. **Use trusted hosts**:
```bash
pip3 install --trusted-host pypi.org --trusted-host pypi.python.org package_name
```

### Virtual Environment Issues

**Problem**: Virtual environment not working properly

**Solutions**:
1. **Install venv module**:
```bash
# Ubuntu/Debian
sudo apt install python3-venv

# CentOS/RHEL/Fedora
sudo dnf install python3-venv
```
2. **Check activation**:
```bash
source venv/bin/activate
which python  # Should point to venv/bin/python
```

### Multiple Python Versions

**Problem**: Managing multiple Python versions

**Solutions**:
1. **Use update-alternatives** (Ubuntu/Debian):
```bash
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 2
sudo update-alternatives --config python
```
2. **Use pyenv** (recommended for development)
3. **Use specific version commands**: `python3.8`, `python3.9`, etc.

### Package Installation Fails

**Problem**: Packages fail to install due to missing dependencies

**Solutions**:
1. **Install build tools**:
```bash
# Ubuntu/Debian
sudo apt install build-essential

# CentOS/RHEL/Fedora
sudo dnf groupinstall "Development Tools"

# Arch Linux
sudo pacman -S base-devel
```
2. **Install specific libraries as needed**:
```bash
# For packages requiring specific libraries
sudo apt install libffi-dev libssl-dev  # Ubuntu/Debian
sudo dnf install libffi-devel openssl-devel  # Fedora
```

## Common Commands Reference

```bash
# Check Python version
python3 --version

# Check pip version
pip3 --version

# Install a package
pip3 install package_name

# Install package for current user only
pip3 install --user package_name

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

# Check Python executable path
python3 -c "import sys; print(sys.executable)"

# Check installed packages location
python3 -c "import site; print(site.getsitepackages())"
```

## Linux-Specific Tips

### File Permissions
```bash
# Make Python file executable
chmod +x script.py

# Add shebang to Python file
echo '#!/usr/bin/env python3' | cat - script.py > temp && mv temp script.py
```

### System Service Integration
```bash
# Create systemd service for Python script
sudo nano /etc/systemd/system/myapp.service

# Example service file content:
[Unit]
Description=My Python App
After=network.target

[Service]
Type=simple
User=myuser
WorkingDirectory=/path/to/app
ExecStart=/usr/bin/python3 /path/to/app/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### Environment Variables
```bash
# Set Python path
export PYTHONPATH="${PYTHONPATH}:/path/to/your/modules"

# Set pip configuration
export PIP_USER=true
```

## Next Steps

1. Complete the verification steps above
2. Set up your preferred development environment
3. Create and run your first Python program
4. Set up virtual environments for your projects
5. Start with the Basic Level modules in the Python Learning Path

## Additional Resources

- [Official Python Documentation](https://docs.python.org/)
- [Python Developer's Guide](https://devguide.python.org/)
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [pyenv Documentation](https://github.com/pyenv/pyenv)
- [Linux Python Development Setup](https://realpython.com/python-development-on-linux/)