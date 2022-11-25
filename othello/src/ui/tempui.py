"""Väliaikainen teksipohjainen ui. Altis virhekomennoille"""


class TempUI:
    def __init__(self, board):
        self.board = board

    def start(self):
        while True:
            self.board.show()
            if len(self.board.legal_moves()) == 0:
                if self.board.check_end():
                    tally = self.board.check_tally()
                    if tally[0] > tally[1]:
                        print("Musta voitti!")
                        break
                    elif tally[0] < tally[1]:
                        print("Valkoinen voitti!")
                        break
                    print("Tasapeli!")
                    break
            if self.board.player:
                print("Mustan (1) vuoro")
            else:
                print("Valkoisen (2) vuoro")
            print("Lopeta suorittaminen komennolla: x")
            x = input("Anna kordinaatit muodossa y,x:")
            if x[0] == "x" or x[0] == "X":
                break
            if self.board.make_move(int(x[0]), int(x[2])):
                self.board.change_player()
                continue
            print()
            print("Laiton siirto")
