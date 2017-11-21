class Settings():
    """存储《外形人大战》的所以设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 240, 245)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的设置
        self.bullets_speed_factor = 1
        self.bullets_width = 3
        self.bullets_height = 15
        self.bullet_color = 220, 20, 60
        self.bullet_allowed = 5 # 当前屏幕最大子弹数

        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1
