"""
CheckoutRecord class for the Library Management System - Reference Solution

This module contains the complete implementation of the CheckoutRecord class.
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
        self.book = book
        self.patron = patron
        self.checkout_date = checkout_date if checkout_date else date.today()
        self.due_date = self.checkout_date + timedelta(days=self.LOAN_PERIOD_DAYS)
        self.return_date = None
        self.fine_amount = 0.0
    
    def is_overdue(self, check_date: Optional[date] = None) -> bool:
        """
        Check if the book is overdue.
        
        Args:
            check_date: Date to check against (default: today)
            
        Returns:
            bool: True if book is overdue and not returned, False otherwise
        """
        if self.return_date is not None:
            return False  # Book has been returned
        
        check_date = check_date if check_date else date.today()
        return check_date > self.due_date
    
    def days_overdue(self, check_date: Optional[date] = None) -> int:
        """
        Calculate number of days the book is overdue.
        
        Args:
            check_date: Date to check against (default: today)
            
        Returns:
            int: Number of days overdue (0 if not overdue)
        """
        if self.return_date is not None:
            return 0  # Book has been returned
        
        check_date = check_date if check_date else date.today()
        
        if check_date <= self.due_date:
            return 0  # Not overdue
        
        return (check_date - self.due_date).days
    
    def calculate_fine(self, check_date: Optional[date] = None) -> float:
        """
        Calculate the fine amount for an overdue book.
        
        Args:
            check_date: Date to calculate fine for (default: today)
            
        Returns:
            float: Fine amount
        """
        days_overdue = self.days_overdue(check_date)
        return max(0.0, days_overdue * self.DAILY_FINE_RATE)
    
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
        if self.return_date is not None:
            raise ValueError("Book has already been returned")
        
        self.return_date = return_date if return_date else date.today()
        self.fine_amount = self.calculate_fine(self.return_date)
        return self.fine_amount
    
    def is_returned(self) -> bool:
        """
        Check if the book has been returned.
        
        Returns:
            bool: True if book has been returned, False otherwise
        """
        return self.return_date is not None
    
    def get_info(self) -> dict:
        """
        Get a dictionary containing all checkout record information.
        
        Returns:
            dict: Dictionary containing checkout record details
        """
        return {
            'book_title': self.book.title,
            'book_isbn': self.book.isbn,
            'patron_name': self.patron.name,
            'patron_id': self.patron.patron_id,
            'checkout_date': self.checkout_date.isoformat(),
            'due_date': self.due_date.isoformat(),
            'return_date': self.return_date.isoformat() if self.return_date else None,
            'is_overdue': self.is_overdue(),
            'days_overdue': self.days_overdue(),
            'fine_amount': self.fine_amount
        }
    
    def __str__(self) -> str:
        """
        Return a string representation of the checkout record.
        
        Returns:
            str: Formatted string with checkout record information
        """
        status = "Returned" if self.is_returned() else ("Overdue" if self.is_overdue() else "Active")
        fine_info = f" | Fine: ${self.fine_amount:.2f}" if self.fine_amount > 0 else ""
        
        return (f"'{self.book.title}' checked out by {self.patron.name} "
                f"on {self.checkout_date} (Due: {self.due_date}) | Status: {status}{fine_info}")
    
    def __eq__(self, other) -> bool:
        """
        Check if two checkout records are equal.
        
        Args:
            other: Another CheckoutRecord to compare with
            
        Returns:
            bool: True if records have same book, patron, and checkout_date
        """
        if not isinstance(other, CheckoutRecord):
            return False
        return (self.book == other.book and 
                self.patron == other.patron and 
                self.checkout_date == other.checkout_date)