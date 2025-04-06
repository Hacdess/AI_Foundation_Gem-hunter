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
    if not solution:
        print("No solution")
        return
        
    with open(filename, 'w' if overwrite else 'a') as file:
        file.write(solution_name)
        file.write('\n')
        for i in range(len(solution)):
            for j in range(len(solution[0])):
                file.write(str(solution[i][j]))
                file.write(", ")
            file.write('\n')
        file.write('\n')    
