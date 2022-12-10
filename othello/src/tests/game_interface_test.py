import unittest
from logic.game_interface import GameInterface
from logic.board import Board


class TestGameInterface(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game_interface = GameInterface(self.board)

    def test_legal_coordinates_alter_board(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.game_interface.handle_click((550, 350))
        self.assertEqual(self.board.board_state, state)

    def test_illegal_coordinates_dont_alter_board(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.game_interface.handle_click((0, 0))
        self.assertEqual(self.board.board_state, state)

    def test_black_can_win(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board.set_state(state)
        self.assertEqual(self.game_interface.handle_click((550, 350)), 2)
    
    def test_white_can_win(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board.change_player()
        self.board.set_state(state)
        self.assertEqual(self.game_interface.handle_click((550, 350)), 3)

    def test_no_legal_moves_skips_turn(self):
        state = [[0, 0, 0, 0, 0, 0, 2, 1],
                 [0, 0, 0, 0, 0, 0, 2, 1],
                 [0, 0, 0, 0, 0, 0, 2, 1],
                 [0, 0, 0, 0, 0, 0, 2, 1],
                 [0, 0, 0, 0, 0, 0, 2, 1],
                 [0, 0, 0, 0, 0, 0, 2, 1],
                 [0, 0, 0, 0, 0, 0, 2, 1],
                 [0, 0, 0, 0, 0, 0, 2, 1]]
        self.board.set_state(state)
        self.assertEqual(self.game_interface.handle_click((50, 550)), 1)

    def test_game_can_be_tied(self):
        state = [[2, 0, 0, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 0, 2],
                 [2, 0, 0, 0, 0, 0, 0, 1],
                 [2, 0, 0, 0, 0, 0, 0, 1],
                 [2, 0, 0, 0, 0, 0, 0, 1],
                 [2, 0, 0, 0, 0, 0, 0, 1],
                 [2, 0, 0, 0, 0, 0, 0, 1],
                 [2, 0, 0, 0, 0, 0, 0, 1]]
        self.board.set_state(state)
        self.assertEqual(self.game_interface.handle_click((50, 750)), 4)
    
    def test_coordinates_dont_wrap_around(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board.set_state(state)
        self.assertEqual(self.game_interface.handle_click((805, 805)), 2)
