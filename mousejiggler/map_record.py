#Map movement recorder
import pyautogui

#Record user mouse movement for 20 seconds and store the map in a file
def map_record(letter_to_record, file):
    print("Enter R to start recording mouse movement")
    begin_recording = input()
    if(begin_recording == "R"):
        print("Starting recording...")
        local_map = [[0]*1080] * 1920
        pyautogui.move(0, 0, duration=1)
        for i in range(0, 10000):
            print(i)
            i += 1
            local_map[pyautogui.position()[0]][pyautogui.position()[1]] = 1
        file.write(letter_to_record + ": " + str(local_map) + "\n")

map_record("A", open("mouse_maps.txt", "w"))
        
        
