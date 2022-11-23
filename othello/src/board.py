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

    def change_player(self):
        self.player = not self.player

    def set_state(self, state):
        if len(state) == 8 and len(state[0]) == 8:
            self.board_state = state
            return True
        return False

    def make_move(self, y_square, x_square):
        if (y_square, x_square) in self.legal_list:
            self.alter_board(y_square, x_square)
            return True
        return False

    def show(self):
        print()
        i = 0
        print("   0  1  2  3  4  5  6  7")
        for row in self.board_state:
            print(i, row)
            i += 1
        print()

    def alter_board(self, y_square, x_square):
        for move in self.legal_list[(y_square, x_square)]:
            self.fill(y_square, x_square, move)

    def fill(self, y_square, x_square, move):
        if self.player:
            pnum = 1
        else:
            pnum = 2
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
            self.board_state[y_square+(i*y_step)][x_square+(i*x_step)] = pnum

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

    def legal_check(self, y_square, x_square):
        moves = []
        if self.player:
            pnum = 1
            onum = 2
        else:
            pnum = 2
            onum = 1

        temp_y = y_square - 1
        temp_x = x_square
        if temp_y > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_y > 0:
                temp_y -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y, temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y_square + 1
        if temp_y < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_y < 7:
                temp_y += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y, temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y_square
        temp_x = x_square - 1
        if temp_x > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_x > 0:
                temp_x -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y, temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_x = x_square + 1
        if temp_x < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_x < 7:
                temp_x += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y, temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y_square - 1
        temp_x = x_square - 1
        if temp_y > 0 and temp_x > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_y > 0 and temp_x > 0:
                temp_y -= 1
                temp_x -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y, temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y_square + 1
        temp_x = x_square + 1
        if temp_y < 7 and temp_x < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_y < 7 and temp_x < 7:
                temp_y += 1
                temp_x += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y, temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y_square - 1
        temp_x = x_square + 1
        if temp_y > 0 and temp_x < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_y > 0 and temp_x < 7:
                temp_y -= 1
                temp_x += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y, temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y_square + 1
        temp_x = x_square - 1
        if temp_y < 7 and temp_x > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_y < 7 and temp_x > 0:
                temp_y += 1
                temp_x -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y, temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break

        return moves
