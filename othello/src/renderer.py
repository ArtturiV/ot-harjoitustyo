import os
import pygame


class Renderer:
    def __init__(self, display, board):
        dirname = os.path.dirname(__file__)
        self.display = display
        self.bg_img = pygame.image.load(
            os.path.join(dirname, "assets", "board.png"))
        self.board = board

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
