from items import *
from floor4 import *

room_exit_3 = {
    "name": """Floor 3, Exit room""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : ["""Another rush of adrenaline strikes you as you use the sawed-off wooden beam to barge your way in to the next room, the final one according to the map. 
You hope, at least. With the time left growing ever shorter, you quickly come to your senses to once again search for the solution to your conundrum and to be able to escape unscathed."""],

    "exits":  {"north": "Main_3"},

    "status" : "locked",

    "map" : """,
                 
       
+-------------------+        +-------------------+       +--------Exit-------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|                   |        |                   |       |                   |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Cell 1       |------- |     Main room     |-------|      Cell 2       |
|                   |        |                   |       |                   | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |        Exit       |       |     Bathroom 2    |
|                   |        |   (you are here)  |       |                   |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : True,

    "id" : "" 
}

room_main_3 = {
    "name": """Floor 3, Main room""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : ["As you enter the final floor's main room you spot a piece of paper with what seems to be a code written on it."],

    "exits":  {"west" : "Cell_1", "east": "Cell_2", "south" : "Exit_3", "north" : "Cell_3"},

    "status" : "unlocked",

    "map" : """             
       
+-------------------+        +-------------------+       +-------Exit -------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|                   |        |                   |       |                   |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Cell 1       |------- |    Main room      |-------|      Cell 2       |
|                   |        |   (you are here)  |       |                   | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |                   |       |     Bathroom 2    |
|                   |        |        Exit       |       |                   |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [item_code_1, item_code_2, item_code_3, item_code_4],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : False,

    "id" : "" 
}

room_cell_1 = {
    "name": """Floor 3, Cell 1""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : [""],

    "exits":  {"east": "Main_3", "south": "Bathroom_1"},

    "status" : "unlocked",

    "map" : """             
       
+-------------------+        +-------------------+       +--------Exit-------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|                   |        |                   |       |                   |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|       Cell 1      |------- |     Main room     |-------|      Cell 2       |
|   (you are here)  |        |                   |       |                   | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |                   |       |     Bathroom 2    |
|                   |        |        Exit       |       |                   |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : False,

    "id" : "" 
}

room_cell_2 = {
    "name": """Floor 3, Cell 2""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : [""],

    "exits":  {"west": "Main_3", "south" : "Bathroom_2"},

    "status" : "unlocked",

    "map" : """             
       
+-------------------+        +-------------------+       +-------Exit--------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|                   |        |                   |       |                   |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Cell 1       |------- |    Main room      |-------|      Cell 2       |
|                   |        |                   |       |   (you are here)  | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |                   |       |     Bathroom 2    |
|                   |        |        Exit       |       |                   |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : False,

    "id" : "" 
}

room_cell_3 = {
    "name": """Floor 3, Cell 3""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : [""],

    "exits":  {"south": "Main_3", "west": "Bathroom_3", "east": "Dugout"},

    "status" : "unlocked",

    "map" : """             
       
+-------------------+        +-------------------+       +--------Exit-------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|                   |        |   (you are here)  |       |                   |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Cell 1       |------- |     Main room     |-------|      Cell 2       |
|                   |        |                   |       |                   | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |                   |       |     Bathroom 2    |
|                   |        |        Exit       |       |                   |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : False,

    "id" : "" 
}

room_bathroom_1 = {
    "name": """Floor 3, Bathroom 1""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : [""],

    "exits":  {"north": "Cell_1"},

    "status" : "unlocked",

    "map" : """             
       
+-------------------+        +-------------------+       +--------Exit-------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|                   |        |                   |       |                   |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Cell 1       |------- |     Main room     |-------|      Cell 2       |
|                   |        |                   |       |                   | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |                   |       |     Bathroom 2    |
|   (you are here)  |        |        Exit       |       |                   |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : False,

    "id" : "" 
}

room_bathroom_2 = {
    "name": """Floor 3, Bathroom 2""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : [""],

    "exits":  {"north": "Cell_2"},

    "status" : "unlocked",

   "map" : """             
       
+-------------------+        +-------------------+       +--------Exit-------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|                   |        |                   |       |                   |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Cell 1       |------- |     Main room     |-------|      Cell 2       |
|                   |        |                   |       |                   | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |                   |       |     Bathroom 2    |
|                   |        |        Exit       |       |   (you are here)  |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : False,

    "id" : "" 
}

room_bathroom_3 = {
    "name": """Floor 3, Bathroom 3""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : [""],

    "exits":  {"east": "Cell_3"},

    "status" : "unlocked",

   "map" : """             
       
+-------------------+        +-------------------+       +-------Exit--------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|  (you are here)   |        |                   |       |                   |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Cell 1       |------- |     Main room     |-------|      Cell 2       |
|                   |        |                   |       |                   | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |                   |       |     Bathroom 2    |
|                   |        |        Exit       |       |                   |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : False,

    "id" : "" 
}

room_dugout = {
    "name": """Floor 3, Dugout room""",

    "times entered" : 0,

    "description":
    """""",

    "dialogue" : [""],

    "exits":  {"west": "Cell_3", "east" : "Final_room"},

    "status" : "unlocked",

   "map" : """             
       
+-------------------+        +-------------------+       +--------Exit-------+
|     Bathroom 3    |--------|       Cell 3      |-------|    Dug Out Room   |
|                   |        |                   |       |   (you are here)  |
+-------------------+        +---------|---------+       +-------------------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Cell 1       |------- |     Main room     |-------|      Cell 2       |
|                   |        |                   |       |                   | 
+---------|---------+        |                   |       +---------|---------+
          |                  +---------|---------+                 |
          |                            |                           |
+---------|---------+        +---------|---------+       +---------|---------+
|     Bathroom 1    |        |                   |       |     Bathroom 2    |
|                   |        |        Exit       |       |                   |
+-------------------+        |                   |       +-------------------+                    
                             +-------------------+       
""",

    "items": [],

    "key" : [item_code_1, item_code_2, item_code_3, item_code_4],

    "target" : final_room,

    "inspectable" : False,

    "id" : "" 
}

