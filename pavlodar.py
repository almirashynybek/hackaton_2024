import pygame
import os
import random
pygame.init()

info = pygame.display.Info()
screen_w = info.current_w
screen_h = info.current_h
screen = pygame.display.set_mode((screen_w, screen_h))
RUNNING = [pygame.transform.scale(pygame.image.load("images/run1.png"), (200, 250)),
           pygame.transform.scale(pygame.image.load("images/run2.png"), (200, 250))]
JUMPING = [pygame.transform.scale(pygame.image.load("images/person_stand.png"), (200, 250))]
DUCKING = [pygame.transform.scale(pygame.image.load("images/ducking1.png"), (200, 230)), 
           pygame.transform.scale(pygame.image.load("images/ducking2.png"), (200, 230))]
OBSTACLES = [pygame.transform.scale(pygame.image.load("images/rock.png"), (100, 70)),
             pygame.transform.scale(pygame.image.load("images/2rock.png"), (170, 70)),
             pygame.transform.scale(pygame.image.load("images/3rock.png"), (230, 70))]
BIRDS = [pygame.transform.scale(pygame.image.load("images/bird.png"), (200, 70)),
         pygame.transform.scale(pygame.image.load("images/bird2.png"), (200, 70))]
CLOUDS = [pygame.transform.scale(pygame.image.load("images/cloud.png"), (250, 100)),
          pygame.transform.scale(pygame.image.load("images/cloud2.png"), (250, 100)),
          pygame.transform.scale(pygame.image.load("images/cloud3.png"), (150, 60)),
          pygame.transform.scale(pygame.image.load("images/cloud4.png"), (400, 70)),
          pygame.transform.scale(pygame.image.load("images/cloud5.png"), (150, 60)),
          pygame.transform.scale(pygame.image.load("images/cloud6.png"), (250, 100))]


class Person:
    x_pos = 80
    y_pos = 500
    y_pos_duck = 530
    jump_velocity = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING[0]

        self.person_duck = False
        self.person_run = True
        self.person_jump = False

        self.step_index = 0
        self.jump_vel = self.jump_velocity
        self.image = self.run_img[0]
        self.person_rect = self.image.get_rect()
        self.person_rect.x = self.x_pos
        self.person_rect.y = self.y_pos

    def update(self, userInput):
        if self.person_run:
            self.run()
        if self.person_jump:
            self.jump()
        if self.person_duck:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_UP] and not self.person_jump:
            self.person_jump = True
            self.person_duck = False
            self.person_run = False
        elif userInput[pygame.K_DOWN] and not self.person_jump:
            self.person_jump = False
            self.person_run = False
            self.person_duck = True
        elif not (self.person_jump or userInput[pygame.K_DOWN]):
            self.person_duck = False
            self.person_jump = False
            self.person_run = True


    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.person_rect = self.image.get_rect()
        self.person_rect.x = self.x_pos
        self.person_rect.y = self.y_pos_duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.person_rect = self.image.get_rect()
        self.person_rect.x = self.x_pos
        self.person_rect.y = self.y_pos
        self.step_index += 1
    
    def jump(self):
        self.image = self.jump_img
        if self.person_jump:
            self.person_rect.y -= self.jump_vel * 5
            self.jump_vel -= 0.8
        if self.jump_vel < - self.jump_velocity:
            self.person_jump = False
            self.jump_vel = self.jump_velocity

    def show(self, screen):
        screen.blit(self.image, self.person_rect)


class Cloud:
    def __init__(self):
        self.INDEX = 0
        self.x = screen_w + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.index = self.INDEX
        self.image = CLOUDS[self.index]
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = screen_w + random.randint(2500, 3000)
            self.y = random.randint(50, 200)
            self.INDEX = random.randint(0, 5)
            self.image = CLOUDS[self.INDEX]
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
        

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_w

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def show(self, screen):
        screen.blit(self.image[self.type], self.rect)


class Rocks(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 700

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 440
        self.index = 0

    def show(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1



def pavlodar():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    obstacles = []
    game_speed = 17
    x_pos_bg = 0
    y_pos_bg = 730
    points = 0

    background = pygame.transform.scale(pygame.image.load('images/background_pvl_main.png'), (screen_w, screen_h))
    ground = pygame.transform.scale(pygame.image.load('images/ground.png'), (screen_w, screen_h - 730))
    clock = pygame.time.Clock()
    player = Person()
    cloud = Cloud()

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        font = pygame.font.Font("fonts/PIXY.ttf", 40)
        text = font.render("POINTS: " + str(points), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen_w - 180, 50)
        screen.blit(text, text_rect)

    def Background():
        global x_pos_bg, y_pos_bg
        image_width = ground.get_width()
        screen.blit(ground, (x_pos_bg, y_pos_bg))
        screen.blit(ground, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= - image_width:
            screen.blit(ground, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        screen.blit(background, (0,0))
        userInput = pygame.key.get_pressed()

        Background()

        player.show(screen)
        player.update(userInput)
        
        if not obstacles:
            if random.randint(0, 1) == 0:
                obstacles.append(Rocks(OBSTACLES))
            elif random.randint(0, 1) == 1:
                obstacles.append(Bird(BIRDS))

        for obstacle in obstacles:
            obstacle.show(screen)
            obstacle.update()
            if player.person_rect.colliderect(obstacle.rect) and not player.person_jump:
                pygame.quit()

        cloud.show(screen)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

pavlodar()