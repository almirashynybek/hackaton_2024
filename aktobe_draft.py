import pygame
import sys
pygame.init()

def aktobe_game(screen):
    flasks = [['pink', 'darkblue', 'lightgreen', 'darkblue'],
              ['yellow', 'grey', 'pink', 'red'],
              ['darkblue', 'lightblue', 'lightblue', 'lightgreen'],
              ['pink', 'yellow', 'yellow', 'lightgreen'],
              ['grey', 'grey', 'lightgreen', 'red'],
              ['darkblue', 'red', 'lightblue', 'lightblue'],
              ['red', 'pink', 'yellow', 'grey'],
              [], []]

    mouse_x, mouse_y = 0, 0
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
        screen.fill("black")

        for i in range(1, 10):
            pygame.draw.rect(screen, "white", (100*i + 50, 200, 70, 270), 5)
        


info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
test_tube = pygame.transform.scale(pygame.image.load("images/test_tube.png"), (120, 450))
test_tube_rect = test_tube.get_rect()


flasks = [['pink', 'darkblue', 'lightgreen', 'darkblue'],
              ['yellow', 'grey', 'pink', 'red'],
              ['darkblue', 'lightblue', 'lightblue', 'lightgreen'],
              ['pink', 'yellow', 'yellow', 'lightgreen'],
              ['grey', 'grey', 'lightgreen', 'red'],
              ['darkblue', 'red', 'lightblue', 'lightblue'],
              ['red', 'pink', 'yellow', 'grey'],
              [], []]

ball_radius = 30
ball_rect = int(ball_radius * 2 ** 0.5)
#pink_ball = pygame.Rect()

mouse_x, mouse_y = 0, 0
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
    screen.fill("grey")

    for i in range(1, 6):
        screen.blit(test_tube, (220*i + 50, screen_height // 2 - 225))
    
    
        
    pygame.display.flip()

print(screen_width, screen_height)


