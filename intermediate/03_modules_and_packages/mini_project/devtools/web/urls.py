"""URL utilities."""

import re
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from typing import Dict, Any, Optional
from ..exceptions import WebError

def validate_url(url: str) -> bool:
    """
    Validate URL format.
    
    Args:
        url (str): URL to validate
        
    Returns:
        bool: True if valid URL
        
    Example:
        >>> validate_url("https://www.example.com")
        True
        >>> validate_url("not-a-url")
        False
    """
    if not isinstance(url, str):
        return False
    
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse URL into components.
    
    Args:
        url (str): URL to parse
        
    Returns:
        Dict[str, Any]: URL components
        
    Example:
        >>> components = parse_url("https://example.com:8080/path?param=value#section")
        >>> components['scheme']
        'https'
    """
    if not isinstance(url, str):
        raise WebError("URL must be a string")
    
    if not validate_url(url):
        raise WebError(f"Invalid URL: {url}")
    
    try:
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        
        return {
            'scheme': parsed.scheme,
            'netloc': parsed.netloc,
            'hostname': parsed.hostname,
            'port': parsed.port,
            'path': parsed.path,
            'params': parsed.params,
            'query': parsed.query,
            'query_params': query_params,
            'fragment': parsed.fragment,
            'username': parsed.username,
            'password': parsed.password
        }
    except Exception as e:
        raise WebError(f"Cannot parse URL: {e}")

def build_url(scheme: str, hostname: str, path: str = "", 
              query_params: Optional[Dict[str, str]] = None,
              port: Optional[int] = None, fragment: str = "") -> str:
    """
    Build URL from components.
    
    Args:
        scheme (str): URL scheme (http, https)
        hostname (str): Hostname
        path (str): URL path
        query_params (Dict, optional): Query parameters
        port (int, optional): Port number
        fragment (str): URL fragment
        
    Returns:
        str: Built URL
        
    Example:
        >>> url = build_url("https", "example.com", "/api", {"key": "value"})
        >>> "https://example.com/api?key=value" == url
        True
    """
    if not scheme or not hostname:
        raise WebError("Scheme and hostname are required")
    
    # Build netloc
    netloc = hostname
    if port:
        netloc = f"{hostname}:{port}"
    
    # Build query string
    query = ""
    if query_params:
        query = urlencode(query_params)
    
    # Build URL
    url_parts = (scheme, netloc, path, "", query, fragment)
    return urlunparse(url_parts)

def extract_domain(url: str) -> str:
    """
    Extract domain from URL.
    
    Args:
        url (str): URL to extract domain from
        
    Returns:
        str: Domain name
        
    Example:
        >>> extract_domain("https://www.example.com/path")
        'www.example.com'
    """
    if not validate_url(url):
        raise WebError(f"Invalid URL: {url}")
    
    try:
        parsed = urlparse(url)
        return parsed.netloc
    except Exception as e:
        raise WebError(f"Cannot extract domain: {e}")

def get_base_url(url: str) -> str:
    """
    Get base URL (scheme + netloc).
    
    Args:
        url (str): Full URL
        
    Returns:
        str: Base URL
        
    Example:
        >>> get_base_url("https://example.com/path/to/page")
        'https://example.com'
    """
    if not validate_url(url):
        raise WebError(f"Invalid URL: {url}")
    
    try:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"
    except Exception as e:
        raise WebError(f"Cannot get base URL: {e}")

def add_query_params(url: str, params: Dict[str, str]) -> str:
    """
    Add query parameters to URL.
    
    Args:
        url (str): Base URL
        params (Dict[str, str]): Parameters to add
        
    Returns:
        str: URL with added parameters
        
    Example:
        >>> url = add_query_params("https://example.com", {"key": "value"})
        >>> "key=value" in url
        True
    """
    if not validate_url(url):
        raise WebError(f"Invalid URL: {url}")
    
    try:
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        
        # Add new parameters
        for key, value in params.items():
            query_params[key] = [value]
        
        # Build new query string
        query = urlencode(query_params, doseq=True)
        
        # Rebuild URL
        new_parts = (parsed.scheme, parsed.netloc, parsed.path, 
                    parsed.params, query, parsed.fragment)
        return urlunparse(new_parts)
    except Exception as e:
        raise WebError(f"Cannot add query parameters: {e}")

def remove_query_params(url: str, params_to_remove: list = None) -> str:
    """
    Remove query parameters from URL.
    
    Args:
        url (str): URL with parameters
        params_to_remove (list, optional): Specific parameters to remove
        
    Returns:
        str: URL without specified parameters
        
    Example:
        >>> url = remove_query_params("https://example.com?key=value&other=data", ["key"])
        >>> "key=value" not in url
        True
    """
    if not validate_url(url):
        raise WebError(f"Invalid URL: {url}")
    
    try:
        parsed = urlparse(url)
        
        if params_to_remove is None:
            # Remove all parameters
            query = ""
        else:
            query_params = parse_qs(parsed.query)
            
            # Remove specified parameters
            for param in params_to_remove:
                query_params.pop(param, None)
            
            # Build new query string
            query = urlencode(query_params, doseq=True)
        
        # Rebuild URL
        new_parts = (parsed.scheme, parsed.netloc, parsed.path, 
                    parsed.params, query, parsed.fragment)
        return urlunparse(new_parts)
    except Exception as e:
        raise WebError(f"Cannot remove query parameters: {e}")

def is_absolute_url(url: str) -> bool:
    """
    Check if URL is absolute (has scheme).
    
    Args:
        url (str): URL to check
        
    Returns:
        bool: True if absolute URL
        
    Example:
        >>> is_absolute_url("https://example.com")
        True
        >>> is_absolute_url("/relative/path")
        False
    """
    if not isinstance(url, str):
        return False
    
    try:
        parsed = urlparse(url)
        return bool(parsed.scheme)
    except Exception:
        return False

def join_urls(base_url: str, relative_url: str) -> str:
    """
    Join base URL with relative URL.
    
    Args:
        base_url (str): Base URL
        relative_url (str): Relative URL or path
        
    Returns:
        str: Joined URL
        
    Example:
        >>> join_urls("https://example.com", "/api/data")
        'https://example.com/api/data'
    """
    from urllib.parse import urljoin
    
    if not validate_url(base_url):
        raise WebError(f"Invalid base URL: {base_url}")
    
    try:
        return urljoin(base_url, relative_url)
    except Exception as e:
        raise WebError(f"Cannot join URLs: {e}")