import game_functions as gf
import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # sets size of display window
    pygame.display.set_caption('ALIEN INVASION')

    # make a play button
    play_button = Button(ai_settings, screen, "Play")


    # create an instance to store game statistics and a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in
    bullets = Group()
    # make an alien
    aliens = Group()
    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # main loop of the game with events, manages screen updates. an event is an action that the user peforms on the game
    while True:  # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
           ship.update()
           gf.update_bullets(ai_settings, screen, stats, sb , ship, aliens, bullets)
           gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
