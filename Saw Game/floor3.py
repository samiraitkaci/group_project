from items import *

room_exit_3 = {
    "name": "Exit room",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"north": "Main_3"},

    "status" : "unlocked",

    "items": []
}

room_main_3 = {
    "name": "Main room 3",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"north" : "Room_1_3", "east": "Room_2_3", "south" : "Exit_3", "west" : "Room_3_3"},

    "status" : "unlocked",

    "items": []
}

room_1_3 = {
    "name": "Room 1",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"south": "Main_3"},

    "status" : "unlocked",

    "items": []
}

room_2_3 = {
    "name": "Room 2",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"west": "Main_3"},

    "status" : "unlocked",

    "items": []
}

room_3_3 = {
    "name": "Room 3",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"east": "Main_3"},

    "status" : "unlocked",

    "items": []
}

