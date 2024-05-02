import pygame
import games
import city_menu
import time
import os
import flags

pygame.init()


# основной экран с картой Казахстана
def map():
    pygame.init()
    info = pygame.display.Info()
    screen_w = 1536
    screen_h = 864
    screen = pygame.display.set_mode((screen_w, screen_h))
    
    
    background = pygame.transform.scale(pygame.image.load("images/backgrounds/main_map.png"), screen.get_size())
    mouse_x, mouse_y = 0, 0
    press_x, press_y = 0, 0

    # инициализируем метки, по которым можно будет переходить на мини-игры
    pointer = pygame.transform.scale(pygame.image.load("images/cities/red.png"), (80, 90))
    ala_pointer, pvl_pointer, akx_pointer = pointer, pointer, pointer 
    ala_pointer_rect, pvl_pointer_rect, akx_pointer_rect = ala_pointer.get_rect(), pvl_pointer.get_rect(), akx_pointer.get_rect()
    ala_pointer_rect.topleft, pvl_pointer_rect.topleft, akx_pointer_rect.topleft = (1100, 600), (1080, 220), (425, 350)
   
    # при наведении мыши на метки появляется название города, инициализируем картинки с названиями
    almaty = pygame.transform.scale(pygame.image.load("images/cities/almaty.png"), (110, 25))
    aktobe = pygame.transform.scale(pygame.image.load("images/cities/aktobe.png"), (110, 25))
    pavlodar = pygame.transform.scale(pygame.image.load("images/cities/pavlodar.png"), (110, 25))
    almaty_rect, aktobe_rect, pavlodar_rect = almaty.get_rect(), aktobe.get_rect(), pavlodar.get_rect()
    almaty_rect.topleft = ala_pointer_rect.bottomright
    aktobe_rect.topleft = akx_pointer_rect.bottomright 
    pavlodar_rect.topleft = pvl_pointer_rect.bottomright


    close_button = pygame.transform.scale(pygame.image.load("images/buttons/close.png"), (180, 70))
    close_button_rect = close_button.get_rect()
    close_button_rect.topleft = (screen_w//2, screen_h - 150) 
    button_click = pygame.mixer.Sound('sounds/button.mp3')

    kbtu = pygame.image.load("images/KBTU/KBTU.png")
    kbtu_rect = kbtu.get_rect()
    kbtu_rect.center = screen.get_rect().center 

    button_click = pygame.mixer.Sound('sounds/button.mp3')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                press_x, press_y = event.pos
        screen.blit(background, (0,0))

        screen.blit(ala_pointer, ala_pointer_rect)
        screen.blit(pvl_pointer, pvl_pointer_rect)
        screen.blit(akx_pointer, akx_pointer_rect)

        # если курсор мыши наведен на метку, то показывается название города
        if ala_pointer_rect.collidepoint(mouse_x, mouse_y):
            screen.blit(almaty, almaty_rect)
        elif pvl_pointer_rect.collidepoint(mouse_x, mouse_y):
            screen.blit(pavlodar, pavlodar_rect)
        elif akx_pointer_rect.collidepoint(mouse_x, mouse_y):
            screen.blit(aktobe, aktobe_rect)

        # при нажатии на метку переходим на мини-игру
        if ala_pointer_rect.collidepoint(press_x, press_y):
            button_click.play()
            city_menu.almaty_menu()
        if pvl_pointer_rect.collidepoint(press_x, press_y):
            button_click.play()
            city_menu.pavlodar_menu()
        if akx_pointer_rect.collidepoint(press_x, press_y):
            button_click.play()
            city_menu.aktobe_menu()
        if flags.victory1 and flags.victory2 and flags.victory3:
            victory()
        
        pygame.display.flip()
    


def win1():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))

    background_button = pygame.transform.scale(pygame.image.load("images/backgrounds/background_buttons.jpg"), (screen_w, screen_h))
    part1 = pygame.image.load('images/KBTU/part1_done.png')
    part1_rect = part1.get_rect()
    part1_rect.center = screen.get_rect().center
    close_button = pygame.transform.scale(pygame.image.load("images/buttons/close.png"), (180, 70))
    close_button_rect = close_button.get_rect()
    close_button_rect.topleft = (screen_w - 250, screen_h - 150) 
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
            
        screen.blit(background_button, (0,0))
        screen.blit(part1, part1_rect)
        screen.blit(close_button, close_button_rect)
    
        if close_button_rect.collidepoint(press_x, press_y):
            button_click
            map()
        pygame.display.flip()

def win2():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))

    background_button = pygame.transform.scale(pygame.image.load("images/backgrounds/background_buttons.jpg"), (screen_w, screen_h))
    part1 = pygame.image.load('images/KBTU/part2_done.png')
    part1_rect = part1.get_rect()
    part1_rect.center = screen.get_rect().center
    close_button = pygame.transform.scale(pygame.image.load("images/buttons/close.png"), (180, 70))
    close_button_rect = close_button.get_rect()
    close_button_rect.topleft = (screen_w - 250, screen_h - 150) 
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
            
        screen.blit(background_button, (0,0))
        screen.blit(part1, part1_rect)
        screen.blit(close_button, close_button_rect)
    
        if close_button_rect.collidepoint(press_x, press_y):
            button_click
            map()
        pygame.display.flip()

def win3():
    info = pygame.display.Info()
    screen_w = 1536
    screen_h = 864
    screen = pygame.display.set_mode((screen_w, screen_h))

    background_button = pygame.transform.scale(pygame.image.load("images/backgrounds/background_buttons.jpg"), (screen_w, screen_h))
    part1 = pygame.image.load('images/KBTU/part3_done.png')
    part1_rect = part1.get_rect()
    part1_rect.center = screen.get_rect().center
    close_button = pygame.transform.scale(pygame.image.load("images/buttons/close.png"), (180, 70))
    close_button_rect = close_button.get_rect()
    close_button_rect.topleft = (screen_w - 250, screen_h - 150) 
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
            
        screen.blit(background_button, (0,0))
        screen.blit(part1, part1_rect)
        screen.blit(close_button, close_button_rect)
    
        if close_button_rect.collidepoint(press_x, press_y):
            button_click
            map()
        pygame.display.flip()


def victory():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))
    kbtu_image = pygame.transform.scale(pygame.image.load("images/KBTU/KBTU.png"), (700, 500))
    kbtu_image_rect = kbtu_image.get_rect()
    kbtu_image_rect.center = screen.get_rect().center
    close_button = pygame.transform.scale(pygame.image.load("images/buttons/close.png"), (180, 70))
    close_button_rect = close_button.get_rect()
    close_button_rect.topleft = (screen_w - 250, screen_h - 150) 
    button_click = pygame.mixer.Sound('sounds/button.mp3')
    mouse_x, mouse_y = 0, 0

    sound = pygame.mixer.Sound('sounds/victory_sound.mp3')
    sound.play()
    background_button = pygame.transform.scale(pygame.image.load("images/backgrounds/background_buttons.jpg"), (screen_w, screen_h))
    font = pygame.font.Font("fonts/Silkscreen.ttf", 60)
    text = font.render("CONGRATULATIONS!!!", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (kbtu_image_rect.centerx, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
        
        screen.blit(background_button, (0,0))
        screen.blit(kbtu_image, kbtu_image_rect)
        screen.blit(text, text_rect)
        screen.blit(close_button, close_button_rect)

        if close_button_rect.collidepoint(mouse_x, mouse_y):
            button_click.play()
            running = False
            pygame.quit()
        
        pygame.display.flip()
