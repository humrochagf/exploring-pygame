import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Collision')

# create the square Rect
square = pygame.Rect(300, 230, 20, 20)

# create the pads Rect
left_pad = pygame.Rect(20, 210, 20, 60)
right_pad = pygame.Rect(600, 210, 20, 60)

pads = [left_pad, right_pad]

velocity_x = 0.1

clock = pygame.time.Clock()

while True:
    dt = clock.tick(30)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    # use the move function inplace
    square.move_ip(velocity_x * dt, 0)

    # check for collision with the pads
    if square.collidelist(pads) >= 0:
        velocity_x = -velocity_x

    screen.fill(BLACK)

    # draw using the rect
    pygame.draw.rect(screen, WHITE, square)

    # draw the pads
    for pad in pads:
        pygame.draw.rect(screen, WHITE, pad)

    pygame.display.flip()
