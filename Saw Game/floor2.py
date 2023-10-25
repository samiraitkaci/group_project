from items import *
from floor3 import *


room_exit_2 = {
    "name": """Floor 2, Exit room""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : ["""After using the hammer and nails to dismantle the door's makeshift lock, you climb a shabby set of stairs and step into yet another dimly lit passageway.""", """Entering the room, you're greeted by a large atrium. Thinking back to the first exit, you're confident there's something in these rooms for the exit, just like last time. But time is of the essence; you better be quick."""],

    "exits":  {"north": "Main_2"},

    "status" : "locked",

    "map" : """                             +-------------------+
                             |      Break room   |
                             +---------|---------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +--------Exit-------+
|      Office       |------- |     Main Room     |-------|    Storage room   | 
+-------------------+        |                   |       +-------------------+
                             +---------|---------+
                                       |
                             +---------|---------+
                             | Exit(you are here)|
                             +-------------------+
""",

    "items": [],

    "key" : [item_saw, item_beam],

    "target" : room_exit_3,

    "inspectable" : True,

    "id" : "door" 
}

   


room_main_2 = {
    "name": """Floor 2, Main room""",

    "times entered" : 0,

    "description":
    """ENTER DESCRIPTION HERE""",

    "dialogue" : [""],

    "exits":  {"north" : "Room_1_2", "east": "Room_2_2", "south" : "Exit_2", "west" : "Room_3_2"},

    "status" : "unlocked",

    "map" : """                             +-------------------+
                             |    Break room     |
                             +---------|---------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +--------Exit-------+
|      Office       |------- |     Main Room     |       |    Storage room   |
|                   |        |  (you are here)   |-------|                   | 
+-------------------+        |                   |       +-------------------+
                             +---------|---------+
                                       |
                             +---------|---------+
                             |       Exit        |
                             +-------------------+
""",

    "items": [item_storage_note],

    "key" : [item_saw, item_beam],

    "target" : room_exit_3,

    "inspectable" : False,

    "id" : "" 
}

room_1_2 = {
    "name": """Floor 2, Break room""",

    "times entered" : 0,

    "description":
    """ENTER DESCRIPTION HERE""",

    "dialogue" : ["As you step into the break room, you notice that all of the lights are still on. Strange..."],

    "exits":  {"south": "Main_2"},

    "status" : "unlocked",

    "map" : """                             +-------------------+
                             |      Break room   |
                             |   (you are here)  |
                             +---------|---------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +--------Exit-------+
|      Office       |------- |     Main Room     |-------|   Storage room    |
|                   |        |                   |       |                   | 
+-------------------+        |                   |       +-------------------+
                             +---------|---------+
                                       |
                             +---------|---------+
                             |       Exit        |
                             +-------------------+
""",


    "items": [],

    "key" : [item_saw, item_beam],

    "target" : room_exit_3,

    "inspectable" : False,

    "id" : "" 
}

room_2_2 = {
    "name": """Floor 2, Storage room""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : ["""As you enter the storage room, you spot a rather worn looking door, a few blows could probably open it.""", """After taking a look around, you see that one of the wooden beams holding the roof together has become dislodged, however it looks too heavy to carry at the moment.
Perhaps you could find a use for it?"""],

    "exits":  {"west": "Main_2", "east" : "Exit_3"},

    "status" : "unlocked",

    "map" : """                             +-------------------+
                             |      Break room   |
                             +---------|---------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------Exit--------+
|      Office       |------- |     Main Room     |       |    Storage room   |
|                   |        |                   |-------|   (you are here)  | 
+-------------------+        |                   |       +-------------------+
                             +---------|---------+
                                       |
                             +---------|---------+
                             |       Exit        |
                             +-------------------+
""",

    "items": [item_beam],

    "key" : [item_saw, item_beam],

    "target" : room_exit_3,

    "inspectable" : False,

    "id" : "" 
}

room_3_2 = {
    "name": """Floor 2, Office""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : ["As you enter the office, the walls spattered with blood, you spot a rusty looking saw perched on the desk."],

    "exits":  {"east": "Main_2"},

    "status" : "unlocked",

    "map" : """                             +-------------------+
                             |      Break room   |
                             +---------|---------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------Exit--------+
|      Office       |------- |     Main Room     |       |    Storage room   |
|   (you are here)  |        |                   |-------|                   | 
+-------------------+        |                   |       +-------------------+
                             +---------|---------+
                                       |
                             +---------|---------+
                             |       Exit        |
                             +-------------------+
""",

    "items": [item_saw],

    "key" : [item_saw, item_beam],

    "target" : room_exit_3,

    "inspectable" : False,

    "id" : "" 
}



