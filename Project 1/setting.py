import pygame

class Settings():
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1080
        self.screen_height = 900
        self.bg_color = pygame.color.Color('#000000')
        self.ship_speed_factor = 5