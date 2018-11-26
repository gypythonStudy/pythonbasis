import sys
import pygame
from  pygame.sprite import  Group
from  settings import Settings
from ship import Ship
import  game_functions
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("武装飞船")
    # bg_color = (230,230,230)

    # ship = Ship(screen)
    ship = Ship(ai_settings,screen)

    bullets = Group()
    while True:

        screen.fill(ai_settings.bg_color)

        game_functions.check_events(ai_settings,screen,ship,bullets)
        # bullets.update()
        #
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        game_functions.update_bullets(bullets)

        print(len(bullets))

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        ship.update()
        game_functions.update_screen(ai_settings,screen,ship,bullets)
        # ship.blitme()
        #
        # pygame.display.flip() #让最近绘制的屏幕可见


run_game()

