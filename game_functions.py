import sys
from time import sleep

import pygame
# from pygame.sprite import Group
from bullet import Bullet
from aliens import Alien, Alien1, Alien2, Alien3, Alien4


def create_alien(settings, screen, aliens, alien_number, row_number):
    # CREATE ALIEN AND PLACE INTO ROW
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    # Spacing between each alien is equal to one alien width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(settings, screen, ship, aliens):
    # Create a full fleet of aliens
    alien = Alien1(settings=settings, screen=screen)
    # Alien is declared just to get its width
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # CREATE AN ALIEN AND PLACE IT IN THE ROW.
            create_alien(settings=settings, screen=screen,
                         aliens=aliens, alien_number=alien_number, row_number=row_number)


def change_fleet_direction(settings, aliens):
    # Drop the entire fleet and change the direction
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb):
    # Check if any aliens have reached the bottom of the screen.
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship was hit
            ship_hit(settings=settings, stats=stats, screen=screen,
                     ship=ship, aliens=aliens, bullets=bullets, sb=sb)
            break


def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    # Responds to bullet collisions
    # Remove any bullets that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # Destroy existing bullets, speed up the game and create new fleet.
        bullets.empty()
        settings.increase_speed()

        # Increasing the level
        stats.level += 1
        sb.prep_level()

        create_fleet(settings, screen, ship, aliens)


def check_high_score(stats, sb):
    # Check to see if there's a new high score.
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_fleet_edges(settings, aliens):
    # Respond appropriately if aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def check_keyup_events(event, ship):
    # Responds to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keydown_events(event, settings, screen, ship, bullets):
    # Responds to key presses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # MOVE SHIP TO RIGHT
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # MOVE SHIP TO LEFT
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)


def check_play_button(settings, screen, stats, sb, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y):
    # START NEW GAME WHEN PLAYER CLICKS ON PLAY BUTTON
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        settings.initialize_dynamic_settings()
        # WILL HIDE MOUSE CURSOR WHEN CLICKED AND PLAY BUTTON IS NOT VISIBLE ANYMORE
        pygame.mouse.set_visible(False)

        # Should also reset the stats of the game so that it can continue
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Should create a new fleet
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()


def check_events(settings, screen, stats, sb, play_button, ship, bullets, aliens):
    # RESPONDS TO KEY PRESSES & MOUSE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_axis, mouse_y_axis = pygame.mouse.get_pos()
            check_play_button(mouse_x=mouse_x_axis, mouse_y=mouse_y_axis,
                              play_button=play_button, stats=stats, screen=screen,
                              aliens=aliens, bullets=bullets, settings=settings,
                              ship=ship, sb=sb)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def get_number_aliens_x(settings, alien_width):
    """DETERMINE NUMBER OF ALIENS THAT FIT ON ROW"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
    # DETERMINE NUMBER OF ROWS OF ALIENS THAT FIT ON THE SCREEN
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    # EACH ROW IS HEIGHT OF 1 ALIEN (including empty)
    # SO THE AVAILABLE SPACE IS DIVIDED BY 2 ALIENS
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def fire_bullet(settings, screen, ship, bullets):
    # FIRE A BULLET IF LIMIT NOT REACHED
    # CREATES NEW BULLET ENTITY
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        pygame.mixer.music.load('sounds/shoot.wav')
        pygame.mixer.music.play()
        bullets.add(new_bullet)


def ship_hit(settings, stats, sb, screen, ship, aliens, bullets):
    # Responds to ship being hit by alien.
    # Decrements ship-left
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # UPDATE SCOREBOARD
        sb.prep_ships()
        # Empty list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        # PAUSE GAME FOR A BIT
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_screen(ai_settings, screen, ship, stats, aliens, bullets, play_button, sb):
    # UPDATES IMAGES ON SCREEN AND FLIP TO NEW SCREEN
    screen.fill(ai_settings.bg_color)

    # REDRAWS ALL BULLETS ON SCREEN
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Draw the score information
    sb.show_score()

    # DRAW PLAY BUTTON IF THE GAME IS INACTIVE.
    if not stats.game_active:
        play_button.draw_button()
    # Most recent screen is visible
    pygame.display.flip()
    # ship.blitme()
    # alien.blitme()


def update_aliens(settings, stats, screen, sb, ship, aliens, bullets):
    # UPDATE ALL POSITIONS OF ALIENS IN FLEET
    # CHECK IF AT EDGE THEN UPDATE
    check_fleet_edges(settings, aliens)
    aliens.update()

    # LOOK FOR ALIEN-SHIP COLLISIONS.
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("SHIP HIT")
        ship_hit(settings=settings, stats=stats, screen=screen,
                 ship=ship, aliens=aliens, bullets=bullets, sb=sb)

    # LOOK FOR ALIENS HITTING BOTTOM OF SCREEN
    check_aliens_bottom(settings=settings, stats=stats, screen=screen,
                        bullets=bullets, ship=ship, aliens=aliens, sb=sb)


def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    # UPDATE BULLET POSITION
    bullets.update()
    # GET RID OF OLD BULLETS NOT ON SCREEN
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(settings=settings, screen=screen, ship=ship,
                                  aliens=aliens, bullets=bullets, sb=sb, stats=stats)
    # print(len(bullets))
