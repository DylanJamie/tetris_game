## main.py
#

# main python file for tetris in pygame'

# Imports
import pygame
import pygame_menu
import sys
import random
import src.utils as utils

# Set the difficulty
def set_difficulty(value, difficulty):
    pass

# Grid for the game
def draw_grid():
    block_size = 20
    for x in range(0, utils.X, block_size):
        for y in range(0, utils.Y, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(SCREEN, utils.WHITE, rect, 1)

# Main Function
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((utils.X, utils.Y))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(utils.TETRIS_BLUE)
    
    # Main while loop
    running = True
    while running == True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
        
        # Current dropping block
        # pygame.rect(SCREEN, utils.LIME_GREEN, (20, 20, 20, 20))
            
        # Update the display
        pygame.display.update()
    
# End of main loop
#
if __name__=="__main__":
    main()
    
pygame.quit()
sys.exit()
# End of File

