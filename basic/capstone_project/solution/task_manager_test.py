#!/usr/bin/env python3
"""
Test module for the Command-Line Task Manager application.

This module contains tests for the Task and TaskManager classes.
"""

import os
import unittest
from task_manager import Task, TaskManager


class TestTask(unittest.TestCase):
    """Test cases for the Task class."""
    
    def test_task_initialization(self):
        """Test that a Task object is initialized correctly."""
        task = Task(1, "Test Task", "Test Description", "2023-12-31", False)
        
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.due_date, "2023-12-31")
        self.assertEqual(task.completed, False)
    
    def test_task_string_representation(self):
        """Test the string representation of a Task."""
        task = Task(1, "Test Task", "Test Description", "2023-12-31", False)
        expected_str = "[✗] Task 1: Test Task (Due: 2023-12-31)"
        self.assertEqual(str(task), expected_str)
        
        task.completed = True
        expected_str = "[✓] Task 1: Test Task (Due: 2023-12-31)"
        self.assertEqual(str(task), expected_str)
        
        task = Task(2, "Another Task")
        expected_str = "[✗] Task 2: Another Task (Due: Not set)"
        self.assertEqual(str(task), expected_str)


class TestTaskManager(unittest.TestCase):
    """Test cases for the TaskManager class."""
    
    def setUp(self):
        """Set up the test environment."""
        # Use a test-specific data file
        self.test_file = "test_tasks.csv"
        self.task_manager = TaskManager(self.test_file)
    
    def tearDown(self):
        """Clean up after the tests."""
        # Remove the test file if it exists
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_task(self):
        """Test adding a task."""
        task = self.task_manager.add_task("Test Task", "Test Description", "2023-12-31")
        
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.due_date, "2023-12-31")
        self.assertEqual(task.completed, False)
        
        # Verify that the task was added to the task manager
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].task_id, 1)
        self.assertEqual(tasks[0].title, "Test Task")
    
    def test_get_task(self):
        """Test getting a task by ID."""
        # Add a task
        self.task_manager.add_task("Test Task", "Test Description", "2023-12-31")
        
        # Get the task by ID
        task = self.task_manager.get_task(1)
        
        # Verify that the task was retrieved correctly
        self.assertIsNotNone(task)
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.due_date, "2023-12-31")
        self.assertEqual(task.completed, False)
        
        # Try to get a non-existent task
        task = self.task_manager.get_task(999)
        self.assertIsNone(task)
    
    def test_update_task(self):
        """Test updating a task."""
        # Add a task
        self.task_manager.add_task("Test Task", "Test Description", "2023-12-31")
        
        # Update the task
        result = self.task_manager.update_task(1, title="Updated Task", description="Updated Description")
        
        # Verify that the update was successful
        self.assertTrue(result)
        
        # Get the updated task
        task = self.task_manager.get_task(1)
        
        # Verify that the task was updated correctly
        self.assertEqual(task.title, "Updated Task")
        self.assertEqual(task.description, "Updated Description")
        self.assertEqual(task.due_date, "2023-12-31")  # Unchanged
        self.assertEqual(task.completed, False)  # Unchanged
        
        # Try to update a non-existent task
        result = self.task_manager.update_task(999, title="Non-existent Task")
        self.assertFalse(result)
    
    def test_delete_task(self):
        """Test deleting a task."""
        # Add a task
        self.task_manager.add_task("Test Task", "Test Description", "2023-12-31")
        
        # Verify that the task exists
        self.assertEqual(len(self.task_manager.get_all_tasks()), 1)
        
        # Delete the task
        result = self.task_manager.delete_task(1)
        
        # Verify that the deletion was successful
        self.assertTrue(result)
        
        # Verify that the task was deleted
        self.assertEqual(len(self.task_manager.get_all_tasks()), 0)
        
        # Try to delete a non-existent task
        result = self.task_manager.delete_task(999)
        self.assertFalse(result)
    
    def test_get_all_tasks(self):
        """Test getting all tasks."""
        # Add multiple tasks
        self.task_manager.add_task("Task 1", "Description 1", "2023-12-31")
        self.task_manager.add_task("Task 2", "Description 2", "2023-12-31")
        self.task_manager.add_task("Task 3", "Description 3", "2023-12-31")
        
        # Get all tasks
        tasks = self.task_manager.get_all_tasks()
        
        # Verify that all tasks were retrieved
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")
        self.assertEqual(tasks[2].title, "Task 3")
    
    def test_get_completed_tasks(self):
        """Test getting completed tasks."""
        # Add both completed and incomplete tasks
        self.task_manager.add_task("Task 1", "Description 1", "2023-12-31")
        self.task_manager.add_task("Task 2", "Description 2", "2023-12-31")
        self.task_manager.add_task("Task 3", "Description 3", "2023-12-31")
        
        # Mark some tasks as completed
        self.task_manager.update_task(1, completed=True)
        self.task_manager.update_task(3, completed=True)
        
        # Get completed tasks
        completed_tasks = self.task_manager.get_completed_tasks()
        
        # Verify that only completed tasks were retrieved
        self.assertEqual(len(completed_tasks), 2)
        self.assertEqual(completed_tasks[0].task_id, 1)
        self.assertEqual(completed_tasks[1].task_id, 3)
    
    def test_get_incomplete_tasks(self):
        """Test getting incomplete tasks."""
        # Add both completed and incomplete tasks
        self.task_manager.add_task("Task 1", "Description 1", "2023-12-31")
        self.task_manager.add_task("Task 2", "Description 2", "2023-12-31")
        self.task_manager.add_task("Task 3", "Description 3", "2023-12-31")
        
        # Mark some tasks as completed
        self.task_manager.update_task(1, completed=True)
        self.task_manager.update_task(3, completed=True)
        
        # Get incomplete tasks
        incomplete_tasks = self.task_manager.get_incomplete_tasks()
        
        # Verify that only incomplete tasks were retrieved
        self.assertEqual(len(incomplete_tasks), 1)
        self.assertEqual(incomplete_tasks[0].task_id, 2)
    
    def test_save_and_load_tasks(self):
        """Test saving and loading tasks."""
        # Add tasks
        self.task_manager.add_task("Task 1", "Description 1", "2023-12-31")
        self.task_manager.add_task("Task 2", "Description 2", "2023-12-31")
        self.task_manager.update_task(1, completed=True)
        
        # Create a new TaskManager to load the tasks
        new_task_manager = TaskManager(self.test_file)
        
        # Verify that the tasks were loaded correctly
        tasks = new_task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        
        # Verify the details of the loaded tasks
        self.assertEqual(tasks[0].task_id, 1)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[0].description, "Description 1")
        self.assertEqual(tasks[0].due_date, "2023-12-31")
        self.assertEqual(tasks[0].completed, True)
        
        self.assertEqual(tasks[1].task_id, 2)
        self.assertEqual(tasks[1].title, "Task 2")
        self.assertEqual(tasks[1].description, "Description 2")
        self.assertEqual(tasks[1].due_date, "2023-12-31")
        self.assertEqual(tasks[1].completed, False)


if __name__ == "__main__":
    unittest.main()