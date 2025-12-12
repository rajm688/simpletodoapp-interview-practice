# Bug Injection Report

## Project: SimpleTodoApp

### Bug Summary
- Total Bugs Injected: 3
- Bug Types: Logic error, Incorrect implementation, State management issue

---

### BUG-001: Logic error - Missing condition check
**File:** models.py:48
**Type:** Logic error - Missing condition check

**Description:**
mark_completed() doesn't check if todo is already completed, allowing redundant operations

**Original Code:**
```python
if todo and not todo.completed:
```

**Buggy Code:**
```python
if todo:
```

**Reason:**
Common oversight when implementing state change operations - forgetting to check current state

**Expected Impact:**
Test expecting False return for already completed todos will fail

---

### BUG-002: Incorrect implementation - Using wrong method
**File:** models.py:53
**Type:** Incorrect implementation - Using wrong method

**Description:**
delete_todo() uses manual loop instead of get_todo_by_id(), creating inconsistent behavior

**Original Code:**
```python
todo = self.get_todo_by_id(todo_id)
        if todo:
            self.todos.remove(todo)
            return True
        return False
```

**Buggy Code:**
```python
for i in range(len(self.todos)):
            if self.todos[i].id == todo_id:
                self.todos.pop(i)
                return True
        return False
```

**Reason:**
Developer chose different approach than established pattern, creating potential for inconsistency

**Expected Impact:**
While functionally similar, this breaks the established pattern and could cause issues with future modifications

---

### BUG-003: State management issue - Missing global state reset
**File:** models.py:67
**Type:** State management issue - Missing global state reset

**Description:**
clear_all_todos() doesn't reset the global next_id counter

**Original Code:**
```python
global next_id
        self.todos.clear()
        next_id = 1
```

**Buggy Code:**
```python
self.todos.clear()
```

**Reason:**
Common mistake when clearing data - forgetting to reset associated counters or state

**Expected Impact:**
Test expecting new todos to start with ID 1 after clear will fail
