# Gem Hunter Game

## Description
The Gem Hunter game is a puzzle where players explore a grid to find hidden gems while avoiding traps. Each tile with a number represents the number of traps surrounding it. (Number from 1 - 8). Each tile without a number represents the unknown position. Those positions must be Trap (T) or Gem(G). This program's task is to formulate the problem as Conjunctive Normal Form (CNF) constraints and solve it using logic.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Algorithms](#algorithms)
- [Requirements](#requirements)

## Installation
To run the Gem Hunter game, ensure you have Python installed on your machine. You will also need to install the pysat library. You can install it using pip:

```bash
pip install pysat
```

## Usage
### Installation
- Method 1: Clone the repository: [text](https://github.com/Hacdess/AI_Foundation_Gem-hunter.git).
- Method 2: Using the ZIP File.
### Running
- Prepare your input files in the input directory. The input files should be named input_x.txt where x is the number of the input.
- Run the main program:
    - Method 1: Navigate to the AI_Foundation_Gem-hunter directory then use the command:
    ```bash
    python source/main.py
    ```
    - Method 2: Visit file main.py and use the Run botton.
- The output will be saved in the output directory as output_x.txt corresponding to each input file.

## File Structure
``` bash
MultipleFiles/
│
├── cnf_handle.py        # Handles CNF generation and variable management
├── file.py              # Contains functions for reading and writing files
├── grid.py              # Defines the Grid class for managing the game grid
├── main.py              # Main entry point for the game
├── solving_agent.py     # Contains solving algorithms (brute force, backtracking, pysat)
└── Lab.pdf              # Documentation and requirements for the project
```

## Algorithms
The game implements three solving algorithms:

- **Brute Force**: 
  - Tries all possible combinations to find a solution.
  
- **Backtracking**: 
  - Uses a recursive approach to find a solution by exploring possible variable assignments.
  
- **PySAT**: 
  - Utilizes the PySAT library to solve the CNF problem efficiently.

## Requirements
Python 3.x
pysat library