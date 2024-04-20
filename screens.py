import pygame

# самый начальный экран, который показывается только раз при запуске кода: на экране только кнопка "START THE GAME!"

def menu(menu_flag, screen, button_start_the_game, button_sound, background_sound):
    
    color = (0, 0, 0)
    mouse_x, mouse_y = 0, 0
    button_start_the_game = pygame.transform.scale(pygame.image.load(""))
    button_start_the_game_rect = button_start_the_game.get_rect()
    button_start_the_game_rect.center = screen.get_rect().center 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
        background_sound.play()
        screen.fill(color)
        screen.blit(button_start_the_game, button_start_the_game_rect)

        if button_start_the_game_rect.collidepoint(mouse_x, mouse_y):
            button_sound.play()
            menu_flag = False




# экран паузы, на экране три кнопки: retry(начать мини-игру заново), continue(продолжить мини-игру), map(выйти в меню с картой)

def pause(screen, pause_flag, retry_flag, map_flag, retry_image, continue_image,
           map_image, button_sound, background_sound):

    screen_width, screen_height = screen.get_size()
    color = (0, 0, 0)
    # экспериментально подобрала размеры кнопок...
    a = screen_height * (7/13)
    b = screen_width * (18/35)

    # приводим все кнопки до одинакого размера
    retry_image = pygame.transform.scale(retry_image, (a * (2/7), b))
    continue_image = pygame.transform.scale(continue_image, (a * (2/7), b))
    map_image = pygame.transform.scale(map_image, (a * (2/7), b))


    retry_image_rect = retry_image.get_rect()
    continue_image_rect = continue_image.get_rect()
    map_image_rect = map_image.get_rect()

    continue_image_rect.topleft = (screen_width * (17/70), screen_height * (3/13))
    retry_image_rect.topleft = (screen_width * (17/70), screen_height * (3/13) + a * (5/14))
    map_image_rect.topleft = (screen_width * (17/70), screen_height * (3/13) + a * (5/7))

    mouse_x, mouse_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
            
        background_sound.play()
        screen.fill(color)
        # так же экспериментально подобрала местоположения кнопок...

        screen.blit(continue_image, continue_image_rect)
        screen.blit(retry_image, retry_image_rect)
        screen.blit(map_image, map_image_rect)
        
        if continue_image_rect.collidepoint(mouse_x, mouse_y):
            button_sound.play()
            pause_flag = False
        elif retry_image_rect.collidepoint(mouse_x, mouse_y):
            button_sound.play()
            pause_flag = False 
            retry_flag = True
        elif map_image_rect.collidepoint(mouse_x, mouse_y):
            button_sound.play()
            pause_flag = False
            retry_flag = True
            map_flag = True




# основной экран с картой Казахстана

def map(screen, almaty_flag, pavlodar_flag, aktobe_flag, map_flag, map_image,
        ala_ball_x, ala_ball_y, pvl_ball_x, pvl_ball_y, akx_ball_x, akx_ball_y,
        ala_bubble_image, pvl_bubble_image, akx_bubble_image,
        background_sound, sound_of_choice):
    
    ball_radius = 8
    map_image = pygame.transform.scale(map_image, screen.get_size())
    mouse_x, mouse_y = 0, 0
    bubble_x, bubble_y = 0, 0
    bubble_size = (100, 100)
    ala_bubble = pygame.transform.scale(ala_bubble_image, bubble_size)
    pvl_bubble = pygame.transform.scale(pvl_bubble_image, bubble_size)
    akx_bubble = pygame.transform.scale(pvl_bubble_image, bubble_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEMOTION:
                bubble_x, bubble_y = event.pos

        # устанавливаем на весь экран карту
        screen.blit(map_image, (0,0))

        background_sound.play()

        pygame.draw.circle(screen, "red", (ala_ball_x, ala_ball_y), 8)
        pygame.draw.circle(screen, "red", (pvl_ball_x, pvl_ball_y), 8)
        pygame.draw.circle(screen, "red", (akx_ball_x, akx_ball_y), 8)

        ball_size = int(ball_radius * 2 ** 0.5)
        ala_ball = pygame.Rect(ala_ball_x, ala_ball_y,  ball_size, ball_size)
        pvl_ball = pygame.Rect(pvl_ball_x, pvl_ball_y,  ball_size, ball_size)
        akx_ball = pygame.Rect(akx_ball_x, akx_ball_y,  ball_size, ball_size)


        if ala_ball.collidepoint(bubble_x, bubble_y):
            screen.blit(ala_bubble, (ala_ball_x, ala_ball_y))
        elif pvl_ball.collidepoint(bubble_x, bubble_y):
            screen.blit(pvl_bubble, (pvl_ball_x, pvl_ball_y))
        elif akx_ball.collidepoint(bubble_x, bubble_y):
            screen.blit(akx_bubble, (akx_ball_x, akx_ball_y))

        if ala_ball.collidepoint(mouse_x, mouse_y):
            sound_of_choice.play()
            almaty_flag = True
            pavlodar_flag = False
            aktobe_flag = False
            map_flag = False
        elif pvl_ball.collidepoint(mouse_x, mouse_y):
            sound_of_choice.play()
            pavlodar_flag = True
            almaty_flag = False
            aktobe_flag = False
            map_flag = False
        elif akx_ball.collidepoint(mouse_x, mouse_y):
            sound_of_choice.play()
            aktobe_flag = True
            almaty_flag = False
            pavlodar_flag = False
            map_flag = False




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
