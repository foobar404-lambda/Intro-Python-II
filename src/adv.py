from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    "rock": Item("rock", "its a rock"),
    "candle": Item("candle", "its a candle"),
    "grass": Item("grass", "its grass"),
    "shoe": Item("shoe", "its a shoe"),
    "gold": Item("gold", "its gold"),
}

rooms = {
    "outside": Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons", [items["rock"]]
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
        [items["candle"]],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [items["rock"]],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Some valuables are spread accross the room. The only exit is to the south.""",
        [items["gold"]],
    ),
}


# Link rooms together

rooms["outside"].n_to = rooms["foyer"]
rooms["overlook"].s_to = rooms["foyer"]
rooms["foyer"].s_to = rooms["outside"]
rooms["foyer"].n_to = rooms["overlook"]
rooms["foyer"].e_to = rooms["narrow"]
rooms["narrow"].w_to = rooms["foyer"]
rooms["narrow"].n_to = rooms["treasure"]
rooms["treasure"].s_to = rooms["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(rooms["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


def parse(words):
    words = words.split(" ")
    dirs = ["n", "s", "e", "w"]
    verbs = ["get", "take", "drop", "throw"]

    rtn = ""

    if words[0] in dirs:
        rtn = "direction"
    elif words[0] in verbs:
        rtn = "verb"
    elif words[0] == "i":
        rtn = "inventory"
    else:
        rtn = "none"

    return rtn


print(player.room.name)
print(player.room.description)
print("items:" + " ".join(map(lambda x: x.name, player.room.items)))

# main event loop

while True:

    msg = input("??? What Now ??? \n").lower()
    if msg == "q":
        break

    words_type = parse(msg)
    room_items = " ".join(map(lambda x: x.name, player.room.items))
    player_items = " ".join(map(lambda x: x.name, player.items))

    if words_type == "direction":

        while not hasattr(player.room, f"{msg}_to") and msg != "q":
            print("!!! Your Path Is Blocked !!!")
            msg = input("??? What Now ??? \n").lower()

        player.room = getattr(player.room, f"{msg}_to")

        print(player.room.name)
        print(player.room.description)
        print("items:" + room_items)

    if words_type == "verb":
        action = msg.split(" ")[0]
        item = items[" ".join(msg.split(" ")[1:]).strip()]
        player.room.item_action(action, item, player)

        room_items = " ".join(map(lambda x: x.name, player.room.items))

        print("ITEMS::" + room_items)

    if words_type == "inventory":
        print(f"BAG::{player_items}")


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
