class GameStats:
    # Track statistics for Alien Invasion

    def __init__(self, ai_settings):
        # Initialize statistics.
        self.settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an active state
        self.game_active = False
        # High score should never be reset
        self.high_score = 0

        # Initialize statistics that can change during the game.
        """Also in the reset_stats class, but all these were made outside
        of class initialization, so they are here too"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
