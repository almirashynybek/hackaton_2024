import pygame
import menus


pygame.init()

# устанавливаем экран
info = pygame.display.Info()
screen_w = info.current_w
screen_h = info.current_h
screen = pygame.display.set_mode((screen_w, screen_h))

# включаем фоновый звук игры, который будет проигрываться бесконечно
background_sound = pygame.mixer.Sound('sounds/background_sound.mp3')
background_sound.play(-1)

# устанавливаем кнопку, которая начнет игру. устанавливаем звук, который будет проигрываться после нажатия кнопки
button_start_the_game = pygame.transform.scale(pygame.image.load("images/buttons/start_the_game.png"), (800, 250))
button_start_the_game_rect = button_start_the_game.get_rect()
button_start_the_game_rect.center = screen.get_rect(). center
button_click = pygame.mixer.Sound('sounds/button.mp3')


# для установки координат нажатия мыши
press_x, press_y = 0, 0

background_button = pygame.transform.scale(pygame.image.load("images/backgrounds/background_buttons.jpg"), (screen_w, screen_h))

# основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # если нажали на левую кнопку мыши, запоминаем координаты нажатия
        if event.type == pygame.MOUSEBUTTONDOWN:
            press_x, press_y = event.pos
    # устанавливаем кнопку "START THE GAME!" на черном фоне
    screen.blit(background_button, (0,0))
    screen.blit(button_start_the_game, button_start_the_game_rect)    
        
    # если нажали на кнопку, то игра начинается
    if button_start_the_game_rect.collidepoint(press_x, press_y):
        button_click.play()
        menus.menu()
    



    pygame.display.flip()