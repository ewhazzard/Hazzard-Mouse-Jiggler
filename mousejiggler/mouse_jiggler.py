import pyautogui
import random
import map_record
import string

def random_jiggle():
    """Randomly jiggles the mouse for a set amount of time starting at the current mouse position

    Args:
        cur_pos (tupple): current mouse position retrieved by pyautogui.position()
        duration (_type_): amount of time to jiggle the mouse
    """
    cur_pos = pyautogui.position()
    duration = 100
    i = 0
    width,height = pyautogui.size()
    
    while(i < duration):
        try:
            random_x_step = random.randrange(-100, 100, 10)
            random_y_step = random.randrange(-100, 100, 10)
            new_pos = (cur_pos[0] + random_x_step, cur_pos[1] + random_y_step)
            pyautogui.moveTo(new_pos[0], new_pos[1], .5)
            i += 1
        except pyautogui.FailSafeException:
            cur_pos = (pyautogui.size()[0]/2, pyautogui.size()[1]/2)
            i += 1

#Trace the user inputed letter with the mouse from a mouse map
def custom_jiggler(letter):
    map_record.read_maps("mouse_map.txt")
    custom_map = map_record.map_dict[letter]
    # Loop through the map, drawing the letter
    for coord in custom_map:
        pyautogui.moveTo(coord[0], coord[1])

def main():
    print("Starting...")
    print("Enter 1 for random, 2 for custom")
    choice = input()
    if choice == "1":
        random_jiggle()
    else:
        print("Enter the letter you would like to be drawn")
        letter = input()
        custom_jiggler(letter)
    
main()
    