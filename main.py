# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Creates groups for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Creates asteroid & field group membership & initializes
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Adds player group membership class variable & initializes player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Adds shot group membership class variable & initializes shots
    Shot.containers = (updatable, drawable, shots)

    while True:
        # Makes the exit button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draws and refreshes the objects/screen
        updatable.update(dt)

        for aster in asteroids:
            if aster.collisions(player) == True:
                print("Game Over!")
                return
        
            for bullet in shots:
                if aster.collisions(bullet) == True:
                    bullet.kill()
                    aster.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limit the framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()