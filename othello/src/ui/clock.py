import pygame


class Clock:
    """Pelin kello
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Säätää pelin frameraten

        Args:
            fps (int): Rajoittaa kutsujen määrää
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """Palauttaa ajan konstruktorin kutsusta.
        Käytetään ajastamaan pelin tekstilaatikot.

        Returns:
            int: Aika konstruktorin kutsusta
        """
        return pygame.time.get_ticks()
