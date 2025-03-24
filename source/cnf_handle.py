# the standard way to import PySAT:
from pysat.formula import CNF
from pysat.solvers import Solver
from grid import Grid
from itertools import combinations
from copy import deepcopy

class CNF_solving_agent:        
    def get_neighbors_positions(self, row, col, n_rows, n_cols):
        return[(row + i, col + j) for i in (-1, 0, 1) for j in (-1, 0, 1)
                if (i != 0 or j != 0) and 0 <= row + i < n_rows and 0 <= col + j < n_cols]

    def logical_var_converter(self, row, col, n_cols):
        # Return value n => x_n
        # Example: return 12 => x_12
        return row * n_cols + col + 1
    
    def generate_cnf(self, grid: Grid):
        rows, cols = grid.rows, grid.cols
        cnf = CNF()
        
        for i in range(rows):
            for j in range (cols):
                if isinstance(grid.grid[i][j], int):
                    n_traps = grid.grid[i][j]
                    
                    # Get integer neighbor (legal)
                    neighbors = [
                        self.logical_var_converter(row, col, cols)
                        for (row, col) in self.get_neighbors_positions(i, j, rows, cols)
                        if isinstance(grid.grid[row][col], int)
                    ]

                    # Get traps
                    for combination in combinations(neighbors, n_traps): 
                        cnf.append([v for v in combination])
                    
                    # Get golds
                    length = len(neighbors) - n_traps
                    if length >= 0:
                        for combination in combinations(neighbors, length):
                            cnf.append([-v for v in combination])
        
        return cnf

    def solve_cnf(self, cnf, grid: Grid):
        solution = deepcopy(grid.grid)

        rows, cols = grid.rows, grid.cols
        solver = Solver()
        solver.append_formula(cnf)
        
        if solver.solve():
            model = solver.get_model()  # Lấy nghiệm
            print(model)
            # True = Trap, False = Gold
            # var = (row × cols) + col + 1
            for var in model:
                col = (abs(var) - 1) % cols
                row = (abs(var) - 1) // cols
                
                if var > 0:  # Chỉ quan tâm các biến dương
                    solution[row][col] = 'T'  # Bẫy (Trap)
                elif var < 0:

                    solution[row][col] = 'G'  # Đá quý (Gold)

            return solution
        else:
            print("Không có nghiệm hợp lệ!")
            return None
