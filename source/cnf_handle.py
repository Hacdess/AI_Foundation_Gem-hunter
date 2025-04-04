# the standard way to import PySAT:
from pysat.formula import CNF
from pysat.solvers import Solver
from grid import Grid, pos_to_var, var_to_pos
from itertools import combinations
from copy import deepcopy

class CNF_handle:
    def generate_clause(self, vars: list[int], n_traps: int):
        clause = []

        length = len(vars) - n_traps
        if (length < 0):
            return clause
        
        # At least n traps
        for combination in combinations(vars, length + 1): 
            clause.append([v for v in combination])

        # No more than n trap
        # If n_trap == len(vars), it should be included in the previous part
        if (length > 0):
            for combination in combinations(vars, n_traps + 1):
                clause.append([-v for v in combination])

        # Then we will get exactly n traps
        return clause

    def generate_cnf(self, grid: Grid):
        rows, cols = grid.rows, grid.cols
        cnf = CNF()
        
        for i in range(rows):
            for j in range (cols):
                if isinstance(grid.grid[i][j], int):
                    n_traps = grid.grid[i][j]
                    
                    # Get integer neighbor (legal)
                    neighbors_var = [
                        pos_to_var(row, col, cols)
                        for (row, col) in grid.get_neighbors_positions(i, j)
                        if not isinstance(grid.grid[row][col], int)
                    ]

                    cnf.extend(self.generate_clause(neighbors_var, n_traps))
        
        # Remove duplicated clauses
        cnf.clauses = [list(clause) for clause in set(tuple(sorted(clause)) for clause in cnf.clauses)]
        return cnf

    def is_satisfiable_clause(self, clause: list[int], assignments: list[int]):
        for literal in clause:
            var = abs(literal)
            value = assignments[var]

            # 1 literal is satisfiable, then the whole clause is satisfiable
            if (literal > 0 and value) or (literal < 0 and not value):
                return True
            
        return False
    
    def is_satisfiable(self, cnf: list[list[int]], assignments: list[int]):
        for clause in cnf:
            if not self.is_satisfiable_clause(cnf, assignments):
                return False
        return True