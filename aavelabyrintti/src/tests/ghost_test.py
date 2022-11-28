import unittest
from ghost import Ghost

class TestGhost(unittest.TestCase):
    def setUp(self):

        MAP =  [[1, 1, 1, 1, 1, 1, 1],
                [1, 3, 1, 0, 0, 0, 1],
                [1, 1, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 2, 1],
                [1, 1, 1, 1, 1, 1, 1],]

        self.test_ghost = Ghost(MAP)

    def test_get_right_ghost_coords(self):
        self.assertEqual(self.test_ghost.get_coords(), (1, 1))

    def test_ghost_cant_move_into_wall(self):
        self.test_ghost.move((5, 4))
        self.assertEqual(self.test_ghost.get_coords(), (1, 1))

    def test_ghost_moves_towards_player(self):
        MAP2 =  [[1, 1, 1, 1, 1, 1, 1],
                [1, 3, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 2, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],]

        test_ghost = Ghost(MAP2)
        test_ghost.move((1, 3))
        self.assertEqual(test_ghost.get_coords(), (1, 2))