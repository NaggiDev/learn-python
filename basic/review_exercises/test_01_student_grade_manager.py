"""
Test cases for Student Grade Manager

This test file demonstrates testing concepts that bridge to intermediate topics
while reinforcing basic Python concepts.
"""

import os
import tempfile
import unittest
from solutions.student_grade_manager_solution import StudentGradeManager


class TestStudentGradeManager(unittest.TestCase):
    """Test cases for the StudentGradeManager class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Use a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        self.temp_file.close()
        self.manager = StudentGradeManager(self.temp_file.name)
    
    def tearDown(self):
        """Clean up after each test method."""
        # Remove the temporary file
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_add_student_success(self):
        """Test successfully adding a new student."""
        result = self.manager.add_student("Alice")
        self.assertTrue(result)
        self.assertIn("Alice", self.manager.students)
        self.assertEqual(self.manager.students["Alice"], [])
    
    def test_add_student_duplicate(self):
        """Test adding a student that already exists."""
        self.manager.add_student("Alice")
        result = self.manager.add_student("Alice")
        self.assertFalse(result)
    
    def test_add_grade_success(self):
        """Test successfully adding a grade."""
        self.manager.add_student("Alice")
        result = self.manager.add_grade("Alice", 85.5)
        self.assertTrue(result)
        self.assertEqual(self.manager.students["Alice"], [85.5])
    
    def test_add_grade_invalid_student(self):
        """Test adding a grade for non-existent student."""
        result = self.manager.add_grade("NonExistent", 85.5)
        self.assertFalse(result)
    
    def test_add_grade_invalid_range(self):
        """Test adding grades outside valid range."""
        self.manager.add_student("Alice")
        
        # Test negative grade
        result = self.manager.add_grade("Alice", -10)
        self.assertFalse(result)
        
        # Test grade over 100
        result = self.manager.add_grade("Alice", 110)
        self.assertFalse(result)
        
        # Test valid boundary values
        self.assertTrue(self.manager.add_grade("Alice", 0))
        self.assertTrue(self.manager.add_grade("Alice", 100))
    
    def test_get_student_average_success(self):
        """Test calculating student average."""
        self.manager.add_student("Alice")
        self.manager.add_grade("Alice", 80)
        self.manager.add_grade("Alice", 90)
        self.manager.add_grade("Alice", 70)
        
        average = self.manager.get_student_average("Alice")
        self.assertEqual(average, 80.0)
    
    def test_get_student_average_no_grades(self):
        """Test getting average for student with no grades."""
        self.manager.add_student("Alice")
        average = self.manager.get_student_average("Alice")
        self.assertIsNone(average)
    
    def test_get_student_average_nonexistent(self):
        """Test getting average for non-existent student."""
        average = self.manager.get_student_average("NonExistent")
        self.assertIsNone(average)
    
    def test_get_all_averages(self):
        """Test getting averages for all students."""
        # Add students with grades
        self.manager.add_student("Alice")
        self.manager.add_grade("Alice", 80)
        self.manager.add_grade("Alice", 90)
        
        self.manager.add_student("Bob")
        self.manager.add_grade("Bob", 75)
        self.manager.add_grade("Bob", 85)
        
        # Add student with no grades
        self.manager.add_student("Charlie")
        
        averages = self.manager.get_all_averages()
        
        self.assertEqual(len(averages), 2)  # Only students with grades
        self.assertEqual(averages["Alice"], 85.0)
        self.assertEqual(averages["Bob"], 80.0)
        self.assertNotIn("Charlie", averages)
    
    def test_find_students_by_grade_range(self):
        """Test finding students within a grade range."""
        # Set up test data
        students_grades = {
            "Alice": [90, 95],      # Average: 92.5
            "Bob": [70, 80],        # Average: 75.0
            "Charlie": [85, 90],    # Average: 87.5
            "David": [60, 70]       # Average: 65.0
        }
        
        for name, grades in students_grades.items():
            self.manager.add_student(name)
            for grade in grades:
                self.manager.add_grade(name, grade)
        
        # Test range that includes some students
        students = self.manager.find_students_by_grade_range(75, 90)
        self.assertEqual(set(students), {"Alice", "Bob", "Charlie"})
        
        # Test narrow range
        students = self.manager.find_students_by_grade_range(85, 90)
        self.assertEqual(set(students), {"Alice", "Charlie"})
        
        # Test range with no matches
        students = self.manager.find_students_by_grade_range(95, 100)
        self.assertEqual(students, [])
    
    def test_generate_report(self):
        """Test generating a formatted report."""
        # Test empty system
        report = self.manager.generate_report()
        self.assertEqual(report, "No students in the system.")
        
        # Add test data
        self.manager.add_student("Alice")
        self.manager.add_grade("Alice", 85)
        self.manager.add_grade("Alice", 90)
        
        self.manager.add_student("Bob")
        self.manager.add_grade("Bob", 75)
        
        report = self.manager.generate_report()
        
        # Check that report contains expected elements
        self.assertIn("Student Grade Report", report)
        self.assertIn("Alice", report)
        self.assertIn("Bob", report)
        self.assertIn("87.50", report)  # Alice's average
        self.assertIn("75.00", report)  # Bob's average
        self.assertIn("Class Statistics", report)
    
    def test_save_and_load_file(self):
        """Test saving to and loading from file."""
        # Add test data
        self.manager.add_student("Alice")
        self.manager.add_grade("Alice", 85)
        self.manager.add_grade("Alice", 90)
        
        self.manager.add_student("Bob")
        self.manager.add_grade("Bob", 75)
        
        # Save to file
        result = self.manager.save_to_file()
        self.assertTrue(result)
        
        # Create new manager and load from file
        new_manager = StudentGradeManager(self.temp_file.name)
        
        # Verify data was loaded correctly
        self.assertIn("Alice", new_manager.students)
        self.assertIn("Bob", new_manager.students)
        self.assertEqual(new_manager.students["Alice"], [85.0, 90.0])
        self.assertEqual(new_manager.students["Bob"], [75.0])
    
    def test_load_nonexistent_file(self):
        """Test loading from a non-existent file."""
        manager = StudentGradeManager("nonexistent_file.csv")
        self.assertEqual(manager.students, {})


def run_basic_tests():
    """Run basic functionality tests with simple assertions."""
    print("Running basic functionality tests...")
    
    # Test 1: Basic student management
    manager = StudentGradeManager("test_grades.csv")
    
    # Add students
    assert manager.add_student("Alice") == True
    assert manager.add_student("Bob") == True
    assert manager.add_student("Alice") == False  # Duplicate
    
    # Add grades
    assert manager.add_grade("Alice", 85) == True
    assert manager.add_grade("Alice", 90) == True
    assert manager.add_grade("Bob", 75) == True
    assert manager.add_grade("NonExistent", 80) == False
    
    # Test averages
    alice_avg = manager.get_student_average("Alice")
    assert abs(alice_avg - 87.5) < 0.01
    
    bob_avg = manager.get_student_average("Bob")
    assert abs(bob_avg - 75.0) < 0.01
    
    # Test grade range finding
    students = manager.find_students_by_grade_range(70, 90)
    assert "Alice" in students
    assert "Bob" in students
    
    print("✓ All basic tests passed!")
    
    # Clean up
    if os.path.exists("test_grades.csv"):
        os.remove("test_grades.csv")


if __name__ == "__main__":
    print("Student Grade Manager - Test Suite")
    print("=" * 40)
    
    # Run basic tests first
    run_basic_tests()
    
    print("\nRunning comprehensive unit tests...")
    unittest.main(verbosity=2)