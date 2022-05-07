import pyautogui
import random
import mouse_map
import string

def random_jiggle(cur_pos, duration):
    """Randomly jiggles the mouse for a set amount of time starting at the current mouse position

    Args:
        cur_pos (tupple): current mouse position retrieved by pyautogui.position()
        duration (_type_): amount of time to jiggle the mouse
    """
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

default_map = mouse_map.mouse_map(pyautogui.size()[0], pyautogui.size()[1])
#Dictionary of mouse map objects
map_dict = {
        'A': default_map,
        'B': default_map,
        'C': default_map,
        'D': default_map,
        'E': default_map,
        'F': default_map,
        'G': default_map,
        'H': default_map,
        'I': default_map,
        'J': default_map,
        'K': default_map,
        'L': default_map,
        'M': default_map,
        'N': default_map,
        'O': default_map,
        'P': default_map,
        'Q': default_map,
        'R': default_map,
        'S': default_map,
        'T': default_map,
        'U': default_map,
        'V': default_map,
        'W': default_map,
        'X': default_map,
        'Y': default_map,
        'Z': default_map
    }

def fill_dict():
    alphabet =  list(string.ascii_lowercase)
    for item in alphabet:
        map_dict[item] = mouse_map.mouse_map(pyautogui.size()[0], pyautogui.size()[1])
        
        

def main():
    fill_dict()
    