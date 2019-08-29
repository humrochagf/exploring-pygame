import pygame

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Game Loop')

# the ball variables
position_x = 300
position_y = 200
velocity_x = 1
velocity_y = 1

# starting the game loop
while True:
    # INPUT PROCESSING

    # catch the events
    event = pygame.event.poll()
    # if the QUIT event is caught (when you click on the x to close the window)
    if event.type == pygame.QUIT:
        # end the loop and finish the program
        break

    # GAME UPDATE

    # change the ball position
    position_x += velocity_x
    position_y += velocity_y

    # change the x direction at the corners
    if position_x > 600:
        velocity_x = -1
    elif position_x < 0:
        velocity_x = 1

    # change the y direction at the corners
    if position_y > 440:
        velocity_y = -1
    elif position_y < 0:
        velocity_y = 1

    # DRAWING

    # fill the background with black
    screen.fill(BLACK)

    # draw the ball
    pygame.draw.ellipse(screen, RED, [position_x, position_y, 40, 40])

    # update the screen
    pygame.display.flip()
