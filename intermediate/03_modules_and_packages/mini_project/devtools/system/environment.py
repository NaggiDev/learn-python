"""Environment variable utilities."""

import os
from typing import Dict, Optional, Any
from ..exceptions import SystemError

def get_env_var(name: str, default: Optional[str] = None) -> Optional[str]:
    """
    Get environment variable value.
    
    Args:
        name (str): Environment variable name
        default (str, optional): Default value if not found
        
    Returns:
        Optional[str]: Environment variable value or default
        
    Example:
        >>> path = get_env_var("PATH")
        >>> isinstance(path, str)
        True
    """
    return os.environ.get(name, default)

def set_env_var(name: str, value: str) -> bool:
    """
    Set environment variable.
    
    Args:
        name (str): Environment variable name
        value (str): Environment variable value
        
    Returns:
        bool: True if successful
        
    Note:
        This only affects the current process and its children.
        
    Example:
        >>> set_env_var("MY_VAR", "test_value")
        True
        >>> get_env_var("MY_VAR")
        'test_value'
    """
    try:
        os.environ[name] = str(value)
        return True
    except Exception as e:
        raise SystemError(f"Cannot set environment variable: {e}")

def get_all_env_vars() -> Dict[str, str]:
    """
    Get all environment variables.
    
    Returns:
        Dict[str, str]: Dictionary of all environment variables
        
    Example:
        >>> env_vars = get_all_env_vars()
        >>> "PATH" in env_vars
        True
    """
    return dict(os.environ)

def unset_env_var(name: str) -> bool:
    """
    Remove environment variable.
    
    Args:
        name (str): Environment variable name
        
    Returns:
        bool: True if successful
        
    Example:
        >>> set_env_var("TEMP_VAR", "value")
        True
        >>> unset_env_var("TEMP_VAR")
        True
        >>> get_env_var("TEMP_VAR") is None
        True
    """
    try:
        if name in os.environ:
            del os.environ[name]
        return True
    except Exception as e:
        raise SystemError(f"Cannot unset environment variable: {e}")

def get_path_dirs() -> list:
    """
    Get directories in PATH environment variable.
    
    Returns:
        list: List of directories in PATH
        
    Example:
        >>> dirs = get_path_dirs()
        >>> isinstance(dirs, list)
        True
    """
    path = get_env_var("PATH", "")
    if not path:
        return []
    
    # Handle different path separators
    separator = ";" if os.name == "nt" else ":"
    return [d.strip() for d in path.split(separator) if d.strip()]

def add_to_path(directory: str) -> bool:
    """
    Add directory to PATH environment variable.
    
    Args:
        directory (str): Directory to add to PATH
        
    Returns:
        bool: True if successful
        
    Note:
        This only affects the current process and its children.
        
    Example:
        >>> add_to_path("/usr/local/bin")
        True
    """
    if not os.path.exists(directory):
        raise SystemError(f"Directory does not exist: {directory}")
    
    current_path = get_env_var("PATH", "")
    separator = ";" if os.name == "nt" else ":"
    
    # Check if already in PATH
    path_dirs = get_path_dirs()
    if directory in path_dirs:
        return True
    
    # Add to beginning of PATH
    new_path = f"{directory}{separator}{current_path}"
    return set_env_var("PATH", new_path)

def get_home_directory() -> str:
    """
    Get user's home directory.
    
    Returns:
        str: Path to home directory
        
    Example:
        >>> home = get_home_directory()
        >>> os.path.exists(home)
        True
    """
    return os.path.expanduser("~")

def get_temp_directory() -> str:
    """
    Get system temporary directory.
    
    Returns:
        str: Path to temporary directory
        
    Example:
        >>> temp = get_temp_directory()
        >>> os.path.exists(temp)
        True
    """
    import tempfile
    return tempfile.gettempdir()

def expand_path(path: str) -> str:
    """
    Expand path with environment variables and user directory.
    
    Args:
        path (str): Path to expand
        
    Returns:
        str: Expanded path
        
    Example:
        >>> expanded = expand_path("~/Documents")
        >>> "Documents" in expanded
        True
    """
    # Expand user directory (~)
    expanded = os.path.expanduser(path)
    # Expand environment variables
    expanded = os.path.expandvars(expanded)
    # Convert to absolute path
    return os.path.abspath(expanded)