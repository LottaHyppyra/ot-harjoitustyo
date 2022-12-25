from entities.constants import FLOOR, PLAYER, FINISH, SMUDGE_STICK

class Player():
    """Pelaajan toiminnoista vastaava luokka."""

    def __init__(self, labyrinth, inventory=1):
        """Luokan konstruktori.

        Args:
            labyrinth: Labyrintti matriisi, jossa pelaaja liikkuu.
            inventory: Kokonaisluku arvo, joka kertoo montako suitsuketta pelaajalla on.

        """

        self.labyrinth = labyrinth
        self.inventory = inventory

    def get_coords(self):
        """Palauttaa pelaajan sijainnin labyrintissa."""
        for y_coord in range(len(self.labyrinth)):
            for x_coord in range(len(self.labyrinth[y_coord])):
                if self.labyrinth[y_coord][x_coord] == PLAYER:
                    return (x_coord, y_coord)
        return None

    def move(self, x_diff, y_diff):
        """Liikuttaa pelaajaa labyrintissa.

        Args:
            x_diff: Muutos vaakatasossa.
            y_diff: Muutos pystysuunnassa.

        """

        pos_now = self.get_coords()

        if self.labyrinth[pos_now[1] + y_diff][pos_now[0] + x_diff] == FINISH:
            self.labyrinth[pos_now[1]][pos_now[0]] = FLOOR
            return True

        if self.labyrinth[pos_now[1] + y_diff][pos_now[0] + x_diff] == FLOOR:
            self.labyrinth[pos_now[1]][pos_now[0]] = FLOOR
            self.labyrinth[pos_now[1] + y_diff][pos_now[0] + x_diff] = PLAYER

        if self.labyrinth[pos_now[1] + y_diff][pos_now[0] + x_diff] == SMUDGE_STICK:
            self.inventory += 1
            self.labyrinth[pos_now[1]][pos_now[0]] = FLOOR
            self.labyrinth[pos_now[1] + y_diff][pos_now[0] + x_diff] = PLAYER

        return False

    def use_smudge(self):
        """Pienentää pelaajan varastoa.

        Returns:
            Palauttaa True/False riippuen onnistuiko suitsukkeen käyttö."""

        if self.inventory == 0:
            return False

        self.inventory -= 1
        return True

    def count_smudges(self):
        """Palauttaa varastossa olevien suitsukkeiden määrän."""
        return self.inventory
