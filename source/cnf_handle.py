# the standard way to import PySAT:
from pysat.formula import CNF
from pysat.solvers import Solver
from itertools import combinations
from grid import Grid

class cnf_handle:
    def __init__(self):
        self.vars_dict = {}  # {(row, col): var_id}
        self.var_counter = 1  # var ID
        self.cnf: list[list[int]]

    def add_var(self, pos: tuple[int, int]):
        if pos not in self.vars_dict:
            self.vars_dict[pos] = self.var_counter
            self.var_counter += 1

    def pos_to_var(self, pos: tuple[int, int]):
        return self.vars_dict.get(pos)  # Return None if there is no key
    
    def var_to_pos(self, var: int):
        for pos, value in self.vars_dict.items():
            if abs(var) == value:
                return pos
        return None
    
    def convert_empty_pos_to_vars(self, grid: Grid):
        rows, cols = grid.rows, grid.cols

        for row in range(rows):
            for col in range(cols):
                if grid.grid[row][col] == '_':
                    self.add_var((row, col))

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
        self.convert_empty_pos_to_vars(grid)
        cnf = CNF()
        
        for i in range(rows):
            for j in range (cols):
                if isinstance(grid.grid[i][j], int):
                    n_traps = grid.grid[i][j]
                    
                    # Get integer neighbor (legal)
                    neighbors_vars = [
                        self.pos_to_var((row, col))
                        for (row, col) in grid.get_neighbors_positions(i, j)
                        if not isinstance(grid.grid[row][col], int)
                    ]

                    cnf.extend(self.generate_clause(neighbors_vars, n_traps))
        
        # Remove duplicated clauses
        cnf.clauses = [list(clause) for clause in set(tuple(sorted(clause)) for clause in cnf.clauses)]
        
        self.cnf = cnf
        return cnf

    def get_variables(self, cnf: CNF):
        variables = set()  # Set to avoid duplicates
        for clause in cnf.clauses:
            for literal in clause:
                variables.add(abs(literal))  # Only add the absolute value of the literal (i.e., the variable itself)
        return list(variables)
    
    def is_satisfiable_clause(self, clause: list[int], assignments: list[bool]):
        for literal in clause:
            var = abs(literal)
            value = assignments[var - 1] # vars start from 1

            # 1 literal is satisfiable, then the whole clause is satisfiable
            if (literal > 0 and value) or (literal < 0 and not value):
                return True
            
        return False
    
    def is_satisfiable(self, cnf: CNF, assignments: list[bool]):
        for clause in cnf.clauses:
            if not self.is_satisfiable_clause(clause, assignments):
                return False
        return True