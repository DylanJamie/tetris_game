## main.py
#

# main python file for tetris in pygame'

# Imports
import pygame
import pygame_menu
import sys
import random
import src.utils as utils

# BLock movement
MOVE_RATE  = 20
BLOCK_SIZE = 20

# Continuous falling speed
# 500 ms, make the block drop
BLOCK_FALL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BLOCK_FALL_EVENT, 500)

# Grid for the game
def draw_grid(screen):
    for x in range(0, utils.X, BLOCK_SIZE):
        for y in range(0, utils.Y, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, utils.GRID_COLOR, rect, 1)

# Main Function
def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((utils.X, utils.Y))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Tetris")
    
    # block prop
    x_pos = utils.X // 2 - (BLOCK_SIZE // 2)
    y_pos = 0
    
    # Main while loop
    running = True
    while running == True:
        # wipe the screen to prevent block trail
        SCREEN.fill(utils.TETRIS_BLUE)

        # Draw Grid
        draw_grid(SCREEN)

        # Handle the inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            # continuous falling event falling from timer    
            if event.type == BLOCK_FALL_EVENT:
                if y_pos < utils.Y - BLOCK_SIZE:
                    y_pos += MOVE_RATE

            # Snap to the bottom when hitting the bottom floor
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_pos = utils.Y - BLOCK_SIZE

                # Make boundry checks so the blocks don't go off screen
                if event.key == pygame.K_RIGHT:
                    if x_pos < utils.X - BLOCK_SIZE:
                        x_pos += MOVE_RATE
                if event.key == pygame.K_LEFT:
                    if x_pos > 0:
                        x_pos -= MOVE_RATE
                    
        # Define and draw active falling piece
        current_block = pygame.Rect(x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, utils.LIME_GREEN, current_block)

        # Update the display
        pygame.display.update()
        CLOCK.tick(60)

    # Quit the game
    pygame.quit()
    sys.exit()
        
# End of main loop
#
if __name__=="__main__":
    main()
#
# End of File

