from art import *
from playsound import playsound
import threading


def play_background_sound(audio_path):
    while True:
        playsound(audio_path)

def main():
    tprint("SAW")
    print("hello world")
    input()

    # Your game logic here

if __name__ == "__main__":
    background_sound_thread = threading.Thread(target=play_background_sound, args=("music_menu.mp3",))
    background_sound_thread.start()

    # Your game logic runs here
    while True:
        main()