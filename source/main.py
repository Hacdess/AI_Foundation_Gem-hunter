from cnf_handle import CNF_solving_agent
from grid import Grid

solving_agent = CNF_solving_agent()

filename = input("Nhap ten file: ")
grid = Grid(filename)
print(grid.grid)
cnf = solving_agent.generate_cnf(grid)
print(cnf)
solution = solving_agent.solve_cnf(cnf, grid)
print(solution)
