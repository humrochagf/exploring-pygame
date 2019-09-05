import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Collision')

# create the ball Rect
ball = pygame.Rect(300, 220, 40, 40)

# create the pads Rect
left_pad = pygame.Rect(20, 200, 20, 80)
right_pad = pygame.Rect(600, 200, 20, 80)

pads = [left_pad, right_pad]

velocity_x = 0.1

clock = pygame.time.Clock()

while True:
    dt = clock.tick(30)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    # use the move function inplace
    ball.move_ip(velocity_x * dt, 0)

    # check for collision with the pads
    if ball.collidelist(pads) >= 0:
        velocity_x = -velocity_x

    screen.fill(BLACK)

    # draw using the rect
    pygame.draw.ellipse(screen, WHITE, ball)

    # draw the pads
    for pad in pads:
        pygame.draw.rect(screen, WHITE, pad)

    pygame.display.flip()
