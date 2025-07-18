#!/usr/bin/env python3
"""
Command-Line Task Manager (Solution)

This module implements a simple command-line task manager application
that allows users to create, view, update, and delete tasks.
"""

import csv
import os
from datetime import datetime


class Task:
    """
    Represents a task in the task manager.
    
    Attributes:
        task_id (int): Unique identifier for the task
        title (str): Title of the task
        description (str): Detailed description of the task
        due_date (str): Due date in YYYY-MM-DD format
        completed (bool): Whether the task is completed
    """
    
    def __init__(self, task_id, title, description="", due_date="", completed=False):
        """
        Initialize a new Task object.
        
        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task
            description (str, optional): Detailed description of the task
            due_date (str, optional): Due date in YYYY-MM-DD format
            completed (bool, optional): Whether the task is completed
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
    
    def __str__(self):
        """Return a string representation of the task."""
        status = "✓" if self.completed else "✗"
        return f"[{status}] Task {self.task_id}: {self.title} (Due: {self.due_date or 'Not set'})"


class TaskManager:
    """
    Manages tasks and provides operations to create, read, update, and delete tasks.
    
    Attributes:
        tasks (list): List of Task objects
        data_file (str): Path to the CSV file for storing tasks
    """
    
    def __init__(self, data_file="tasks.csv"):
        """
        Initialize the TaskManager.
        
        Args:
            data_file (str, optional): Path to the CSV file for storing tasks
        """
        self.tasks = []
        self.data_file = data_file
        self.load_tasks()
    
    def load_tasks(self):
        """
        Load tasks from the CSV file.
        
        If the file doesn't exist, it will be created when save_tasks is called.
        """
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 5:
                        task_id = int(row[0])
                        title = row[1]
                        description = row[2]
                        due_date = row[3]
                        completed = row[4].lower() == "true"
                        
                        task = Task(task_id, title, description, due_date, completed)
                        self.tasks.append(task)
        except (IOError, csv.Error) as e:
            print(f"Error loading tasks: {e}")
    
    def save_tasks(self):
        """Save tasks to the CSV file."""
        try:
            with open(self.data_file, "w", newline="") as file:
                writer = csv.writer(file)
                for task in self.tasks:
                    writer.writerow([
                        task.task_id,
                        task.title,
                        task.description,
                        task.due_date,
                        task.completed
                    ])
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def get_next_id(self):
        """
        Get the next available task ID.
        
        Returns:
            int: The next available task ID
        """
        if not self.tasks:
            return 1
        
        return max(task.task_id for task in self.tasks) + 1
    
    def add_task(self, title, description="", due_date=""):
        """
        Add a new task.
        
        Args:
            title (str): Title of the task
            description (str, optional): Detailed description of the task
            due_date (str, optional): Due date in YYYY-MM-DD format
            
        Returns:
            Task: The newly created task
        """
        task_id = self.get_next_id()
        task = Task(task_id, title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_task(self, task_id):
        """
        Get a task by ID.
        
        Args:
            task_id (int): ID of the task to get
            
        Returns:
            Task or None: The task with the given ID, or None if not found
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def update_task(self, task_id, title=None, description=None, due_date=None, completed=None):
        """
        Update a task.
        
        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            due_date (str, optional): New due date for the task
            completed (bool, optional): New completion status for the task
            
        Returns:
            bool: True if the task was updated, False otherwise
        """
        task = self.get_task(task_id)
        if not task:
            return False
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date
        if completed is not None:
            task.completed = completed
        
        self.save_tasks()
        return True
    
    def delete_task(self, task_id):
        """
        Delete a task.
        
        Args:
            task_id (int): ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False otherwise
        """
        task = self.get_task(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        self.save_tasks()
        return True
    
    def get_all_tasks(self):
        """
        Get all tasks.
        
        Returns:
            list: List of all tasks
        """
        return self.tasks
    
    def get_completed_tasks(self):
        """
        Get all completed tasks.
        
        Returns:
            list: List of completed tasks
        """
        return [task for task in self.tasks if task.completed]
    
    def get_incomplete_tasks(self):
        """
        Get all incomplete tasks.
        
        Returns:
            list: List of incomplete tasks
        """
        return [task for task in self.tasks if not task.completed]


def display_menu():
    """Display the main menu of the application."""
    print("\n===== Task Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Complete")
    print("5. Delete Task")
    print("6. Exit")
    print("=======================")


def get_user_input(prompt, required=False):
    """
    Get input from the user with the given prompt.
    
    Args:
        prompt (str): The prompt to display to the user
        required (bool, optional): Whether the input is required
        
    Returns:
        str: The user's input
    """
    while True:
        user_input = input(prompt).strip()
        if user_input or not required:
            return user_input
        print("This field is required. Please try again.")


def validate_date(date_str):
    """
    Validate that the given string is a valid date in YYYY-MM-DD format.
    
    Args:
        date_str (str): The date string to validate
        
    Returns:
        bool: True if the date is valid, False otherwise
    """
    if not date_str:
        return True  # Empty date is valid (no due date)
    
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_task_ui(task_manager):
    """
    User interface for adding a task.
    
    Args:
        task_manager (TaskManager): The task manager instance
    """
    print("\n----- Add Task -----")
    
    title = get_user_input("Enter task title: ", required=True)
    description = get_user_input("Enter task description (optional): ")
    
    while True:
        due_date = get_user_input("Enter due date (YYYY-MM-DD, optional): ")
        if validate_date(due_date):
            break
        print("Invalid date format. Please use YYYY-MM-DD format.")
    
    task = task_manager.add_task(title, description, due_date)
    print(f"Task added successfully: {task}")


def display_tasks(tasks):
    """
    Display a list of tasks.
    
    Args:
        tasks (list): List of Task objects to display
    """
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nTasks:")
    for task in tasks:
        print(f"{task}")
        if task.description:
            print(f"   Description: {task.description}")
        print()


def view_tasks_ui(task_manager):
    """
    User interface for viewing tasks.
    
    Args:
        task_manager (TaskManager): The task manager instance
    """
    print("\n----- View Tasks -----")
    print("1. All Tasks")
    print("2. Completed Tasks")
    print("3. Incomplete Tasks")
    print("4. Back to Main Menu")
    
    choice = get_user_input("Enter your choice (1-4): ")
    
    if choice == "1":
        tasks = task_manager.get_all_tasks()
        print("\n----- All Tasks -----")
        display_tasks(tasks)
    elif choice == "2":
        tasks = task_manager.get_completed_tasks()
        print("\n----- Completed Tasks -----")
        display_tasks(tasks)
    elif choice == "3":
        tasks = task_manager.get_incomplete_tasks()
        print("\n----- Incomplete Tasks -----")
        display_tasks(tasks)
    elif choice == "4":
        return
    else:
        print("Invalid choice.")


def update_task_ui(task_manager):
    """
    User interface for updating a task.
    
    Args:
        task_manager (TaskManager): The task manager instance
    """
    print("\n----- Update Task -----")
    
    try:
        task_id = int(get_user_input("Enter task ID: ", required=True))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    task = task_manager.get_task(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    
    print(f"Current task: {task}")
    if task.description:
        print(f"Description: {task.description}")
    
    print("\nEnter new values (leave blank to keep current value):")
    
    title = get_user_input(f"Title [{task.title}]: ")
    description = get_user_input(f"Description [{task.description}]: ")
    
    while True:
        due_date = get_user_input(f"Due date [{task.due_date}] (YYYY-MM-DD): ")
        if validate_date(due_date):
            break
        print("Invalid date format. Please use YYYY-MM-DD format.")
    
    # Only update fields that were provided
    updates = {}
    if title:
        updates["title"] = title
    if description:
        updates["description"] = description
    if due_date:
        updates["due_date"] = due_date
    
    if updates:
        task_manager.update_task(task_id, **updates)
        print("Task updated successfully.")
    else:
        print("No changes made.")


def mark_task_complete_ui(task_manager):
    """
    User interface for marking a task as complete.
    
    Args:
        task_manager (TaskManager): The task manager instance
    """
    print("\n----- Mark Task as Complete -----")
    
    try:
        task_id = int(get_user_input("Enter task ID: ", required=True))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    task = task_manager.get_task(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    
    if task.completed:
        choice = get_user_input("Task is already marked as complete. Mark as incomplete? (y/n): ")
        if choice.lower() == "y":
            task_manager.update_task(task_id, completed=False)
            print("Task marked as incomplete.")
    else:
        task_manager.update_task(task_id, completed=True)
        print("Task marked as complete.")


def delete_task_ui(task_manager):
    """
    User interface for deleting a task.
    
    Args:
        task_manager (TaskManager): The task manager instance
    """
    print("\n----- Delete Task -----")
    
    try:
        task_id = int(get_user_input("Enter task ID: ", required=True))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    task = task_manager.get_task(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    
    print(f"Task to delete: {task}")
    
    confirm = get_user_input("Are you sure you want to delete this task? (y/n): ")
    if confirm.lower() == "y":
        task_manager.delete_task(task_id)
        print("Task deleted successfully.")
    else:
        print("Deletion cancelled.")


def main():
    """Main function to run the task manager application."""
    task_manager = TaskManager()
    
    print("Welcome to the Command-Line Task Manager!")
    
    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_task_ui(task_manager)
        elif choice == "2":
            view_tasks_ui(task_manager)
        elif choice == "3":
            update_task_ui(task_manager)
        elif choice == "4":
            mark_task_complete_ui(task_manager)
        elif choice == "5":
            delete_task_ui(task_manager)
        elif choice == "6":
            print("Thank you for using the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()