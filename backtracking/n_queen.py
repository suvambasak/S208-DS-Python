def is_safe(board: list[list[int]], row: int, col: int, n: int):
    # Check if there is a queen in the same column up to the current row
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board: list[list[int]], row: int, n: int, solutions: list) -> None:
    if row == n:
        # If all queens are placed successfully, add the solution to the list
        solutions.append(["".join(map(str, row)) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen if it's safe
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens_util(board, row + 1, n, solutions)

            # Backtrack and remove the queen if no solution found
            board[row][col] = 0


def solve_n_queens(n: int) -> list[list[str]]:
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


# Example usage:
n = 4
solutions = solve_n_queens(n)
for idx, solution in enumerate(solutions, start=1):
    print(f"Solution {idx}:")
    for row in solution:
        print(" ".join(row))
    print()


# (base) suvam@KD-304G:/mnt/Storage/Repositories/S208-DS-Python$ /bin/python /mnt/Storage/Repositories/S208-DS-Python/backtracking/n_queen.py
# Solution 1:
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0

# Solution 2:
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0
