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
        # TODO: Implement this test
        # Add a task and verify that it was added correctly
        pass
    
    def test_get_task(self):
        """Test getting a task by ID."""
        # TODO: Implement this test
        # Add a task, then get it by ID and verify that it's the same task
        pass
    
    def test_update_task(self):
        """Test updating a task."""
        # TODO: Implement this test
        # Add a task, update it, and verify that it was updated correctly
        pass
    
    def test_delete_task(self):
        """Test deleting a task."""
        # TODO: Implement this test
        # Add a task, delete it, and verify that it was deleted
        pass
    
    def test_get_all_tasks(self):
        """Test getting all tasks."""
        # TODO: Implement this test
        # Add multiple tasks and verify that get_all_tasks returns all of them
        pass
    
    def test_get_completed_tasks(self):
        """Test getting completed tasks."""
        # TODO: Implement this test
        # Add both completed and incomplete tasks
        # Verify that get_completed_tasks returns only the completed ones
        pass
    
    def test_get_incomplete_tasks(self):
        """Test getting incomplete tasks."""
        # TODO: Implement this test
        # Add both completed and incomplete tasks
        # Verify that get_incomplete_tasks returns only the incomplete ones
        pass
    
    def test_save_and_load_tasks(self):
        """Test saving and loading tasks."""
        # TODO: Implement this test
        # Add tasks, save them, create a new TaskManager, and verify that the tasks were loaded
        pass


if __name__ == "__main__":
    unittest.main()