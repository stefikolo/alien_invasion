import pygame
from game.settings import Settings
from game.ship import Ship
import game.game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion 3000")
    ship = Ship(screen, settings)
    bullets = Group()
    # Start the main loop for the game.
    while True:
        gf.check_events(ship, settings, screen, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
