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

def moving(player, input):
    if ( player.location == room['outside']) and (input == 'n'):
        player.location = room['outside'].n_to
    elif ( player.location == room['foyer']) and (input == 's'):
        player.location = room['foyer'].s_to
    elif ( player.location == room['foyer']) and (input == 'n'):
        player.location = room['foyer'].n_to
    elif ( player.location == room['foyer']) and (input == 'e'):
        player.location = room['foyer'].e_to
    elif ( player.location == room['overlook']) and (input == 's'):
        player.location = room['overlook'].s_to
    elif ( player.location == room['narrow']) and (input == 'n'):
        player.location = room['narrow'].n_to
    elif ( player.location == room['narrow']) and (input == 'w'):
        player.location = room['narrow'].w_to
    elif ( player.location == room['treasure']) and (input == 's'):
        player.location = room['treasure'].s_to
    elif input != 'n' or input != 's' or input != 'w' or input != 'e':
        print("Please enter a direction. n s w e for north south west east")
    else:
        print("This path is not cleared!")
        print("You stay at the same place.")
def adventure(player):
    while(True):
        print(player)
        userInput = input("Where you want to go?")
        moving(player, userInput)
        if userInput == 'q':
            return 'Exiting'

print(adventure(heroSim))

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
