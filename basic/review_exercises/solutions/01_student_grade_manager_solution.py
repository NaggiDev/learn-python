"""
Student Grade Manager - Solution

This solution demonstrates the integration of multiple basic Python concepts
while introducing patterns that prepare students for intermediate topics.
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
        """Add a new student to the system."""
        if name in self.students:
            return False
        self.students[name] = []
        return True
    
    def add_grade(self, name: str, grade: float) -> bool:
        """Add a grade for a student."""
        if not (0 <= grade <= 100):
            return False
        if name not in self.students:
            return False
        self.students[name].append(grade)
        return True
    
    def get_student_average(self, name: str) -> Optional[float]:
        """Calculate the average grade for a student."""
        if name not in self.students or not self.students[name]:
            return None
        return sum(self.students[name]) / len(self.students[name])
    
    def get_all_averages(self) -> Dict[str, float]:
        """Get average grades for all students."""
        averages = {}
        for name in self.students:
            avg = self.get_student_average(name)
            if avg is not None:
                averages[name] = avg
        return averages
    
    def find_students_by_grade_range(self, min_grade: float, max_grade: float) -> List[str]:
        """Find students whose average falls within a grade range."""
        matching_students = []
        averages = self.get_all_averages()
        
        for name, avg in averages.items():
            if min_grade <= avg <= max_grade:
                matching_students.append(name)
        
        return sorted(matching_students)
    
    def generate_report(self) -> str:
        """Generate a formatted grade report for all students."""
        if not self.students:
            return "No students in the system."
        
        report_lines = ["Student Grade Report", "=" * 50]
        
        all_averages = []
        for name in sorted(self.students.keys()):
            grades = self.students[name]
            if grades:
                avg = sum(grades) / len(grades)
                all_averages.append(avg)
                grade_str = ", ".join(f"{g:.1f}" for g in grades)
                report_lines.append(f"{name:<20} | Grades: {grade_str:<30} | Average: {avg:.2f}")
            else:
                report_lines.append(f"{name:<20} | No grades recorded")
        
        # Add class statistics
        if all_averages:
            report_lines.extend([
                "=" * 50,
                f"Class Statistics:",
                f"Number of students: {len(all_averages)}",
                f"Class average: {sum(all_averages) / len(all_averages):.2f}",
                f"Highest average: {max(all_averages):.2f}",
                f"Lowest average: {min(all_averages):.2f}"
            ])
        
        return "\n".join(report_lines)
    
    def save_to_file(self) -> bool:
        """Save student data to CSV file."""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for name, grades in self.students.items():
                    row = [name] + [str(grade) for grade in grades]
                    writer.writerow(row)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
    
    def load_from_file(self) -> bool:
        """Load student data from CSV file."""
        if not os.path.exists(self.filename):
            return False
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Skip empty rows
                        name = row[0]
                        grades = []
                        for grade_str in row[1:]:
                            try:
                                grades.append(float(grade_str))
                            except ValueError:
                                continue  # Skip invalid grades
                        self.students[name] = grades
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False


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


def get_float_input(prompt: str, min_val: float = None, max_val: float = None) -> Optional[float]:
    """Helper function to get validated float input."""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            return None


def main():
    """Main program loop with menu-driven interface."""
    manager = StudentGradeManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            name = input("Enter student name: ").strip()
            if name:
                if manager.add_student(name):
                    print(f"Student '{name}' added successfully.")
                else:
                    print(f"Student '{name}' already exists.")
            else:
                print("Please enter a valid name.")
                
        elif choice == "2":
            name = input("Enter student name: ").strip()
            if name not in manager.students:
                print(f"Student '{name}' not found. Add the student first.")
                continue
            
            grade = get_float_input("Enter grade (0-100): ", 0, 100)
            if grade is not None:
                if manager.add_grade(name, grade):
                    print(f"Grade {grade} added for {name}.")
                else:
                    print("Failed to add grade.")
            
        elif choice == "3":
            name = input("Enter student name: ").strip()
            avg = manager.get_student_average(name)
            if avg is not None:
                print(f"{name}'s average: {avg:.2f}")
            else:
                print(f"Student '{name}' not found or has no grades.")
                
        elif choice == "4":
            averages = manager.get_all_averages()
            if averages:
                print("\nStudent Averages:")
                print("-" * 30)
                for name, avg in sorted(averages.items()):
                    print(f"{name:<20}: {avg:.2f}")
            else:
                print("No students with grades found.")
                
        elif choice == "5":
            min_grade = get_float_input("Enter minimum grade: ", 0, 100)
            if min_grade is None:
                continue
            max_grade = get_float_input("Enter maximum grade: ", min_grade, 100)
            if max_grade is None:
                continue
                
            students = manager.find_students_by_grade_range(min_grade, max_grade)
            if students:
                print(f"\nStudents with averages between {min_grade} and {max_grade}:")
                for student in students:
                    avg = manager.get_student_average(student)
                    print(f"  {student}: {avg:.2f}")
            else:
                print(f"No students found in grade range {min_grade}-{max_grade}.")
                
        elif choice == "6":
            report = manager.generate_report()
            print("\n" + report)
            
        elif choice == "7":
            if manager.save_to_file():
                print(f"Data saved to {manager.filename}")
            else:
                print("Failed to save data.")
                
        elif choice == "8":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()