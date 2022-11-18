from board import Board

lauta = Board()
lauta.show()
print(lauta.legal_moves())
lauta.change_player()
print(lauta.legal_moves())
