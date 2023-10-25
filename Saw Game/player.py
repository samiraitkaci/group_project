from items import *
from floor1 import rooms

player_name = ""
inventory = []

# Start game at the prison
#current_room = rooms["Prison_1"]
current_room = rooms["Final_room"]


def update_inventory(item):
    inventory.append(item)
    return inventory
    
def remove_inventory(item):
    inventory.remove(item)
    return inventory

