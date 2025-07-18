"""
Patron class for the Library Management System

This module contains the Patron class that represents a library patron.
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
        # TODO: Implement input validation
        # - Check that patron_id, name, email are not empty
        # - Validate email format (simple check for @ symbol)
        # - Check that max_books is positive
        
        # TODO: Initialize instance attributes
        # Set all provided parameters as instance attributes
        # Set registration_date to today's date
        # Initialize checked_out_books as an empty list
        pass
    
    def can_checkout_book(self) -> bool:
        """
        Check if patron can check out another book.
        
        Returns:
            bool: True if patron can check out more books, False otherwise
        """
        # TODO: Implement this method
        # Check if the number of currently checked out books is less than max_books
        pass
    
    def checkout_book(self, book: Book) -> bool:
        """
        Add a book to the patron's checked out books.
        
        Args:
            book: The book to check out
            
        Returns:
            bool: True if successful, False if patron has reached limit or book already checked out
        """
        # TODO: Implement this method
        # - Check if patron can check out another book
        # - Check if the book is not already in checked_out_books
        # - If both checks pass, add book to checked_out_books and return True
        # - Otherwise, return False
        pass
    
    def return_book(self, book: Book) -> bool:
        """
        Remove a book from the patron's checked out books.
        
        Args:
            book: The book to return
            
        Returns:
            bool: True if successful, False if book was not checked out by this patron
        """
        # TODO: Implement this method
        # - Check if the book is in checked_out_books
        # - If yes, remove it and return True
        # - If no, return False
        pass
    
    def get_checked_out_books(self) -> List[Book]:
        """
        Get a copy of the list of currently checked out books.
        
        Returns:
            List[Book]: Copy of checked out books list
        """
        # TODO: Implement this method
        # Return a copy of the checked_out_books list (not the original list)
        pass
    
    def get_checkout_count(self) -> int:
        """
        Get the number of books currently checked out.
        
        Returns:
            int: Number of checked out books
        """
        # TODO: Implement this method
        # Return the length of checked_out_books list
        pass
    
    def get_info(self) -> dict:
        """
        Get a dictionary containing all patron information.
        
        Returns:
            dict: Dictionary containing patron details
        """
        # TODO: Implement this method
        # Return a dictionary with patron information
        # Include: patron_id, name, email, phone, registration_date, 
        #         checkout_count, max_books
        # Convert registration_date to string format
        pass
    
    def __str__(self) -> str:
        """
        Return a string representation of the patron.
        
        Returns:
            str: Formatted string with patron information
        """
        # TODO: Implement this method
        # Return a nicely formatted string showing patron details
        # Example: "Patron: John Doe (ID: P001) | Books: 2/5 | Email: john@email.com"
        pass
    
    def __eq__(self, other) -> bool:
        """
        Check if two patrons are equal (same patron_id).
        
        Args:
            other: Another Patron instance to compare with
            
        Returns:
            bool: True if patrons have the same patron_id, False otherwise
        """
        # TODO: Implement this method
        # Two patrons are equal if they have the same patron_id
        # Handle the case where 'other' is not a Patron instance
        pass
    
    def __hash__(self) -> int:
        """
        Return hash value for the patron (based on patron_id).
        
        Returns:
            int: Hash value
        """
        # TODO: Implement this method
        # Use patron_id to generate hash value
        pass