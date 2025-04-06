from grid import Grid
import time
from solving_agent import brute_force_solving_agent, backtracking_solving_agent, pysat_solving_agent

filename = input("Enter input file: ")
grid = Grid(filename)
print(grid.grid)

brute_force_agent = brute_force_solving_agent(grid)
backtracking_agent = backtracking_solving_agent(grid)
pysat_agent = pysat_solving_agent(grid)

filename = input("Enter output file: ")
brute_force_agent.output_solution(filename)
backtracking_agent.output_solution(filename)
pysat_agent.output_solution(filename)

if brute_force_agent.solution:
    checkgrid1 = Grid(brute_force_agent.solution)
    print("Brute force: ", checkgrid1.is_solved())

if backtracking_agent.solution:
    checkgrid2 = Grid(backtracking_agent.solution)
    print("Backtracking: ", checkgrid2.is_solved())

if pysat_agent.solution:
    checkgrid3 = Grid(pysat_agent.solution)
    print("Pysat: ", checkgrid3.is_solved())