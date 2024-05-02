import pygame
import os
import time
import random
import screens
import flags
pygame.init()

info = pygame.display.Info()
screen_w = info.current_w
screen_h = info.current_h
screen = pygame.display.set_mode((screen_w, screen_h))
jump_sound = pygame.mixer.Sound('sounds/up.mp3')
background_sound = pygame.mixer.Sound('sounds/background_sound.mp3')
RUNNING = [pygame.transform.scale(pygame.image.load("images/person/run1.png"), (200, 250)),
           pygame.transform.scale(pygame.image.load("images/person/run2.png"), (200, 250))]
JUMPING = [pygame.transform.scale(pygame.image.load("images/person/person_stand.png"), (200, 250))]
DUCKING = [pygame.transform.scale(pygame.image.load("images/person/ducking1.png"), (200, 230)), 
           pygame.transform.scale(pygame.image.load("images/person/ducking2.png"), (200, 230))]
SMALL_OBSTACLES = [pygame.transform.scale(pygame.image.load("images/obstacles/rock.png"), (100, 70)),
             pygame.transform.scale(pygame.image.load("images/obstacles/2rock.png"), (170, 70)),
             pygame.transform.scale(pygame.image.load("images/obstacles/3rock.png"), (230, 70))]
BIG_OBSTACLES = [pygame.transform.scale(pygame.image.load("images/obstacles/konus1.png"), (100, 150)),
                 pygame.transform.scale(pygame.image.load("images/obstacles/konus2.png"), (200, 150)),
                 pygame.transform.scale(pygame.image.load("images/obstacles/konus3.png"), (300, 150))]
BIRDS = [pygame.transform.scale(pygame.image.load("images/obstacles/bird.png"), (200, 70)),
         pygame.transform.scale(pygame.image.load("images/obstacles/bird2.png"), (200, 70))]
CLOUDS = [pygame.transform.scale(pygame.image.load("images/clouds/cloud.png"), (250, 100)),
          pygame.transform.scale(pygame.image.load("images/clouds/cloud2.png"), (250, 100)),
          pygame.transform.scale(pygame.image.load("images/clouds/cloud3.png"), (150, 60)),
          pygame.transform.scale(pygame.image.load("images/clouds/cloud4.png"), (400, 70)),
          pygame.transform.scale(pygame.image.load("images/clouds/cloud5.png"), (150, 60)),
          pygame.transform.scale(pygame.image.load("images/clouds/cloud6.png"), (250, 100))]


class Person:
    x_pos = 80
    y_pos = 500
    y_pos_duck = 530
    jump_velocity = 8.5

    def __init__(self):
        self.sound_count = 0
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING[0]

        self.person_duck = False
        self.person_run = True
        self.person_jump = False
        self.jump_sound_played = False

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
            self.jump_sound_played = False
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
        if not self.jump_sound_played:
            jump_sound.play()
            self.jump_sound_played = True
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

class Cone(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 600

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

global victory3
victory3 = False

def pavlodar():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    obstacles = []
    game_speed = 25
    x_pos_bg = 0
    y_pos_bg = 730
   
    mouse_x, mouse_y = 0, 0
    points = 0
    global victory3
    victory3 = False

    background_button = pygame.transform.scale(pygame.image.load("images/backgrounds/background_buttons.jpg"), (screen_w, screen_h))
    background = pygame.transform.scale(pygame.image.load('images/backgrounds/background_pvl_main.png'), (screen_w, screen_h))
    ground = pygame.transform.scale(pygame.image.load('images/backgrounds/ground.png'), (screen_w, screen_h - 730))
    clock = pygame.time.Clock()
    player = Person()
    cloud = Cloud()

    settings = pygame.transform.scale(pygame.image.load("images/settings.png"), (50, 50))
    settings_rect = settings.get_rect()
    settings_rect.topleft = (screen_w - 70, 20)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 2

        font = pygame.font.Font("fonts/PIXY.ttf", 40)
        text = font.render("POINTS: " + str(points), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen_w - 200, 50)
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


    retry_image = pygame.transform.scale(pygame.image.load("images/buttons/retry.png"), (500, 120))
    continue_image = pygame.transform.scale(pygame.image.load("images/buttons/close.png"), (500, 120))
    menu_image = pygame.transform.scale(pygame.image.load("images/buttons/menu.png"), (500, 120))

    retry_image_rect = retry_image.get_rect()
    continue_image_rect = continue_image.get_rect()
    menu_image_rect = menu_image.get_rect()

    continue_image_rect.topleft = (screen_w//2 - 250, 150)
    retry_image_rect.topleft = (screen_w//2 - 250, 350)
    menu_image_rect.topleft = (screen_w//2 - 250, 550)

    button_click = pygame.mixer.Sound('sounds/button.mp3')
    #background_sound.play(-1)
    pause = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
        
        if not pause:
            screen.blit(background, (0,0))
            userInput = pygame.key.get_pressed()

            Background()
            

            player.show(screen)
            player.update(userInput)
            
            if not obstacles:
                if random.randint(0, 2) == 0:
                    obstacles.append(Rocks(SMALL_OBSTACLES))
                elif random.randint(0, 2) == 1:
                    obstacles.append(Cone(BIG_OBSTACLES))
                elif random.randint(0, 2) == 2:
                    obstacles.append(Bird(BIRDS))

            for obstacle in obstacles:
                obstacle.show(screen)
                obstacle.update()
                if player.person_rect.colliderect(obstacle.rect) and not player.person_jump:
                    pavlodar()

            cloud.show(screen)
            cloud.update()

            score()
            
            screen.blit(settings, settings_rect)

            if settings_rect.collidepoint(mouse_x, mouse_y):
                button_click.play()
                pause = True
                
            if points == 1500:
                time.sleep(0.5)
                flags.victory3 = True
                screens.win2()

            clock.tick(30)
        else:
            screen.blit(background_button, (0,0))

            # так же экспериментально подобрала местоположения кнопок...
            screen.blit(continue_image, continue_image_rect)
            screen.blit(retry_image, retry_image_rect)
            screen.blit(menu_image, menu_image_rect)
            
            if continue_image_rect.collidepoint(mouse_x, mouse_y):
                button_click.play()
                pause = False
            elif retry_image_rect.collidepoint(mouse_x, mouse_y):
                button_click.play()
                pavlodar()
            elif menu_image_rect.collidepoint(mouse_x, mouse_y):
                button_click.play()
                screens.map()
        pygame.display.update()

