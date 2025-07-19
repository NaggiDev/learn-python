# Mini-Project: Test-Driven Development Exercise

## Project Overview

This mini-project will guide you through building a **Task Management System** using Test-Driven Development (TDD) methodology. You'll implement a command-line task manager that allows users to create, update, delete, and organize tasks while following the Red-Green-Refactor cycle.

## Learning Objectives

By completing this project, you will:

- **Master TDD Workflow**: Practice the Red-Green-Refactor cycle
- **Write Effective Tests**: Create comprehensive test suites before implementation
- **Design Through Testing**: Use tests to drive your code design
- **Apply Testing Best Practices**: Use fixtures, parametrization, and proper test organization
- **Integrate Quality Tools**: Use linting, formatting, and type checking
- **Handle Edge Cases**: Test and implement robust error handling

## Project Requirements

### Core Features

1. **Task Management**
   - Create tasks with title, description, and priority
   - Mark tasks as complete/incomplete
   - Delete tasks
   - List all tasks with filtering options

2. **Task Organization**
   - Assign categories to tasks
   - Set due dates
   - Priority levels (Low, Medium, High)
   - Search tasks by keywords

3. **Data Persistence**
   - Save tasks to JSON file
   - Load tasks from file on startup
   - Handle file corruption gracefully

4. **Command-Line Interface**
   - Interactive menu system
   - Command-line arguments for quick operations
   - User-friendly error messages

### Technical Requirements

- **Python 3.8+**
- **Type hints** for all functions and methods
- **Comprehensive test coverage** (aim for >90%)
- **PEP 8 compliance** using Black and flake8
- **Documentation** with docstrings
- **Error handling** for all edge cases

## TDD Methodology

### The Red-Green-Refactor Cycle

1. **Red**: Write a failing test for the next small piece of functionality
2. **Green**: Write the minimal code to make the test pass
3. **Refactor**: Improve the code while keeping tests green

### TDD Rules

1. **Don't write production code** until you have a failing test
2. **Don't write more test code** than necessary to fail
3. **Don't write more production code** than necessary to pass the test

## Project Structure

```
mini_project/
├── README.md                 # This file
├── requirements.txt          # Project dependencies
├── src/                      # Source code
│   ├── __init__.py
│   ├── task.py              # Task model
│   ├── task_manager.py      # Task management logic
│   ├── storage.py           # Data persistence
│   └── cli.py               # Command-line interface
├── tests/                    # Test files
│   ├── __init__.py
│   ├── test_task.py         # Task model tests
│   ├── test_task_manager.py # Task manager tests
│   ├── test_storage.py      # Storage tests
│   └── test_cli.py          # CLI tests
├── pyproject.toml           # Tool configuration
└── main.py                  # Application entry point
```

## Getting Started

### Step 1: Setup

1. Create the project structure
2. Install dependencies: `pip install pytest pytest-cov black flake8 mypy`
3. Configure tools (pyproject.toml provided)

### Step 2: TDD Implementation Plan

Follow this order to implement features using TDD:

#### Phase 1: Task Model (Start Here)
1. **Test**: Task creation with title
2. **Test**: Task with description and priority
3. **Test**: Task completion status
4. **Test**: Task string representation
5. **Test**: Task equality comparison

#### Phase 2: Task Manager
1. **Test**: Add task to manager
2. **Test**: List all tasks
3. **Test**: Mark task as complete
4. **Test**: Delete task
5. **Test**: Filter tasks by status
6. **Test**: Search tasks by keyword

#### Phase 3: Data Persistence
1. **Test**: Save tasks to JSON file
2. **Test**: Load tasks from JSON file
3. **Test**: Handle missing file
4. **Test**: Handle corrupted file
5. **Test**: Backup and recovery

#### Phase 4: Command-Line Interface
1. **Test**: Parse command-line arguments
2. **Test**: Interactive menu display
3. **Test**: User input validation
4. **Test**: Error message formatting
5. **Test**: Integration tests

## Implementation Guidelines

### Task Model Specifications

```python
class Task:
    """Represents a single task with metadata."""
    
    def __init__(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM):
        """Initialize a new task."""
        pass
    
    def mark_complete(self) -> None:
        """Mark the task as completed."""
        pass
    
    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for serialization."""
        pass
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary."""
        pass
```

### Task Manager Specifications

```python
class TaskManager:
    """Manages a collection of tasks."""
    
    def add_task(self, task: Task) -> None:
        """Add a task to the manager."""
        pass
    
    def get_tasks(self, status: Optional[TaskStatus] = None) -> List[Task]:
        """Get tasks, optionally filtered by status."""
        pass
    
    def complete_task(self, task_id: str) -> bool:
        """Mark a task as complete by ID."""
        pass
    
    def delete_task(self, task_id: str) -> bool:
        """Delete a task by ID."""
        pass
    
    def search_tasks(self, keyword: str) -> List[Task]:
        """Search tasks by keyword in title or description."""
        pass
```

## Example TDD Session

Here's how to start with the first feature:

### 1. Write the First Test (Red)

```python
# tests/test_task.py
import pytest
from src.task import Task

def test_create_task_with_title():
    """Test creating a task with just a title."""
    task = Task("Buy groceries")
    assert task.title == "Buy groceries"
    assert task.description == ""
    assert not task.is_complete
```

**Run the test**: `pytest tests/test_task.py::test_create_task_with_title`
**Expected result**: Test fails (Red) because Task class doesn't exist

### 2. Write Minimal Code (Green)

```python
# src/task.py
class Task:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.is_complete = False
```

**Run the test**: Test should now pass (Green)

### 3. Refactor (if needed)

The code is simple enough, no refactoring needed yet.

### 4. Next Test (Red)

```python
def test_create_task_with_description():
    """Test creating a task with title and description."""
    task = Task("Buy groceries", "Milk, bread, eggs")
    assert task.title == "Buy groceries"
    assert task.description == "Milk, bread, eggs"
```

Continue this cycle for each feature!

## Testing Guidelines

### Test Organization

```python
class TestTask:
    """Test class for Task model."""
    
    def test_task_creation(self):
        """Test basic task creation."""
        pass
    
    def test_task_completion(self):
        """Test marking tasks complete/incomplete."""
        pass
    
    @pytest.mark.parametrize("title,description,expected", [
        ("Task 1", "Description 1", "Task 1: Description 1"),
        ("Task 2", "", "Task 2"),
    ])
    def test_task_string_representation(self, title, description, expected):
        """Test task string representation with various inputs."""
        pass
```

### Fixtures for Common Setup

```python
@pytest.fixture
def sample_task():
    """Create a sample task for testing."""
    return Task("Sample Task", "Sample description")

@pytest.fixture
def task_manager_with_tasks():
    """Create a task manager with some sample tasks."""
    manager = TaskManager()
    manager.add_task(Task("Task 1", "Description 1"))
    manager.add_task(Task("Task 2", "Description 2"))
    return manager
```

## Quality Assurance

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_task.py

# Run tests matching pattern
pytest -k "test_task_creation"
```

### Code Quality Checks

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/

# Security check
bandit -r src/
```

## Deliverables

### Required Files

1. **Source Code**: Complete implementation in `src/` directory
2. **Test Suite**: Comprehensive tests in `tests/` directory
3. **Configuration**: Tool configuration in `pyproject.toml`
4. **Documentation**: Updated README with usage instructions
5. **Requirements**: `requirements.txt` with dependencies

### Success Criteria

- [ ] All tests pass
- [ ] Test coverage > 90%
- [ ] No linting errors
- [ ] Type checking passes
- [ ] All features implemented
- [ ] CLI works as expected
- [ ] Data persistence functions correctly

## Extension Challenges

Once you complete the basic requirements, try these extensions:

1. **Advanced Features**
   - Task dependencies (task A must complete before task B)
   - Recurring tasks
   - Task templates
   - Time tracking

2. **Enhanced CLI**
   - Colored output
   - Progress bars
   - Auto-completion
   - Configuration file support

3. **Data Features**
   - Export to CSV/PDF
   - Import from other formats
   - Data validation
   - Migration system

4. **Testing Enhancements**
   - Property-based testing with Hypothesis
   - Performance testing
   - Integration testing with temporary files
   - Mock external dependencies

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [TDD by Example (Kent Beck)](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530)
- [Python Testing 101](https://realpython.com/python-testing/)
- [Clean Code (Robert Martin)](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

## Getting Help

If you get stuck:

1. **Review the TDD cycle** - Are you following Red-Green-Refactor?
2. **Start smaller** - Break down the feature into smaller tests
3. **Check the tests** - Are your tests actually testing what you think?
4. **Read error messages** - They often contain the solution
5. **Refactor gradually** - Don't try to perfect everything at once

Remember: The goal is to learn TDD, not to build the perfect task manager. Focus on the process, and the product will follow!

---

**Good luck with your TDD journey!** 🚀