"""
Main application for the Library Management System - Reference Solution

This module provides a complete command-line interface for the library system.
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
        
        book = Book(title, author, isbn, year, genre)
        
        if library.add_book(book):
            print(f"✓ Book '{title}' added successfully!")
        else:
            print(f"✗ Error: A book with ISBN '{isbn}' already exists.")
        
    except ValueError as e:
        print(f"✗ Error: Invalid input - {e}")
    except Exception as e:
        print(f"✗ Error adding book: {e}")


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
        
        patron = Patron(patron_id, name, email, phone, max_books)
        
        if library.register_patron(patron):
            print(f"✓ Patron '{name}' registered successfully!")
        else:
            print(f"✗ Error: A patron with ID '{patron_id}' already exists.")
        
    except ValueError as e:
        print(f"✗ Error: Invalid input - {e}")
    except Exception as e:
        print(f"✗ Error registering patron: {e}")


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
            print("✗ Invalid search type selected.")
            return
        
        results = library.search_books(query, search_type)
        
        if results:
            print(f"\n📚 Found {len(results)} book(s):")
            print("-" * 80)
            for i, book in enumerate(results, 1):
                status = "✓ Available" if book.is_available else "✗ Checked Out"
                print(f"{i}. {book.title}")
                print(f"   Author: {book.author}")
                print(f"   ISBN: {book.isbn}")
                print(f"   Year: {book.publication_year}")
                print(f"   Genre: {book.genre}")
                print(f"   Status: {status}")
                print("-" * 80)
        else:
            print(f"📭 No books found matching '{query}' in {search_type}.")
        
    except Exception as e:
        print(f"✗ Error searching books: {e}")


def checkout_book_menu(library: Library):
    """Handle book checkout."""
    print("\n--- Checkout Book ---")
    try:
        isbn = input("Enter book ISBN: ").strip()
        patron_id = input("Enter patron ID: ").strip()
        
        success, message = library.checkout_book(isbn, patron_id)
        
        if success:
            print(f"✓ {message}")
        else:
            print(f"✗ Checkout failed: {message}")
        
    except Exception as e:
        print(f"✗ Error during checkout: {e}")


def return_book_menu(library: Library):
    """Handle book return."""
    print("\n--- Return Book ---")
    try:
        isbn = input("Enter book ISBN: ").strip()
        patron_id = input("Enter patron ID: ").strip()
        
        success, message, fine = library.return_book(isbn, patron_id)
        
        if success:
            print(f"✓ {message}")
            if fine > 0:
                print(f"💰 Fine amount: ${fine:.2f}")
        else:
            print(f"✗ Return failed: {message}")
        
    except Exception as e:
        print(f"✗ Error during return: {e}")


def view_overdue_books(library: Library):
    """Display overdue books."""
    print("\n--- Overdue Books ---")
    try:
        overdue_records = library.get_overdue_books()
        
        if overdue_records:
            print(f"⚠️  Found {len(overdue_records)} overdue book(s):")
            print("-" * 100)
            
            total_fines = 0
            for i, record in enumerate(overdue_records, 1):
                fine = record.calculate_fine()
                total_fines += fine
                
                print(f"{i}. Book: '{record.book.title}'")
                print(f"   Patron: {record.patron.name} (ID: {record.patron.patron_id})")
                print(f"   Checkout Date: {record.checkout_date}")
                print(f"   Due Date: {record.due_date}")
                print(f"   Days Overdue: {record.days_overdue()}")
                print(f"   Fine: ${fine:.2f}")
                print("-" * 100)
            
            print(f"💰 Total fines: ${total_fines:.2f}")
        else:
            print("✓ No overdue books found!")
        
    except Exception as e:
        print(f"✗ Error retrieving overdue books: {e}")


def view_patron_history(library: Library):
    """Display patron checkout history."""
    print("\n--- Patron History ---")
    try:
        patron_id = input("Enter patron ID: ").strip()
        
        if patron_id not in library.patrons:
            print(f"✗ Patron with ID '{patron_id}' not found.")
            return
        
        patron = library.patrons[patron_id]
        history = library.get_patron_history(patron_id)
        
        print(f"\n📖 Checkout history for {patron.name} (ID: {patron_id}):")
        print(f"📧 Email: {patron.email}")
        print(f"📞 Phone: {patron.phone}")
        print(f"📅 Registration Date: {patron.registration_date}")
        print(f"📚 Current Books: {patron.get_checkout_count()}/{patron.max_books}")
        
        if history:
            print(f"\n📋 Total checkout records: {len(history)}")
            print("-" * 100)
            
            for i, record in enumerate(history, 1):
                status = "Returned" if record.is_returned() else ("Overdue" if record.is_overdue() else "Active")
                
                print(f"{i}. Book: '{record.book.title}'")
                print(f"   Checkout Date: {record.checkout_date}")
                print(f"   Due Date: {record.due_date}")
                print(f"   Return Date: {record.return_date if record.return_date else 'Not returned'}")
                print(f"   Status: {status}")
                if record.fine_amount > 0:
                    print(f"   Fine: ${record.fine_amount:.2f}")
                print("-" * 100)
        else:
            print("📭 No checkout history found for this patron.")
        
    except Exception as e:
        print(f"✗ Error retrieving patron history: {e}")


def generate_report(library: Library):
    """Generate and display inventory report."""
    print("\n--- Inventory Report ---")
    try:
        report = library.generate_inventory_report()
        info = library.get_library_info()
        
        print(f"📊 {info['name']} - Inventory Report")
        print(f"📅 Generated on: {info['current_date']}")
        print("=" * 50)
        
        print(f"📚 Books:")
        print(f"   Total Books: {report['total_books']}")
        print(f"   Available: {report['available_books']}")
        print(f"   Checked Out: {report['checked_out_books']}")
        
        print(f"\n👥 Patrons:")
        print(f"   Total Registered: {report['total_patrons']}")
        
        print(f"\n📋 Checkouts:")
        print(f"   Active Checkouts: {report['active_checkouts']}")
        print(f"   Overdue Books: {report['overdue_books']}")
        
        # Calculate utilization rate
        if report['total_books'] > 0:
            utilization = (report['checked_out_books'] / report['total_books']) * 100
            print(f"\n📈 Library Utilization: {utilization:.1f}%")
        
        print("=" * 50)
        
    except Exception as e:
        print(f"✗ Error generating report: {e}")


def main():
    """Main application loop."""
    print("🏛️  Welcome to the Library Management System!")
    library = Library("Community Library")
    
    # Try to load existing data
    print("📂 Loading library data...")
    if library.load_data():
        print("✓ Library data loaded successfully!")
        info = library.get_library_info()
        print(f"📚 {info['total_books']} books, 👥 {info['total_patrons']} patrons")
    else:
        print("📝 Starting with empty library (no existing data found).")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-11): ").strip()
        
        if choice == "0":
            # Ask if user wants to save before exiting
            save_choice = input("💾 Save data before exiting? (y/n): ").strip().lower()
            if save_choice == 'y':
                if library.save_data():
                    print("✓ Data saved successfully!")
                else:
                    print("✗ Error saving data.")
            print("👋 Thank you for using the Library Management System!")
            break
        elif choice == "1":
            add_book_menu(library)
        elif choice == "2":
            isbn = input("Enter ISBN of book to remove: ").strip()
            if library.remove_book(isbn):
                print("✓ Book removed successfully!")
            else:
                print("✗ Book not found or currently checked out.")
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
                print("✓ Data saved successfully!")
            else:
                print("✗ Error saving data.")
        elif choice == "11":
            if library.load_data():
                print("✓ Data loaded successfully!")
            else:
                print("✗ Error loading data.")
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()