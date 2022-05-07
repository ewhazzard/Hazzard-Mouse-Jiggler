#Mouse Map class that defines a map of mouse movements

from threading import local


class mouse_map:
    m_map = [0][0]
    letter_maps = {
        
    }

    #Constructor for mouse_map class
    #Args: self, height, width
    #Returns: None
    def __init__(self, height, width):
        self.m_map = [[0 for i in range(width)] for j in range(height)]
        
    def get_map(self):
        return self.m_map
    
    def set_map(self, key):
        local_map = [0][0]
        self.letter_maps[key] = local_map