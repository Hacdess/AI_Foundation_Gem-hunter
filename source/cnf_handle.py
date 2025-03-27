# the standard way to import PySAT:
from pysat.formula import CNF
from pysat.solvers import Solver
from grid import Grid
from itertools import combinations
from copy import deepcopy

class CNF_solving_agent:
    def generate_cnf(self, grid: Grid):
        rows, cols = grid.rows, grid.cols
        cnf = CNF()

        var = lambda row, col : row * cols + col + 1
        
        for i in range(rows):
            for j in range (cols):
                if isinstance(grid.grid[i][j], int):
                    n_traps = grid.grid[i][j]
                    
                    # Get integer neighbor (legal)
                    neighbors = [
                        var(row, col)
                        for (row, col) in grid.get_neighbors_positions(i, j)
                        if not isinstance(grid.grid[row][col], int)
                    ]

                    # Get traps
                    length = len(neighbors) - n_traps
                    for combination in combinations(neighbors, length + 1): 
                        cnf.append([v for v in combination])
                    
                    # Get gems
                    for combination in combinations(neighbors, n_traps + 1):
                        cnf.append([-v for v in combination])
        
        # Remove duplicated clauses
        cnf.clauses = [list(clause) for clause in set(tuple(sorted(clause)) for clause in cnf.clauses)]
        return cnf

    def solve_cnf(self, cnf, grid: Grid):
        solution = deepcopy(grid.grid)

        cols = grid.cols
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
                
                if not isinstance(solution[row][col], int):
                    if var > 0:  # Chỉ quan tâm các biến dương
                        solution[row][col] = 'T'  # Bẫy (Trap)
                    else:
                        solution[row][col] = 'G'  # Đá quý (Gem)

            return solution
        else:
            print("No solution")
            return None
