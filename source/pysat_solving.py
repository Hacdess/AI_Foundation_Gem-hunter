from cnf_handle import CNF_handle

    # def solve_cnf(self, cnf, grid: Grid):
    #     solution = deepcopy(grid.grid)

    #     cols = grid.cols
    #     solver = Solver()
    #     solver.append_formula(cnf)
        
    #     if solver.solve():
    #         model = solver.get_model()  # Lấy nghiệm
    #         print(model)
    #         # True = Trap, False = Gold
    #         # var = (row × cols) + col + 1
    #         for var in model:
    #             col = (abs(var) - 1) % cols
    #             row = (abs(var) - 1) // cols
                
    #             if not isinstance(solution[row][col], int):
    #                 if var > 0:  # Chỉ quan tâm các biến dương
    #                     solution[row][col] = 'T'  # Bẫy (Trap)
    #                 else:
    #                     solution[row][col] = 'G'  # Đá quý (Gem)

    #         return solution
    #     else:
    #         print("No solution")
    #         return None