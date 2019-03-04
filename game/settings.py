class Settings:
    """class to store all settings for Alien invasion"""

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (0, 0, 230)

        # ship settings
        self.ship_speed_factor = 1.5

        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

