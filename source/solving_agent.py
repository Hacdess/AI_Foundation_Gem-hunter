from copy import deepcopy
from grid import Grid
from cnf_handle import cnf_handle
from pysat.solvers import Solver
from pysat.formula import CNF
from typing import Optional
from file import write_output_file
import time

class solving_agent:
    def __init__(self, grid: Grid, cnf_agent: cnf_handle):
        self.grid = deepcopy(grid)
        self.cnf_agent = cnf_agent
        self.cnf = cnf_agent.cnf
        self.solution = []
        self.time = 0

    def solve(self) -> Optional[list[int]]:
        pass

    def get_solution(self):
        start = time.time()
        model = self.solve()
        self.time = time.time() - start

        if not model:
            return None

        solution = deepcopy(self.grid.grid)

        for var in model:
            pos = self.cnf_agent.var_to_pos(var)
            
            if var > 0:  # Chỉ quan tâm các biến dương
                solution[pos[0]][pos[1]] = 'T'  # Bẫy (Trap)
            else:
                solution[pos[0]][pos[1]] = 'G'  # Đá quý (Gem)
                
        rows, cols = len(solution), len(solution[0])
        
        for i in range(rows):
            for j in range(cols):
                if solution[i][j] == '_':
                    solution[i][j] = 'G'

        self.solution = solution
        return solution
        
    def output_solution(self, filename: str):
        pass

class brute_force_solving_agent(solving_agent):
    def __init__(self, grid: Grid, cnf_agent: cnf_handle):
        super().__init__(grid, cnf_agent)
        self.n_attempts = 2000000

    def solve(self) -> Optional[list[int]]:
        length = self.cnf_agent.var_counter - 1

        # Use binary representations to create all cases
        total = 1 << length

        assignments = [False] * length

        for bits in range(total):
            if self.n_attempts < 1:
                print("Brute force reached limit attemptss.")
                return None
            
            self.n_attempts -= 1
            
            for i in range(length):
                assignments[i] = bool((bits >> i) & 1)

            if self.cnf_agent.is_satisfiable(self.cnf, assignments):
                model = [var if assignments[var - 1] else -var for var in range(1, length + 1)]
                print("Brute force's model: ", model)
                return model

        print("Brute Force: No solution")
        return None
    
    def output_solution(self, filename: str):
        solution = self.get_solution()
        if not solution:
            print("Brute Force: No solution")
        write_output_file(solution, filename, "Brute force", True)
        
class backtracking_solving_agent(solving_agent):
    def __init__(self, grid: Grid, cnf_agent: cnf_handle):
        super().__init__(grid, cnf_agent)
        self.n_attempts = 2000000

    def solve(self) -> Optional[list[int]]:
        result = self.dpll(self.cnf_agent.cnf)

        if self.n_attempts < 1:
            print("Backtracking reached limit attemptss.")
                
        if result is None:
            return None

        sat, assignments = result
        if not sat:
            return None
        
        model = []
        for var in self.cnf_agent.get_variables(self.cnf):
            value = assignments.get(var, False)
            model.append(var if value else -var)

        print("Backtracking's model: ", model)
        return model

    def dpll(self, cnf: list[list[int]], assignments: dict[int, bool] = {}) -> Optional[tuple[bool, dict[int, bool]]]:
        if self.n_attempts < 1:
            return None
        self.n_attempts -= 1
        
        if not cnf:
            return True, assignments

        if any(len(clause) == 0 for clause in cnf):
            return False, {}

        # Find unassigned variables
        unassigned_lits = list(abs(lit) for clause in cnf for lit in clause if abs(lit) not in assignments)
        
        if not unassigned_lits:
            return False, {}  # Because there is no variable left to assign but cnf is still not satisfiable

        l = unassigned_lits[0] # Choose one unassigned variable to assign (the first one)

        for value in [True, False]:
            new_assignments = assignments.copy()
            new_assignments[l] = value

            new_cnf = []
            for clause in cnf:
                if (l if value else -l) in clause:
                    continue  # Clause is satifiable
                # Eliminates the literals that are assigned the opposite value. Ex: x1 = True -> eliminate neg(x1)
                new_clause = [lit for lit in clause if lit != (-l if value else l)] 
                new_cnf.append(new_clause)

            result = self.dpll(new_cnf, new_assignments)
            if result is not None:
                satisfiable, final_assignments = result
                if satisfiable:
                    return True, final_assignments

        return False, {}
    
    def output_solution(self, filename: str):
        solution = self.get_solution()
        if not solution:
            print("Backtracking: No solution")
        write_output_file(solution, filename, "Backtracking", False)
    
class pysat_solving_agent(solving_agent):
    def __init__(self, grid: Grid, cnf_agent: cnf_handle):
        super().__init__(grid, cnf_agent)

    def solve(self) -> Optional[list[int]]:
        solver = Solver()
        solver.append_formula(self.cnf)
        
        if solver.solve():
            model = solver.get_model()  # Lấy nghiệm
            print("Pysat's model: ", model)
            return model

        else:
            print("Pysat: No solution")
            return None

    def output_solution(self, filename: str):
        solution = self.get_solution()
        if not solution:
            print("Pysat: No solution")
        write_output_file(solution, filename, "Pysat", False)