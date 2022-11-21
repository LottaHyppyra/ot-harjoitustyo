from map import Map

class Player():
    def __init__(self, map: Map):
        self.map = map
        self.inventory = []

    def get_coords(self):
        for y in range(len(self.map.map)):
            for x in range(len(self.map.map[y])):
                if self.map.map[y][x] == 2:
                    return (x, y)       

    def move(self, x, y):
        pos_now = self.get_coords()

        if self.map.map[pos_now[1] + y][pos_now[0] + x] != 1:
            self.map.map[pos_now[1]][pos_now[0]] = 0
            self.map.map[pos_now[1] + y][pos_now[0] + x] = 2
