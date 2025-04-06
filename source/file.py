import os

def read_input_file(filename: str):
    if not os.path.exists(filename):
        print("File", filename, "does not exist\n")
        return None
    
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(', ')
            grid.append([int(cell) if cell.isdigit() else cell for cell in row])
    return grid

def write_output_file(solution: list[list], filename: str, solution_name: str, overwrite: bool):
    with open(filename, 'w' if overwrite else 'a') as file:
        file.write(solution_name)
        file.write(":\n")
        if not solution:
            file.write("No solution\n\n")
            return
        
        cols = len(solution[0])
        for i in range(len(solution)):
            for j in range(len(solution[0])):
                file.write(str(solution[i][j]))
                
                if j < cols - 1:
                    file.write(", ")
            file.write('\n')
        file.write('\n')    

def output_times(filename: str, times: list[list[float]]):
    if not times:
        return

    with open(filename, 'w') as file:
        file.write(f"{'Testcase':>10} | {'Brute Force (s)':>20} | {'Backtracking (s)':>20} | {'PySAT (s)':>20}\n")
        for idx, row in enumerate(times):
            bf, bt, ps = (t for t in row)  # convert to milliseconds
            file.write(f"{idx:10} | {bf:20.6f} | {bt:20.6f} | {ps:20.6f}\n")
