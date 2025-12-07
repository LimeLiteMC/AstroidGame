import circleshape
import constants
import pygame
import shot

class Player(circleshape.CircleShape):
    def __init__(self,x,y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0 
        self.shot_cool_down = 0
        self.__x = x
        self.__y = y
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH) 
    
    def rotate(self, dt):
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)
        return self.rotation

    def update(self, dt):
        if self.shot_cool_down > 0:
            self.shot_cool_down -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            return self.rotate(-dt)

        if keys[pygame.K_d]:
            return self.rotate(dt)
        
        if keys[pygame.K_w]:
            return self.move(dt)

        if keys[pygame.K_s]:
            return self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cool_down > 0:
            return
        else:
            self.shot_cool_down = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
        bullet = shot.Shot(self.position[0], self.position[1], constants.SHOT_RADIUS)        
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
        

