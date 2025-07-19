"""
Solution: HTTP Requests with Python

This file contains the complete solutions for the HTTP requests exercise.
"""

import requests
import json
from typing import Dict, Any, Optional
from requests.exceptions import RequestException, Timeout, ConnectionError


def make_get_request(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Make a GET request to the specified URL and return response information.
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # Try to parse JSON, fall back to text
        try:
            data = response.json()
        except (ValueError, json.JSONDecodeError):
            data = response.text
        
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'data': data,
            'success': 200 <= response.status_code < 300
        }
    except Exception as e:
        return {
            'status_code': None,
            'headers': {},
            'data': None,
            'success': False,
            'error': str(e)
        }


def make_post_request(url: str, data: Dict[str, Any], 
                     headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Make a POST request with JSON data.
    """
    try:
        # Set default headers for JSON
        if headers is None:
            headers = {}
        headers.setdefault('Content-Type', 'application/json')
        
        response = requests.post(url, json=data, headers=headers, timeout=10)
        
        # Try to parse JSON, fall back to text
        try:
            response_data = response.json()
        except (ValueError, json.JSONDecodeError):
            response_data = response.text
        
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'data': response_data,
            'success': 200 <= response.status_code < 300
        }
    except Exception as e:
        return {
            'status_code': None,
            'headers': {},
            'data': None,
            'success': False,
            'error': str(e)
        }


def handle_http_errors(url: str) -> Dict[str, Any]:
    """
    Make a request and properly handle different types of HTTP errors.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises HTTPError for bad status codes
        
        return {
            'success': True,
            'status_code': response.status_code,
            'error_type': None,
            'error_message': None
        }
        
    except Timeout:
        return {
            'success': False,
            'status_code': None,
            'error_type': 'timeout',
            'error_message': 'Request timed out'
        }
    except ConnectionError:
        return {
            'success': False,
            'status_code': None,
            'error_type': 'connection',
            'error_message': 'Failed to connect to the server'
        }
    except requests.exceptions.HTTPError as e:
        return {
            'success': False,
            'status_code': e.response.status_code if e.response else None,
            'error_type': 'http',
            'error_message': f'HTTP error: {e}'
        }
    except RequestException as e:
        return {
            'success': False,
            'status_code': None,
            'error_type': 'request',
            'error_message': f'Request failed: {e}'
        }


def analyze_response_headers(url: str) -> Dict[str, Any]:
    """
    Make a request and analyze the response headers.
    """
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        # Extract specific headers
        content_length = headers.get('Content-Length')
        if content_length:
            try:
                content_length = int(content_length)
            except ValueError:
                content_length = None
        
        return {
            'content_type': headers.get('Content-Type'),
            'content_length': content_length,
            'server': headers.get('Server'),
            'cache_control': headers.get('Cache-Control'),
            'all_headers': dict(headers)
        }
    except Exception as e:
        return {
            'content_type': None,
            'content_length': None,
            'server': None,
            'cache_control': None,
            'all_headers': {},
            'error': str(e)
        }


def make_authenticated_request(url: str, token: str) -> Dict[str, Any]:
    """
    Make a GET request with Bearer token authentication.
    """
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # Try to parse JSON response
        try:
            data = response.json()
        except (ValueError, json.JSONDecodeError):
            data = response.text
        
        return {
            'status_code': response.status_code,
            'authenticated': response.status_code == 200,
            'data': data if response.status_code == 200 else None,
            'error': None if response.status_code == 200 else f'Authentication failed with status {response.status_code}'
        }
    except Exception as e:
        return {
            'status_code': None,
            'authenticated': False,
            'data': None,
            'error': str(e)
        }


def download_file(url: str, filename: str) -> Dict[str, Any]:
    """
    Download a file from the given URL and save it locally.
    """
    try:
        response = requests.get(url, timeout=30, stream=True)
        response.raise_for_status()
        
        file_size = 0
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    file_size += len(chunk)
        
        return {
            'success': True,
            'file_size': file_size,
            'content_type': response.headers.get('Content-Type'),
            'error': None
        }
    except Exception as e:
        return {
            'success': False,
            'file_size': 0,
            'content_type': None,
            'error': str(e)
        }


def use_session_for_multiple_requests(base_url: str, endpoints: list) -> Dict[str, Any]:
    """
    Use a requests session to make multiple requests efficiently.
    """
    results = []
    successful_requests = 0
    
    with requests.Session() as session:
        # Set common headers for all requests in the session
        session.headers.update({
            'User-Agent': 'Python-Exercise/1.0'
        })
        
        for endpoint in endpoints:
            try:
                url = base_url.rstrip('/') + '/' + endpoint.lstrip('/')
                response = session.get(url, timeout=10)
                
                success = 200 <= response.status_code < 300
                if success:
                    successful_requests += 1
                
                results.append({
                    'endpoint': endpoint,
                    'status_code': response.status_code,
                    'success': success
                })
            except Exception as e:
                results.append({
                    'endpoint': endpoint,
                    'status_code': None,
                    'success': False,
                    'error': str(e)
                })
    
    return {
        'results': results,
        'total_requests': len(endpoints),
        'successful_requests': successful_requests
    }


# Test functions (same as in the exercise file)
def test_get_request():
    """Test the GET request function"""
    print("Testing GET request...")
    
    result = make_get_request('https://httpbin.org/get')
    
    assert result is not None, "Function should return a result"
    assert 'status_code' in result, "Result should contain status_code"
    assert 'headers' in result, "Result should contain headers"
    assert 'data' in result, "Result should contain data"
    assert 'success' in result, "Result should contain success flag"
    
    assert result['status_code'] == 200, f"Expected status 200, got {result['status_code']}"
    assert result['success'] == True, "Request should be successful"
    
    print("✓ GET request test passed")


def test_post_request():
    """Test the POST request function"""
    print("Testing POST request...")
    
    test_data = {'name': 'Test User', 'email': 'test@example.com'}
    result = make_post_request('https://httpbin.org/post', test_data)
    
    assert result is not None, "Function should return a result"
    assert result['status_code'] == 200, f"Expected status 200, got {result['status_code']}"
    assert result['success'] == True, "Request should be successful"
    
    if isinstance(result['data'], dict) and 'json' in result['data']:
        assert result['data']['json'] == test_data, "Posted data should be echoed back"
    
    print("✓ POST request test passed")


def test_error_handling():
    """Test error handling function"""
    print("Testing error handling...")
    
    result = handle_http_errors('https://this-domain-does-not-exist-12345.com')
    
    assert result is not None, "Function should return a result"
    assert 'success' in result, "Result should contain success flag"
    assert 'error_type' in result, "Result should contain error_type"
    assert 'error_message' in result, "Result should contain error_message"
    
    assert result['success'] == False, "Request should not be successful"
    assert result['error_type'] is not None, "Error type should be specified"
    
    print("✓ Error handling test passed")


def test_header_analysis():
    """Test response header analysis"""
    print("Testing header analysis...")
    
    result = analyze_response_headers('https://httpbin.org/get')
    
    assert result is not None, "Function should return a result"
    assert 'content_type' in result, "Result should contain content_type"
    assert 'all_headers' in result, "Result should contain all_headers"
    
    assert isinstance(result['all_headers'], dict), "all_headers should be a dictionary"
    
    print("✓ Header analysis test passed")


def test_authenticated_request():
    """Test authenticated request function"""
    print("Testing authenticated request...")
    
    result = make_authenticated_request('https://httpbin.org/bearer', 'test-token')
    
    assert result is not None, "Function should return a result"
    assert 'status_code' in result, "Result should contain status_code"
    assert 'authenticated' in result, "Result should contain authenticated flag"
    
    assert result['status_code'] == 200, f"Expected status 200, got {result['status_code']}"
    assert result['authenticated'] == True, "Authentication should be successful"
    
    print("✓ Authenticated request test passed")


def test_session_requests():
    """Test session-based requests"""
    print("Testing session requests...")
    
    endpoints = ['/get', '/headers', '/user-agent']
    result = use_session_for_multiple_requests('https://httpbin.org', endpoints)
    
    assert result is not None, "Function should return a result"
    assert 'results' in result, "Result should contain results"
    assert 'total_requests' in result, "Result should contain total_requests"
    assert 'successful_requests' in result, "Result should contain successful_requests"
    
    assert len(result['results']) == len(endpoints), "Should have results for all endpoints"
    assert result['total_requests'] == len(endpoints), "Total requests should match endpoint count"
    
    print("✓ Session requests test passed")


def run_all_tests():
    """Run all test functions"""
    print("Running HTTP Requests Solution Tests")
    print("=" * 40)
    
    try:
        test_get_request()
        test_post_request()
        test_error_handling()
        test_header_analysis()
        test_authenticated_request()
        test_session_requests()
        
        print("\n" + "=" * 40)
        print("All tests passed! 🎉")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    run_all_tests()