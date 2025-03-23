def read_input_file(filename: str):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            grid.append([int(cell) if cell.isdigit() else cell for cell in row])
    return grid