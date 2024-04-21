import pygame
import games
import city_menu

pygame.init()

# основной экран с картой Казахстана
def map():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
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
    almaty = pygame.transform.scale(pygame.image.load("images/cities/almaty.jpg"), (120, 30))
    aktobe = pygame.transform.scale(pygame.image.load("images/cities/aktobe.jpg"), (120, 30))
    pavlodar = pygame.transform.scale(pygame.image.load("images/cities/pavlodar.jpg"), (120, 30))
    almaty_rect, aktobe_rect, pavlodar_rect = almaty.get_rect(), aktobe.get_rect(), pavlodar.get_rect()
    almaty_rect.topleft = ala_pointer_rect.bottomright 
    aktobe_rect.topleft = akx_pointer_rect.bottomright 
    pavlodar_rect.topleft = pvl_pointer_rect.bottomright 

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
        
        pygame.display.flip()
    



# экран паузы, на экране три кнопки: retry(начать мини-игру заново), continue(продолжить мини-игру), menu(выйти в меню с картой)

def pause_aktobe():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))

    # приводим все кнопки до одинакого размера
    retry_image = pygame.transform.scale(pygame.image.load("images/buttons/retry.png"), (800, 200))
    continue_image = pygame.transform.scale(pygame.image.load("images/buttons/continue.png"), (800, 200))
    menu_image = pygame.transform.scale(pygame.image.load("images/buttons/menu.png"), (800, 200))

    retry_image_rect = retry_image.get_rect()
    continue_image_rect = continue_image.get_rect()
    menu_image_rect = menu_image.get_rect()

    continue_image_rect.topleft = (350, 100)
    retry_image_rect.topleft = (350, 350)
    menu_image_rect.topleft = (350, 600)

    mouse_x, mouse_y = 0, 0
    button_click = pygame.mixer.Sound('sounds/button.mp3')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
            
        screen.fill("black")

        # так же экспериментально подобрала местоположения кнопок...
        screen.blit(continue_image, continue_image_rect)
        screen.blit(retry_image, retry_image_rect)
        screen.blit(menu_image, menu_image_rect)
        
        if continue_image_rect.collidepoint(mouse_x, mouse_y):
            button_click.play()
        elif retry_image_rect.collidepoint(mouse_x, mouse_y):
            button_click.play()
            games.game_aktobe()
        elif menu_image_rect.collidepoint(mouse_x, mouse_y):
            button_click.play()
            map()

        pygame.display.flip()



def pause_pavlodar():
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))

    # приводим все кнопки до одинакого размера
    retry_image = pygame.transform.scale(pygame.image.load("images/buttons/retry.png"), (800, 200))
    continue_image = pygame.transform.scale(pygame.image.load("images/buttons/continue.png"), (800, 200))
    menu_image = pygame.transform.scale(pygame.image.load("images/buttons/menu.png"), (800, 200))

    retry_image_rect = retry_image.get_rect()
    continue_image_rect = continue_image.get_rect()
    menu_image_rect = menu_image.get_rect()

    continue_image_rect.topleft = (350, 100)
    retry_image_rect.topleft = (350, 350)
    menu_image_rect.topleft = (350, 600)

    mouse_x, mouse_y = 0, 0
    button_click = pygame.mixer.Sound('sounds/button.mp3')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
            
        screen.fill("black")

        # так же экспериментально подобрала местоположения кнопок...
        screen.blit(continue_image, continue_image_rect)
        screen.blit(retry_image, retry_image_rect)
        screen.blit(menu_image, menu_image_rect)
        
        if continue_image_rect.collidepoint(mouse_x, mouse_y):
            button_click.play()
        elif retry_image_rect.collidepoint(mouse_x, mouse_y):
            button_click.play()
            games.game_pavlodar()
        elif menu_image_rect.collidepoint(mouse_x, mouse_y):
            button_click.play()
            map()

        pygame.display.flip()




    


'''
def recieve(screen, kbtu_part, recieve_flag, map_flag, recive_sound, button_sound, continue_image, count):
    
    kbtu_part = pygame.transform.scale(kbtu_part, (600, 500))
    kbtu_part_rect = kbtu_part.get_rect()
    kbtu_part_rect.center = screen.get_rect().center
    color = (0, 0, 0)
    continue_image = pygame.transform.scale(continue_image, (500, 300))
    continue_image_rect = continue_image.get_rect()
    continue_image_rect.bottomright = (screen_width - 200, screen_height - 200)
    mouse_x, mouse_y = 0, 0
    screen_width, screen_height = screen.get_size()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

        screen.fill(color)
        screen.blit(kbtu_part, kbtu_part_rect)
        screen.blit(continue_image, continue_image_rect)

        # звук должен проиграться один раз при получении, дальше будет показываться только картинка получения
        if count == 0:
            recive_sound.play()
            count += 1

        if continue_image_rect.collidepoint(mouse_x, mouse_y):
            button_sound.play()
            map_flag = True




# экран для объявления конечной победы

def victory(screen, kbtu_image, close_image, victory_sound, button_sound):

    kbtu_image = pygame.transform.scale(kbtu_image, (800, 700))
    kbtu_image_rect = kbtu_image.get_rect()
    kbtu_image_rect.center = screen.get_size().center
    close_image = pygame.transform.scale(close_image, (400, 300))
    close_image_rect = close_image.get_rect()
    close_image_rect.center = (screen.get_width - 250, screen.get_height - 250)
    mouse_x, mouse_y = 0, 0
    color = (0, 0, 0)

    font = pygame.font.Font("fonts/bahnschrift.ttf", 30)
    text = font.render("CONGRATULATIONS!!!", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (kbtu_image_rect.centerx, kbtu_image_rect.centery + 150)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

        victory_sound.play()
        screen.fill(color)
        screen.blit(kbtu_image, kbtu_image_rect)
        screen.blit(text, text_rect)
        screen.blit(close_image, close_image_rect)

        if close_image_rect.collidepoint(mouse_x, mouse_y):
            button_sound.play()
            running = False
            pygame.quit()
'''

