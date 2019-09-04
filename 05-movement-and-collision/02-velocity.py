import time

import pygame

BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Velocity')

position_x = 0
# 10 pyxels per second
velocity_x = 100

# capture the initial time
ti = time.time()

while True:
    # get how much time has passed
    # between the cycles
    tf = time.time()
    # calculate the delta
    dt = (tf - ti)
    # sets final time as the initial time
    ti = tf

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    # moves the ball one pixel per cycle
    position_x += velocity_x * dt

    screen.fill(BLACK)

    pygame.draw.ellipse(screen, RED, [position_x, 300, 40, 40])

    pygame.display.flip()
