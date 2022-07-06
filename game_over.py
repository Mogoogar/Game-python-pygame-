import pygame


class GameOver:
    """класс вывески """
    def __init__(self, ai_settings, screen):
        """Инициализирует вывеску и задает её начальную позицию"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения вывески и получение прямоугольника.
        self.image = pygame.image.load('images/game_over.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # положение по центру
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует вывеску в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_over(self):
        """Размещает вывеску в центре нижней стороны."""
        self.center = self.screen_rect.centerx
