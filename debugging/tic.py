def print_board(board):
    """
    Function Description:
    Prints the Tic Tac Toe board.

    Parameters:
    - board: The Tic Tac Toe board represented as a 2D list.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Function Description:
    Checks if there's a winner on the Tic Tac Toe board.

    Parameters:
    - board: The Tic Tac Toe board represented as a 2D list.

    Returns:
    True if there's a winner, False otherwise.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Function Description:
    Checks if the game is a draw (no winner and no empty cells left).

    Parameters:
    - board: The Tic Tac Toe board represented as a 2D list.

    Returns:
    True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Function Description:
    Implements the Tic Tac Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board) and not check_draw(board):
        print_board(board)
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input! Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter integers.")

    print_board(board)
    if check_winner(board):
        print(f"Player {player} wins!")
    else:
        print("It's a draw!")

tic_tac_toe()

