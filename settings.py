class Settings:
    # Class to store setting
    def __init__(self):
        # Initialize game's static settings
        self.screen_width = 1200
        # self.dims = 1200, 800
        self.screen_height = 800
        self.bg_color = (15, 15, 15)
        # SHIP SETTINGS
        self.ship_limit = 3

        # BULLETS
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 160, 160, 160
        self.bullets_allowed = 1

        # ALIEN SETTINGS
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # self.drop_scale = 1.02
        # How quickly the game speeds up
        self.score_scale = 1.5
        # Here to have a check mark
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50
        self.fleet_direction = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # INITIALIZE SETTINGS THAT CHANGE THROUGHOUT THE GAME.
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Scoring
        self.alien_points = 50

        # fleet direction of 1 represents right, -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        # Increase speed settings & alien point values.
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    # def dropdown_speed(self):
        # Increases the speed per level
