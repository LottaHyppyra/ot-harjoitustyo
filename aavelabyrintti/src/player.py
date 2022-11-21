class Player():
    def __init__(self, map):
        self.map = map
        self.inventory = []

    def get_coords(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 2:
                    return (x, y)
        return None 

    def move(self, x, y):
        pos_now = self.get_coords()

        if self.map[pos_now[1] + y][pos_now[0] + x] != 1 and self.map[pos_now[1] + y][pos_now[0] + x] != 3:
            self.map[pos_now[1]][pos_now[0]] = 0
            self.map[pos_now[1] + y][pos_now[0] + x] = 2
