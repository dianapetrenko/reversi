import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
PAD = 1

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reversi")

# Draw the board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, GREEN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE-PAD, SQUARE_SIZE-PAD))


def convert_xy_to_grid(x, y):
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col


def draw_piece(row, col, player):
    radius = int(0.9 * SQUARE_SIZE // 2)
    color = BLACK if player == 1 else WHITE
    x = SQUARE_SIZE * col + SQUARE_SIZE //2
    y = SQUARE_SIZE * row + SQUARE_SIZE //2
    pygame.draw.circle(screen, color, (x, y), radius)

def check_nearby_piece(row, col, color):
    nearby_positions = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1), (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    ]
    same_color_nearby = []

    for r, c in nearby_positions:
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == color:
            same_color_nearby.append((r, c))

    return same_color_nearby

# Main game loop
screen.fill(BLACK)
draw_board()

player = -1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            x, y = pygame.mouse.get_pos()
            print(f"Mouse clicked at ({x}, {y})")
            row, col = convert_xy_to_grid(x, y)
            draw_piece(row, col, player)
            player = -player

    pygame.display.flip()
