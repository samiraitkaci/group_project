from items import *


room_exit_2 = {
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

   


room_main_2 = {
    "name": "Main room 2",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"north" : "Room_1_2", "east": "Room_2_2", "south" : "Exit_2", "west" : "Room_3_2"},

    "status" : "unlocked",

    "items": []
}

room_1_2 = {
    "name": "Room 1",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"south": "Main_2"},

    "status" : "unlocked",

    "items": []
}

room_2_2 = {
    "name": "Room 2",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"west": "Main_2"},

    "status" : "unlocked",

    "items": []
}

room_3_2 = {
    "name": "Room 3",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"east": "Main_2"},

    "status" : "unlocked",

    "items": []
}



