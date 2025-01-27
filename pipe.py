import pygame as py
from pygame.sprite import Sprite
from random import randint

class Pipe(Sprite):
    """A Class to represent a pipe"""
    def __init__(self, ai_game):
        """Intializes attributes of a Pipe"""
        super().__init__()
        #Get Screen settings from main class
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.screen_width = ai_game.settings.screen_width
        self.screen_height = ai_game.settings.screen_height
        
        #Get settings from main class
        self.settings = ai_game.settings

        #Get Top Pipe settings
        self.image_top = py.image.load("images/pipe-green-flip.bmp")
        self.pipe_top_width = self.image_top.get_rect().width
        self.pipe_top_height = self.screen_height
        self.image_top = py.transform.scale(self.image_top, (self.pipe_top_width, self.pipe_top_height))
        self.pipe_top_rect = self.image_top.get_rect()


        #Get Bottom Pipe settings
        self.image_bottom = py.image.load("images/pipe-green.bmp")
        self.pipe_bottom_width = self.image_bottom.get_rect().width
        self.pipe_bottom_height = self.screen_height
        self.image_bottom = py.transform.scale(self.image_bottom, (self.pipe_bottom_width, self.pipe_bottom_height))
        self.pipe_bottom_rect = self.image_bottom.get_rect()

        #create randomn height for pipes
        self._create_height()

    def _create_height(self):
        """Create random heights for the pipe set"""
        gap_y = randint(100, self.screen_height - self.settings.gap_size - 100)

        self.pipe_bottom_rect.y = gap_y + self.settings.gap_size 
        self.pipe_top_rect.y = gap_y - self.pipe_top_height  
        
    def draw_pipe_set(self):
        """Draws pipe set to the screen"""
        self.screen.blit(self.image_bottom, self.pipe_bottom_rect)
        self.screen.blit(self.image_top, self.pipe_top_rect)

    def update(self):
        """Moves pipe to the left"""
        self.x -= self.settings.pipe_moving_speed
        self.pipe_top_rect.x = self.x
        self.pipe_bottom_rect.x = self.x



