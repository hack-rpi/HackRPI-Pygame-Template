# https://www.pygame.org/docs/
import pygame

# Initialize the pygame library
pygame.init()

SCREEN_DIMENSIONS = (750, 750)

# Creating the base pygame screen
screen = pygame.display.set_mode(SCREEN_DIMENSIONS)

# Creating the clock used to frame rate management
clock = pygame.time.Clock()

logo = pygame.image.load('logo.png')

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fills the screen in (r, g, b) format
    screen.fill((255, 0, 0))

    # Displays the HackRPI logo in (x, y) format
    screen.blit(logo, (60, 60))

    # Updates the screen
    pygame.display.flip()

    clock.tick(60)
