import pygame
#import almaty
import aktobe
import pavlodar
pygame.init()

# экран для описания мини-игры в Алмате
def almaty_menu():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))
    background = pygame.transform.scale(pygame.image.load("images/texts/3.png"), (screen_w, screen_h))

    button_start = pygame.transform.scale(pygame.image.load("images/buttons/start.png"), (180, 70))
    button_start_rect = button_start.get_rect()
    button_start_rect.topleft = (screen_w - 250, screen_h - 150) 
    button_click = pygame.mixer.Sound('sounds/button.mp3')

    press_x, press_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                press_x, press_y = event.pos
        screen.blit(background, (0, 0))
        screen.blit(button_start, button_start_rect)
        ''''
        # при нажатии кнопки "START" начинается игра
        if button_start_rect.collidepoint(press_x, press_y):
            button_click.play()
            almaty.almaty()
        '''

        pygame.display.flip()


# меню для описания игры в Актобе
def aktobe_menu():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))

    background = pygame.transform.scale(pygame.image.load("images/texts/2.png"), (screen_w, screen_h))

    button_start = pygame.transform.scale(pygame.image.load("images/buttons/OK.png"), (180, 70))
    button_start_rect = button_start.get_rect()
    button_start_rect.topleft = (screen_w - 250, screen_h - 150) 
    button_click = pygame.mixer.Sound('sounds/button.mp3')

    press_x, press_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                press_x, press_y = event.pos
        screen.blit(background, (0, 0))
        screen.blit(button_start, button_start_rect)

        if button_start_rect.collidepoint(press_x, press_y):
           button_click.play()
           aktobe.aktobe()

        pygame.display.flip()

# меню для описания игры в Павлодаре
def pavlodar_menu():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))

    background = pygame.transform.scale(pygame.image.load("images/texts/4.png"), (screen_w, screen_h))

    press_x, press_y = 0, 0 

    button_start = pygame.transform.scale(pygame.image.load("images/buttons/OK.png"), (180, 70))
    button_start_rect = button_start.get_rect()
    button_start_rect.topleft = (screen_w - 250, screen_h - 150) 
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
        screen.blit(button_start, button_start_rect)

        if button_start_rect.collidepoint(press_x, press_y):
            button_click.play()
            pavlodar.pavlodar()

        pygame.display.flip()