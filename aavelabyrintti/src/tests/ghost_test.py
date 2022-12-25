import unittest
from services.ghost import Ghost


class TestGhost(unittest.TestCase):
    def setUp(self):

        MAP = [[1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 0, 0, 1],
               [1, 1, 3, 1, 0, 0, 1],
               [1, 1, 1, 1, 0, 0, 1],
               [1, 0, 0, 0, 0, 2, 1],
               [1, 1, 1, 1, 1, 1, 1],]

        self.test_ghost = Ghost(MAP)

    def test_get_right_ghost_coords(self):
        self.assertEqual(self.test_ghost.get_coords(), (2, 2))

    def test_ghost_cant_move_into_wall(self):
        self.test_ghost.move((5, 4))
        self.assertEqual(self.test_ghost.get_coords(), (2, 2))

    def test_ghost_moves_towards_player(self):
        MAP2 = [[1, 1, 1, 1, 1, 1, 1],
                [1, 3, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 2, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],]

        test_ghost = Ghost(MAP2)
        test_ghost.move((1, 3))
        self.assertEqual(test_ghost.get_coords(), (1, 2))

    def test_ghost_cant_move_into_smudges(self):
        MAP2 = [[1, 1, 1, 1, 1, 1, 1],
                [1, 3, 5, 0, 0, 0, 1],
                [1, 5, 5, 0, 0, 0, 1],
                [1, 2, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],]

        test_ghost = Ghost(MAP2)
        test_ghost.move((1, 3))
        self.assertEqual(test_ghost.get_coords(), (1, 1))

    def test_ghost_cant_move_into_finish_tile(self):
        MAP2 = [[1, 1, 1, 1, 1, 1, 1],
                [1, 3, 4, 0, 0, 0, 1],
                [1, 4, 4, 0, 0, 0, 1],
                [1, 2, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],]

        test_ghost = Ghost(MAP2)
        test_ghost.move((1, 3))
        self.assertEqual(test_ghost.get_coords(), (1, 1))

    def test_get_coords_return_none_when_no_ghost_on_the_map(self):
        MAP2 = [[1, 1, 1, 1, 1, 1, 1],
                [1, 0, 4, 0, 0, 0, 1],
                [1, 4, 4, 0, 0, 0, 1],
                [1, 2, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],]
            
        test_ghost = Ghost(MAP2)
        self.assertEqual(test_ghost.get_coords(), None)