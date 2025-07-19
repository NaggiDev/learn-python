"""File system utilities."""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from ..exceptions import SystemError

def backup_file(filepath: str, backup_dir: Optional[str] = None) -> str:
    """
    Create a backup copy of a file.
    
    Args:
        filepath (str): Path to file to backup
        backup_dir (str, optional): Directory for backup (default: same directory)
        
    Returns:
        str: Path to backup file
        
    Example:
        >>> backup_path = backup_file("important.txt")
        >>> backup_path.endswith("_backup_")
        True
    """
    if not os.path.exists(filepath):
        raise SystemError(f"File not found: {filepath}")
    
    path = Path(filepath)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if backup_dir:
        backup_path = Path(backup_dir) / f"{path.stem}_backup_{timestamp}{path.suffix}"
        Path(backup_dir).mkdir(parents=True, exist_ok=True)
    else:
        backup_path = path.parent / f"{path.stem}_backup_{timestamp}{path.suffix}"
    
    try:
        shutil.copy2(filepath, backup_path)
        return str(backup_path)
    except (OSError, IOError) as e:
        raise SystemError(f"Backup failed: {e}")

def copy_file(source: str, destination: str, overwrite: bool = False) -> bool:
    """
    Copy file from source to destination.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
        overwrite (bool): Whether to overwrite existing file
        
    Returns:
        bool: True if successful
        
    Example:
        >>> copy_file("source.txt", "dest.txt")
        True
    """
    if not os.path.exists(source):
        raise SystemError(f"Source file not found: {source}")
    
    if os.path.exists(destination) and not overwrite:
        raise SystemError(f"Destination exists and overwrite=False: {destination}")
    
    try:
        # Create destination directory if needed
        Path(destination).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        return True
    except (OSError, IOError) as e:
        raise SystemError(f"Copy failed: {e}")

def get_file_info(filepath: str) -> Dict[str, Any]:
    """
    Get detailed information about a file.
    
    Args:
        filepath (str): Path to file
        
    Returns:
        Dict[str, Any]: File information
        
    Example:
        >>> info = get_file_info("test.txt")
        >>> 'size' in info
        True
    """
    if not os.path.exists(filepath):
        raise SystemError(f"File not found: {filepath}")
    
    try:
        stat = os.stat(filepath)
        path = Path(filepath)
        
        return {
            'name': path.name,
            'path': str(path.absolute()),
            'size': stat.st_size,
            'size_human': _format_bytes(stat.st_size),
            'created': datetime.fromtimestamp(stat.st_ctime),
            'modified': datetime.fromtimestamp(stat.st_mtime),
            'accessed': datetime.fromtimestamp(stat.st_atime),
            'is_file': path.is_file(),
            'is_directory': path.is_dir(),
            'extension': path.suffix,
            'permissions': oct(stat.st_mode)[-3:]
        }
    except (OSError, IOError) as e:
        raise SystemError(f"Cannot get file info: {e}")

def list_directory(directory: str, pattern: Optional[str] = None, 
                  recursive: bool = False) -> List[Dict[str, Any]]:
    """
    List directory contents with detailed information.
    
    Args:
        directory (str): Directory path
        pattern (str, optional): File pattern to match
        recursive (bool): Whether to search recursively
        
    Returns:
        List[Dict[str, Any]]: List of file information
        
    Example:
        >>> files = list_directory(".")
        >>> isinstance(files, list)
        True
    """
    if not os.path.exists(directory):
        raise SystemError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise SystemError(f"Not a directory: {directory}")
    
    try:
        path = Path(directory)
        files = []
        
        if recursive:
            if pattern:
                items = path.rglob(pattern)
            else:
                items = path.rglob("*")
        else:
            if pattern:
                items = path.glob(pattern)
            else:
                items = path.iterdir()
        
        for item in items:
            try:
                stat = item.stat()
                files.append({
                    'name': item.name,
                    'path': str(item.absolute()),
                    'size': stat.st_size if item.is_file() else 0,
                    'size_human': _format_bytes(stat.st_size) if item.is_file() else "0 B",
                    'modified': datetime.fromtimestamp(stat.st_mtime),
                    'is_file': item.is_file(),
                    'is_directory': item.is_dir(),
                    'extension': item.suffix if item.is_file() else ""
                })
            except (OSError, IOError):
                # Skip files we can't access
                continue
        
        return sorted(files, key=lambda x: (not x['is_directory'], x['name'].lower()))
    
    except (OSError, IOError) as e:
        raise SystemError(f"Cannot list directory: {e}")

def create_directory(directory: str, parents: bool = True) -> bool:
    """
    Create directory.
    
    Args:
        directory (str): Directory path to create
        parents (bool): Create parent directories if needed
        
    Returns:
        bool: True if successful
        
    Example:
        >>> create_directory("new/nested/directory")
        True
    """
    try:
        Path(directory).mkdir(parents=parents, exist_ok=True)
        return True
    except (OSError, IOError) as e:
        raise SystemError(f"Cannot create directory: {e}")

def delete_file(filepath: str, force: bool = False) -> bool:
    """
    Delete file or directory.
    
    Args:
        filepath (str): Path to delete
        force (bool): Force deletion of directories
        
    Returns:
        bool: True if successful
        
    Example:
        >>> delete_file("temp.txt")
        True
    """
    if not os.path.exists(filepath):
        return True  # Already deleted
    
    try:
        path = Path(filepath)
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            if force:
                shutil.rmtree(filepath)
            else:
                path.rmdir()  # Only works if empty
        return True
    except (OSError, IOError) as e:
        raise SystemError(f"Cannot delete: {e}")

def _format_bytes(bytes_size: int) -> str:
    """Format bytes in human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} PB"