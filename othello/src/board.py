class Board:

    def __init__(self):
        self.board_state = [[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 2, 0, 0, 0],
                            [0, 0, 0, 2, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]
        self.player = True
        self.legal_list = {}
        self.player_number = 1
        self.opponent_number = 2

        self.legal_moves()

    def change_player(self):
        self.player = not self.player
        if self.player:
            self.player_number = 1
            self.opponent_number = 2
        else:
            self.player_number = 2
            self.opponent_number = 1

    def set_state(self, state):
        if len(state) == 8 and len(state[0]) == 8:
            for i in range(len(state)):
                if not all(square in [0, 1, 2] for square in state[i]):
                    return False
            self.board_state = state
            self.legal_moves()
            return True
        return False

    def check_end(self):
        if len(self.legal_list) == 0:
            self.change_player()
            if len(self.legal_moves()) == 0:
                return True
        return False

    def check_tally(self):
        black_tally = 0
        white_tally = 0

        for i in range(8):
            for j in range(8):
                if self.board_state[i][j] == 1:
                    black_tally += 1
                elif self.board_state[i][j] == 2:
                    white_tally += 1
        return (black_tally, white_tally)

    def make_move(self, y_square, x_square):
        if (y_square, x_square) in self.legal_list:
            self.alter_board(y_square, x_square)
            return True
        return False

    def alter_board(self, y_square, x_square):
        for move in self.legal_list[(y_square, x_square)]:
            self.fill(y_square, x_square, move)

    def fill(self, y_square, x_square, move):
        dist = max(abs(y_square-move[0]), abs(x_square-move[1]))
        if y_square == move[0]:
            y_step = 0
        else:
            y_step = (move[0]-y_square)//abs((move[0]-y_square))
        if x_square == move[1]:
            x_step = 0
        else:
            x_step = (move[1]-x_square)//abs((move[1]-x_square))
        for i in range(dist+1):
            self.board_state[y_square +
                             (i*y_step)][x_square+(i*x_step)] = self.player_number

    def legal_moves(self):
        moves = {}
        temp_moves = []
        for i in range(8):
            for j in range(8):
                if self.board_state[i][j] == 0:
                    temp_moves = self.legal_check(i, j)
                    if len(temp_moves) > 0:
                        moves[(i, j)] = temp_moves.copy()
                    temp_moves.clear()
        self.legal_list = moves
        return moves

    def check_directions(self, y_square, x_square, direction):
        y_direction = direction[0]
        x_direction = direction[1]

        temp_y = y_square + y_direction
        temp_x = x_square + x_direction

        if -1 < temp_y < 8 and -1 < temp_x < 8 and self.board_state[temp_y][temp_x] == self.opponent_number:
            while -1 < temp_y < 8 and -1 < temp_x < 8:
                if self.board_state[temp_y][temp_x] == self.player_number:
                    return (temp_y, temp_x)
                if self.board_state[temp_y][temp_x] == 0:
                    break
                temp_y += y_direction
                temp_x += x_direction
        return False

    def legal_check(self, y_square, x_square):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (1, 1), (-1, 1), (1, -1)]

        for direction in directions:
            temp = self.check_directions(y_square, x_square, direction)
            if temp is not False:
                moves.append(temp)

        return moves
