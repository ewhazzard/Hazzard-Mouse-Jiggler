import pyautogui
import random

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
            random_step = random.randrange(-100, 100, 10)
            new_pos = (cur_pos[0] + random_step, cur_pos[1] + random_step)
            pyautogui.moveTo(new_pos[0], new_pos[1], .5)
            i += 1
            cur_pos = pyautogui.position()
        except pyautogui.FailSafeException:
            cur_pos = (pyautogui.size()[0]/2, pyautogui.size()[1]/2)
            i += 1
        

