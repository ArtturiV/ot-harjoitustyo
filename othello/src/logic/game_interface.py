class GameInterface:
    """Luokka, joka ottaa vastaan käyttäjän klikkuasten koordinaatit,
    välittää tiedon laudalle ja tulkitsee laudan vastauksen.

    Attributes:
        board: Pelilautaa kuvaavan luokan olio.
    """

    def __init__(self, board):
        """Luokan konsruktori

        Args:
            board (board): Pelilautaa kuvaava olio.
        """
        self.board = board

    def handle_click(self, coordinates):
        """Funtkio muuttaa hiiren koordnaatit laudalle ymmärrettävään muotoon,
        välittää koordinaatit laudalle ja palauttaa pelintilan gameloopille.

        Args:
            coordinates (Tuple): Hiiren sijainnin koordinaatit

        Returns:
            int: 0 = peli jatkuu, 1 = vuorossa olevalla pelaajalla ei laillisia siirtoja,
            2 = musta voitti pelin, 3 = valkoinen voitti pelin, 4 = tasapeli.
        """
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
                return self._handle_no_moves()
        return 0

    def _handle_no_moves(self):
        """Hoitaa tilanteen, jossa vuorossa olevalla pelaajalla ei ole siirtoja

        Returns:
            int: 1 = peli jatkuu, 2 = musta voitti, 3 = valkoinen voitti,
            4 = tasapeli
        """
        if self.board.check_end():
            tally = self.board.check_tally()
            if tally[0] > tally[1]:
                return 2
            if tally[1] > tally[0]:
                return 3
            return 4
        return 1
