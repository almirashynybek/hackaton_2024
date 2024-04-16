import pygame
pygame.init()

screen = pygame.display.set_mode((640, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()