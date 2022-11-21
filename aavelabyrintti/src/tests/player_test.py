import unittest
from player import Player

MAP =  [[1, 1, 1, 1, 1, 1, 1],
        [1, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],]

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player = Player(MAP)

    def test_get_right_player_coords(self):
        self.assertEqual(self.test_player.get_coords(), (1, 1))

    def test_player_can_move_on_floor(self):
        self.test_player.move(1, 1)
        self.assertEqual(self.test_player.get_coords(), (2, 2))
