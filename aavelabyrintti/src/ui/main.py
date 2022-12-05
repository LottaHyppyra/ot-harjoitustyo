import pygame
from entities.map_list import *
from images.images import Images
from player import Player
from ghost import Ghost

class Game():

    def __init__(self) -> None:
        pygame.init()
        self.map = map1
        self.images = Images()
        self.player = Player(map1)
        self.ghost = Ghost(map1)
        self.pics = self.images.download_images()
        self.scale = self.pics[0].get_width()
        self.screen_height = self.scale * len(self.map)
        self.screen_width = self.scale * len(self.map[0])
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Aavelabyrintti")
        self.black_screen = pygame.Surface((self.screen_width, self.screen_height))
        self.black_screen.set_colorkey('RED')
        self.font = pygame.font.SysFont(None, 50)
        
    def main_menu(self):
        click = False
        while True:
            self.screen.fill((255, 255, 255))

            play_button = pygame.Rect(self.screen_width / 2 - 150, self.screen_height / 3 - 50, 300, 100)
            pygame.draw.rect(self.screen, (0, 0, 0), play_button)
            play_text_img = self.font.render('PELAA', True, 'GREEN')
            self.screen.blit(play_text_img, (self.screen_width / 2 - play_text_img.get_width() / 2, self.screen_height / 3 - 15))

            rules_button = pygame.Rect(self.screen_width / 2 - 150, self.screen_height / 2 - 50, 300, 100)
            pygame.draw.rect(self.screen, (0, 0, 0), rules_button)
            rules_text_img = self.font.render('SÄÄNNÖT', True, 'GREEN')
            self.screen.blit(rules_text_img, (self.screen_width / 2 - rules_text_img.get_width() / 2, self.screen_height / 2 - 15))

            leaderboard_button = pygame.Rect(self.screen_width / 2 - 150, self.screen_height / 3 * 2 - 50, 300, 100)
            pygame.draw.rect(self.screen, (0, 0, 0), leaderboard_button)
            leaderboard_text_img = self.font.render('TULOSTAULU', True, 'GREEN')
            self.screen.blit(leaderboard_text_img, (self.screen_width / 2 - leaderboard_text_img.get_width() / 2, self.screen_height / 3 * 2 - 15))

            if play_button.collidepoint(pygame.mouse.get_pos()):
                if click:
                    self.play()

            click = False

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

                if event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()

    def play(self):
        not_smudged = True
        counter = 0
        is_won = False
        while True:

            for event in pygame.event.get():
                if self.player.get_coords() is not None:
                    if event.type == pygame.KEYDOWN:
                        moved = True
                        if event.key == pygame.K_1:
                            if self.player.use_smudge():
                                not_smudged = False
                        if event.key == pygame.K_RIGHT:
                            is_won = self.player.move(1, 0)
                        elif event.key == pygame.K_LEFT:
                            is_won = self.player.move(-1, 0)
                        elif event.key == pygame.K_UP:
                            is_won = self.player.move(0, -1)
                        elif event.key == pygame.K_DOWN:
                            is_won = self.player.move(0, 1)
                        else:
                            moved = False

                        if not_smudged and moved and self.player.get_coords() is not None:
                            self.ghost.move(self.player.get_coords())

                        if not_smudged is False:
                            counter += 1

                        if counter == 4:
                            not_smudged = True
                            counter = 0

                if event.type == pygame.QUIT:
                    exit()

            self.screen.fill((0, 0, 0))
            for y in range(len(self.map)):
                for x in range(len(self.map[0])):
                    box = self.map[y][x]
                    self.screen.blit(self.pics[box], (x * self.scale, y * self.scale))

            if self.player.get_coords() is not None:
                pygame.Surface.fill(self.black_screen, (0, 0, 0))
                pygame.draw.circle(
                    self.black_screen,
                    ('RED'),
                    ((self.player.get_coords()[0] * self.pics[2].get_width() + self.pics[2].get_width() / 2),
                    (self.player.get_coords()[1] * self.pics[2].get_height() + self.pics[2].get_height() / 2)),
                    self.pics[0].get_width() * 2.5
                    )

            else:
                pygame.Surface.fill(self.black_screen, ('RED'))
                if is_won:
                    self.won()
                else:
                    self.lost()

            self.screen.blit(self.black_screen, (0, 0))
            pygame.display.flip()

    def won(self):
            won_text_img = self.font.render('VOITIT PELIN', True, 'GREEN')
            self.screen.blit(won_text_img, (self.screen_width / 2 - won_text_img.get_width() / 2, self.screen_height - 50))

    def lost(self):
            lost_text_img = self.font.render('HÄVISIT PELIN', True, 'GREEN')
            self.screen.blit(lost_text_img, (self.screen_width / 2 - lost_text_img.get_width() / 2, self.screen_height - 50))