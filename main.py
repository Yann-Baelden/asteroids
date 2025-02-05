# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get(): # close the window's game 
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # ou pygame.Surface.fill(screen,(0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()