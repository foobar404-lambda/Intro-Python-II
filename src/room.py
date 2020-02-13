# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name.lower()
        self.description = description
        self.items = items

    def item_action(self, action, item, player):
        if action == "drop" or action == "throw":
            if player.has_item(item):
                player.manage_items("remove", item)
                self.manage_items("add", item)

                print("item dropped")
        if action == "take" or action == "get":
            found = False
            for local_item in self.items:
                if item.name == local_item.name:
                    found = True
                    player.manage_items("add", item)
                    self.manage_items("remove", item)

                    print(f"*** You Have Picked Up {item.name} ***")

            if not found:
                print("!!! Item Does Not Exist !!!")

    def manage_items(self, type, item):
        if type == "add":
            self.items.append(item)
        if type == "remove":
            for i in range(len(self.items)):
                if self.items[i].name == item.name:
                    del self.items[i]
                    break
