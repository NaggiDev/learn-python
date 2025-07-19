"""
Solution: Code Quality Tools Practice

This file contains the cleaned-up version of the code quality exercise,
with all style violations and issues fixed.

The original file had the following types of issues:
- Import sorting and organization
- PEP 8 style violations
- Security vulnerabilities
- Poor naming conventions
- Missing type annotations
- Overly complex functions
- Poor error handling
- Unused variables and imports
"""

import json
import os
import sys
from collections import defaultdict
from typing import Dict, List, Optional, Any

import requests


# Constants with proper naming
MAX_RETRIES = 5
DEFAULT_USER = "admin"

# Note: Removed hardcoded password - should be loaded from environment
# PASSWORD = os.getenv("APP_PASSWORD", "")


def calculate_user_score(
    user_data: Optional[Dict[str, Any]],
    bonus_points: int = 0,
    penalty_points: int = 0,
) -> float:
    """
    Calculate user score with bonus and penalty points.
    
    Args:
        user_data: Dictionary containing user score data
        bonus_points: Additional points to add
        penalty_points: Points to subtract
        
    Returns:
        Calculated total score
    """
    if user_data is None:
        return 0.0
    
    base_score = user_data.get("base_score", 0)
    
    # Calculate total score with proper error handling
    try:
        total_score = (base_score + bonus_points - penalty_points) * 1.5
    except (TypeError, ValueError):
        total_score = 0.0
    
    return max(0.0, total_score)  # Ensure non-negative score


class UserAccount:
    """Represents a user account with basic operations."""
    
    def __init__(self, username: str, email: str, age: int) -> None:
        """
        Initialize user account.
        
        Args:
            username: User's username
            email: User's email address
            age: User's age
        """
        self.username = username
        self.email = email
        self.age = age
        self._balance = 0.0
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            
        Returns:
            True if deposit successful, False otherwise
        """
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def authenticate(self, password: str) -> bool:
        """
        Authenticate user with password.
        
        Args:
            password: Password to check
            
        Returns:
            True if authentication successful
            
        Note:
            In production, use proper password hashing and comparison
        """
        # Use secure password comparison in production
        stored_password = os.getenv("USER_PASSWORD", "")
        return password == stored_password
    
    def get_user_info(self) -> Dict[str, Any]:
        """
        Get user information dictionary.
        
        Returns:
            Dictionary containing user information
        """
        return {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "balance": self._balance
        }


def get_user_by_id(user_id: int) -> str:
    """
    Get user from database by ID using parameterized query.
    
    Args:
        user_id: User ID to search for
        
    Returns:
        SQL query string (parameterized)
        
    Note:
        In production, use proper ORM or parameterized queries
    """
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE id = %s"
    # In real application, execute with: cursor.execute(query, (user_id,))
    return query


def process_api_data(
    url: str, 
    headers: Optional[Dict[str, str]] = None
) -> List[Dict[str, Any]]:
    """
    Process data from API endpoint.
    
    Args:
        url: API endpoint URL
        headers: Optional HTTP headers
        
    Returns:
        List of active items from API response
        
    Raises:
        requests.RequestException: If API request fails
        ValueError: If response is not valid JSON
    """
    if headers is None:
        headers = {}
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Filter active items
        active_items = [
            item for item in data 
            if isinstance(item, dict) and item.get('status') == 'active'
        ]
        
        return active_items
        
    except requests.RequestException as e:
        raise requests.RequestException(f"API request failed: {e}") from e
    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError(f"Invalid JSON response: {e}") from e


def calculate_weighted_average(
    data: List[float],
    weights: Optional[List[float]] = None,
    apply_bonus: bool = True,
    bonus_multiplier: float = 1.0
) -> float:
    """
    Calculate weighted average with optional bonus.
    
    Args:
        data: List of numeric values
        weights: Optional weights for each value
        apply_bonus: Whether to apply bonus multiplier
        bonus_multiplier: Multiplier for bonus calculation
        
    Returns:
        Calculated weighted average
        
    Raises:
        ValueError: If data is empty or weights don't match data length
    """
    if not data:
        raise ValueError("Data list cannot be empty")
    
    if weights is None:
        weights = [1.0] * len(data)
    
    if len(data) != len(weights):
        raise ValueError("Data and weights must have the same length")
    
    weighted_sum = sum(value * weight for value, weight in zip(data, weights))
    total_weight = sum(weights)
    
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    
    average = weighted_sum / total_weight
    
    if apply_bonus:
        average *= bonus_multiplier
    
    return average


def merge_dictionaries(
    dict1: Dict[str, Any], 
    dict2: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Merge two dictionaries, with dict2 values taking precedence.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary
        
    Returns:
        Merged dictionary
    """
    result = dict1.copy()
    result.update(dict2)
    return result


def safe_execute_code(code_string: str, allowed_names: Optional[List[str]] = None) -> Any:
    """
    Safely execute user code with restricted namespace.
    
    Args:
        code_string: Code to execute
        allowed_names: List of allowed variable/function names
        
    Returns:
        Result of code execution
        
    Raises:
        ValueError: If code contains disallowed operations
        
    Note:
        This is still not completely safe - use proper sandboxing in production
    """
    if allowed_names is None:
        allowed_names = ['abs', 'len', 'max', 'min', 'sum']
    
    # Basic safety checks
    dangerous_keywords = ['import', 'exec', 'eval', 'open', '__']
    if any(keyword in code_string for keyword in dangerous_keywords):
        raise ValueError("Code contains potentially dangerous operations")
    
    # Create restricted namespace
    safe_namespace = {name: globals().get(name) for name in allowed_names}
    
    try:
        # Use compile and exec instead of eval for better control
        compiled_code = compile(code_string, '<string>', 'eval')
        return eval(compiled_code, {"__builtins__": {}}, safe_namespace)
    except Exception as e:
        raise ValueError(f"Code execution failed: {e}") from e


def is_truthy(value: Any) -> bool:
    """
    Check if a value is truthy.
    
    Args:
        value: Value to check
        
    Returns:
        True if value is truthy, False otherwise
    """
    return bool(value)


class DataProcessor:
    """Processes and stores data with various operations."""
    
    def __init__(self, data: List[Any]) -> None:
        """
        Initialize data processor.
        
        Args:
            data: Initial data to process
        """
        self._data = data
        self._processed_count = 0
    
    def process_data(self) -> List[Any]:
        """
        Process the stored data.
        
        Returns:
            Processed data
        """
        processed = [item for item in self._data if item is not None]
        self._processed_count = len(processed)
        return processed
    
    def get_statistics(self) -> Dict[str, int]:
        """
        Get processing statistics.
        
        Returns:
            Dictionary with processing statistics
        """
        return {
            'total_items': len(self._data),
            'processed_items': self._processed_count
        }
    
    def reset(self) -> None:
        """Reset the processor state."""
        self._data.clear()
        self._processed_count = 0


def process_numeric_data() -> float:
    """
    Process numeric data and return sum.
    
    Returns:
        Sum of processed data
    """
    data = [1, 2, 3, 4, 5]
    return sum(data)


def add_to_list(item: Any, target_list: Optional[List[Any]] = None) -> List[Any]:
    """
    Add item to list (safe version with no mutable default argument).
    
    Args:
        item: Item to add
        target_list: Optional target list
        
    Returns:
        List with item added
    """
    if target_list is None:
        target_list = []
    
    result = target_list.copy()  # Don't modify original list
    result.append(item)
    return result


def get_value(key: str, data: Dict[str, Any]) -> Optional[Any]:
    """
    Get value from dictionary.
    
    Args:
        key: Key to look up
        data: Dictionary to search
        
    Returns:
        Value if key exists, None otherwise
    """
    return data.get(key)


def main() -> None:
    """Main function demonstrating the cleaned-up code."""
    print("Starting application...")
    
    # Create user account
    user = UserAccount("john_doe", "john@example.com", 25)
    
    # Calculate score
    user_data = {"base_score": 100}
    score = calculate_user_score(user_data, 10, 5)
    
    print(f"User score: {score}")
    
    # Process numeric data
    numeric_result = process_numeric_data()
    print(f"Numeric processing result: {numeric_result}")
    
    # Demonstrate safe list operations
    my_list = add_to_list("item1")
    my_list = add_to_list("item2", my_list)
    print(f"List contents: {my_list}")
    
    print("Application finished.")


if __name__ == "__main__":
    main()