from grid import Grid
from copy import deepcopy
from cnf_handle import CNF_handle

class backtracking_agent:
    def dpll_backtracking(self, grid: Grid, empty_pos: list, idx = 0):
        print(idx, len(empty_pos))

        if idx == len(empty_pos):
            return grid.is_solved()
        
        row, col = empty_pos[idx]
        
        # Try 'T'
        grid.grid[row][col] = 'T'
        if grid.is_correct_pos(row, col) and self.dpll_backtracking(grid, empty_pos, idx + 1):
            return True
        print("hi")

        # Try 'G'
        grid.grid[row][col] = 'G'
        if grid.is_correct_pos(row, col) and self.dpll_backtracking(grid, empty_pos, idx + 1):
            return True

        grid.grid[row][col] = '_'
        return False

    def solve(self, grid: Grid):
        solution = deepcopy(grid)
        empty_pos = solution.get_empty_pos()

        if self.dpll_backtracking(solution, empty_pos):
            return solution.grid
        
        return None