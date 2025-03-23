# the standard way to import PySAT:
from pysat.formula import CNF
from pysat.solvers import Solver

def get_neighbors(row, col, n_rows, n_cols):
    return[(row + i, col + j) for i in (-1, 0, 1) for j in (-1, 0, 1)
            if (i != 0 or j != 0) and 0 <= row + i < n_rows and 0 <= col + j < n_rows]

def generate_cnf(grid):
    rows, cols = len(grid), len(grid[0])
    cnf = CNF()
