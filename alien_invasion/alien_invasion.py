import sys
import pygame
from  settings import Settings
from ship import Ship
import  game_functions
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("武装飞船")
    # bg_color = (230,230,230)

    ship = Ship(screen)
    while True:

        screen.fill(ai_settings.bg_color)

        game_functions.check_events()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        ship.blitme()

        pygame.display.flip() #让最近绘制的屏幕可见


run_game()

