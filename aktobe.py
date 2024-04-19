import pygame

class RedBall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/red_ball.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def move(self):
        self.rect.move_ip(0, -60)
        

class PurpleBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/purple_ball.png'), (50, 50))
        self.rect = self.image.get_rect()
    
    def move(self):
        self.rect.move_ip(0, -60)


class YellowBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/yellow_ball.png'), (50, 50))
        self.rect = self.image.get_rect()
    
    def move(self):
        self.rect.move_ip(0, -60)


class Tube()

def aktobe(screen):

    background_aktobe = pygame.transform.scale(pygame.image.load("images/background_aktobe.avif"), (screen.get_width(), screen.get_height()))
    test_tube = pygame.transform.scale(pygame.image.load("images/test_tube.png"), (120, 450))
    running = True

    # первая пробирка
    purple1 = PurpleBall()
    red1 = RedBall()
    yellow1_1 = YellowBall()
    yellow1_2 = YellowBall()
    tube1 = [purple1, red1, yellow1_1, yellow1_2]

    # вторая пробирка
    purple2_1 = PurpleBall()
    red2_1 = RedBall()
    purple2_2 = PurpleBall()
    red2_2 = RedBall()
    tube2 = [purple2_1, red2_1, purple2_2, red2_2]

    # третья пробирка
    yellow3_1 = YellowBall()
    purple3 = PurpleBall()
    red3 = RedBall()
    yellow3_2 = YellowBall()
    tube3 = [yellow3_1, purple3, red3, yellow3_2]

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
        screen.blit(background_aktobe, (0,0))

        for i in range(1, 6):
            screen.blit(test_tube, (220*i + 50, screen.get_height() // 2 - 225))
        
        screen.blit(purple1,)


