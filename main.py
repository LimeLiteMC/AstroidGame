import pygame
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import * 
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    number =1
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Containers
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    #Ojects
    field = AsteroidField()
    player1 = Player(x,y)

    while number > 0:
        log_state()
        for roid in asteroids:
            for bullet in shots:
                if roid.collides_with(bullet):
                    log_event("asteroid_shot")
                    roid.split()
                    bullet.kill()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if obj.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()





