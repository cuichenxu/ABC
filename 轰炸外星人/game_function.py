import sys

import pygame

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1

def update_screen(ai_setting, screen, ship):
    screen.fill(ai_setting, screen, ship)
    ship.blitme()

    pygame.display.flip()