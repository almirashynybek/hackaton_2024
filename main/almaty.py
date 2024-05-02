import pygame
from pygame.locals import *
import sys
import random, time
import screens
import flags


pygame.init()

def almaty():
    
    info = pygame.display.Info()
    back_w = info.current_w
    back_h = info.current_h

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 800

    retry_image = pygame.transform.scale(pygame.image.load("images/buttons/retry.png"), (500, 120))
    continue_image = pygame.transform.scale(pygame.image.load("images/buttons/close.png"), (500, 120))
    menu_image = pygame.transform.scale(pygame.image.load("images/buttons/menu.png"), (500, 120))

    retry_image_rect = retry_image.get_rect()
    continue_image_rect = continue_image.get_rect()
    menu_image_rect = menu_image.get_rect()

    continue_image_rect.topleft = (back_w//2 - 250, 150)
    retry_image_rect.topleft = (back_w//2 - 250, 350)
    menu_image_rect.topleft = (back_w//2 - 250, 550)

    background_button = pygame.transform.scale(pygame.image.load("images/backgrounds/background_buttons.jpg"), (back_w, back_h))

    back = pygame.display.set_mode((back_w, back_h))
    screen = pygame.Surface((SCREEN_WIDTH, back_w))
    back.fill("black")
    background = pygame.image.load("images/background_main.png").convert()
    background_y = back_h - background.get_height()

    BLACK = (0, 0, 0)

    clock = pygame.time.Clock()
    speed_1 = 9
    background_speed = 0
    player_change_time = 100 
    player2_change_time = 100 
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
            self.image = pygame.image.load('images/obstacles/rock_alm.png')
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 800))
            self.speed = speed_1

        def move(self):
            self.rect.move_ip(0, self.speed)
            if (self.rect.top > SCREEN_HEIGHT):
                self.rect.top = 0
                self.speed += 0.5
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    class Standing(pygame.sprite.Sprite):
        def __init__(self, images, frame_duration=200):
            super().__init__()
            self.images = images
            self.frame_duration = frame_duration
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.image = self.images[self.current_frame]
            self.rect = self.image.get_rect()

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_duration:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.images)
                self.image = self.images[self.current_frame]

    class Win(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load('images/KBTU/part3.png'), (200,100))
            self.rect = self.image.get_rect()
            self.rect.centerx = SCREEN_WIDTH // 2 - 25
            self.rect.top = 0
            

    part_kbtu = Win()
    enemy1 = Enemy()
    win_pic = pygame.sprite.Group()
    stone1 = pygame.sprite.Group()
    stone1.add(enemy1)
    win_pic.add(part_kbtu)

    current_sprite_index = 0
    background_displayed = 0

    player_sprite = [
        pygame.image.load("images/person2/i1.png").convert_alpha(),
        pygame.image.load("images/person2/i2.png").convert_alpha(),
        pygame.image.load("images/person2/i3.png").convert_alpha(),
        pygame.image.load("images/person2/i4.png").convert_alpha(),
        pygame.image.load("images/person2/i5.png").convert_alpha()
    ]

    player_sprite2 = [
        pygame.image.load("images/person2/end1.png").convert_alpha(),
        pygame.image.load("images/person2/end2.png").convert_alpha()
    ]

    class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, images, frame_duration=200):
            super().__init__()
            self.images = images
            self.frame_duration = frame_duration
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.image = self.images[self.current_frame]
            self.rect = self.image.get_rect()

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_duration:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.images)
                self.image = self.images[self.current_frame]

        def start_animation(self):
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()

    player = Player(player_sprite)
    end_pos = AnimatedSprite(player_sprite2, frame_duration=200)
    player_end = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    player_group.add(player)
    player_end.add(end_pos)
    press_x, press_y = 0, 0
    pause = False
    settings = pygame.transform.scale(pygame.image.load("images/settings.png"), (50, 50))
    settings_rect = settings.get_rect()
    settings_rect.topleft = (back.get_rect().width - 70, 20)
    button_click = pygame.mixer.Sound('sounds/button.mp3')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                press_x, press_y = event.pos
                
        if not pause:
            back.blit(screen, (back_w//2 - SCREEN_WIDTH//2, 0))
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
            
            clock.tick(60)
            
            screen.blit(background, (0, background_y))
            player_group.draw(screen)

            if player.rect.y < 400:
                win_pic.draw(screen)

            if player.rect.y > 500:
                for entity in stone1:
                    screen.blit(entity.image, entity.rect)
                    entity.move()
            
            if player.rect.y == 0:
                
                screen.blit(player_sprite2[0], (0, background_y))
                end_pos.start_animation()
            
            if pygame.sprite.spritecollideany(player, win_pic):
                player_group.remove(player)
                screen.blit(player_sprite2[0], (0, background_y))
                end_pos.start_animation()
                for entity in player_end:
                    entity.update()
                    screen.blit(entity.image, entity.rect)
                    
                time.sleep(0.5)
                flags.victory1 = True
                screens.win3()

            if pygame.sprite.spritecollideany(player, stone1):
                pygame.mixer.Sound('images/sound.mp3').play()
                time.sleep(0.5)
                almaty()
            back.blit(settings, settings_rect)
            if settings_rect.collidepoint(press_x, press_y):
                pause = True
        else:
            back.blit(background_button, (0,0))
            back.blit(continue_image, continue_image_rect)
            back.blit(retry_image, retry_image_rect)
            back.blit(menu_image, menu_image_rect)
            
            if continue_image_rect.collidepoint(press_x, press_y):
                button_click.play()
                back.fill("black")
                pause = False
            elif retry_image_rect.collidepoint(press_x, press_y):
                button_click.play() 
                almaty()
            elif menu_image_rect.collidepoint(press_x, press_y):
                button_click.play()
                screens.map()

        pygame.display.update()
        pygame.display.flip()