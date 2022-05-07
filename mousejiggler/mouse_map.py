#Mouse Map class that defines a map of mouse movements

class mouse_map:
    m_map = [0][0]

    #Constructor for mouse_map class
    #Args: self, height, width
    #Returns: None
    def __init__(self, height, width):
        m_map = [[0 for i in range(width)] for j in range(height)]
        
    def get_map(self):
        return m_map
    
    def set_map(self, key):
        pass      