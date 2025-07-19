"""
Exercise 1: HTTP Requests with Python

This exercise will help you practice making HTTP requests using the requests library.
You'll learn to handle different HTTP methods, status codes, headers, and error handling.

Instructions:
1. Complete each function according to the specifications
2. Run the tests to verify your solutions
3. Pay attention to error handling and proper HTTP practices
"""

import requests
import json
from typing import Dict, Any, Optional


def make_get_request(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Make a GET request to the specified URL and return response information.
    
    Args:
        url: The URL to make the request to
        headers: Optional headers to include in the request
    
    Returns:
        Dictionary containing:
        - 'status_code': HTTP status code
        - 'headers': Response headers (as dict)
        - 'data': Response data (parsed JSON if possible, otherwise text)
        - 'success': Boolean indicating if request was successful (2xx status)
    
    TODO: Implement this function
    """
    # Your code here
    pass


def make_post_request(url: str, data: Dict[str, Any], 
                     headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Make a POST request with JSON data.
    
    Args:
        url: The URL to make the request to
        data: Dictionary to send as JSON in the request body
        headers: Optional headers to include in the request
    
    Returns:
        Dictionary containing:
        - 'status_code': HTTP status code
        - 'headers': Response headers (as dict)
        - 'data': Response data (parsed JSON if possible, otherwise text)
        - 'success': Boolean indicating if request was successful (2xx status)
    
    TODO: Implement this function
    """
    # Your code here
    pass


def handle_http_errors(url: str) -> Dict[str, Any]:
    """
    Make a request and properly handle different types of HTTP errors.
    
    Args:
        url: The URL to make the request to
    
    Returns:
        Dictionary containing:
        - 'success': Boolean indicating if request completed without exceptions
        - 'status_code': HTTP status code (if request completed)
        - 'error_type': Type of error that occurred (if any)
        - 'error_message': Human-readable error message
    
    Handle these specific cases:
    - Timeout errors
    - Connection errors
    - HTTP errors (4xx, 5xx status codes)
    - General request exceptions
    
    TODO: Implement this function
    """
    # Your code here
    pass


def analyze_response_headers(url: str) -> Dict[str, Any]:
    """
    Make a request and analyze the response headers.
    
    Args:
        url: The URL to make the request to
    
    Returns:
        Dictionary containing:
        - 'content_type': Content-Type header value
        - 'content_length': Content-Length header value (as int, or None)
        - 'server': Server header value
        - 'cache_control': Cache-Control header value
        - 'all_headers': All headers as a dictionary
    
    TODO: Implement this function
    """
    # Your code here
    pass


def make_authenticated_request(url: str, token: str) -> Dict[str, Any]:
    """
    Make a GET request with Bearer token authentication.
    
    Args:
        url: The URL to make the request to
        token: Bearer token for authentication
    
    Returns:
        Dictionary containing:
        - 'status_code': HTTP status code
        - 'authenticated': Boolean indicating if authentication was successful
        - 'data': Response data (if successful)
        - 'error': Error message (if authentication failed)
    
    TODO: Implement this function
    """
    # Your code here
    pass


def download_file(url: str, filename: str) -> Dict[str, Any]:
    """
    Download a file from the given URL and save it locally.
    
    Args:
        url: URL of the file to download
        filename: Local filename to save the file as
    
    Returns:
        Dictionary containing:
        - 'success': Boolean indicating if download was successful
        - 'file_size': Size of downloaded file in bytes
        - 'content_type': Content-Type of the downloaded file
        - 'error': Error message (if download failed)
    
    TODO: Implement this function
    """
    # Your code here
    pass


def use_session_for_multiple_requests(base_url: str, endpoints: list) -> Dict[str, Any]:
    """
    Use a requests session to make multiple requests efficiently.
    
    Args:
        base_url: Base URL for all requests
        endpoints: List of endpoint paths to request
    
    Returns:
        Dictionary containing:
        - 'results': List of dictionaries, each containing:
            - 'endpoint': The endpoint that was requested
            - 'status_code': HTTP status code
            - 'success': Boolean indicating success
        - 'total_requests': Total number of requests made
        - 'successful_requests': Number of successful requests
    
    TODO: Implement this function using requests.Session()
    """
    # Your code here
    pass


# Test functions
def test_get_request():
    """Test the GET request function"""
    print("Testing GET request...")
    
    # Test with a public API
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
    
    # Check if our data was echoed back
    if isinstance(result['data'], dict) and 'json' in result['data']:
        assert result['data']['json'] == test_data, "Posted data should be echoed back"
    
    print("✓ POST request test passed")


def test_error_handling():
    """Test error handling function"""
    print("Testing error handling...")
    
    # Test with a non-existent domain
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
    
    # Test with httpbin's bearer auth endpoint
    result = make_authenticated_request('https://httpbin.org/bearer', 'test-token')
    
    assert result is not None, "Function should return a result"
    assert 'status_code' in result, "Result should contain status_code"
    assert 'authenticated' in result, "Result should contain authenticated flag"
    
    # httpbin should return 200 for any bearer token
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
    print("Running HTTP Requests Exercise Tests")
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
        print("\nYou've successfully completed the HTTP requests exercise.")
        print("You now understand how to:")
        print("- Make GET and POST requests")
        print("- Handle HTTP errors properly")
        print("- Analyze response headers")
        print("- Use authentication")
        print("- Use sessions for multiple requests")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("Please review your implementation and try again.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your code for syntax errors.")


if __name__ == "__main__":
    run_all_tests()