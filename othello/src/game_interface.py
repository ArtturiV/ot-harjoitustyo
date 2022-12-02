

class GameInterface:
    def __init__(self, board):
        self.board = board

    def handle_click(self, coordinates):
        print(coordinates)
        x_coord = ((coordinates[0]-5)//100) % 8
        y_coord = ((coordinates[1]-5)//100) % 8
        if coordinates[0] < 6:
            x_coord = 0
        elif coordinates[0] > 804:
            x_coord = 7

        if coordinates[1] > 804:
            y_coord = 7
        elif coordinates[1] < 6:
            y_coord = 0

        if self.board.make_move(x_coord, y_coord):
            self.board.change_player()
            if len(self.board.legal_moves()) == 0:
                if self.board.check_end():
                    tally = self.board.check_tally()
                    if tally[0] > tally[1]:
                        return 2
                    if tally[1] > tally[0]:
                        return 3
                    return 4
                return 1
        return 0
