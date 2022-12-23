class Board:
    """Luokka, joka hallitsee pelilaudan tilaa.

    Attributes:
        board_state: Laudan alkutila.
        0 kuvaa tyhjää ruutua, 1 mustaa nappulaa ja 2 valkoista nappulaa.
        player: Vuorossa olevaa pelaajaa kuvaava muuttuja.
        True on mustan vuoro ja False valkoisen.
        legal_list: Sanakirja, jossa aivaimina on lailliset siirrot
        ja arvoina lista ruuduista, joihin siirto päättyy.
        player_number: Vuorossa olevan pelaajan nappulan numero.
        opponent_number: Toisen pelaajan nappulan numero.
        tally: Muuttuja, johon tallennetaan kuinka monta nappulaa kullakin pelaajalla on.
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa luokan attribuuttien arvot.
        """
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
        self.tally = (2, 2)

        self.legal_moves()

    def change_player(self):
        """Vaihtaa vuorossa olevaa pelaajaa.
        """
        self.player = not self.player
        if self.player:
            self.player_number = 1
            self.opponent_number = 2
        else:
            self.player_number = 2
            self.opponent_number = 1

    def set_state(self, state):
        """Asettaa laudalle uuden tilan, jos se on laillinen.

        Args:
            state (Lista): Laudan tilaa kuvaava lista

        Returns:
            Boolean: True jos lista kelpaa, False jos lista ei kelpaa
        """
        if len(state) == 8 and len(state[0]) == 8:
            for i in range(len(state)):
                if not all(square in [0, 1, 2] for square in state[i]):
                    return False
            self.board_state = state
            self.legal_moves()
            return True
        return False

    def check_end(self):
        """Tarkistaa onko peli ohi eli onko kummallakaan pelaajalla laillisia siirtoja.
        Vaihtaa pelaajaa, jos vain toisella pelaajalla on siirtoja.

        Returns:
            Boolean: True jos peli on ohi. False jos toisella tai molemmilla pelaajilla on siirtoja.
        """
        if len(self.legal_list) == 0:
            self.change_player()
            if len(self.legal_moves()) == 0:
                return True
        return False

    def check_tally(self):
        """Laskee montako nappulaa pelaajilla on.

        Returns:
            Tuple: Nappuloiden määrät.
        """
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
        """Tarkistaa onko annettu siirto laillinen ja tekee sen.

        Args:
            y_square (int): Siirron y-koordinaatti
            x_square (int): Siirron x-koordinaatti

        Returns:
            Boolean: True jos siirto on laillinen, False jos ei
        """
        if (y_square, x_square) in self.legal_list:
            self._alter_board(y_square, x_square)
            self.tally = self.check_tally()
            return True
        return False

    def _alter_board(self, y_square, x_square):
        """Muuttaa laudan tilaa annetun siirron mukaan

        Args:
            y_square (int): Siirron y-koordinaatti
            x_square (int): Siirron x-koordinaatti
        """
        for move in self.legal_list[(y_square, x_square)]:
            self._fill(y_square, x_square, move)

    def _fill(self, y_square, x_square, move):
        """Muuttaa laudan tilaa lähtöruudusta loppuruutuun.

        Args:
            y_square (int): Siirron y-koordinaatti
            x_square (int): Siirron x-koordinaatti
            move (Tuple): Loppuruudun koordinaatit
        """
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
        """Tarkistaa kaikki laudan lailliset siirrot.

        Returns:
            Sanakirja: Sanakirja laillisista siirroista
        """
        moves = {}
        temp_moves = []
        for i in range(8):
            for j in range(8):
                if self.board_state[i][j] == 0:
                    temp_moves = self._legal_check(i, j)
                    if len(temp_moves) > 0:
                        moves[(i, j)] = temp_moves.copy()
                    temp_moves.clear()
        self.legal_list = moves
        return moves

    def _check_directions(self, y_square, x_square, direction):
        """Tarkistaa onko annetusta ruudusta annettuun suuntaan laillinen siirto

        Args:
            y_square (int): Ruudun y-koordinaatti
            x_square (int): Ruudun x-koordinaatti
            direction (Tuple): Suunta johon funktio tarkistaa

        Returns:
            Tuple/Boolean: Jos siirto on laillinen palauttaa funktio loppuruudun, muuten False
        """
        y_direction = direction[0]
        x_direction = direction[1]

        temp_y = y_square + y_direction
        temp_x = x_square + x_direction

        if 7 < temp_y or temp_y < 0 or 7 < temp_x or temp_x < 0:
            return False

        if self.board_state[temp_y][temp_x] == self.opponent_number:
            while -1 < temp_y < 8 and -1 < temp_x < 8:
                if self.board_state[temp_y][temp_x] == self.player_number:
                    return (temp_y, temp_x)
                if self.board_state[temp_y][temp_x] == 0:
                    break
                temp_y += y_direction
                temp_x += x_direction
        return False

    def _legal_check(self, y_square, x_square):
        """Tarkistaa lähteekö annetusta ruudusta laillisia siirtoja eri suuntiin

        Args:
            y_square (int): Ruudun y-koordinaatti
            x_square (int): Ruudun x-koordinaatti

        Returns:
            Lista: Ruudusta lähtevien siirtojen loppuruutujen koordinaatit
        """
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (1, 1), (-1, 1), (1, -1)]

        for direction in directions:
            temp = self._check_directions(y_square, x_square, direction)
            if temp is not False:
                moves.append(temp)

        return moves
