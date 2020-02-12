from room import Room
from player import Player

# Declare all the rooms

rooms = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        ["stick", "rock", "gun"],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
        ["chair", "rug", "candle"],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        ["grass"],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        ["bones", "shoe"],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Some valuables are spread accross the room. The only exit is to the south.""",
        ["gold", "sword", "diamond"],
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
print("items:" + " ".join(player.room.items))

while True:

    msg = input("what now?\n").lower()
    if msg == "q":
        break

    words_type = parse(msg)

    if words_type == "direction":

        while not hasattr(player.room, f"{msg}_to") and msg != "q":
            print("your path is blocked")
            msg = input("what now?\n").lower()

        player.room = getattr(player.room, f"{msg}_to")

        print(player.room.name)
        print(player.room.description)
        print("items:" + " ".join(player.room.items))

    if words_type == "verb":
        action = msg.split(" ")[0]
        item = " ".join(msg.split(" ")[1:])
        player.room.item_action(action, item, player)

        print("items:" + " ".join(player.room.items))

    if words_type == "inventory":
        print(f"bag:{' '.join(player.items)}")


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
