import pygame


class GameLoop:
    def __init__(self, gameinterface, clock, renderer, event_queue):
        self.gameinterface = gameinterface
        self.clock = clock
        self.renderer = renderer
        self.event_queue = event_queue
        self.game_state = 0

    def start(self):
        while True:
            if self.handle_events() is False:
                break
            if self.game_state > 0:
                if self.render_state(self.game_state) is False:
                    break
                if self.game_state > 1:
                    break
                self.game_state = 0
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.game_state = self.gameinterface.handle_click(
                    pygame.mouse.get_pos())
            elif event.type == pygame.QUIT:
                return False
        return True

    def handle_state(self):
        for event in self.event_queue.get():
            if event.type == pygame.MOUSEBUTTONUP:
                return 1
            if event.type == pygame.QUIT:
                return 2
        return 0

    def render(self):
        self.renderer.render()

    def render_state(self, state):
        self.render()
        self.renderer.render_state(state)
        start_time = self.clock.get_ticks()
        current_time = self.clock.get_ticks()
        event = 0
        while current_time - start_time < 3000:
            current_time = self.clock.get_ticks()
            event = self.handle_state()
            if event > 0:
                break
        if event == 2:
            return False
        return True
