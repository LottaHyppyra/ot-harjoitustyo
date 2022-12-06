import pygame
import random
from entities.map_list import *
from images.images import Images
from player import Player
from ghost import Ghost

class Game():

    def __init__(self) -> None:
        pygame.init()
        self.map = MAP1
        self.images = Images()
        self.player = Player(MAP1)
        self.ghost = Ghost(MAP1)
        self.pics = self.images.download_images()
        self.scale = self.pics[0].get_width()
        self.screen_height = self.scale * len(self.map)
        self.screen_width = self.scale * len(self.map[0])
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Aavelabyrintti")
        self.black_screen = pygame.Surface((self.screen_width, self.screen_height))
        self.black_screen.set_colorkey('RED')
        self.font = pygame.font.SysFont('arialblack', 30)
        self.counter = 0

    def main_menu(self):
        click = False
        while True:
            self.screen.fill((227, 227, 227))

            play_button_background = pygame.Rect(self.screen_width / 2 - 152, self.screen_height / 3 - 52, 304, 104)
            pygame.draw.rect(self.screen, ('BLACK'), play_button_background)

            play_button = pygame.Rect(self.screen_width / 2 - 150, self.screen_height / 3 - 50, 300, 100)
            pygame.draw.rect(self.screen, (130, 130, 130), play_button)
            play_text_img = self.font.render('PELAA', True, 'BLACK')
            self.screen.blit(play_text_img, (self.screen_width / 2 - play_text_img.get_width() / 2, self.screen_height / 3 - play_text_img.get_height() / 2))

            rules_button_background = pygame.Rect(self.screen_width / 2 - 152, self.screen_height / 2 - 52, 304, 104)
            pygame.draw.rect(self.screen, ('BLACK'), rules_button_background)

            help_button = pygame.Rect(self.screen_width / 2 - 150, self.screen_height / 2 - 50, 300, 100)
            pygame.draw.rect(self.screen, (130, 130, 130), help_button)
            help_text_img = self.font.render('SÄÄNNÖT', True, 'BLACK')
            self.screen.blit(help_text_img, (self.screen_width / 2 - help_text_img.get_width() / 2, self.screen_height / 2 - help_text_img.get_height() / 2))

            leaderboard_button_background = pygame.Rect(self.screen_width / 2 - 152, self.screen_height / 3 * 2- 52, 304, 104)
            pygame.draw.rect(self.screen, ('BLACK'), leaderboard_button_background)


            leaderboard_button = pygame.Rect(self.screen_width / 2 - 150, self.screen_height / 3 * 2 - 50, 300, 100)
            pygame.draw.rect(self.screen, (130, 130, 130), leaderboard_button)
            leaderboard_text_img = self.font.render('TULOSTAULU', True, 'BLACK')
            self.screen.blit(leaderboard_text_img, (self.screen_width / 2 - leaderboard_text_img.get_width() / 2, self.screen_height / 3 * 2 - leaderboard_text_img.get_height() / 2))

            if play_button.collidepoint(pygame.mouse.get_pos()):
                if click:
                    self.play()

            if help_button.collidepoint(pygame.mouse.get_pos()):
                if click:
                    self.help()

            if leaderboard_button.collidepoint(pygame.mouse.get_pos()):
                if click:
                    self.leader_board()

            click = False

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

                if event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()

    def help(self):
        click = False
        while True:
            self.screen.fill((227, 227, 227))
            help_image = self.pics[6]
            self.screen.blit(help_image, ((self.screen_width - help_image.get_width()) / 2, (self.screen_height - help_image.get_height()) / 2) )

            close_text_img = self.font.render('<<', True, 'BLACK')
            close_button = pygame.Rect(self.screen_width / 2 - close_text_img.get_width() / 2, 680, close_text_img.get_width(), close_text_img.get_height())
            pygame.draw.rect(self.screen, (227, 227, 227), close_button)
            self.screen.blit(close_text_img, (self.screen_width / 2 - close_text_img.get_width() / 2, 680))


            for event in pygame.event.get():

                if close_button.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        self.main_menu()

                click = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

                if event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()

    def leader_board(self):
        click = False
        while True:
            self.screen.fill((227, 227, 227))

            coming_soon_text_img = self.font.render('TULOSSA PIAN!', True, 'BLACK')
            self.screen.blit(coming_soon_text_img, (self.screen_width / 2 - coming_soon_text_img.get_width() / 2, self.screen_height / 2 - coming_soon_text_img.get_height() / 2))

            close_text_img = self.font.render('<<', True, 'BLACK')
            close_button = pygame.Rect(self.screen_width / 2 - close_text_img.get_width() / 2, 680, close_text_img.get_width(), close_text_img.get_height())
            pygame.draw.rect(self.screen, (227, 227, 227), close_button)
            self.screen.blit(close_text_img, (self.screen_width / 2 - close_text_img.get_width() / 2, 680))

            for event in pygame.event.get():

                if close_button.collidepoint(pygame.mouse.get_pos()):
                    if click:
                        self.main_menu()

                click = False

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

        floors = []
        for y_coord in range(len(self.map)):
            for x_coord in range(len(self.map[y_coord])):
                if self.map[y_coord][x_coord] == 0:
                    floors.append((x_coord, y_coord))

        square = floors[random.randrange(0, len(floors))]
        self.map[square[1]][square[0]] = 3

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

                        if moved:
                            self.counter += 1

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
                    object = self.map[y][x]
                    self.screen.blit(self.pics[object], (x * self.scale, y * self.scale))

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
            self.player_inventory()
            self.moves()
            pygame.display.flip()

    def player_inventory(self):
        smudges = self.player.count_smudges()
        smudges_text_img = self.font.render('Suitsukkeita: ' + str(smudges), True, 'WHITE')
        self.screen.blit(smudges_text_img, (60, 10))

    def moves(self):
        moves_text_img = self.font.render('Siirtoja: ' + str(self.counter), True, 'WHITE')
        self.screen.blit(moves_text_img, (self.screen_width - 60 - moves_text_img.get_width(), 10)) 

    def won(self):
            won_text_img = self.font.render('Voitit pelin ' + str(self.counter) + ' siirrolla!', True, 'WHITE')
            self.screen.blit(won_text_img, (self.screen_width - 60 - won_text_img.get_width(), self.screen_height - 50))

    def lost(self):
            lost_text_img = self.font.render('Hävisit pelin!', True, 'WHITE')
            self.screen.blit(lost_text_img, (self.screen_width - 60 - lost_text_img.get_width(), self.screen_height - 50))