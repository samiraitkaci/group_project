from items import *


exit_2 = {
    "name": "Exit room",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"north": "Main_2"},

    "status" : "locked",

    "map" : """                             +-------------------+
                             |      Room 1       |
                             +---------|---------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Room 3       |------- |     Main Room     |-------|       Room 2      | 
+-------------------+        |                   |       +-------------------+
                             +---------|---------+
                                       |
                             +---------|---------+
                             | Exit(you are here)|
                             +-------------------+
""",

    "items": []
}

   


main_2 = {
    "name": "Main room",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"north" : "Room1_2", "east": "Room2_2", "south" : "Exit_2", "west" : "Room3_2"},

    "status" : "unlocked",

    "map" : """                             +-------------------+
                             |      Room 1       |
                             +---------|---------+
                                       |
                             +---------|---------+
+-------------------+        |                   |       +-------------------+
|      Room 3       |------- |     Main Room     |-------|       Room 2      | 
+-------------------+        |   (you are here)  |       +-------------------+
                             +---------|---------+
                                       |
                             +---------|---------+
                             |       Exit        |
                             +-------------------+
""",

    "items": []
}

room1_2 = {
    "name": "Break Room",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"south": "Main_2"},

    "status" : "unlocked",

    "items": []

    
}

room2_2 = {
    "name": "Storage Room",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"west": "Main_2"},

    "status" : "unlocked",

    "items": []
}

room3_2 = {
    "name": "Office",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"east": "Main_2"},

    "status" : "unlocked",

    "items": []
}



