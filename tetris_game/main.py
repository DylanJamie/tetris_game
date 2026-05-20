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
curr_block_movement = 0
game_active = True
move_rate = 20

# Spawn Block
block_list = []
block_time = 10000 # 10 sec
block_spawn = pygame.USEREVENT
pygame.time.set_timer(block_spawn, block_time)
block_shape = [] # eventually we will put all the shapes here

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

    # block prop
    x_pos = utils.X // 2 - 10
    y_pos = 100
    
    # Main while loop
    running = True
    while running == True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == block_spawn:
                y_pos += move_rate
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_pos = 0
                if event.key == pygame.K_RIGHT:
                    x_pos += move_rate
                if event.key == pygame.K_LEFT:
                    x_pos -= move_rate
                    
        # Current dropping block
        current_block = pygame.Rect(x_pos, y_pos, 20, 20)

        # Draw the actual block using an adjusted rect obj
        current_block = pygame.draw.rect(SCREEN, utils.LIME_GREEN, current_block)

        # Update the display
        pygame.display.update()
        
# End of main loop
#
if __name__=="__main__":
    main()
    
pygame.quit()
sys.exit()
# End of File

