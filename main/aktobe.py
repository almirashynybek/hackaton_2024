import pygame
import time
import screens
import screens
import flags
pygame.init()



def aktobe():
    
    info = pygame.display.Info()
    screen_w = info.current_w
    screen_h = info.current_h
    screen = pygame.display.set_mode((screen_w, screen_h))

    # move_h - высота, на которую будут подниматься шарики при нажатии на пробирку
    move_h = screen.get_height() // 2 - 295

    


    # проверка на 4 одинаковых шарика в пробирке
    def Check_identity(color_list):
        for i in range(len(color_list) - 1):
            if color_list[i] != color_list[i + 1]:
                return False
        if len(color_list) == 4:
            return True
        
    def Check(colors):
        count = 0
        for list in colors:
            if Check_identity(list):
                count += 1
        if count == 3:
            return True
        return False

    # класс для красных шариков для автоматического определения изображения и его прямоугольника
    class RedBall(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load('images/aktobe/red_ball.png'), (100, 100))
            self.rect = self.image.get_rect()
            
    # класс для фиолетовых шариков для автоматического определения изображения и его прямоугольника 
    class PurpleBall(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load('images/aktobe/purple_ball.png'), (100, 100))
            self.rect = self.image.get_rect()

    # класс для желтых шариков для автоматического определения изображения и его прямоугольника
    class YellowBall(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load('images/aktobe/yellow_ball.png'), (100, 100))
            self.rect = self.image.get_rect()

    # класс для пробирок для автоматического определения изображения пробирки и ее прямоугольника, какие именно шарики находятся
    # в пробирке (список шаров), каких именно они цветов и по каким координатам нужно отображать шары в конкретной пробирке,
    # а также на сколько пикселей нужно подняться определенному шарику, чтобы достигнуть move_h и т.д. 
    class TestTube:
        def __init__(self, tube, colors, coordinates):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load("images/aktobe/test_tube.png"), (160, 500))
            self.rect = self.image.get_rect()
            self.tube = tube
            self.colors = colors
            self.coordinates = coordinates
            self.movement = 0
            
        # поднятие шарика с индексом ball_index на высоту move_h 
        def move_up(self, ball_index):
            self.movement = move_h - self.tube[-1].rect.centery
            coord_list = list(self.coordinates[ball_index])
            coord_list[1] += self.movement
            self.coordinates[ball_index] = tuple(coord_list)
            self.tube[-1].rect.y += self.movement

        # опускание шарика с индексом ball_index с высоты move_h
        def move_down(self, ball_index):
            coord_list = list(self.coordinates[ball_index])
            coord_list[1] -= self.movement
            self.coordinates[ball_index] = tuple(coord_list)
            self.tube[-1].rect.y -= self.movement
            self.movement = 0
            
        # отображение шаров на экране
        def show(self, screen, x):
            self.rect.topleft = (x, screen.get_height() // 2 - 225)
            screen.blit(self.image, self.rect)
            for i, ball in enumerate(self.tube):
                ball.rect.center = self.coordinates[i]
                screen.blit(ball.image, ball.rect)

    def game(screen):
        mouse_x, mouse_y = 0,0 
        background_aktobe = pygame.transform.scale(pygame.image.load("images/backgrounds/background_aktobe.png"), (screen.get_width(), screen.get_height()))
        settings = pygame.transform.scale(pygame.image.load("images/settings.png"), (50, 50))
        settings_rect = settings.get_rect()
        settings_rect.topleft = (screen_w - 70, 20)


        retry_image = pygame.transform.scale(pygame.image.load("images/buttons/retry.png"), (500, 120))
        continue_image = pygame.transform.scale(pygame.image.load("images/buttons/close.png"), (500, 120))
        menu_image = pygame.transform.scale(pygame.image.load("images/buttons/menu.png"), (500, 120))

        retry_image_rect = retry_image.get_rect()
        continue_image_rect = continue_image.get_rect()
        menu_image_rect = menu_image.get_rect()

        continue_image_rect.topleft = (screen_w//2 - 250, 150)
        retry_image_rect.topleft = (screen_w//2 - 250, 350)
        menu_image_rect.topleft = (screen_w//2 - 250, 550)

        
        # определяем на какой ширине будут находиться верхние левые углы прямоугольников пробирок
        tubes_width = []
        for i in range(1, 6):
            tubes_width.append(220*i + 130)

        # наполнение первой пробирки с определенными координатами
        purple1, red1, yellow1_1, yellow1_2 = PurpleBall(), RedBall(), YellowBall(), YellowBall()
        tube1_elements = [purple1, red1, yellow1_1, yellow1_2]
        tube1_colors = ['purple', 'red', 'yellow', 'yellow']
        tube1_coordinates = [(tubes_width[0], screen.get_height() // 2 + 200), (tubes_width[0], screen.get_height() // 2 + 95),
                            (tubes_width[0], screen.get_height() // 2 - 10), (tubes_width[0], screen.get_height() // 2 - 115)]
        tube1 = TestTube(tube1_elements, tube1_colors, tube1_coordinates)
        

        # вторая пробирка
        purple2_1, red2_1, purple2_2, red2_2 = PurpleBall(), RedBall(), PurpleBall(), RedBall()
        tube2_elements = [purple2_1, red2_1, purple2_2, red2_2]
        tube2_colors = ['purple', 'red', 'purple', 'red']
        tube2_coordinates = [(tubes_width[1], screen.get_height() // 2 + 200), (tubes_width[1], screen.get_height() // 2 + 95),
                            (tubes_width[1], screen.get_height() // 2 - 10), (tubes_width[1], screen.get_height() // 2 - 115)]
        tube2 = TestTube(tube2_elements, tube2_colors, tube2_coordinates)
        

        # третья пробирка
        yellow3_1, purple3, red3, yellow3_2 = YellowBall(), PurpleBall(), RedBall(), YellowBall()
        tube3_elements = [yellow3_1, purple3, red3, yellow3_2]
        tube3_colors = ['yellow', 'purple', 'red', 'yellow']
        tube3_coordinates = [(tubes_width[2], screen.get_height() // 2 + 200), (tubes_width[2], screen.get_height() // 2 + 95),
                            (tubes_width[2], screen.get_height() // 2 - 10), (tubes_width[2], screen.get_height() // 2 - 115)]
        tube3 = TestTube(tube3_elements, tube3_colors, tube3_coordinates)  
        
    

        # две пока что пустые пробирки
        tube4_elements = []
        tube4_colors = []
        tube4_coordinates = [(tubes_width[3], screen.get_height() // 2 + 200), (tubes_width[3], screen.get_height() // 2 + 95),
                            (tubes_width[3], screen.get_height() // 2 - 10), (tubes_width[3], screen.get_height() // 2 - 115)]
        tube4 = TestTube(tube4_elements, tube4_colors, tube4_coordinates)

        tube5_elements = []
        tube5_colors = [] 
        tube5_coordinates = [(tubes_width[4], screen.get_height() // 2 + 200), (tubes_width[4], screen.get_height() // 2 + 95),
                            (tubes_width[4], screen.get_height() // 2 - 10), (tubes_width[4], screen.get_height() // 2 - 115)]
        tube5 = TestTube(tube5_elements, tube5_colors, tube5_coordinates)  
        

        tubes = [tube1, tube2, tube3, tube4, tube5]
        #colors = [tube1_colors, tube2_colors, tube3_colors, tube4_colors, tube5_colors]

        full_tube = pygame.mixer.Sound('sounds/full_tube.mp3')
        ball_down = pygame.mixer.Sound('sounds/up.mp3')
        ball_up = pygame.mixer.Sound('sounds/down.mp3')

        background_button = pygame.transform.scale(pygame.image.load("images/backgrounds/background_buttons.jpg"), (screen_w, screen_h))
        # выбранные пробирка, шарик и цвет - это конкретного цвет конкретный шарик из конкретной пробирки, который мы собираемся перемещать
        selected_ball = None
        selected_tube = None
        selected_color = None
        press_x, press_y = 0, 0
        button_click = pygame.mixer.Sound('sounds/button.mp3')
        pause = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    press_x, press_y = event.pos
            if not pause:
                screen.blit(background_aktobe, (0,0))
                
                # отображаем пробирки с шариками
                screen.blit(settings, settings_rect)
                [tubes[i - 1].show(screen, 220*i + 50) for i in range(1, 6)]
                colors = []
                # перемещение шаров
                for i, tube in enumerate(tubes):
                    
                    # если нажали на пробирку
                    if tube.rect.collidepoint(mouse_x, mouse_y):
                        # если до нажатия на пробирку у нас не было шарика, который мы собирались переместить, то теперь есть, при условии, что пробирка не пуста
                        if selected_tube == None and tube.tube:
                            selected_tube = tube
                            selected_ball = tube.tube[-1]
                            selected_color = tube.colors[-1]
                            selected_tube.move_up(len(selected_tube.tube) - 1)
                            ball_up.play()
                        # если у нас уже был выбранный шарик для перемещения, значит мы нажали на пробирку, в которую хотим перенести этот шарик
                        elif selected_tube:
                            # если пробирка не пустая
                            if tube.tube:
                                # и либо заполненная, либо цвет последнего в ней шарика не совпадает с нашим, который хотим перенести, то меняет выбранный для перемещения шар
                                if len(tube.tube) == 4 or tube.colors[-1] != selected_color:
                                    selected_tube.move_down(len(selected_tube.tube) - 1)
                                    ball_down.play()
                                    selected_tube = tube
                                    selected_ball = tube.tube[-1]
                                    selected_color = tube.colors[-1]
                                    selected_tube.move_up(len(selected_tube.tube) - 1)
                                    ball_up.play()
                                # если все-таки цвета совпадают и пробирка не заполнена, то перемещаем шар
                                elif tube.colors[-1] == selected_color and len(tube.tube) < 4:
                                    selected_tube.move_down(len(selected_tube.tube) - 1)
                                    ball_down.play()
                                    tube.tube.append(selected_ball)
                                    tube.colors.append(selected_color)
                                    if Check_identity(tube.colors):
                                        full_tube.play(maxtime = 1000)
                                    selected_tube.tube.pop()
                                    selected_tube.colors.pop()
                                    selected_tube = None
                                    selected_ball = None
                                    selected_color = None
                            # если пробирка, в которую мы хотим пернести шар, пуста, то спокойно перемещаем без каких-либо проверок
                            else:
                                selected_tube.move_down(len(selected_tube.tube) - 1)
                                ball_down.play()
                                tube.tube.append(selected_ball)
                                tube.colors.append(selected_color)
                                selected_tube.tube.pop()
                                selected_tube.colors.pop()
                                selected_tube = None
                                selected_ball = None
                                selected_color = None
                        
                        mouse_x, mouse_y = 0, 0
                    colors.append(tube.colors)
                
                if Check(colors):
                    time.sleep(0.5)
                    flags.victory2 = True
                    screens.win1()
                if settings_rect.collidepoint(mouse_x, mouse_y):
                    button_click.play()
                    pause = True

            else:
                screen.blit(background_button, (0,0))
                screen.blit(continue_image, continue_image_rect)
                screen.blit(retry_image, retry_image_rect)
                screen.blit(menu_image, menu_image_rect)
            
                if continue_image_rect.collidepoint(press_x, press_y):
                    button_click.play()
                    pause = False
                elif retry_image_rect.collidepoint(press_x, press_y):
                    button_click.play()
                    aktobe()
                elif menu_image_rect.collidepoint(press_x, press_y):
                    button_click.play()
                    screens.map()
            
            pygame.display.flip()
    game(screen)