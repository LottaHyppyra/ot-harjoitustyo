import unittest
from services.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):

        MAP = [[1, 1, 1, 1, 1, 1, 1],
               [1, 2, 0, 0, 0, 0, 1],
               [1, 5, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1],]

        self.test_player = Player(MAP)

    def test_get_right_player_coords(self):
        self.assertEqual(self.test_player.get_coords(), (1, 1))

    def test_player_can_move_on_floor(self):
        self.test_player.move(1, 1)
        self.assertEqual(self.test_player.get_coords(), (2, 2))

    def test_player_cant_move_into_wall(self):
        self.test_player.move(-1, -1)
        self.assertEqual(self.test_player.get_coords(), (1, 1))

    def test_returns_none_when_no_player_on_the_map(self):

        MAP2 = [[1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],]

        test_player = Player(MAP2)
        self.assertEqual(test_player.get_coords(), None)

    def test_player_has_right_amount_of_smudges_at_the_start(self):
        self.assertEqual(self.test_player.count_smudges(), 1)

    def test_smudge_disappears_from_inventory_when_used(self):
        self.test_player.use_smudge()
        self.assertEqual(self.test_player.count_smudges(), 0)

    def test_collected_smudges_go_into_inventory(self):
        self.test_player.move(0, 1)
        self.assertEqual(self.test_player.count_smudges(), 2)

    def test_inventory_cant_be_negative(self):
        self.test_player.use_smudge()
        self.test_player.use_smudge()
        self.assertEqual(self.test_player.count_smudges(), 0)

    def test_player_gets_out_after_moving_to_finish_tile(self):
        MAP2 = [[1, 1, 1, 1, 1, 1, 1],
                [1, 2, 0, 0, 0, 0, 1],
                [1, 4, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],]

        test_player = Player(MAP2)
        self.assertEqual(test_player.move(0, 1), True)
        self.assertEqual(test_player.get_coords(), None)
