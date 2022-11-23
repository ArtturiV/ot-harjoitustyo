import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_setup(self):
        bstate = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 2, 0, 0, 0],
                  [0, 0, 0, 2, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.board.board_state, bstate)

    def test_initial_player(self):
        self.assertEqual(self.board.player, True)

    def test_change_player_changes_player(self):
        self.board.change_player()
        self.assertEqual(self.board.player, False)

    def test_set_state_sets_board_state(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 2, 0],
                 [0, 2, 2, 2, 2, 2, 2, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]

        self.board.set_state(state)
        self.assertEqual(self.board.board_state, state)

    def test_legal_set_state_returns_true(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 2, 0],
                 [0, 2, 2, 2, 2, 2, 2, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.board.set_state(state), True)

    def test_illegal_set_state_returns_false(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 2, 0],
                 [0, 2, 2, 2, 2, 2, 2, 0]]
        self.assertEqual(self.board.set_state(state), False)
