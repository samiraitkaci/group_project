from items import *
from floor2 import *
from floor3 import *

room_main_1 = {
    "name": "Main room",

    "description":
    """""",

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

prison_room_1 = {
    "name": "Prison room",

    "description":
    """You slowly open your eyes to an unfamiliar room, lying flat on concrete flooring with your school attire on. 
Before being able to question how you have ended up in such a macabre room, an agonizing pain seeps through your body from your left hand. 
A crudely made watch is nailed into your skin; the bloodstains clearly show that it has been present for a while. 
As you attempt to gain some form of understanding of your predicament, a screen suddenly flashes to life!
""",

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
    "Main_1": room_main_1,
    "Prison_1": prison_room_1,
    ########################

    # rooms in room 2
    "Exit_2": room_exit_2,
    "Main_2": room_main_2,
    "Room_1_2": room_1_2,
    "Room_2_2": room_2_2,
    "Room_3_2": room_3_2,
    ########################

    # rooms in room 3

    

}
