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

# List of all the colors
# LIST_COLOR = [utils.CYAN, utils.YELLOW, utils.PURPLE, utils.ORANGE, utils.BLUE, utils.LIME_GREEN, utils.RED]

# Continuous falling speed
# 500 ms, make the block drop
BLOCK_FALL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BLOCK_FALL_EVENT, 500)

# Make a new function to store a new block ath the top center
def spawn_new_block():
    # pick a random color for the block
    block_color = random.choice(utils.LIST_COLOR)
    return (utils.X // 2), 0, block_color

# Main Function
def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((utils.X, utils.Y))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Tetris")

    # Creating a 20x20 grid martix to store the landed blocks
    # Rows = 400 // 20 = 20 | cols = 400 // 20 = 20
    grid_rows = utils.Y // utils.BLOCK_SIZE
    grid_cols = utils.X // utils.BLOCK_SIZE

    # Create an empty list for the grid rows
    grid = []

    # Loop for all the rows on the screen
    for row in range(grid_rows):
        new_row = []

        # fill this with empty columns
        for col in range(grid_cols):
            new_row.append(None)

        # add the completed row to our main grid
        grid.append(new_row)

    # this makes every block spawn in the center 0
    # the spawn new block funct returns a tuple of coords
    x_pos, y_pos, current_color = spawn_new_block()
        
    # Main while loop
    running = True
    while running == True:
        # wipe the screen to prevent block trail
        SCREEN.fill(utils.TETRIS_BLUE)

        # Draw Grid
        utils.draw_grid(SCREEN)

        # Draw all the static blocks that have already been stacked
        for r in range(grid_rows):
            for c in range(grid_cols):
                if grid[r][c] is not None:
                    # render the locked block using the color stored in the grid
                    locked_rect = pygame.Rect(c * utils.BLOCK_SIZE, r * utils.BLOCK_SIZE, utils.BLOCK_SIZE, utils.BLOCK_SIZE)
                    pygame.draw.rect(SCREEN, grid[r][c], locked_rect)

        # Handle the inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            # continuous falling event falling from timer    
            if event.type == BLOCK_FALL_EVENT:
                if y_pos < utils.Y - utils.BLOCK_SIZE:
                    next_y = y_pos + MOVE_RATE
                    grid_x = x_pos // utils.BLOCK_SIZE
                    next_grid_y = next_y // utils.BLOCK_SIZE

                    # Check if hitting the floor or the blocks already placed
                    if next_y >= utils.Y or (next_grid_y < grid_rows and grid[next_grid_y][grid_x] is not None):
                        # Lock current block into thr grid matrix
                        current_grid_y = y_pos // utils.BLOCK_SIZE
                        grid[current_grid_y][grid_x] = current_color

                        # Spawn a brnd new block at the top
                        x_pos, y_pos, current_color = spawn_new_block()
                    else:
                        y_pos = next_y
                        
            # Snap to the bottom when hitting the bottom floor
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    # Find what the lowest avalible point to drop to is
                    grid_x = x_pos // utils.BLOCK_SIZE
                    target_row = y_pos // utils.BLOCK_SIZE

                    # Look down row by row intil wee hit the floor or filled cell in the matrix
                    while target_row + 1 < grid_rows and grid[target_row + 1][grid_x] is None:
                        target_row += 1

                    # Lock it into that target row
                    grid[target_row][grid_x] = current_color
                    # instantly spawn the next block
                    x_pos, y_pos, current_color = spawn_new_block()
                        
                # Move to the right
                if event.key == pygame.K_RIGHT:
                    next_x = x_pos + MOVE_RATE
                    grid_x = next_x // utils.BLOCK_SIZE
                    grid_y = y_pos  // utils.BLOCK_SIZE

                    # Only move to the right if it stays in bounds
                    if next_x < utils.X and grid[grid_y][grid_x] is None:
                        x_pos = next_x
                        
                # Move to the left                    
                if event.key == pygame.K_LEFT:
                    next_x = x_pos - MOVE_RATE
                    grid_x = next_x // utils.BLOCK_SIZE
                    grid_y = y_pos  // utils.BLOCK_SIZE

                    # Keep in bounds
                    if next_x >= 0 and grid[grid_y][grid_x] is None:
                        x_pos = next_x
                    
        # Define and draw active falling piece
        current_block = pygame.Rect(x_pos, y_pos, utils.BLOCK_SIZE, utils.BLOCK_SIZE)
        pygame.draw.rect(SCREEN, current_color, current_block)

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

