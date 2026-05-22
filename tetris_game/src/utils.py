# utils.py
#

# we will keep all our utility variables and functions within this file

# imports
import pygame
import sys

# Set up the constraints
X = 200
Y = 400
BLOCK_SIZE = 20

# Load Game Colors RGB
TETRIS_BLUE = ( 26,  41, 107)
WHITE       = (200, 200, 200) 
DARK_GRAY   = ( 40,  40,  40)

# Grid color
GRID_COLOR  = ( 38,  56, 138)

# Colors for blocks
CYAN        = (  0, 255, 255)
YELLOW      = (255, 255,   0)
PURPLE      = (128,   0, 128)
ORANGE      = (255, 165,   0)
BLUE        = (  0,   0, 255)
LIME_GREEN  = ( 50, 205,  50)
RED         = (255,   0,   0)
PINK        = (255, 192, 203)

# Dictioary of shapes
SHAPE = {
    'O': [(0,0), (0,1), (1,0), (1,1)],
    'I': [(0,0), (0,1), (0,2), (0,3)],
    'S': [(0,1), (1,1), (1,0), (2,0)],
    'Z': [(0,0), (1,0), (1,1), (2,1)],
    'L': [(0,0), (0,1), (0,2), (1,2)],
    'J': [(1,0), (1,1), (1,2), (0,2)],
    'T': [(0,0), (1,0), (2,0), (1,1)]
}

# Dictionary of shapes to offical Tetris colors
SHAPE_COLOR = {
    'O': YELLOW,
    'I': CYAN,
    'S': RED,
    'Z': LIME_GREEN,
    'L': ORANGE,
    'J': PINK,
    'T': PURPLE
}

## Functions ##

# Grid for the game
def draw_grid(screen):
    for x in range(0, X, BLOCK_SIZE):
        for y in range(0, Y, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)
