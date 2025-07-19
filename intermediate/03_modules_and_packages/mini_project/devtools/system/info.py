"""System information utilities."""

import os
import sys
import platform
import shutil
from typing import Dict, Any
from ..exceptions import SystemError

def get_system_info() -> Dict[str, Any]:
    """
    Get comprehensive system information.
    
    Returns:
        Dict[str, Any]: System information dictionary
        
    Example:
        >>> info = get_system_info()
        >>> 'platform' in info
        True
    """
    try:
        return {
            'platform': platform.system(),
            'platform_release': platform.release(),
            'platform_version': platform.version(),
            'architecture': platform.machine(),
            'hostname': platform.node(),
            'processor': platform.processor(),
            'python_version': platform.python_version(),
            'python_implementation': platform.python_implementation(),
            'os_name': os.name,
            'current_directory': os.getcwd(),
            'user': os.getenv('USER') or os.getenv('USERNAME', 'unknown')
        }
    except Exception as e:
        raise SystemError(f"Cannot get system info: {e}")

def get_python_info() -> Dict[str, Any]:
    """
    Get detailed Python interpreter information.
    
    Returns:
        Dict[str, Any]: Python information dictionary
        
    Example:
        >>> info = get_python_info()
        >>> 'version' in info
        True
    """
    try:
        return {
            'version': sys.version,
            'version_info': {
                'major': sys.version_info.major,
                'minor': sys.version_info.minor,
                'micro': sys.version_info.micro,
                'releaselevel': sys.version_info.releaselevel,
                'serial': sys.version_info.serial
            },
            'executable': sys.executable,
            'platform': sys.platform,
            'implementation': platform.python_implementation(),
            'compiler': platform.python_compiler(),
            'build': platform.python_build(),
            'path': sys.path[:5],  # First 5 entries
            'modules_count': len(sys.modules),
            'recursion_limit': sys.getrecursionlimit(),
            'default_encoding': sys.getdefaultencoding()
        }
    except Exception as e:
        raise SystemError(f"Cannot get Python info: {e}")

def get_disk_usage(path: str = ".") -> Dict[str, Any]:
    """
    Get disk usage information for specified path.
    
    Args:
        path (str): Path to check (default: current directory)
        
    Returns:
        Dict[str, Any]: Disk usage information
        
    Example:
        >>> usage = get_disk_usage()
        >>> 'total' in usage
        True
    """
    if not os.path.exists(path):
        raise SystemError(f"Path does not exist: {path}")
    
    try:
        total, used, free = shutil.disk_usage(path)
        
        return {
            'total': total,
            'used': used,
            'free': free,
            'total_human': _format_bytes(total),
            'used_human': _format_bytes(used),
            'free_human': _format_bytes(free),
            'usage_percent': round((used / total) * 100, 2) if total > 0 else 0,
            'path': os.path.abspath(path)
        }
    except Exception as e:
        raise SystemError(f"Cannot get disk usage: {e}")

def get_memory_info() -> Dict[str, Any]:
    """
    Get basic memory information (limited without external libraries).
    
    Returns:
        Dict[str, Any]: Memory information
        
    Note:
        This provides basic info. For detailed memory stats, use psutil library.
    """
    try:
        import resource
        
        # Get memory usage of current process
        usage = resource.getrusage(resource.RUSAGE_SELF)
        
        return {
            'max_rss': usage.ru_maxrss,  # Maximum resident set size
            'max_rss_human': _format_bytes(usage.ru_maxrss * 1024),  # Convert to bytes
            'user_time': usage.ru_utime,  # User CPU time
            'system_time': usage.ru_stime,  # System CPU time
            'page_faults': usage.ru_majflt,  # Major page faults
            'note': 'Limited info without psutil library'
        }
    except ImportError:
        return {
            'error': 'Memory info requires resource module (Unix only)',
            'note': 'Install psutil for detailed memory information'
        }
    except Exception as e:
        raise SystemError(f"Cannot get memory info: {e}")

def get_network_info() -> Dict[str, Any]:
    """
    Get basic network information.
    
    Returns:
        Dict[str, Any]: Network information
        
    Note:
        This provides basic info. For detailed network stats, use psutil library.
    """
    try:
        import socket
        
        hostname = socket.gethostname()
        
        try:
            local_ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            local_ip = "127.0.0.1"
        
        return {
            'hostname': hostname,
            'local_ip': local_ip,
            'fqdn': socket.getfqdn(),
            'note': 'Limited info without psutil library'
        }
    except Exception as e:
        raise SystemError(f"Cannot get network info: {e}")

def get_environment_summary() -> Dict[str, Any]:
    """
    Get summary of important environment information.
    
    Returns:
        Dict[str, Any]: Environment summary
        
    Example:
        >>> summary = get_environment_summary()
        >>> 'python' in summary
        True
    """
    try:
        return {
            'python': {
                'version': platform.python_version(),
                'executable': sys.executable,
                'implementation': platform.python_implementation()
            },
            'system': {
                'platform': platform.system(),
                'release': platform.release(),
                'machine': platform.machine()
            },
            'paths': {
                'current_dir': os.getcwd(),
                'home_dir': os.path.expanduser("~"),
                'temp_dir': os.environ.get('TEMP') or os.environ.get('TMP') or '/tmp'
            },
            'user': {
                'name': os.getenv('USER') or os.getenv('USERNAME', 'unknown'),
                'shell': os.getenv('SHELL', 'unknown')
            }
        }
    except Exception as e:
        raise SystemError(f"Cannot get environment summary: {e}")

def _format_bytes(bytes_size: int) -> str:
    """Format bytes in human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} PB"