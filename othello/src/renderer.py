import os
import pygame


class Renderer:
    def __init__(self, display, board):
        pygame.font.init()
        dirname = os.path.dirname(__file__)
        self.display = display
        self.bg_img = pygame.image.load(
            os.path.join(dirname, "assets", "board2.png"))
        self.board = board
        self.font = pygame.font.SysFont(None, 100)
        self.tally_font = pygame.font.SysFont(None, 50)

    def render(self, help_mode):
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
        self._render_tally()
        self._render_help_mode(help_mode)

        pygame.display.update()

    def _render_tally(self):
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
        self.display.blit(black_tally_text, (600, 820))
        self.display.blit(white_tally_text, (730, 820))

    def _render_help_mode(self, help_mode):
        if help_mode:
            button_colour = (21, 209, 90)
            button_text = self.tally_font.render(
                "Aputila: päällä", True, (255, 255, 255))
            button_rect = pygame.Rect(190, 818, 250, 40)
        else:
            button_colour = (222, 9, 9)
            button_text = self.tally_font.render(
                "Aputila: pois", True, (255, 255, 255))
            button_rect = pygame.Rect(190, 818, 220, 40)
        pygame.draw.rect(self.display, button_colour, button_rect)
        self.display.blit(button_text, (200, 820))

    def render_state(self, state):
        if state == 2:
            text = self.font.render("Musta voitti", True, (255, 255, 255))
            text_pos = (215, 360)
            bg_rect = pygame.Rect(195, 350, 420, 100)
        elif state == 3:
            text = self.font.render("Valkoinen voitti", True, (255, 255, 255))
            text_pos = (150, 360)
            bg_rect = pygame.Rect(135, 350, 550, 100)
        elif state == 4:
            text = self.font.render("Tasapeli", True, (255, 255, 255))
            text_pos = (250, 360)
            bg_rect = pygame.Rect(235, 350, 300, 100)
        elif state == 1:
            text = self.font.render("Ei siirtoja", True, (255, 255, 255))
            text_pos = (250, 360)
            bg_rect = pygame.Rect(230, 350, 350, 100)
        pygame.draw.rect(self.display, (120, 110, 110), bg_rect)

        self.display.blit(text, text_pos)
        pygame.display.update()
