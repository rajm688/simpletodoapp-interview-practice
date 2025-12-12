#!/usr/bin/env python3
"""Simple Todo App - Command Line Interface"""

from models import TodoItem, TodoManager

def display_menu():
    """Display the main menu options"""
    print("\n=== Simple Todo App ===")
    print("1. Add new todo")
    print("2. View all todos")
    print("3. Mark todo as completed")
    print("4. Delete todo")
    print("5. Exit")
    print("=" * 23)

def get_user_choice():
    """Get and validate user menu choice"""
    try:
        choice = int(input("Enter your choice (1-5): "))
        if 1 <= choice <= 5:
            return choice
        else:
            print("Please enter a number between 1 and 5.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def add_todo_interactive(manager):
    """Interactive function to add a new todo"""
    description = input("Enter todo description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return
    
    print("Priority levels: 1=Low, 2=Medium, 3=High")
    try:
        priority = int(input("Enter priority (1-3): "))
        if priority not in [1, 2, 3]:
            print("Invalid priority. Using default (Medium).")
            priority = 2
    except ValueError:
        print("Invalid input. Using default priority (Medium).")
        priority = 2
    
    todo = manager.add_todo(description, priority)
    print(f"Todo added successfully! ID: {todo.id}")

def view_todos_interactive(manager):
    """Interactive function to view all todos"""
    todos = manager.get_all_todos()
    if not todos:
        print("No todos found.")
        return
    
    print("\n=== Your Todos ===")
    priority_names = {1: "Low", 2: "Medium", 3: "High"}
    
    for todo in todos:
        status = "✓" if todo.completed else "○"
        priority_name = priority_names.get(todo.priority, "Unknown")
        print(f"[{todo.id}] {status} {todo.description} (Priority: {priority_name})")

def complete_todo_interactive(manager):
    """Interactive function to mark todo as completed"""
    view_todos_interactive(manager)
    if not manager.get_all_todos():
        return
    
    try:
        todo_id = int(input("Enter todo ID to mark as completed: "))
        if manager.mark_completed(todo_id):
            print("Todo marked as completed!")
        else:
            print("Todo not found or already completed.")
    except ValueError:
        print("Please enter a valid todo ID.")

def delete_todo_interactive(manager):
    """Interactive function to delete a todo"""
    view_todos_interactive(manager)
    if not manager.get_all_todos():
        return
    
    try:
        todo_id = int(input("Enter todo ID to delete: "))
        if manager.delete_todo(todo_id):
            print("Todo deleted successfully!")
        else:
            print("Todo not found.")
    except ValueError:
        print("Please enter a valid todo ID.")

def main():
    """Main application loop"""
    manager = TodoManager()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice is None:
            continue
        
        if choice == 1:
            add_todo_interactive(manager)
        elif choice == 2:
            view_todos_interactive(manager)
        elif choice == 3:
            complete_todo_interactive(manager)
        elif choice == 4:
            delete_todo_interactive(manager)
        elif choice == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()