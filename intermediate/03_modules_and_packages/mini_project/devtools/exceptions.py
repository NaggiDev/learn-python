"""Custom exceptions for the devtools package."""

class DevToolsError(Exception):
    """Base exception for devtools package."""
    pass

class ValidationError(DevToolsError):
    """Raised when data validation fails."""
    pass

class ProcessingError(DevToolsError):
    """Raised when data processing fails."""
    pass

class SystemError(DevToolsError):
    """Raised when system operations fail."""
    pass

class WebError(DevToolsError):
    """Raised when web operations fail."""
    pass