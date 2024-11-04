def is_safe(board, row, col):
    # Check if no queens threaten the current cell in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * n  # Initialize an empty chessboard
    solutions = []
    backtrack(0)
    return solutions

def print_solution(board):
    for row in board:
        line = ['.'] * len(board)
        line[row] = 'Q'
        print(' '.join(line))
    print()

def main():
    try:
        n = int(input("Enter the number of queens (e.g., 4): "))
        if n < 4:
            print("The number of queens must be at least 4.")
            return
        solutions = solve_n_queens(n)
        if solutions:
            print(f"Found {len(solutions)} solution(s) for {n}-queens problem:")
            for i, solution in enumerate(solutions):
                print(f"Solution {i + 1}:")
                print_solution(solution)
        else:
            print(f"No solution found for {n}-queens problem.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


'''
1.Check Safety: For each queen, check if placing it on a specific row and column is safe:
    Make sure no other queens are in the same column.
    Check the diagonals to ensure no queens are positioned there, as they would attack each other.
2.Solve with Backtracking:
    Start with an empty chessboard.
    Try to place a queen in each row, one by one:
        For each row, attempt to place the queen in each column.
        If it’s safe, place the queen and move to the next row.
        If placing the queen leads to a solution, save it.
        If not, remove the queen and try the next column (backtracking).
        Repeat this process until you find all possible solutions.
3.Display Solutions:
    For each solution, print the board, showing queens as "Q" and empty spots as ".".
4.Run the Program:
    Ask the user for the number of queens.
    If the input is valid and greater than 3, run the backtracking solution.
    Print each solution or notify if none are found.
'''
