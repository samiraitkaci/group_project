from items import *
from floor2 import *
from floor3 import *

main_1 = {
    "name": "Main room",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits": {"east": "Prison_1", "north" : "Exit_2"}, # The value i.e "Start_1" refers to the key of the room in the "rooms" dictionary

    "status" : "unlocked",

    "map" : """ 
+------ Exit -------+       +-------------------+
|                   |------ |                   |
|     Main room     |       |   Prison room     |
|   (You are here)  |------ |                   |
|                   |       |                   |
+-------------------+       +-------------------+
""", 


    "items": []
}

start_1 = {
    "name": "Starting room",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"west": "Main_1"}, 

    "status" : "unlocked",

    "map" : """ 
+------ Exit -------+       +-------------------+
|                   |------ |                   |
|     Main room     |       |   Prison room     |
|                   |------ |   (You are here)  |
|                   |       |                   |
+-------------------+       +-------------------+
""",

    "items": []
}



rooms = {
    # rooms in room 1 
    "Main_1": main_1,
    "Start_1": start_1,
    ########################

    # rooms in room 2
    "Exit_2": exit_2,
    "Main_2": main_2,
    "Room1_2": room1_2,
    "Room2_2": room2_2,
    "Room3_2": room3_2,
    ########################

    # rooms in room 3
    "Main_3" : main_3,
    "Exit_3" : exit_3,
    "Room1_3": room1_3,
    "Room2_3": room2_3,
    "Room3_3": room3_3,

    

}
