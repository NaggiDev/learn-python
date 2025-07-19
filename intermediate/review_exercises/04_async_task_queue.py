"""
Async Task Queue System - Review Exercise

This exercise combines multiple intermediate concepts while introducing asynchronous programming:
- Object-oriented programming (classes, inheritance, composition)
- Functional programming patterns (decorators, higher-order functions)
- Module organization and package structure
- Testing and debugging practices
- Introduction to asynchronous programming and event loops (advanced topic)

Requirements:
1. Create an AsyncTaskQueue system that can:
   - Queue tasks for asynchronous execution
   - Support different task priorities and scheduling
   - Implement worker pools for concurrent task processing
   - Provide task status tracking and result retrieval
   - Handle task failures and retry mechanisms
   - Support task dependencies and chaining
   - Implement rate limiting and throttling

2. Implement proper OOP design with abstract base classes
3. Use decorators for task registration and configuration
4. Include comprehensive test coverage with async testing
5. Demonstrate functional programming concepts with async patterns

This bridges to advanced concepts by introducing:
- Asynchronous programming with async/await
- Event loops and coroutines
- Concurrent task execution patterns
- Producer-consumer patterns with async queues
"""

import asyncio
import time
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, Union, Coroutine
import logging
import json


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class TaskStatus(Enum):
    """Task status enumeration."""
    PENDING = "pending"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    RETRYING = "retrying"


class TaskPriority(Enum):
    """Task priority levels."""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class TaskResult:
    """Result of task execution."""
    task_id: str
    status: TaskStatus
    result: Any = None
    error: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    execution_time: float = 0.0
    retry_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TaskConfig:
    """Configuration for task execution."""
    max_retries: int = 3
    retry_delay: float = 1.0
    timeout: Optional[float] = None
    priority: TaskPriority = TaskPriority.NORMAL
    dependencies: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class TaskException(Exception):
    """Base exception for task-related errors."""
    
    def __init__(self, message: str, task_id: str = None):
        super().__init__(message)
        self.task_id = task_id


class TaskTimeoutException(TaskException):
    """Exception for task timeout errors."""
    pass


class TaskDependencyException(TaskException):
    """Exception for task dependency errors."""
    pass


def async_task_decorator(priority: TaskPriority = TaskPriority.NORMAL,
                        max_retries: int = 3,
                        timeout: Optional[float] = None) -> Callable:
    """
    Decorator to mark functions as async tasks.
    
    Args:
        priority: Task priority level
        max_retries: Maximum retry attempts
        timeout: Task timeout in seconds
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        # TODO: Implement async task decorator
        # - Mark function as async task
        # - Store task configuration
        # - Preserve function metadata
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        
        # Add task metadata
        wrapper._is_async_task = True
        wrapper._task_config = TaskConfig(
            priority=priority,
            max_retries=max_retries,
            timeout=timeout
        )
        
        return wrapper
    return decorator


def retry_decorator(max_attempts: int = 3, delay: float = 1.0, 
                   backoff_factor: float = 2.0) -> Callable:
    """
    Decorator for retrying failed async operations.
    
    Args:
        max_attempts: Maximum retry attempts
        delay: Initial delay between retries
        backoff_factor: Exponential backoff factor
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        # TODO: Implement async retry decorator
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        await asyncio.sleep(current_delay)
                        current_delay *= backoff_factor
                    else:
                        raise last_exception
            
        return wrapper
    return decorator


def rate_limit_decorator(calls_per_second: float = 1.0) -> Callable:
    """
    Decorator to implement rate limiting for async functions.
    
    Args:
        calls_per_second: Maximum calls per second
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        # TODO: Implement async rate limiting decorator
        last_called = 0.0
        min_interval = 1.0 / calls_per_second
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            nonlocal last_called
            current_time = time.time()
            time_since_last = current_time - last_called
            
            if time_since_last < min_interval:
                await asyncio.sleep(min_interval - time_since_last)
            
            last_called = time.time()
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator


class AsyncTask:
    """Represents an asynchronous task."""
    
    def __init__(self, task_id: str, func: Callable, args: tuple = (), 
                 kwargs: dict = None, config: TaskConfig = None):
        """
        Initialize async task.
        
        Args:
            task_id: Unique task identifier
            func: Function to execute
            args: Function arguments
            kwargs: Function keyword arguments
            config: Task configuration
        """
        # TODO: Implement async task initialization
        self.task_id = task_id
        self.func = func
        self.args = args
        self.kwargs = kwargs or {}
        self.config = config or TaskConfig()
        self.status = TaskStatus.PENDING
        self.result = None
        self.error = None
        self.created_at = datetime.now()
        self.started_at = None
        self.completed_at = None
        self.retry_count = 0
    
    async def execute(self) -> TaskResult:
        """
        Execute the task.
        
        Returns:
            Task execution result
        """
        # TODO: Implement task execution
        self.status = TaskStatus.RUNNING
        self.started_at = datetime.now()
        
        try:
            # Handle timeout if specified
            if self.config.timeout:
                result = await asyncio.wait_for(
                    self.func(*self.args, **self.kwargs),
                    timeout=self.config.timeout
                )
            else:
                result = await self.func(*self.args, **self.kwargs)
            
            self.result = result
            self.status = TaskStatus.COMPLETED
            self.completed_at = datetime.now()
            
        except asyncio.TimeoutError:
            self.error = f"Task timed out after {self.config.timeout} seconds"
            self.status = TaskStatus.FAILED
            self.completed_at = datetime.now()
            
        except Exception as e:
            self.error = str(e)
            self.status = TaskStatus.FAILED
            self.completed_at = datetime.now()
        
        return self.get_result()
    
    def get_result(self) -> TaskResult:
        """Get task execution result."""
        # TODO: Implement result retrieval
        execution_time = 0.0
        if self.started_at and self.completed_at:
            execution_time = (self.completed_at - self.started_at).total_seconds()
        
        return TaskResult(
            task_id=self.task_id,
            status=self.status,
            result=self.result,
            error=self.error,
            start_time=self.started_at,
            end_time=self.completed_at,
            execution_time=execution_time,
            retry_count=self.retry_count,
            metadata=self.config.metadata
        )
    
    def can_retry(self) -> bool:
        """Check if task can be retried."""
        return (self.status == TaskStatus.FAILED and 
                self.retry_count < self.config.max_retries)
    
    def reset_for_retry(self) -> None:
        """Reset task for retry attempt."""
        # TODO: Implement retry reset
        self.status = TaskStatus.PENDING
        self.result = None
        self.error = None
        self.started_at = None
        self.completed_at = None
        self.retry_count += 1
    
    def __lt__(self, other: 'AsyncTask') -> bool:
        """Compare tasks for priority queue ordering."""
        # Higher priority values come first
        return self.config.priority.value > other.config.priority.value


class TaskQueue:
    """Asynchronous task queue with priority support."""
    
    def __init__(self, maxsize: int = 0):
        """
        Initialize task queue.
        
        Args:
            maxsize: Maximum queue size (0 for unlimited)
        """
        # TODO: Implement task queue initialization
        self.queue = asyncio.PriorityQueue(maxsize=maxsize)
        self.tasks: Dict[str, AsyncTask] = {}
        self.completed_tasks: Dict[str, TaskResult] = {}
        self.logger = logging.getLogger("task_queue")
    
    async def put_task(self, task: AsyncTask) -> None:
        """
        Add a task to the queue.
        
        Args:
            task: Task to add
        """
        # TODO: Implement task queuing
        task.status = TaskStatus.QUEUED
        self.tasks[task.task_id] = task
        
        # Use negative priority for correct ordering (higher priority first)
        priority_value = -task.config.priority.value
        await self.queue.put((priority_value, task.created_at, task))
        
        self.logger.info(f"Task {task.task_id} queued with priority {task.config.priority.name}")
    
    async def get_task(self) -> AsyncTask:
        """
        Get the next task from the queue.
        
        Returns:
            Next task to execute
        """
        # TODO: Implement task retrieval
        _, _, task = await self.queue.get()
        return task
    
    def task_done(self) -> None:
        """Mark a task as done."""
        self.queue.task_done()
    
    async def join(self) -> None:
        """Wait for all tasks to be processed."""
        await self.queue.join()
    
    def get_task_status(self, task_id: str) -> Optional[TaskStatus]:
        """Get status of a specific task."""
        # TODO: Implement task status retrieval
        if task_id in self.tasks:
            return self.tasks[task_id].status
        elif task_id in self.completed_tasks:
            return self.completed_tasks[task_id].status
        return None
    
    def get_task_result(self, task_id: str) -> Optional[TaskResult]:
        """Get result of a completed task."""
        # TODO: Implement task result retrieval
        if task_id in self.completed_tasks:
            return self.completed_tasks[task_id]
        elif task_id in self.tasks:
            return self.tasks[task_id].get_result()
        return None
    
    def get_queue_stats(self) -> Dict[str, Any]:
        """Get queue statistics."""
        # TODO: Implement queue statistics
        pending_count = sum(1 for task in self.tasks.values() 
                          if task.status in [TaskStatus.PENDING, TaskStatus.QUEUED])
        running_count = sum(1 for task in self.tasks.values() 
                          if task.status == TaskStatus.RUNNING)
        completed_count = len(self.completed_tasks)
        failed_count = sum(1 for result in self.completed_tasks.values() 
                         if result.status == TaskStatus.FAILED)
        
        return {
            "pending_tasks": pending_count,
            "running_tasks": running_count,
            "completed_tasks": completed_count,
            "failed_tasks": failed_count,
            "total_tasks": len(self.tasks) + len(self.completed_tasks),
            "queue_size": self.queue.qsize()
        }


class TaskWorker:
    """Worker that processes tasks from the queue."""
    
    def __init__(self, worker_id: str, task_queue: TaskQueue):
        """
        Initialize task worker.
        
        Args:
            worker_id: Unique worker identifier
            task_queue: Task queue to process
        """
        # TODO: Implement worker initialization
        self.worker_id = worker_id
        self.task_queue = task_queue
        self.is_running = False
        self.current_task = None
        self.processed_count = 0
        self.logger = logging.getLogger(f"worker.{worker_id}")
    
    async def start(self) -> None:
        """Start the worker."""
        # TODO: Implement worker start
        self.is_running = True
        self.logger.info(f"Worker {self.worker_id} started")
        
        while self.is_running:
            try:
                # Get next task from queue
                task = await self.task_queue.get_task()
                self.current_task = task
                
                self.logger.info(f"Worker {self.worker_id} processing task {task.task_id}")
                
                # Execute task with retry logic
                result = await self._execute_task_with_retry(task)
                
                # Store result
                self.task_queue.completed_tasks[task.task_id] = result
                if task.task_id in self.task_queue.tasks:
                    del self.task_queue.tasks[task.task_id]
                
                self.processed_count += 1
                self.current_task = None
                
                # Mark task as done in queue
                self.task_queue.task_done()
                
                self.logger.info(f"Worker {self.worker_id} completed task {task.task_id}")
                
            except asyncio.CancelledError:
                self.logger.info(f"Worker {self.worker_id} cancelled")
                break
            except Exception as e:
                self.logger.error(f"Worker {self.worker_id} error: {str(e)}")
                if self.current_task:
                    self.task_queue.task_done()
    
    async def _execute_task_with_retry(self, task: AsyncTask) -> TaskResult:
        """Execute task with retry logic."""
        # TODO: Implement task execution with retry
        while True:
            result = await task.execute()
            
            if result.status == TaskStatus.COMPLETED:
                return result
            elif result.status == TaskStatus.FAILED and task.can_retry():
                self.logger.warning(f"Task {task.task_id} failed, retrying ({task.retry_count + 1}/{task.config.max_retries})")
                
                # Wait before retry
                if task.config.retry_delay > 0:
                    await asyncio.sleep(task.config.retry_delay)
                
                task.reset_for_retry()
                task.status = TaskStatus.RETRYING
            else:
                return result
    
    def stop(self) -> None:
        """Stop the worker."""
        # TODO: Implement worker stop
        self.is_running = False
        self.logger.info(f"Worker {self.worker_id} stopping")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get worker statistics."""
        # TODO: Implement worker statistics
        return {
            "worker_id": self.worker_id,
            "is_running": self.is_running,
            "processed_count": self.processed_count,
            "current_task": self.current_task.task_id if self.current_task else None
        }


class AsyncTaskManager:
    """Main task manager that orchestrates the async task system."""
    
    def __init__(self, max_workers: int = 4, queue_size: int = 0):
        """
        Initialize async task manager.
        
        Args:
            max_workers: Maximum number of worker tasks
            queue_size: Maximum queue size (0 for unlimited)
        """
        # TODO: Implement task manager initialization
        self.max_workers = max_workers
        self.task_queue = TaskQueue(maxsize=queue_size)
        self.workers: List[TaskWorker] = []
        self.worker_tasks: List[asyncio.Task] = []
        self.is_running = False
        self.logger = logging.getLogger("task_manager")
        self.task_registry: Dict[str, Callable] = {}
    
    def register_task_function(self, name: str, func: Callable) -> None:
        """
        Register a function as a task.
        
        Args:
            name: Task name
            func: Function to register
        """
        # TODO: Implement task function registration
        self.task_registry[name] = func
        self.logger.info(f"Registered task function: {name}")
    
    async def submit_task(self, func: Union[str, Callable], *args, 
                         task_id: str = None, config: TaskConfig = None, 
                         **kwargs) -> str:
        """
        Submit a task for execution.
        
        Args:
            func: Function to execute or registered task name
            args: Function arguments
            task_id: Optional task ID (generated if not provided)
            config: Task configuration
            kwargs: Function keyword arguments
            
        Returns:
            Task ID
        """
        # TODO: Implement task submission
        if task_id is None:
            task_id = str(uuid.uuid4())
        
        # Resolve function if string name provided
        if isinstance(func, str):
            if func not in self.task_registry:
                raise ValueError(f"Task function '{func}' not registered")
            func = self.task_registry[func]
        
        # Create task
        task = AsyncTask(task_id, func, args, kwargs, config)
        
        # Add to queue
        await self.task_queue.put_task(task)
        
        self.logger.info(f"Submitted task {task_id}")
        return task_id
    
    async def start(self) -> None:
        """Start the task manager and workers."""
        # TODO: Implement task manager start
        if self.is_running:
            return
        
        self.is_running = True
        self.logger.info(f"Starting task manager with {self.max_workers} workers")
        
        # Create and start workers
        for i in range(self.max_workers):
            worker = TaskWorker(f"worker-{i}", self.task_queue)
            self.workers.append(worker)
            
            # Start worker as asyncio task
            worker_task = asyncio.create_task(worker.start())
            self.worker_tasks.append(worker_task)
        
        self.logger.info("Task manager started")
    
    async def stop(self) -> None:
        """Stop the task manager and workers."""
        # TODO: Implement task manager stop
        if not self.is_running:
            return
        
        self.logger.info("Stopping task manager")
        self.is_running = False
        
        # Stop workers
        for worker in self.workers:
            worker.stop()
        
        # Cancel worker tasks
        for worker_task in self.worker_tasks:
            worker_task.cancel()
        
        # Wait for workers to finish
        await asyncio.gather(*self.worker_tasks, return_exceptions=True)
        
        self.workers.clear()
        self.worker_tasks.clear()
        
        self.logger.info("Task manager stopped")
    
    async def wait_for_completion(self) -> None:
        """Wait for all tasks to complete."""
        # TODO: Implement completion waiting
        await self.task_queue.join()
    
    def get_task_status(self, task_id: str) -> Optional[TaskStatus]:
        """Get status of a specific task."""
        return self.task_queue.get_task_status(task_id)
    
    def get_task_result(self, task_id: str) -> Optional[TaskResult]:
        """Get result of a completed task."""
        return self.task_queue.get_task_result(task_id)
    
    def get_system_stats(self) -> Dict[str, Any]:
        """Get system statistics."""
        # TODO: Implement system statistics
        queue_stats = self.task_queue.get_queue_stats()
        worker_stats = [worker.get_stats() for worker in self.workers]
        
        return {
            "is_running": self.is_running,
            "max_workers": self.max_workers,
            "active_workers": len([w for w in self.workers if w.is_running]),
            "queue_stats": queue_stats,
            "worker_stats": worker_stats,
            "registered_tasks": list(self.task_registry.keys())
        }


# Example task functions for demonstration

@async_task_decorator(priority=TaskPriority.NORMAL, max_retries=2, timeout=5.0)
async def sample_computation_task(n: int, delay: float = 1.0) -> Dict[str, Any]:
    """Sample computational task."""
    await asyncio.sleep(delay)  # Simulate work
    
    result = sum(i * i for i in range(n))
    return {
        "input": n,
        "result": result,
        "computation_type": "sum_of_squares"
    }


@async_task_decorator(priority=TaskPriority.HIGH, max_retries=3)
async def sample_io_task(filename: str, content: str) -> Dict[str, Any]:
    """Sample I/O task."""
    # Simulate file I/O
    await asyncio.sleep(0.5)
    
    return {
        "filename": filename,
        "content_length": len(content),
        "operation": "write",
        "timestamp": datetime.now().isoformat()
    }


@async_task_decorator(priority=TaskPriority.LOW, max_retries=1)
async def sample_network_task(url: str) -> Dict[str, Any]:
    """Sample network task."""
    # Simulate network request
    await asyncio.sleep(2.0)
    
    return {
        "url": url,
        "status_code": 200,
        "response_time": 2.0,
        "content_type": "application/json"
    }


async def demonstrate_async_task_system():
    """Demonstrate the async task queue system."""
    print("Async Task Queue System Demonstration")
    print("=" * 50)
    
    # Create task manager
    manager = AsyncTaskManager(max_workers=3, queue_size=10)
    
    # Register task functions
    manager.register_task_function("computation", sample_computation_task)
    manager.register_task_function("io_operation", sample_io_task)
    manager.register_task_function("network_request", sample_network_task)
    
    print("Task manager created with 3 workers")
    print("Registered task functions:", list(manager.task_registry.keys()))
    
    # Start task manager
    await manager.start()
    print("Task manager started")
    
    # Submit various tasks
    task_ids = []
    
    print("\nSubmitting tasks...")
    
    # High priority computation tasks
    for i in range(3):
        config = TaskConfig(priority=TaskPriority.HIGH, max_retries=2)
        task_id = await manager.submit_task(
            sample_computation_task, 100 + i * 50, 0.5, config=config
        )
        task_ids.append(task_id)
        print(f"Submitted computation task {task_id}")
    
    # Normal priority I/O tasks
    for i in range(2):
        config = TaskConfig(priority=TaskPriority.NORMAL)
        task_id = await manager.submit_task(
            "io_operation", f"file_{i}.txt", f"Content for file {i}", config=config
        )
        task_ids.append(task_id)
        print(f"Submitted I/O task {task_id}")
    
    # Low priority network tasks
    for i in range(2):
        config = TaskConfig(priority=TaskPriority.LOW, timeout=3.0)
        task_id = await manager.submit_task(
            "network_request", f"https://api.example.com/data/{i}", config=config
        )
        task_ids.append(task_id)
        print(f"Submitted network task {task_id}")
    
    print(f"\nSubmitted {len(task_ids)} tasks total")
    
    # Show system stats while processing
    print("\nSystem stats during processing:")
    stats = manager.get_system_stats()
    print(f"Active workers: {stats['active_workers']}")
    print(f"Queue stats: {stats['queue_stats']}")
    
    # Wait for completion
    print("\nWaiting for all tasks to complete...")
    await manager.wait_for_completion()
    
    # Show results
    print("\nTask Results:")
    print("-" * 40)
    
    for task_id in task_ids:
        result = manager.get_task_result(task_id)
        if result:
            print(f"Task {task_id[:8]}...")
            print(f"  Status: {result.status.value}")
            print(f"  Execution time: {result.execution_time:.3f}s")
            print(f"  Retry count: {result.retry_count}")
            if result.error:
                print(f"  Error: {result.error}")
            elif result.result:
                print(f"  Result: {result.result}")
            print()
    
    # Final system stats
    print("Final system statistics:")
    final_stats = manager.get_system_stats()
    print(json.dumps(final_stats, indent=2, default=str))
    
    # Stop task manager
    await manager.stop()
    print("\nTask manager stopped")


async def main():
    """Main function with menu-driven interface."""
    print("=== Async Task Queue System ===")
    print("1. Run demonstration")
    print("2. Interactive task submission")
    print("3. Performance testing")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            await demonstrate_async_task_system()
            
        elif choice == "2":
            # TODO: Implement interactive task submission
            print("Interactive task submission not yet implemented")
            
        elif choice == "3":
            # TODO: Implement performance testing
            print("Performance testing not yet implemented")
            
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    asyncio.run(main())