import pygame

BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Simple Movement')

position_x = 0

while True:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    # moves the ball one pixel per cicle
    position_x += 1

    screen.fill(BLACK)

    # draws the ball with the incremented position
    pygame.draw.ellipse(screen, RED, [position_x, 300, 40, 40])

    pygame.display.flip()
