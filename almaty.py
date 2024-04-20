
import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("mountain-removebg-preview.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, background.get_height()))

background_y = SCREEN_HEIGHT - background.get_height()

BLACK = (0, 0, 0)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

clock = pygame.time.Clock()

background_speed = 0
player_change_time = 100
last_player_change = pygame.time.get_ticks()


class Player(pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT
        self.index = 0
        self.change_time = 200
        self.last_change = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change > self.change_time:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.last_change = current_time


class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('s3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-SCREEN_HEIGHT, -100),
        )
        self.speed = 4

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (
                random.randint(40, SCREEN_WIDTH - 40),
                random.randint(-SCREEN_HEIGHT, -100),
            )
            self.speed = 4

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('s5.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-SCREEN_HEIGHT, -100),
        )
        self.speed = 4

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (
                random.randint(40, SCREEN_WIDTH - 40),
                random.randint(-SCREEN_HEIGHT, -100),
            )
            self.speed = 4


class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('s6.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-SCREEN_HEIGHT, -100),
        )
        self.speed = 4

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (
                random.randint(40, SCREEN_WIDTH - 40),
                random.randint(-SCREEN_HEIGHT, -100),
            )
            self.speed = 4


class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('stone1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-SCREEN_HEIGHT, -100),
        )
        self.speed = 4

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (
                random.randint(40, SCREEN_WIDTH - 40),
                random.randint(-SCREEN_HEIGHT, -100),
            )
            self.speed = 4


current_sprite_index = 0
background_displayed = 0

player_sprite = [
    pygame.image.load("Pink_Png_Quote_National_Love_Your_Pet_Day_Instagram_Post_3_removebg.png").convert_alpha(),
    pygame.image.load("Pink_Png_Quote_National_Love_Your_Pet_Day_Instagram_Post_4_fotor.png").convert_alpha(),
    pygame.image.load("Pink_Png_Quote_National_Love_Your_Pet_Day_Instagram_Post_5_fotor.png").convert_alpha(),
    pygame.image.load("Pink_Png_Quote_National_Love_Your_Pet_Day_Instagram_Post_6_fotor.png").convert_alpha(),
    pygame.image.load("Pink_Png_Quote_National_Love_Your_Pet_Day_Instagram_Post_7_fotor.png").convert_alpha()
]

player = Player(player_sprite)
enemy1 = Enemy1()
enemy2 = Enemy2()
enemy3 = Enemy3()
enemy4 = Enemy4()

player_group = pygame.sprite.Group()
player_group.add(player)

enemy_group = pygame.sprite.Group()
enemy_group.add(enemy1)
enemy_group.add(enemy2)
enemy_group.add(enemy3)
enemy_group.add(enemy4)

game_over_displayed = False

while True:

    current_sprite_index += 1
    if current_sprite_index == 4:
        current_sprite_index = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_UP]:
        background_speed = 4
        player.update()
    else:
        background_speed = 0

    if pressed_key[K_LEFT]:
        if player.rect.left >= 0:
            player.rect.x -= 10
            player.update()
    elif pressed_key[K_RIGHT]:
        if player.rect.right <= SCREEN_WIDTH:
            player.rect.x += 10
            player.update()

    background_y += background_speed
    if background_y > 0:
        background_y = 0
        if pressed_key[K_UP]:
            if player.rect.y < 0:
                player.rect.y = 0
            else:
                player.rect.y -= 5

    current_time = pygame.time.get_ticks()
    if current_time - last_player_change > player_change_time:
        current_sprite_index = (current_sprite_index + 1) % len(player_sprite)
        last_player_change = current_time

    clock.tick(60)

    screen.blit(background, (0, background_y))
    player_group.draw(screen)
    enemy_group.draw(screen)
    player_group.update()
    enemy_group.update()

    if pygame.sprite.spritecollide(player, enemy_group, False) and not game_over_displayed:
        pygame.mixer.Sound('crash_sound.mp3').play()
        time.sleep(0.5)
        screen.blit(game_over, (30, 250))
        game_over_displayed = True

    pygame.display.flip()