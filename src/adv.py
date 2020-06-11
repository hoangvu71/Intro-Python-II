from room import Room
from player import Player as Player
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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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

def adventure(player):
    while(True):
        print("You arrived at",player.current_room)
        userInput = input("Where do you want to go?")
        if userInput not in "n s w e".split():
            print("*****Please enter a direction with the letters 'n' 's' 'w' 'e'*****")
        if hasattr(player.current_room, f'{userInput}_to'):
            if userInput == 'n' and player.current_room.n_to is not None:
                player.current_room = player.current_room.n_to
            elif userInput == 'w' and player.current_room.w_to is not None:
                player.current_room = player.current_room.w_to
            elif userInput == 'e' and player.current_room.e_to is not None:
                player.current_room = player.current_room.e_to
            elif userInput == 's' and player.current_room.s_to is not None:
                player.current_room = player.current_room.s_to
            else:
                print("*****That was is blocked!*****")
        if userInput == 'q':
            print("*****Exiting...*****")
            return 0
adventure(heroSim)
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
