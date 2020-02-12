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
                player.items.remove(item)
                self.items.append(item)

                print("item dropped")
        if action == "take" or action == "get":
            if item in self.items:
                player.items.append(item)
                self.items.remove(item)

                print("you have picked up " + item)
            else:
                print("item doesint exist")

