from room import Room
from player import Player as Player
from item import Item
from tools import *

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    "knife": Item("knife", "Cut and slice"),
    "pen": Item("pen", "Write something?"),
    "pot": Item("pot", "hold and hot")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add Items
room['outside'].items.append(items['knife'])
room['outside'].items.append(items['pen'])
room['foyer'].items = items['pot']
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
heroSim = Player("Sim", room['foyer'].s_to)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


#-----------Main--------#
def adventure(player):
    while(True):
        print("-----------------------------")
        # 1.0 Display player's location
        location = player.current_room
        
        print("\nPlayer's location: ",player.current_room,"\n")

        # 1.1 Display rooms items if any
        if location.items is not None:
            listItems = ""
            for item in location.items:
                listItems += f"{item.name}, "
            listItems = listItems[:-2]
            listItems += "."
            print(f"You see {listItems}")
            

        # 1.2 Display user's items if any

        if len(player.items) != 0:
            listItems = ""
            for item in player.items:
                listItems += f"{item.name}, "
            listItems = listItems[:-2]
            listItems += "."
            print(f"Inventory {listItems}")

        # 2.0 Ask user what to do
        userInput = askUser()
        
        # 2.1 userInput == 0 means that player presses 'q'
        if userInput == 0:
            return 0
        # 3.0 Take or drop item
        takeDropItem(userInput, player)

        
        
        if hasattr(player.current_room, f'{userInput}_to'):
            moving(userInput, player)
        
adventure(heroSim)
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
