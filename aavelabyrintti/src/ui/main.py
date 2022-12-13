import pygame
import pygame_textinput
import random
from repositories.results_repository import get_sorted_results, add_result_to_database
from entities.map_list import *
from images.images import Images
from player import Player
from ghost import Ghost

class Game():
    """Luokka, joka huolehtii pelin käyttöliittymästä.
    
    """

    def __init__(self):
        """Luokan konstruktori, joka luo käyttöliittymän.
        
        """

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
        self.name = ""

    def main_menu(self):
        """Piirtää pelin aloitusvalikon, jossa painikkeet "pelaa", "ohjeet" ja "tulostaulu".

        Painikkeita klikkaamalla siirtyy pois aloitusvalikosta.
        
        """

        click = False

        while True:
            self.screen.fill((227, 227, 227))

            play_button = self.draw_menu_button('PELAA', 3)
            help_button = self.draw_menu_button('OHJEET', 2)
            leaderboard_button = self.draw_menu_button('TULOSTAULU', 3/2)

            if play_button.collidepoint(pygame.mouse.get_pos()):
                if click:
                    self.ask_name()

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
        """Piirtää pelin ohjesivun.
        
        Sivulla on painike, jota klikkaamalla pääsee takaisin aloitusvalikkoon.

        """

        click = False
        while True:
            self.screen.fill((227, 227, 227))
            help_image = self.pics[6]
            self.screen.blit(help_image, ((self.screen_width - help_image.get_width()) / 2, (self.screen_height - help_image.get_height()) / 2) )

            close_button = self.draw_close_button()

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
        """Piirtää pelin tulostaulu -sivun.
        
        Tulostaa enintään TOP 3 tulosta. Sivulla on painike, jota klikkaamalla siirtyy takaisin aloitusvalikkoon.
        
        """


        click = False
        results = get_sorted_results()

        while True:
            self.screen.fill((227, 227, 227))

            leaders_text_img = self.font.render('- TOP 3 -', True, 'BLACK')
            self.screen.blit(leaders_text_img, (self.screen_width / 2 - leaders_text_img.get_width() / 2, 200))

            if len(results) >= 1:
                text = f"1. {results[0][0]} - {results[0][1]} siirtoa"
                result_text_img = self.font.render(text, True, 'BLACK')
                self.screen.blit(result_text_img, (self.screen_width / 2 - result_text_img.get_width() / 2, 275))

            if len(results) >= 2:
                text = f"2. {results[1][0]} - {results[1][1]} siirtoa"
                result_text_img = self.font.render(text, True, 'BLACK')
                self.screen.blit(result_text_img, (self.screen_width / 2 - result_text_img.get_width() / 2, 350))

            if len(results) >= 3:
                text = f"3. {results[2][0]} - {results[2][1]} siirtoa"
                result_text_img = self.font.render(text, True, 'BLACK')
                self.screen.blit(result_text_img, (self.screen_width / 2 - result_text_img.get_width() / 2, 425))

            close_button = self.draw_close_button()

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
        """Piirtää varsinaisen pelin ja huolehtii pelinaikaisten tietojen päivityksestä.
        
        """

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

            if self.player_is_alive():
                self.limit_player_vision()

            else:
                pygame.Surface.fill(self.black_screen, ('RED'))

                if is_won:
                    self.print_won()
                    if self.name != "":
                        add_result_to_database(self.name, self.counter)
                        self.name = ""

                else:
                    self.print_lost()

            self.screen.blit(self.black_screen, (0, 0))
            self.print_player_inventory()
            self.print_moves()
            pygame.display.flip()

    def ask_name(self):
        """Piirtää näkymän, jossa kysytään pelaajan nimeä.
        
        Syötetty nimi otetaan talteen self.name muuttujaan.
        
        """

        manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 10)
        textinput = pygame_textinput.TextInputVisualizer(manager=manager, font_object = self.font)

        clock = pygame.time.Clock()

        while True:
            self.screen.fill((227, 227, 227))
            events = pygame.event.get()

            ask_name_text_img = self.font.render('Pelaajan nimi:', True, 'BLACK')
            self.screen.blit(ask_name_text_img, (self.screen_width / 2 - 150, self.screen_height / 2 - 100))

            name_field_background = pygame.Rect(self.screen_width / 2 - 152, self.screen_height / 2 - 52, 304, 104)
            pygame.draw.rect(self.screen, ('BLACK'), name_field_background)

            name_field = pygame.Rect(self.screen_width / 2 - 150, self.screen_height / 2 - 50, 300, 100)
            pygame.draw.rect(self.screen, (130, 130, 130), name_field)

            textinput.update(events)
            self.screen.blit(textinput.surface, (self.screen_width / 2 - 150 + 25, self.screen_height / 2 - 50 + 25))
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.name = str(textinput.value)
                    self.play()

            pygame.display.update()
            clock.tick(30)

    def limit_player_vision(self):
        """Täyttää ruudun mustalla jättäen halkaisijalta kahden ruudun suuruisen aukon pelaajan päälle.
        
        """

        pygame.Surface.fill(self.black_screen, (0, 0, 0))
        pygame.draw.circle(
            self.black_screen,
            ('RED'),
            ((self.player.get_coords()[0] * self.pics[2].get_width() + self.pics[2].get_width() / 2),
            (self.player.get_coords()[1] * self.pics[2].get_height() + self.pics[2].get_height() / 2)),
            self.pics[0].get_width() * 2.5
            )

    def draw_menu_button(self, text, part):
        """ Piirtää aloitusvalikon painikkeet.
        
        Args: 
            text: painikkeeseen tulostuva teksti.
            place: millä näytön korkeus jaetaan, jossa painike piirtyy oikeaan kohtaan.

        Returns:
            Suorakulmion mutoinen painike.
        
        """

        menu_button_background = pygame.Rect(self.screen_width / 2 - 152, self.screen_height / part - 52, 304, 104)
        pygame.draw.rect(self.screen, ('BLACK'), menu_button_background)

        menu_button = pygame.Rect(self.screen_width / 2 - 150, self.screen_height / part - 50, 300, 100)
        pygame.draw.rect(self.screen, (130, 130, 130), menu_button)
        text_img = self.font.render(text, True, 'BLACK')
        self.screen.blit(text_img, (self.screen_width / 2 - text_img.get_width() / 2, self.screen_height / part - text_img.get_height() / 2))

        return menu_button

    def draw_close_button(self):
        """Piirtää painikkeen "<<" tulostuksella.
        
        Returns: 
            Suorakulmion muotoinen painike.

        """

        close_text_img = self.font.render('<<', True, 'BLACK')
        close_button = pygame.Rect(self.screen_width / 2 - close_text_img.get_width() / 2, 680, close_text_img.get_width(), close_text_img.get_height())
        pygame.draw.rect(self.screen, (227, 227, 227), close_button)
        self.screen.blit(close_text_img, (self.screen_width / 2 - close_text_img.get_width() / 2, 680))

        return close_button

    def print_player_inventory(self):
        """Tulostaa näytölle pelaajan suitsukkeiden lukumäärän.
        
        """

        smudges = self.player.count_smudges()
        smudges_text_img = self.font.render('Suitsukkeita: ' + str(smudges), True, 'WHITE')
        self.screen.blit(smudges_text_img, (60, 10))

    def print_moves(self):
        """Piirtää näytölle pelaajan siirtymien määrän.
        
        """

        moves_text_img = self.font.render('Siirtoja: ' + str(self.counter), True, 'WHITE')
        self.screen.blit(moves_text_img, (self.screen_width - 60 - moves_text_img.get_width(), 10)) 

    def print_won(self):
        """Tulostaa voittotekstin.
        
        """

        won_text_img = self.font.render('Voitit pelin ' + str(self.counter) + ' siirrolla!', True, 'WHITE')
        self.screen.blit(won_text_img, (self.screen_width - 60 - won_text_img.get_width(), self.screen_height - 50))

    def print_lost(self):
        """Tulostaa häviötekstin.
        
        """

        lost_text_img = self.font.render('Hävisit pelin!', True, 'WHITE')
        self.screen.blit(lost_text_img, (self.screen_width - 60 - lost_text_img.get_width(), self.screen_height - 50))

    def player_is_alive(self):
        """Kertoo onko pelaaja vielä elossa.

        Returns: 
            True, jos pelaaja vielä löytyy labyrintilta, muussa tapauksessa False.
        
        """

        return self.player.get_coords() is not None
