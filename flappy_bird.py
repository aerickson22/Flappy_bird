import sys

import pygame
from pygame.sprite import Group
from time import sleep
  
from settings import Settings
from pipe import Pipe
from bird import Bird
from buttons import Button
from scoreboard import Scoreboard
from game_stats import GameStats

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

        #Game active flap set to false
        self.game_active = False
        self.play_button = Button(self, "Play")

        #Create an instance to store gaem statistics
        # and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

    def run_game(self):
        """Runs the main logic of game"""
        while True:
            self._event_tracker()
            if self.game_active:
                self._update_pipe()
                self._bird_gravity()
                self._check_pipe_bird_collisions()
                self._check_difficult()
            self._update_screen()  
            self.clock.tick(60)

    def _event_tracker(self):
        """Keeps Track of key events"""
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        self._update_bird()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_pipe_bird_collisions(self):
        """Check for if the bird colides with pipes"""
        pipe_scored = False
        for pipe in self.pipes.sprites():
            if pipe.pipe_top_rect.colliderect(self.bird.rect) or pipe.pipe_bottom_rect.colliderect(self.bird.rect):
                self.game_active = False
                pygame.mouse.set_visible(True)
            if pipe.pipe_bottom_rect.x < self.bird.x and not pipe_scored:
                self.stats.score += 1
                self.sb.prep_score()
                pipe_scored = True
        if self.bird.rect.y >= self.settings.screen_height - 50:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the plater click Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True
            self.stats.reset_stats()
            self.sb.prep_score()
            self.pipes.empty()
            self.bird.draw_bird()
            self.bird.center_bird()
            self._create_pipes()
            #Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_pipe_pos(self):
        """Check pipe postion and does the certain conditon"""
        for pipe in self.pipes.sprites():
            if pipe.pipe_bottom_rect.x == self.settings.screen_width/4 and pipe.pipe_top_rect.x == self.settings.screen_width/4 :
                self._create_pipe(self.settings.screen_width + (4 * pipe.pipe_bottom_rect.width))
            elif pipe.pipe_bottom_rect.x < 0 and pipe.pipe_top_rect.x < 0:
                self.pipes.remove(pipe)

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
        current_x = self.settings.screen_width/4
        while current_x < self.settings.screen_width:
            self._create_pipe(current_x)
            current_x += 4 * pipe_width
        current_x = pipe_width

    def _draw_pipes(self):
        """draws pipes to screen and check pipe conditions"""
        for pipe in self.pipes.sprites():
            pipe.draw_pipe_set()

    def _bird_gravity(self):
        """Creates birds articial gravity"""
        self.bird.gravity_bird()
 
    def _update_bird(self):
        """Allows player to jump the bird"""
        if self.bird.rect.y >= 0:
            self.bird.jump_bird()

    def _update_pipe(self):
        """Moves pipes to the left"""
        self._check_pipe_pos()
        self.pipes.update()

    def _check_difficult(self):
        if self.stats.score > 100:
            self.settings.pipe_moving_speed *= 4
        elif self.stats.score > 50:
            self.settings.pipe_moving_speed *= 3.5
        elif self.stats.score > 50:
            self.settings.pipe_moving_speed *= 3
        elif self.stats.score > 30:
            self.settings.pipe_moving_speed *= 2.5
        elif self.stats.score > 20:
            self.settings.pipe_moving_speed *= 2
        elif self.stats.score > 10:
            self.settings.pipe_moving_speed *= 1.5

    def _update_screen(self):
        """Updates the Screen of game"""
        self.screen.blit(self.bg_image, self.bg_image_rect)
        self.bird.draw_bird()
        self._draw_pipes()
        self.sb.show_score()
        #Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = Flappy_Bird()
    ai.run_game()