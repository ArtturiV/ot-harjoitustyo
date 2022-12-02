import pygame
from board import Board
from game_loop import GameLoop
from event_queue import EventQueue
from clock import Clock
from renderer import Renderer
from game_interface import GameInterface


def main():
    board = Board()
    display = pygame.display.set_mode((810, 810))
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
