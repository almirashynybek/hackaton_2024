import pygame
import screens
pygame.init()
            
# экран для текста с предысторией игры
def menu():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))

    background = pygame.transform.scale(pygame.image.load("images/texts/1.png"), (screen_w, screen_h))
    press_x, press_y = 0, 0

    button_OK = pygame.transform.scale(pygame.image.load("images/buttons/OK.png"), (180, 70))
    button_OK_rect = button_OK.get_rect()
    button_OK_rect.topleft = (screen_w - 250, screen_h - 150) 
    button_click = pygame.mixer.Sound('sounds/button.mp3')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                press_x, press_y = event.pos
        screen.blit(background, (0, 0))
        screen.blit(button_OK, button_OK_rect)

        if button_OK_rect.collidepoint(press_x, press_y):
            button_click.play()
            screens.map()

        pygame.display.flip()
