"""
Test file for Task model - TDD Exercise

This file contains the first tests to get you started with TDD.
Follow the Red-Green-Refactor cycle:

1. RED: Write a failing test
2. GREEN: Write minimal code to make it pass
3. REFACTOR: Improve the code while keeping tests green

Start by uncommenting the first test and running it.
It should fail (RED) because the Task class doesn't exist yet.
Then implement the minimal Task class to make it pass (GREEN).
"""

import pytest
from datetime import datetime, date
from enum import Enum

# Uncomment this import once you create the task.py file
# from src.task import Task, Priority, TaskStatus


# TODO: Uncomment and run this test first
# def test_create_task_with_title():
#     """Test creating a task with just a title."""
#     task = Task("Buy groceries")
#     assert task.title == "Buy groceries"
#     assert task.description == ""
#     assert task.is_complete is False


# TODO: After the first test passes, uncomment and implement this test
# def test_create_task_with_description():
#     """Test creating a task with title and description."""
#     task = Task("Buy groceries", "Milk, bread, eggs")
#     assert task.title == "Buy groceries"
#     assert task.description == "Milk, bread, eggs"
#     assert task.is_complete is False


# TODO: Continue with these tests one by one
# def test_create_task_with_priority():
#     """Test creating a task with priority."""
#     task = Task("Important task", priority=Priority.HIGH)
#     assert task.priority == Priority.HIGH


# def test_task_default_priority():
#     """Test that tasks have medium priority by default."""
#     task = Task("Regular task")
#     assert task.priority == Priority.MEDIUM


# def test_mark_task_complete():
#     """Test marking a task as complete."""
#     task = Task("Complete me")
#     task.mark_complete()
#     assert task.is_complete is True


# def test_mark_task_incomplete():
#     """Test marking a task as incomplete."""
#     task = Task("Complete me")
#     task.mark_complete()
#     task.mark_incomplete()
#     assert task.is_complete is False


# def test_task_string_representation():
#     """Test task string representation."""
#     task = Task("Test task", "Test description")
#     expected = "Test task: Test description"
#     assert str(task) == expected


# def test_task_string_representation_no_description():
#     """Test task string representation without description."""
#     task = Task("Test task")
#     expected = "Test task"
#     assert str(task) == expected


# def test_task_equality():
#     """Test task equality comparison."""
#     task1 = Task("Same task", "Same description")
#     task2 = Task("Same task", "Same description")
#     task3 = Task("Different task", "Same description")
    
#     assert task1 == task2
#     assert task1 != task3


# def test_task_has_unique_id():
#     """Test that each task has a unique ID."""
#     task1 = Task("Task 1")
#     task2 = Task("Task 2")
    
#     assert task1.id != task2.id
#     assert isinstance(task1.id, str)
#     assert len(task1.id) > 0


# def test_task_creation_date():
#     """Test that task has creation date."""
#     task = Task("Test task")
#     assert isinstance(task.created_at, datetime)
#     assert task.created_at <= datetime.now()


# def test_task_due_date():
#     """Test setting task due date."""
#     due_date = date(2024, 12, 31)
#     task = Task("Task with due date", due_date=due_date)
#     assert task.due_date == due_date


# def test_task_category():
#     """Test setting task category."""
#     task = Task("Work task", category="Work")
#     assert task.category == "Work"


# def test_task_to_dict():
#     """Test converting task to dictionary."""
#     task = Task("Test task", "Test description", Priority.HIGH)
#     task_dict = task.to_dict()
    
#     assert task_dict["title"] == "Test task"
#     assert task_dict["description"] == "Test description"
#     assert task_dict["priority"] == "HIGH"
#     assert task_dict["is_complete"] is False
#     assert "id" in task_dict
#     assert "created_at" in task_dict


# def test_task_from_dict():
#     """Test creating task from dictionary."""
#     task_data = {
#         "id": "test-id",
#         "title": "Test task",
#         "description": "Test description",
#         "priority": "HIGH",
#         "is_complete": True,
#         "created_at": "2023-01-01T12:00:00",
#         "category": "Work",
#         "due_date": "2023-12-31"
#     }
    
#     task = Task.from_dict(task_data)
    
#     assert task.id == "test-id"
#     assert task.title == "Test task"
#     assert task.description == "Test description"
#     assert task.priority == Priority.HIGH
#     assert task.is_complete is True
#     assert task.category == "Work"


# Parametrized tests for comprehensive coverage
# @pytest.mark.parametrize("title,description,priority,expected_str", [
#     ("Task 1", "Description 1", Priority.LOW, "Task 1: Description 1"),
#     ("Task 2", "", Priority.MEDIUM, "Task 2"),
#     ("Task 3", "Long description here", Priority.HIGH, "Task 3: Long description here"),
# ])
# def test_task_string_representations(title, description, priority, expected_str):
#     """Test various task string representations."""
#     task = Task(title, description, priority)
#     assert str(task) == expected_str


# @pytest.mark.parametrize("priority", [Priority.LOW, Priority.MEDIUM, Priority.HIGH])
# def test_task_priority_values(priority):
#     """Test all priority values."""
#     task = Task("Test task", priority=priority)
#     assert task.priority == priority


# Fixtures for common test data
# @pytest.fixture
# def sample_task():
#     """Create a sample task for testing."""
#     return Task("Sample Task", "Sample description", Priority.MEDIUM)


# @pytest.fixture
# def completed_task():
#     """Create a completed task for testing."""
#     task = Task("Completed Task", "This task is done")
#     task.mark_complete()
#     return task


# @pytest.fixture
# def task_with_due_date():
#     """Create a task with due date for testing."""
#     return Task("Task with deadline", due_date=date(2024, 12, 31))


# Tests using fixtures
# def test_sample_task_properties(sample_task):
#     """Test sample task properties using fixture."""
#     assert sample_task.title == "Sample Task"
#     assert sample_task.description == "Sample description"
#     assert sample_task.priority == Priority.MEDIUM
#     assert not sample_task.is_complete


# def test_completed_task_status(completed_task):
#     """Test completed task status using fixture."""
#     assert completed_task.is_complete is True


# def test_task_due_date_fixture(task_with_due_date):
#     """Test task due date using fixture."""
#     assert task_with_due_date.due_date == date(2024, 12, 31)


# Edge cases and error handling
# def test_task_empty_title_raises_error():
#     """Test that empty title raises ValueError."""
#     with pytest.raises(ValueError, match="Title cannot be empty"):
#         Task("")


# def test_task_none_title_raises_error():
#     """Test that None title raises TypeError."""
#     with pytest.raises(TypeError):
#         Task(None)


# def test_task_invalid_priority_raises_error():
#     """Test that invalid priority raises ValueError."""
#     with pytest.raises(ValueError):
#         Task("Test task", priority="INVALID")


# TDD Instructions:
# 1. Uncomment the first test and run it - it should fail (RED)
# 2. Create src/task.py with minimal Task class to make it pass (GREEN)
# 3. Refactor if needed while keeping the test green
# 4. Uncomment the next test and repeat the cycle
# 5. Continue until all tests are implemented and passing

# Remember: Write only enough code to make the current test pass!