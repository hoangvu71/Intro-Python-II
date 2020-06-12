#---------Moving through maps---------#
def moving(userInput, player):
  #1.0 Making 'n_to' attribute  
  direction = f'{userInput}_to' 

  location = player.current_room

  #2.0 if it has attr, room = room + direction attribute
  if getattr(location, direction) is not None:
    player.current_room = getattr(location, direction)

  #2.1 if it doesn't have attr, it means that there is no route to go to another map
  elif getattr(location, direction) is  None:
    print("That direction is blocked!")

#----------User Input--------#
def askUser():
    userInput = input("What do you want to do?")
    if userInput == 'q':
            print("*****Exiting...*****")
            return 0

    # Keep asking if input not a direction or action of take and drop 
    while userInput not in "n s w e".split() and userInput.split()[0] not in'take item'.split() and userInput.split()[0] not in 'drop item'.split() :
            print("*****Please enter a direction with the letters 'n' 's' 'w' 'e'*****")
            print("*****Or you can say 'take \"item\"'*****")
            userInput = input("What do you want to do?")
            if userInput == 'q':
                print("*****Exiting...*****")
                return 0 

    return userInput

#----------Take and Drop Items ----------#
def takeDropItem(userInput, player):
    # 3.0 Input analyzer
    location = player.current_room

    # If input is more than 1 word
    if len(userInput.split()) > 1: 

        # Then we will have a verb in the first word
        verb = userInput.split()[0]

        # Object in the second word
        item = userInput.split()[1]

        if verb == 'take' and itemInList(item, location.items):
            # Find index of item in the room
            for i in range(len(location.items)):
                if location.items[i].name == item:
                    itemIndex = i
                            
                    # Add that item to player        
                    player.items.append(location.items[itemIndex])
                        
                    # Remove that item from room
                    location.items.remove(location.items[itemIndex])
                    return print(player.items[-1].on_take)              
        elif verb == 'take' and not itemInList(item, location.items):
            print(f'No {item} in here')

        elif verb == 'drop' and  itemInList(item, player.items):
            for i in range(len(player.items)):
                if player.items[i].name == item:
                    itemIndex = i

                    # Add that item to room
                    player.current_room.items.append(player.items[itemIndex])

                    # Remove that item from player
                    player.items.remove(player.items[itemIndex])
                    return print(location.items[-1].on_drop)

        elif verb == 'drop' and not itemInList(item, player.items):
            print(f'You don\'t have {item}')
    
#-----------Is Item In List?---------#
def itemInList(item, listItems):
    for stuff in listItems:
        if item in stuff.name:
            return True
    return False 