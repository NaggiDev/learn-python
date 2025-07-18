"""
CheckoutRecord class for the Library Management System

This module contains the CheckoutRecord class that tracks book checkouts.
"""

from datetime import datetime, date, timedelta
from typing import Optional
from book import Book
from patron import Patron


class CheckoutRecord:
    """
    Represents a record of a book checkout transaction.
    
    Attributes:
        book (Book): The book that was checked out
        patron (Patron): The patron who checked out the book
        checkout_date (date): Date when book was checked out
        due_date (date): Date when book is due to be returned
        return_date (Optional[date]): Date when book was actually returned (None if not returned)
        fine_amount (float): Fine amount for overdue book
    """
    
    # Class constants
    LOAN_PERIOD_DAYS = 14  # Standard loan period
    DAILY_FINE_RATE = 0.50  # Fine per day for overdue books
    
    def __init__(self, book: Book, patron: Patron, 
                 checkout_date: Optional[date] = None):
        """
        Initialize a new CheckoutRecord.
        
        Args:
            book: The book being checked out
            patron: The patron checking out the book
            checkout_date: Date of checkout (default: today)
        """
        # TODO: Implement initialization
        # - Set book and patron attributes
        # - Set checkout_date (use today's date if not provided)
        # - Calculate due_date (checkout_date + LOAN_PERIOD_DAYS)
        # - Set return_date to None
        # - Set fine_amount to 0.0
        pass
    
    def is_overdue(self, check_date: Optional[date] = None) -> bool:
        """
        Check if the book is overdue.
        
        Args:
            check_date: Date to check against (default: today)
            
        Returns:
            bool: True if book is overdue and not returned, False otherwise
        """
        # TODO: Implement this method
        # - Use today's date if check_date is not provided
        # - Return True if book is not returned and check_date > due_date
        # - Return False otherwise
        pass
    
    def days_overdue(self, check_date: Optional[date] = None) -> int:
        """
        Calculate number of days the book is overdue.
        
        Args:
            check_date: Date to check against (default: today)
            
        Returns:
            int: Number of days overdue (0 if not overdue)
        """
        # TODO: Implement this method
        # - Use today's date if check_date is not provided
        # - If book is returned, return 0
        # - If not overdue, return 0
        # - Otherwise, return the number of days past due_date
        pass
    
    def calculate_fine(self, check_date: Optional[date] = None) -> float:
        """
        Calculate the fine amount for an overdue book.
        
        Args:
            check_date: Date to calculate fine for (default: today)
            
        Returns:
            float: Fine amount
        """
        # TODO: Implement this method
        # - Calculate days overdue
        # - Multiply by DAILY_FINE_RATE
        # - Return the fine amount (minimum 0.0)
        pass
    
    def return_book(self, return_date: Optional[date] = None) -> float:
        """
        Mark the book as returned and calculate final fine.
        
        Args:
            return_date: Date book was returned (default: today)
            
        Returns:
            float: Final fine amount
            
        Raises:
            ValueError: If book is already returned
        """
        # TODO: Implement this method
        # - Check if book is already returned (return_date is not None)
        # - If already returned, raise ValueError
        # - Set return_date (use today if not provided)
        # - Calculate and set fine_amount
        # - Return the fine amount
        pass
    
    def is_returned(self) -> bool:
        """
        Check if the book has been returned.
        
        Returns:
            bool: True if book has been returned, False otherwise
        """
        # TODO: Implement this method
        # Return True if return_date is not None
        pass
    
    def get_info(self) -> dict:
        """
        Get a dictionary containing all checkout record information.
        
        Returns:
            dict: Dictionary containing checkout record details
        """
        # TODO: Implement this method
        # Return a dictionary with all relevant information:
        # - book_title, book_isbn
        # - patron_name, patron_id
        # - checkout_date, due_date, return_date (as strings)
        # - is_overdue, days_overdue, fine_amount
        pass
    
    def __str__(self) -> str:
        """
        Return a string representation of the checkout record.
        
        Returns:
            str: Formatted string with checkout record information
        """
        # TODO: Implement this method
        # Return a formatted string showing:
        # - Book title and patron name
        # - Checkout and due dates
        # - Return status and any fine information
        pass
    
    def __eq__(self, other) -> bool:
        """
        Check if two checkout records are equal.
        
        Args:
            other: Another CheckoutRecord to compare with
            
        Returns:
            bool: True if records have same book, patron, and checkout_date
        """
        # TODO: Implement this method
        # Two records are equal if they have the same book, patron, and checkout_date
        # Handle case where 'other' is not a CheckoutRecord
        pass