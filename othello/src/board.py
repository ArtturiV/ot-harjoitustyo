class Board:
    # Laudan tila tallennetaan listaan, jossa 0 on tyhjä ruutu,
    # 1 on musta nappula ja 2 on valkoinen nappula.
    # Pelaajan vuoro tallennetaan boolean muuttujaan, jossa
    # True on mustan vuoro ja False valkoisen.
    def __init__(self):
        self.board_state = [[0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,1,2,0,0,0],
                            [0,0,0,2,1,0,0,0],
                            [0,0,1,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0]]
        self.player = True

    # Funktio käy läpi legal_moves() funktion antamat ruudut ja tarkistaa
    # onko niihin päättyviä laillisia siirtoja.
    # Muuttujat pnum ja onum viittaavat sanoihin player number ja opponent number.
    def legal_check(self, y, x):
        moves = []
        if self.player:
            pnum = 1
            onum = 2
        else:
            pnum = 2
            onum = 1

        temp_y = y - 1
        temp_x = x
        if temp_y > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_y > 0:
                temp_y -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    moves.append((temp_y,temp_x))
                    break
        temp_y = y + 1
        if temp_y < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_y < 7:
                temp_y += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    moves.append((temp_y,temp_x))
                    break
        # Korjattavaa: x suunnan muutokset ja viistoon menemiset!!!
        if temp_y > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_y > 0:
                temp_y -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    moves.append((temp_y,temp_x))
                    break
        if temp_y > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_y > 0:
                temp_y -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    moves.append((temp_y,temp_x))
                    break
        return moves

    # Funktio käy läpi laudan joka ruudun ja löytäessään pelaajan nappulan,
    # antaa sen sijainnin funktiolle legal_check(). Funktio palauttaa listan siirroista.
    def legal_moves(self):
        moves = []
        temp_moves = []
        if self.player:
            pnum = 1
        else:
            pnum = 2
        for i in range(8):
            for j in range(8):
                if self.board_state[i][j] == pnum:
                    temp_moves = self.legal_check(i,j)
                    if len(temp_moves) > 0:
                        moves += temp_moves
                    temp_moves.clear()
        return moves
                        
