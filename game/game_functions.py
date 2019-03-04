import sys
import pygame


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
            if event.key == pygame.K_LEFT:
                ship.rect.centerx -= 1


def update_screen(settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    screen.fill(settings.bg_color)
    ship.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()
