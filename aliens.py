from abc import ABC

import pygame
from pygame.sprite import Sprite
from timer import Timer


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, settings, screen):
        # Initialize the alien and set its starting position.
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = settings

        # Load alien image and set its hitbox
        self.images = []
        self.rect = pygame.Rect(60, 60)
        # self.rect = self.images[0].get_rect()
        # Start each new alien near top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)
        self.points = 1

        self.explode_f = []

    def blitme(self):
        # Draw the alien at its current location.
        self.screen.blit(self.images, self.rect)

    def check_edges(self):
        # RETURN TRUE IF ALIENS ARE AT THE EDGE OF SCREEN
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

    def explode(self):
        raise NotImplementedError

    def points(self):
        raise NotImplementedError

    def update(self):
        # MOVE ALIEN TO RIGHT
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


class Alien1(Alien):
    def __init__(self, screen, settings):
        super().__init__(screen=screen, settings=settings)
        self.images.append(pygame.image.load('images/alien1_f1'))
        self.images.append(pygame.image.load('images/alien1_f2'))

    def points(self):
        self.points = 30

    def explode(self):
        self.explode_f.append()


class Alien2(Alien):
    def __init__(self, screen, settings):
        super().__init__(screen=screen, settings=settings)

    def points(self):
        self.points = 25

    def explode(self):
        x = 1


class Alien3(Alien):
    def __init__(self, screen, settings):
        super().__init__(screen=screen, settings=settings)

    def points(self):
        self.points = 20

    def explode(self):
        x = 1


class Alien4(Alien):
    def __init__(self, screen, settings):
        super().__init__(screen=screen, settings=settings)
        self.image = pygame.image.load

    def points(self):
        self.points = 10

    def explode(self):
        x = 1
