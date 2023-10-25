#!/usr/bin/python3

from floor1 import rooms
from player import *
from items import *
from gameparser import *
from art import *
import time 
import threading
from playsound import playsound
from concurrent.futures import ThreadPoolExecutor
import os
import sys
from colorama import *
from floor4 import final_room


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """


    item_list = []
    for keyword in items:
        item_list.append(keyword["name"])
    return ', '.join(item_list)
    


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """

    if list_of_items(room['items']) != '':
        print('There is ' + list_of_items(room['items']) + ' here.')
        print('')

    


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """

    if inventory != []:
        print('You have ' + list_of_items(inventory) + '.')
        print('')
    


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()

    # Display room items
    if room['items'] != []:
        print_room_items(room)
        

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
   


    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    
    # 
    '''for item in range(0, len(room_items)):
        print("TAKE " + room_items[item]['id'].upper() + " to take a " + room_items[item]['name'] + '.')'''
    
    for item in room_items:
        print("TAKE " + item['id'].upper() + " to take a " + item['name'] + '.')

    #

    for inventory in range(0, len(inv_items)):
        print("DROP " + inv_items[inventory]['id'] + ' to drop your ' + inv_items[inventory]['name'])

    for key, room in exits.items():
        if rooms[room]["inspectable"] == True:
            print("INSPECT " + rooms[room]["id"] + " to inspect " + rooms[room]["name"])
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
   
    if is_valid_exit(current_room['exits'], direction) == True:
        temp_room = move(current_room['exits'], direction) 
        if temp_room["status"] == "locked":
            print(Fore.WHITE)
            print("This room is currently locked")
            input(">Press enter to continue")
        else:
            current_room = move(current_room['exits'], direction)
    else:
        print(Fore.WHITE + "You cannot go there.")
        input(">Press enter to continue")
    
def check_key(): # checks if inventory contains the items needed to unlock a given door 
    if all(value in inventory for value in current_room['key']):
        current_room['target']['status'] = "unlocked"
    

def execute_take(id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    
    
    """
    flag = False
    for item in current_room['items']:
        print(item['id'])
        if item['id'] == id:
            update_inventory(item)
            current_room['items'].remove(item)
            flag = True
            check_key()
    if flag == False:
        print("You cannot take this")
        input(">Press enter to continue")
        



            
    
        
            
    

def execute_drop(id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."

    """

    for item in inventory:
        if item['id'] == id:
            current_room['items'].append(item)
            remove_inventory(item) 
        elif item['id'] != id and item == inventory[len(inventory)-1]:
            print("You cannot drop that")

    
def execute_inspect(id):
    if is_valid_id(id) == True:
        for key, room in current_room["exits"].items():
            if rooms[room]["inspectable"] == True:
                print(rooms[room]["description"])
    elif is_valid_id(id) == False:
        print("Inspect what?")
    input(">Press enter to continue")

def is_valid_id(id):
    for key, room in current_room["exits"].items():       
        if rooms[room]["id"] == id:
            return True
    return False
     
    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
            input("Press enter to retry")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")
            input(">Press enter to retry")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
            input("Press enter to retry")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            input("Press enter to retry")

    else:
        print("This makes no sense.")
        input("Press enter to retry")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")
   

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    
    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]

# utility functions


def countdown_timer(minutes, global_timer):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        global_timer[0] = timeformat
        time.sleep(1)
        seconds -= 1
    global_timer[0] = "Time's up!"
    playsound('song_lose.mp3')
    
def assign_items(): # this will randomly assign items to each room
    pass
    

def scrollTxt(text): # make text scroll across the screen
   for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.009)


def print_dialogue():
    if current_room["times entered"] == 0:
        for dialogue in current_room["dialogue"]:
            scrollTxt(dialogue)
            print()
            current_room["times entered"] += 1
            input(Fore.RED + "> Continue (enter)")
            print(Fore.WHITE)
    else:
        choice = input("Press any key to continue or type Y to show dialogue for room")
        normalised_choice = normalise_input(choice)
        if normalised_choice == ['y']:
            current_room["times entered"] = 0
            print_dialogue()


####################################################

# This is the entry point of our program
def main(global_timer):
    # Main game loop
    
    while True: 
        if current_room == final_room:
            playsound("song_win.mp3")
        print("\n" * 1000)
        print(Fore.WHITE + "Time remaining:", global_timer[0])
        # Display game status (room description, inventory etc.)
        print(Fore.RED)
        print(current_room['map'])
        print(Fore.WHITE)
        print(current_room["name"].upper())
        print("-")
        print_inventory_items(inventory)
        print_dialogue()
        # Show the menu with possible actions and ask the player
        print(Fore.RED)
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)     
        print("\n" * 1000)
       



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
def start_game(time, time_as_int):
    global_timer = [time]

    timer_thread = threading.Thread(target=countdown_timer, args=(time_as_int, global_timer))
    game_thread = threading.Thread(target=main, args=(global_timer,))

    timer_thread.start()
    game_thread.start()

    timer_thread.join()
    game_thread.join()

    assign_items()
