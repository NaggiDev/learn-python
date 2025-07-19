"""
Task Manager for the Task Manager TDD Project.

This module contains the TaskManager class that handles
collections of tasks and provides operations on them.
"""

from typing import List, Optional, Dict, Any
from .task import Task, Priority, TaskStatus


class TaskManager:
    """
    Manages a collection of tasks.
    
    Provides methods to add, remove, update, and query tasks.
    """
    
    def __init__(self) -> None:
        """Initialize an empty task manager."""
        self._tasks: Dict[str, Task] = {}
    
    def add_task(self, task: Task) -> None:
        """
        Add a task to the manager.
        
        Args:
            task: Task instance to add
            
        Raises:
            ValueError: If task with same ID already exists
        """
        if task.id in self._tasks:
            raise ValueError(f"Task with ID {task.id} already exists")
        
        self._tasks[task.id] = task
    
    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: ID of the task to retrieve
            
        Returns:
            Task instance if found, None otherwise
        """
        return self._tasks.get(task_id)
    
    def get_tasks(self, status: Optional[TaskStatus] = None) -> List[Task]:
        """
        Get all tasks, optionally filtered by status.
        
        Args:
            status: Optional status filter
            
        Returns:
            List of tasks matching the criteria
        """
        tasks = list(self._tasks.values())
        
        if status is not None:
            tasks = [task for task in tasks if task.status == status]
        
        return tasks
    
    def complete_task(self, task_id: str) -> bool:
        """
        Mark a task as complete by ID.
        
        Args:
            task_id: ID of the task to complete
            
        Returns:
            True if task was found and completed, False otherwise
        """
        task = self._tasks.get(task_id)
        if task is None:
            return False
        
        task.mark_complete()
        return True
    
    def incomplete_task(self, task_id: str) -> bool:
        """
        Mark a task as incomplete by ID.
        
        Args:
            task_id: ID of the task to mark incomplete
            
        Returns:
            True if task was found and marked incomplete, False otherwise
        """
        task = self._tasks.get(task_id)
        if task is None:
            return False
        
        task.mark_incomplete()
        return True
    
    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by ID.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if task was found and deleted, False otherwise
        """
        if task_id not in self._tasks:
            return False
        
        del self._tasks[task_id]
        return True
    
    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description.
        
        Args:
            keyword: Keyword to search for (case-insensitive)
            
        Returns:
            List of tasks containing the keyword
        """
        if not keyword:
            return []
        
        keyword_lower = keyword.lower()
        matching_tasks = []
        
        for task in self._tasks.values():
            if (keyword_lower in task.title.lower() or 
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)
        
        return matching_tasks
    
    def get_tasks_by_category(self, category: str) -> List[Task]:
        """
        Get all tasks in a specific category.
        
        Args:
            category: Category to filter by
            
        Returns:
            List of tasks in the specified category
        """
        return [
            task for task in self._tasks.values()
            if task.category.lower() == category.lower()
        ]
    
    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """
        Get all tasks with a specific priority.
        
        Args:
            priority: Priority level to filter by
            
        Returns:
            List of tasks with the specified priority
        """
        return [
            task for task in self._tasks.values()
            if task.priority == priority
        ]
    
    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all overdue tasks.
        
        Returns:
            List of tasks that are overdue
        """
        return [
            task for task in self._tasks.values()
            if task.is_overdue()
        ]
    
    def get_task_count(self) -> int:
        """
        Get the total number of tasks.
        
        Returns:
            Total number of tasks in the manager
        """
        return len(self._tasks)
    
    def get_completed_count(self) -> int:
        """
        Get the number of completed tasks.
        
        Returns:
            Number of completed tasks
        """
        return len([task for task in self._tasks.values() if task.is_complete])
    
    def get_pending_count(self) -> int:
        """
        Get the number of pending tasks.
        
        Returns:
            Number of pending tasks
        """
        return len([task for task in self._tasks.values() if not task.is_complete])
    
    def clear_completed_tasks(self) -> int:
        """
        Remove all completed tasks.
        
        Returns:
            Number of tasks that were removed
        """
        completed_ids = [
            task.id for task in self._tasks.values()
            if task.is_complete
        ]
        
        for task_id in completed_ids:
            del self._tasks[task_id]
        
        return len(completed_ids)
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about the tasks.
        
        Returns:
            Dictionary containing various statistics
        """
        total = self.get_task_count()
        completed = self.get_completed_count()
        pending = self.get_pending_count()
        overdue = len(self.get_overdue_tasks())
        
        # Count by priority
        priority_counts = {
            Priority.LOW: len(self.get_tasks_by_priority(Priority.LOW)),
            Priority.MEDIUM: len(self.get_tasks_by_priority(Priority.MEDIUM)),
            Priority.HIGH: len(self.get_tasks_by_priority(Priority.HIGH)),
        }
        
        # Count by category
        categories = set(task.category for task in self._tasks.values() if task.category)
        category_counts = {
            category: len(self.get_tasks_by_category(category))
            for category in categories
        }
        
        return {
            "total_tasks": total,
            "completed_tasks": completed,
            "pending_tasks": pending,
            "overdue_tasks": overdue,
            "completion_rate": (completed / total * 100) if total > 0 else 0,
            "priority_counts": {p.value: count for p, count in priority_counts.items()},
            "category_counts": category_counts,
        }