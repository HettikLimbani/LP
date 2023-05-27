
def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]  # Create an empty chessboard
    queens = []  # List to store the column position of queens

    def is_safe(row, col):
        # Check if placing a queen at the given position is safe
        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False
        # Check upper diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        # Check lower diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
        return True
    

    # The backtrack function is a recursive helper function that tries to place queens on the 
    # chessboard row by row, starting from the given row parameter. If row is equal to n, it
    # means all queens have been placed successfully, so it calls the print_solution function
    # to print the board configuration and returns True to indicate a solution was found

    '''Inside the backtrack function, it iterates over each column in the current row and checks if it's safe to place a queen at that position. If it is safe, it marks that position as occupied (1) on the board, adds the column index to the queens list, and recursively calls backtrack with the next row.

If the recursive call to backtrack returns True, it means a solution was found, so it immediately returns True to propagate the success upward through the recursive calls.

If the current configuration doesn't lead to a solution, it backtracks by marking the current position as empty (0) on the board, removing the last column index from the queens list, and continues with the next column.

If all columns have been tried in the current row and none led to a solution, it returns False to backtrack further.

The print_solution function prints the board configuration. It iterates over each cell in the board and checks if the corresponding column index is present in the queens list. If it is, it prints "Q" to represent a queen; otherwise, it prints "." to represent an empty cell.

Finally, the code prompts the user to enter the number of queens (n), and it calls the solve_n_queens function with the user-provided value to solve the N-Queens problem'''
    def backtrack(row):
        if row == n:
            # All queens have been placed, print the solution
            print_solution()
            return True
        for col in range(n):
            if is_safe(row, col):
                # Place a queen at the current position
                board[row][col] = 1
                queens.append(col)

                # Recursively backtrack to place the remaining queens
                if backtrack(row + 1):
                    return True

                # If the current configuration doesn't lead to a solution, backtrack
                board[row][col] = 0
                queens.pop()

        return False

    def print_solution():
        # Print the board configuration
        for row in range(n):
            for col in range(n):
                if queens[row] == col:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

    # Start with the first row (row index 0)
    backtrack(0)

# Prompt the user to enter the number of queens
n = int(input("Enter the number of queens: "))
solve_n_queens(n)