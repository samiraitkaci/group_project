from items import *
from floor2 import *



room_main_1 = {
    "name": "Main room",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : ["""You dash into a run-down hallway where a dimly lit sign labeled "exit" calls out to you.
Seemingly, your first challenge to escape, as it appears to be slammed shut by some contraption. 
Perhaps something in these two rooms can help you escape?"""],

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


    "items": [item_hammer], 

    "key" : [item_hammer, item_nails],

    "target" : room_exit_2,

    "inspectable" : False,

    "id" : "" 
}

prison_room_1 = {
    "name": "Prison room",

    "times entered" : 0,

    "description" : "",

    "dialogue" : ["""You slowly open your eyes to an unfamiliar room, lying flat on concrete flooring with your school attire on. 
Before being able to question how you have ended up in such a macabre room, an agonizing pain seeps through your body from your left hand. 
A crudely made watch is nailed into your skin; the bloodstains clearly show that it has been present for a while. 
As you attempt to gain some form of understanding of your predicament, a screen suddenly flashes to life!""", """Hello. I assume you don't know me, nor this room, but I know a lot about you. Do you wish to play a game?
I have set up a labyrinth of illusion and misdirections, and now you find yourself in it. 
You see, coming to university and being late to your lectures pays a price.
So, will you find your way out of this labyrinth, or will it become your tomb?""", """I have made you a gift, a watch, so you won't be late for your next lecture, and if we look, you don't have very long. 
You'd better get out of this maze in time; otherwise, you may not have the chance to go to that graduation ceremony in one piece. 
Good luck.""", """Recovering from the initial shock, you frantically look around for what you have to do. 
You spot a map with three levels, which you surmise to be the building you are trapped in. 
Furthermore, there are multiple items on the ground in front of you, as well as a hallway leading to another room..."""],

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

    "items": [item_nails],

    "key" : [item_hammer, item_nails],

    "target" : room_exit_2,

    "inspectable" : False,

    "id" : "" 

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

    "Exit_3": room_exit_3,
    "Main_3": room_main_3,
    "Cell_1": room_cell_1,
    "Cell_2": room_cell_2,
    "Cell_3": room_cell_3,
    "Bathroom_1": room_bathroom_1,
    "Bathroom_2": room_bathroom_2,
    "Bathroom_3": room_bathroom_3,
    "Dugout": room_dugout,

    # final room

    "Final_room" : final_room

}
