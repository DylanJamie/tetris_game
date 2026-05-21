# utils.py
#

# we will keep all our utility variables and functions within this file

# imports
import pygame
import sys

# Set up the constraints
X = 400
Y = 400
BLOCK_SIZE = 20

# Define the screen
SCREEN = pygame.display.set_mode((X, Y))

# Load Game Colors RGB
TETRIS_BLUE = ( 26,  41, 107)
WHITE       = (200, 200, 200) 
DARK_GRAY   = ( 40,  40,  40)

# Grid color
GRID_COLOR  = ( 38,  56, 138)

# Colors for blocks
LIME_GREEN  = ( 50, 205,  50)

## Functions ##

# Grid for the game
def draw_grid(screen):
    for x in range(0, X, BLOCK_SIZE):
        for y in range(0, Y, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)
