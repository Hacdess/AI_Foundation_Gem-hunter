from file import read_input_file

class Grid:
    def __init__(self, input_file):
        self.grid = read_input_file(input_file)
        self.width = len(self.grid[0])
        self.height = len(self.grid)
    
    def is_valid_pos(self, x: int, y: int):
        return x >= 0 and y >= 0 and x < self.width and y < self.height

