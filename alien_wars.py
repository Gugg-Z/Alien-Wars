import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化pygame 设置和屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Wars")

    # 创建一艘飞船
    ship = Ship(settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建外星人群
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(settings, screen, ship, aliens, bullets)


run_game()
