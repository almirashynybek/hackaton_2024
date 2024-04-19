import pygame
import time
import screens
pygame.init()

info = pygame.display.Info()
screen_w = info.current_w
screen_h = info.current_h
screen = pygame.display.set_mode((screen_w, screen_h))

move_h = screen.get_height() // 2 - 295

def Check_identity(color_list):
    for i in range(len(color_list) - 1):
        if color_list[i] != color_list[i + 1]:
            return False
    if len(color_list) == 4:
        return True

class RedBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/red_ball.png'), (100, 100))
        self.rect = self.image.get_rect()
        

class PurpleBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/purple_ball.png'), (100, 100))
        self.rect = self.image.get_rect()


class YellowBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/yellow_ball.png'), (100, 100))
        self.rect = self.image.get_rect()

class TestTube:
    def __init__(self, tube, colors, coordinates):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/test_tube.png"), (160, 500))
        self.rect = self.image.get_rect()
        self.tube = tube
        self.colors = colors
        self.coordinates = coordinates
        self.movement = 0
        

    def move_up(self, ball_index):
        self.movement = move_h - self.tube[-1].rect.centery
        coord_list = list(self.coordinates[ball_index])
        coord_list[1] += self.movement
        self.coordinates[ball_index] = tuple(coord_list)
        self.tube[-1].rect.y += self.movement

        
    def move_down(self, ball_index):
        coord_list = list(self.coordinates[ball_index])
        coord_list[1] -= self.movement
        self.coordinates[ball_index] = tuple(coord_list)
        self.tube[-1].rect.y -= self.movement
        self.movement = 0
        

    def show(self, screen, x):
        self.rect.topleft = (x, screen.get_height() // 2 - 225)
        screen.blit(self.image, self.rect)
        for i, ball in enumerate(self.tube):
            ball.rect.center = self.coordinates[i]
            screen.blit(ball.image, ball.rect)



            




def aktobe(screen):
    mouse_x, mouse_y = 0,0 
    #background_aktobe = pygame.transform.scale(pygame.image.load("images/background_aktobe.jpeg"), (screen.get_width(), screen.get_height()))
    test_tube = pygame.transform.scale(pygame.image.load("images/test_tube.png"), (160, 500))
    settings = pygame.transform.scale(pygame.image.load("images/settings_y.png"), (50, 50))
    settings_rect = settings.get_rect()
    settings_rect.topleft = (screen_w - 70, 20)

    tubes_width = []
    for i in range(1, 6):
        tubes_width.append(220*i + 130)

    # первая пробирка
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

    full_tube = pygame.mixer.Sound('sounds/full_tube.mp3')
    ball_down = pygame.mixer.Sound('sounds/up.mp3')
    ball_up = pygame.mixer.Sound('sounds/down.mp3')

    selected_ball = None
    selected_tube = None
    selected_color = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    pygame.quit()
        #screen.blit(background_aktobe, (0,0))
        screen.fill("black")
        screen.blit(settings, settings_rect)
        [tubes[i - 1].show(screen, 220*i + 50) for i in range(1, 6)]

        
        
        for i, tube in enumerate(tubes):
            if tube.rect.collidepoint(mouse_x, mouse_y):
                if selected_tube == None and tube.tube:
                    selected_tube = tube
                    selected_ball = tube.tube[-1]
                    selected_tube.move_up(len(selected_tube.tube) - 1)
                    ball_up.play()
                    selected_color = tube.colors[-1]
                elif selected_tube:
                    if tube.tube:
                        if len(tube.tube) == 4 or tube.colors[-1] != selected_color:
                            selected_tube.move_down(len(selected_tube.tube) - 1)
                            ball_down.play()
                            selected_tube = tube
                            selected_ball = tube.tube[-1]
                            selected_color = tube.colors[-1]
                            selected_tube.move_up(len(selected_tube.tube) - 1)
                            ball_up.play()
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
        pygame.display.flip()
        


aktobe(screen)



