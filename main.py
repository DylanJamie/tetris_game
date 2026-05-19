## main.py
#

# main python file for tetris in pygame'

# Imports
import pygame
import sys
import random

# Set up the constraints
pygame.init()
X = 1400
Y = 700
screen = pygame.display.set_mode((X, Y))

# Load
LIGHT_BLUE = (173, 216, 230)
DARK_GRAY  = (40,   40,  40)

# Main while loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    # Fill the screen with Light blue
    screen.fill(LIGHT_BLUE)

    # Update the display
    pygame.display.flip()
    
    # Logic for Dropping the blocks

# End of main loop
#
pygame.quit()
sys.exit()
# End of File

