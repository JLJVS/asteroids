import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # start pygame
    print("Starting Asteroids!")
    pygame.init()

    # initalize the clock
    timer = pygame.time.Clock()
    dt = 0

    # start the screen
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    

    # create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # create containers
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    # create the player
    p = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # create the asteroid field
    asteroid_field = AsteroidField()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for to_draw in drawable:
            to_draw.draw(screen)

        for to_update in updateable:
            to_update.update(dt)

        for a in asteroids:
            if a.collision_detection(p):
                print("Game Over!")
                return

            for s in shots:
                if a.collision_detection(s):
                    s.kill()
                    a.split()
        
        pygame.display.flip()
        dt = timer.tick(60)/1000



if __name__ == "__main__":
    main()