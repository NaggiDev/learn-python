"""
Test suite for the Library Management System

Run this file to test your implementation:
python test_library_system.py

Or use pytest if you have it installed:
pytest test_library_system.py -v
"""

import unittest
from datetime import date, timedelta
import os
import json
from book import Book
from patron import Patron
from checkout_record import CheckoutRecord
from library import Library


class TestBook(unittest.TestCase):
    """Test cases for the Book class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.book = Book("Python Programming", "John Doe", "978-0123456789", 2020, "Programming")
    
    def test_book_creation(self):
        """Test book creation with valid data."""
        self.assertEqual(self.book.title, "Python Programming")
        self.assertEqual(self.book.author, "John Doe")
        self.assertEqual(self.book.isbn, "978-0123456789")
        self.assertEqual(self.book.publication_year, 2020)
        self.assertEqual(self.book.genre, "Programming")
        self.assertTrue(self.book.is_available)
    
    def test_book_checkout_return(self):
        """Test book checkout and return functionality."""
        # Test checkout
        self.assertTrue(self.book.mark_as_checked_out())
        self.assertFalse(self.book.is_available)
        
        # Test checkout when already checked out
        self.assertFalse(self.book.mark_as_checked_out())
        
        # Test return
        self.assertTrue(self.book.mark_as_available())
        self.assertTrue(self.book.is_available)
        
        # Test return when already available
        self.assertFalse(self.book.mark_as_available())
    
    def test_book_info(self):
        """Test book info method."""
        info = self.book.get_info()
        self.assertIsInstance(info, dict)
        self.assertEqual(info['title'], "Python Programming")
        self.assertEqual(info['isbn'], "978-0123456789")
        self.assertIn('is_available', info)
    
    def test_book_equality(self):
        """Test book equality based on ISBN."""
        book2 = Book("Different Title", "Different Author", "978-0123456789", 2021)
        book3 = Book("Python Programming", "John Doe", "978-9876543210", 2020)
        
        self.assertEqual(self.book, book2)  # Same ISBN
        self.assertNotEqual(self.book, book3)  # Different ISBN
    
    def test_book_string_representation(self):
        """Test book string representation."""
        book_str = str(self.book)
        self.assertIsInstance(book_str, str)
        self.assertIn("Python Programming", book_str)


class TestPatron(unittest.TestCase):
    """Test cases for the Patron class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.patron = Patron("P001", "Jane Smith", "jane@email.com", "555-1234")
        self.book1 = Book("Book 1", "Author 1", "1111111111", 2020)
        self.book2 = Book("Book 2", "Author 2", "2222222222", 2021)
    
    def test_patron_creation(self):
        """Test patron creation with valid data."""
        self.assertEqual(self.patron.patron_id, "P001")
        self.assertEqual(self.patron.name, "Jane Smith")
        self.assertEqual(self.patron.email, "jane@email.com")
        self.assertEqual(self.patron.phone, "555-1234")
        self.assertEqual(self.patron.max_books, 5)
        self.assertEqual(len(self.patron.checked_out_books), 0)
    
    def test_patron_checkout_limit(self):
        """Test patron checkout limit functionality."""
        self.assertTrue(self.patron.can_checkout_book())
        
        # Checkout books up to limit
        for i in range(5):
            book = Book(f"Book {i}", f"Author {i}", f"{i}000000000", 2020)
            self.assertTrue(self.patron.checkout_book(book))
        
        # Should not be able to checkout more
        self.assertFalse(self.patron.can_checkout_book())
        extra_book = Book("Extra Book", "Extra Author", "9999999999", 2020)
        self.assertFalse(self.patron.checkout_book(extra_book))
    
    def test_patron_book_operations(self):
        """Test patron book checkout and return operations."""
        # Test checkout
        self.assertTrue(self.patron.checkout_book(self.book1))
        self.assertEqual(self.patron.get_checkout_count(), 1)
        self.assertIn(self.book1, self.patron.get_checked_out_books())
        
        # Test duplicate checkout
        self.assertFalse(self.patron.checkout_book(self.book1))
        
        # Test return
        self.assertTrue(self.patron.return_book(self.book1))
        self.assertEqual(self.patron.get_checkout_count(), 0)
        self.assertNotIn(self.book1, self.patron.get_checked_out_books())
        
        # Test return non-checked-out book
        self.assertFalse(self.patron.return_book(self.book2))
    
    def test_patron_info(self):
        """Test patron info method."""
        info = self.patron.get_info()
        self.assertIsInstance(info, dict)
        self.assertEqual(info['patron_id'], "P001")
        self.assertEqual(info['name'], "Jane Smith")
        self.assertIn('checkout_count', info)


class TestCheckoutRecord(unittest.TestCase):
    """Test cases for the CheckoutRecord class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.book = Book("Test Book", "Test Author", "1234567890", 2020)
        self.patron = Patron("P001", "Test Patron", "test@email.com", "555-0000")
        self.checkout_date = date.today() - timedelta(days=10)
        self.record = CheckoutRecord(self.book, self.patron, self.checkout_date)
    
    def test_checkout_record_creation(self):
        """Test checkout record creation."""
        self.assertEqual(self.record.book, self.book)
        self.assertEqual(self.record.patron, self.patron)
        self.assertEqual(self.record.checkout_date, self.checkout_date)
        self.assertIsNone(self.record.return_date)
        self.assertEqual(self.record.fine_amount, 0.0)
    
    def test_overdue_calculation(self):
        """Test overdue calculation."""
        # Record is 10 days old, due date should be checkout_date + 14 days
        # So it should not be overdue yet
        self.assertFalse(self.record.is_overdue())
        
        # Test with a date that makes it overdue
        future_date = self.checkout_date + timedelta(days=20)
        self.assertTrue(self.record.is_overdue(future_date))
        self.assertEqual(self.record.days_overdue(future_date), 6)  # 20 - 14 = 6 days overdue
    
    def test_fine_calculation(self):
        """Test fine calculation."""
        # Not overdue, no fine
        self.assertEqual(self.record.calculate_fine(), 0.0)
        
        # 6 days overdue
        overdue_date = self.checkout_date + timedelta(days=20)
        expected_fine = 6 * CheckoutRecord.DAILY_FINE_RATE
        self.assertEqual(self.record.calculate_fine(overdue_date), expected_fine)
    
    def test_book_return(self):
        """Test book return functionality."""
        return_date = date.today()
        fine = self.record.return_book(return_date)
        
        self.assertTrue(self.record.is_returned())
        self.assertEqual(self.record.return_date, return_date)
        self.assertGreaterEqual(fine, 0.0)
        
        # Test returning already returned book
        with self.assertRaises(ValueError):
            self.record.return_book()


class TestLibrary(unittest.TestCase):
    """Test cases for the Library class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.library = Library("Test Library", "test_data.json")
        self.book1 = Book("Book 1", "Author 1", "1111111111", 2020)
        self.book2 = Book("Book 2", "Author 2", "2222222222", 2021)
        self.patron1 = Patron("P001", "Patron 1", "p1@email.com", "555-0001")
        self.patron2 = Patron("P002", "Patron 2", "p2@email.com", "555-0002")
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")
    
    def test_library_creation(self):
        """Test library creation."""
        self.assertEqual(self.library.name, "Test Library")
        self.assertEqual(len(self.library.books), 0)
        self.assertEqual(len(self.library.patrons), 0)
        self.assertEqual(len(self.library.checkout_records), 0)
    
    def test_add_remove_books(self):
        """Test adding and removing books."""
        # Test add book
        self.assertTrue(self.library.add_book(self.book1))
        self.assertEqual(len(self.library.books), 1)
        
        # Test add duplicate ISBN
        duplicate_book = Book("Different Title", "Different Author", "1111111111", 2022)
        self.assertFalse(self.library.add_book(duplicate_book))
        
        # Test remove book
        self.assertTrue(self.library.remove_book("1111111111"))
        self.assertEqual(len(self.library.books), 0)
        
        # Test remove non-existent book
        self.assertFalse(self.library.remove_book("9999999999"))
    
    def test_register_patron(self):
        """Test patron registration."""
        self.assertTrue(self.library.register_patron(self.patron1))
        self.assertEqual(len(self.library.patrons), 1)
        
        # Test duplicate patron ID
        duplicate_patron = Patron("P001", "Different Name", "different@email.com", "555-9999")
        self.assertFalse(self.library.register_patron(duplicate_patron))
    
    def test_book_search(self):
        """Test book search functionality."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        
        # Test search by title
        results = self.library.search_books("Book 1", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Book 1")
        
        # Test search by author
        results = self.library.search_books("Author", "author")
        self.assertEqual(len(results), 2)  # Both books have "Author" in author name
        
        # Test search by ISBN
        results = self.library.search_books("1111111111", "isbn")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].isbn, "1111111111")
    
    def test_checkout_return_workflow(self):
        """Test complete checkout and return workflow."""
        # Setup
        self.library.add_book(self.book1)
        self.library.register_patron(self.patron1)
        
        # Test checkout
        success, message = self.library.checkout_book("1111111111", "P001")
        self.assertTrue(success)
        self.assertFalse(self.book1.is_available)
        self.assertEqual(len(self.library.checkout_records), 1)
        
        # Test return
        success, message, fine = self.library.return_book("1111111111", "P001")
        self.assertTrue(success)
        self.assertTrue(self.book1.is_available)
        self.assertGreaterEqual(fine, 0.0)
    
    def test_overdue_books(self):
        """Test overdue books functionality."""
        # Setup checkout with past date
        self.library.add_book(self.book1)
        self.library.register_patron(self.patron1)
        
        # Create overdue checkout record manually
        past_date = date.today() - timedelta(days=20)
        record = CheckoutRecord(self.book1, self.patron1, past_date)
        self.library.checkout_records.append(record)
        self.book1.mark_as_checked_out()
        self.patron1.checkout_book(self.book1)
        
        overdue_books = self.library.get_overdue_books()
        self.assertEqual(len(overdue_books), 1)
        self.assertTrue(overdue_books[0].is_overdue())
    
    def test_inventory_report(self):
        """Test inventory report generation."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.register_patron(self.patron1)
        
        report = self.library.generate_inventory_report()
        self.assertIsInstance(report, dict)
        self.assertEqual(report['total_books'], 2)
        self.assertEqual(report['available_books'], 2)
        self.assertEqual(report['total_patrons'], 1)


def run_tests():
    """Run all tests."""
    # Create test suite
    test_classes = [TestBook, TestPatron, TestCheckoutRecord, TestLibrary]
    
    suite = unittest.TestSuite()
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print(f"\nFAILURES:")
        for test, traceback in result.failures:
            error_msg = traceback.split('AssertionError: ')[-1].split('\n')[0]
            print(f"- {test}: {error_msg}")
    
    if result.errors:
        print(f"\nERRORS:")
        for test, traceback in result.errors:
            error_msg = traceback.split('\n')[-2]
            print(f"- {test}: {error_msg}")
    
    if not result.failures and not result.errors:
        print("All tests passed! 🎉")
    else:
        print("Some tests failed. Check your implementation.")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    print("Running Library Management System Tests...")
    print("="*60)
    run_tests()