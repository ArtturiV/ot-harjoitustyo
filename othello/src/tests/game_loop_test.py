import unittest
import pygame
from game_loop import GameLoop


class StubEventQueue:
    def __init__(self, event_type) -> None:
        self.event_type = event_type
    def get(self):
        event = StubEvent(self.event_type)
        return [event]

class StubEvent:
    def __init__(self, event_type):
        if event_type:
            self.type = pygame.MOUSEBUTTONUP
        else:
            self.type = pygame.QUIT

class StubGameInterface:
    def __init__(self, state):
        self.state = state

    def handle_click(self, coordinates):
        return self.state

class StubRenderer:
    def render(self, help_mode):
        pass
    def render_state(self, state):
        pass

class StubClock:
    def tick(self, fps):
        pass
    def get_ticks(self):
        return 0


class TestGameInterface(unittest.TestCase):
    def setUp(self):
        pygame.init()
    
    def test_loop(self):
        game_loop = GameLoop(StubGameInterface(3),StubClock(),StubRenderer(),StubEventQueue(True))
        game_loop.start()
        self.assertEqual(game_loop.game_state, 3)

    def test_quit_game(self):
        game_loop = GameLoop(StubGameInterface(3),StubClock(),StubRenderer(),StubEventQueue(False))
        game_loop.start()
        self.assertEqual(game_loop.game_state, 0)