"""Data models and business logic for SimpleTodoApp"""

from typing import List, Optional

# In-memory storage
todos_storage = []
next_id = 1

class TodoItem:
    """Represents a single todo item"""
    
    def __init__(self, id: int, description: str, priority: int = 2):
        self.id = id
        self.description = description
        self.priority = priority  # 1=Low, 2=Medium, 3=High
        self.completed = False
    
    def mark_completed(self):
        """Mark this todo item as completed"""
        self.completed = True
    
    def __repr__(self):
        status = "completed" if self.completed else "pending"
        return f"TodoItem(id={self.id}, description='{self.description}', priority={self.priority}, status={status})"

class TodoManager:
    """Manages todo items and operations"""
    
    def __init__(self):
        self.todos = todos_storage
    
    def add_todo(self, description: str, priority: int = 2) -> TodoItem:
        """Add a new todo item"""
        global next_id
        todo = TodoItem(next_id, description, priority)
        next_id += 1
        self.todos.append(todo)
        return todo
    
    def get_all_todos(self) -> List[TodoItem]:
        """Get all todo items sorted by priority (high to low) then by ID"""
        return sorted(self.todos, key=lambda x: (-x.priority, x.id))
    
    def get_todo_by_id(self, todo_id: int) -> Optional[TodoItem]:
        """Get a specific todo item by ID"""
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def mark_completed(self, todo_id: int) -> bool:
        """Mark a todo item as completed"""
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.mark_completed()
            return True
        return False
    
    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo item by ID"""
        for i in range(len(self.todos)):
            if self.todos[i].id == todo_id:
                self.todos.pop(i)
                return True
        return False
    
    def get_pending_todos(self) -> List[TodoItem]:
        """Get all pending (not completed) todo items"""
        return [todo for todo in self.get_all_todos() if not todo.completed]
    
    def get_completed_todos(self) -> List[TodoItem]:
        """Get all completed todo items"""
        return [todo for todo in self.get_all_todos() if todo.completed]
    
    def clear_all_todos(self):
        """Clear all todos (useful for testing)"""
        self.todos.clear()