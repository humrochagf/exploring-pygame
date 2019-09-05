import time

import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

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

    # moves the square at the velocity defined
    position_x += velocity_x * dt

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [position_x, 230, 20, 20])

    pygame.display.flip()
