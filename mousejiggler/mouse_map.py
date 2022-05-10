#Mouse Map class that defines a map of mouse movements


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



class mouse_map:
    m_map = [(0,0)]
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