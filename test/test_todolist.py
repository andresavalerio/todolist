from src.todolist import TodoList

def test_todolist_creation(capsys):
    my_list = TodoList("Test")
    output = capsys.readouterr()
    assert output
    assert my_list

def test_todolist_item_insertion(capsys):
    my_list = TodoList("Test")
    new_list = my_list.create_item("Worship the Lord")
    output = capsys.readouterr()
    assert output
    assert new_list
    assert new_list == my_list.show_items()