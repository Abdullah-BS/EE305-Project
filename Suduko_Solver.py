import tkinter as tk
from dokusan import generators
import numpy as np

def generate():
    grid = generators.random_sudoku(avg_rank=150)
    grid = str(grid)
    grid = list(grid)
    grid = np.array(grid).reshape(9,9)
    grid = grid.astype(int)
    grid = grid.tolist()
    return grid

def is_valid_move(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return True  # Puzzle solved
    else:
        row, col = find
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack
    return False

class SudokuGUI:
    def __init__(self, master, initial_grid):
        self.master = master
        self.grid = initial_grid.copy()
        self.solution = [row[:] for row in self.grid]
        solve_sudoku(self.solution)  # Solve and store the solution without showing it
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        master.title("Sudoku Solver")

        for i in range(9):
            for j in range(9):
                self.cells[i][j] = tk.Entry(master, width=2, font=('Arial', 24), borderwidth=1, justify='center')
                self.cells[i][j].grid(row=i, column=j)
                if self.grid[i][j] != 0:
                    self.cells[i][j].insert(0, self.grid[i][j])
                    self.cells[i][j].config(state='readonly')

        self.solve_button = tk.Button(master, text='Solve', command=self.solve)
        self.solve_button.grid(row=9, column=0, columnspan=3)
        
        self.restart_button = tk.Button(master, text='Restart', command=self.restart)
        self.restart_button.grid(row=9, column=3, columnspan=3)
        
        self.check_button = tk.Button(master, text='Check', command=self.check)
        self.check_button.grid(row=9, column=6, columnspan=3)

    def solve(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, self.solution[i][j])
                self.cells[i][j].config(state='readonly')

    def restart(self):
        new_grid = generate()
        self.grid = new_grid.copy()
        self.solution = [row[:] for row in new_grid]
        solve_sudoku(self.solution)  # Solve the new puzzle in the background
        for i in range(9):
            for j in range(9):
                self.cells[i][j].config(state='normal', bg="white")
                self.cells[i][j].delete(0, tk.END)
                if self.grid[i][j] != 0:
                    self.cells[i][j].insert(0, self.grid[i][j])
                    self.cells[i][j].config(state='readonly')


    def check(self):
        correct = True
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].get()
                if val.isdigit() and int(val) == self.solution[i][j]:
                    self.cells[i][j].config(bg="light green")
                elif val.isdigit() and int(val) != self.solution[i][j]:
                    self.cells[i][j].config(bg="red")
                    correct = False
                else:
                    self.cells[i][j].config(bg="white")
        if correct:
            print("All entries are correct!")
        else:
            print("There are errors in your entries.")

root = tk.Tk()
initial_grid = generate()
gui = SudokuGUI(root, initial_grid)
root.mainloop()
