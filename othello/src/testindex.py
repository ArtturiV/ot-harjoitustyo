import pygame
from board import Board
from game_loop import GameLoop
from event_queue import EventQueue
from clock import Clock
from renderer import Renderer


def main():

    board = Board()
    display = pygame.display.set_mode((810, 810))
    pygame.display.set_caption("Othello")
    event_queue = EventQueue()
    renderer = Renderer(display, board)
    clock = Clock()
    gameloop = GameLoop(board, clock, renderer, event_queue)

    pygame.init()
    gameloop.start()

    if __name__ == "__main__":
        main()
