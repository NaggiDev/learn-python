#!/usr/bin/env python3
"""
Command-Line Task Manager

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
        # TODO: Implement loading tasks from the CSV file
        # If the file exists, read each row and create Task objects
        # Add the tasks to self.tasks
        pass
    
    def save_tasks(self):
        """Save tasks to the CSV file."""
        # TODO: Implement saving tasks to the CSV file
        # Write each task as a row in the CSV file
        pass
    
    def get_next_id(self):
        """
        Get the next available task ID.
        
        Returns:
            int: The next available task ID
        """
        # TODO: Implement getting the next available task ID
        # If there are no tasks, return 1
        # Otherwise, return the maximum task ID + 1
        return 1
    
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
        # TODO: Implement adding a new task
        # Create a new Task object with the next available ID
        # Add it to self.tasks
        # Save tasks to the file
        # Return the new task
        pass
    
    def get_task(self, task_id):
        """
        Get a task by ID.
        
        Args:
            task_id (int): ID of the task to get
            
        Returns:
            Task or None: The task with the given ID, or None if not found
        """
        # TODO: Implement getting a task by ID
        # Find the task with the given ID in self.tasks
        # Return the task or None if not found
        pass
    
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
        # TODO: Implement updating a task
        # Find the task with the given ID
        # Update the fields that are not None
        # Save tasks to the file
        # Return True if the task was found and updated, False otherwise
        pass
    
    def delete_task(self, task_id):
        """
        Delete a task.
        
        Args:
            task_id (int): ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False otherwise
        """
        # TODO: Implement deleting a task
        # Find the task with the given ID
        # Remove it from self.tasks
        # Save tasks to the file
        # Return True if the task was found and deleted, False otherwise
        pass
    
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
        # TODO: Implement getting all completed tasks
        # Return a list of tasks where completed is True
        pass
    
    def get_incomplete_tasks(self):
        """
        Get all incomplete tasks.
        
        Returns:
            list: List of incomplete tasks
        """
        # TODO: Implement getting all incomplete tasks
        # Return a list of tasks where completed is False
        pass


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
    
    # TODO: Implement the UI for adding a task
    # Get the title, description, and due date from the user
    # Validate the due date
    # Add the task using task_manager.add_task()
    # Display a confirmation message
    
    print("Task added successfully!")


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
    
    # TODO: Implement the UI for viewing tasks
    # Get the user's choice
    # Display the appropriate tasks based on the choice
    # If there are no tasks, display a message


def update_task_ui(task_manager):
    """
    User interface for updating a task.
    
    Args:
        task_manager (TaskManager): The task manager instance
    """
    print("\n----- Update Task -----")
    
    # TODO: Implement the UI for updating a task
    # Get the task ID from the user
    # Get the task using task_manager.get_task()
    # If the task doesn't exist, display an error message
    # Get the new values for the task fields
    # Update the task using task_manager.update_task()
    # Display a confirmation message


def mark_task_complete_ui(task_manager):
    """
    User interface for marking a task as complete.
    
    Args:
        task_manager (TaskManager): The task manager instance
    """
    print("\n----- Mark Task as Complete -----")
    
    # TODO: Implement the UI for marking a task as complete
    # Get the task ID from the user
    # Update the task's completed status using task_manager.update_task()
    # Display a confirmation message


def delete_task_ui(task_manager):
    """
    User interface for deleting a task.
    
    Args:
        task_manager (TaskManager): The task manager instance
    """
    print("\n----- Delete Task -----")
    
    # TODO: Implement the UI for deleting a task
    # Get the task ID from the user
    # Confirm that the user wants to delete the task
    # Delete the task using task_manager.delete_task()
    # Display a confirmation message


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