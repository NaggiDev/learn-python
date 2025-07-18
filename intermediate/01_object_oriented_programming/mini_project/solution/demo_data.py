"""
Demo script to populate the library with sample data

Run this script to create sample books and patrons for testing the system.
"""

from book import Book
from patron import Patron
from library import Library


def create_sample_data():
    """Create and populate library with sample data."""
    
    # Create library
    library = Library("Community Library", "demo_library_data.json")
    
    # Sample books
    books = [
        Book("Python Crash Course", "Eric Matthes", "978-1593279288", 2019, "Programming"),
        Book("Clean Code", "Robert C. Martin", "978-0132350884", 2008, "Programming"),
        Book("The Pragmatic Programmer", "David Thomas", "978-0201616224", 1999, "Programming"),
        Book("Design Patterns", "Gang of Four", "978-0201633612", 1994, "Programming"),
        Book("Introduction to Algorithms", "Thomas H. Cormen", "978-0262033848", 2009, "Computer Science"),
        Book("The Art of Computer Programming", "Donald E. Knuth", "978-0201896831", 1997, "Computer Science"),
        Book("Code Complete", "Steve McConnell", "978-0735619678", 2004, "Programming"),
        Book("Refactoring", "Martin Fowler", "978-0201485677", 1999, "Programming"),
        Book("Head First Design Patterns", "Eric Freeman", "978-0596007126", 2004, "Programming"),
        Book("Effective Python", "Brett Slatkin", "978-0134853987", 2019, "Programming")
    ]
    
    # Sample patrons
    patrons = [
        Patron("P001", "Alice Johnson", "alice.johnson@email.com", "555-0101"),
        Patron("P002", "Bob Smith", "bob.smith@email.com", "555-0102"),
        Patron("P003", "Carol Davis", "carol.davis@email.com", "555-0103"),
        Patron("P004", "David Wilson", "david.wilson@email.com", "555-0104"),
        Patron("P005", "Eva Brown", "eva.brown@email.com", "555-0105")
    ]
    
    # Add books to library
    print("Adding books to library...")
    for book in books:
        if library.add_book(book):
            print(f"✓ Added: {book.title}")
        else:
            print(f"✗ Failed to add: {book.title}")
    
    # Register patrons
    print("\nRegistering patrons...")
    for patron in patrons:
        if library.register_patron(patron):
            print(f"✓ Registered: {patron.name}")
        else:
            print(f"✗ Failed to register: {patron.name}")
    
    # Create some sample checkouts
    print("\nCreating sample checkouts...")
    checkouts = [
        ("978-1593279288", "P001"),  # Alice checks out Python Crash Course
        ("978-0132350884", "P002"),  # Bob checks out Clean Code
        ("978-0201616224", "P003"),  # Carol checks out The Pragmatic Programmer
    ]
    
    for isbn, patron_id in checkouts:
        success, message = library.checkout_book(isbn, patron_id)
        if success:
            print(f"✓ {message}")
        else:
            print(f"✗ Checkout failed: {message}")
    
    # Save the data
    print("\nSaving library data...")
    if library.save_data():
        print("✓ Data saved successfully!")
    else:
        print("✗ Failed to save data")
    
    # Generate and display report
    print("\n" + "="*60)
    print("LIBRARY INVENTORY REPORT")
    print("="*60)
    
    report = library.generate_inventory_report()
    info = library.get_library_info()
    
    print(f"Library: {info['name']}")
    print(f"Date: {info['current_date']}")
    print(f"\nBooks: {report['total_books']} total, {report['available_books']} available, {report['checked_out_books']} checked out")
    print(f"Patrons: {report['total_patrons']} registered")
    print(f"Active Checkouts: {report['active_checkouts']}")
    print(f"Overdue Books: {report['overdue_books']}")
    
    print("\n" + "="*60)
    print("Sample data created successfully!")
    print("You can now run 'python main.py' to interact with the library system.")
    print("The data will be loaded automatically from 'demo_library_data.json'")
    print("="*60)
    
    return library


if __name__ == "__main__":
    create_sample_data()