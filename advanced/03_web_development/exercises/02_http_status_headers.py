"""
Exercise 2: HTTP Status Codes and Headers

This exercise focuses on understanding and working with HTTP status codes and headers.
You'll practice interpreting different status codes and manipulating request/response headers.

Instructions:
1. Complete each function according to the specifications
2. Run the tests to verify your solutions
3. Pay attention to proper HTTP status code handling
"""

import requests
from typing import Dict, Any, List, Optional


def categorize_status_code(status_code: int) -> Dict[str, Any]:
    """
    Categorize an HTTP status code and provide information about it.
    
    Args:
        status_code: HTTP status code to categorize
    
    Returns:
        Dictionary containing:
        - 'category': Category name ('informational', 'success', 'redirection', 'client_error', 'server_error')
        - 'description': Human-readable description of the status code
        - 'is_error': Boolean indicating if this is an error status
        - 'should_retry': Boolean indicating if the request should be retried
    
    TODO: Implement this function
    """
    # Your code here
    pass


def test_different_status_codes(base_url: str = 'https://httpbin.org/status') -> Dict[str, Any]:
    """
    Test different HTTP status codes by making requests to endpoints that return specific codes.
    
    Args:
        base_url: Base URL for status code testing (httpbin.org/status by default)
    
    Returns:
        Dictionary containing:
        - 'results': List of dictionaries, each containing:
            - 'status_code': The status code that was requested
            - 'received_code': The actual status code received
            - 'category': Category of the status code
            - 'success': Boolean indicating if codes match
        - 'total_tests': Total number of status codes tested
        - 'successful_tests': Number of tests where received code matched expected
    
    Test these status codes: [200, 201, 204, 301, 302, 400, 401, 403, 404, 500, 502, 503]
    
    TODO: Implement this function
    """
    # Your code here
    pass


def analyze_request_headers(url: str, custom_headers: Dict[str, str]) -> Dict[str, Any]:
    """
    Make a request with custom headers and analyze what headers were sent.
    
    Args:
        url: URL to make the request to (use httpbin.org/headers for testing)
        custom_headers: Dictionary of custom headers to send
    
    Returns:
        Dictionary containing:
        - 'sent_headers': Headers that were sent with the request
        - 'received_headers': Headers received in the response
        - 'custom_headers_echoed': Boolean indicating if custom headers were echoed back
        - 'user_agent': The User-Agent header that was sent
        - 'content_type': The Content-Type header that was sent (if any)
    
    TODO: Implement this function
    """
    # Your code here
    pass


def handle_redirects(url: str, follow_redirects: bool = True) -> Dict[str, Any]:
    """
    Make a request and analyze redirect behavior.
    
    Args:
        url: URL that may redirect (use httpbin.org/redirect/3 for testing)
        follow_redirects: Whether to follow redirects automatically
    
    Returns:
        Dictionary containing:
        - 'final_status_code': Final status code after redirects
        - 'redirect_count': Number of redirects that occurred
        - 'final_url': Final URL after all redirects
        - 'redirect_chain': List of URLs in the redirect chain
        - 'followed_redirects': Boolean indicating if redirects were followed
    
    TODO: Implement this function
    """
    # Your code here
    pass


def test_content_negotiation(base_url: str = 'https://httpbin.org') -> Dict[str, Any]:
    """
    Test content negotiation by requesting different content types.
    
    Args:
        base_url: Base URL for testing
    
    Returns:
        Dictionary containing:
        - 'json_response': Response when requesting JSON
        - 'xml_response': Response when requesting XML
        - 'html_response': Response when requesting HTML
        - 'default_response': Response with no Accept header
    
    Each response should contain:
        - 'content_type': Content-Type header from response
        - 'status_code': HTTP status code
        - 'data_preview': First 100 characters of response data
    
    TODO: Implement this function
    """
    # Your code here
    pass


def analyze_caching_headers(url: str) -> Dict[str, Any]:
    """
    Analyze caching-related headers in a response.
    
    Args:
        url: URL to analyze (use httpbin.org/cache for testing)
    
    Returns:
        Dictionary containing:
        - 'cache_control': Cache-Control header value
        - 'expires': Expires header value
        - 'etag': ETag header value
        - 'last_modified': Last-Modified header value
        - 'is_cacheable': Boolean indicating if response appears cacheable
        - 'max_age': Max-age value from Cache-Control (if present)
    
    TODO: Implement this function
    """
    # Your code here
    pass


def test_conditional_requests(url: str) -> Dict[str, Any]:
    """
    Test conditional requests using If-None-Match and If-Modified-Since headers.
    
    Args:
        url: URL to test with (use httpbin.org/etag/{etag} for testing)
    
    Returns:
        Dictionary containing:
        - 'first_request': Response from initial request
        - 'conditional_request': Response from conditional request
        - 'etag_matched': Boolean indicating if ETag was matched
        - 'not_modified': Boolean indicating if 304 Not Modified was returned
    
    TODO: Implement this function
    """
    # Your code here
    pass


# Test functions
def test_status_code_categorization():
    """Test status code categorization"""
    print("Testing status code categorization...")
    
    # Test success status
    result = categorize_status_code(200)
    assert result['category'] == 'success', f"200 should be success, got {result['category']}"
    assert result['is_error'] == False, "200 should not be an error"
    
    # Test client error
    result = categorize_status_code(404)
    assert result['category'] == 'client_error', f"404 should be client_error, got {result['category']}"
    assert result['is_error'] == True, "404 should be an error"
    
    # Test server error
    result = categorize_status_code(500)
    assert result['category'] == 'server_error', f"500 should be server_error, got {result['category']}"
    assert result['is_error'] == True, "500 should be an error"
    assert result['should_retry'] == True, "500 should suggest retry"
    
    print("✓ Status code categorization test passed")


def test_status_code_testing():
    """Test the status code testing function"""
    print("Testing status code testing...")
    
    result = test_different_status_codes()
    
    assert result is not None, "Function should return a result"
    assert 'results' in result, "Result should contain results"
    assert 'total_tests' in result, "Result should contain total_tests"
    assert 'successful_tests' in result, "Result should contain successful_tests"
    
    assert len(result['results']) > 0, "Should have test results"
    assert result['total_tests'] > 0, "Should have tested some status codes"
    
    print("✓ Status code testing test passed")


def test_header_analysis():
    """Test request header analysis"""
    print("Testing header analysis...")
    
    custom_headers = {
        'X-Custom-Header': 'test-value',
        'User-Agent': 'Python-Test/1.0'
    }
    
    result = analyze_request_headers('https://httpbin.org/headers', custom_headers)
    
    assert result is not None, "Function should return a result"
    assert 'sent_headers' in result, "Result should contain sent_headers"
    assert 'user_agent' in result, "Result should contain user_agent"
    
    print("✓ Header analysis test passed")


def test_redirect_handling():
    """Test redirect handling"""
    print("Testing redirect handling...")
    
    result = handle_redirects('https://httpbin.org/redirect/2')
    
    assert result is not None, "Function should return a result"
    assert 'final_status_code' in result, "Result should contain final_status_code"
    assert 'redirect_count' in result, "Result should contain redirect_count"
    assert 'final_url' in result, "Result should contain final_url"
    
    assert result['final_status_code'] == 200, "Should end with 200 status"
    assert result['redirect_count'] >= 0, "Should have non-negative redirect count"
    
    print("✓ Redirect handling test passed")


def test_content_negotiation_function():
    """Test content negotiation"""
    print("Testing content negotiation...")
    
    result = test_content_negotiation()
    
    assert result is not None, "Function should return a result"
    assert 'json_response' in result, "Result should contain json_response"
    assert 'default_response' in result, "Result should contain default_response"
    
    print("✓ Content negotiation test passed")


def test_caching_analysis():
    """Test caching header analysis"""
    print("Testing caching analysis...")
    
    result = analyze_caching_headers('https://httpbin.org/cache/60')
    
    assert result is not None, "Function should return a result"
    assert 'cache_control' in result, "Result should contain cache_control"
    assert 'is_cacheable' in result, "Result should contain is_cacheable"
    
    print("✓ Caching analysis test passed")


def run_all_tests():
    """Run all test functions"""
    print("Running HTTP Status Codes and Headers Exercise Tests")
    print("=" * 50)
    
    try:
        test_status_code_categorization()
        test_status_code_testing()
        test_header_analysis()
        test_redirect_handling()
        test_content_negotiation_function()
        test_caching_analysis()
        
        print("\n" + "=" * 50)
        print("All tests passed! 🎉")
        print("\nYou've successfully completed the HTTP status codes and headers exercise.")
        print("You now understand how to:")
        print("- Categorize and handle different HTTP status codes")
        print("- Work with request and response headers")
        print("- Handle redirects properly")
        print("- Implement content negotiation")
        print("- Analyze caching headers")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("Please review your implementation and try again.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your code for syntax errors.")


if __name__ == "__main__":
    run_all_tests()