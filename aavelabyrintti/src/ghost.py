import random

class Ghost():
    def __init__(self, map):
        self.map = map

    def get_coords(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 3:
                    return (x, y)

    def move(self):
        pos_now = self.get_coords()
        not_moved = True

        while not_moved:
            x = random.randrange(-1,2)
            y = random.randrange(-1, 2)
            if self.map[pos_now[1] + y][pos_now[0] + x] != 1:
                self.map[pos_now[1]][pos_now[0]] = 0
                self.map[pos_now[1] + y][pos_now[0] + x] = 3
                not_moved = False
