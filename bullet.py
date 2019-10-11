import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # CLASS TO MANAGE THE BULLETS FIRED FROM SHIP

    def __init__(self, ai_settings, screen, ship):
        # CREATE BULLET AT CURRENT POSITION
        super(Bullet, self).__init__()
        """" Or do super().__init__()"""
        self.screen = screen

        # CREATE BULLET RECT @ (0, 0) AND THEN SET TO CORRECT PLACE
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # STORE BULLET'S POSITION
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # MOVE BULLETS UP THE SCREEN
        # UPDATE DECIMAL PLACE OF BULLET
        self.y -= self.speed_factor
        # UPDATE RECT POSITION
        self.rect.y = self.y

    def draw_bullet(self):
        """DRAW BULLET ON SCREEN"""
        pygame.draw.rect(self.screen, self.color, self.rect)