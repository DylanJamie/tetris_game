## main.py
#

# main python file for tetris in pygame'

# Imports
import pygame
import pygame_menu
import sys
import random

# Set up the constraints
X = 400
Y = 400

# Load
TETRIS_BLUE = ( 26,  41, 107)
WHITE       = (200, 200, 200) 
DARK_GRAY   = ( 40,  40,  40)

# Set the difficulty
def set_difficulty(value, difficulty):
    pass

# Start the game
def start_game():
    pass

def draw_grid():
    block_size = 20
    for x in range(0, X, block_size):
        for y in range(0, Y, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((X, Y))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(TETRIS_BLUE)
    
    # Main while loop
    running = True
    while running == True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                
        # Make the menu for 
        # menu = pygame_menu.Menu("Tetris", 400, 300, theme=pygame_menu.themes.THEME_BLUE)
    
        # menu.add.text_input('Name :', default='Dylan Jamie')
        # menu.add.button('Play', start_game)
        # menu.add.button('Quit', pygame_menu.events.EXIT)
        
        # menu.mainloop(SCREEN)
            
        # Update the display
        pygame.display.update()
    
# End of main loop
#
if __name__=="__main__":
    main()
    
pygame.quit()
sys.exit()
# End of File

