import numpy as np
import pygame
import sys
import math


# colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7
player1_color = RED
player2_color = GREEN
screen_color = BLUE


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


def reverse_board(board):
    return np.flip(board, 0)

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, screen_color, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if reverse_board(board)[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif reverse_board(board)[r][c] == 1:
                pygame.draw.circle(screen, player1_color, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, player2_color, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


board = create_board()
game_over = False
turn = 0

pygame.init()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
RADIUS = SQUARESIZE // 2
myfont = pygame.font.SysFont('calibri', 75)

screen = pygame.display.set_mode((width, height))
draw_board(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, player1_color, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, player2_color, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # ask for player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, col, row, 1)

                    if winning_move(board, 1):
                        label = myfont.render('Player 1 Wins!!', 1, player1_color)
                        screen.blit(label, (60, 10))
                        game_over = True
                        continue

            # # ask for player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, col, row, 2)
            
                    if winning_move(board, 2):
                        label = myfont.render('Player 2 Wins!!', 1, player2_color)
                        screen.blit(label, (60, 10))
                        game_over = True
                        continue    

            
            
            draw_board(board)
            
            turn += 1
            turn = turn % 2

    if game_over:
        draw_board(board)
        pygame.time.wait(3000)
        