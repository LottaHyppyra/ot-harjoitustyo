from entities.map_list import *
from images.images import Images
from player import Player
from ghost import Ghost
import pygame

def main():
    pygame.init()
    map = map1
    images = Images()
    player = Player(map1)
    ghost = Ghost(map1)
    pics = images.download_images()
    scale = pics[0].get_width()
    screen_height = scale * len(map)
    screen_width = scale * len(map[0])
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Aavelabyrintti")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move(1, 0)
                if event.key == pygame.K_LEFT:
                    player.move(-1, 0)
                if event.key == pygame.K_UP:
                    player.move(0, -1)
                if event.key == pygame.K_DOWN:
                    player.move(0, 1)

                ghost.move()
                if player.get_coords() == None:
                    exit()

            if event.type == pygame.QUIT:
                exit()

        screen.fill((0,0,0))
        for y in range(len(map)):
            for x in range(len(map[0])):
                box = map[y][x]
                screen.blit(pics[box], (x * scale, y * scale))

        pygame.display.flip()

if __name__ == "__main__":
    main()