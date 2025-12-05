import circleshape
import constants
import pygame

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, center):
        return pygame.draw.circle(screen, "white", center, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 

