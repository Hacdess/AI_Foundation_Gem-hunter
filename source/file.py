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

def write_output_file(solution: list, filename: str):
    with open(filename, 'w') as file:
        for i in range(len(solution)):
            for j in range(len(solution[0])):
                file.write(str(solution[i][j]))
                file.write(", ")
            file.write('\n')
    
