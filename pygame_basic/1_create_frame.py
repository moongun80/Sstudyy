import pygame

pygame.init() # initial

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# game title
pygame.display.set_caption("bubble pang Game")

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame end
pygame.quit()
