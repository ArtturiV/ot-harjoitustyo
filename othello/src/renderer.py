import os
import pygame


class Renderer:
    def __init__(self, display, board):
        pygame.font.init()
        dirname = os.path.dirname(__file__)
        self.display = display
        self.bg_img = pygame.image.load(
            os.path.join(dirname, "assets", "board.png"))
        self.board = board
        self.font = pygame.font.SysFont(None, 100)

    def render(self):
        self.display.blit(self.bg_img, (0, 0))
        for i in range(8):
            for j in range(8):
                if self.board.board_state[i][j] == 1:
                    pygame.draw.circle(self.display, (0, 0, 0),
                                       (55+(100*i), 55+(100*j)), 40)
                elif self.board.board_state[i][j] == 2:
                    pygame.draw.circle(
                        self.display, (255, 255, 255), (55+(100*i), 55+(100*j)), 40)
        pygame.display.update()

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
