import pygame
import random


pygame.font.init()

# global Vars
screen_width = 800
screen_height = 700
play_width = 300
play_height = 600
row_length = 20
column_length = 10
block_size = 30

top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height


# shapes
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece(object):
    rows = row_length
    columns = column_length

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def create_grid(locked_positions = {}):
    grid = [[(0, 0, 0) for j in range(10)] for i in range(20)]

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (c, r) in locked_positions:
                color = locked_positions[(c, r)]
                grid[r][c] = color
    
    return grid


def convert_shape_format(object):
    positions = []
    format = object.shape[object.rotation % len(object.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((object.x + j, object.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0]-2, pos[1]-4)

    return positions


def valid_space(shape, grid):
    accepted_positions = []
    for r in range(20):
        for c in range(10):
            if grid[r][c] == (0, 0, 0):
                accepted_positions.append((c, r))
    
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    global shapes, shape_colors

    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold = True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2 - (label.get_height()/2)))


def draw_grid(surface, row, column):
    for i in range(row):
        pygame.draw.line(surface, (128, 128, 128), (top_left_x, top_left_y + i*block_size), (top_left_x + play_width, top_left_y + i*block_size)) 
        for j in range(column):
            pygame.draw.line(surface, (128, 128, 128), (top_left_x + j*block_size, top_left_y), (top_left_x + j*block_size, top_left_y + play_height))   


def clear_rows(grid, locked, score):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            score += 1
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    
    if inc > 0:
        for key in sorted(list(locked), key = lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                new_key = (x, y+inc)
                locked[new_key] = locked.pop(key)
    return score


def draw_next_shape(object, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape:', 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = object.shape[object.rotation % len(object.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, object.color, (sx + j*block_size, sy + i*block_size, 30, 30), 0)

    surface.blit(label, (sx + 10, sy - 40))


def draw_window(surface):
    # draw the game's name
    surface.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 20))

    # draw the grid blocks
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    # draw grid lines
    draw_grid(surface, row_length, column_length)

    # draw the game screen's border
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)


def draw_score(surface, score):
    sx = 80
    sy = top_left_y + play_height/2 - 40

    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score:', 1, (255, 255, 255))
    Score = font.render(str(score), 1, (255, 255, 255))

    surface.blit(label, (sx, sy))
    surface.blit(Score, (sx, sy + 30))
      
      
      
def main():
    global grid

    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    score = 0

    while run:
        fall_speed = 0.27

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
        
        # key pressing managing 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                       current_piece.x += 1 
                
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                
                elif event.key == pygame.K_UP:
                    current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)
        
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1


        shape_pos = convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # if piece hit ground
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            score = clear_rows(grid, locked_positions, score)
        
        draw_window(win)
        draw_next_shape(next_piece, win)
        draw_score(win, score)
        pygame.display.update()

        # check if user lost
        if check_lost(locked_positions):
            run = False


    draw_text_middle('YOU LOST!!', 40, (255, 255, 255), win)
    pygame.display.update()
    pygame.time.delay(2000)
    

def main_menu():
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle('Press any key to play...', 30, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main()
    
    pygame.quit()



win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

# start the game
main_menu()
