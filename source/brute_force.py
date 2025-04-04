from grid import Grid
from copy import deepcopy
from cnf_handle import CNF_handle

class brute_force_agent:
    def solve(self, grid: Grid):
        solution = deepcopy(grid)
        empty_pos = solution.get_empty_pos()

        n_empty = len(empty_pos)
        
        # Get the legnth of binary reprsentation of n_empty
        total_combinations = 2 ** n_empty

        for comb in range(total_combinations):
            binary_representation = [(comb >> i) & 1 for i in range(n_empty)]

            for idx, (row, col) in enumerate(empty_pos):
                solution.grid[row][col] = 'T' if binary_representation[idx] else 'G'

            if solution.is_solved():
                return solution.grid

        return None


