import pygame
pygame.init()

info = pygame.display.Info()
screen_w = info.current_w
screen_h = info.current_h
screen = pygame.display.set_mode((screen_w, screen_h))

move_h = screen.get_height() // 2 - 115 - 180
movement = 0

def Check_colors(color_list):
    for list in color_list:
        if (len(list) > 1):
            for i in range(len(list) - 1):
                if list[i] != list[i + 1]:
                    return False
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
        

    def move_up(self, num):
        self.movement = move_h - self.tube[-1].rect.centery
        coord_list = list(self.coordinates[num])
        coord_list[1] += self.movement
        self.coordinates[num] = tuple(coord_list)
        self.tube[-1].rect.y += self.movement

        
    def move_down(self, num):

        coord_list = list(self.coordinates[num])
        coord_list[1] -= self.movement
        self.coordinates[num] = tuple(coord_list)
        self.tube[-1].rect.y -= self.movement
        self.movement = 0
        

    def show(self, screen, x):
        self.rect.topleft = (x, screen.get_height() // 2 - 225)
        screen.blit(self.image, self.rect)
        for i, ball in enumerate(self.tube):
            ball.rect.center = self.coordinates[i]
            screen.blit(ball.image, ball.rect)



            




def aktobe(screen):

    flag1, flag2, flag3, flag4, flag5 = False, False, False, False, False
    flags = [flag1, flag2, flag3, flag4, flag5]
    mouse_x, mouse_y = 0,0 
    background_aktobe = pygame.transform.scale(pygame.image.load("images/background_aktobe.jpeg"), (screen.get_width(), screen.get_height()))
    test_tube = pygame.transform.scale(pygame.image.load("images/test_tube.png"), (160, 500))
    running = True
    tube_w = []


    for i in range(1, 6):
        tube_w.append(220*i + 130)

    # первая пробирка
    purple1 = PurpleBall()
    red1 = RedBall()
    yellow1_1 = YellowBall()
    yellow1_2 = YellowBall()
    tube1_elements = [purple1, red1, yellow1_1, yellow1_2]
    tube1_colors = ['purple', 'red', 'yellow', 'yellow']
    tube1_coordinates = [(tube_w[0], screen.get_height() // 2 + 200), (tube_w[0], screen.get_height() // 2 + 95),
                         (tube_w[0], screen.get_height() // 2 - 10), (tube_w[0], screen.get_height() // 2 - 115)]
    tube1 = TestTube(tube1_elements, tube1_colors, tube1_coordinates)
    

    # вторая пробирка
    purple2_1 = PurpleBall()
    red2_1 = RedBall()
    purple2_2 = PurpleBall()
    red2_2 = RedBall()
    tube2_elements = [purple2_1, red2_1, purple2_2, red2_2]
    tube2_colors = ['purple', 'red', 'purple', 'red']
    tube2_coordinates = [(tube_w[1], screen.get_height() // 2 + 200), (tube_w[1], screen.get_height() // 2 + 95),
                         (tube_w[1], screen.get_height() // 2 - 10), (tube_w[1], screen.get_height() // 2 - 115)]
    tube2 = TestTube(tube2_elements, tube2_colors, tube2_coordinates)
    

    # третья пробирка
    yellow3_1 = YellowBall()
    purple3 = PurpleBall()
    red3 = RedBall()
    yellow3_2 = YellowBall()
    tube3_elements = [yellow3_1, purple3, red3, yellow3_2]
    tube3_colors = ['yellow', 'purple', 'red', 'yellow']
    tube3_coordinates = [(tube_w[2], screen.get_height() // 2 + 200), (tube_w[2], screen.get_height() // 2 + 95),
                         (tube_w[2], screen.get_height() // 2 - 10), (tube_w[2], screen.get_height() // 2 - 115)]
    tube3 = TestTube(tube3_elements, tube3_colors, tube3_coordinates)  
    
 

    # две пока что пустые пробирки
    tube4_elements = []
    tube4_colors = []
    tube4_coordinates = [(tube_w[3], screen.get_height() // 2 + 200), (tube_w[3], screen.get_height() // 2 + 95),
                         (tube_w[3], screen.get_height() // 2 - 10), (tube_w[3], screen.get_height() // 2 - 115)]
    tube4 = TestTube(tube4_elements, tube4_colors, tube4_coordinates)
    tube5_elements = []
    tube5_colors = [] 
    tube5_coordinates = [(tube_w[4], screen.get_height() // 2 + 200), (tube_w[4], screen.get_height() // 2 + 95),
                         (tube_w[4], screen.get_height() // 2 - 10), (tube_w[4], screen.get_height() // 2 - 115)]
    tube5 = TestTube(tube5_elements, tube5_colors, tube5_coordinates)  
    

    tubes = [tube1, tube2, tube3, tube4, tube5]
    coord = [tube1_coordinates, tube2_coordinates, tube3_coordinates, tube4_coordinates, tube5_coordinates]
    colors = [tube1_colors, tube2_colors, tube3_colors, tube4_colors, tube5_colors]

    selected_ball = None
    selected_tube = None
    ball_flag = False
    selected_color = None

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
        [tubes[i - 1].show(screen, 220*i + 50) for i in range(1, 6)]
        if Check_colors(colors):
            screen.fill("white")

        for i, tube in enumerate(tubes):
            if tube.rect.collidepoint(mouse_x, mouse_y):
                if selected_tube == None and tube.tube:
                    selected_tube = tube
                    selected_ball = tube.tube[-1]
                    selected_tube.move_up(len(selected_tube.tube) - 1)
                    selected_color = tube.colors[-1]
                
                elif selected_tube:
                    if tube.tube:
                        if len(tube.tube) == 4 or tube.colors[-1] != selected_color:
                            selected_tube.move_down(len(selected_tube.tube) - 1)
                            selected_tube = tube
                            selected_ball = tube.tube[-1]
                            selected_tube.move_up(len(selected_tube.tube) - 1)
                            selected_color = tube.colors[-1]
                        elif tube.colors[-1] == selected_color and len(tube.tube) < 4:
                            selected_tube.move_down(len(selected_tube.tube) - 1)
                            tube.tube.append(selected_ball)
                            tube.colors.append(selected_color)
                            selected_tube.tube.pop()
                            selected_tube.colors.pop()
                            selected_tube = None
                            selected_ball = None
                            selected_color = None
                    else:
                        selected_tube.move_down(len(selected_tube.tube) - 1)
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



