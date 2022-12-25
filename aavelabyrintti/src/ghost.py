import random
import math
from entities.constants import GHOST, FLOOR, WALL, FINISH, SMUDGE_STICK

CANT_MOVE_HERE = [WALL, FINISH, SMUDGE_STICK]

class Ghost():
    """Aaveen toiminnoista vastaava luokka."""

    def __init__(self, labyrinth):
        """Luokan konstruktori.
        
        Args:
            labyrinth = Labyrintti matriisi, jossa aave liikkuu.
            
        """

        self.labyrinth = labyrinth

    def get_coords(self):
        """Palauttaa aaveen sijainnin labyrintissa."""
        for y_coord in range(len(self.labyrinth)):
            for x_coord in range(len(self.labyrinth[y_coord])):
                if self.labyrinth[y_coord][x_coord] == GHOST:
                    return (x_coord, y_coord)
        return None

    def distance(self, ghost_x, ghost_y, player_x, player_y):
        """Laskee aaveen ja pelaajan välisen etäisyyden."""
        return math.sqrt(math.pow(ghost_x-player_x, 2) + math.pow(ghost_y-player_y, 2))

    def move(self, player_coords):
        """Liikuttaa aavetta labyrintissa."""
        pos_now = self.get_coords()
        not_moved = True
        if abs(player_coords[0] - pos_now[0]) <= 2 and abs(player_coords[1] - pos_now[1]) <= 2:
            min_distance = None
            new_coords = None
            for y_coord in range(-1, 2):
                for x_coord in range(-1, 2):
                    if self.labyrinth[pos_now[1] + y_coord][pos_now[0] + x_coord] != 1:
                        distance = self.distance(
                            pos_now[0] + x_coord,
                            pos_now[1] + y_coord,
                            player_coords[0],
                            player_coords[1])
                        if min_distance is None or min_distance > distance:
                            new_coords = (pos_now[0] + x_coord, pos_now[1] + y_coord)
                            min_distance = distance

            if self.labyrinth[new_coords[1]][new_coords[0]] not in CANT_MOVE_HERE:
                self.labyrinth[pos_now[1]][pos_now[0]] = FLOOR
                self.labyrinth[new_coords[1]][new_coords[0]] = GHOST
                not_moved = False

        while not_moved:
            x_diff = random.randrange(-1, 2)
            y_diff = random.randrange(-1, 2)
            if self.labyrinth[pos_now[1] + y_diff][pos_now[0] + x_diff] not in CANT_MOVE_HERE:
                self.labyrinth[pos_now[1]][pos_now[0]] = FLOOR
                self.labyrinth[pos_now[1] + y_diff][pos_now[0] + x_diff] = GHOST
                not_moved = False
