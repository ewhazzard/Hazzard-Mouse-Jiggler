#Map movement recorder
from threading import local
import pyautogui
import time
import re

#Dictionary of mouse maps to trace each letter on the screen. Each map is a list of mouse coordinates (x pos, y pos).
map_dict = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
        'G': 0,
        'H': 0,
        'I': 0,
        'J': 0,
        'K': 0,
        'L': 0,
        'M': 0,
        'N': 0,
        'O': 0,
        'P': 0,
        'Q': 0,
        'R': 0,
        'S': 0,
        'T': 0,
        'U': 0,
        'V': 0,
        'W': 0,
        'X': 0,
        'Y': 0,
        'Z': 0
    }

#Record user mouse movement for 3 seconds and store the map in a file
def map_record(letter_to_record, file):
    print("Enter R to start recording mouse movement for " + letter_to_record)
    begin_recording = input()
    if(begin_recording == "R"):
        print("Starting recording for 3 seconds...")
        local_map = []
        local_map.append((pyautogui.position()[0], pyautogui.position()[1]))
        last_pos = pyautogui.position()
        pyautogui.move(0, 0, duration=1)
        end_time = time.time() + 3
        while time.time() < end_time:
            if (pyautogui.position() != last_pos):
                local_map.append((pyautogui.position()[0], pyautogui.position()[1]))
            last_pos = pyautogui.position()
        file.write(letter_to_record + ": " + str(local_map) + "\n")
        print("Recording complete")
        return local_map
        


#Fill the map_dict with mouse map for each letter
def fill_map_dict():
    file = open("mouse_map.txt", "w")
    for letter in map_dict:
        map_dict[letter] = map_record(letter, file)
    file.close()

def read_maps(file_name):
   with open(file_name) as f:
        for line in f:
            letter, m_map = line.split(': ')
            m_map = parse_tuple_string(m_map)
            map_dict[letter] = m_map
    
  
#Function that takes in a string representation of a list of tuples and parses it into a list of tuples          
def parse_tuple_string(tuple_string):
    tuple_list = re.findall(r'\(\d+, \d+\)', tuple_string)
    parsed_tuple_list = []
    for tup in tuple_list:
        parsed_tuple_list.append((int(tup[1:4]),int(tup[6:9])))
    return parsed_tuple_list
