from grid import Grid
from solving_agent import brute_force_solving_agent, backtracking_solving_agent, pysat_solving_agent
from file import output_times
from cnf_handle import cnf_handle

def main():
    times: list[list[float]] = []

    for i in range (10):
        filename = "input/input_" + str(i) + ".txt"
        print(filename + ":")
        grid = Grid(filename)
        
        cnf_agent = cnf_handle()
        cnf_agent.generate_cnf(grid)

        brute_force_agent = brute_force_solving_agent(grid, cnf_agent)
        backtracking_agent = backtracking_solving_agent(grid, cnf_agent)
        pysat_agent = pysat_solving_agent(grid, cnf_agent)
        
        filename = "output/output_" + str(i) + ".txt"
        brute_force_agent.output_solution(filename)
        backtracking_agent.output_solution(filename)
        pysat_agent.output_solution(filename)

        if pysat_agent.solution:
            checkgrid3 = Grid(pysat_agent.solution)
            print("Pysat: ", "satisfiable" if checkgrid3.is_solved() else "not satisfiable")
            
        if backtracking_agent.solution:
            checkgrid2 = Grid(backtracking_agent.solution)
            print("Backtracking: ", "satisfiable" if checkgrid2.is_solved() else "not satisfiable")

        
        if brute_force_agent.solution:
            checkgrid1 = Grid(brute_force_agent.solution)
            print("Brute force: ", "satisfiable" if checkgrid1.is_solved() else "not satisfiable")
            
        time0 = []
        time0.append(brute_force_agent.time)
        time0.append(backtracking_agent.time)
        time0.append(pysat_agent.time)
        
        times.append(time0)
        
        print("\n")

    filename = "times"  + ".txt"
    output_times(filename, times)
    
if __name__ == "__main__":
    main()