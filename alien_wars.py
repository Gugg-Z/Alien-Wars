import sys
import pygame
from settings import Settings


def run_game():
    # 初始化pygame 设置和屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Wars")

    # 开始游戏主循环
    while True:

        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环是都重新绘制屏幕
        screen.fill(settings.bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
