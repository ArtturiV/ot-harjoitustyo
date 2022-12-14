import os
import pygame


class Renderer:
    """Pelin renderöimisestä vastaava luokka.
    """

    def __init__(self, display, board):
        """Luokan kostruktori tallentaa muuttujiin renderöitävät
        fontit sekä laudan kuvan.

        Args:
            display (display): Ruutu, jolle kuva renderöidään
            board (olio): Pelilautaa kuvaavan luokan olio
        """
        pygame.font.init()
        dirname = os.path.dirname(__file__)
        self.display = display
        self.bg_img = pygame.image.load(
            os.path.join(dirname, "..", "assets", "board2.png"))
        font_path = os.path.join(
            dirname, "..", "assets", "font", "RobotoCondensed-Regular.ttf")
        self.board = board
        self.font = pygame.font.Font(font_path, 90)
        self.tally_font = pygame.font.Font(font_path, 40)

    def render(self, help_mode):
        """Metodi renderöi pelin näkymän. Renderöiminen on jaettu pelilaudasta,
        pelaajien nappuloiden määristä sekä pelin aputilan napista vastaaviin
        metodeihin. Metodi kutsuu ensin kaikkia näitä metodeita ja lopuksi päivittää
        ruudun.

        Args:
            help_mode (Boolean): Kertoo onko pelin aputila päällä.
        """
        self._render_board(help_mode)
        self._render_tally()
        self._render_help_mode(help_mode)

        pygame.display.update()

    def _render_board(self, help_mode):
        """Metodi renderöi laudan tilan. Ensin ruudulle lisätään laudan kuva, joka
        on valmiina kuvana tiedostoissa. Tämän jälkeen metodi käy läpi laudan joka
        ruudun ja piirtää ympyrän mikäli siinä on pelinappula. Jos aputila on päällä
        piirretään myös laillisten siirtojen ruutuihin siniset ympyrät.

        Args:
            help_mode (Boolean): Kertoo onko pelin aputila päällä.
        """

        self.display.blit(self.bg_img, (0, 0))
        for i in range(8):
            for j in range(8):
                if self.board.board_state[i][j] == 1:
                    pygame.draw.circle(self.display, (0, 0, 0),
                                       (55+(100*i), 55+(100*j)), 40)
                elif self.board.board_state[i][j] == 2:
                    pygame.draw.circle(
                        self.display, (255, 255, 255), (55+(100*i), 55+(100*j)), 40)
                elif (i, j) in self.board.legal_list and help_mode:
                    pygame.draw.circle(
                        self.display, (3, 177, 252), (55+(100*i), 55+(100*j)), 40)

    def _render_tally(self):
        """Metodi piirtää pelaajien nappuloiden määrät ruudun alapalkkiin.
        Lisäksi metodi piirtää vuorossa olevan pelaajan nappulan alapalkkiin.
        """
        if self.board.player:
            turn_colour = (0, 0, 0)
        else:
            turn_colour = (255, 255, 255)
        pygame.draw.circle(
            self.display, turn_colour, (30, 840), 20)
        pygame.draw.circle(
            self.display, (0, 0, 0), (570, 840), 20)
        pygame.draw.circle(
            self.display, (255, 255, 255), (700, 840), 20)
        black_tally = "= " + str(self.board.tally[0])
        white_tally = "= " + str(self.board.tally[1])
        black_tally_text = self.tally_font.render(
            black_tally, True, (255, 255, 255))
        white_tally_text = self.tally_font.render(
            white_tally, True, (255, 255, 255))
        self.display.blit(black_tally_text, (600, 815))
        self.display.blit(white_tally_text, (730, 815))

    def _render_help_mode(self, help_mode):
        """Metodi renderöi pelin aputilan napin.

        Args:
            help_mode (Boolean): Kertoo onko pelin aputila päällä
        """
        if help_mode:
            button_colour = (21, 209, 90)
            button_text = self.tally_font.render(
                "Aputila: päällä", True, (255, 255, 255))
            button_rect = pygame.Rect(190, 818, 245, 45)
        else:
            button_colour = (222, 9, 9)
            button_text = self.tally_font.render(
                "Aputila: pois", True, (255, 255, 255))
            button_rect = pygame.Rect(190, 818, 220, 45)
        pygame.draw.rect(self.display, button_colour, button_rect)
        self.display.blit(button_text, (200, 815))

    def render_state(self, state):
        """Metodi renderöi pelin tilaa vastaavan tekstilaatikon.

        Args:
            state (int): Pelin tilaa kuvaava muuttuja:
            1 = Ei siirtoja
            2 = Musta voitti
            3 = Valkoinen voitti
            4 = Tasapeli
        """
        if state == 2:
            text = self.font.render("Musta voitti", True, (255, 255, 255))
            text_pos = (215, 355)
            bg_rect = pygame.Rect(205, 360, 440, 100)
        elif state == 3:
            text = self.font.render("Valkoinen voitti", True, (255, 255, 255))
            text_pos = (150, 355)
            bg_rect = pygame.Rect(140, 360, 560, 100)
        elif state == 4:
            text = self.font.render("Tasapeli", True, (255, 255, 255))
            text_pos = (250, 355)
            bg_rect = pygame.Rect(245, 360, 310, 100)
        elif state == 1:
            text = self.font.render("Ei siirtoja", True, (255, 255, 255))
            text_pos = (250, 355)
            bg_rect = pygame.Rect(240, 360, 350, 100)
        pygame.draw.rect(self.display, (120, 110, 110), bg_rect)

        self.display.blit(text, text_pos)
        pygame.display.update()
