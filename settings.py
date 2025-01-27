import pygame as py

class Settings:
    """A class to represent settings in a game"""
    def __init__(self, ai_game):
        #Screen Settings
        self.screen = ai_game.screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.bg_color = (6, 255, 239)

        #Pipe Settings
        self.gap_size = 150
        self.pipe_moving_speed = 1.5