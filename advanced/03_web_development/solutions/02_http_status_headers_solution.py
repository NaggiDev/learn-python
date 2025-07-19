"""
Solution: HTTP Status Codes and Headers

This file contains the complete solutions for the HTTP status codes and headers exercise.
"""

import requests
from typing import Dict, Any, List, Optional
import re


def categorize_status_code(status_code: int) -> Dict[str, Any]:
    """
    Categorize an HTTP status code and provide information about it.
    """
    # Status code descriptions
    descriptions = {
        # 1xx Informational
        100: "Continue",
        101: "Switching Protocols",
        102: "Processing",
        
        # 2xx Success
        200: "OK",
        201: "Created",
        202: "Accepted",
        204: "No Content",
        206: "Partial Content",
        
        # 3xx Redirection
        300: "Multiple Choices",
        301: "Moved Permanently",
        302: "Found",
        304: "Not Modified",
        307: "Temporary Redirect",
        308: "Permanent Redirect",
        
        # 4xx Client Error
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        409: "Conflict",
        422: "Unprocessable Entity",
        429: "Too Many Requests",
        
        # 5xx Server Error
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout"
    }
    
    # Determine category
    if 100 <= status_code < 200:
        category = 'informational'
        is_error = False
        should_retry = False
    elif 200 <= status_code < 300:
        category = 'success'
        is_error = False
        should_retry = False
    elif 300 <= status_code < 400:
        category = 'redirection'
        is_error = False
        should_retry = False
    elif 400 <= status_code < 500:
        category = 'client_error'
        is_error = True
        should_retry = status_code in [408, 429]  # Request Timeout, Too Many Requests
    elif 500 <= status_code < 600:
        category = 'server_error'
        is_error = True
        should_retry = True
    else:
        category = 'unknown'
        is_error = True
        should_retry = False
    
    description = descriptions.get(status_code, f"Unknown status code {status_code}")
    
    return {
        'category': category,
        'description': description,
        'is_error': is_error,
        'should_retry': should_retry
    }


def test_different_status_codes(base_url: str = 'https://httpbin.org/status') -> Dict[str, Any]:
    """
    Test different HTTP status codes by making requests to endpoints that return specific codes.
    """
    test_codes = [200, 201, 204, 301, 302, 400, 401, 403, 404, 500, 502, 503]
    results = []
    successful_tests = 0
    
    for code in test_codes:
        try:
            url = f"{base_url}/{code}"
            response = requests.get(url, timeout=10, allow_redirects=False)
            
            received_code = response.status_code
            category_info = categorize_status_code(received_code)
            success = received_code == code
            
            if success:
                successful_tests += 1
            
            results.append({
                'status_code': code,
                'received_code': received_code,
                'category': category_info['category'],
                'success': success
            })
            
        except Exception as e:
            results.append({
                'status_code': code,
                'received_code': None,
                'category': 'error',
                'success': False,
                'error': str(e)
            })
    
    return {
        'results': results,
        'total_tests': len(test_codes),
        'successful_tests': successful_tests
    }


def analyze_request_headers(url: str, custom_headers: Dict[str, str]) -> Dict[str, Any]:
    """
    Make a request with custom headers and analyze what headers were sent.
    """
    try:
        response = requests.get(url, headers=custom_headers, timeout=10)
        
        # httpbin.org/headers returns the headers that were sent
        response_data = response.json() if response.status_code == 200 else {}
        sent_headers = response_data.get('headers', {})
        
        # Check if custom headers were echoed back
        custom_headers_echoed = all(
            key in sent_headers and sent_headers[key] == value
            for key, value in custom_headers.items()
        )
        
        return {
            'sent_headers': sent_headers,
            'received_headers': dict(response.headers),
            'custom_headers_echoed': custom_headers_echoed,
            'user_agent': sent_headers.get('User-Agent'),
            'content_type': sent_headers.get('Content-Type')
        }
        
    except Exception as e:
        return {
            'sent_headers': {},
            'received_headers': {},
            'custom_headers_echoed': False,
            'user_agent': None,
            'content_type': None,
            'error': str(e)
        }


def handle_redirects(url: str, follow_redirects: bool = True) -> Dict[str, Any]:
    """
    Make a request and analyze redirect behavior.
    """
    try:
        response = requests.get(url, allow_redirects=follow_redirects, timeout=10)
        
        # Count redirects from response history
        redirect_count = len(response.history)
        
        # Build redirect chain
        redirect_chain = [r.url for r in response.history] + [response.url]
        
        return {
            'final_status_code': response.status_code,
            'redirect_count': redirect_count,
            'final_url': response.url,
            'redirect_chain': redirect_chain,
            'followed_redirects': follow_redirects
        }
        
    except Exception as e:
        return {
            'final_status_code': None,
            'redirect_count': 0,
            'final_url': None,
            'redirect_chain': [],
            'followed_redirects': follow_redirects,
            'error': str(e)
        }


def test_content_negotiation(base_url: str = 'https://httpbin.org') -> Dict[str, Any]:
    """
    Test content negotiation by requesting different content types.
    """
    def make_request_with_accept(accept_header):
        try:
            headers = {'Accept': accept_header} if accept_header else {}
            response = requests.get(f"{base_url}/headers", headers=headers, timeout=10)
            
            return {
                'content_type': response.headers.get('Content-Type'),
                'status_code': response.status_code,
                'data_preview': response.text[:100] if response.text else ''
            }
        except Exception as e:
            return {
                'content_type': None,
                'status_code': None,
                'data_preview': '',
                'error': str(e)
            }
    
    return {
        'json_response': make_request_with_accept('application/json'),
        'xml_response': make_request_with_accept('application/xml'),
        'html_response': make_request_with_accept('text/html'),
        'default_response': make_request_with_accept(None)
    }


def analyze_caching_headers(url: str) -> Dict[str, Any]:
    """
    Analyze caching-related headers in a response.
    """
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        cache_control = headers.get('Cache-Control')
        expires = headers.get('Expires')
        etag = headers.get('ETag')
        last_modified = headers.get('Last-Modified')
        
        # Determine if response is cacheable
        is_cacheable = False
        max_age = None
        
        if cache_control:
            # Check for no-cache, no-store directives
            if 'no-cache' not in cache_control.lower() and 'no-store' not in cache_control.lower():
                is_cacheable = True
                
                # Extract max-age value
                max_age_match = re.search(r'max-age=(\d+)', cache_control)
                if max_age_match:
                    max_age = int(max_age_match.group(1))
        
        # If no cache-control but has expires, it might be cacheable
        if not cache_control and expires:
            is_cacheable = True
        
        return {
            'cache_control': cache_control,
            'expires': expires,
            'etag': etag,
            'last_modified': last_modified,
            'is_cacheable': is_cacheable,
            'max_age': max_age
        }
        
    except Exception as e:
        return {
            'cache_control': None,
            'expires': None,
            'etag': None,
            'last_modified': None,
            'is_cacheable': False,
            'max_age': None,
            'error': str(e)
        }


def test_conditional_requests(url: str = 'https://httpbin.org/etag/test-etag') -> Dict[str, Any]:
    """
    Test conditional requests using If-None-Match and If-Modified-Since headers.
    """
    try:
        # First request to get ETag
        first_response = requests.get(url, timeout=10)
        first_result = {
            'status_code': first_response.status_code,
            'etag': first_response.headers.get('ETag'),
            'last_modified': first_response.headers.get('Last-Modified')
        }
        
        # Conditional request with If-None-Match
        etag = first_response.headers.get('ETag')
        conditional_headers = {}
        if etag:
            conditional_headers['If-None-Match'] = etag
        
        conditional_response = requests.get(url, headers=conditional_headers, timeout=10)
        conditional_result = {
            'status_code': conditional_response.status_code,
            'etag': conditional_response.headers.get('ETag')
        }
        
        return {
            'first_request': first_result,
            'conditional_request': conditional_result,
            'etag_matched': etag is not None,
            'not_modified': conditional_response.status_code == 304
        }
        
    except Exception as e:
        return {
            'first_request': {'status_code': None, 'etag': None, 'last_modified': None},
            'conditional_request': {'status_code': None, 'etag': None},
            'etag_matched': False,
            'not_modified': False,
            'error': str(e)
        }


# Test functions (same as in exercise file)
def test_status_code_categorization():
    """Test status code categorization"""
    print("Testing status code categorization...")
    
    result = categorize_status_code(200)
    assert result['category'] == 'success', f"200 should be success, got {result['category']}"
    assert result['is_error'] == False, "200 should not be an error"
    
    result = categorize_status_code(404)
    assert result['category'] == 'client_error', f"404 should be client_error, got {result['category']}"
    assert result['is_error'] == True, "404 should be an error"
    
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
    print("Running HTTP Status Codes and Headers Solution Tests")
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
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    run_all_tests()