"""
Complete test suite for Task model - TDD Solution

This file demonstrates the complete TDD process for the Task class.
All tests follow the Red-Green-Refactor cycle.
"""

import pytest
from datetime import datetime, date
from src.task import Task, Priority, TaskStatus


class TestTaskCreation:
    """Test task creation and initialization."""
    
    def test_create_task_with_title(self):
        """Test creating a task with just a title."""
        task = Task("Buy groceries")
        assert task.title == "Buy groceries"
        assert task.description == ""
        assert task.is_complete is False
    
    def test_create_task_with_description(self):
        """Test creating a task with title and description."""
        task = Task("Buy groceries", "Milk, bread, eggs")
        assert task.title == "Buy groceries"
        assert task.description == "Milk, bread, eggs"
        assert task.is_complete is False
    
    def test_create_task_with_priority(self):
        """Test creating a task with priority."""
        task = Task("Important task", priority=Priority.HIGH)
        assert task.priority == Priority.HIGH
    
    def test_task_default_priority(self):
        """Test that tasks have medium priority by default."""
        task = Task("Regular task")
        assert task.priority == Priority.MEDIUM
    
    def test_task_has_unique_id(self):
        """Test that each task has a unique ID."""
        task1 = Task("Task 1")
        task2 = Task("Task 2")
        
        assert task1.id != task2.id
        assert isinstance(task1.id, str)
        assert len(task1.id) > 0
    
    def test_task_creation_date(self):
        """Test that task has creation date."""
        task = Task("Test task")
        assert isinstance(task.created_at, datetime)
        assert task.created_at <= datetime.now()
    
    def test_task_due_date(self):
        """Test setting task due date."""
        due_date = date(2024, 12, 31)
        task = Task("Task with due date", due_date=due_date)
        assert task.due_date == due_date
    
    def test_task_category(self):
        """Test setting task category."""
        task = Task("Work task", category="Work")
        assert task.category == "Work"


class TestTaskCompletion:
    """Test task completion functionality."""
    
    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = Task("Complete me")
        task.mark_complete()
        assert task.is_complete is True
    
    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        task = Task("Complete me")
        task.mark_complete()
        task.mark_incomplete()
        assert task.is_complete is False
    
    def test_task_status_property(self):
        """Test task status property."""
        task = Task("Test task")
        assert task.status == TaskStatus.PENDING
        
        task.mark_complete()
        assert task.status == TaskStatus.COMPLETED


class TestTaskRepresentation:
    """Test task string representation and equality."""
    
    def test_task_string_representation(self):
        """Test task string representation."""
        task = Task("Test task", "Test description")
        expected = "Test task: Test description"
        assert str(task) == expected
    
    def test_task_string_representation_no_description(self):
        """Test task string representation without description."""
        task = Task("Test task")
        expected = "Test task"
        assert str(task) == expected
    
    def test_task_equality(self):
        """Test task equality comparison."""
        task1 = Task("Same task", "Same description")
        task2 = Task("Same task", "Same description")
        task3 = Task("Different task", "Same description")
        
        assert task1 == task2
        assert task1 != task3
    
    def test_task_equality_different_types(self):
        """Test task equality with different types."""
        task = Task("Test task")
        assert task != "Test task"
        assert task != 42
        assert task != None


class TestTaskSerialization:
    """Test task serialization and deserialization."""
    
    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task("Test task", "Test description", Priority.HIGH)
        task_dict = task.to_dict()
        
        assert task_dict["title"] == "Test task"
        assert task_dict["description"] == "Test description"
        assert task_dict["priority"] == "HIGH"
        assert task_dict["is_complete"] is False
        assert "id" in task_dict
        assert "created_at" in task_dict
    
    def test_task_from_dict(self):
        """Test creating task from dictionary."""
        task_data = {
            "id": "test-id",
            "title": "Test task",
            "description": "Test description",
            "priority": "HIGH",
            "is_complete": True,
            "created_at": "2023-01-01T12:00:00",
            "category": "Work",
            "due_date": "2023-12-31"
        }
        
        task = Task.from_dict(task_data)
        
        assert task.id == "test-id"
        assert task.title == "Test task"
        assert task.description == "Test description"
        assert task.priority == Priority.HIGH
        assert task.is_complete is True
        assert task.category == "Work"
    
    def test_task_from_dict_minimal(self):
        """Test creating task from minimal dictionary."""
        task_data = {"title": "Minimal task"}
        task = Task.from_dict(task_data)
        
        assert task.title == "Minimal task"
        assert task.description == ""
        assert task.priority == Priority.MEDIUM


class TestTaskDueDates:
    """Test task due date functionality."""
    
    def test_task_is_overdue(self):
        """Test checking if task is overdue."""
        past_date = date(2020, 1, 1)
        task = Task("Overdue task", due_date=past_date)
        assert task.is_overdue() is True
    
    def test_task_not_overdue(self):
        """Test task that is not overdue."""
        future_date = date(2030, 12, 31)
        task = Task("Future task", due_date=future_date)
        assert task.is_overdue() is False
    
    def test_completed_task_not_overdue(self):
        """Test that completed tasks are not considered overdue."""
        past_date = date(2020, 1, 1)
        task = Task("Completed task", due_date=past_date)
        task.mark_complete()
        assert task.is_overdue() is False
    
    def test_task_no_due_date_not_overdue(self):
        """Test that tasks without due date are not overdue."""
        task = Task("No due date task")
        assert task.is_overdue() is False
    
    def test_days_until_due(self):
        """Test calculating days until due date."""
        future_date = date.today().replace(day=date.today().day + 5)
        task = Task("Future task", due_date=future_date)
        assert task.days_until_due() == 5
    
    def test_days_until_due_no_date(self):
        """Test days until due with no due date."""
        task = Task("No due date")
        assert task.days_until_due() is None


class TestTaskValidation:
    """Test task input validation and error handling."""
    
    def test_task_empty_title_raises_error(self):
        """Test that empty title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Task("")
    
    def test_task_whitespace_title_raises_error(self):
        """Test that whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Task("   ")
    
    def test_task_none_title_raises_error(self):
        """Test that None title raises TypeError."""
        with pytest.raises(TypeError, match="Title cannot be None"):
            Task(None)
    
    def test_task_title_stripped(self):
        """Test that task title is stripped of whitespace."""
        task = Task("  Test task  ")
        assert task.title == "Test task"


# Parametrized tests for comprehensive coverage
@pytest.mark.parametrize("title,description,priority,expected_str", [
    ("Task 1", "Description 1", Priority.LOW, "Task 1: Description 1"),
    ("Task 2", "", Priority.MEDIUM, "Task 2"),
    ("Task 3", "Long description here", Priority.HIGH, "Task 3: Long description here"),
])
def test_task_string_representations(title, description, priority, expected_str):
    """Test various task string representations."""
    task = Task(title, description, priority)
    assert str(task) == expected_str


@pytest.mark.parametrize("priority", [Priority.LOW, Priority.MEDIUM, Priority.HIGH])
def test_task_priority_values(priority):
    """Test all priority values."""
    task = Task("Test task", priority=priority)
    assert task.priority == priority


# Fixtures for common test data
@pytest.fixture
def sample_task():
    """Create a sample task for testing."""
    return Task("Sample Task", "Sample description", Priority.MEDIUM)


@pytest.fixture
def completed_task():
    """Create a completed task for testing."""
    task = Task("Completed Task", "This task is done")
    task.mark_complete()
    return task


@pytest.fixture
def task_with_due_date():
    """Create a task with due date for testing."""
    return Task("Task with deadline", due_date=date(2024, 12, 31))


@pytest.fixture
def overdue_task():
    """Create an overdue task for testing."""
    return Task("Overdue task", due_date=date(2020, 1, 1))


# Tests using fixtures
def test_sample_task_properties(sample_task):
    """Test sample task properties using fixture."""
    assert sample_task.title == "Sample Task"
    assert sample_task.description == "Sample description"
    assert sample_task.priority == Priority.MEDIUM
    assert not sample_task.is_complete


def test_completed_task_status(completed_task):
    """Test completed task status using fixture."""
    assert completed_task.is_complete is True
    assert completed_task.status == TaskStatus.COMPLETED


def test_task_due_date_fixture(task_with_due_date):
    """Test task due date using fixture."""
    assert task_with_due_date.due_date == date(2024, 12, 31)


def test_overdue_task_fixture(overdue_task):
    """Test overdue task using fixture."""
    assert overdue_task.is_overdue() is True


# Integration tests
def test_task_complete_workflow():
    """Test complete task workflow from creation to completion."""
    # Create task
    task = Task("Complete workflow", "Test the entire workflow")
    assert not task.is_complete
    assert task.status == TaskStatus.PENDING
    
    # Complete task
    task.mark_complete()
    assert task.is_complete
    assert task.status == TaskStatus.COMPLETED
    
    # Mark incomplete again
    task.mark_incomplete()
    assert not task.is_complete
    assert task.status == TaskStatus.PENDING


def test_task_serialization_roundtrip():
    """Test task serialization and deserialization roundtrip."""
    original_task = Task(
        "Test task",
        "Test description",
        Priority.HIGH,
        "Work",
        date(2024, 12, 31)
    )
    original_task.mark_complete()
    
    # Serialize to dict
    task_dict = original_task.to_dict()
    
    # Deserialize from dict
    restored_task = Task.from_dict(task_dict)
    
    # Verify all properties match
    assert restored_task.title == original_task.title
    assert restored_task.description == original_task.description
    assert restored_task.priority == original_task.priority
    assert restored_task.category == original_task.category
    assert restored_task.due_date == original_task.due_date
    assert restored_task.is_complete == original_task.is_complete