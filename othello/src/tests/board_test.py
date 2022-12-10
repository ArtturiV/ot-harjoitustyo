import unittest
from logic.board import Board


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

    def test_change_player_changes_player2(self):
        self.board.change_player()
        self.board.change_player()
        self.assertEqual(self.board.player, True)

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

    def test_set_illegal_squares_return_false(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 9, 1, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 2, 0],
                 [0, 2, 2, 2, 2, 2, 2, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.board.set_state(state), False)

    def test_legal_moves_player1(self):
        moves = {(2, 4): [(4, 4)], (3, 5): [(3, 3)],
                 (4, 2): [(4, 4)], (5, 3): [(3, 3)]}

        self.assertEqual(self.board.legal_moves(), moves)

    def test_legal_moves_player2(self):
        moves = {(2, 3): [(4, 3)], (3, 2): [(3, 4)],
                 (4, 5): [(4, 3)], (5, 4): [(3, 4)]}
        self.board.change_player()

        self.assertEqual(self.board.legal_moves(), moves)

    def test_make_move_legal_move_returns_true(self):
        self.board.legal_moves()
        self.assertEqual(self.board.make_move(2, 4), True)

    def test_make_move_illegal_move_returns_False(self):
        self.board.legal_moves()
        self.assertEqual(self.board.make_move(2, 5), False)

    def test_make_move_legal_move_changes_board_player1(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 1, 2, 2, 2, 1, 0, 0],
                 [0, 1, 2, 0, 2, 1, 0, 0],
                 [0, 1, 2, 2, 2, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board.set_state(state)
        self.board.legal_moves()
        self.board.make_move(4, 3)
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.board.board_state, state)

    def test_make_move_legal_move_changes_board_player2(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 2, 1, 1, 1, 2, 0, 0],
                 [0, 2, 1, 0, 1, 2, 0, 0],
                 [0, 2, 1, 1, 1, 2, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board.set_state(state)
        self.board.change_player()
        self.board.legal_moves()
        self.board.make_move(4, 3)
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.board.board_state, state)

    def test_make_move_illegal_move_doesnt_change_board(self):
        self.board.legal_moves()
        self.board.make_move(6, 4)
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.board.board_state, state)

    def test_legal_check_stays_inside_board(self):
        state = [[2, 0, 0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 0, 2]]
        self.board.set_state(state)
        self.assertEqual(self.board.legal_moves(), {})

    def test_legal_check_player1(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 1, 2, 2, 2, 1, 0, 0],
                 [0, 1, 2, 0, 2, 1, 0, 0],
                 [0, 1, 2, 2, 2, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board.set_state(state)
        moves = [(2, 3), (6, 3), (4, 1), (4, 5),
                 (2, 1), (6, 5), (2, 5), (6, 1)]
        self.assertEqual(self.board.legal_check(4, 3), moves)

    def test_legal_check_player2(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 2, 1, 1, 1, 2, 0, 0],
                 [0, 2, 1, 0, 1, 2, 0, 0],
                 [0, 2, 1, 1, 1, 2, 0, 0],
                 [0, 2, 2, 2, 2, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board.set_state(state)
        self.board.change_player()
        moves = [(2, 3), (6, 3), (4, 1), (4, 5),
                 (2, 1), (6, 5), (2, 5), (6, 1)]
        self.assertEqual(self.board.legal_check(4, 3), moves)

    def test_empty_legal_check_player1(self):
        moves = []
        self.assertEqual(self.board.legal_check(1, 1), moves)

    def test_empty_legal_check_player2(self):
        moves = []
        self.board.change_player()
        self.assertEqual(self.board.legal_check(1, 1), moves)

    def test_check_tally(self):
        self.assertEqual(self.board.check_tally(), (2, 2))

    def test_check_end_returns_false_if_player_has_moves(self):
        self.board.legal_moves()
        self.assertEqual(self.board.check_end(), False)

    def test_check_end_doesnt_change_player_if_player_has_moves(self):
        self.board.legal_moves()
        self.board.check_end()
        self.assertEqual(self.board.player, True)

    def test_check_end_returns_false_if_other_player_has_moves(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0]]
        self.board.set_state(state)
        self.board.legal_moves()
        self.assertEqual(self.board.check_end(), False)

    def test_check_end_changes_player(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0]]
        self.board.set_state(state)
        self.board.legal_moves()
        self.board.check_end()
        self.assertEqual(self.board.player, False)

    def test_check_end_returns_true_if_neither_have_moves(self):
        state = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 2, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board.set_state(state)
        self.board.legal_moves()
        self.assertEqual(self.board.check_end(), True)

    def test_check_tally(self):
        self.assertEqual(self.board.check_tally(), (2, 2))
