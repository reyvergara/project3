import pygame
from settings import Settings
from start_screen import Start
from timer import Timer
import game_functions as gf


from pygame.sprite import Group
from ship import Ship
from gamestats import GameStats
from scoreboard import Scoreboard


def run_game():
    # initialize pygame, settings and object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    pygame.display.set_caption('Alien Invasion')

    # MAKE PLAY BUTTON
    start_screen = Start  # settings=settings,
    # Create instance to store game statistics & create a scoreboard.
    stats = GameStats(settings)
    sb = Scoreboard(settings=settings, screen=screen, stats=stats)
    # Makes a ship
    ship = Ship(settings, screen)
    """MAKE A GROUP TO STORE BULLETS IN"""
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)
    # Main game loop
    while True:
        gf.check_events(ship=ship, settings=settings, bullets=bullets,
                        screen=screen, stats=stats,
                        aliens=aliens, sb=sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings=settings, screen=screen, ship=ship,
                              aliens=aliens, bullets=bullets, sb=sb, stats=stats)
            gf.update_aliens(settings=settings, stats=stats, screen=screen,
                             ship=ship, aliens=aliens, bullets=bullets, sb=sb)

        gf.update_screen(ai_settings=settings, screen=screen, ship=ship,
                         aliens=aliens, bullets=bullets, play_button=play_button,
                         stats=stats, sb=sb)


run_game()


