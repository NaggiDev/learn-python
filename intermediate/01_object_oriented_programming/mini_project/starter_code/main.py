"""
Main application for the Library Management System

This module provides a command-line interface for the library system.
Run this file to interact with the library management system.
"""

from datetime import date
from book import Book
from patron import Patron
from library import Library


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Register Patron")
    print("4. Search Books")
    print("5. Checkout Book")
    print("6. Return Book")
    print("7. View Overdue Books")
    print("8. View Patron History")
    print("9. Generate Inventory Report")
    print("10. Save Data")
    print("11. Load Data")
    print("0. Exit")
    print("="*50)


def add_book_menu(library: Library):
    """Handle adding a new book."""
    print("\n--- Add New Book ---")
    try:
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        isbn = input("Enter ISBN: ").strip()
        year = int(input("Enter publication year: "))
        genre = input("Enter genre (optional): ").strip() or "General"
        
        # TODO: Create a Book object and add it to the library
        # - Create Book instance with the provided information
        # - Use library.add_book() to add it
        # - Print success or error message based on result
        
        print("TODO: Implement book addition")
        
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except Exception as e:
        print(f"Error adding book: {e}")


def register_patron_menu(library: Library):
    """Handle registering a new patron."""
    print("\n--- Register New Patron ---")
    try:
        patron_id = input("Enter patron ID: ").strip()
        name = input("Enter full name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone number: ").strip()
        max_books = input("Enter max books (default 5): ").strip()
        max_books = int(max_books) if max_books else 5
        
        # TODO: Create a Patron object and register it
        # - Create Patron instance with the provided information
        # - Use library.register_patron() to register
        # - Print success or error message based on result
        
        print("TODO: Implement patron registration")
        
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except Exception as e:
        print(f"Error registering patron: {e}")


def search_books_menu(library: Library):
    """Handle book search."""
    print("\n--- Search Books ---")
    print("1. Search by Title")
    print("2. Search by Author") 
    print("3. Search by ISBN")
    
    try:
        choice = input("Enter search type (1-3): ").strip()
        query = input("Enter search query: ").strip()
        
        search_types = {"1": "title", "2": "author", "3": "isbn"}
        search_type = search_types.get(choice)
        
        if not search_type:
            print("Invalid search type selected.")
            return
            
        # TODO: Implement book search
        # - Use library.search_books() with query and search_type
        # - Display results in a formatted way
        # - Show book availability status
        
        print("TODO: Implement book search")
        
    except Exception as e:
        print(f"Error searching books: {e}")


def checkout_book_menu(library: Library):
    """Handle book checkout."""
    print("\n--- Checkout Book ---")
    try:
        isbn = input("Enter book ISBN: ").strip()
        patron_id = input("Enter patron ID: ").strip()
        
        # TODO: Implement book checkout
        # - Use library.checkout_book() with isbn and patron_id
        # - Display success or error message
        
        print("TODO: Implement book checkout")
        
    except Exception as e:
        print(f"Error during checkout: {e}")


def return_book_menu(library: Library):
    """Handle book return."""
    print("\n--- Return Book ---")
    try:
        isbn = input("Enter book ISBN: ").strip()
        patron_id = input("Enter patron ID: ").strip()
        
        # TODO: Implement book return
        # - Use library.return_book() with isbn and patron_id
        # - Display success message and any fine information
        
        print("TODO: Implement book return")
        
    except Exception as e:
        print(f"Error during return: {e}")


def view_overdue_books(library: Library):
    """Display overdue books."""
    print("\n--- Overdue Books ---")
    try:
        # TODO: Implement overdue books display
        # - Use library.get_overdue_books()
        # - Display each overdue record with book, patron, and fine info
        
        print("TODO: Implement overdue books display")
        
    except Exception as e:
        print(f"Error retrieving overdue books: {e}")


def view_patron_history(library: Library):
    """Display patron checkout history."""
    print("\n--- Patron History ---")
    try:
        patron_id = input("Enter patron ID: ").strip()
        
        # TODO: Implement patron history display
        # - Use library.get_patron_history() with patron_id
        # - Display checkout history in a formatted way
        
        print("TODO: Implement patron history display")
        
    except Exception as e:
        print(f"Error retrieving patron history: {e}")


def generate_report(library: Library):
    """Generate and display inventory report."""
    print("\n--- Inventory Report ---")
    try:
        # TODO: Implement inventory report
        # - Use library.generate_inventory_report()
        # - Display the report in a formatted way
        
        print("TODO: Implement inventory report")
        
    except Exception as e:
        print(f"Error generating report: {e}")


def main():
    """Main application loop."""
    library = Library("Community Library")
    
    # Try to load existing data
    if library.load_data():
        print("Library data loaded successfully!")
    else:
        print("Starting with empty library (no existing data found).")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-11): ").strip()
        
        if choice == "0":
            # Ask if user wants to save before exiting
            save_choice = input("Save data before exiting? (y/n): ").strip().lower()
            if save_choice == 'y':
                if library.save_data():
                    print("Data saved successfully!")
                else:
                    print("Error saving data.")
            print("Thank you for using the Library Management System!")
            break
        elif choice == "1":
            add_book_menu(library)
        elif choice == "2":
            isbn = input("Enter ISBN of book to remove: ").strip()
            if library.remove_book(isbn):
                print("Book removed successfully!")
            else:
                print("Book not found or currently checked out.")
        elif choice == "3":
            register_patron_menu(library)
        elif choice == "4":
            search_books_menu(library)
        elif choice == "5":
            checkout_book_menu(library)
        elif choice == "6":
            return_book_menu(library)
        elif choice == "7":
            view_overdue_books(library)
        elif choice == "8":
            view_patron_history(library)
        elif choice == "9":
            generate_report(library)
        elif choice == "10":
            if library.save_data():
                print("Data saved successfully!")
            else:
                print("Error saving data.")
        elif choice == "11":
            if library.load_data():
                print("Data loaded successfully!")
            else:
                print("Error loading data.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()