import random
import math
from entities.constants import GHOST, FLOOR, WALL, FINISH, SMUDGE_STICK

CANT_MOVE_HERE = [WALL, FINISH, SMUDGE_STICK]

class Ghost():
    def __init__(self, labyrint):
        self.labyrint = labyrint

    def get_coords(self):
        for y_coord in range(len(self.labyrint)):
            for x_coord in range(len(self.labyrint[y_coord])):
                if self.labyrint[y_coord][x_coord] == GHOST:
                    return (x_coord, y_coord)
        return None

    def distance(self, ghost_x, ghost_y, player_x, player_y):
        return math.sqrt(math.pow(ghost_x-player_x, 2) + math.pow(ghost_y-player_y, 2))

    def move(self, player_coords):
        pos_now = self.get_coords()
        not_moved = True
        if abs(player_coords[0] - pos_now[0]) <= 2 and abs(player_coords[1] - pos_now[1]) <= 2:
            min_distance = None
            new_coords = None
            for y_coord in range(-1, 2):
                for x_coord in range(-1, 2):
                    if self.labyrint[pos_now[1] + y_coord][pos_now[0] + x_coord] != 1:
                        distance = self.distance(
                            pos_now[0] + x_coord,
                            pos_now[1] + y_coord,
                            player_coords[0],
                            player_coords[1])
                        if min_distance is None or min_distance > distance:
                            new_coords = (pos_now[0] + x_coord, pos_now[1] + y_coord)
                            min_distance = distance

            if self.labyrint[new_coords[1]][new_coords[0]] not in CANT_MOVE_HERE:
                self.labyrint[pos_now[1]][pos_now[0]] = FLOOR
                self.labyrint[new_coords[1]][new_coords[0]] = GHOST
                not_moved = False

        while not_moved:
            x_diff = random.randrange(-1, 2)
            y_diff = random.randrange(-1, 2)
            if self.labyrint[pos_now[1] + y_diff][pos_now[0] + x_diff] not in CANT_MOVE_HERE:
                self.labyrint[pos_now[1]][pos_now[0]] = FLOOR
                self.labyrint[pos_now[1] + y_diff][pos_now[0] + x_diff] = GHOST
                not_moved = False
