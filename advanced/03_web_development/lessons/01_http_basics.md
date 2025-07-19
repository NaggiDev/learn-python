# HTTP Basics: Understanding the Web's Foundation

## Introduction

HTTP (HyperText Transfer Protocol) is the foundation of data communication on the World Wide Web. As a Python web developer, understanding HTTP is crucial for building effective web applications and APIs. This lesson covers the essential concepts you need to know about HTTP.

## What is HTTP?

HTTP is an application-layer protocol that defines how messages are formatted and transmitted between web clients (like browsers) and web servers. It follows a simple request-response model:

1. **Client** sends an HTTP request to a server
2. **Server** processes the request and sends back an HTTP response
3. **Client** receives and processes the response

## HTTP Methods (Verbs)

HTTP defines several methods that indicate the desired action to be performed:

### GET
- **Purpose**: Retrieve data from the server
- **Characteristics**: Safe, idempotent, cacheable
- **Example**: Getting a web page, fetching user information

```python
import requests

# GET request example
response = requests.get('https://api.github.com/users/octocat')
print(response.status_code)  # 200
print(response.json())       # User data
```

### POST
- **Purpose**: Submit data to be processed by the server
- **Characteristics**: Not safe, not idempotent
- **Example**: Creating a new user, submitting a form

```python
# POST request example
data = {'name': 'John Doe', 'email': 'john@example.com'}
response = requests.post('https://api.example.com/users', json=data)
print(response.status_code)  # 201 (Created)
```

### PUT
- **Purpose**: Update or create a resource
- **Characteristics**: Idempotent
- **Example**: Updating user profile, replacing a document

```python
# PUT request example
updated_data = {'name': 'John Smith', 'email': 'johnsmith@example.com'}
response = requests.put('https://api.example.com/users/123', json=updated_data)
print(response.status_code)  # 200 (OK) or 204 (No Content)
```

### DELETE
- **Purpose**: Remove a resource from the server
- **Characteristics**: Idempotent
- **Example**: Deleting a user account, removing a file

```python
# DELETE request example
response = requests.delete('https://api.example.com/users/123')
print(response.status_code)  # 204 (No Content)
```

### PATCH
- **Purpose**: Partially update a resource
- **Characteristics**: Not necessarily idempotent
- **Example**: Updating only the email field of a user

```python
# PATCH request example
partial_data = {'email': 'newemail@example.com'}
response = requests.patch('https://api.example.com/users/123', json=partial_data)
print(response.status_code)  # 200 (OK)
```

## HTTP Status Codes

Status codes indicate the result of the HTTP request:

### 1xx - Informational
- **100 Continue**: Server received request headers, client should send body
- **101 Switching Protocols**: Server is switching protocols

### 2xx - Success
- **200 OK**: Request successful
- **201 Created**: Resource successfully created
- **204 No Content**: Request successful, no content to return
- **206 Partial Content**: Partial content delivered

### 3xx - Redirection
- **301 Moved Permanently**: Resource permanently moved
- **302 Found**: Resource temporarily moved
- **304 Not Modified**: Resource not modified since last request

### 4xx - Client Error
- **400 Bad Request**: Invalid request syntax
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Server understood but refuses to authorize
- **404 Not Found**: Resource not found
- **405 Method Not Allowed**: HTTP method not supported
- **422 Unprocessable Entity**: Request well-formed but semantically incorrect

### 5xx - Server Error
- **500 Internal Server Error**: Generic server error
- **502 Bad Gateway**: Invalid response from upstream server
- **503 Service Unavailable**: Server temporarily unavailable
- **504 Gateway Timeout**: Upstream server timeout

## HTTP Headers

Headers provide additional information about the request or response:

### Common Request Headers
```python
headers = {
    'Content-Type': 'application/json',      # Type of data being sent
    'Accept': 'application/json',            # Type of data client expects
    'Authorization': 'Bearer token123',      # Authentication credentials
    'User-Agent': 'MyApp/1.0',              # Client application info
    'Accept-Language': 'en-US,en;q=0.9'     # Preferred languages
}

response = requests.get('https://api.example.com/data', headers=headers)
```

### Common Response Headers
```python
# Examining response headers
response = requests.get('https://api.example.com/data')
print(response.headers['Content-Type'])      # application/json
print(response.headers['Content-Length'])    # Size of response body
print(response.headers['Cache-Control'])     # Caching directives
print(response.headers['Set-Cookie'])        # Cookie information
```

## Request and Response Bodies

### JSON Data
Most modern APIs use JSON for data exchange:

```python
# Sending JSON data
data = {
    'username': 'johndoe',
    'email': 'john@example.com',
    'age': 30
}

response = requests.post('https://api.example.com/users', json=data)

# Receiving JSON data
if response.status_code == 200:
    user_data = response.json()
    print(f"Created user: {user_data['username']}")
```

### Form Data
Traditional web forms send data as form-encoded:

```python
# Sending form data
form_data = {
    'username': 'johndoe',
    'password': 'secretpassword'
}

response = requests.post('https://example.com/login', data=form_data)
```

### File Uploads
Uploading files requires multipart/form-data:

```python
# File upload
files = {'file': open('document.pdf', 'rb')}
response = requests.post('https://api.example.com/upload', files=files)
files['file'].close()
```

## URL Structure

Understanding URL components is essential:

```
https://api.example.com:443/v1/users/123?include=profile&format=json#section1
│     │ │              │   │  │        │                              │
│     │ │              │   │  │        └── Query parameters           │
│     │ │              │   │  └── Path                                 │
│     │ │              │   └── Port (optional)                        │
│     │ │              └── Host                                        │
│     │ └── Subdomain                                                  │
│     └── Protocol                                                     │
└── Fragment (client-side)
```

## HTTP Sessions and Cookies

### Sessions
Sessions maintain state across multiple requests:

```python
# Using sessions for persistent connections
session = requests.Session()
session.headers.update({'Authorization': 'Bearer token123'})

# All requests in this session will include the authorization header
response1 = session.get('https://api.example.com/profile')
response2 = session.get('https://api.example.com/settings')

session.close()
```

### Cookies
Cookies store small pieces of data on the client:

```python
# Working with cookies
response = requests.get('https://example.com/login')
print(response.cookies)  # View cookies set by server

# Sending cookies with requests
cookies = {'session_id': 'abc123', 'user_pref': 'dark_mode'}
response = requests.get('https://example.com/dashboard', cookies=cookies)
```

## Content Types and Encoding

### Common Content Types
- `application/json` - JSON data
- `application/x-www-form-urlencoded` - Form data
- `multipart/form-data` - File uploads
- `text/html` - HTML content
- `text/plain` - Plain text
- `application/xml` - XML data

### Character Encoding
```python
# Handling different encodings
response = requests.get('https://example.com/data')
print(response.encoding)  # utf-8
print(response.text)      # Decoded text
print(response.content)   # Raw bytes
```

## Error Handling

Proper error handling is crucial for robust applications:

```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def make_safe_request(url, method='GET', **kwargs):
    try:
        response = requests.request(method, url, timeout=10, **kwargs)
        response.raise_for_status()  # Raises HTTPError for bad status codes
        return response
    except Timeout:
        print(f"Request to {url} timed out")
    except ConnectionError:
        print(f"Failed to connect to {url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except RequestException as e:
        print(f"Request failed: {e}")
    return None

# Usage
response = make_safe_request('https://api.example.com/data')
if response:
    data = response.json()
```

## Best Practices

### 1. Use Appropriate HTTP Methods
- Use GET for retrieving data
- Use POST for creating resources
- Use PUT for full updates
- Use PATCH for partial updates
- Use DELETE for removing resources

### 2. Handle Status Codes Properly
```python
response = requests.post('https://api.example.com/users', json=user_data)

if response.status_code == 201:
    print("User created successfully")
elif response.status_code == 400:
    print("Bad request - check your data")
elif response.status_code == 409:
    print("User already exists")
else:
    print(f"Unexpected status code: {response.status_code}")
```

### 3. Set Appropriate Headers
```python
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'MyApp/1.0'
}
```

### 4. Use Sessions for Multiple Requests
```python
with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer token'})
    # Make multiple requests with shared configuration
```

### 5. Implement Proper Timeout
```python
# Always set timeouts to prevent hanging requests
response = requests.get('https://api.example.com/data', timeout=10)
```

## Security Considerations

### 1. HTTPS vs HTTP
- Always use HTTPS in production
- HTTPS encrypts data in transit
- Protects against man-in-the-middle attacks

### 2. Authentication
```python
# Bearer token authentication
headers = {'Authorization': 'Bearer your-token-here'}
response = requests.get('https://api.example.com/protected', headers=headers)

# Basic authentication
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.example.com/protected', 
                       auth=HTTPBasicAuth('username', 'password'))
```

### 3. Input Validation
- Always validate and sanitize user input
- Use parameterized queries for database operations
- Implement rate limiting to prevent abuse

## Debugging HTTP Requests

### Using Python's logging
```python
import logging
import requests

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

response = requests.get('https://api.example.com/data')
```

### Inspecting Requests and Responses
```python
response = requests.get('https://api.example.com/data')

# Request information
print(f"Request URL: {response.request.url}")
print(f"Request Headers: {response.request.headers}")
print(f"Request Body: {response.request.body}")

# Response information
print(f"Status Code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Response Body: {response.text}")
```

## Summary

HTTP is the backbone of web communication. Key takeaways:

1. **HTTP Methods** define the action to be performed
2. **Status Codes** indicate the result of the request
3. **Headers** provide metadata about requests and responses
4. **Proper error handling** is essential for robust applications
5. **Security considerations** should always be implemented
6. **Sessions and cookies** help maintain state across requests

Understanding these concepts will help you build better web applications and debug issues more effectively.

## Next Steps

In the next lesson, we'll explore the Flask web framework and learn how to build web applications that handle HTTP requests and responses.