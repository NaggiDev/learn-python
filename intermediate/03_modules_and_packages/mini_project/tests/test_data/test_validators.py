"""Tests for data validation utilities."""

import pytest
from devtools.data.validators import (
    validate_email, validate_phone, validate_url, 
    is_valid_json, validate_password_strength
)

class TestValidateEmail:
    """Test validate_email function."""
    
    def test_valid_emails(self):
        """Test with valid email addresses."""
        valid_emails = [
            "user@example.com",
            "test.email@domain.org",
            "user+tag@example.co.uk",
            "123@example.com"
        ]
        for email in valid_emails:
            assert validate_email(email), f"Should be valid: {email}"
    
    def test_invalid_emails(self):
        """Test with invalid email addresses."""
        invalid_emails = [
            "invalid-email",
            "@example.com",
            "user@",
            "user@.com",
            "user space@example.com",
            ""
        ]
        for email in invalid_emails:
            assert not validate_email(email), f"Should be invalid: {email}"
    
    def test_non_string_input(self):
        """Test with non-string input."""
        assert not validate_email(123)
        assert not validate_email(None)
        assert not validate_email([])

class TestValidatePhone:
    """Test validate_phone function."""
    
    def test_valid_us_phones(self):
        """Test with valid US phone numbers."""
        valid_phones = [
            "(123) 456-7890",
            "123-456-7890",
            "1234567890",
            "1-123-456-7890",
            "+1-123-456-7890"
        ]
        for phone in valid_phones:
            assert validate_phone(phone), f"Should be valid: {phone}"
    
    def test_invalid_phones(self):
        """Test with invalid phone numbers."""
        invalid_phones = [
            "123",
            "123-456",
            "abc-def-ghij",
            ""
        ]
        for phone in invalid_phones:
            assert not validate_phone(phone), f"Should be invalid: {phone}"
    
    def test_non_string_input(self):
        """Test with non-string input."""
        assert not validate_phone(123)
        assert not validate_phone(None)

class TestValidateUrl:
    """Test validate_url function."""
    
    def test_valid_urls(self):
        """Test with valid URLs."""
        valid_urls = [
            "https://www.example.com",
            "http://example.com",
            "https://example.com/path",
            "http://subdomain.example.com"
        ]
        for url in valid_urls:
            assert validate_url(url), f"Should be valid: {url}"
    
    def test_invalid_urls(self):
        """Test with invalid URLs."""
        invalid_urls = [
            "not-a-url",
            "ftp://example.com",  # Not http/https
            "example.com",  # No scheme
            ""
        ]
        for url in invalid_urls:
            assert not validate_url(url), f"Should be invalid: {url}"

class TestIsValidJson:
    """Test is_valid_json function."""
    
    def test_valid_json(self):
        """Test with valid JSON strings."""
        valid_json = [
            '{"name": "John", "age": 30}',
            '[]',
            '{}',
            '"string"',
            '123',
            'true',
            'null'
        ]
        for json_str in valid_json:
            assert is_valid_json(json_str), f"Should be valid: {json_str}"
    
    def test_invalid_json(self):
        """Test with invalid JSON strings."""
        invalid_json = [
            "invalid json",
            "{'name': 'John'}",  # Single quotes
            "{name: 'John'}",  # Unquoted keys
            ""
        ]
        for json_str in invalid_json:
            assert not is_valid_json(json_str), f"Should be invalid: {json_str}"

class TestValidatePasswordStrength:
    """Test validate_password_strength function."""
    
    def test_strong_password(self):
        """Test with strong password."""
        result = validate_password_strength("MyPass123!")
        assert result['is_strong']
        assert result['score'] >= 4
    
    def test_weak_password(self):
        """Test with weak password."""
        result = validate_password_strength("weak")
        assert not result['is_strong']
        assert result['score'] < 4
        assert len(result['feedback']) > 1
    
    def test_password_criteria(self):
        """Test individual password criteria."""
        result = validate_password_strength("Password123!")
        assert result['has_upper']
        assert result['has_lower']
        assert result['has_digit']
        assert result['has_special']
        assert result['length'] >= 8