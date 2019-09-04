import pygame

BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('FPS')

position_x = 0
# since pygame clock returns its value
# in milliseconds, we divide the velocity
# by 1000 to keep the 100 pixel per seconds
velocity_x = 0.1

# create pygame clock
clock = pygame.time.Clock()

while True:
    # call the clock tick for 30 fps
    # and store the delta time
    dt = clock.tick(30)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    position_x += velocity_x * dt

    screen.fill(BLACK)

    pygame.draw.ellipse(screen, RED, [position_x, 300, 40, 40])

    pygame.display.flip()
