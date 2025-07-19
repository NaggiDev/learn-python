"""
RESTful API Client Library - Review Exercise

This exercise combines multiple intermediate concepts while introducing web development:
- Object-oriented programming (classes, inheritance, composition)
- Module organization and package structure
- Testing with mocks and fixtures
- Error handling and custom exceptions
- Functional programming patterns
- Introduction to HTTP and web APIs (advanced topic)

Requirements:
1. Create an APIClient library that can:
   - Make HTTP requests (GET, POST, PUT, DELETE)
   - Handle authentication (API keys, tokens)
   - Implement retry logic and rate limiting
   - Parse and validate responses
   - Provide a fluent interface for building requests
   - Cache responses when appropriate
   - Log requests and responses for debugging

2. Implement proper OOP design with inheritance and composition
3. Use decorators for authentication, caching, and rate limiting
4. Include comprehensive test coverage with mocking
5. Demonstrate functional programming concepts

This bridges to advanced concepts by introducing:
- HTTP protocol and web APIs
- Authentication and security patterns
- Caching strategies and performance optimization
- Network programming concepts
"""

import json
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from functools import wraps
from typing import Any, Dict, List, Optional, Callable, Union
from urllib.parse import urljoin, urlparse
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class HTTPMethod(Enum):
    """HTTP methods enumeration."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class AuthType(Enum):
    """Authentication types."""
    NONE = "none"
    API_KEY = "api_key"
    BEARER_TOKEN = "bearer_token"
    BASIC_AUTH = "basic_auth"


@dataclass
class APIResponse:
    """Data class to hold API response information."""
    status_code: int
    data: Any
    headers: Dict[str, str] = field(default_factory=dict)
    response_time: float = 0.0
    cached: bool = False
    error_message: Optional[str] = None


@dataclass
class RateLimitInfo:
    """Information about rate limiting."""
    requests_per_minute: int
    current_requests: int = 0
    window_start: datetime = field(default_factory=datetime.now)


class APIException(Exception):
    """Base exception for API-related errors."""
    
    def __init__(self, message: str, status_code: int = None, response: APIResponse = None):
        """
        Initialize API exception.
        
        Args:
            message: Error message
            status_code: HTTP status code
            response: API response object
        """
        # TODO: Implement API exception initialization
        pass


class AuthenticationError(APIException):
    """Exception for authentication-related errors."""
    pass


class RateLimitError(APIException):
    """Exception for rate limit exceeded errors."""
    pass


class ValidationError(APIException):
    """Exception for request validation errors."""
    pass


def rate_limit_decorator(requests_per_minute: int = 60) -> Callable:
    """
    Decorator to implement rate limiting.
    
    Args:
        requests_per_minute: Maximum requests per minute
        
    Returns:
        Decorator function
    """
    # TODO: Implement rate limiting decorator
    # - Track request timestamps
    # - Enforce rate limits
    # - Raise RateLimitError when exceeded
    # - Use a sliding window approach
    pass


def cache_decorator(ttl_seconds: int = 300) -> Callable:
    """
    Decorator to cache API responses.
    
    Args:
        ttl_seconds: Time to live for cached responses
        
    Returns:
        Decorator function
    """
    # TODO: Implement caching decorator
    # - Cache responses based on request parameters
    # - Implement TTL (time to live)
    # - Return cached responses when available
    # - Mark cached responses appropriately
    pass


def retry_decorator(max_attempts: int = 3, backoff_factor: float = 1.0) -> Callable:
    """
    Decorator for retrying failed API requests.
    
    Args:
        max_attempts: Maximum number of retry attempts
        backoff_factor: Exponential backoff factor
        
    Returns:
        Decorator function
    """
    # TODO: Implement retry decorator with exponential backoff
    # - Retry on specific HTTP status codes (5xx, 429)
    # - Implement exponential backoff
    # - Log retry attempts
    # - Re-raise exception after max attempts
    pass


class Authenticator(ABC):
    """Abstract base class for authentication methods."""
    
    @abstractmethod
    def authenticate_request(self, headers: Dict[str, str]) -> Dict[str, str]:
        """
        Add authentication to request headers.
        
        Args:
            headers: Existing request headers
            
        Returns:
            Updated headers with authentication
        """
        pass
    
    @abstractmethod
    def get_auth_type(self) -> AuthType:
        """Get the authentication type."""
        pass


class APIKeyAuthenticator(Authenticator):
    """API key authentication."""
    
    def __init__(self, api_key: str, header_name: str = "X-API-Key"):
        """
        Initialize API key authenticator.
        
        Args:
            api_key: The API key
            header_name: Header name for the API key
        """
        # TODO: Implement API key authenticator initialization
        pass
    
    def authenticate_request(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Add API key to request headers."""
        # TODO: Implement API key authentication
        pass
    
    def get_auth_type(self) -> AuthType:
        """Get the authentication type."""
        return AuthType.API_KEY


class BearerTokenAuthenticator(Authenticator):
    """Bearer token authentication."""
    
    def __init__(self, token: str):
        """
        Initialize bearer token authenticator.
        
        Args:
            token: The bearer token
        """
        # TODO: Implement bearer token authenticator initialization
        pass
    
    def authenticate_request(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Add bearer token to request headers."""
        # TODO: Implement bearer token authentication
        pass
    
    def get_auth_type(self) -> AuthType:
        """Get the authentication type."""
        return AuthType.BEARER_TOKEN


class RequestBuilder:
    """Builder class for constructing API requests."""
    
    def __init__(self, base_url: str):
        """
        Initialize request builder.
        
        Args:
            base_url: Base URL for the API
        """
        # TODO: Implement request builder initialization
        # - Set base URL
        # - Initialize headers, parameters, and data
        pass
    
    def endpoint(self, path: str) -> 'RequestBuilder':
        """
        Set the endpoint path.
        
        Args:
            path: API endpoint path
            
        Returns:
            Self for method chaining
        """
        # TODO: Implement endpoint setting
        pass
    
    def header(self, key: str, value: str) -> 'RequestBuilder':
        """
        Add a header to the request.
        
        Args:
            key: Header name
            value: Header value
            
        Returns:
            Self for method chaining
        """
        # TODO: Implement header addition
        pass
    
    def headers(self, headers: Dict[str, str]) -> 'RequestBuilder':
        """
        Add multiple headers to the request.
        
        Args:
            headers: Dictionary of headers
            
        Returns:
            Self for method chaining
        """
        # TODO: Implement multiple headers addition
        pass
    
    def param(self, key: str, value: Any) -> 'RequestBuilder':
        """
        Add a query parameter.
        
        Args:
            key: Parameter name
            value: Parameter value
            
        Returns:
            Self for method chaining
        """
        # TODO: Implement parameter addition
        pass
    
    def params(self, params: Dict[str, Any]) -> 'RequestBuilder':
        """
        Add multiple query parameters.
        
        Args:
            params: Dictionary of parameters
            
        Returns:
            Self for method chaining
        """
        # TODO: Implement multiple parameters addition
        pass
    
    def json_data(self, data: Dict[str, Any]) -> 'RequestBuilder':
        """
        Set JSON data for the request body.
        
        Args:
            data: Data to be sent as JSON
            
        Returns:
            Self for method chaining
        """
        # TODO: Implement JSON data setting
        pass
    
    def build_url(self) -> str:
        """Build the complete URL for the request."""
        # TODO: Implement URL building
        # - Combine base URL with endpoint
        # - Add query parameters
        pass
    
    def build_request_data(self) -> Dict[str, Any]:
        """Build the complete request data."""
        # TODO: Implement request data building
        # - Return dictionary with all request information
        pass


class ResponseValidator:
    """Validates API responses."""
    
    def __init__(self):
        """Initialize response validator."""
        self.validators = []
    
    def add_validator(self, validator: Callable[[APIResponse], bool]) -> None:
        """
        Add a response validator function.
        
        Args:
            validator: Function that validates response and returns bool
        """
        # TODO: Implement validator addition
        pass
    
    def validate_response(self, response: APIResponse) -> bool:
        """
        Validate a response using all registered validators.
        
        Args:
            response: API response to validate
            
        Returns:
            True if all validators pass, False otherwise
        """
        # TODO: Implement response validation
        # - Run all validators
        # - Return True only if all pass
        pass
    
    def validate_status_code(self, response: APIResponse, expected_codes: List[int] = None) -> bool:
        """
        Validate response status code.
        
        Args:
            response: API response
            expected_codes: List of expected status codes (default: [200])
            
        Returns:
            True if status code is expected
        """
        # TODO: Implement status code validation
        pass
    
    def validate_json_structure(self, response: APIResponse, required_fields: List[str]) -> bool:
        """
        Validate JSON response structure.
        
        Args:
            response: API response
            required_fields: List of required field names
            
        Returns:
            True if all required fields are present
        """
        # TODO: Implement JSON structure validation
        pass


class APIClient:
    """Main API client class."""
    
    def __init__(self, base_url: str, authenticator: Authenticator = None):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for the API
            authenticator: Authentication method
        """
        # TODO: Implement API client initialization
        # - Set base URL and authenticator
        # - Initialize logger, cache, and rate limiter
        # - Set up default headers
        pass
    
    def set_authenticator(self, authenticator: Authenticator) -> None:
        """Set the authentication method."""
        # TODO: Implement authenticator setting
        pass
    
    def create_request(self) -> RequestBuilder:
        """
        Create a new request builder.
        
        Returns:
            New RequestBuilder instance
        """
        # TODO: Implement request builder creation
        pass
    
    @rate_limit_decorator(requests_per_minute=60)
    @cache_decorator(ttl_seconds=300)
    @retry_decorator(max_attempts=3)
    def get(self, endpoint: str, params: Dict[str, Any] = None, 
            headers: Dict[str, str] = None) -> APIResponse:
        """
        Make a GET request.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            headers: Additional headers
            
        Returns:
            API response
        """
        # TODO: Implement GET request
        pass
    
    @rate_limit_decorator(requests_per_minute=60)
    @retry_decorator(max_attempts=3)
    def post(self, endpoint: str, data: Dict[str, Any] = None, 
             headers: Dict[str, str] = None) -> APIResponse:
        """
        Make a POST request.
        
        Args:
            endpoint: API endpoint
            data: Request body data
            headers: Additional headers
            
        Returns:
            API response
        """
        # TODO: Implement POST request
        pass
    
    @rate_limit_decorator(requests_per_minute=60)
    @retry_decorator(max_attempts=3)
    def put(self, endpoint: str, data: Dict[str, Any] = None, 
            headers: Dict[str, str] = None) -> APIResponse:
        """
        Make a PUT request.
        
        Args:
            endpoint: API endpoint
            data: Request body data
            headers: Additional headers
            
        Returns:
            API response
        """
        # TODO: Implement PUT request
        pass
    
    @rate_limit_decorator(requests_per_minute=60)
    @retry_decorator(max_attempts=3)
    def delete(self, endpoint: str, headers: Dict[str, str] = None) -> APIResponse:
        """
        Make a DELETE request.
        
        Args:
            endpoint: API endpoint
            headers: Additional headers
            
        Returns:
            API response
        """
        # TODO: Implement DELETE request
        pass
    
    def _make_request(self, method: HTTPMethod, endpoint: str, 
                     params: Dict[str, Any] = None, data: Dict[str, Any] = None,
                     headers: Dict[str, str] = None) -> APIResponse:
        """
        Internal method to make HTTP requests.
        
        This method simulates HTTP requests since we don't want to add external dependencies.
        In a real implementation, this would use requests library or similar.
        """
        # TODO: Implement internal request method
        # - Build complete URL
        # - Add authentication headers
        # - Simulate HTTP request (for this exercise)
        # - Parse response
        # - Handle errors
        # - Return APIResponse object
        pass
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        # TODO: Implement cache statistics
        pass
    
    def clear_cache(self) -> None:
        """Clear the response cache."""
        # TODO: Implement cache clearing
        pass
    
    def get_rate_limit_info(self) -> RateLimitInfo:
        """Get current rate limit information."""
        # TODO: Implement rate limit info retrieval
        pass


class APIClientFactory:
    """Factory class for creating configured API clients."""
    
    @staticmethod
    def create_json_api_client(base_url: str, api_key: str = None) -> APIClient:
        """
        Create an API client configured for JSON APIs.
        
        Args:
            base_url: Base URL for the API
            api_key: Optional API key for authentication
            
        Returns:
            Configured API client
        """
        # TODO: Implement JSON API client creation
        # - Create client with appropriate headers
        # - Set up authentication if API key provided
        # - Configure for JSON responses
        pass
    
    @staticmethod
    def create_rest_api_client(base_url: str, token: str = None) -> APIClient:
        """
        Create an API client configured for REST APIs.
        
        Args:
            base_url: Base URL for the API
            token: Optional bearer token for authentication
            
        Returns:
            Configured API client
        """
        # TODO: Implement REST API client creation
        pass


def demonstrate_api_client():
    """Demonstrate the API client capabilities."""
    print("RESTful API Client Library Demonstration")
    print("=" * 50)
    
    # Create a mock API client
    client = APIClient("https://api.example.com")
    
    # Set up authentication
    auth = APIKeyAuthenticator("test-api-key-12345")
    client.set_authenticator(auth)
    
    print("Created API client with API key authentication")
    
    # Demonstrate fluent interface
    request_builder = (client.create_request()
                      .endpoint("/users")
                      .param("page", 1)
                      .param("limit", 10)
                      .header("Accept", "application/json"))
    
    print("Built request using fluent interface:")
    print(f"URL: {request_builder.build_url()}")
    
    # Simulate API calls
    print("\nSimulating API calls...")
    
    try:
        # GET request
        response = client.get("/users", params={"page": 1, "limit": 5})
        print(f"GET /users: Status {response.status_code}, Time: {response.response_time:.3f}s")
        
        # POST request
        user_data = {"name": "John Doe", "email": "john@example.com"}
        response = client.post("/users", data=user_data)
        print(f"POST /users: Status {response.status_code}, Time: {response.response_time:.3f}s")
        
        # Show cache and rate limit info
        print(f"\nCache stats: {client.get_cache_stats()}")
        rate_info = client.get_rate_limit_info()
        print(f"Rate limit: {rate_info.current_requests}/{rate_info.requests_per_minute} requests")
        
    except APIException as e:
        print(f"API Error: {e}")


def main():
    """Main function with menu-driven interface."""
    print("=== RESTful API Client Library ===")
    print("1. Run demonstration")
    print("2. Test authentication methods")
    print("3. Test request builder")
    print("4. Test caching and rate limiting")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            demonstrate_api_client()
            
        elif choice == "2":
            # TODO: Implement authentication testing
            print("Authentication testing not yet implemented")
            
        elif choice == "3":
            # TODO: Implement request builder testing
            print("Request builder testing not yet implemented")
            
        elif choice == "4":
            # TODO: Implement caching and rate limiting testing
            print("Caching and rate limiting testing not yet implemented")
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()