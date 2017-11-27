import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹管理类"""

    def __init__(self, settings, screen, ship):
        # Python 2.7语法
        # super(Bullet, self).__init__()
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, settings.bullets_width,
                                settings.bullets_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示子弹的位置
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullets_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
