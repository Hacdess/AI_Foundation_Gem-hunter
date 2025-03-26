from cnf_handle import CNF_solving_agent
from grid import Grid
from file import write_output_file
import time

solving_agent = CNF_solving_agent()

filename = input("Nhap ten file: ")
grid = Grid(filename)
print(grid.grid)

start = time.time()
cnf = solving_agent.generate_cnf(grid)
solution = solving_agent.solve_cnf(cnf, grid)
end = time.time()
elapsed_time_ms = (end - start) * 1000
print(f"Thời gian thực thi: {elapsed_time_ms:.10f} ms")

print(solution)
filename = input("Nhap ten file: ")
write_output_file(solution, filename)