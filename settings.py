class Settings():
    """存储《外形人大战》的所以设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # 飞船的设置
        self.ship_speed_factor = 1.5
