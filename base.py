def get_puzzle():
    # Prompt the user for the Sudoku puzzle
    print("Enter the Sudoku puzzle, one row at a time. Use 0 or a dot (.) for empty cells.")
    puzzle = []
    for i in range(9):
        row_str = input(f"Row {i+1}: ")
        row = [int(c) if c.isdigit() else 0 for c in row_str]
        puzzle.append(row)
    return puzzle

def print_puzzle(puzzle):
    # Print the Sudoku puzzle
    print("Puzzle:")
    for row in puzzle:
        row_str = " ".join(str(c) if c != 0 else "." for c in row)
        print(row_str)

def is_valid(puzzle, row, col, value):
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

def solve_puzzle(puzzle):
    # Solve the Sudoku puzzle using the backtracking algorithm
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for k in range(1, 10):
                    if is_valid(puzzle, i, j, k):
                        puzzle[i][j] = k
                        if solve_puzzle(puzzle):
                            return True
                        else:
                            puzzle[i][j] = 0
                return False
    return True

# Main program
puzzle = get_puzzle()
print_puzzle(puzzle)
if solve_puzzle(puzzle):
    print("Solution:")
    for row in puzzle:
        row_str = " ".join(str(c) for c in row)
        print(row_str)
else:
    print("The puzzle is unsolvable.")
