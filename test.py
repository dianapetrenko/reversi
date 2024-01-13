import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
PAD = 1

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

# 1 = black
player = 1

# Initialize the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reversi test")

board = []
def init_board():
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(0)
        board.append(row)

    SCREEN.fill(BLACK)
    x1, y1 = 0, 0
    dx, dy = SQUARE_SIZE, SQUARE_SIZE
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(SCREEN, GREEN, (x1, y1, dx - PAD, dy - PAD))
            x1 += SQUARE_SIZE
        y1 += SQUARE_SIZE
        x1 = 0

def draw_pieces():
    x, y = SQUARE_SIZE // 2, SQUARE_SIZE // 2
    radius = SQUARE_SIZE // 2 - PAD*2
    for i in range(ROWS):
        for j in range(COLS):
            p = board[i][j]
            if p != 0:
                color = BLACK if p == 1 else WHITE
                pygame.draw.circle(SCREEN, color, (x, y), radius)
            x += SQUARE_SIZE
        y += SQUARE_SIZE
        x = radius

def initial_placement():
    make_move(3, 3, -1)
    make_move(4, 4, -1)
    make_move(4, 3, 1)
    make_move(3, 4, 1)



def make_move(i, j, p):
    board[i][j] = p

def convert_xy_to_rowcol(x, y):
    print(f"x={x}, y={y}")
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def valid_move(row, col):
    # check if piece is already there
    if board[row][col] != 0:
        return False

    # check if neighboring pieces
    neighbor_count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            i_neighbor = row + i
            j_neighbor = col + j
            if i_neighbor < 0 or j_neighbor < 0 or i_neighbor >= ROWS or j_neighbor >= COLS:
                continue
            if board[i_neighbor][j_neighbor] != 0:
                neighbor_count += 1
    if neighbor_count == 0:
        return False

    # move is valid
    return True

def valid_row(x):
    return 0 <= x < ROWS

def valid_col(x):
    return 0 <= x < COLS

def flip_pieces(row, col, p):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            x = row + dx
            y = col + dy
            count = 0
            while valid_row(x) and valid_col(y) and board[x][y] == -p:
                x += dx
                y += dy
                count += 1
            if count > 0 and valid_row(x) and valid_col(y) and board[x][y] == p:
                x = row + dx
                y = col + dy
                while board[x][y] != p:
                    # make a flip
                    board[x][y] = p
                    x += dx
                    y += dy


# main
init_board()
initial_placement()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            row, col = convert_xy_to_rowcol(x, y)
            if valid_move(row, col):
                make_move(row, col, player)
                flip_pieces(row, col, player)
            player = -player

    # game code
    draw_pieces()
    pygame.display.flip()


