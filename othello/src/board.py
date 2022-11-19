class Board:
    """Laudan tila tallennetaan listaan, jossa 0 on tyhjä ruutu,
    1 on musta nappula ja 2 on valkoinen nappula.
    Pelaajan vuoro tallennetaan boolean muuttujaan, jossa
    True on mustan vuoro ja False valkoisen."""
    def __init__(self):
        self.board_state = [[0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,1,2,0,0,0],
                            [0,0,0,2,1,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0]]
        self.player = True
        self.legal_list = {}

    def change_player(self):
        self.player = not self.player

    def set_state(self, state):
        if len(state) == 8 and len(state[0]) == 8:
            self.board_state = state
            return True
        return False
    
    """Funktio ottaa vastaan ruudun ja tarkistaa onko ruutu laillinen siirto.
    Jos siirto on laillinen, muuttaa se laudan tilaa ja palauttaa True.
    Jos siirto on laiton, palauttaa funktio False eikä muuta lautaa."""
    def make_move(self,y,x):
        if (y,x) in self.legal_list:
            self.alter_board(y,x)
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

        
    def alter_board(self,y,x):
        for move in self.legal_list[(y,x)]:
            self.fill(y,x,move)

    def fill(self,y,x,move):
        if self.player:
            pnum = 1
        else:
            pnum = 2
        dist = max(abs(y-move[0]),abs(x-move[1]))
        if y == move[0]:
            y_step = 0
        else:
            y_step = (move[0]-y)//abs((move[0]-y))
        if x == move[1]:
            x_step = 0
        else:
            x_step = (move[1]-x)//abs((move[1]-x))
        for i in range(dist+1):
            self.board_state[y+(i*y_step)][x+(i*x_step)] = pnum
            
                

    """Funktio käy läpi laudan ruudut. Jokaisen löytämämsä tyhjän ruudun kohdalla
    funktio antaa ruudun legal_check() funktiolle tarkistettavaksi"""
    def legal_moves(self):
        moves = {}
        temp_moves = []
        if self.player:
            pnum = 1
        else:
            pnum = 2
        for i in range(8):
            for j in range(8):
                if self.board_state[i][j] == 0:
                    temp_moves = self.legal_check(i,j)
                    if len(temp_moves) > 0:
                        moves[(i,j)] = temp_moves.copy()
                    temp_moves.clear()
        self.legal_list = moves
        return moves


    """Funktio käy läpi legal_moves() funktion antamat ruudut ja tarkistaa
    onko niistä alkavia laillisia siirtoja.
    Muuttujat pnum ja onum viittaavat sanoihin player number ja opponent number."""
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
                    moves.append((temp_y,temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y + 1
        if temp_y < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_y < 7:
                temp_y += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y,temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y
        temp_x = x - 1
        if temp_x > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_x > 0:
                temp_x -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y,temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_x = x + 1
        if temp_x < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_x < 7:
                temp_x += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y,temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y - 1
        temp_x = x - 1
        if temp_y > 0 and temp_x > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_y > 0 and temp_x > 0:
                temp_y -= 1
                temp_x -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y,temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y + 1
        temp_x = x + 1
        if temp_y < 7 and temp_x < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_y < 7 and temp_x < 7:
                temp_y += 1
                temp_x += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y,temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y - 1
        temp_x = x + 1
        if temp_y > 0 and temp_x < 7 and self.board_state[temp_y][temp_x] == onum:
            while temp_y > 0 and temp_x < 7:
                temp_y -= 1
                temp_x += 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y,temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break
        temp_y = y + 1
        temp_x = x - 1
        if temp_y < 7 and temp_x > 0 and self.board_state[temp_y][temp_x] == onum:
            while temp_y < 7 and temp_x > 0:
                temp_y += 1
                temp_x -= 1
                if self.board_state[temp_y][temp_x] == pnum:
                    moves.append((temp_y,temp_x))
                    break
                if self.board_state[temp_y][temp_x] == 0:
                    break

        return moves
                        
