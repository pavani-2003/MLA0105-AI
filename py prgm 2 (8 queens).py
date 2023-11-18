def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col == n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, n):
                return True

            board[i][col] = 0  # Backtrack if placing a queen in this position doesn't lead to a solution

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist.")
        return None

    return board

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

if __name__ == "__main__":
    n = 8  # You can change this to solve for different board sizes
    solution = solve_n_queens(n)

    if solution:
        print(f"Solution for {n}-Queens problem:")
        print_solution(solution)
