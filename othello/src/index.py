import pygame
from logic.board import Board
from logic.game_interface import GameInterface
from game_loop import GameLoop
from ui.event_queue import EventQueue
from ui.clock import Clock
from ui.renderer import Renderer


def main():
    """Alustaa oliot ja käynnistää pelin.
    """
    board = Board()
    display = pygame.display.set_mode((810, 870))
    pygame.display.set_caption("Othello")
    event_queue = EventQueue()
    renderer = Renderer(display, board)
    clock = Clock()
    gameinterface = GameInterface(board)
    gameloop = GameLoop(gameinterface, clock, renderer, event_queue)

    pygame.init()
    gameloop.start()


if __name__ == "__main__":
    main()
