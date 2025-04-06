from file import read_input_file

class Grid:
    def __init__(self, input_file):
        self.grid = read_input_file(input_file)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0

    def is_valid_pos(self, row: int, col: int):
        return (0 <= row < self.rows and 0 <= col < self.cols)

    def get_neighbors_positions(self, row: int, col: int):
        if not self.is_valid_pos(row, col):
            return None
        
        return[
            (row + i, col + j) 
            for i in (-1, 0, 1) 
            for j in (-1, 0, 1)
            # Check valid pos
            if (i != 0 or j != 0) and self.is_valid_pos(row + i, col + j)
        ]
    
    def count_surrounding_traps(self, row: int, col: int):
        n_trap = 0
        neighbors = self.get_neighbors_positions(row, col)
        
        for pos in neighbors:
            if self.grid[pos[0]][pos[1]] == 'T':
                n_trap += 1

        return n_trap
    
    def get_empty_pos(self):
        return [
            (row, col)
            for row in range(self.rows)
            for col in range(self.cols)
            if self.grid[row][col] == '_'
        ]

    def is_correct_pos(self, row: int, col: int):
        if not self.is_valid_pos(row, col):
            return False
        
        return self.count_surrounding_traps(row, col) == self.grid[row][col]
    
    def is_solved(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if isinstance(self.grid[i][j], int) and not self.is_correct_pos(i, j):
                    return False
                
        return True