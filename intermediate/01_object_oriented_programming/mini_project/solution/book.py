"""
Book class for the Library Management System - Reference Solution

This module contains the complete implementation of the Book class.
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
        # Input validation
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if not author or not author.strip():
            raise ValueError("Author cannot be empty")
        if not isbn or not isbn.strip():
            raise ValueError("ISBN cannot be empty")
        if len(isbn.strip()) < 10:
            raise ValueError("ISBN must be at least 10 characters long")
        
        current_year = datetime.now().year
        if publication_year > current_year:
            raise ValueError(f"Publication year cannot be in the future (current year: {current_year})")
        if publication_year < 1000:
            raise ValueError("Publication year must be a valid 4-digit year")
        
        # Initialize instance attributes
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.publication_year = publication_year
        self.genre = genre.strip() if genre else "General"
        self.is_available = True
    
    def mark_as_checked_out(self) -> bool:
        """
        Mark the book as checked out (not available).
        
        Returns:
            bool: True if successfully marked as checked out, False if already checked out
        """
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def mark_as_available(self) -> bool:
        """
        Mark the book as available for checkout.
        
        Returns:
            bool: True if successfully marked as available, False if already available
        """
        if not self.is_available:
            self.is_available = True
            return True
        return False
    
    def get_info(self) -> dict:
        """
        Get a dictionary containing all book information.
        
        Returns:
            dict: Dictionary containing book details
        """
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'publication_year': self.publication_year,
            'genre': self.genre,
            'is_available': self.is_available
        }
    
    def __str__(self) -> str:
        """
        Return a string representation of the book.
        
        Returns:
            str: Formatted string with book information
        """
        availability = "Available" if self.is_available else "Checked Out"
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | {availability}"
    
    def __eq__(self, other) -> bool:
        """
        Check if two books are equal (same ISBN).
        
        Args:
            other: Another Book instance to compare with
            
        Returns:
            bool: True if books have the same ISBN, False otherwise
        """
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn
    
    def __hash__(self) -> int:
        """
        Return hash value for the book (based on ISBN).
        
        Returns:
            int: Hash value
        """
        return hash(self.isbn)