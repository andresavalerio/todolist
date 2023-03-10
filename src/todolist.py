class TodoItem():
    def __init__(self, description: str):
            self.description = description
            self.status = False
    
    def set_done(self):
        self.status = True
    
    def set_undone(self):
        self.status = False

    def get_item_status(self):
        return self.status

    def get_item_description(self):
        return self.description


class TodoList():
    def __init__(self, name):
        self.name = name
        self.items = []
        print(f"List {self.name} has being created.")

    def create_item(self, description: int):
        new_item = TodoItem(description)
        self.items.append(new_item)
        print(f"Item successfully inserted: {description}")
        return self.items

    def delete_item(self, position: int):
        item_description = self.items[position].get_item_description()
        print(f"The item you've choosen is \"{item_description}\"")
        delete_approval = input("This action cannot be undone. Continue? (y/N)")

        if delete_approval == "y" or delete_approval == "Y":
            self.items.pop(position)
            print("Item successfully removed.")
        else:
            print("There is nothing to do.")
        
        return self.items
        

    def show_items(self):
        if self.items:
            print(f"Here are the items from {self.name}:")
            print("")

            for item in self.items:
                if item.get_item_status():
                    print(f"[X] {item.get_item_description()}")
                else:
                    print(f"[ ] {item.get_item_description()}")
        
        else:
            print(f"There are no items to show from {self.name}. Consider creating an item.")
        
        return self.items
