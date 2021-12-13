# nlaobappha CSC 120 0002
# file name: board.py

# 3*3 Tic-Tac-Toe game
def start():
    print("The game will start with Player X and alternate turns with Player O.")
    # Create a new 3*3 board
    board = [["-" for _ in range(3)] for _ in range(3)]
    # Starts with Player X
    is_x = True
    game_over = False
    # Use while loop to keep playing until there is a winner
    while not game_over:
        print_board(board)
        try:
            square = convert_square(check_square())
            place_mark(square, is_x, board)
        except ValueError:
            print("Sorry, please select a square from 1-9 and make sure it is empty.")
            continue
        game_over = is_win(board) or is_draw(board)
        is_x = not is_x


# Function to print board
def print_board(board):
    print("Printing board...")
    for row in board:
        print(row)
    print("Board printed.")


# --------------------------------------------------------------------------------------------------------
# Functionality for stage 2:
# Players 1 and 2 can take alternate turns while placing a mark on the board.
# Players 1 and 2 are able to place a mark on the board from Stage 1.
# Players should not be able to place a mark at an invalid location on the board.
# Players should not be able to place a mark at a location which is not empty.
# --------------------------------------------------------------------------------------------------------
# Convert the square number 1–9 from the user to row and column
def convert_square(square):
    square -= 1
    return square // 3, square % 3


def check_square():
    square = int(input("Please pick a square: "))
    if not 1 <= square <= 9:
        raise ValueError
    return square


# Use i & j as row and column
def place_mark(square, is_x, board):
    i, j = square
    if board[i][j] == "-":
        board[i][j] = "X" if is_x else "O"
    else:
        raise ValueError


# --------------------------------------------------------------------------------------------------------
# Functionality for stage 3:
# Add the logic for player winning, losing or a draw.
# --------------------------------------------------------------------------------------------------------
# Function to check for a win
def is_win(board):
    winner = None
    for i in range(3):
        # check for win horizontally
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            winner = board[i][0]
            break
        # check for win vertically
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            winner = board[0][i]
            break
    # check for win diagonally
    if board[1][1] != "-":
        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            winner = board[1][1]
    if winner is not None:
        print_board(board)
        print(f"{winner} is the winner! Thanks for playing.")
        return True
    return False


# Function to check for a draw
def is_draw(board):
    for row in board:
        for val in row:
            if val == "-":
                return False
    print_board(board)
    print("This game is a draw! Thanks for playing.")
    return True


# Let's Play!
start()
