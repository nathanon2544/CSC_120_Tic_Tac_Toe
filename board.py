# Create a new 3*3 board 

board = [["-" for _ in range(3)] for _ in range(3)]

def print_board_list(board):
    print("Printing board")
    [print(row) for row in board]
    print("Board printed")

def print_board_for(board):
    for row in board:
        print(row)

print_board_list(board)
