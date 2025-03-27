from grid import Grid
from copy import deepcopy

class BruteForce:
    def get_empty_pos(self, grid: Grid):
        rows, cols = grid.rows, grid.cols

        return [
            (row, col)
            for row in range(rows)
            for col in range(cols)
            if grid.grid[row][col] == '_'
        ]

    def solve(self, grid: Grid):
        solution = deepcopy(grid)
        empty_pos = self.get_empty_pos(solution)

        n_empty = len(empty_pos)
        
        # Get the legnth of binary reprsentation of n_empty
        total_combinations = 2 ** n_empty

        for comb in range(total_combinations):
            binary_representation = [(comb >> i) & 1 for i in range(n_empty)]

            for idx, (row, col) in enumerate(empty_pos):
                solution.grid[row][col] = 'T' if binary_representation[idx] else 'G'

            if solution.is_correct_solution():
                return solution.grid

        return None


