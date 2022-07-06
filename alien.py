import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """класс пришельца """
    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения пришельца и получение прямоугольника.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется  в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)

    def blitme(self):
        """Рисует пришельца в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает пришельца влево или вправо"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
