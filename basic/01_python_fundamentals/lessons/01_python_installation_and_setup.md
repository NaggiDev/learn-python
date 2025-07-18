# Python Installation and Setup

Welcome to the first lesson in your Python journey! Before you can start writing Python code, you need to set up your development environment. This lesson will guide you through installing Python on your operating system, configuring a code editor, and running your first Python program.

## Table of Contents
1. [Installing Python](#installing-python)
   - [Windows Installation](#windows-installation)
   - [macOS Installation](#macos-installation)
   - [Linux Installation](#linux-installation)
2. [Setting Up a Code Editor](#setting-up-a-code-editor)
   - [Visual Studio Code](#visual-studio-code)
   - [PyCharm](#pycharm)
   - [Other Options](#other-options)
3. [Running Your First Python Program](#running-your-first-python-program)
   - [Using the Python Interactive Shell](#using-the-python-interactive-shell)
   - [Running Python Scripts](#running-python-scripts)
4. [Setting Up Virtual Environments](#setting-up-virtual-environments)
   - [Why Use Virtual Environments](#why-use-virtual-environments)
   - [Creating and Activating Virtual Environments](#creating-and-activating-virtual-environments)
5. [Troubleshooting Common Issues](#troubleshooting-common-issues)

## Installing Python

Python is available for all major operating systems. We recommend installing Python 3.8 or newer, as Python 2 is no longer supported.

### Windows Installation

1. **Download the installer**:
   - Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Click on the "Download Python" button (it will show the latest version)
   - Scroll down to find older versions if needed

2. **Run the installer**:
   - **Important**: Check the box that says "Add Python to PATH" before clicking "Install Now"
   - This option ensures you can run Python from the command prompt

   ![Windows Python Installer](https://docs.python.org/3/_images/win_installer.png)

3. **Verify the installation**:
   - Open Command Prompt (search for "cmd" in the Start menu)
   - Type `python --version` and press Enter
   - You should see the Python version number displayed

4. **Alternative: Install from Microsoft Store**:
   - Search for "Python" in the Microsoft Store
   - Select the version you want to install
   - Click "Get" or "Install"
   - This method automatically adds Python to PATH

### macOS Installation

macOS comes with Python pre-installed, but it's usually an older version. Here's how to install the latest version:

1. **Using Homebrew (recommended)**:
   - Install Homebrew if you don't have it already:
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Install Python using Homebrew:
     ```
     brew install python
     ```

2. **Using the official installer**:
   - Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download the macOS installer
   - Open the downloaded .pkg file and follow the installation instructions

3. **Verify the installation**:
   - Open Terminal
   - Type `python3 --version` and press Enter
   - You should see the Python version number displayed

### Linux Installation

Most Linux distributions come with Python pre-installed. Here's how to install or update Python on common distributions:

1. **Ubuntu/Debian**:
   ```
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Fedora**:
   ```
   sudo dnf install python3 python3-pip
   ```

3. **Arch Linux**:
   ```
   sudo pacman -S python python-pip
   ```

4. **Verify the installation**:
   - Open Terminal
   - Type `python3 --version` and press Enter
   - You should see the Python version number displayed

## Setting Up a Code Editor

While you can write Python code in any text editor, using a dedicated code editor or Integrated Development Environment (IDE) will make your coding experience much more productive.

### Visual Studio Code

Visual Studio Code (VS Code) is a free, lightweight, and powerful code editor that works well with Python.

1. **Installation**:
   - Download VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/)
   - Follow the installation instructions for your operating system

2. **Python Extension**:
   - Open VS Code
   - Go to the Extensions view by clicking on the square icon on the sidebar or pressing `Ctrl+Shift+X`
   - Search for "Python"
   - Install the Python extension by Microsoft

3. **Configuration**:
   - Open a Python file (create one with a `.py` extension if needed)
   - VS Code should automatically detect your Python installation
   - You can select a specific Python interpreter by clicking on the Python version in the bottom status bar

### PyCharm

PyCharm is a full-featured Python IDE that offers more advanced features.

1. **Installation**:
   - Download PyCharm Community Edition (free) from [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
   - Follow the installation instructions for your operating system

2. **Configuration**:
   - Open PyCharm
   - Create a new project or open an existing one
   - PyCharm should automatically detect your Python installation
   - If not, go to File > Settings > Project > Python Interpreter to configure it

### Other Options

- **Jupyter Notebook**: Great for data science and interactive coding
- **Atom**: Lightweight editor with Python plugins
- **Sublime Text**: Fast and minimalist editor
- **IDLE**: Comes bundled with Python, good for beginners

## Running Your First Python Program

Now that you have Python installed and a code editor set up, let's run your first Python program.

### Using the Python Interactive Shell

The Python interactive shell (also called the REPL - Read-Eval-Print Loop) allows you to execute Python code line by line.

1. **Open the shell**:
   - Windows: Open Command Prompt and type `python`
   - macOS/Linux: Open Terminal and type `python3`

2. **Try some simple commands**:
   ```python
   print("Hello, World!")
   2 + 3
   name = "Python Learner"
   print(f"Welcome, {name}!")
   ```

3. **Exit the shell**:
   - Type `exit()` or press `Ctrl+Z` (Windows) or `Ctrl+D` (macOS/Linux)

### Running Python Scripts

1. **Create a Python file**:
   - Open your code editor
   - Create a new file named `hello.py`
   - Add the following code:
     ```python
     # My first Python program
     print("Hello, World!")
     print("Welcome to Python!")
     
     # Let's do some simple math
     result = 5 * 7
     print(f"5 * 7 = {result}")
     ```
   - Save the file

2. **Run the script**:
   - **From the command line**:
     - Navigate to the directory containing your file
     - Run `python hello.py` (Windows) or `python3 hello.py` (macOS/Linux)
   
   - **From VS Code**:
     - Open the file in VS Code
     - Click the "Run" button (triangle) in the top-right corner or press `F5`
   
   - **From PyCharm**:
     - Open the file in PyCharm
     - Right-click in the editor and select "Run 'hello'" or press `Shift+F10`

3. **Observe the output**:
   ```
   Hello, World!
   Welcome to Python!
   5 * 7 = 35
   ```

## Setting Up Virtual Environments

### Why Use Virtual Environments

Virtual environments are isolated Python environments that allow you to install packages for specific projects without affecting your system-wide Python installation. This is considered a best practice for Python development.

Benefits include:
- Avoiding package version conflicts between projects
- Easily sharing project dependencies with others
- Keeping your system Python installation clean
- Testing applications with different package versions

### Creating and Activating Virtual Environments

Python comes with the `venv` module for creating virtual environments.

1. **Create a virtual environment**:
   - **Windows**:
     ```
     python -m venv myenv
     ```
   - **macOS/Linux**:
     ```
     python3 -m venv myenv
     ```
   This creates a directory called `myenv` containing the virtual environment.

2. **Activate the virtual environment**:
   - **Windows**:
     ```
     myenv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```
     source myenv/bin/activate
     ```
   When activated, you'll see the environment name in your command prompt.

3. **Install packages in the virtual environment**:
   ```
   pip install package_name
   ```

4. **Deactivate the virtual environment**:
   ```
   deactivate
   ```

5. **Create a requirements.txt file** to share your environment:
   ```
   pip freeze > requirements.txt
   ```

6. **Install from a requirements.txt file**:
   ```
   pip install -r requirements.txt
   ```

## Troubleshooting Common Issues

### Python Not Found in PATH

**Symptoms**:
- `'python' is not recognized as an internal or external command`
- `command not found: python`

**Solutions**:
1. **Windows**:
   - Reinstall Python and make sure to check "Add Python to PATH"
   - Or manually add Python to PATH:
     - Find your Python installation path (e.g., `C:\Python39`)
     - Open System Properties > Advanced > Environment Variables
     - Edit the PATH variable and add the Python path

2. **macOS/Linux**:
   - Use `python3` instead of `python`
   - Or create an alias in your shell profile:
     ```
     echo "alias python=python3" >> ~/.bashrc
     source ~/.bashrc
     ```

### Permission Errors

**Symptoms**:
- `Permission denied` when installing packages
- `Access is denied` when running Python

**Solutions**:
1. **Windows**:
   - Run Command Prompt as Administrator
   - Use `--user` flag with pip: `pip install --user package_name`

2. **macOS/Linux**:
   - Use `sudo` (not recommended for pip): `sudo pip install package_name`
   - Better: Use virtual environments or `pip install --user package_name`
   - Fix permissions: `chmod +x your_script.py`

### SSL Certificate Errors

**Symptoms**:
- `SSL: CERTIFICATE_VERIFY_FAILED` when downloading packages

**Solutions**:
1. Update your Python installation
2. Install certificates:
   - **macOS**: Run `/Applications/Python 3.x/Install Certificates.command`
3. Temporarily bypass (not recommended for production):
   ```
   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package_name
   ```

### Import Errors

**Symptoms**:
- `ModuleNotFoundError: No module named 'package_name'`

**Solutions**:
1. Install the missing package: `pip install package_name`
2. Check if you're using the correct virtual environment
3. Verify the package name (case-sensitive)
4. Check if the package is installed in the correct Python version

### Python Version Conflicts

**Symptoms**:
- Code works in one environment but not another
- `SyntaxError` for features not available in your Python version

**Solutions**:
1. Use virtual environments to manage different Python versions
2. Check your Python version: `python --version`
3. Use version-specific features conditionally:
   ```python
   import sys
   if sys.version_info >= (3, 6):
       # Use f-strings
       message = f"Hello, {name}"
   else:
       # Use older string formatting
       message = "Hello, {}".format(name)
   ```

## Next Steps

Congratulations! You've set up your Python development environment and run your first Python program. In the next lesson, we'll dive into Python variables and data types.

Before moving on, make sure you:
- Can run Python from the command line
- Have set up a code editor
- Can create and run a simple Python script
- Understand how to create and use virtual environments

## Additional Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Python Virtual Environments Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [PyCharm Getting Started Guide](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)