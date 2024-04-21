import pygame
from pygame.locals import *
import sys
import random, time

pygame.init()

SCREEN_WIDTH = 600

SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("17.png").convert()

background_y = SCREEN_HEIGHT - background.get_height()

BLACK = (0, 0, 0)

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('snowball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 800))
        self.speed = 15

    def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

enemy1 = Enemy()
stone1 = pygame.sprite.Group()
stone1.add(enemy1)

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

player_group = pygame.sprite.Group()
player_group.add(player)


while True:
    
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
        background_speed = 3
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
    for entity in stone1:
            screen.blit(entity.image, entity.rect)
            entity.move()
    if pygame.sprite.spritecollideany(player, stone1):
        
        pygame.mixer.Sound('crash_sound.mp3').play()
        time.sleep(0.5)
        pygame.quit()
        
    
    pygame.display.update()
    
    
    pygame.display.flip()