from entities.constants import *

class Player():
    def __init__(self, map):
        self.map = map
        self.inventory = []

    def get_coords(self):
        for y_coord in range(len(self.map)):
            for x_coord in range(len(self.map[y_coord])):
                if self.map[y_coord][x_coord] == PLAYER:
                    return (x_coord, y_coord)
        return None

    def move(self, x_diff, y_diff):
        pos_now = self.get_coords()

        if self.map[pos_now[1] + y_diff][pos_now[0] + x_diff] == FLOOR:
            self.map[pos_now[1]][pos_now[0]] = FLOOR
            self.map[pos_now[1] + y_diff][pos_now[0] + x_diff] = PLAYER

        if self.map[pos_now[1] + y_diff][pos_now[0] + x_diff] == FINISH:
            self.map[pos_now[1]][pos_now[0]] = FLOOR
