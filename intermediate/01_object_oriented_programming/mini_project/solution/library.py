"""
Library class for the Library Management System - Reference Solution

This module contains the complete implementation of the Library class.
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
        self.name = name
        self.data_file = data_file
        self.books = {}  # ISBN -> Book
        self.patrons = {}  # patron_id -> Patron
        self.checkout_records = []
    
    def add_book(self, book: Book) -> bool:
        """
        Add a book to the library inventory.
        
        Args:
            book: Book instance to add
            
        Returns:
            bool: True if book was added, False if ISBN already exists
        """
        if book.isbn in self.books:
            return False
        
        self.books[book.isbn] = book
        return True
    
    def remove_book(self, isbn: str) -> bool:
        """
        Remove a book from the library inventory.
        
        Args:
            isbn: ISBN of the book to remove
            
        Returns:
            bool: True if book was removed, False if not found or currently checked out
        """
        if isbn not in self.books:
            return False
        
        book = self.books[isbn]
        if not book.is_available:
            return False  # Book is currently checked out
        
        del self.books[isbn]
        return True
    
    def register_patron(self, patron: Patron) -> bool:
        """
        Register a new patron with the library.
        
        Args:
            patron: Patron instance to register
            
        Returns:
            bool: True if patron was registered, False if patron_id already exists
        """
        if patron.patron_id in self.patrons:
            return False
        
        self.patrons[patron.patron_id] = patron
        return True
    
    def search_books(self, query: str, search_type: str = "title") -> List[Book]:
        """
        Search for books by title, author, or ISBN.
        
        Args:
            query: Search query string
            search_type: Type of search ("title", "author", or "isbn")
            
        Returns:
            List[Book]: List of matching books
        """
        query_lower = query.lower()
        results = []
        
        for book in self.books.values():
            if search_type == "title":
                if query_lower in book.title.lower():
                    results.append(book)
            elif search_type == "author":
                if query_lower in book.author.lower():
                    results.append(book)
            elif search_type == "isbn":
                if query_lower == book.isbn.lower():
                    results.append(book)
        
        return results
    
    def checkout_book(self, isbn: str, patron_id: str) -> Tuple[bool, str]:
        """
        Process a book checkout.
        
        Args:
            isbn: ISBN of book to checkout
            patron_id: ID of patron checking out book
            
        Returns:
            Tuple[bool, str]: (Success status, message)
        """
        # Check if book exists
        if isbn not in self.books:
            return False, "Book not found"
        
        book = self.books[isbn]
        
        # Check if book is available
        if not book.is_available:
            return False, "Book is currently checked out"
        
        # Check if patron exists
        if patron_id not in self.patrons:
            return False, "Patron not found"
        
        patron = self.patrons[patron_id]
        
        # Check if patron can checkout more books
        if not patron.can_checkout_book():
            return False, f"Patron has reached maximum checkout limit ({patron.max_books} books)"
        
        # Process checkout
        book.mark_as_checked_out()
        patron.checkout_book(book)
        
        # Create checkout record
        checkout_record = CheckoutRecord(book, patron)
        self.checkout_records.append(checkout_record)
        
        return True, f"Book '{book.title}' checked out successfully to {patron.name}"
    
    def return_book(self, isbn: str, patron_id: str) -> Tuple[bool, str, float]:
        """
        Process a book return.
        
        Args:
            isbn: ISBN of book to return
            patron_id: ID of patron returning book
            
        Returns:
            Tuple[bool, str, float]: (Success status, message, fine amount)
        """
        # Find the active checkout record
        checkout_record = None
        for record in self.checkout_records:
            if (record.book.isbn == isbn and 
                record.patron.patron_id == patron_id and 
                not record.is_returned()):
                checkout_record = record
                break
        
        if not checkout_record:
            return False, "No active checkout found for this book and patron", 0.0
        
        # Process return
        book = checkout_record.book
        patron = checkout_record.patron
        
        book.mark_as_available()
        patron.return_book(book)
        fine = checkout_record.return_book()
        
        message = f"Book '{book.title}' returned successfully"
        if fine > 0:
            message += f" (Fine: ${fine:.2f})"
        
        return True, message, fine
    
    def get_overdue_books(self) -> List[CheckoutRecord]:
        """
        Get list of all overdue checkout records.
        
        Returns:
            List[CheckoutRecord]: List of overdue checkout records
        """
        overdue_records = []
        for record in self.checkout_records:
            if not record.is_returned() and record.is_overdue():
                overdue_records.append(record)
        
        return overdue_records
    
    def get_patron_history(self, patron_id: str) -> List[CheckoutRecord]:
        """
        Get checkout history for a specific patron.
        
        Args:
            patron_id: ID of the patron
            
        Returns:
            List[CheckoutRecord]: List of checkout records for the patron
        """
        patron_records = []
        for record in self.checkout_records:
            if record.patron.patron_id == patron_id:
                patron_records.append(record)
        
        return patron_records
    
    def generate_inventory_report(self) -> Dict:
        """
        Generate a report of library inventory.
        
        Returns:
            Dict: Dictionary containing inventory statistics
        """
        total_books = len(self.books)
        available_books = sum(1 for book in self.books.values() if book.is_available)
        checked_out_books = total_books - available_books
        
        active_checkouts = sum(1 for record in self.checkout_records if not record.is_returned())
        overdue_books = len(self.get_overdue_books())
        
        return {
            'total_books': total_books,
            'available_books': available_books,
            'checked_out_books': checked_out_books,
            'total_patrons': len(self.patrons),
            'active_checkouts': active_checkouts,
            'overdue_books': overdue_books
        }
    
    def save_data(self) -> bool:
        """
        Save library data to JSON file.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            data = {
                'library_name': self.name,
                'books': [book.get_info() for book in self.books.values()],
                'patrons': [patron.get_info() for patron in self.patrons.values()],
                'checkout_records': [record.get_info() for record in self.checkout_records]
            }
            
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self) -> bool:
        """
        Load library data from JSON file.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            # Clear existing data
            self.books.clear()
            self.patrons.clear()
            self.checkout_records.clear()
            
            # Load library name
            self.name = data.get('library_name', self.name)
            
            # Load books
            for book_data in data.get('books', []):
                book = Book(
                    book_data['title'],
                    book_data['author'],
                    book_data['isbn'],
                    book_data['publication_year'],
                    book_data['genre']
                )
                if not book_data['is_available']:
                    book.mark_as_checked_out()
                self.books[book.isbn] = book
            
            # Load patrons
            for patron_data in data.get('patrons', []):
                patron = Patron(
                    patron_data['patron_id'],
                    patron_data['name'],
                    patron_data['email'],
                    patron_data['phone'],
                    patron_data['max_books']
                )
                # Set registration date from saved data
                patron.registration_date = datetime.fromisoformat(patron_data['registration_date']).date()
                self.patrons[patron.patron_id] = patron
            
            # Load checkout records
            for record_data in data.get('checkout_records', []):
                book = self.books[record_data['book_isbn']]
                patron = self.patrons[record_data['patron_id']]
                
                checkout_date = datetime.fromisoformat(record_data['checkout_date']).date()
                record = CheckoutRecord(book, patron, checkout_date)
                
                if record_data['return_date']:
                    return_date = datetime.fromisoformat(record_data['return_date']).date()
                    record.return_book(return_date)
                else:
                    # Book is still checked out, update patron's checked out books
                    patron.checkout_book(book)
                
                record.fine_amount = record_data['fine_amount']
                self.checkout_records.append(record)
            
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def get_library_info(self) -> Dict:
        """
        Get general information about the library.
        
        Returns:
            Dict: Dictionary with library information
        """
        return {
            'name': self.name,
            'total_books': len(self.books),
            'total_patrons': len(self.patrons),
            'current_date': date.today().isoformat()
        }
    
    def __str__(self) -> str:
        """
        Return string representation of the library.
        
        Returns:
            str: Formatted string with library information
        """
        return f"{self.name} - Books: {len(self.books)}, Patrons: {len(self.patrons)}"