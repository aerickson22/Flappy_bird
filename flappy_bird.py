import sys

import pygame
from pygame.sprite import Group
from time import sleep

from settings import Settings
from pipe import Pipe
from bird import Bird


class Flappy_Bird:
    """Represents a game of Flappy bird"""
    def __init__(self):
        """Intialize key elements in the game"""
        pygame.init()
        self.clock = pygame.time.Clock() 
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)     
        pygame.display.set_caption("Flappy Bird")

        #Creates Background Image
        self.bg_image = pygame.image.load("images/bg.bmp")
        self.bg_image_rect = self.bg_image.get_rect()

        #Create pipe Instances
        self.settings = Settings(self)

        #Create pipe Instances
        self.pipes = Group()
        self._create_pipes()

        #Create bird Instance
        self.bird = Bird(self)

    def run_game(self):
        """Runs the main logic of game"""
        while True: 
            self._update_screen()  
            self._update_pipe()
            self._bird_gravity()
            self._event_tracker()
            self._check_pipe_bird_collisions()
            self.clock.tick(60)

    def _event_tracker(self):
        """Keeps Track of key events"""
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        self._update_bird()

    def _check_pipe_bird_collisions(self):
        """Check for if the bird colides with pipes"""
        if pygame.sprite.spritecollideany(self.bird, self.pipes):
            sys.exit()
        elif self.bird.rect.y == 0:
            sys.exit()

    def _create_pipe(self, current_x):
        """creates new Instance of pipe"""
        new_pipe = Pipe(self)
        new_pipe.x = current_x
        new_pipe.pipe_top_rect.x = current_x
        new_pipe.pipe_bottom_rect.x = current_x
        self.pipes.add(new_pipe)

    def _create_pipes(self):
        """Creates a row of pipes"""       
        #Creates a row of pipes top and bottom
        pipe = Pipe(self)
        pipe_width = pipe.pipe_bottom_rect.width
        current_x = pipe_width
        while current_x < self.settings.screen_width:
            self._create_pipe(current_x)
            current_x += 4 * pipe_width

    def _draw_pipes(self): 
        """draws pipes to screen and check pipe conditions"""
        for pipe in self.pipes.sprites():
            pipe.draw_pipe_set()
            if pipe.pipe_bottom_rect.x < 0 and pipe.pipe_top_rect.x < 0:
                self.pipes.remove(pipe)
                self._create_pipe(self.settings.screen_width + pipe.pipe_bottom_width)

    def _bird_gravity(self):
        """Updates birds positon on y axis"""
        self.bird.gravity_bird()
 
    def _update_bird(self):
        """Allows player to jump the bird"""
        self.bird.jump_bird()

    def _update_pipe(self):
        """Moves pipes to the left"""
        self.pipes.update()
        
    def _update_screen(self, game_active = False):
        """Updates the Screen of game"""
        self.screen.blit(self.bg_image, self.bg_image_rect)
        self._draw_pipes()
        self.bird.draw_bird()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = Flappy_Bird()
    ai.run_game()