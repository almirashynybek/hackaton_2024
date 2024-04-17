import pygame

def aktobe_game(screen, full_flask_sound):
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
        screen.fill("black")

        for i in range(1, 10):
            pygame.draw.rect(screen, 100*i + 50, 200, 'grey', 5)


