"""
Patron class for the Library Management System - Reference Solution

This module contains the complete implementation of the Patron class.
"""

from datetime import datetime, date
from typing import List, Optional
from book import Book


class Patron:
    """
    Represents a library patron.
    
    Attributes:
        patron_id (str): Unique identifier for the patron
        name (str): Full name of the patron
        email (str): Email address of the patron
        phone (str): Phone number of the patron
        registration_date (date): Date when patron registered
        checked_out_books (List[Book]): List of currently checked out books
        max_books (int): Maximum number of books patron can check out
    """
    
    def __init__(self, patron_id: str, name: str, email: str, 
                 phone: str, max_books: int = 5):
        """
        Initialize a new Patron instance.
        
        Args:
            patron_id: Unique identifier for the patron
            name: Full name of the patron
            email: Email address of the patron
            phone: Phone number of the patron
            max_books: Maximum books patron can check out (default: 5)
            
        Raises:
            ValueError: If any required field is empty or invalid
        """
        # Input validation
        if not patron_id or not patron_id.strip():
            raise ValueError("Patron ID cannot be empty")
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if not email or not email.strip():
            raise ValueError("Email cannot be empty")
        if '@' not in email:
            raise ValueError("Email must contain @ symbol")
        if max_books <= 0:
            raise ValueError("Maximum books must be positive")
        
        # Initialize instance attributes
        self.patron_id = patron_id.strip()
        self.name = name.strip()
        self.email = email.strip()
        self.phone = phone.strip() if phone else ""
        self.max_books = max_books
        self.registration_date = date.today()
        self.checked_out_books = []
    
    def can_checkout_book(self) -> bool:
        """
        Check if patron can check out another book.
        
        Returns:
            bool: True if patron can check out more books, False otherwise
        """
        return len(self.checked_out_books) < self.max_books
    
    def checkout_book(self, book: Book) -> bool:
        """
        Add a book to the patron's checked out books.
        
        Args:
            book: The book to check out
            
        Returns:
            bool: True if successful, False if patron has reached limit or book already checked out
        """
        if not self.can_checkout_book():
            return False
        
        if book in self.checked_out_books:
            return False
        
        self.checked_out_books.append(book)
        return True
    
    def return_book(self, book: Book) -> bool:
        """
        Remove a book from the patron's checked out books.
        
        Args:
            book: The book to return
            
        Returns:
            bool: True if successful, False if book was not checked out by this patron
        """
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)
            return True
        return False
    
    def get_checked_out_books(self) -> List[Book]:
        """
        Get a copy of the list of currently checked out books.
        
        Returns:
            List[Book]: Copy of checked out books list
        """
        return self.checked_out_books.copy()
    
    def get_checkout_count(self) -> int:
        """
        Get the number of books currently checked out.
        
        Returns:
            int: Number of checked out books
        """
        return len(self.checked_out_books)
    
    def get_info(self) -> dict:
        """
        Get a dictionary containing all patron information.
        
        Returns:
            dict: Dictionary containing patron details
        """
        return {
            'patron_id': self.patron_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'registration_date': self.registration_date.isoformat(),
            'checkout_count': self.get_checkout_count(),
            'max_books': self.max_books
        }
    
    def __str__(self) -> str:
        """
        Return a string representation of the patron.
        
        Returns:
            str: Formatted string with patron information
        """
        return f"Patron: {self.name} (ID: {self.patron_id}) | Books: {self.get_checkout_count()}/{self.max_books} | Email: {self.email}"
    
    def __eq__(self, other) -> bool:
        """
        Check if two patrons are equal (same patron_id).
        
        Args:
            other: Another Patron instance to compare with
            
        Returns:
            bool: True if patrons have the same patron_id, False otherwise
        """
        if not isinstance(other, Patron):
            return False
        return self.patron_id == other.patron_id
    
    def __hash__(self) -> int:
        """
        Return hash value for the patron (based on patron_id).
        
        Returns:
            int: Hash value
        """
        return hash(self.patron_id)