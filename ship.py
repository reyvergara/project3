import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        # Start the ship up and set start position
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship_.png')
        # Got sprite from https://www.spriters-resource.com/neo_geo_ngcd/ms3/sheet/11346/
        # Credit to Gussprint for ripping the sprite from the game
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Ship starts at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # STORES DECIMAL VALUE FOR SHIP'S CENTER
        self.center = float(self.rect.centerx)

        # MOVEMENT FLAG
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # UPDATE SHIP POSITION BASED ON MOVEMENT FLAG
        # UPDATE SHIP'S CENTER VALUE, NOT THE RECTANGLE
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            # self.rect.centerx -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        # UPDATE THE RECTANGLE OBJECT FROM SELF.CENTER

    def blitme(self):
        # Draw ship at current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # Center the ship on the screen
        self.center = self.screen_rect.centerx
