"""
Library class for the Library Management System

This module contains the main Library class that manages books, patrons, and checkouts.
"""

import json
from datetime import date, datetime
from typing import List, Dict, Optional, Tuple
from book import Book
from patron import Patron
from checkout_record import CheckoutRecord


class Library:
    """
    Main library management system class.
    
    Attributes:
        name (str): Name of the library
        books (Dict[str, Book]): Dictionary of books indexed by ISBN
        patrons (Dict[str, Patron]): Dictionary of patrons indexed by patron_id
        checkout_records (List[CheckoutRecord]): List of all checkout records
        data_file (str): Path to the data persistence file
    """
    
    def __init__(self, name: str = "Community Library", data_file: str = "library_data.json"):
        """
        Initialize a new Library instance.
        
        Args:
            name: Name of the library
            data_file: Path to file for data persistence
        """
        # TODO: Initialize instance attributes
        # - Set name and data_file
        # - Initialize books as empty dictionary
        # - Initialize patrons as empty dictionary  
        # - Initialize checkout_records as empty list
        pass
    
    def add_book(self, book: Book) -> bool:
        """
        Add a book to the library inventory.
        
        Args:
            book: Book instance to add
            
        Returns:
            bool: True if book was added, False if ISBN already exists
        """
        # TODO: Implement this method
        # - Check if book's ISBN already exists in books dictionary
        # - If not, add the book and return True
        # - If ISBN exists, return False
        pass
    
    def remove_book(self, isbn: str) -> bool:
        """
        Remove a book from the library inventory.
        
        Args:
            isbn: ISBN of the book to remove
            
        Returns:
            bool: True if book was removed, False if not found or currently checked out
        """
        # TODO: Implement this method
        # - Check if ISBN exists in books dictionary
        # - Check if book is currently available (not checked out)
        # - If both conditions met, remove book and return True
        # - Otherwise, return False
        pass
    
    def register_patron(self, patron: Patron) -> bool:
        """
        Register a new patron with the library.
        
        Args:
            patron: Patron instance to register
            
        Returns:
            bool: True if patron was registered, False if patron_id already exists
        """
        # TODO: Implement this method
        # - Check if patron's patron_id already exists
        # - If not, add patron and return True
        # - If exists, return False
        pass
    
    def search_books(self, query: str, search_type: str = "title") -> List[Book]:
        """
        Search for books by title, author, or ISBN.
        
        Args:
            query: Search query string
            search_type: Type of search ("title", "author", or "isbn")
            
        Returns:
            List[Book]: List of matching books
        """
        # TODO: Implement this method
        # - Convert query to lowercase for case-insensitive search
        # - Search through books based on search_type
        # - For title and author, use substring matching
        # - For ISBN, use exact matching
        # - Return list of matching Book objects
        pass
    
    def checkout_book(self, isbn: str, patron_id: str) -> Tuple[bool, str]:
        """
        Process a book checkout.
        
        Args:
            isbn: ISBN of book to checkout
            patron_id: ID of patron checking out book
            
        Returns:
            Tuple[bool, str]: (Success status, message)
        """
        # TODO: Implement this method
        # - Check if book exists and is available
        # - Check if patron exists and can checkout more books
        # - If all checks pass:
        #   - Mark book as checked out
        #   - Add book to patron's checked out list
        #   - Create and store checkout record
        #   - Return (True, success message)
        # - If any check fails, return (False, error message)
        pass
    
    def return_book(self, isbn: str, patron_id: str) -> Tuple[bool, str, float]:
        """
        Process a book return.
        
        Args:
            isbn: ISBN of book to return
            patron_id: ID of patron returning book
            
        Returns:
            Tuple[bool, str, float]: (Success status, message, fine amount)
        """
        # TODO: Implement this method
        # - Find the active checkout record for this book and patron
        # - If found:
        #   - Mark book as available
        #   - Remove book from patron's checked out list
        #   - Process return in checkout record (calculate fine)
        #   - Return (True, success message, fine amount)
        # - If not found, return (False, error message, 0.0)
        pass
    
    def get_overdue_books(self) -> List[CheckoutRecord]:
        """
        Get list of all overdue checkout records.
        
        Returns:
            List[CheckoutRecord]: List of overdue checkout records
        """
        # TODO: Implement this method
        # - Filter checkout_records for unreturned, overdue books
        # - Return list of overdue CheckoutRecord objects
        pass
    
    def get_patron_history(self, patron_id: str) -> List[CheckoutRecord]:
        """
        Get checkout history for a specific patron.
        
        Args:
            patron_id: ID of the patron
            
        Returns:
            List[CheckoutRecord]: List of checkout records for the patron
        """
        # TODO: Implement this method
        # - Filter checkout_records for the specified patron
        # - Return list of CheckoutRecord objects
        pass
    
    def generate_inventory_report(self) -> Dict:
        """
        Generate a report of library inventory.
        
        Returns:
            Dict: Dictionary containing inventory statistics
        """
        # TODO: Implement this method
        # Return a dictionary with:
        # - total_books: total number of books
        # - available_books: number of available books
        # - checked_out_books: number of checked out books
        # - total_patrons: number of registered patrons
        # - active_checkouts: number of current checkouts
        # - overdue_books: number of overdue books
        pass
    
    def save_data(self) -> bool:
        """
        Save library data to JSON file.
        
        Returns:
            bool: True if successful, False otherwise
        """
        # TODO: Implement this method
        # - Create a dictionary with all library data
        # - Convert objects to dictionaries using their get_info() methods
        # - Handle dates by converting to strings
        # - Save to JSON file specified in data_file
        # - Handle file I/O exceptions
        # - Return True if successful, False if error occurred
        pass
    
    def load_data(self) -> bool:
        """
        Load library data from JSON file.
        
        Returns:
            bool: True if successful, False otherwise
        """
        # TODO: Implement this method
        # - Try to load data from JSON file
        # - Recreate Book, Patron, and CheckoutRecord objects from dictionaries
        # - Handle date string conversion back to date objects
        # - Handle file not found and JSON parsing errors
        # - Return True if successful, False if error occurred
        pass
    
    def get_library_info(self) -> Dict:
        """
        Get general information about the library.
        
        Returns:
            Dict: Dictionary with library information
        """
        # TODO: Implement this method
        # Return dictionary with:
        # - name: library name
        # - total_books, total_patrons
        # - current_date: today's date as string
        pass
    
    def __str__(self) -> str:
        """
        Return string representation of the library.
        
        Returns:
            str: Formatted string with library information
        """
        # TODO: Implement this method
        # Return formatted string showing library name and basic statistics
        pass