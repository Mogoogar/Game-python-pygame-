class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует cтатические настройки игры"""
        # Параметры экрна
        self.screen_width = 1100
        self.screen_height = 500
        self.bg_color = (210, 190, 210)
        # настройки корабля
        self.ship_limit = 2
        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # настройки пришельцев
        self.fleet_drop_speed = 10  # Скорость опускания
        # темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.2  # скорость передвижения
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """увеличивает настройки скорости и стоимости пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)
