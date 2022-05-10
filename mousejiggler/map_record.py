#Map movement recorder
from threading import local
import pyautogui
import time

#Record user mouse movement for 3 seconds and store the map in a file
def map_record(letter_to_record, file):
    print("Enter R to start recording mouse movement")
    begin_recording = input()
    if(begin_recording == "R"):
        print("Starting recording for 3 seconds...")
        local_map = []
        local_map.append(pyautogui.position())
        last_pos = pyautogui.position()
        pyautogui.move(0, 0, duration=1)
        end_time = time.time() + 3
        while time.time() < end_time:
            if (pyautogui.position() != last_pos):
                local_map.append(pyautogui.position())
            last_pos = pyautogui.position()
        file.write(letter_to_record + ": " + str(local_map) + "\n")

map_record("A", open("mouse_maps.txt", "w"))
        
        
