import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from game_over import GameOver
import game_functions as gf
from button import Button


def run_game():
    """Инициализирует игру и создаёт объект экрана"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # создание кнопки play
    play_button = Button(ai_settings, screen, "Play")
    # Создание корабля, группы пуль, группы пришельцев
    ship = Ship(ai_settings, screen)
    over = GameOver(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        # else:
            # gf.update_screen2(ai_settings, screen, stats, ship, aliens, bullets, over)


run_game()
