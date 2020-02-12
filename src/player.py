# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.room = room
        self.items = []

    def has_item(self, item):
        return item in self.items
