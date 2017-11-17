import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame 设置和屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Wars")

    # 创建一艘飞船
    ship = Ship(settings, screen)

    # 开始游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)


run_game()
