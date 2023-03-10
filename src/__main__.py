from src.todolist import TodoItem, TodoList

print("Creating a list")

todolist = TodoList("test")

print("Now, let's see if the list is empty")

todolist.show_items()

print("Let's insert a item")

todolist.create_item("Worship the Lord")

print("Show me what you've got!")

todolist.show_items()
