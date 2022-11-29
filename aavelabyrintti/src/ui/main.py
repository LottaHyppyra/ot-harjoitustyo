import pygame
from entities.map_list import *
from images.images import Images
from player import Player
from ghost import Ghost

class Game():

    def __init__(self) -> None:
        pass

    def play(self):
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
        black_screen = pygame.Surface((screen_width, screen_height))
        black_screen.set_colorkey('RED')

        while True:

            for event in pygame.event.get():
                if player.get_coords() is not None:
                    if event.type == pygame.KEYDOWN:
                        moved = True
                        if event.key == pygame.K_RIGHT:
                            player.move(1, 0)
                        elif event.key == pygame.K_LEFT:
                            player.move(-1, 0)
                        elif event.key == pygame.K_UP:
                            player.move(0, -1)
                        elif event.key == pygame.K_DOWN:
                            player.move(0, 1)
                        else:
                            moved = False

                        if moved and player.get_coords() is not None:
                            ghost.move(player.get_coords())

                if event.type == pygame.QUIT:
                    exit()

            screen.fill((0, 0, 0))
            for y in range(len(map)):
                for x in range(len(map[0])):
                    box = map[y][x]
                    screen.blit(pics[box], (x * scale, y * scale))

            if player.get_coords() is not None:
                pygame.Surface.fill(black_screen, (0, 0, 0))
                pygame.draw.circle(
                    black_screen,
                    ('RED'),
                    ((player.get_coords()[0] * pics[2].get_width() + pics[2].get_width() / 2),
                    (player.get_coords()[1] * pics[2].get_height() + pics[2].get_height() / 2)),
                    pics[0].get_width() * 2.5
                    )

            else:
                pygame.Surface.fill(black_screen, ('RED'))

            screen.blit(black_screen, (0, 0))
            pygame.display.flip()