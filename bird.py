import pygame as py

class Bird:
    """Class represents a bird"""
    def __init__(self, ai_game):
        """Intialize all bird attributes"""
        #Get Screen settings from main class
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.screen_width = ai_game.settings.screen_width
        self.screen_height = ai_game.settings.screen_height
        
        #Get settings from main class
        self.settings = ai_game.settings

        #Initalizing bird images and rects
        self.image = py.image.load("images/bluebird-midflap.bmp")
        self.rect = self.image.get_rect()

        self.x = self.rect.x

        self.rect.midleft = self.screen.get_rect().midleft  # Start at the left edge of the screen
        self.y = float(self.rect.y)

        #Bird Physiscs
        self.vel = 0

    def gravity_bird(self):
        """Creates atrifical gravity for bird"""
        #Birds Gravity
        self.vel += 0.5
        if self.vel > 8:
            self.vel = 8
        if self.rect.bottom < self.screen_height:
            self.rect.y += (self.vel)

    def jump_bird(self):
        """makes bird jump"""
        self.vel = -8
        
    def draw_bird(self):
        """Draw birds to screen"""
        self.screen.blit(self.image, self.rect)

    def center_bird(self):
        """Center the bird"""
        self.rect.midleft = self.screen.get_rect().midleft