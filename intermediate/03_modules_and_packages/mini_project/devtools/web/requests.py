"""HTTP request utilities."""

import json
from typing import Dict, Any, Optional
from ..exceptions import WebError

def make_request(url: str, method: str = "GET", headers: Optional[Dict[str, str]] = None,
                data: Optional[Dict[str, Any]] = None, timeout: int = 30) -> Dict[str, Any]:
    """
    Make HTTP request (simplified implementation without external dependencies).
    
    Args:
        url (str): URL to request
        method (str): HTTP method
        headers (Dict, optional): Request headers
        data (Dict, optional): Request data
        timeout (int): Request timeout in seconds
        
    Returns:
        Dict[str, Any]: Response information
        
    Note:
        This is a simplified implementation. For production use, install requests library.
        
    Example:
        >>> # This would work with requests library installed
        >>> # response = make_request("https://httpbin.org/get")
        >>> # response['status_code'] == 200
        True
    """
    try:
        # Try to use requests library if available
        import requests
        
        kwargs = {'timeout': timeout}
        if headers:
            kwargs['headers'] = headers
        if data and method.upper() in ['POST', 'PUT', 'PATCH']:
            kwargs['json'] = data
        
        response = requests.request(method.upper(), url, **kwargs)
        
        # Try to parse JSON response
        try:
            response_data = response.json()
        except (ValueError, json.JSONDecodeError):
            response_data = response.text
        
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'data': response_data,
            'url': response.url,
            'ok': response.ok,
            'reason': response.reason
        }
        
    except ImportError:
        # Fallback implementation using urllib
        import urllib.request
        import urllib.parse
        import urllib.error
        
        try:
            # Prepare request
            if data and method.upper() in ['POST', 'PUT', 'PATCH']:
                data_bytes = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=data_bytes, method=method.upper())
                req.add_header('Content-Type', 'application/json')
            else:
                req = urllib.request.Request(url, method=method.upper())
            
            # Add headers
            if headers:
                for key, value in headers.items():
                    req.add_header(key, value)
            
            # Make request
            with urllib.request.urlopen(req, timeout=timeout) as response:
                response_data = response.read().decode('utf-8')
                
                # Try to parse JSON
                try:
                    response_data = json.loads(response_data)
                except (ValueError, json.JSONDecodeError):
                    pass
                
                return {
                    'status_code': response.getcode(),
                    'headers': dict(response.headers),
                    'data': response_data,
                    'url': response.geturl(),
                    'ok': 200 <= response.getcode() < 300,
                    'reason': response.reason if hasattr(response, 'reason') else 'OK'
                }
                
        except urllib.error.HTTPError as e:
            return {
                'status_code': e.code,
                'headers': dict(e.headers) if e.headers else {},
                'data': e.read().decode('utf-8') if e.fp else '',
                'url': url,
                'ok': False,
                'reason': e.reason
            }
        except Exception as e:
            raise WebError(f"Request failed: {e}")

def check_url_status(url: str, timeout: int = 10) -> Dict[str, Any]:
    """
    Check URL status with HEAD request.
    
    Args:
        url (str): URL to check
        timeout (int): Request timeout
        
    Returns:
        Dict[str, Any]: Status information
        
    Example:
        >>> status = check_url_status("https://httpbin.org")
        >>> 'status_code' in status
        True
    """
    try:
        response = make_request(url, method="HEAD", timeout=timeout)
        return {
            'url': url,
            'status_code': response['status_code'],
            'ok': response['ok'],
            'reason': response['reason'],
            'accessible': response['ok']
        }
    except Exception as e:
        return {
            'url': url,
            'status_code': 0,
            'ok': False,
            'reason': str(e),
            'accessible': False
        }

def download_file(url: str, filepath: str, chunk_size: int = 8192) -> Dict[str, Any]:
    """
    Download file from URL.
    
    Args:
        url (str): URL to download from
        filepath (str): Local file path to save to
        chunk_size (int): Download chunk size
        
    Returns:
        Dict[str, Any]: Download information
        
    Example:
        >>> # result = download_file("https://httpbin.org/json", "test.json")
        >>> # result['success'] == True
        True
    """
    try:
        # Try requests library first
        import requests
        
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = 0
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    total_size += len(chunk)
        
        return {
            'success': True,
            'filepath': filepath,
            'size': total_size,
            'url': url,
            'status_code': response.status_code
        }
        
    except ImportError:
        # Fallback to urllib
        import urllib.request
        
        try:
            with urllib.request.urlopen(url) as response:
                with open(filepath, 'wb') as f:
                    total_size = 0
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        f.write(chunk)
                        total_size += len(chunk)
            
            return {
                'success': True,
                'filepath': filepath,
                'size': total_size,
                'url': url,
                'status_code': 200
            }
            
        except Exception as e:
            return {
                'success': False,
                'filepath': filepath,
                'error': str(e),
                'url': url,
                'status_code': 0
            }
            
    except Exception as e:
        return {
            'success': False,
            'filepath': filepath,
            'error': str(e),
            'url': url,
            'status_code': getattr(e, 'response', {}).get('status_code', 0)
        }

def get_url_info(url: str) -> Dict[str, Any]:
    """
    Get comprehensive information about a URL.
    
    Args:
        url (str): URL to analyze
        
    Returns:
        Dict[str, Any]: URL information
        
    Example:
        >>> info = get_url_info("https://httpbin.org")
        >>> 'domain' in info
        True
    """
    from .urls import parse_url, extract_domain
    
    try:
        # Parse URL
        parsed = parse_url(url)
        
        # Check status
        status = check_url_status(url)
        
        return {
            'url': url,
            'domain': extract_domain(url),
            'scheme': parsed['scheme'],
            'path': parsed['path'],
            'query_params': parsed['query_params'],
            'status': status,
            'is_secure': parsed['scheme'] == 'https',
            'has_query': bool(parsed['query']),
            'has_fragment': bool(parsed['fragment'])
        }
        
    except Exception as e:
        raise WebError(f"Cannot get URL info: {e}")