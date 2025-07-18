# Library Management System Mini-Project

## Project Overview

This mini-project will help you apply object-oriented programming concepts by building a library management system. You'll create classes to represent books, patrons, and the library itself, implementing features like book checkout, returns, and inventory management.

## Learning Objectives

By completing this project, you will:
- Apply class design principles and object-oriented concepts
- Implement inheritance and polymorphism
- Practice encapsulation and data validation
- Use composition to model real-world relationships
- Handle exceptions and edge cases
- Write comprehensive tests for your classes

## Project Requirements

### Core Features

1. **Book Management**
   - Add new books to the library inventory
   - Remove books from inventory
   - Search for books by title, author, or ISBN
   - Track book availability status

2. **Patron Management**
   - Register new library patrons
   - Maintain patron information (name, ID, contact details)
   - Track books currently checked out by each patron
   - Implement borrowing limits

3. **Checkout/Return System**
   - Allow patrons to check out available books
   - Process book returns
   - Calculate and track due dates
   - Handle overdue books and fines

4. **Library Operations**
   - Generate reports on library inventory
   - List overdue books and associated patrons
   - Display patron checkout history

### Technical Requirements

1. **Object-Oriented Design**
   - Use appropriate classes with clear responsibilities
   - Implement inheritance where beneficial
   - Apply encapsulation to protect data integrity
   - Use composition to model relationships

2. **Error Handling**
   - Handle invalid operations gracefully
   - Provide meaningful error messages
   - Validate input data

3. **Data Persistence**
   - Save library data to files (JSON format)
   - Load existing data on startup
   - Handle file I/O errors

## Class Structure

Your implementation should include the following classes:

### Book Class
- Properties: title, author, ISBN, publication_year, genre, availability_status
- Methods: mark_as_checked_out(), mark_as_available(), get_info()

### Patron Class  
- Properties: patron_id, name, email, phone, checked_out_books, registration_date
- Methods: checkout_book(), return_book(), get_checkout_history()

### Library Class
- Properties: books, patrons, checkout_records
- Methods: add_book(), remove_book(), register_patron(), checkout_book(), return_book(), search_books(), generate_reports()

### CheckoutRecord Class
- Properties: book, patron, checkout_date, due_date, return_date
- Methods: is_overdue(), calculate_fine()

## Implementation Guidelines

1. **Start with the Book class** - implement basic properties and methods
2. **Create the Patron class** - focus on patron management functionality  
3. **Build the CheckoutRecord class** - handle checkout/return logic
4. **Implement the Library class** - tie everything together
5. **Add data persistence** - save/load functionality
6. **Write comprehensive tests** - ensure all functionality works correctly

## Testing Requirements

Your implementation should include tests for:
- Book creation and status management
- Patron registration and book tracking
- Checkout and return operations
- Search functionality
- Error handling scenarios
- Data persistence operations

## Extension Challenges

Once you complete the core requirements, try these additional features:

1. **Advanced Search**
   - Search by multiple criteria
   - Fuzzy string matching
   - Search result ranking

2. **Fine Management**
   - Calculate fines for overdue books
   - Track fine payments
   - Generate fine reports

3. **Book Reservations**
   - Allow patrons to reserve checked-out books
   - Notification system for available reservations
   - Priority queue for popular books

4. **Library Statistics**
   - Most popular books/authors
   - Patron activity reports
   - Inventory turnover analysis

5. **GUI Interface**
   - Create a simple GUI using tkinter
   - Implement user-friendly forms
   - Add visual reports and charts

## Getting Started

1. Review the starter code in the `starter_code/` directory
2. Run the existing tests to understand the expected behavior
3. Implement the classes one by one, running tests after each implementation
4. Add your own test cases to ensure comprehensive coverage
5. Test the complete system with realistic data

## Evaluation Criteria

Your project will be evaluated on:
- **Correctness**: Does the code work as specified?
- **Design**: Are OOP principles applied appropriately?
- **Code Quality**: Is the code clean, readable, and well-documented?
- **Testing**: Are there comprehensive tests with good coverage?
- **Error Handling**: Are edge cases and errors handled gracefully?

## Resources

- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)
- [JSON in Python](https://docs.python.org/3/library/json.html)

Good luck with your library management system!