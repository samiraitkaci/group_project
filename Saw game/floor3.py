from items import *

exit_3 = {
    "name": "Exit room",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"north": "Main_3"},

    "status" : "unlocked",

    "items": []
}

main_3 = {
    "name": "Main room 3",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"north" : "Room1_3", "east": "Room2_3", "south" : "Exit_3", "west" : "Room3_3"},

    "status" : "unlocked",

    "items": []
}

room1_3 = {
    "name": "Room 1",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"south": "Main_3"},

    "status" : "unlocked",

    "items": []
}

room2_3 = {
    "name": "Room 2",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"west": "Main_3"},

    "status" : "unlocked",

    "items": []
}

room3_3 = {
    "name": "Room 3",

    "description":
    """ENTER DESCRIPTION HERE""",

    "exits":  {"east": "Main_3"},

    "status" : "unlocked",

    "items": []
}

