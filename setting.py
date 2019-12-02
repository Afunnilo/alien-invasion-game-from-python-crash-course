class Settings():
    """a class to store settings for aien invasion"""

    def __init__(self):
        """initialise the games static settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_colour = (230, 230, 230)

        # ship settings

        self.ship_limit = 3
        # bullet settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings

        self.fleet_drop_speed = 10


        # how quikly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change through out the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # scoring
        self.alien_points = 50


        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print( self.alien_points )





