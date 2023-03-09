import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Solver")

        self.puzzle = []
        self.entries = []
        self.solved = False  # track whether the puzzle has been solved
        self.moves = []  # track the user's moves for undo functionality

        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(master, width=2, font=('Arial', 16))
                entry.grid(row=i, column=j)
                row.append(entry)
            self.puzzle.append([0] * 9)
            self.entries.append(row)

        solve_button = tk.Button(master, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=4)

        clear_button = tk.Button(master, text="Clear", command=self.clear)
        clear_button.grid(row=9, column=5)

        undo_button = tk.Button(master, text="Undo", command=self.undo)
        undo_button.grid(row=9, column=3)

    def clear(self):
        # Clear all the entries
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)

    def undo(self):
        if self.moves:
            row, col, value = self.moves.pop()
            entry = self.entries[row][col]
            entry.delete(0, tk.END)
            if value != 0:
                entry.insert(0, str(value))
            self.puzzle[row][col] = value

    def get_puzzle(self):
        # Get the Sudoku puzzle from the entries
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit():
                    if int(value) < 1 or int(value) > 9:  # Check if value is between 1 and 9
                        tk.messagebox.showerror("Error", "Values must be between 1 and 9.")
                        return None
                    row.append(int(value))
                elif value == "":  # Handle empty entries
                    row.append(0)
                else:  # Handle non-digit characters
                    tk.messagebox.showerror("Error", "Entries must be digits between 1 and 9.")
                    return None
            puzzle.append(row)
        self.moves = []
        self.puzzle = []
        return puzzle


    def print_puzzle(self, puzzle):
        # Print the Sudoku puzzle to the entries
        for i in range(9):
            for j in range(9):
                value = puzzle[i][j]
                if value == 0:
                    self.entries[i][j].delete(0, tk.END)
                else:
                    self.entries[i][j].delete(0, tk.END)  # Delete original value first
                    self.entries[i][j].insert(0, str(value))

    def is_valid(self, puzzle, row, col, value):
        # Check if the value is already used in the same row
        if value in puzzle[row]:
            return False

        # Check if the value is already used in the same column
        for i in range(9):
            if puzzle[i][col] == value:
                return False

        # Check if the value is already used in the same 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row+3):
            for j in range(box_col, box_col+3):
                if puzzle[i][j] == value:
                    return False

        # If the value is not already used in the same row, column, or box, it is valid
        return True

    def solve_puzzle(self, puzzle):
        # Solve the Sudoku puzzle using the backtracking algorithm
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for k in range(1, 10):
                        if self.is_valid(puzzle, i, j, k):
                            puzzle[i][j] = k
                            if self.solve_puzzle(puzzle):
                                return True
                            else:
                                puzzle[i][j] = 0
                    return False
        return True

    def solve(self):
        # Get the Sudoku puzzle and solve it
        if not self.solved:  # check if puzzle has already been solved
            puzzle = self.get_puzzle()
            if puzzle is not None:  # Check if there were any errors in the puzzle input
                if self.solve_puzzle(puzzle):
                    self.print_puzzle(puzzle)
                    self.solved = True  # set solved to True if puzzle is solved
                else:
                    tk.messagebox.showerror("Error", "The puzzle is unsolvable.")
        else:
            self.solved = False  # reset solved to False if puzzle has already been solved

root = tk.Tk()
app = SudokuSolver(root)
root.mainloop()
