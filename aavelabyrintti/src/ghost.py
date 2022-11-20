from map import Map
import random

class Ghost():
    def __init__(self, map: Map):
        self.map = map

    def move(self):
        self.map.move_ghost()
