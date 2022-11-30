import pygame


class GameLoop:
    def __init__(self, gameinterface, clock, renderer, event_queue):
        self.gameinterface = gameinterface
        self.clock = clock
        self.renderer = renderer
        self.event_queue = event_queue

    def start(self):
        while True:
            if self.handle_events() == False:
                break
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.gameinterface.handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.QUIT:
                return False

    def render(self):
        self.renderer.render()
