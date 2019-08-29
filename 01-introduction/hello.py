import time

import pygame

# initializes pygame variables
pygame.init()

# define the screen size to 640x480
screen = pygame.display.set_mode([640, 480])

# writes the Hello World at the screen title
pygame.display.set_caption('Hello World')

# fills the screen with black color
screen.fill([0, 0, 0])

# updates the screen
pygame.display.flip()

# waits 5 seconds to close the program
time.sleep(5)
