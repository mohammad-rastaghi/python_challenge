import numpy as np


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, col, row, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    # check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    # heck for the positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # check for the negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True


def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # ask for player 1 input
    if turn == 0:
        col = int(input('\nPlayer 1 make your selection (0 - 6): '))
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, col, row, 1)

            if winning_move(board, 1):
                print('Player 1 Wins!!! Congrate...')
                game_over = True
                continue

    # ask for player 2 input
    else:
        col = int(input('\nPlayer 2 make your selection (0 - 6): '))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, col, row, 2)
    
            if winning_move(board, 2):
                print('Player 2 Wins!!! Congrate...')
                game_over = True
                continue    


    print_board(board)
    
    turn += 1
    turn = turn % 2
