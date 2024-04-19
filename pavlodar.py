import pygame
import os
pygame.init()

info = pygame.display.Info()
screen_w = info.current_w
screen_h = info.current_h
screen = pygame.display.set_mode((screen_w, screen_h))
RUNNING = [pygame.transform.scale(pygame.image.load("images/run1.png"), (200, 250)), pygame.transform.scale(pygame.image.load("images/run2.png"), (200, 250))]
JUMPING = [pygame.transform.scale(pygame.image.load("images/person_stand.png"), (200, 250))]
OBSTACLES = [pygame.image.load("images/rock.png"), pygame.image.load("images/2rock.png"),
             pygame.image.load("images/3rock.png")]
BIRDS = [pygame.image.load("images/bird.png"), pygame.image.load("images/bird2.png")]
 


class Person:
    x_pos = 80
    y_pos = 310
    jump_velocity = 8.5

    def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMPING[0]

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

        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_SPACE] and not self.person_jump:
            self.person_jump = True
            self.person_run = False
        elif not self.person_jump:
            self.person_jump = False
            self.person_run = True

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.person_rect = self.image.get_rect()
        self.person_rect.x = self.x_pos
        self.person_rect.y = self.y_pos
        self.step_index += 1
    
    def jump(self):
        self.image = self.jump_img
        if self.person_jump:
            self.person_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.jump_velocity:
            self.person_jump = False
            self.jump_vel = self.jump_velocity

    def show(self, screen):
        screen.blit(self.image, self.person_rect)

def pavlodar():
    global game_speed
    game_speed = 14
    background = pygame.transform.scale(pygame.image.load('images/background_pvl.png'), (screen_w, screen_h))
    clock = pygame.time.Clock()
    player = Person()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        #screen.blit(background, (0,0))
        screen.fill("white")
        userInput = pygame.key.get_pressed()


        player.show(screen)
        player.update(userInput)
        clock.tick(30)
        pygame.display.update()

pavlodar()