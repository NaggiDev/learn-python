"""
Task model for the Task Manager TDD Project.

This module contains the Task class and related enums.
Built using Test-Driven Development methodology.
"""

import uuid
from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, Optional


class Priority(Enum):
    """Task priority levels."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class TaskStatus(Enum):
    """Task status values."""
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class Task:
    """
    Represents a single task with metadata.
    
    A task has a title, optional description, priority level,
    completion status, and various metadata fields.
    """
    
    def __init__(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        category: str = "",
        due_date: Optional[date] = None
    ) -> None:
        """
        Initialize a new task.
        
        Args:
            title: Task title (required, cannot be empty)
            description: Optional task description
            priority: Task priority level
            category: Optional task category
            due_date: Optional due date
            
        Raises:
            ValueError: If title is empty
            TypeError: If title is None
        """
        if title is None:
            raise TypeError("Title cannot be None")
        if not title.strip():
            raise ValueError("Title cannot be empty")
        
        self.id = str(uuid.uuid4())
        self.title = title.strip()
        self.description = description
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.is_complete = False
        self.created_at = datetime.now()
    
    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.is_complete = True
    
    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.is_complete = False
    
    def __str__(self) -> str:
        """
        Return string representation of the task.
        
        Returns:
            String in format "title: description" or just "title" if no description
        """
        if self.description:
            return f"{self.title}: {self.description}"
        return self.title
    
    def __eq__(self, other: object) -> bool:
        """
        Check equality with another task.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if tasks have same title and description
        """
        if not isinstance(other, Task):
            return False
        return (
            self.title == other.title and
            self.description == other.description
        )
    
    def __hash__(self) -> int:
        """Return hash of the task based on ID."""
        return hash(self.id)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert task to dictionary for serialization.
        
        Returns:
            Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority.value,
            "category": self.category,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "is_complete": self.is_complete,
            "created_at": self.created_at.isoformat(),
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """
        Create task from dictionary.
        
        Args:
            data: Dictionary containing task data
            
        Returns:
            Task instance created from dictionary data
            
        Raises:
            KeyError: If required fields are missing
            ValueError: If data is invalid
        """
        # Create task with required fields
        task = cls(
            title=data["title"],
            description=data.get("description", ""),
            priority=Priority(data.get("priority", "MEDIUM")),
            category=data.get("category", ""),
        )
        
        # Set optional fields
        if "id" in data:
            task.id = data["id"]
        
        if "is_complete" in data:
            task.is_complete = data["is_complete"]
        
        if "created_at" in data:
            task.created_at = datetime.fromisoformat(data["created_at"])
        
        if "due_date" in data and data["due_date"]:
            task.due_date = date.fromisoformat(data["due_date"])
        
        return task
    
    @property
    def status(self) -> TaskStatus:
        """
        Get the current status of the task.
        
        Returns:
            TaskStatus enum value
        """
        return TaskStatus.COMPLETED if self.is_complete else TaskStatus.PENDING
    
    def is_overdue(self) -> bool:
        """
        Check if the task is overdue.
        
        Returns:
            True if task has due date and it's in the past, False otherwise
        """
        if self.due_date is None or self.is_complete:
            return False
        return self.due_date < date.today()
    
    def days_until_due(self) -> Optional[int]:
        """
        Calculate days until due date.
        
        Returns:
            Number of days until due date, None if no due date set
        """
        if self.due_date is None:
            return None
        
        delta = self.due_date - date.today()
        return delta.days