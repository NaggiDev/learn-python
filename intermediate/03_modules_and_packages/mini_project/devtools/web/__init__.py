"""
Web utilities.

This subpackage provides functions for web-related operations including
URL handling, HTTP requests, and JSON processing.
"""

from .urls import validate_url, parse_url, build_url, extract_domain
from .requests import make_request, download_file, check_url_status
from .json_utils import parse_json, format_json, validate_json_schema

__all__ = [
    # URL utilities
    'validate_url', 'parse_url', 'build_url', 'extract_domain',
    # Request utilities
    'make_request', 'download_file', 'check_url_status',
    # JSON utilities
    'parse_json', 'format_json', 'validate_json_schema'
]