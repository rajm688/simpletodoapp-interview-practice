"""Comprehensive tests for SimpleTodoApp"""

import pytest
from models import TodoItem, TodoManager, todos_storage

@pytest.fixture
def manager():
    """Create a fresh TodoManager for each test"""
    # Clear storage before each test
    todos_storage.clear()
    import models
    models.next_id = 1
    return TodoManager()

class TestTodoItem:
    """Test TodoItem class"""
    
    def test_todo_item_creation(self):
        """Test creating a new TodoItem"""
        todo = TodoItem(1, "Test todo", 2)
        assert todo.id == 1
        assert todo.description == "Test todo"
        assert todo.priority == 2
        assert todo.completed is False
    
    def test_todo_item_mark_completed(self):
        """Test marking a todo item as completed"""
        todo = TodoItem(1, "Test todo")
        assert todo.completed is False
        todo.mark_completed()
        assert todo.completed is True
    
    def test_todo_item_default_priority(self):
        """Test default priority is medium (2)"""
        todo = TodoItem(1, "Test todo")
        assert todo.priority == 2

class TestTodoManager:
    """Test TodoManager class"""
    
    def test_add_todo(self, manager):
        """Test adding a new todo"""
        todo = manager.add_todo("Test todo", 1)
        assert todo.id == 1
        assert todo.description == "Test todo"
        assert todo.priority == 1
        assert len(manager.get_all_todos()) == 1
    
    def test_add_multiple_todos(self, manager):
        """Test adding multiple todos with auto-incrementing IDs"""
        todo1 = manager.add_todo("First todo", 1)
        todo2 = manager.add_todo("Second todo", 3)
        
        assert todo1.id == 1
        assert todo2.id == 2
        assert len(manager.get_all_todos()) == 2
    
    def test_get_all_todos_sorted(self, manager):
        """Test getting all todos sorted by priority"""
        manager.add_todo("Low priority", 1)
        manager.add_todo("High priority", 3)
        manager.add_todo("Medium priority", 2)
        
        todos = manager.get_all_todos()
        assert len(todos) == 3
        assert todos[0].priority == 3  # High priority first
        assert todos[1].priority == 2  # Medium priority second
        assert todos[2].priority == 1  # Low priority last
    
    def test_get_todo_by_id(self, manager):
        """Test getting a specific todo by ID"""
        todo = manager.add_todo("Test todo")
        found_todo = manager.get_todo_by_id(todo.id)
        assert found_todo is not None
        assert found_todo.id == todo.id
        assert found_todo.description == "Test todo"
        
        # Test non-existent ID
        not_found = manager.get_todo_by_id(999)
        assert not_found is None
    
    def test_mark_completed(self, manager):
        """Test marking a todo as completed"""
        todo = manager.add_todo("Test todo")
        assert todo.completed is False
        
        result = manager.mark_completed(todo.id)
        assert result is True
        assert todo.completed is True
        
        # Test marking already completed todo
        result = manager.mark_completed(todo.id)
        assert result is False
        
        # Test non-existent ID
        result = manager.mark_completed(999)
        assert result is False
    
    def test_delete_todo(self, manager):
        """Test deleting a todo"""
        todo = manager.add_todo("Test todo")
        assert len(manager.get_all_todos()) == 1
        
        result = manager.delete_todo(todo.id)
        assert result is True
        assert len(manager.get_all_todos()) == 0
        
        # Test deleting non-existent todo
        result = manager.delete_todo(999)
        assert result is False
    
    def test_get_pending_todos(self, manager):
        """Test getting only pending todos"""
        todo1 = manager.add_todo("Pending todo")
        todo2 = manager.add_todo("Another todo")
        manager.mark_completed(todo2.id)
        
        pending = manager.get_pending_todos()
        assert len(pending) == 1
        assert pending[0].id == todo1.id
        assert pending[0].completed is False
    
    def test_get_completed_todos(self, manager):
        """Test getting only completed todos"""
        todo1 = manager.add_todo("Pending todo")
        todo2 = manager.add_todo("Completed todo")
        manager.mark_completed(todo2.id)
        
        completed = manager.get_completed_todos()
        assert len(completed) == 1
        assert completed[0].id == todo2.id
        assert completed[0].completed is True
    
    def test_clear_all_todos(self, manager):
        """Test clearing all todos"""
        manager.add_todo("Todo 1")
        manager.add_todo("Todo 2")
        assert len(manager.get_all_todos()) == 2
        
        manager.clear_all_todos()
        assert len(manager.get_all_todos()) == 0
        
        # Test that next ID is reset
        new_todo = manager.add_todo("New todo")
        assert new_todo.id == 1