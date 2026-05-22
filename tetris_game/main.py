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

# Make a new function to store a new block ath the top center
def spawn_new_block():
    # pick a random color for the block
    shape_type = random.choice(list(utils.SHAPE.keys()))
    shape_layout = utils.SHAPE[shape_type]
    shape_color = utils.SHAPE_COLOR[shape_type]
    
    # We spawn the pivot point at the top center
    return (utils.GRID_WIDTH // 2), 0, shape_layout, shape_color

# this function checks to see if the blocks can
def is_valid_position(pivot_x, pivot_y, shape_layout, grid):
    for row_off, col_off in shape_layout:
        # Calculate where the specific block wants to be
        block_x = pivot_x + (col_off * utils.BLOCK_SIZE)
        block_y = pivot_y + (row_off * utils.BLOCK_SIZE)

        # Check the screen boudries
        if block_x < 0 or block_x >= utils.GRID_WIDTH or block_y >= utils.Y:
            return False

        # Check grid matrix collision (only if it is within the grid height)
        if block_y >= 0:
            grid_x = block_x // utils.BLOCK_SIZE
            grid_y = block_y // utils.BLOCK_SIZE
            if grid[grid_y][grid_x] is not None:
                return False
    return True

# Check if the line is fully filled
def check_clear_lines(grid, grid_cols):
    lines_cleared = 0

    # Iterate bakcwards from the bottom row (19) to top (0)
    for r in range(len(grid) - 1, -1, -1):
        # If there are no None Values in this row it is full
        if None not in grid[r]:
            # remove the row
            del grid[r]
            # insert a brand new empty row at the very top
            grid.insert(0, [None] * grid_cols)
            lines_cleared += 1

    # Tetris scoring system
    score_table = {
        1: 100,
        2: 300,
        3: 500,
        4: 800
    }
    return score_table.get(lines_cleared, 0)

# Main Function
def main():
    pygame.init()

    # Add some music
    pygame.mixer.init()

    # Load the audio
    pygame.mixer.music.load("./assets/Tetris_main_theme.mp3")

    # Play the track on loop
    pygame.mixer.music.play(-1)

    # Lower the volume
    pygame.mixer.music.set_volume(0.3)
    
    pygame.time.set_timer(BLOCK_FALL_EVENT, 500)
    SCREEN = pygame.display.set_mode((utils.X, utils.Y))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Tetris")

    # intialize the score font
    pygame.font.init()

    # use font from flappy bird
    score_font = pygame.font.SysFont('./assets/ARCADECLASSIC.TTF', 24)

    # Load the score and highschore
    score = 0
    high_score = 0
    
    # Creating a 20x20 grid martix to store the landed blocks
    # Rows = 400 // 20 = 20 | cols = 400 // 20 = 20
    grid_rows = utils.Y // utils.BLOCK_SIZE
    grid_cols = utils.GRID_WIDTH // utils.BLOCK_SIZE

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
    x_pos, y_pos, current_shape, current_color = spawn_new_block()

    # Check if the new block clips existing blocks
    if not is_valid_position(x_pos, y_pos, current_shape, grid):
        print("Game_Over!")
        running = False
        
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
                # Test if moving down by MOVE_RATE is safe
                if is_valid_position(x_pos, y_pos + MOVE_RATE, current_shape, grid):
                    y_pos += MOVE_RATE
                else:
                    # It cant move down down so lock all 4 blocks into the grid matrix
                    for row_off, col_off in current_shape:
                        block_x = x_pos + (col_off * utils.BLOCK_SIZE)
                        block_y = y_pos + (row_off * utils.BLOCK_SIZE)
                        if block_y >= 0:
                            grid[block_y // utils.BLOCK_SIZE][block_x // utils.BLOCK_SIZE] = current_color

                    # Spawn the next piece
                    x_pos, y_pos, current_shape, current_color = spawn_new_block()

                    # Check if the new block clips existing blocks
                    if not is_valid_position(x_pos, y_pos, current_shape, grid):
                        print("Game_Over!")
                        running = False
                    
            # Snap to the bottom when hitting the bottom floor
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    # Keep shifting the pivot down 1 block until it hits an invalid pos
                    while is_valid_position(x_pos, y_pos + utils.BLOCK_SIZE, current_shape, grid):
                        y_pos += utils.BLOCK_SIZE

                    # Lock all 4 blocks into their final destination
                    for row_off, col_off in current_shape:
                        block_x = x_pos + (col_off * utils.BLOCK_SIZE)
                        block_y = y_pos + (row_off * utils.BLOCK_SIZE)
                        if block_y >= 0:
                            grid[block_y // utils.BLOCK_SIZE][block_x // utils.BLOCK_SIZE] = current_color

                    # Add points up
                    points_earned = check_clear_lines(grid, grid_cols)
                    score += points_earned
                            
                    # Spawn next
                    x_pos, y_pos, current_shape, current_color = spawn_new_block() 

                    # Check if the new block clips existing blocks
                    if not is_valid_position(x_pos, y_pos, current_shape, grid):
                        print("Game_Over!")
                        running = False
        
                # Move to the right
                if event.key == pygame.K_RIGHT:
                    if is_valid_position(x_pos + MOVE_RATE, y_pos, current_shape, grid):
                        x_pos += MOVE_RATE
                    
                # Move to the left                    
                if event.key == pygame.K_LEFT:
                    if is_valid_position(x_pos - MOVE_RATE, y_pos, current_shape, grid):
                        x_pos -= MOVE_RATE

                # Rotate the piece
                if event.key == pygame.K_UP:
                    # Calculate the rotated shape coordinates
                    rotated_shape = []
                    
                    # Loop through the blocks in postion in current shape matrix
                    for row, col in current_shape:
                        # Apply the 90 degree turn
                        new_block = (col, -row)
                        rotated_shape.append(new_block)

                    # Check if the rotated version is safe to use
                    if is_valid_position(x_pos, y_pos, rotated_shape, grid):
                        current_shape = rotated_shape
                        
        # Make it so it is not just a single block
        for row_off, col_off in current_shape:
            block_x = x_pos + (col_off * utils.BLOCK_SIZE)
            block_y = y_pos + (row_off * utils.BLOCK_SIZE)

            # Only draw if it is visible on board
            if block_y >= 0:
                # Define and draw active falling piece
                current_block = pygame.Rect(block_x, block_y, utils.BLOCK_SIZE, utils.BLOCK_SIZE)
                pygame.draw.rect(SCREEN, current_color, current_block)

        # Draw Vertical line
        pygame.draw.line(SCREEN, utils.WHITE, (utils.GRID_WIDTH, 0), (utils.GRID_WIDTH, utils.Y), 2)

        # Render the text surfaces
        score_label = score_font.render("SCORE", True, utils.WHITE)
        score_number = score_font.render(str(score), True, utils.CYAN)

        high_score_label = score_font.render("HIGH SCORE", True, utils.WHITE)
        high_score_number = score_font.render(str(high_score), True, utils.YELLOW)

        # BLit is draw the text surfaces with a specific offset
        SCREEN.blit(score_label, (utils.GRID_WIDTH + 20, 30))
        SCREEN.blit(score_number, (utils.GRID_WIDTH + 20, 60))

        SCREEN.blit(high_score_label, (utils.GRID_WIDTH + 20, 130))
        SCREEN.blit(high_score_number, (utils.GRID_WIDTH + 20, 160))
                
        # Update The display
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

