import random
import math

class Ghost():
    def __init__(self, map):
        self.map = map

    def get_coords(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 3:
                    return (x, y)

    def distance(self, x, y, x2, y2):
        return math.sqrt(math.pow(x-x2, 2) + math.pow(y-y2, 2))

    def move(self, player_coords):
        pos_now = self.get_coords()
        not_moved = True
        if abs(player_coords[0] - pos_now[0]) <= 2 and abs(player_coords[1] - pos_now[1]) <=2:
            min_distance = None
            new_coords = None
            for y in range(-1,2):
                for x in range(-1,2):
                    if self.map[pos_now[1] + y][pos_now[0] + x] != 1:
                        distance = self.distance(pos_now[0] + x, pos_now[1] + y, player_coords[0], player_coords[1])
                        if min_distance == None or min_distance > distance:
                            new_coords = (pos_now[0] + x, pos_now[1] + y)
                            min_distance = distance
            
            self.map[pos_now[1]][pos_now[0]] = 0
            self.map[new_coords[1]][new_coords[0]] = 3
            not_moved = False

        while not_moved:
            x = random.randrange(-1, 2)
            y = random.randrange(-1, 2)
            if self.map[pos_now[1] + y][pos_now[0] + x] != 1:
                self.map[pos_now[1]][pos_now[0]] = 0
                self.map[pos_now[1] + y][pos_now[0] + x] = 3
                not_moved = False
