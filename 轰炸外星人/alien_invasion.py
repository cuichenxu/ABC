import sys

import pygame
from setting import Settings
from ship import Ship
import game_function as gf
def run_game():
    pygame.init()
    ai_setting = Settings()
    a = (ai_setting.screen_width, ai_setting.screen_height)
    screen = pygame.display.set_mode(a)
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:
        gf.check_event()
        gf.update_screen(ai_setting, screen, ship)
run_game()
