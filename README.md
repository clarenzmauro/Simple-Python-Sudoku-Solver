# Simple-Python-Sudoku-Solver
What is this nonsense?

This is a Python program that solves a given Sudoku puzzle using the backtracking algorithm.
The program prompts the user to enter the Sudoku puzzle one row at a time, with empty cells represented by 0 or a dot (.). 
The puzzle is then printed to the console, and the program attempts to solve it using the solve_puzzle() function.
The is_valid() function checks if a given value can be placed in a specific cell of the puzzle, according to the rules of Sudoku. 
If the value is already present in the same row, column, or 3x3 box, it is not valid.
The solve_puzzle() function uses a recursive backtracking algorithm to try different values for each empty cell until a solution is found. 
If a value is found to be invalid, the algorithm backtracks to the previous cell and tries a different value until a solution is found.
Finally, the program prints the solved puzzle to the console, or prints a message indicating that the puzzle is unsolvable.

-sirclar
