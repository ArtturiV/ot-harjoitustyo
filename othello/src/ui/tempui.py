from board import Board
"""Väliaikainen teksipohjainen ui. Altis virhekomennoille"""


class TempUI:
    def __init__(self):
        self.board = Board()
        while True:
            self.board.show()
            if self.board.player:
                print("Mustan (1) vuoro")
            else:
                print("Valkoisen (2) vuoro")
            self.board.legal_moves()
            print("Lopeta suorittaminen komennolla: x")
            x = input("Anna kordinaatit muodossa y,x:")
            if x[0] == "x" or x[0] == "X":
                break
            if self.board.make_move(int(x[0]), int(x[2])):
                self.board.change_player()
                continue
            print()
            print("Laiton siirto")
