import circleshape
import constants
import pygame
from logger import log_event
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__radius = radius
        self.__x = x
        self.__y = y
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 

    def split(self):
        self.kill()
        if self.__radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            roid1_velosity = self.velocity.rotate(angle)
            roid2_velosity = self.velocity.rotate(-angle)
            new_radius = self.__radius - constants.ASTEROID_MIN_RADIUS
            roid1 = Asteroid(self.position[0], self.position[1], new_radius)
            roid2 = Asteroid(self.position[0], self.position[1], new_radius)
            roid1.velocity = roid1_velosity * 1.2
            roid2.velocity = roid2_velosity * 1.2
