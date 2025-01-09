import sys
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")                
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field1 = AsteroidField()
    
    fps_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for game_object in updatable:
            game_object.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player1):
                sys.exit("Game over!")
        
        screen.fill((0, 0, 0))

        for game_object in drawable:
            game_object.draw(screen)

        pygame.display.flip()

        dt = fps_clock.tick(60) / 1000 # pauses the game loop until 1/60 of a second has passed + converts return value of time passed in ms to senconds
 



if __name__ == "__main__":
    main()
