from file import read_input_file

class Grid:
    def __init__(self, input_file):
        self.grid = read_input_file(input_file)
        self.cols = len(self.grid[0])
        self.rows = len(self.grid)
    
def is_valid_pos(row: int, col: int, rows: int, cols: int):
    return (0 <= row < rows and 0 <= col < cols)