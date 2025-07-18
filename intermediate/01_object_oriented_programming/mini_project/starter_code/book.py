"""
Book class for the Library Management System

This module contains the Book class that represents a book in the library.
"""

from datetime import datetime
from typing import Optional


class Book:
    """
    Represents a book in the library system.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        isbn (str): The ISBN of the book
        publication_year (int): The year the book was published
        genre (str): The genre of the book
        is_available (bool): Whether the book is currently available for checkout
    """
    
    def __init__(self, title: str, author: str, isbn: str, 
                 publication_year: int, genre: str = "General"):
        """
        Initialize a new Book instance.
        
        Args:
            title: The title of the book
            author: The author of the book
            isbn: The ISBN of the book (should be unique)
            publication_year: The year the book was published
            genre: The genre of the book (default: "General")
        
        Raises:
            ValueError: If any required field is empty or invalid
        """
        # TODO: Implement input validation
        # - Check that title, author, and isbn are not empty
        # - Check that publication_year is a valid year (not in the future)
        # - Check that isbn follows a valid format (you can use a simple length check)
        
        # TODO: Initialize instance attributes
        # Set all the provided parameters as instance attributes
        # Set is_available to True by default
        pass
    
    def mark_as_checked_out(self) -> bool:
        """
        Mark the book as checked out (not available).
        
        Returns:
            bool: True if successfully marked as checked out, False if already checked out
        """
        # TODO: Implement this method
        # - Check if the book is currently available
        # - If available, mark as not available and return True
        # - If not available, return False
        pass
    
    def mark_as_available(self) -> bool:
        """
        Mark the book as available for checkout.
        
        Returns:
            bool: True if successfully marked as available, False if already available
        """
        # TODO: Implement this method
        # - Check if the book is currently not available
        # - If not available, mark as available and return True
        # - If already available, return False
        pass
    
    def get_info(self) -> dict:
        """
        Get a dictionary containing all book information.
        
        Returns:
            dict: Dictionary containing book details
        """
        # TODO: Implement this method
        # Return a dictionary with all book attributes
        # Include: title, author, isbn, publication_year, genre, is_available
        pass
    
    def __str__(self) -> str:
        """
        Return a string representation of the book.
        
        Returns:
            str: Formatted string with book information
        """
        # TODO: Implement this method
        # Return a nicely formatted string showing book details
        # Example: "Title: Python Programming | Author: John Doe | Available: Yes"
        pass
    
    def __eq__(self, other) -> bool:
        """
        Check if two books are equal (same ISBN).
        
        Args:
            other: Another Book instance to compare with
            
        Returns:
            bool: True if books have the same ISBN, False otherwise
        """
        # TODO: Implement this method
        # Two books are considered equal if they have the same ISBN
        # Make sure to handle the case where 'other' is not a Book instance
        pass
    
    def __hash__(self) -> int:
        """
        Return hash value for the book (based on ISBN).
        
        Returns:
            int: Hash value
        """
        # TODO: Implement this method
        # Use the ISBN to generate a hash value
        # This allows Book objects to be used in sets and as dictionary keys
        pass