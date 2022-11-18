from map import Map

class Player():
    def __init__(self, map: Map):
        self.map = map

    def move(self, x, y):
        self.map.move_player(x, y)
