import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


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

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(settings)

    # 创建计分板
    sb = ScoreBoard(settings, screen, stats)

    # 创建Play按钮
    play_button = Button(settings, screen, "Play")

    # 开始游戏主循环
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()
