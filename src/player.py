# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.room = room
        self.items = []

    def has_item(self, item):
        found = False
        for local_item in self.items:
            if local_item.name == item.name:
                found = True
        return found

    def manage_items(self, type, item):
        if type == "add":
            self.items.append(item)
        if type == "remove":
            for i in range(len(self.items)):
                if self.items[i].name == item.name:
                    self.items.pop(i)
                    break
