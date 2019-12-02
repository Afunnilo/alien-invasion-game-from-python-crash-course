import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """initialise the ship and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start new ship at the bottom centre of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ships center
        self.center = float(self.rect.centerx)

        self.ship_speed_factor = 1.5

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ships position based on the movement flag"""
        # update the ships center value, not the rect
        if self.moving_right:
            self.center += self.ship_speed_factor
        if self.moving_left:
            self.center -= self.ship_speed_factor

        if self.center <= self.screen_rect.left:
            self.center = self.screen_rect.right
        elif self.center >= self.screen_rect.right:
            self.center = self.screen_rect.left

        #if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += self.ai_settings.ship_speed_factor
       # if self.moving_left and self.rect.left > 0:
           # self.rect.centerx -= self.ai_settings.ship_speed_factor
        # update rect object from self.center
        self.rect.centerx = (self.center)
    def center_ship(self):
        """center the shi on te screen"""
        self.center = self.screen_rect.centerx
    def blitme(self):
        """draw the ship at current location"""
        self.screen.blit(self.image, self.rect)
