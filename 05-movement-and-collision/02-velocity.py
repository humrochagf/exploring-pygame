import time

import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Velocity')

position_x = 0
# 100 pixels per second
velocity_x = 100

# capture the initial time
ti = time.time()

while True:
    # gets the time for
    # this cycle
    tf = time.time()
    # calculate the delta
    dt = (tf - ti)
    # sets final time as the initial time
    ti = tf

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    # moves the ball at the velocity defined
    position_x += velocity_x * dt

    screen.fill(BLACK)

    pygame.draw.ellipse(screen, WHITE, [position_x, 300, 40, 40])

    pygame.display.flip()
