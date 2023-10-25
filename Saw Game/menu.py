from art import *
from playsound import playsound
import threading
from game import start_game
from gameparser import *
from player import player_name
from colorama import *
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


minutes = "10:00"
minutes_as_int = 10
level = "Hard"

def play_background_sound(audio_path):
    while True:
        playsound(audio_path)

def main():
    global minutes
    global minutes_as_int
    global player_name
    print("\n" * 1000)
    print(Fore.RED + "**********************************")
    print(Fore.RED + "**********************************")
    tprint("saw","poison")
    print(Fore.RED + "**********************************")
    print(Fore.RED + "**********************************")
    print()
    print(Fore.WHITE + "Difficulty: " + level)
    print(Fore.RED + "> START")
    print(Fore.WHITE + "> DIFFICULTY")
    print(Fore.RED + "> EXIT")
    

    choice = input(Fore.WHITE + ">")
    normalise_input(choice)
    if choice == "start":
        print("\n" * 1000)
        start_game(minutes, minutes_as_int)
    elif choice == "difficulty":
        select_difficulty()
    elif choice == "exit":
        exit()
    else: 
        print("Invalid choice")
        input()
        main()
    

    # Your game logic here

def select_difficulty():
    global level
    global minutes
    global minutes_as_int
    print("\n" * 1000)
    print("Select difficulty:")
    print("> EASY")
    print("> MEDIUM")
    print("> HARD")
    difficulty = input(">")

    normalise_input(difficulty)
    if difficulty == "easy":
        minutes = "30:00"
        minutes_as_int = 40
        level = "easy"
        main()
    if difficulty == "medium":
        minutes = "20:00"
        minutes_as_int = 30
        level = "medium"
        main()
    if difficulty == "hard":
        minutes = "10:00"
        minutes_as_int = 20
        level = "hard"
        main()
    

if __name__ == "__main__":
    background_sound_thread = threading.Thread(target=play_background_sound, args=("music_menu.mp3",))

    background_sound_thread.start()

    # Your game logic runs here
    while True:
        main()


