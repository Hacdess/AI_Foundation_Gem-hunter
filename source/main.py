from grid import Grid
import time
from solving_agent import brute_force_solving_agent, backtracking_solving_agent, pysat_solving_agent

filename = input("Nhap ten file: ")
grid = Grid(filename)
print(grid.grid)

brute_force_agent = brute_force_solving_agent(grid)
backtracking_agent = backtracking_solving_agent(grid)
pysat_agent = pysat_solving_agent(grid)

brute_force_res = brute_force_agent.solve()
backtracking_res = backtracking_agent.solve()
pysat_res = pysat_agent.solve()

if brute_force_res:
    print("Brute Force:", brute_force_res)
if backtracking_res:
    print("Backtracking: ", backtracking_res)
if pysat_res:
    print("Pysat: ", pysat_res)