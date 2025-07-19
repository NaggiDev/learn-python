"""
Student Grade Manager - Review Exercise

This exercise combines multiple basic concepts:
- Functions and parameter handling
- Dictionaries and lists
- File operations (reading/writing)
- Control flow and error handling
- String manipulation and formatting

Requirements:
1. Create a StudentGradeManager class that can:
   - Add students and their grades
   - Calculate average grades for students
   - Save/load data from a CSV file
   - Generate grade reports
   - Find students by grade range

2. Implement proper error handling for file operations
3. Use appropriate data structures for efficient operations
4. Provide a simple command-line interface

This bridges to intermediate concepts by introducing:
- Basic class structure (preparation for OOP)
- Data persistence patterns
- Menu-driven applications
"""

import csv
import os
from typing import Dict, List, Tuple, Optional


class StudentGradeManager:
    """A simple grade management system combining basic Python concepts."""
    
    def __init__(self, filename: str = "grades.csv"):
        """Initialize the grade manager with an optional filename."""
        self.filename = filename
        self.students = {}  # Dict[str, List[float]]
        self.load_from_file()
    
    def add_student(self, name: str) -> bool:
        """
        Add a new student to the system.
        
        Args:
            name: Student's name
            
        Returns:
            True if student was added, False if already exists
        """
        # TODO: Implement this method
        # - Check if student already exists
        # - Add student with empty grade list if new
        # - Return appropriate boolean value
        pass
    
    def add_grade(self, name: str, grade: float) -> bool:
        """
        Add a grade for a student.
        
        Args:
            name: Student's name
            grade: Grade value (0-100)
            
        Returns:
            True if grade was added, False if student doesn't exist or invalid grade
        """
        # TODO: Implement this method
        # - Validate grade is between 0 and 100
        # - Check if student exists
        # - Add grade to student's list
        # - Return appropriate boolean value
        pass
    
    def get_student_average(self, name: str) -> Optional[float]:
        """
        Calculate the average grade for a student.
        
        Args:
            name: Student's name
            
        Returns:
            Average grade or None if student doesn't exist or has no grades
        """
        # TODO: Implement this method
        # - Check if student exists
        # - Calculate and return average of grades
        # - Handle case where student has no grades
        pass
    
    def get_all_averages(self) -> Dict[str, float]:
        """
        Get average grades for all students.
        
        Returns:
            Dictionary mapping student names to their averages
        """
        # TODO: Implement this method
        # - Calculate averages for all students
        # - Return dictionary of name -> average
        # - Skip students with no grades
        pass
    
    def find_students_by_grade_range(self, min_grade: float, max_grade: float) -> List[str]:
        """
        Find students whose average falls within a grade range.
        
        Args:
            min_grade: Minimum average grade
            max_grade: Maximum average grade
            
        Returns:
            List of student names within the range
        """
        # TODO: Implement this method
        # - Get all student averages
        # - Filter students within the specified range
        # - Return list of matching student names
        pass
    
    def generate_report(self) -> str:
        """
        Generate a formatted grade report for all students.
        
        Returns:
            Formatted string report
        """
        # TODO: Implement this method
        # - Create a formatted report showing each student's grades and average
        # - Include overall class statistics
        # - Format nicely with proper alignment
        pass
    
    def save_to_file(self) -> bool:
        """
        Save student data to CSV file.
        
        Returns:
            True if successful, False otherwise
        """
        # TODO: Implement this method
        # - Write student data to CSV file
        # - Format: student_name, grade1, grade2, grade3, ...
        # - Handle file writing errors
        # - Return success status
        pass
    
    def load_from_file(self) -> bool:
        """
        Load student data from CSV file.
        
        Returns:
            True if successful, False otherwise
        """
        # TODO: Implement this method
        # - Read student data from CSV file
        # - Parse grades as floats
        # - Handle file reading errors (file not found, etc.)
        # - Return success status
        pass


def display_menu():
    """Display the main menu options."""
    print("\n=== Student Grade Manager ===")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Student Average")
    print("4. View All Averages")
    print("5. Find Students by Grade Range")
    print("6. Generate Report")
    print("7. Save Data")
    print("8. Exit")
    print("=" * 30)


def main():
    """Main program loop with menu-driven interface."""
    manager = StudentGradeManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            # TODO: Implement add student functionality
            # - Get student name from user
            # - Call add_student method
            # - Display appropriate success/error message
            pass
            
        elif choice == "2":
            # TODO: Implement add grade functionality
            # - Get student name and grade from user
            # - Validate grade input
            # - Call add_grade method
            # - Display appropriate success/error message
            pass
            
        elif choice == "3":
            # TODO: Implement view student average functionality
            # - Get student name from user
            # - Call get_student_average method
            # - Display result or error message
            pass
            
        elif choice == "4":
            # TODO: Implement view all averages functionality
            # - Call get_all_averages method
            # - Display all student averages in a formatted way
            pass
            
        elif choice == "5":
            # TODO: Implement find students by grade range functionality
            # - Get min and max grades from user
            # - Call find_students_by_grade_range method
            # - Display matching students
            pass
            
        elif choice == "6":
            # TODO: Implement generate report functionality
            # - Call generate_report method
            # - Display the formatted report
            pass
            
        elif choice == "7":
            # TODO: Implement save data functionality
            # - Call save_to_file method
            # - Display success/error message
            pass
            
        elif choice == "8":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()